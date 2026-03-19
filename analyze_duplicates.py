#!/usr/bin/env python3
"""
Analyze a GEDCOM file for duplicate individuals and families.
Parses INDI and FAM records, then clusters likely duplicates by name/date/place similarity.
"""

import re
import json
import sys
from collections import defaultdict
from datetime import datetime
from difflib import SequenceMatcher

GED_PATH = "/home/user/autoresearch-genealogy/Faulkner.ged"
OUTPUT_PATH = "/home/user/autoresearch-genealogy/duplicate_analysis.json"

# ---------------------------------------------------------------------------
# 1. GEDCOM Parser
# ---------------------------------------------------------------------------

def parse_gedcom(path):
    """Parse GEDCOM into INDI and FAM records."""
    individuals = {}
    families = {}

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_record = None
    current_id = None
    current_tag_stack = []  # track nested tags at each level

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n\r")
        i += 1

        # Parse level, optional xref, tag, optional value
        m = re.match(r"^(\d+)\s+(@[^@]+@)?\s*(\S+)\s*(.*)?$", line)
        if not m:
            continue

        level = int(m.group(1))
        xref = m.group(2)
        tag = m.group(3)
        value = (m.group(4) or "").strip()

        if level == 0:
            # Save previous record
            if current_record and current_id:
                if current_record["_type"] == "INDI":
                    individuals[current_id] = current_record
                elif current_record["_type"] == "FAM":
                    families[current_id] = current_record

            current_record = None
            current_id = None
            current_tag_stack = []

            if xref and tag == "INDI":
                current_id = xref
                current_record = {
                    "_type": "INDI",
                    "id": xref,
                    "names": [],
                    "sex": "",
                    "birt_date": "",
                    "birt_plac": "",
                    "deat_date": "",
                    "deat_plac": "",
                    "famc": [],
                    "fams": [],
                }
                current_tag_stack = [("INDI", None)]
            elif xref and tag == "FAM":
                current_id = xref
                current_record = {
                    "_type": "FAM",
                    "id": xref,
                    "husb": "",
                    "wife": "",
                    "chil": [],
                    "marr_date": "",
                    "marr_plac": "",
                }
                current_tag_stack = [("FAM", None)]
            continue

        if current_record is None:
            continue

        # Trim tag stack to current level
        current_tag_stack = current_tag_stack[:level]

        # Determine parent context
        parent_tag = current_tag_stack[-1][0] if current_tag_stack else None

        if current_record["_type"] == "INDI":
            if level == 1:
                if tag == "NAME":
                    current_record["names"].append(value)
                elif tag == "SEX":
                    current_record["sex"] = value
                elif tag == "FAMC":
                    current_record["famc"].append(value)
                elif tag == "FAMS":
                    current_record["fams"].append(value)
                elif tag in ("BIRT", "DEAT"):
                    pass  # date/plac come at level 2
            elif level == 2:
                if parent_tag == "BIRT":
                    if tag == "DATE":
                        current_record["birt_date"] = value
                    elif tag == "PLAC":
                        current_record["birt_plac"] = value
                elif parent_tag == "DEAT":
                    if tag == "DATE":
                        current_record["deat_date"] = value
                    elif tag == "PLAC":
                        current_record["deat_plac"] = value

        elif current_record["_type"] == "FAM":
            if level == 1:
                if tag == "HUSB":
                    current_record["husb"] = value
                elif tag == "WIFE":
                    current_record["wife"] = value
                elif tag == "CHIL":
                    current_record["chil"].append(value)
                elif tag == "MARR":
                    pass
            elif level == 2:
                if parent_tag == "MARR":
                    if tag == "DATE":
                        current_record["marr_date"] = value
                    elif tag == "PLAC":
                        current_record["marr_plac"] = value

        current_tag_stack.append((tag, value))

    # Save last record
    if current_record and current_id:
        if current_record["_type"] == "INDI":
            individuals[current_id] = current_record
        elif current_record["_type"] == "FAM":
            families[current_id] = current_record

    return individuals, families


# ---------------------------------------------------------------------------
# 2. Name and Date Normalization
# ---------------------------------------------------------------------------

