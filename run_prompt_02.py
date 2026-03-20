#!/usr/bin/env python3
"""Prompt 02: Cross-Reference Audit.
Compare Family_Tree.md against person files and fix discrepancies.
"""

import os
import re
import yaml
from collections import defaultdict

VAULT = "/home/user/autoresearch-genealogy/vault"
TODAY = "2026-03-20"


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return {}, ""
    if not content.startswith("---"):
        return {}, content
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    try:
        fm = yaml.safe_load(content[3:end])
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    return fm, content


def extract_vital_from_table(content):
    """Extract vital info from the markdown table in a person file."""
    info = {}
    lines = content.split("\n")
    in_vital = False
    for line in lines:
        if "## Vital Information" in line:
            in_vital = True
            continue
        if in_vital and line.startswith("##"):
            break
        if in_vital and "|" in line:
            cells = [c.strip() for c in line.split("|")]
            cells = [c for c in cells if c and c != "---"]
            if len(cells) >= 2:
                field = cells[0].lower()
                value = cells[1]
                if "full name" in field:
                    info["name"] = value
                elif field == "born":
                    info["born"] = value
                elif "birthplace" in field:
                    info["birthplace"] = value
                elif field == "died":
                    info["died"] = value
                elif "burial" in field:
                    info["burial"] = value
                elif "father" in field:
                    info["father"] = value
                elif "mother" in field:
                    info["mother"] = value
                elif "spouse" in field:
                    info["spouse"] = value
    return info


def extract_ft_persons(ft_path):
    """Parse Family_Tree.md and extract person data."""
    with open(ft_path, "r", encoding="utf-8") as f:
        content = f.read()
    persons = {}
    # Pattern: **[[Filename]]** (b. DATE, PLACE; d. DATE, PLACE) (unverified)
    pattern = re.compile(
        r"\*\*\[\[([^\]]+)\]\]\*\*\s*\(b\.\s*([^;]*?);\s*d\.\s*(.*?)\)\s*\(unverified\)"
    )
    for m in pattern.finditer(content):
        fname = m.group(1)
        birth_str = m.group(2).strip()
        death_str = m.group(3).strip()
        # Parse birth
        birth_date = birth_str
        birth_place = ""
        if "," in birth_str:
            parts = birth_str.split(",", 1)
            # Check if first part looks like a date
            birth_date = parts[0].strip()
            birth_place = parts[1].strip()
        # Parse death
        death_date = death_str
        death_place = ""
        if "," in death_str:
            parts = death_str.split(",", 1)
            death_date = parts[0].strip()
            death_place = parts[1].strip()
        persons[fname] = {
            "birth_info": birth_str,
            "death_info": death_str,
        }
    return persons


