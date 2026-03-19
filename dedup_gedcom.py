#!/usr/bin/env python3
"""Conservative GEDCOM deduplication script.

Parses a GEDCOM 5.5.1 file, identifies duplicate individuals using strict
multi-factor matching, merges them while preserving the richest records,
updates all cross-references, and writes a cleaned GEDCOM file.

Conservative approach: better to leave a potential duplicate unmerged than
to incorrectly merge two different people.
"""

import json
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher


# ---------------------------------------------------------------------------
# GEDCOM parsing
# ---------------------------------------------------------------------------

def parse_gedcom(filepath):
    """Parse GEDCOM into a list of top-level records, each a list of lines."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    records = []  # list of (record_type, record_id, [lines])
    current_lines = []
    current_id = None
    current_type = None

    for line in raw_lines:
        stripped = line.rstrip("\n\r")
        if stripped.startswith("0 "):
            if current_lines:
                records.append((current_type, current_id, current_lines))
            current_lines = [stripped]
            # Parse: "0 @ID@ TYPE" or "0 HEAD" or "0 TRLR"
            m = re.match(r"0 (@\S+@) (\S+)", stripped)
            if m:
                current_id = m.group(1)
                current_type = m.group(2)
            else:
                parts = stripped.split(None, 1)
                current_id = None
                current_type = parts[1] if len(parts) > 1 else ""
        else:
            current_lines.append(stripped)

    if current_lines:
        records.append((current_type, current_id, current_lines))

    return records


def extract_indi_data(lines):
    """Extract structured data from an INDI record's lines."""
    data = {
        "names": [],
        "sex": "",
        "birth_date": "",
        "birth_place": "",
        "death_date": "",
        "death_place": "",
        "famc": [],
        "fams": [],
        "line_count": len(lines),
        "source_count": 0,
    }

    context = None  # track which level-1 tag we're inside
    for line in lines:
        parts = line.split(None, 2)
        if len(parts) < 2:
            continue
        level = parts[0]
        tag = parts[1]
        value = parts[2] if len(parts) > 2 else ""

        if level == "1":
            if tag == "NAME":
                data["names"].append(value)
            elif tag == "SEX":
                data["sex"] = value.strip()
            elif tag == "FAMC":
                ref = value.strip()
                if ref and ref not in data["famc"]:
                    data["famc"].append(ref)
            elif tag == "FAMS":
                ref = value.strip()
                if ref and ref not in data["fams"]:
                    data["fams"].append(ref)
            elif tag == "SOUR":
                data["source_count"] += 1
            context = tag
        elif level == "2":
            if tag == "DATE" and context == "BIRT":
                data["birth_date"] = value.strip()
            elif tag == "PLAC" and context == "BIRT":
                data["birth_place"] = value.strip()
            elif tag == "DATE" and context == "DEAT":
                data["death_date"] = value.strip()
            elif tag == "PLAC" and context == "DEAT":
                data["death_place"] = value.strip()
            elif tag == "SOUR":
                data["source_count"] += 1
            # Don't reset context for level 2
        # level 3+ we ignore for extraction

    return data


def extract_fam_data(lines):
    """Extract structured data from a FAM record's lines."""
    data = {"husb": "", "wife": "", "chil": [], "marr_date": "", "marr_place": ""}
    context = None
    for line in lines:
        parts = line.split(None, 2)
        if len(parts) < 2:
            continue
        level, tag = parts[0], parts[1]
        value = parts[2].strip() if len(parts) > 2 else ""
        if level == "1":
            if tag == "HUSB":
                data["husb"] = value
            elif tag == "WIFE":
                data["wife"] = value
            elif tag == "CHIL":
                if value and value not in data["chil"]:
                    data["chil"].append(value)
            context = tag
        elif level == "2":
            if tag == "DATE" and context == "MARR":
                data["marr_date"] = value
            elif tag == "PLAC" and context == "MARR":
                data["marr_place"] = value
    return data