SUFFIXES = re.compile(r"\b(jr|sr|ii|iii|iv|v|2nd|3rd|4th|esq|phd|md)\b", re.IGNORECASE)

def normalize_name(name_str):
    """Normalize a GEDCOM NAME value for comparison.
    GEDCOM names use /Surname/ delimiters.
    Returns (given, surname) tuple, lowercased, suffixes stripped.
    """
    # Extract surname from slashes
    m = re.search(r"/([^/]*)/", name_str)
    surname = m.group(1).strip() if m else ""
    given = re.sub(r"/[^/]*/", "", name_str).strip()

    # Strip suffixes
    given = SUFFIXES.sub("", given).strip()
    surname = SUFFIXES.sub("", surname).strip()

    # Collapse whitespace, lowercase
    given = re.sub(r"\s+", " ", given).lower().strip()
    surname = re.sub(r"\s+", " ", surname).lower().strip()

    return (given, surname)


MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    "january": 1, "february": 2, "march": 3, "april": 4,
    "june": 6, "july": 7, "august": 8, "september": 9,
    "october": 10, "november": 11, "december": 12,
}

def parse_date(date_str):
    """Parse various date formats into (year, month, day) tuple.
    Returns None for components that can't be parsed.
    Handles: 'DD Mon YYYY', 'Mon YYYY', 'YYYY', 'MM/DD/YYYY',
    'ABT YYYY', 'BEF YYYY', 'AFT YYYY', 'BET YYYY AND YYYY', etc.
    """
    if not date_str:
        return (None, None, None)

    s = date_str.strip()
    # Strip GEDCOM date modifiers
    s = re.sub(r"^(ABT|ABOUT|EST|CAL|BEF|BEFORE|AFT|AFTER|BET|FROM|TO|INT)\s+", "", s, flags=re.IGNORECASE)
    # For BET X AND Y, take X
    s = re.sub(r"\s+AND\s+.*$", "", s, flags=re.IGNORECASE)
    s = s.strip()

    # Try MM/DD/YYYY
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", s)
    if m:
        return (int(m.group(3)), int(m.group(1)), int(m.group(2)))

    # Try DD Mon YYYY
    m = re.match(r"^(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})$", s)
    if m:
        mon = MONTH_MAP.get(m.group(2).lower())
        return (int(m.group(3)), mon, int(m.group(1)))

    # Try Mon YYYY
    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", s)
    if m:
        mon = MONTH_MAP.get(m.group(1).lower())
        return (int(m.group(2)), mon, None)

    # Try YYYY only
    m = re.match(r"^(\d{4})$", s)
    if m:
        return (int(m.group(1)), None, None)

    return (None, None, None)


def dates_compatible(d1, d2):
    """Compare two parsed date tuples. Return a similarity score 0..1.
    1.0 = exact match, 0.8 = same year+month but day differs, etc.
    """
    y1, m1, day1 = d1
    y2, m2, day2 = d2

    if y1 is None or y2 is None:
        return 0.0  # can't compare without years

    if y1 != y2:
        if abs(y1 - y2) <= 2:
            return 0.2  # close years, might be transcription error
        return 0.0

    # Same year
    if m1 is None or m2 is None:
        return 0.6  # same year, months unknown

    if m1 != m2:
        # Check for day/month swap (common in US vs European formats)
        if day1 and day2 and m1 == day2 and m2 == day1 and m1 <= 12 and m2 <= 12:
            return 0.8  # likely day/month swap
        return 0.4  # same year, different month

    # Same year and month
    if day1 is None or day2 is None:
        return 0.8

    if day1 == day2:
        return 1.0

    if abs(day1 - day2) <= 3:
        return 0.9  # off by a couple days, likely same person

    return 0.7  # same year+month, different day


def normalize_place(place_str):
    """Normalize a place string for comparison."""
    if not place_str:
        return ""
    # Remove leading commas/spaces (Ancestry sometimes has ", , State, Country")
    p = re.sub(r"^[\s,]+", "", place_str)
    p = re.sub(r"\s+", " ", p).strip().lower()
    return p