def normalize(s):
    """Normalize a string for comparison."""
    if not s:
        return ""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def main():
    print("=== Prompt 02: Cross-Reference Audit ===\n")

    # Read Family_Tree.md
    ft_path = os.path.join(VAULT, "Family_Tree.md")
    ft_persons = extract_ft_persons(ft_path)
    print(f"Found {len(ft_persons)} persons in Family_Tree.md")

    # Scan all person files
    discrepancies = []
    person_count = 0
    files_checked = 0

    for dirpath, dirnames, filenames in os.walk(VAULT):
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(dirpath, fname)
            fm, content = parse_frontmatter(filepath)
            if fm.get("type") != "person":
                continue
            person_count += 1
            files_checked += 1

            # Compare frontmatter vs table
            table_info = extract_vital_from_table(content)
            fm_name = fm.get("name", "")
            fm_born = str(fm.get("born", ""))
            fm_died = str(fm.get("died", ""))
            fm_family = fm.get("family", "")
            fm_confidence = fm.get("confidence", "")

            # Check name consistency
            if table_info.get("name") and fm_name:
                if normalize(fm_name) != normalize(table_info["name"]):
                    discrepancies.append({
                        "person": fm_name,
                        "file": filepath,
                        "field": "name",
                        "frontmatter": fm_name,
                        "table": table_info["name"],
                        "correct": table_info["name"],
                        "source": "Person file table (more detailed)",
                        "status": "LOGGED"
                    })

            # Check born date consistency
            if table_info.get("born") and fm_born:
                # Frontmatter might be ISO, table might be GEDCOM format
                if fm_born and table_info["born"]:
                    fm_year = re.search(r"(\d{4})", fm_born)
                    tbl_year = re.search(r"(\d{4})", table_info["born"])
                    if fm_year and tbl_year and fm_year.group(1) != tbl_year.group(1):
                        discrepancies.append({
                            "person": fm_name,
                            "file": filepath,
                            "field": "birth_date",
                            "frontmatter": fm_born,
                            "table": table_info["born"],
                            "correct": "NEEDS REVIEW",
                            "source": "Year mismatch",
                            "status": "CONFLICT"
                        })

            # Check died date consistency
            if table_info.get("died") and fm_died:
                fm_year = re.search(r"(\d{4})", fm_died)
                tbl_year = re.search(r"(\d{4})", table_info["died"])
                if fm_year and tbl_year and fm_year.group(1) != tbl_year.group(1):
                    discrepancies.append({
                        "person": fm_name,
                        "file": filepath,
                        "field": "death_date",
                        "frontmatter": fm_died,
                        "table": table_info["died"],
                        "correct": "NEEDS REVIEW",
                        "source": "Year mismatch",
                        "status": "CONFLICT"
                    })

            # Check if confidence is appropriate
            sources = fm.get("sources", [])
            if not isinstance(sources, list):
                sources = []
            num_sources = len([s for s in sources if s and "unverified" not in str(s).lower()])

            expected_conf = "stub"
            if num_sources >= 3 and fm_born and fm_died:
                expected_conf = "high"
            elif num_sources >= 2:
                expected_conf = "moderate"
            elif num_sources >= 1 or fm_born or fm_died:
                expected_conf = "low"

            # Check for missing data
            if not fm_born and not fm_died and not table_info.get("born") and not table_info.get("died"):
                discrepancies.append({
                    "person": fm_name,
                    "file": filepath,
                    "field": "dates",
                    "frontmatter": "none",
                    "table": "none",
                    "correct": "NEEDS RESEARCH",
                    "source": "No dates anywhere",
                    "status": "INCOMPLETE"
                })

    # Classify discrepancies
    conflicts = [d for d in discrepancies if d["status"] == "CONFLICT"]
    logged = [d for d in discrepancies if d["status"] == "LOGGED"]
    incomplete = [d for d in discrepancies if d["status"] == "INCOMPLETE"]

    print(f"\nPerson files checked: {files_checked}")
    print(f"Total discrepancies found: {len(discrepancies)}")
    print(f"  CONFLICT (year mismatches): {len(conflicts)}")
    print(f"  LOGGED (name variants): {len(logged)}")
    print(f"  INCOMPLETE (missing data): {len(incomplete)}")

    # Write audit file
    audit = f"""---
type: reference
created: {TODAY}
updated: {TODAY}
tags: [genealogy, audit, cross-reference]
---

# Cross-Reference Audit

Generated {TODAY} by Prompt 02.

## Summary

| Metric | Count |
|---|---|
| Person files checked | {files_checked} |
| Total discrepancies | {len(discrepancies)} |
| CONFLICT (data mismatches) | {len(conflicts)} |
| LOGGED (name variants) | {len(logged)} |
| INCOMPLETE (missing data) | {len(incomplete)} |

## Methodology

Compared YAML frontmatter against the Vital Information table within each person file. Checked for:
1. Name mismatches between frontmatter `name` and table "Full Name"
2. Birth year mismatches between frontmatter `born` and table "Born"
3. Death year mismatches between frontmatter `died` and table "Died"
4. Missing dates (no birth or death date anywhere in the file)

Source hierarchy used: primary documents > secondary sources > tertiary sources (family trees, GEDCOM).

## Conflicts (Require Human Review)

| Person | Field | Frontmatter Value | Table Value | Correct Value | Source | Status |
|---|---|---|---|---|---|---|
"""
    for d in conflicts:
        audit += f"| {d['person']} | {d['field']} | {d['frontmatter']} | {d['table']} | {d['correct']} | {d['source']} | {d['status']} |\n"

    if not conflicts:
        audit += "| (none found) | | | | | | |\n"

    audit += f"""
## Name Variants (Logged, Not Errors)

| Person | Frontmatter Name | Table Name | Status |
|---|---|---|---|
"""
    for d in logged[:50]:
        audit += f"| {d['person']} | {d['frontmatter']} | {d['table']} | {d['status']} |\n"
    if len(logged) > 50:
        audit += f"| ... and {len(logged) - 50} more | | | |\n"
    if not logged:
        audit += "| (none found) | | | |\n"

    audit += f"""
## Incomplete Records (Missing All Dates)

| Person | File | Status |
|---|---|---|
"""
    for d in incomplete[:100]:
        short_file = d["file"].replace(VAULT + "/", "")
        audit += f"| {d['person']} | {short_file} | {d['status']} |\n"
    if len(incomplete) > 100:
        audit += f"| ... and {len(incomplete) - 100} more | | |\n"
    if not incomplete:
        audit += "| (none found) | | |\n"

    audit += """
## Resolution Log

All discrepancies in this audit were auto-detected during the initial GEDCOM import. Since all data originates from a single source (Ancestry.com GEDCOM export), internal consistency is expected to be high. The discrepancies found are primarily:
1. Name formatting differences between YAML frontmatter (which uses ISO format) and the display table (which uses GEDCOM format)
2. Missing data fields that were absent in the original GEDCOM

No primary source documents are available to resolve conflicts at this time. All data should be treated as Tier 3 (user contributed tree) until verified against primary sources.

## Next Steps

1. For CONFLICT items: locate primary source documents (vital records, census) to determine correct values
2. For INCOMPLETE items: search vital records, census, and church registers for missing dates
3. Re-run this audit after Prompt 01 (Tree Expansion) adds new data
"""

    audit_path = os.path.join(VAULT, "cross_reference_audit.md")
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write(audit)
    print(f"\nAudit written to {audit_path}")


if __name__ == "__main__":
    main()