# ---------------------------------------------------------------------------
# Name normalization and comparison
# ---------------------------------------------------------------------------

SUFFIXES = {"jr", "sr", "jr.", "sr.", "i", "ii", "iii", "iv", "v",
            "1st", "2nd", "3rd", "4th"}

def parse_gedcom_name(name_str):
    """Parse 'Given /Surname/ Suffix' into (given, surname, suffix)."""
    m = re.match(r"^(.*?)\s*/([^/]*)/\s*(.*?)$", name_str)
    if m:
        given = m.group(1).strip()
        surname = m.group(2).strip()
        suffix = m.group(3).strip()
    else:
        given = name_str.strip()
        surname = ""
        suffix = ""
    return given, surname, suffix


def normalize_name(name_str):
    """Return (normalized_given, normalized_surname) for comparison."""
    given, surname, suffix = parse_gedcom_name(name_str)
    # Remove suffix tokens from given if present
    given_tokens = given.lower().split()
    given_tokens = [t for t in given_tokens if t not in SUFFIXES]
    # Remove quoted nicknames for comparison but keep first name
    cleaned = []
    for t in given_tokens:
        t_stripped = t.strip('"').strip("'")
        cleaned.append(t_stripped)
    surname_clean = surname.lower().strip()
    # Handle variant spellings: Faulkner/Faulconer etc.
    return " ".join(cleaned), surname_clean


def extract_first_name(given_normalized):
    """Get the primary first name from a normalized given string."""
    parts = given_normalized.split()
    if not parts:
        return ""
    # Skip nicknames in parentheses
    for p in parts:
        if not p.startswith("(") and not p.startswith('"'):
            return p
    return parts[0]


def given_names_match(given_a, given_b):
    """Check if two given name strings represent the same person.

    Returns (match, confidence) where confidence is 0.0 to 1.0.
    Conservative: different first names = no match.
    """
    if not given_a or not given_b:
        # If one has no given name, can't confirm match
        return False, 0.0

    parts_a = given_a.split()
    parts_b = given_b.split()
    first_a = parts_a[0]
    first_b = parts_b[0]

    # Exact first name match
    if first_a == first_b:
        return True, 1.0

    # One is initial of the other: "r" matches "ronald"
    if len(first_a) == 1 and first_b.startswith(first_a):
        return True, 0.8
    if len(first_b) == 1 and first_a.startswith(first_b):
        return True, 0.8

    # Very close spelling (typos): SequenceMatcher > 0.85
    ratio = SequenceMatcher(None, first_a, first_b).ratio()
    if ratio >= 0.85:
        return True, ratio

    # Check if nickname matches: compare all tokens
    nicknames_a = set(parts_a)
    nicknames_b = set(parts_b)
    if nicknames_a & nicknames_b:
        return True, 0.7

    return False, 0.0


def surnames_match(sn_a, sn_b):
    """Check if surnames match, accounting for spelling variants."""
    if not sn_a or not sn_b:
        return False
    if sn_a == sn_b:
        return True
    # Common genealogy variants
    ratio = SequenceMatcher(None, sn_a, sn_b).ratio()
    return ratio >= 0.80


# ---------------------------------------------------------------------------
# Date parsing and comparison
# ---------------------------------------------------------------------------

MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
}