def places_similar(p1, p2):
    """Return similarity score 0..1 for two place strings."""
    n1 = normalize_place(p1)
    n2 = normalize_place(p2)

    if not n1 or not n2:
        return 0.0

    if n1 == n2:
        return 1.0

    # Check if one contains the other (e.g., "Cook, Illinois" vs "Chicago, Cook, Illinois, USA")
    parts1 = [x.strip() for x in n1.split(",") if x.strip()]
    parts2 = [x.strip() for x in n2.split(",") if x.strip()]

    # Count overlapping parts
    overlap = len(set(parts1) & set(parts2))
    if overlap == 0:
        return 0.0

    max_parts = max(len(parts1), len(parts2))
    return overlap / max_parts


def name_similarity(names1, names2):
    """Compare two lists of names (each individual can have multiple NAME lines).
    Returns best match score 0..1.
    """
    best = 0.0
    for n1 in names1:
        g1, s1 = normalize_name(n1)
        for n2 in names2:
            g2, s2 = normalize_name(n2)

            if s1 != s2:
                # Different surnames: no match (could add fuzzy but risky)
                continue

            if not s1:
                # Both have empty surname, skip
                continue

            # Same surname; compare given names
            if g1 == g2:
                score = 1.0
            elif not g1 or not g2:
                score = 0.5
            else:
                # Check if one is abbreviation/initial of the other
                g1_parts = g1.split()
                g2_parts = g2.split()

                if g1_parts[0] == g2_parts[0]:
                    # Same first name
                    score = 0.9
                elif len(g1_parts[0]) == 1 and g2_parts[0].startswith(g1_parts[0]):
                    score = 0.7
                elif len(g2_parts[0]) == 1 and g1_parts[0].startswith(g2_parts[0]):
                    score = 0.7
                else:
                    ratio = SequenceMatcher(None, g1, g2).ratio()
                    score = ratio * 0.8  # scale down fuzzy matches

            best = max(best, score)

    return best


# ---------------------------------------------------------------------------
# 3. Duplicate Detection
# ---------------------------------------------------------------------------

