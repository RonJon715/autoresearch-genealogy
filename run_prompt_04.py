#!/usr/bin/env python3
"""Prompt 04: GEDCOM Completeness.
Ensure every person in Family_Tree.md exists in the GEDCOM with all known data.
"""

import os
import re
import yaml

VAULT = "/home/user/autoresearch-genealogy/vault"
GEDCOM = "/home/user/autoresearch-genealogy/Faulkner_cleaned.ged"
TODAY = "2026-03-20"

MONTH_MAP = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
    "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}


def parse_gedcom(path):
    """Parse GEDCOM into individual and family records."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    indis = {}
    fams = {}
    cur_id = None
    cur_type = None
    cur_data = {}
    ctx1 = None

    for raw in lines:
        line = raw.strip()
        parts = line.split(None, 2)
        if not parts:
            continue
        level = int(parts[0])
        tag = parts[1] if len(parts) > 1 else ""
        val = parts[2] if len(parts) > 2 else ""

        if level == 0:
            # Save previous record
            if cur_id and cur_type == "INDI":
                indis[cur_id] = cur_data
            elif cur_id and cur_type == "FAM":
                fams[cur_id] = cur_data
            # Start new record
            m = re.match(r"(@\S+@)\s+(\S+)", line[2:])
            if m:
                cur_id = m.group(1)
                cur_type = m.group(2)
                cur_data = {"names": [], "birth_date": "", "birth_place": "",
                           "death_date": "", "death_place": "", "sex": "",
                           "famc": [], "fams": [], "husb": "", "wife": "",
                           "chil": [], "marr_date": "", "marr_place": ""}
            else:
                cur_id = None
                cur_type = None
                cur_data = {}
            ctx1 = None
        elif level == 1:
            ctx1 = tag
            if cur_type == "INDI":
                if tag == "NAME":
                    cur_data["names"].append(val)
                elif tag == "SEX":
                    cur_data["sex"] = val
                elif tag == "FAMC":
                    cur_data["famc"].append(val)
                elif tag == "FAMS":
                    cur_data["fams"].append(val)
            elif cur_type == "FAM":
                if tag == "HUSB":
                    cur_data["husb"] = val
                elif tag == "WIFE":
                    cur_data["wife"] = val
                elif tag == "CHIL":
                    cur_data["chil"].append(val)
        elif level == 2:
            if tag == "DATE":
                if ctx1 == "BIRT":
                    cur_data["birth_date"] = val
                elif ctx1 == "DEAT":
                    cur_data["death_date"] = val
                elif ctx1 == "MARR":
                    cur_data["marr_date"] = val
            elif tag == "PLAC":
                if ctx1 == "BIRT":
                    cur_data["birth_place"] = val
                elif ctx1 == "DEAT":
                    cur_data["death_place"] = val
                elif ctx1 == "MARR":
                    cur_data["marr_place"] = val

    # Save last record
    if cur_id and cur_type == "INDI":
        indis[cur_id] = cur_data
    elif cur_id and cur_type == "FAM":
        fams[cur_id] = cur_data

    return indis, fams


def parse_frontmatter(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return {}
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    try:
        fm = yaml.safe_load(content[3:end])
        return fm if isinstance(fm, dict) else {}
    except Exception:
        return {}


def ged_name_to_display(name_str):
    m = re.match(r"^(.*?)\s*/([^/]*)/\s*(.*?)$", name_str)
    if m:
        return f"{m.group(1).strip()} {m.group(2).strip()}".strip()
    return name_str.strip()


def main():
    print("=== Prompt 04: GEDCOM Completeness ===\n")

    # Parse GEDCOM
    ged_indis, ged_fams = parse_gedcom(GEDCOM)
    print(f"GEDCOM: {len(ged_indis)} individuals, {len(ged_fams)} families")

    # Build name->id lookup from GEDCOM
    ged_name_lookup = {}
    for iid, data in ged_indis.items():
        for n in data["names"]:
            display = ged_name_to_display(n).lower().strip()
            if display:
                ged_name_lookup[display] = iid

    # Scan vault person files
    vault_persons = []
    for dirpath, _, filenames in os.walk(VAULT):
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(dirpath, fname)
            fm = parse_frontmatter(filepath)
            if fm.get("type") == "person":
                vault_persons.append((filepath, fm))

    print(f"Vault: {len(vault_persons)} person files")

    # Compare
    missing = []
    incomplete = []
    complete = 0
    total_missing_fields = 0

    for filepath, fm in vault_persons:
        name = fm.get("name", "").strip().strip('"')
        born = str(fm.get("born", "")).strip()
        died = str(fm.get("died", "")).strip()

        # Try to find in GEDCOM
        name_lower = name.lower()
        ged_id = ged_name_lookup.get(name_lower)

        if not ged_id:
            # Try fuzzy match
            for gname, gid in ged_name_lookup.items():
                if name_lower in gname or gname in name_lower:
                    ged_id = gid
                    break

        if not ged_id:
            missing.append({
                "name": name,
                "file": filepath.replace(VAULT + "/", ""),
                "born": born,
                "died": died,
                "missing_fields": "all"
            })
            continue

        # Check completeness
        ged = ged_indis[ged_id]
        missing_fields = []
        if born and not ged["birth_date"]:
            missing_fields.append("birth_date")
        if not born and ged["birth_date"]:
            pass  # Vault missing, not GEDCOM
        if born and not ged["birth_place"] and fm.get("birthplace"):
            missing_fields.append("birth_place")
        if died and not ged["death_date"]:
            missing_fields.append("death_date")
        if not ged["sex"]:
            missing_fields.append("sex")
        if not ged["famc"] and not ged["fams"]:
            missing_fields.append("family_links")

        if missing_fields:
            incomplete.append({
                "name": name,
                "file": filepath.replace(VAULT + "/", ""),
                "ged_id": ged_id,
                "missing_fields": ", ".join(missing_fields)
            })
            total_missing_fields += len(missing_fields)
        else:
            complete += 1

    print(f"\nResults:")
    print(f"  Complete (in GEDCOM with all data): {complete}")
    print(f"  Incomplete (in GEDCOM, missing fields): {len(incomplete)}")
    print(f"  Missing (not found in GEDCOM): {len(missing)}")
    print(f"  Total missing fields: {total_missing_fields}")

    # Validate GEDCOM structure
    validation_issues = []

    # Check for INDI without NAME
    nameless = sum(1 for d in ged_indis.values() if not d["names"])
    if nameless:
        validation_issues.append(f"{nameless} INDI records without NAME tag")

    # Check for FAM without HUSB or WIFE
    headless_fam = sum(1 for d in ged_fams.values() if not d["husb"] and not d["wife"])
    if headless_fam:
        validation_issues.append(f"{headless_fam} FAM records without HUSB or WIFE")

    # Check for orphaned CHIL references
    all_indi_ids = set(ged_indis.keys())
    orphaned = 0
    for fam in ged_fams.values():
        for c in fam["chil"]:
            if c not in all_indi_ids:
                orphaned += 1
    if orphaned:
        validation_issues.append(f"{orphaned} orphaned CHIL references (child ID not in INDI)")

    # Check TRLR
    with open(GEDCOM, "r") as f:
        content = f.read()
    if "0 TRLR" not in content:
        validation_issues.append("Missing 0 TRLR at end of file")

    print(f"\nGEDCOM Validation Issues: {len(validation_issues)}")
    for issue in validation_issues:
        print(f"  - {issue}")

    # Write audit
    audit = f"""---