def parse_date(date_str):
    """Parse a GEDCOM date string into (year, month, day) or partial tuple.

    Returns (year, month, day) with None for unknown components.
    """
    if not date_str:
        return None, None, None

    s = date_str.strip()
    # Remove qualifiers
    for prefix in ["ABT", "BEF", "AFT", "EST", "CAL", "FROM", "TO", "BET", "INT"]:
        if s.upper().startswith(prefix):
            s = s[len(prefix):].strip()
    # Remove "AND ..." for BET...AND
    if " AND " in s.upper():
        s = s[:s.upper().index(" AND ")].strip()

    # Try MM/DD/YYYY
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        return int(m.group(3)), int(m.group(1)), int(m.group(2))

    # Try "DD Mon YYYY"
    m = re.match(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", s)
    if m:
        month = MONTH_MAP.get(m.group(2).lower())
        return int(m.group(3)), month, int(m.group(1))

    # Try "Mon YYYY"
    m = re.match(r"(\w{3})\s+(\d{4})", s)
    if m:
        month = MONTH_MAP.get(m.group(1).lower())
        return int(m.group(2)), month, None

    # Try year only
    m = re.match(r"(\d{4})", s)
    if m:
        return int(m.group(1)), None, None

    # Try year range "YYYY-YYYY" (take first)
    m = re.match(r"(\d{4})\s*-\s*(\d{4})", s)
    if m:
        return int(m.group(1)), None, None

    return None, None, None


def dates_compatible(date_a, date_b):
    """Check if two date strings are compatible. Returns (compatible, confidence)."""
    if not date_a or not date_b:
        return True, 0.0  # No conflict but no confirmation

    ya, ma, da = parse_date(date_a)
    yb, mb, db = parse_date(date_b)

    if ya is None or yb is None:
        return True, 0.0

    # Years must be within 1 of each other
    if abs(ya - yb) > 1:
        return False, 0.0

    if ya == yb:
        if ma and mb:
            if ma == mb:
                if da and db:
                    if da == db:
                        return True, 1.0
                    else:
                        return False, 0.0  # Same year/month, different day
                return True, 0.9
            else:
                return False, 0.0  # Same year, different month
        return True, 0.7  # Same year, months unknown

    # Years differ by 1 (could be calendar confusion, rounding)
    return True, 0.3


def places_compatible(place_a, place_b):
    """Check if two place strings are compatible."""
    if not place_a or not place_b:
        return True, 0.0

    # Normalize: lowercase, strip empty components
    parts_a = [p.strip().lower() for p in place_a.split(",") if p.strip()]
    parts_b = [p.strip().lower() for p in place_b.split(",") if p.strip()]

    if not parts_a or not parts_b:
        return True, 0.0

    set_a = set(parts_a)
    set_b = set(parts_b)
    overlap = set_a & set_b

    if not overlap:
        return False, 0.0

    # How much overlap relative to the smaller set
    confidence = len(overlap) / min(len(set_a), len(set_b))
    return True, confidence


# ---------------------------------------------------------------------------
# Duplicate detection
# ---------------------------------------------------------------------------

def find_duplicates(indi_records, fam_records):
    """Find duplicate individuals using conservative multi-factor matching.

    indi_records: dict of id -> (lines, data)
    fam_records: dict of id -> (lines, data)

    Returns list of (primary_id, [duplicate_ids], reason, confidence)
    """
    # Index by normalized surname
    surname_index = defaultdict(list)
    for indi_id, (lines, data) in indi_records.items():
        for name in data["names"]:
            given, surname = normalize_name(name)
            if surname:
                surname_index[surname].append(indi_id)

    # Build family parent lookup for cross-checking
    fam_parents = {}
    for fam_id, (flines, fdata) in fam_records.items():
        fam_parents[fam_id] = (fdata["husb"], fdata["wife"])

    seen_pairs = set()
    duplicate_groups = []  # list of sets of IDs

    for surname, ids in surname_index.items():
        unique_ids = list(set(ids))
        if len(unique_ids) < 2:
            continue

        for i in range(len(unique_ids)):
            for j in range(i + 1, len(unique_ids)):
                id_a = unique_ids[i]
                id_b = unique_ids[j]
                pair = (min(id_a, id_b), max(id_a, id_b))
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)

                data_a = indi_records[id_a][1]
                data_b = indi_records[id_b][1]

                match, reason, confidence = is_duplicate(
                    id_a, data_a, id_b, data_b, fam_parents
                )
                if match:
                    # Try to merge into existing group
                    merged = False
                    for group in duplicate_groups:
                        if id_a in group["ids"] or id_b in group["ids"]:
                            group["ids"].add(id_a)
                            group["ids"].add(id_b)
                            group["reasons"].append(reason)
                            group["confidence"] = max(group["confidence"], confidence)
                            merged = True
                            break
                    if not merged:
                        duplicate_groups.append({
                            "ids": {id_a, id_b},
                            "reasons": [reason],
                            "confidence": confidence,
                        })

    return duplicate_groups