def find_duplicate_individuals(individuals):
    """Find clusters of likely duplicate individuals."""
    # Index by normalized surname for efficiency
    by_surname = defaultdict(list)
    for uid, rec in individuals.items():
        seen_surnames = set()
        for n in rec["names"]:
            _, surn = normalize_name(n)
            if surn and surn not in seen_surnames:
                by_surname[surn].append(uid)
                seen_surnames.add(surn)

    # Track pairs already scored
    pair_scores = {}
    candidates = []

    for surn, ids in by_surname.items():
        if len(ids) < 2:
            continue

        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                id_a, id_b = ids[i], ids[j]
                pair_key = tuple(sorted([id_a, id_b]))
                if pair_key in pair_scores:
                    continue

                rec_a = individuals[id_a]
                rec_b = individuals[id_b]

                # Name similarity
                ns = name_similarity(rec_a["names"], rec_b["names"])
                if ns < 0.5:
                    pair_scores[pair_key] = 0
                    continue

                # Sex must match (or be unknown)
                if rec_a["sex"] and rec_b["sex"] and rec_a["sex"] != rec_b["sex"]:
                    pair_scores[pair_key] = 0
                    continue

                # Birth date similarity
                bd_a = parse_date(rec_a["birt_date"])
                bd_b = parse_date(rec_b["birt_date"])
                ds = dates_compatible(bd_a, bd_b)

                # Birth place similarity
                ps = places_similar(rec_a["birt_plac"], rec_b["birt_plac"])

                # Death date similarity
                dd_a = parse_date(rec_a["deat_date"])
                dd_b = parse_date(rec_b["deat_date"])
                dds = dates_compatible(dd_a, dd_b)

                # Death place similarity
                dps = places_similar(rec_a["deat_plac"], rec_b["deat_plac"])

                # Composite score
                # Name is most important, then birth date, then places, then death info
                score = 0.0
                score += ns * 0.35

                if bd_a[0] is not None and bd_b[0] is not None:
                    score += ds * 0.30
                elif bd_a[0] is None and bd_b[0] is None:
                    # Both missing birth dates: slight penalty
                    score += 0.05
                else:
                    # One has date, one doesn't: neutral
                    score += 0.10

                if ps > 0:
                    score += ps * 0.15
                elif rec_a["birt_plac"] and rec_b["birt_plac"]:
                    pass  # both have place but no overlap
                else:
                    score += 0.05  # missing place data

                # Death info is supplementary
                if dd_a[0] is not None and dd_b[0] is not None:
                    score += dds * 0.10
                else:
                    score += 0.02

                if dps > 0:
                    score += dps * 0.10
                else:
                    score += 0.01

                pair_scores[pair_key] = score

                if score >= 0.45:
                    candidates.append((id_a, id_b, score))

    # Cluster duplicates using union-find
    parent = {}

    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for id_a, id_b, score in candidates:
        union(id_a, id_b)

    # Build clusters
    clusters_map = defaultdict(set)
    all_ids_in_candidates = set()
    for id_a, id_b, _ in candidates:
        all_ids_in_candidates.add(id_a)
        all_ids_in_candidates.add(id_b)

    for uid in all_ids_in_candidates:
        clusters_map[find(uid)].add(uid)

    # For each cluster, compute pairwise scores and assign confidence
    clusters = []
    for root, members in clusters_map.items():
        if len(members) < 2:
            continue

        member_list = sorted(members)
        pairwise = []
        for i in range(len(member_list)):
            for j in range(i + 1, len(member_list)):
                pk = tuple(sorted([member_list[i], member_list[j]]))
                sc = pair_scores.get(pk, 0)
                if sc > 0:
                    pairwise.append({"ids": [member_list[i], member_list[j]], "score": round(sc, 3)})

        max_score = max(p["score"] for p in pairwise) if pairwise else 0

        if max_score >= 0.75:
            confidence = "exact_match"
        elif max_score >= 0.55:
            confidence = "likely_match"
        else:
            confidence = "possible_match"

        cluster_info = {
            "cluster_id": len(clusters) + 1,
            "confidence": confidence,
            "max_score": round(max_score, 3),
            "members": [],
            "pairwise_scores": pairwise,
        }

        for uid in member_list:
            rec = individuals[uid]
            cluster_info["members"].append({
                "id": uid,
                "names": rec["names"],
                "sex": rec["sex"],
                "birt_date": rec["birt_date"],
                "birt_plac": rec["birt_plac"],
                "deat_date": rec["deat_date"],
                "deat_plac": rec["deat_plac"],
                "famc": rec["famc"],
                "fams": rec["fams"],
            })

        clusters.append(cluster_info)

    # Sort by confidence (exact first) then by max_score desc
    conf_order = {"exact_match": 0, "likely_match": 1, "possible_match": 2}
    clusters.sort(key=lambda c: (conf_order.get(c["confidence"], 3), -c["max_score"]))

    # Re-number
    for i, c in enumerate(clusters):
        c["cluster_id"] = i + 1

    return clusters


def find_duplicate_families(families, individuals):
    """Find FAM records that reference the same couple."""
    # Index families by (husb, wife) pair after normalizing through individuals
    couple_index = defaultdict(list)

    for fam_id, fam in families.items():
        husb = fam.get("husb", "")
        wife = fam.get("wife", "")
        if husb or wife:
            key = tuple(sorted([husb, wife]))
            couple_index[key].append(fam_id)

    # Direct duplicates: same HUSB + WIFE IDs
    direct_dups = []
    for key, fam_ids in couple_index.items():
        if len(fam_ids) > 1:
            direct_dups.append({
                "type": "same_couple_ids",
                "husb_id": key[0] if key[0] else "",
                "wife_id": key[1] if key[1] else "",
                "family_ids": sorted(fam_ids),
                "details": [],
            })
            for fid in sorted(fam_ids):
                f = families[fid]
                detail = {
                    "family_id": fid,
                    "husb": f["husb"],
                    "wife": f["wife"],
                    "children": f["chil"],
                    "marr_date": f["marr_date"],
                    "marr_plac": f["marr_plac"],
                }
                # Add name info
                if f["husb"] and f["husb"] in individuals:
                    detail["husb_names"] = individuals[f["husb"]]["names"]
                if f["wife"] and f["wife"] in individuals:
                    detail["wife_names"] = individuals[f["wife"]]["names"]
                direct_dups[-1]["details"].append(detail)

    # Also look for families where HUSB or WIFE might be duplicate individuals
    # We'll note this in the output but it requires the individual dup clusters
    return direct_dups


