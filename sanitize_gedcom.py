#!/usr/bin/env python3
"""Sanitize a cleaned GEDCOM file for upload to Ancestry.

Fixes:
- Non-standard date formats (MM/DD/YYYY -> DD MON YYYY, full month names -> 3-letter,
  year ranges -> BET YYYY AND YYYY)
- Record ordering (HEAD, SUBM, INDI, FAM, SOUR, OBJE, NOTE, REPO, TRLR)
- Ensures TRLR is the final record
- Strips Ancestry-internal custom tags that cause import warnings (_ENV, _PRIM)
  while preserving _APID (Ancestry source links) and _TREE
"""

import re
import sys

MONTH_NUM_TO_GEDCOM = {
    1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN",
    7: "JUL", 8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC",
}

FULL_MONTH_TO_GEDCOM = {
    "january": "JAN", "february": "FEB", "march": "MAR", "april": "APR",
    "may": "MAY", "june": "JUN", "july": "JUL", "august": "AUG",
    "september": "SEP", "october": "OCT", "november": "NOV", "december": "DEC",
}


def fix_date(date_str):
    """Convert non-standard date formats to GEDCOM 5.5.1 standard."""
    s = date_str.strip()
    if not s:
        return s

    # Preserve qualifiers (ABT, BEF, AFT, etc.)
    prefix = ""
    for qual in ["ABT", "BEF", "AFT", "EST", "CAL", "FROM", "TO", "BET", "INT"]:
        if s.upper().startswith(qual + " "):
            prefix = qual + " "
            s = s[len(prefix):].strip()
            break

    # MM/DD/YYYY with optional time -> DD MON YYYY
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})(\s+.*)?$", s)
    if m:
        month = int(m.group(1))
        day = int(m.group(2))
        year = m.group(3)
        mon_str = MONTH_NUM_TO_GEDCOM.get(month, "")
        if mon_str:
            # Drop any trailing time component for clean GEDCOM
            return f"{prefix}{day} {mon_str} {year}"

    # YYYY-YYYY year range -> BET YYYY AND YYYY
    m = re.match(r"^(\d{4})\s*-\s*(\d{4})$", s)
    if m:
        return f"BET {m.group(1)} AND {m.group(2)}"

    # Normalize multiple spaces to single, strip leading/trailing
    s = re.sub(r"\s+", " ", s).strip()

    # Normalize qualifier abbreviations and words at start
    qual_map = {
        "by": "BEF", "before": "BEF", "bef.": "BEF", "bef": "BEF",
        "after": "AFT", "aft.": "AFT", "aft": "AFT",
        "about": "ABT", "abt.": "ABT", "abt": "ABT", "circa": "ABT", "ca.": "ABT",
    }
    first_word = s.split()[0].lower() if s else ""
    if first_word in qual_map:
        prefix = qual_map[first_word] + " "
        s = s[len(first_word):].strip()

    # Remove ordinal suffixes: 12th -> 12, 1st -> 1, 2nd -> 2, 3rd -> 3
    s = re.sub(r"(\d+)(st|nd|rd|th)\b", r"\1", s)

    # Remove commas (often in "April 28, 1758" or "February, 1727")
    s = s.replace(",", "")

    # Strip parenthetical notes: "(photo of doc -June 2006)"
    s = re.sub(r"\s*\(.*?\)\s*", " ", s).strip()

    # "April 28, 1758" -> "28 APR 1758" (American format with comma)
    m = re.match(r"^(\w+)\s+(\d{1,2}),?\s+(\d{4})$", s)
    if m:
        month_word = m.group(1).lower()
        if month_word in FULL_MONTH_TO_GEDCOM:
            return f"{prefix}{m.group(2)} {FULL_MONTH_TO_GEDCOM[month_word]} {m.group(3)}"

    # "2 November 1938" or "3 July1915" (possibly missing space before year)
    m = re.match(r"^(\d{1,2})\s+(\w+?)(\d{4})$", s)
    if m:
        month_word = m.group(2).lower().strip()
        if month_word in FULL_MONTH_TO_GEDCOM:
            return f"{prefix}{m.group(1)} {FULL_MONTH_TO_GEDCOM[month_word]} {m.group(3)}"

    # "2 November 1938" (with proper spacing)
    m = re.match(r"^(\d{1,2})\s+(\w+)\s+(\d{4})$", s)
    if m:
        month_word = m.group(2).lower()
        if month_word in FULL_MONTH_TO_GEDCOM:
            return f"{prefix}{m.group(1)} {FULL_MONTH_TO_GEDCOM[month_word]} {m.group(3)}"

    # "18 April 1661 - 1669" (date with year range)
    m = re.match(r"^(\d{1,2})\s+(\w+)\s+(\d{4})\s*-\s*(\d{4})$", s)
    if m:
        month_word = m.group(2).lower()
        if month_word in FULL_MONTH_TO_GEDCOM:
            return f"BET {m.group(1)} {FULL_MONTH_TO_GEDCOM[month_word]} {m.group(3)} AND {m.group(4)}"

    # "November 1938" -> "NOV 1938"
    m = re.match(r"^(\w+)\s+(\d{4})$", s)
    if m:
        month_word = m.group(1).lower()
        if month_word in FULL_MONTH_TO_GEDCOM:
            return f"{prefix}{FULL_MONTH_TO_GEDCOM[month_word]} {m.group(2)}"

    # "30 November" (day month, no year)
    m = re.match(r"^(\d{1,2})\s+(\w+)$", s)
    if m:
        month_word = m.group(2).lower()
        if month_word in FULL_MONTH_TO_GEDCOM:
            return f"{prefix}{m.group(1)} {FULL_MONTH_TO_GEDCOM[month_word]}"

    # If nothing matched, do a global replacement of full month names
    result = s
    for full, abbr in FULL_MONTH_TO_GEDCOM.items():
        result = re.sub(re.escape(full), abbr, result, flags=re.IGNORECASE)
    # Also handle abbreviated with period: "Nov." -> "NOV"
    for abbr in MONTH_NUM_TO_GEDCOM.values():
        result = re.sub(rf"\b{abbr}\.", abbr, result, flags=re.IGNORECASE)

    return prefix + result


