#!/usr/bin/env python3
"""Generate an Obsidian vault from a cleaned GEDCOM file."""

import json
import os
import re
from collections import defaultdict, Counter
from datetime import date

GEDCOM_PATH = "/home/user/autoresearch-genealogy/Faulkner_cleaned.ged"
VAULT_PATH = "/home/user/autoresearch-genealogy/vault"
TODAY = "2026-03-20"

MONTH_MAP = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
    "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}
MONTH_NUM = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_gedcom(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    records = []
    cur = []
    cur_id = cur_type = None
    for raw in lines:
        line = raw.rstrip("\r\n")
        if line.startswith("0 "):
            if cur:
                records.append((cur_type, cur_id, cur))
            cur = [line]
            m = re.match(r"0 (@\S+@) (\S+)", line)
            if m:
                cur_id, cur_type = m.group(1), m.group(2)
            else:
                cur_id = None
                cur_type = line.split(None, 1)[1] if " " in line else ""
        else:
            cur.append(line)
    if cur:
        records.append((cur_type, cur_id, cur))
    return records


def parse_level(line):
    parts = line.split(None, 2)
    level = int(parts[0]) if parts else 0
    tag = parts[1] if len(parts) > 1 else ""
    val = parts[2] if len(parts) > 2 else ""
    return level, tag, val.strip()


def extract_indi(lines):
    d = {"names": [], "givn": [], "surn": [], "nsfx": [], "sex": "",
         "birth_date": "", "birth_place": "", "death_date": "", "death_place": "",
         "burial_place": "", "famc": [], "fams": [], "resi": [], "sources": [],
         "occupations": []}
    ctx1 = None
    for line in lines:
        lv, tag, val = parse_level(line)
        if lv == 1:
            ctx1 = tag
            if tag == "NAME":
                d["names"].append(val)
            elif tag == "SEX":
                d["sex"] = val
            elif tag == "FAMC" and val:
                if val not in d["famc"]:
                    d["famc"].append(val)
            elif tag == "FAMS" and val:
                if val not in d["fams"]:
                    d["fams"].append(val)
            elif tag == "SOUR" and val:
                d["sources"].append(val)
            elif tag == "OCCU":
                d["occupations"].append(val)
        elif lv == 2:
            if tag == "GIVN":
                d["givn"].append(val)
            elif tag == "SURN":
                d["surn"].append(val)
            elif tag == "NSFX":
                d["nsfx"].append(val)
            elif tag == "DATE":
                if ctx1 == "BIRT":
                    d["birth_date"] = val
                elif ctx1 == "DEAT":
                    d["death_date"] = val
                elif ctx1 == "BURI":
                    pass
            elif tag == "PLAC":
                if ctx1 == "BIRT":
                    d["birth_place"] = val
                elif ctx1 == "DEAT":
                    d["death_place"] = val
                elif ctx1 == "BURI":
                    d["burial_place"] = val
                elif ctx1 == "RESI":
                    d["resi"].append(val)
            elif tag == "PAGE":
                d["sources"].append(val)
    return d


def extract_fam(lines):
    d = {"husb": "", "wife": "", "chil": [], "marr_date": "", "marr_place": ""}
    ctx1 = None
    for line in lines:
        lv, tag, val = parse_level(line)
        if lv == 1:
            ctx1 = tag
            if tag == "HUSB":
                d["husb"] = val
            elif tag == "WIFE":
                d["wife"] = val
            elif tag == "CHIL" and val:
                if val not in d["chil"]:
                    d["chil"].append(val)
        elif lv == 2:
            if ctx1 == "MARR":
                if tag == "DATE":
                    d["marr_date"] = val
                elif tag == "PLAC":
                    d["marr_place"] = val
    return d


# ---------------------------------------------------------------------------
# Name / date helpers
# ---------------------------------------------------------------------------

def parse_ged_name(name_str):
    m = re.match(r"^(.*?)\s*/([^/]*)/\s*(.*?)$", name_str)
    if m:
        return m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
    return name_str.strip(), "", ""


def best_name(indi):
    """Pick the richest name from the record."""
    best = ""
    best_len = 0
    for n in indi["names"]:
        g, s, sfx = parse_ged_name(n)
        full = f"{g} {s}".strip()
        if sfx:
            full += f" {sfx}"
        if len(full) > best_len:
            best = full
            best_len = len(full)
    if not best:
        g = indi["givn"][0] if indi["givn"] else ""
        s = indi["surn"][0] if indi["surn"] else ""
        best = f"{g} {s}".strip()
    return best


def get_surname(indi):
    if indi["surn"]:
        return indi["surn"][0]
    for n in indi["names"]:
        _, s, _ = parse_ged_name(n)
        if s:
            return s
    return "Unknown"


def format_date_iso(d):
    """Convert GEDCOM date to YYYY-MM-DD or partial."""
    if not d:
        return ""
    s = d.strip()
    for pfx in ["ABT", "BEF", "AFT", "EST", "CAL", "FROM", "TO", "BET", "INT"]:
        if s.upper().startswith(pfx):
            s = s[len(pfx):].strip()
    if " AND " in s.upper():
        s = s[:s.upper().index(" AND ")].strip()
    # MM/DD/YYYY
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        return f"{m.group(3)}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
    # DD Mon YYYY
    m = re.match(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", s)
    if m:
        mo = MONTH_MAP.get(m.group(2).lower(), "00")
        return f"{m.group(3)}-{mo}-{int(m.group(1)):02d}"
    # Mon YYYY
    m = re.match(r"(\w{3})\s+(\d{4})", s)
    if m:
        mo = MONTH_MAP.get(m.group(1).lower(), "00")
        return f"{m.group(2)}-{mo}"
    # YYYY
    m = re.match(r"(\d{4})", s)
    if m:
        return m.group(1)
    return d


def extract_year(d):
    if not d:
        return None
    m = re.search(r"(\d{4})", d)
    return int(m.group(1)) if m else None


def safe_filename(name):
    name = name.replace(" ", "_")
    name = re.sub(r"[^\w.\-]", "", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")


# ---------------------------------------------------------------------------
# Confidence
# ---------------------------------------------------------------------------

def calc_confidence(indi):
    has_birth = bool(indi["birth_date"])
    has_death = bool(indi["death_date"])
    has_sources = len(indi["sources"]) > 0
    has_parents = len(indi["famc"]) > 0
    if has_birth and has_death and has_sources and has_parents:
        return "high"
    if (has_birth or has_death) and has_sources:
        return "moderate"
    if has_birth or has_death or indi["birth_place"] or indi["death_place"]:
        return "low"
    return "stub"


# ---------------------------------------------------------------------------
# Main generation
# ---------------------------------------------------------------------------

def main():
    print("Parsing GEDCOM...")
    records = parse_gedcom(GEDCOM_PATH)

    indis = {}
    fams = {}
    sour_records = {}
    for rtype, rid, rlines in records:
        if rtype == "INDI":
            indis[rid] = extract_indi(rlines)
        elif rtype == "FAM":
            fams[rid] = extract_fam(rlines)
        elif rtype == "SOUR":
            # Extract source name
            for line in rlines:
                lv, tag, val = parse_level(line)
                if lv == 1 and tag == "TITL":
                    sour_records[rid] = val
                    break

    print(f"Loaded {len(indis)} individuals, {len(fams)} families")

    # Build lookup: id -> filename
    filenames = {}
    filename_counts = Counter()
    for iid, indi in indis.items():
        name = best_name(indi)
        surname = get_surname(indi)
        base = safe_filename(name) if name else "Unknown"
        # Disambiguate
        year = extract_year(indi["birth_date"])
        key = base
        filename_counts[key] += 1
        if filename_counts[key] > 1 and year:
            base = f"{base}_{year}"
        elif filename_counts[key] > 1:
            base = f"{base}_{filename_counts[key]}"
        filenames[iid] = (surname, base)

    # Second pass to fix collisions
    used = {}
    final_filenames = {}
    for iid, (surname, base) in filenames.items():
        key = f"{surname}/{base}"
        if key in used:
            # Add a counter
            cnt = 2
            while f"{surname}/{base}_{cnt}" in used:
                cnt += 1
            base = f"{base}_{cnt}"
            key = f"{surname}/{base}"
        used[key] = iid
        final_filenames[iid] = (surname, base)

    def wikilink(target_id):
        if target_id not in final_filenames:
            return "Unknown"
        sn, fn = final_filenames[target_id]
        return f"[[{fn}]]"

    def resolve_parents(indi):
        """Return (father_id, mother_id) from FAMC."""
        for fam_id in indi["famc"]:
            if fam_id in fams:
                f = fams[fam_id]
                return f["husb"] or None, f["wife"] or None
        return None, None

    def resolve_spouses_and_children(indi):
        """Return list of (spouse_id, marr_date, marr_place, [child_ids])."""
        results = []
        for fam_id in indi["fams"]:
            if fam_id in fams:
                f = fams[fam_id]
                if indi["sex"] == "M":
                    spouse_id = f["wife"] if f["wife"] else None
                else:
                    spouse_id = f["husb"] if f["husb"] else None
                results.append((spouse_id, f["marr_date"], f["marr_place"], f["chil"]))
        return results

    # Build person files
    os.makedirs(VAULT_PATH, exist_ok=True)
    surname_counts = Counter()
    confidence_counts = Counter()
    all_locations = set()
    issues = []  # (priority, question_text, detail)
    persons_missing_parents = []
    persons_missing_dates = []
    persons_no_sources = []

    print("Generating person files...")
    for iid, indi in indis.items():
        surname, fname = final_filenames[iid]
        sn_dir = safe_filename(surname) if surname else "Unknown"
        dir_path = os.path.join(VAULT_PATH, sn_dir)
        os.makedirs(dir_path, exist_ok=True)

        name = best_name(indi)
        conf = calc_confidence(indi)
        confidence_counts[conf] += 1
        surname_counts[surname] += 1

        born_iso = format_date_iso(indi["birth_date"])
        died_iso = format_date_iso(indi["death_date"])
        sn_lower = surname.lower().replace(" ", "-") if surname else "unknown"

        # Source citations
        src_list = []
        for s in indi["sources"][:10]:  # cap at 10
            if s.startswith("@") and s.endswith("@"):
                src_list.append(sour_records.get(s, s))
            else:
                src_list.append(s.strip('"'))

        # Relationships
        father_id, mother_id = resolve_parents(indi)
        spouse_info = resolve_spouses_and_children(indi)

        # Collect locations
        for loc in [indi["birth_place"], indi["death_place"], indi["burial_place"]]:
            if loc:
                all_locations.add(loc)

        # Track issues
        if not father_id and not mother_id:
            persons_missing_parents.append((iid, name))
        if not indi["birth_date"] and not indi["death_date"]:
            persons_missing_dates.append((iid, name))
        if not indi["sources"]:
            persons_no_sources.append((iid, name))

        # Build father/mother strings
        father_str = wikilink(father_id) if father_id else "Unknown"
        mother_str = wikilink(mother_id) if mother_id else "Unknown"

        # Build spouse strings
        spouse_lines = []
        all_children = []
        for sp_id, m_date, m_place, children in spouse_info:
            sp_str = wikilink(sp_id) if sp_id else "Unknown"
            m_parts = []
            if m_date:
                m_parts.append(f"m. {m_date}")
            if m_place:
                m_parts.append(m_place)
            if m_parts:
                sp_str += f" ({', '.join(m_parts)})"
            spouse_lines.append(sp_str)
            all_children.extend(children)

        spouse_val = "; ".join(spouse_lines) if spouse_lines else ""
        children_val = ", ".join(wikilink(c) for c in all_children) if all_children else ""

        # YAML sources
        yaml_sources = ""
        if src_list:
            for s in src_list[:5]:
                safe_s = s.replace('"', '\\"')
                yaml_sources += f'\n  - "{safe_s}"'
        else:
            yaml_sources = '\n  - "GEDCOM import (unverified)"'

        # Write file
        content = f"""---
type: person
name: "{name}"
born: {born_iso}
died: {died_iso}
family: "{surname}"
confidence: {conf}
sources:{yaml_sources}
created: {TODAY}
tags: [genealogy, {sn_lower}, person]
---

# {name}

## Vital Information

| Field | Value | Source |
|---|---|---|
| Full Name | {name} | GEDCOM import |
| Born | {indi["birth_date"]} | GEDCOM import |
| Birthplace | {indi["birth_place"]} | GEDCOM import |
| Died | {indi["death_date"]} | GEDCOM import |
| Burial | {indi["burial_place"]} | GEDCOM import |
| Father | {father_str} | GEDCOM import |
| Mother | {mother_str} | GEDCOM import |
| Spouse | {spouse_val} | GEDCOM import |
| Children | {children_val} | GEDCOM import |

## Biography

No biography written yet. See sources and vital information above.

## Document Sources

| Document | Type | Vault Note |
|---|---|---|
| GEDCOM import from Ancestry.com | GEDCOM export | |
"""
        for s in src_list[:5]:
            content += f"| {s} | Ancestry.com hint | |\n"

        content += """
## Data Discrepancies

No discrepancies identified during import.
"""
        filepath = os.path.join(dir_path, f"{fname}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Created {len(indis)} person files")

    # -----------------------------------------------------------------------
    # Family_Tree.md
    # -----------------------------------------------------------------------
    print("Generating Family_Tree.md...")
    ft = f"""---
type: reference
created: {TODAY}
updated: {TODAY}
tags: [genealogy, family-tree]
---

# Family Tree

Complete merged family tree imported from Ancestry.com GEDCOM. All dates from GEDCOM import (unverified against primary sources).

"""
    # Group by surname
    surname_groups = defaultdict(list)
    for iid, indi in indis.items():
        sn = get_surname(indi)
        surname_groups[sn].append((iid, indi))

    for sn in sorted(surname_groups.keys()):
        ft += f"## {sn} Family\n\n"
        members = surname_groups[sn]
        # Sort by birth year
        def sort_key(item):
            y = extract_year(item[1]["birth_date"])
            return y if y else 9999
        members.sort(key=sort_key)
        for iid, indi in members:
            name = best_name(indi)
            link = wikilink(iid)
            by = indi["birth_date"] or "?"
            bp = indi["birth_place"] or ""
            dy = indi["death_date"] or "?"
            dp = indi["death_place"] or ""
            birth_str = f"b. {by}"
            if bp:
                birth_str += f", {bp}"
            death_str = f"d. {dy}"
            if dp:
                death_str += f", {dp}"
            ft += f"**{link}** ({birth_str}; {death_str}) (unverified)\n"

            # Spouse info
            for sp_id, m_date, m_place, children in resolve_spouses_and_children(indi):
                if sp_id:
                    sp_link = wikilink(sp_id)
                    m_info = ""
                    if m_date:
                        m_info += f" on {m_date}"
                    if m_place:
                        m_info += f" at {m_place}"
                    ft += f"- Married {sp_link}{m_info}\n"
                if children:
                    child_links = ", ".join(wikilink(c) for c in children)
                    ft += f"- Children: {child_links}\n"
            ft += "\n"

    # Geographic Origins
    loc_surnames = defaultdict(set)
    for iid, indi in indis.items():
        sn = get_surname(indi)
        for loc in [indi["birth_place"], indi["death_place"]]:
            if loc:
                parts = [p.strip() for p in loc.split(",") if p.strip()]
                if parts:
                    region = parts[-1] if len(parts) >= 1 else loc
                    if len(parts) >= 2:
                        region = f"{parts[-2]}, {parts[-1]}"
                    loc_surnames[region].add(sn)

    ft += "## Geographic Origins\n\n"
    ft += "| Region | Family Lines |\n|---|---|\n"
    for region in sorted(loc_surnames.keys())[:50]:
        snames = ", ".join(sorted(loc_surnames[region])[:5])
        ft += f"| {region} | {snames} |\n"

    with open(os.path.join(VAULT_PATH, "Family_Tree.md"), "w", encoding="utf-8") as f:
        f.write(ft)

    # -----------------------------------------------------------------------
    # Research_Log.md
    # -----------------------------------------------------------------------
    print("Generating Research_Log.md...")
    rl = f"""---
type: reference
created: {TODAY}
updated: {TODAY}
tags: [genealogy, research, log]
---

# Research Log

Chronological record of every archive searched, every query run, and every result (positive or negative). Negative results are as important as positive ones.

## {TODAY}: GEDCOM Import from Ancestry.com

### Full Tree Import

**Query**: Import complete family tree from Ancestry.com GEDCOM export
**Source**: Faulkner.ged (Ancestry.com Family Trees, exported 2026-03-19)
**Results**: Imported {len(indis)} individuals across {len(fams)} families, covering {len(surname_counts)} surnames. After deduplication, reduced from 2,834 to {len(indis)} individuals (567 duplicates removed).
**Implication**: Baseline tree established from Ancestry.com data. All data is Tier 3 (user contributed tree) and needs verification against primary sources. Source citations from Ancestry hints are preserved but the underlying records have not been independently verified.
**Next step**: Run source citation audit (prompt 05) to identify which claims have Ancestry hint sources vs. no sources at all. Then run cross reference audit (prompt 02) to check for internal consistency.

---

## Logging Convention

Every search gets logged, positive or negative. Use this format:

- **Date**: When the search was performed
- **Query**: Exact search terms (so you can avoid repeating the same search)
- **Source**: The database, website, or archive
- **Results**: What was found. "No results" is a valid and important entry.
- **Implication**: What the result (or lack thereof) means for the research
- **Next step**: What to do next based on this result
"""
    with open(os.path.join(VAULT_PATH, "Research_Log.md"), "w", encoding="utf-8") as f:
        f.write(rl)

    # -----------------------------------------------------------------------
    # Open_Questions.md
    # -----------------------------------------------------------------------
    print("Generating Open_Questions.md...")
    oq = f"""---
type: reference
created: {TODAY}
updated: {TODAY}
tags: [genealogy, research, open-questions]
---

# Open Questions

Research gaps and unresolved questions auto-detected during GEDCOM import on {TODAY}. Organized by priority.

## High Priority (Would Significantly Advance Understanding)

"""
    q_num = 1

    # People with no parents and significant data
    high_priority_orphans = [(iid, n) for iid, n in persons_missing_parents
                             if indis[iid]["birth_date"] or indis[iid]["death_date"]]
    if high_priority_orphans:
        oq += f"### {q_num}. Unknown parents for individuals with vital records\n"
        oq += f"- **The conflict**: {len(high_priority_orphans)} individuals have birth or death dates but no parent links in the GEDCOM\n"
        oq += "- **Impact**: Connecting these to parents would extend family lines further back\n"
        oq += "- **Solvability**: MODERATE\n"
        oq += "- **Next step**: Search vital records (birth certificates, church records) for parent names\n"
        oq += "- **Individuals** (top 20):\n"
        for iid, n in high_priority_orphans[:20]:
            oq += f"  - {wikilink(iid)} ({n})\n"
        oq += "\n"
        q_num += 1

    oq += "## Medium Priority\n\n"

    # Missing dates
    if persons_missing_dates:
        oq += f"### {q_num}. Individuals missing both birth and death dates\n"
        oq += f"- **The question**: {len(persons_missing_dates)} individuals have no birth or death dates\n"
        oq += "- **Minimum records needed**: Vital records, census records, or church registers\n"
        oq += "- **Solvability**: MODERATE\n"
        oq += "- **Payoff**: MODERATE (dates help confirm identities and rule out false merges)\n"
        oq += "- **Individuals** (top 20):\n"
        for iid, n in persons_missing_dates[:20]:
            oq += f"  - {wikilink(iid)} ({n})\n"
        oq += "\n"
        q_num += 1

    oq += "## Low Priority / Future Research\n\n"

    if persons_no_sources:
        oq += f"### {q_num}. Individuals with no source citations\n"
        oq += f"- {len(persons_no_sources)} individuals have no source citations whatsoever. These claims are entirely unsourced and should be treated as Tier 3 (speculative) until verified.\n"
        oq += "\n"
        q_num += 1

    oq += """## Data Acquisition Priorities

| Priority | Record Type | Location | Expected Yield | Cost |
|---|---|---|---|---|
| 1 | Vital records (birth, marriage, death) | County courthouses, state archives | Parent names, dates, places | Varies |
| 2 | Census records | Ancestry.com, FamilySearch.org | Household composition, ages, birthplaces | Free (FamilySearch) |
| 3 | Church records | Local parishes, diocesan archives | Baptism, marriage, burial dates | Free to low cost |
| 4 | Immigration records | NARA, Ancestry.com | Ship manifests, naturalization | Free (FamilySearch) |
"""
    with open(os.path.join(VAULT_PATH, "Open_Questions.md"), "w", encoding="utf-8") as f:
        f.write(oq)

    # -----------------------------------------------------------------------
    # Data_Inventory.md
    # -----------------------------------------------------------------------
    print("Generating Data_Inventory.md...")
    di = f"""---
type: reference
created: {TODAY}
tags: [genealogy, data, inventory, sources]
---

# Data Inventory

Complete inventory of all ancestry data assets imported from GEDCOM on {TODAY}.

## Import Summary

| Metric | Count |
|---|---|
| Total person files | {len(indis)} |
| Total family groups | {len(fams)} |
| Unique surnames | {len(surname_counts)} |
| Confidence: high | {confidence_counts.get("high", 0)} |
| Confidence: moderate | {confidence_counts.get("moderate", 0)} |
| Confidence: low | {confidence_counts.get("low", 0)} |
| Confidence: stub | {confidence_counts.get("stub", 0)} |
| Missing parents | {len(persons_missing_parents)} |
| Missing all dates | {len(persons_missing_dates)} |
| No source citations | {len(persons_no_sources)} |

## Surname Breakdown

| Surname | Individuals |
|---|---|
"""
    for sn, cnt in surname_counts.most_common(50):
        di += f"| {sn} | {cnt} |\n"

    di += """
## Genealogical Documents

### High Reliability (official records, primary sources)

No primary source documents imported. GEDCOM contains Ancestry.com hint references only.

### Moderate Reliability (newspaper, secondary sources)

| Document | Family | Location |
|---|---|---|
| Ancestry.com GEDCOM export | All families | Faulkner_cleaned.ged |

### Low Reliability (anecdotal, interpreted)

| Document | Family | Notes |
|---|---|---|
| Ancestry.com user tree hints | All families | Tier 3 source; user contributed, needs independent verification |

## Vault Research Notes

{len(indis)} person markdown files in vault/

## Source Document Archive

| Collection | Files | Location | OCR Status |
|---|---|---|---|
| GEDCOM export | 1 | Faulkner_cleaned.ged | N/A (structured data) |

## What's Missing (Acquisition Priorities)

See [[Open_Questions]] for the full list. Top gaps:

1. Primary source vital records (birth, marriage, death certificates) for all individuals
2. Census records to verify household compositions and dates
3. Church records for baptisms, confirmations, marriages, and burials
4. Immigration and naturalization records for immigrant ancestors
5. Military records for service members
"""
    with open(os.path.join(VAULT_PATH, "Data_Inventory.md"), "w", encoding="utf-8") as f:
        f.write(di)

    # -----------------------------------------------------------------------
    # Estimate generations
    # -----------------------------------------------------------------------
    def count_generations(iid, visited=None):
        if visited is None:
            visited = set()
        if iid in visited or iid not in indis:
            return 0
        visited.add(iid)
        father_id, mother_id = resolve_parents(indis[iid])
        f_gen = count_generations(father_id, visited) if father_id else 0
        m_gen = count_generations(mother_id, visited) if mother_id else 0
        return 1 + max(f_gen, m_gen)

    # Find likely root person (first in file, usually the tree owner)
    first_id = list(indis.keys())[0]
    max_gen = count_generations(first_id)

    # Also try a broader estimate
    all_years = [extract_year(indis[i]["birth_date"]) for i in indis if extract_year(indis[i]["birth_date"])]
    if all_years:
        year_range = max(all_years) - min(all_years)
        est_gen = year_range // 25 + 1
    else:
        est_gen = max_gen

    generations = max(max_gen, est_gen)

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("VAULT GENERATION COMPLETE")
    print("=" * 60)
    print(f"\nTotal person files created: {len(indis)}")
    print(f"Estimated generations: {generations}")
    print(f"Unique surnames: {len(surname_counts)}")
    print(f"\nTop 20 surnames:")
    for sn, cnt in surname_counts.most_common(20):
        print(f"  {sn}: {cnt}")
    print(f"\nConfidence breakdown:")
    for tier in ["high", "moderate", "low", "stub"]:
        print(f"  {tier}: {confidence_counts.get(tier, 0)}")
    print(f"\nData quality issues:")
    print(f"  Missing parents: {len(persons_missing_parents)}")
    print(f"  Missing all dates: {len(persons_missing_dates)}")
    print(f"  No source citations: {len(persons_no_sources)}")
    print(f"\nVault location: {VAULT_PATH}")


if __name__ == "__main__":
    main()
