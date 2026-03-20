#!/usr/bin/env python3
"""Prompt 05: Source Citation Audit.
Verify every person file cites at least two independent sources.
"""

import os
import re
import yaml

VAULT = "/home/user/autoresearch-genealogy/vault"
TODAY = "2026-03-20"


def parse_frontmatter(filepath):
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
        return fm if isinstance(fm, dict) else {}, content
    except Exception:
        return {}, content


def count_doc_sources(content):
    """Count rows in Document Sources table."""
    count = 0
    in_section = False
    for line in content.split("\n"):
        if "## Document Sources" in line:
            in_section = True
            continue
        if in_section and line.startswith("##"):
            break
        if in_section and line.startswith("|") and "---" not in line and "Document" not in line:
            cells = [c.strip() for c in line.split("|")]
            cells = [c for c in cells if c]
            if cells:
                count += 1
    return count


def is_independent_source(s):
    """Check if a source string represents an independent source (not just GEDCOM import)."""
    s = str(s).lower()
    if not s:
        return False
    if "gedcom import" in s:
        return False
    if "unverified" in s:
        return False
    return True


def main():
    print("=== Prompt 05: Source Citation Audit ===\n")

    pass_list = []        # 2+ independent sources
    needs_corr = []       # 1 source
    unsourced = []        # 0 sources
    all_persons = []

    for dirpath, _, filenames in os.walk(VAULT):
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(dirpath, fname)
            fm, content = parse_frontmatter(filepath)
            if fm.get("type") != "person":
                continue

            name = fm.get("name", fname.replace(".md", "")).strip().strip('"')
            sources = fm.get("sources", [])
            if not isinstance(sources, list):
                sources = [sources] if sources else []

            independent = [s for s in sources if is_independent_source(s)]
            doc_count = count_doc_sources(content)
            confidence = fm.get("confidence", "stub")
            family = fm.get("family", "Unknown")

            record = {
                "name": name,
                "file": filepath.replace(VAULT + "/", ""),
                "independent_sources": len(independent),
                "total_sources": len(sources),
                "doc_table_rows": doc_count,
                "confidence": confidence,
                "family": family,
                "sources": [str(s) for s in sources[:5]],
            }
            all_persons.append(record)

            if len(independent) >= 2:
                pass_list.append(record)
            elif len(independent) == 1:
                needs_corr.append(record)
            else:
                unsourced.append(record)

    total = len(all_persons)
    print(f"Total person files: {total}")
    print(f"  PASS (2+ independent sources): {len(pass_list)}")
    print(f"  NEEDS_CORROBORATION (1 source): {len(needs_corr)}")
    print(f"  UNSOURCED (0 independent sources): {len(unsourced)}")

    # Confidence adjustments needed
    adjustments = []
    for p in all_persons:
        n = p["independent_sources"]
        current = p["confidence"]
        if n >= 3 and current != "high":
            adjustments.append((p, "high"))
        elif n == 2 and current not in ("moderate", "high"):
            adjustments.append((p, "moderate"))
        elif n == 1 and current not in ("low", "stub"):
            adjustments.append((p, "low"))
        elif n == 0 and current != "stub":
            adjustments.append((p, "stub"))

    print(f"\nConfidence adjustments needed: {len(adjustments)}")

    # Apply confidence adjustments
    adjusted_count = 0
    for p, new_conf in adjustments:
        filepath = os.path.join(VAULT, p["file"])
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            old_pattern = f"confidence: {p['confidence']}"
            new_pattern = f"confidence: {new_conf}"
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern, 1)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                adjusted_count += 1
        except Exception:
            pass

    print(f"Confidence levels adjusted: {adjusted_count}")

    # By-family breakdown
    family_stats = {}
    for p in all_persons:
        fam = p["family"]
        if fam not in family_stats:
            family_stats[fam] = {"pass": 0, "needs": 0, "unsourced": 0, "total": 0}
        family_stats[fam]["total"] += 1
        if p["independent_sources"] >= 2:
            family_stats[fam]["pass"] += 1
        elif p["independent_sources"] == 1:
            family_stats[fam]["needs"] += 1
        else:
            family_stats[fam]["unsourced"] += 1

    # Write audit
    audit = f"""---
type: reference
created: {TODAY}
updated: {TODAY}
tags: [genealogy, audit, sources, citations]
---

# Source Citation Audit

Generated {TODAY} by Prompt 05.

## Summary

| Category | Count | Percentage |
|---|---|---|
| PASS (2+ independent sources) | {len(pass_list)} | {len(pass_list)*100//total if total else 0}% |
| NEEDS_CORROBORATION (1 source) | {len(needs_corr)} | {len(needs_corr)*100//total if total else 0}% |
| UNSOURCED (0 independent sources) | {len(unsourced)} | {len(unsourced)*100//total if total else 0}% |
| **Total person files** | **{total}** | **100%** |

## Confidence Adjustments

{adjusted_count} person files had their confidence level adjusted based on source count:
- 3+ independent sources: high
- 2 independent sources: moderate
- 1 source: low
- 0 sources: stub

## By Family

| Family | Total | PASS | NEEDS_CORR | UNSOURCED |
|---|---|---|---|---|
"""
    for fam in sorted(family_stats.keys(), key=lambda f: family_stats[f]["total"], reverse=True)[:30]:
        s = family_stats[fam]
        audit += f"| {fam} | {s['total']} | {s['pass']} | {s['needs']} | {s['unsourced']} |\n"

    audit += """
## NEEDS_CORROBORATION Persons (1 source, need a second)

These individuals have exactly one independent source. A second corroborating source would raise their confidence level.

| Person | Family | Current Source | Confidence |
|---|---|---|---|
"""
    for p in needs_corr[:50]:
        src_str = p["sources"][0] if p["sources"] else "unknown"
        audit += f"| {p['name']} | {p['family']} | {src_str[:60]} | {p['confidence']} |\n"
    if len(needs_corr) > 50:
        audit += f"| ... and {len(needs_corr) - 50} more | | | |\n"

    audit += """
## UNSOURCED Persons (no independent sources)

These individuals have no independent source citations. All data comes from the GEDCOM import (Ancestry.com user tree) which is Tier 3 reliability.

| Person | Family | Confidence |
|---|---|---|
"""
    for p in unsourced[:100]:
        audit += f"| {p['name']} | {p['family']} | {p['confidence']} |\n"
    if len(unsourced) > 100:
        audit += f"| ... and {len(unsourced) - 100} more | | |\n"

    audit += """
## Methodology

Sources were classified as "independent" if they are NOT:
- "GEDCOM import (unverified)" or similar generic import markers
- Strings containing "unverified"

This is a conservative classification. Many GEDCOM records include Ancestry.com hint source references which were preserved during import, but these are ultimately user-contributed tree data and should be independently verified.

## Next Steps

1. For NEEDS_CORROBORATION: search Find a Grave, FamilySearch, census records for a second source
2. For UNSOURCED: determine original data source; search for ANY independent verification
3. Flag UNSOURCED persons with stub confidence in [[Open_Questions]]
4. Re-run after Prompt 03 (Find a Grave Sweep) which will add memorial sources
"""

    audit_path = os.path.join(VAULT, "source_citation_audit.md")
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write(audit)
    print(f"\nAudit written to {audit_path}")


if __name__ == "__main__":
    main()