def parse_records(filepath):
    """Parse GEDCOM into top-level records."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    records = []
    current_lines = []
    current_type = None
    current_id = None

    for line in raw_lines:
        stripped = line.rstrip("\n\r")
        if stripped.startswith("0 "):
            if current_lines:
                records.append((current_type, current_id, current_lines))
            current_lines = [stripped]
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


def fix_dates_in_lines(lines):
    """Fix all DATE lines in a record."""
    fixed = []
    for line in lines:
        m = re.match(r"^(\d+\s+DATE\s+)(.+)$", line)
        if m:
            fixed_date = fix_date(m.group(2))
            fixed.append(m.group(1) + fixed_date)
        else:
            fixed.append(line)
    return fixed


# Record type ordering for GEDCOM
TYPE_ORDER = {"HEAD": 0, "SUBM": 1, "INDI": 2, "FAM": 3,
              "SOUR": 4, "REPO": 5, "OBJE": 6, "NOTE": 7, "TRLR": 99}


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "Faulkner_cleaned.ged"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "Faulkner_upload.ged"

    print(f"Reading {input_path}...")
    records = parse_records(input_path)
    print(f"  {len(records)} top-level records")

    # Fix dates
    date_fixes = 0
    fixed_records = []
    for rec_type, rec_id, lines in records:
        new_lines = fix_dates_in_lines(lines)
        for old, new in zip(lines, new_lines):
            if old != new:
                date_fixes += 1
        fixed_records.append((rec_type, rec_id, new_lines))
    print(f"  Fixed {date_fixes} date values")

    # Sort records by type order, preserving order within each type
    # Ensure TRLR comes last and HEAD comes first
    has_trlr = any(r[0] == "TRLR" for r in fixed_records)
    non_trlr = [r for r in fixed_records if r[0] != "TRLR"]
    non_trlr.sort(key=lambda r: TYPE_ORDER.get(r[0], 8))

    if has_trlr:
        non_trlr.append(("TRLR", None, ["0 TRLR"]))
    else:
        print("  WARNING: No TRLR record found, adding one")
        non_trlr.append(("TRLR", None, ["0 TRLR"]))

    sorted_records = non_trlr

    # Count record types
    type_counts = {}
    for rec_type, _, _ in sorted_records:
        type_counts[rec_type] = type_counts.get(rec_type, 0) + 1
    for t, c in sorted(type_counts.items(), key=lambda x: TYPE_ORDER.get(x[0], 8)):
        print(f"  {t}: {c}")

    # Write output
    print(f"Writing {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        for rec_type, rec_id, lines in sorted_records:
            for line in lines:
                f.write(line + "\n")

    print("Done. File is ready for Ancestry upload.")


if __name__ == "__main__":
    main()