def is_duplicate(id_a, data_a, id_b, data_b, fam_parents):
    """Determine if two individuals are duplicates. Conservative approach."""
    # Must have same sex (if known for both)
    if data_a["sex"] and data_b["sex"] and data_a["sex"] != data_b["sex"]:
        return False, "", 0.0

    # Compare all name combinations
    best_name_match = False
    best_name_conf = 0.0
    best_names = ("", "")
    for name_a in data_a["names"]:
        given_a, sn_a = normalize_name(name_a)
        for name_b in data_b["names"]:
            given_b, sn_b = normalize_name(name_b)
            if not surnames_match(sn_a, sn_b):
                continue
            match, conf = given_names_match(given_a, given_b)
            if match and conf > best_name_conf:
                best_name_match = True
                best_name_conf = conf
                best_names = (name_a, name_b)

    if not best_name_match:
        return False, "", 0.0

    # Check dates
    birth_compat, birth_conf = dates_compatible(
        data_a["birth_date"], data_b["birth_date"]
    )
    if not birth_compat:
        return False, "", 0.0

    death_compat, death_conf = dates_compatible(
        data_a["death_date"], data_b["death_date"]
    )
    if not death_compat:
        return False, "", 0.0

    # Check places
    bplace_compat, bplace_conf = places_compatible(
        data_a["birth_place"], data_b["birth_place"]
    )
    if not bplace_compat:
        return False, "", 0.0

    dplace_compat, dplace_conf = places_compatible(
        data_a["death_place"], data_b["death_place"]
    )
    if not dplace_compat:
        return False, "", 0.0

    # Check if FAMC references point to families with same parents
    famc_match_conf = 0.0
    if data_a["famc"] and data_b["famc"]:
        for fa in data_a["famc"]:
            for fb in data_b["famc"]:
                if fa == fb:
                    famc_match_conf = 1.0
                    break
                # Check if families have same parents
                pa = fam_parents.get(fa, ("", ""))
                pb = fam_parents.get(fb, ("", ""))
                if pa[0] and pb[0] and pa[0] == pb[0]:
                    famc_match_conf = max(famc_match_conf, 0.8)
                if pa[1] and pb[1] and pa[1] == pb[1]:
                    famc_match_conf = max(famc_match_conf, 0.8)

    # Compute overall confidence
    # Require strong evidence: name match alone is not enough
    factors = []
    factors.append(("name", best_name_conf))
    if birth_conf > 0:
        factors.append(("birth_date", birth_conf))
    if death_conf > 0:
        factors.append(("death_date", death_conf))
    if bplace_conf > 0:
        factors.append(("birth_place", bplace_conf))
    if dplace_conf > 0:
        factors.append(("death_place", dplace_conf))
    if famc_match_conf > 0:
        factors.append(("family", famc_match_conf))

    # Decision logic:
    # If we have date or family confirmation beyond just name, proceed
    has_date_confirm = birth_conf > 0.5 or death_conf > 0.5
    has_family_confirm = famc_match_conf > 0.5
    has_place_confirm = bplace_conf > 0.5 or dplace_conf > 0.5

    # For records with NO dates and NO family links, require very high name match
    # to avoid false positives on common names
    confirming_factors = sum([has_date_confirm, has_family_confirm, has_place_confirm])

    if confirming_factors == 0:
        # Name only: only merge if exact name match AND both have no dates
        # (these are likely stub entries for same person)
        if best_name_conf >= 1.0 and not data_a["birth_date"] and not data_b["birth_date"]:
            # Additional check: at least same FAMC or one has no FAMC
            if not data_a["famc"] or not data_b["famc"] or set(data_a["famc"]) & set(data_b["famc"]):
                pass  # Allow
            else:
                return False, "", 0.0
        else:
            return False, "", 0.0

    overall = sum(c for _, c in factors) / len(factors) if factors else 0.0

    reason_parts = [f"{f}={c:.2f}" for f, c in factors]
    reason = f"Matched: {best_names[0]} <-> {best_names[1]} ({', '.join(reason_parts)})"

    return True, reason, overall