# ---------------------------------------------------------------------------
# 4. Main
# ---------------------------------------------------------------------------

def main():
    print("Parsing GEDCOM file...")
    individuals, families = parse_gedcom(GED_PATH)
    print(f"  Parsed {len(individuals)} INDI records, {len(families)} FAM records")

    print("\nFinding duplicate individuals...")
    indi_clusters = find_duplicate_individuals(individuals)

    # Count by confidence
    conf_counts = defaultdict(int)
    total_dup_ids = set()
    for c in indi_clusters:
        conf_counts[c["confidence"]] += 1
        for m in c["members"]:
            total_dup_ids.add(m["id"])

    print(f"  Found {len(indi_clusters)} duplicate clusters involving {len(total_dup_ids)} records")
    print(f"    Exact match:    {conf_counts.get('exact_match', 0)} clusters")
    print(f"    Likely match:   {conf_counts.get('likely_match', 0)} clusters")
    print(f"    Possible match: {conf_counts.get('possible_match', 0)} clusters")

    # Estimate unique after dedup: total - (duplicates - clusters)
    # Each cluster of N members represents 1 unique person, so we remove N-1
    removed = sum(len(c["members"]) - 1 for c in indi_clusters)
    est_unique = len(individuals) - removed
    print(f"\n  Total individuals:       {len(individuals)}")
    print(f"  Estimated unique after dedup: {est_unique}")
    print(f"  Estimated duplicates to merge: {removed}")

    print("\nFinding duplicate families...")
    fam_dups = find_duplicate_families(families, individuals)
    print(f"  Found {len(fam_dups)} duplicate family groups")

    # Print detailed cluster info
    print("\n" + "=" * 80)
    print("DUPLICATE INDIVIDUAL CLUSTERS")
    print("=" * 80)

    for c in indi_clusters:
        print(f"\n--- Cluster {c['cluster_id']} [{c['confidence']}] (score: {c['max_score']}) ---")
        for m in c["members"]:
            names_str = " | ".join(m["names"]) if m["names"] else "(no name)"
            print(f"  {m['id']}")
            print(f"    Names: {names_str}")
            print(f"    Sex: {m['sex'] or '?'}")
            if m["birt_date"] or m["birt_plac"]:
                print(f"    Birth: {m['birt_date']}  {m['birt_plac']}")
            if m["deat_date"] or m["deat_plac"]:
                print(f"    Death: {m['deat_date']}  {m['deat_plac']}")
            if m["famc"]:
                print(f"    FAMC: {', '.join(m['famc'])}")
            if m["fams"]:
                print(f"    FAMS: {', '.join(m['fams'])}")

    if fam_dups:
        print("\n" + "=" * 80)
        print("DUPLICATE FAMILY RECORDS")
        print("=" * 80)
        for fd in fam_dups:
            print(f"\n  Family IDs: {', '.join(fd['family_ids'])}")
            for d in fd["details"]:
                print(f"    {d['family_id']}:")
                if "husb_names" in d:
                    print(f"      Husband: {d['husb']} {d['husb_names']}")
                if "wife_names" in d:
                    print(f"      Wife:    {d['wife']} {d['wife_names']}")
                print(f"      Children: {len(d['children'])}")
                if d["marr_date"] or d["marr_plac"]:
                    print(f"      Marriage: {d['marr_date']}  {d['marr_plac']}")

    # Build output JSON
    output = {
        "summary": {
            "total_individuals": len(individuals),
            "total_families": len(families),
            "duplicate_clusters": len(indi_clusters),
            "records_in_clusters": len(total_dup_ids),
            "estimated_unique_after_dedup": est_unique,
            "estimated_merges_needed": removed,
            "confidence_breakdown": {
                "exact_match": conf_counts.get("exact_match", 0),
                "likely_match": conf_counts.get("likely_match", 0),
                "possible_match": conf_counts.get("possible_match", 0),
            },
            "duplicate_family_groups": len(fam_dups),
        },
        "individual_clusters": indi_clusters,
        "duplicate_families": fam_dups,
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nFull analysis saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