type: reference
created: {TODAY}
updated: {TODAY}
tags: [genealogy, audit, gedcom, completeness]
---

# GEDCOM Completeness Audit

Generated {TODAY} by Prompt 04.

## Summary

| Metric | Count |
|---|---|
| GEDCOM individuals | {len(ged_indis)} |
| GEDCOM families | {len(ged_fams)} |
| Vault person files | {len(vault_persons)} |
| Complete (all data in GEDCOM) | {complete} |
| Incomplete (missing fields) | {len(incomplete)} |
| Missing (not in GEDCOM) | {len(missing)} |
| Total missing fields | {total_missing_fields} |

## GEDCOM Validation

| Check | Result |
|---|---|
| INDI records with NAME | {len(ged_indis) - nameless}/{len(ged_indis)} |
| FAM records with HUSB or WIFE | {len(ged_fams) - headless_fam}/{len(ged_fams)} |
| Orphaned CHIL references | {orphaned} |
| TRLR present | {"Yes" if "0 TRLR" in content else "No"} |
"""
    if validation_issues:
        audit += "\n### Issues\n\n"
        for issue in validation_issues:
            audit += f"- {issue}\n"

    audit += """
## Missing from GEDCOM

These persons exist in the vault but were not found in the GEDCOM file. They may have been added during tree expansion or may have name mismatches preventing matching.

| Person | File | Born | Died | Status |
|---|---|---|---|---|
"""
    for m in missing[:100]:
        audit += f"| {m['name']} | {m['file']} | {m['born']} | {m['died']} | MISSING |\n"
    if len(missing) > 100:
        audit += f"| ... and {len(missing) - 100} more | | | | |\n"
    if not missing:
        audit += "| (none) | | | | |\n"

    audit += """
## Incomplete in GEDCOM

These persons exist in the GEDCOM but are missing some data fields.

| Person | GEDCOM ID | Missing Fields | Status |
|---|---|---|---|
"""
    for inc in incomplete[:100]:
        audit += f"| {inc['name']} | {inc['ged_id']} | {inc['missing_fields']} | INCOMPLETE |\n"
    if len(incomplete) > 100:
        audit += f"| ... and {len(incomplete) - 100} more | | | |\n"
    if not incomplete:
        audit += "| (none) | | | |\n"

    audit += """
## Next Steps

1. For MISSING persons: add INDI records to GEDCOM with all known data from vault
2. For INCOMPLETE persons: add missing fields from vault data to GEDCOM
3. Re-validate after changes to ensure no orphaned references
4. Re-run after Prompt 01 (Tree Expansion) adds new persons
"""

    audit_path = os.path.join(VAULT, "gedcom_audit.md")
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write(audit)
    print(f"\nAudit written to {audit_path}")


if __name__ == "__main__":
    main()
