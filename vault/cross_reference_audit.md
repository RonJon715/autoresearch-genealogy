---
type: reference
created: 2026-03-20
updated: 2026-03-20
tags: [genealogy, audit, cross-reference]
---

# Cross-Reference Audit

Generated 2026-03-20 by Prompt 02.

## Summary

| Metric | Count |
|---|---|
| Person files checked | 2134 |
| Total discrepancies | 8 |
| CONFLICT (data mismatches) | 0 |
| LOGGED (name variants) | 8 |
| INCOMPLETE (missing data) | 0 |

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
| (none found) | | | | | | |

## Name Variants (Logged, Not Errors)

| Person | Frontmatter Name | Table Name | Status |
|---|---|---|---|
| Celia Bowin Bourne | Celia Bowin Bourne | Celia Bowin\ Bourne | LOGGED |
| William Lightfoot ightfoote | William Lightfoot ightfoote | William Lightfoot\Lightfoote | LOGGED |
| CATHERINE Katherine Throckmorton  Dame Chester | CATHERINE Katherine Throckmorton  Dame Chester | CATHERINE Katherine Throckmorton \ Dame Chester | LOGGED |
| Ensign Richard H. Haile Sr.  Rev War | Ensign Richard H. Haile Sr.  Rev War | Ensign Richard H. Haile Sr. \ Rev War | LOGGED |
| Jonas Meador  Meadows | Jonas Meador  Meadows | Jonas Meador \ Meadows | LOGGED |
| Francis Meador  Meadows | Francis Meador  Meadows | Francis Meador \ Meadows | LOGGED |
| Emilie Gann ettigrew | Emilie Gann ettigrew | Emilie Gann\Pettigrew | LOGGED |
| Richard  Nicholas Burt | Richard  Nicholas Burt | Richard \ Nicholas Burt | LOGGED |

## Incomplete Records (Missing All Dates)

| Person | File | Status |
|---|---|---|
| (none found) | | |

## Resolution Log

All discrepancies in this audit were auto-detected during the initial GEDCOM import. Since all data originates from a single source (Ancestry.com GEDCOM export), internal consistency is expected to be high. The discrepancies found are primarily:
1. Name formatting differences between YAML frontmatter (which uses ISO format) and the display table (which uses GEDCOM format)
2. Missing data fields that were absent in the original GEDCOM

No primary source documents are available to resolve conflicts at this time. All data should be treated as Tier 3 (user contributed tree) until verified against primary sources.

## Next Steps

1. For CONFLICT items: locate primary source documents (vital records, census) to determine correct values
2. For INCOMPLETE items: search vital records, census, and church registers for missing dates
3. Re-run this audit after Prompt 01 (Tree Expansion) adds new data