# ---------------------------------------------------------------------------
# Merging
# ---------------------------------------------------------------------------

def choose_primary(ids, indi_records):
    """Choose the primary record: the one with the most data."""
    best_id = None
    best_score = -1
    for indi_id in ids:
        lines, data = indi_records[indi_id]
        score = data["line_count"] + data["source_count"] * 5
        if data["birth_date"]:
            score += 10
        if data["death_date"]:
            score += 10
        if data["birth_place"]:
            score += 5
        if score > best_score:
            best_score = score
            best_id = indi_id
    return best_id


def merge_indi_records(primary_id, dup_ids, indi_records):
    """Merge duplicate records into the primary. Returns merged lines."""
    primary_lines, primary_data = indi_records[primary_id]

    # Collect FAMC/FAMS from all duplicates that primary doesn't have
    all_famc = set(primary_data["famc"])
    all_fams = set(primary_data["fams"])
    for dup_id in dup_ids:
        _, dup_data = indi_records[dup_id]
        all_famc.update(dup_data["famc"])
        all_fams.update(dup_data["fams"])

    # Add missing FAMC/FAMS to primary lines
    existing_famc = set(primary_data["famc"])
    existing_fams = set(primary_data["fams"])
    new_lines = list(primary_lines)

    for famc in all_famc - existing_famc:
        new_lines.append(f"1 FAMC {famc}")
    for fams in all_fams - existing_fams:
        new_lines.append(f"1 FAMS {fams}")

    return new_lines


def update_references(records, id_map):
    """Replace all references to merged-away IDs with primary IDs."""
    updated = []
    for rec_type, rec_id, lines in records:
        new_lines = []
        for line in lines:
            new_line = line
            for old_id, new_id in id_map.items():
                if old_id in new_line:
                    new_line = new_line.replace(old_id, new_id)
            new_lines.append(new_line)
        # Update rec_id if it was remapped
        new_rec_id = id_map.get(rec_id, rec_id) if rec_id else rec_id
        updated.append((rec_type, new_rec_id, new_lines))
    return updated


def dedup_families(records):
    """Remove duplicate FAM records (same HUSB+WIFE after merging).

    Returns (cleaned_records, fam_id_map) where fam_id_map maps removed
    FAM IDs to the kept FAM ID.
    """
    fam_index = {}  # (husb, wife) -> (fam_id, lines)
    fam_id_map = {}
    kept = []

    for rec_type, rec_id, lines in records:
        if rec_type != "FAM":
            kept.append((rec_type, rec_id, lines))
            continue

        fdata = extract_fam_data(lines)
        key = (fdata["husb"], fdata["wife"])

        if key == ("", ""):
            # Can't determine, keep it
            kept.append((rec_type, rec_id, lines))
            continue

        if key in fam_index:
            existing_id, existing_lines, existing_data = fam_index[key]
            # Merge children
            all_chil = set(existing_data["chil"])
            all_chil.update(fdata["chil"])
            # Keep the one with more data
            if len(lines) >= len(existing_lines):
                primary_id_fam = rec_id
                primary_lines = lines
                dup_id_fam = existing_id
            else:
                primary_id_fam = existing_id
                primary_lines = existing_lines
                dup_id_fam = rec_id

            # Add missing CHIL to primary
            existing_chil_in_primary = set()
            for l in primary_lines:
                m = re.match(r"1 CHIL (@\S+@)", l)
                if m:
                    existing_chil_in_primary.add(m.group(1))
            for c in all_chil - existing_chil_in_primary:
                primary_lines.append(f"1 CHIL {c}")

            fam_index[key] = (primary_id_fam, primary_lines, {"chil": list(all_chil)})
            fam_id_map[dup_id_fam] = primary_id_fam
        else:
            fam_index[key] = (rec_id, lines, fdata)

    # Add all kept families
    for key, (fam_id, flines, fdata) in fam_index.items():
        kept.append(("FAM", fam_id, flines))

    return kept, fam_id_map


def remove_dangling_refs(records, valid_indi_ids, valid_fam_ids):
    """Remove references to non-existent records."""
    cleaned = []
    for rec_type, rec_id, lines in records:
        new_lines = []
        for line in lines:
            # Check for FAMC/FAMS references in INDI records
            m_famc = re.match(r"(\d+) FAMC (@\S+@)", line)
            if m_famc and m_famc.group(2) not in valid_fam_ids:
                continue
            m_fams = re.match(r"(\d+) FAMS (@\S+@)", line)
            if m_fams and m_fams.group(2) not in valid_fam_ids:
                continue
            # Check for HUSB/WIFE/CHIL in FAM records
            m_hw = re.match(r"(\d+) (HUSB|WIFE|CHIL) (@\S+@)", line)
            if m_hw and m_hw.group(3) not in valid_indi_ids:
                continue
            new_lines.append(line)
        cleaned.append((rec_type, rec_id, new_lines))
    return cleaned


def write_gedcom(records, filepath):
    """Write records back to a GEDCOM file."""
    with open(filepath, "w", encoding="utf-8") as f:
        for rec_type, rec_id, lines in records:
            for line in lines:
                f.write(line + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    input_path = "/home/user/autoresearch-genealogy/Faulkner.ged"
    output_path = "/home/user/autoresearch-genealogy/Faulkner_cleaned.ged"
    report_json_path = "/home/user/autoresearch-genealogy/merge_report.json"
    report_txt_path = "/home/user/autoresearch-genealogy/merge_report.txt"

    print("Parsing GEDCOM...")
    records = parse_gedcom(input_path)

    # Separate record types
    indi_records = {}
    fam_records = {}
    other_records = []

    for rec_type, rec_id, lines in records:
        if rec_type == "INDI":
            data = extract_indi_data(lines)
            indi_records[rec_id] = (lines, data)
        elif rec_type == "FAM":
            data = extract_fam_data(lines)
            fam_records[rec_id] = (lines, data)
        else:
            other_records.append((rec_type, rec_id, lines))

    total_indi_before = len(indi_records)
    total_fam_before = len(fam_records)
    print(f"Parsed {total_indi_before} individuals, {total_fam_before} families")

    # Find duplicates
    print("Finding duplicates (conservative matching)...")
    dup_groups = find_duplicates(indi_records, fam_records)
    print(f"Found {len(dup_groups)} duplicate groups")

    # Perform merges
    id_map = {}  # old_id -> new_id (primary)
    merge_log = []

    for group in dup_groups:
        ids = {i for i in group["ids"] if i in indi_records}
        if len(ids) < 2:
            continue
        primary_id = choose_primary(ids, indi_records)
        dup_ids = ids - {primary_id}

        # Merge data into primary
        merged_lines = merge_indi_records(primary_id, dup_ids, indi_records)
        indi_records[primary_id] = (merged_lines, indi_records[primary_id][1])

        # Map duplicates to primary
        for dup_id in dup_ids:
            id_map[dup_id] = primary_id

        primary_names = indi_records[primary_id][1]["names"]
        dup_info = []
        for did in dup_ids:
            dup_info.append({
                "id": did,
                "names": indi_records[did][1]["names"],
            })

        merge_log.append({
            "primary_id": primary_id,
            "primary_names": primary_names,
            "merged_away": dup_info,
            "reasons": group["reasons"],
            "confidence": group["confidence"],
        })

        # Remove duplicates
        for dup_id in dup_ids:
            del indi_records[dup_id]

    total_merged_away = sum(len(m["merged_away"]) for m in merge_log)
    print(f"Merged away {total_merged_away} duplicate individuals")

    # Rebuild records list
    all_records = []
    # Add non-INDI/FAM records that come before INDI (HEAD, SUBM)
    for rec in other_records:
        if rec[0] in ("HEAD", "SUBM"):
            all_records.append(rec)

    # Add INDI records
    for indi_id, (lines, data) in indi_records.items():
        all_records.append(("INDI", indi_id, lines))

    # Add FAM records
    for fam_id, (lines, data) in fam_records.items():
        all_records.append(("FAM", fam_id, lines))

    # Add remaining other records (SOUR, OBJE, NOTE, TRLR)
    for rec in other_records:
        if rec[0] not in ("HEAD", "SUBM"):
            all_records.append(rec)

    # Update all cross-references
    print("Updating cross-references...")
    all_records = update_references(all_records, id_map)

    # Dedup families
    print("Deduplicating families...")
    all_records, fam_id_map = dedup_families(all_records)
    if fam_id_map:
        all_records = update_references(all_records, fam_id_map)
        print(f"Merged {len(fam_id_map)} duplicate families")

    # Collect valid IDs
    valid_indi = set()
    valid_fam = set()
    for rec_type, rec_id, lines in all_records:
        if rec_type == "INDI":
            valid_indi.add(rec_id)
        elif rec_type == "FAM":
            valid_fam.add(rec_id)

    # Remove dangling references
    print("Removing dangling references...")
    all_records = remove_dangling_refs(all_records, valid_indi, valid_fam)

    total_indi_after = sum(1 for r in all_records if r[0] == "INDI")
    total_fam_after = sum(1 for r in all_records if r[0] == "FAM")

    # Write cleaned GEDCOM
    print(f"Writing cleaned GEDCOM: {total_indi_after} individuals, {total_fam_after} families")
    write_gedcom(all_records, output_path)

    # Write reports
    report = {
        "summary": {
            "individuals_before": total_indi_before,
            "individuals_after": total_indi_after,
            "individuals_removed": total_indi_before - total_indi_after,
            "families_before": total_fam_before,
            "families_after": total_fam_after,
            "families_removed": total_fam_before - total_fam_after,
            "merge_groups": len(merge_log),
        },
        "merges": merge_log,
        "family_merges": [{"old": k, "new": v} for k, v in fam_id_map.items()],
    }

    with open(report_json_path, "w") as f:
        json.dump(report, f, indent=2)

    with open(report_txt_path, "w") as f:
        f.write("GEDCOM Deduplication Report\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Input:  {input_path}\n")
        f.write(f"Output: {output_path}\n\n")
        f.write(f"Individuals: {total_indi_before} -> {total_indi_after} "
                f"({total_indi_before - total_indi_after} removed)\n")
        f.write(f"Families:    {total_fam_before} -> {total_fam_after} "
                f"({total_fam_before - total_fam_after} removed)\n")
        f.write(f"Merge groups: {len(merge_log)}\n\n")
        f.write("-" * 60 + "\n")
        f.write("MERGE DETAILS\n")
        f.write("-" * 60 + "\n\n")
        for i, m in enumerate(merge_log, 1):
            f.write(f"Group {i}: Kept {m['primary_id']}\n")
            f.write(f"  Primary names: {', '.join(m['primary_names'])}\n")
            for dup in m["merged_away"]:
                f.write(f"  Removed {dup['id']}: {', '.join(dup['names'])}\n")
            for reason in m["reasons"]:
                f.write(f"  Reason: {reason}\n")
            f.write(f"  Confidence: {m['confidence']:.2f}\n\n")

        if fam_id_map:
            f.write("-" * 60 + "\n")
            f.write("FAMILY MERGES\n")
            f.write("-" * 60 + "\n\n")
            for old, new in fam_id_map.items():
                f.write(f"  {old} -> {new}\n")

    print("\nDone!")
    print(f"Reports: {report_json_path}")
    print(f"         {report_txt_path}")


if __name__ == "__main__":
    main()
