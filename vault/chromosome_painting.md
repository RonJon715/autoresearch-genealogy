---
type: reference
created: 2026-03-20
updated: 2026-03-20
tags: [genealogy, dna, chromosome, negative-result]
---

# Chromosome Painting Analysis

## Status: No DNA Data Available

Searched the entire vault on 2026-03-20 for DNA ancestry composition data. No chromosome painting, ancestry composition CSV, segment data, or raw genotype files were found. This is a negative result.

### What Was Searched

| Search Target | Result |
|---|---|
| CSV, TSV, or JSON data files in vault | None found |
| Files mentioning "23andMe" | None found |
| Files mentioning "AncestryDNA" | None found |
| Files mentioning "chromosome" or "segment" | None found |
| Files mentioning "haplogroup" or "admixture" | None found |
| Files mentioning "composition" (genetic context) | None found |
| Files with "DNA" in filename or content | One person file (Corp. Richard HAIL/HALE) has "DNA" in the name field, but contains no genetic data |
| Research_Log.md mention of DNA | One mention: Samuel Jordan connection "disproven by DNA" (no raw data attached) |

## Data Needed for Chromosome Analysis

To perform per chromosome ancestry composition analysis, the following data would be required:

### Primary Data (Required)

1. **23andMe Ancestry Composition CSV**: Available from 23andMe account under Tools > Browse Raw Data > Download. The "Ancestry Composition" chromosome painting file provides per segment ancestry assignments with start/end positions and confidence levels. File format: CSV with columns for chromosome number, start position, end position, ancestry label, and confidence score.

2. **AncestryDNA Ethnicity Estimate Data**: AncestryDNA provides ethnicity estimates but does not offer a per chromosome, per segment download in the same format as 23andMe. The raw DNA download from AncestryDNA is a genotype file (SNP level), not a chromosome painting file. Third party tools (e.g., DNA Painter, GEDmatch) can generate segment level ancestry assignments from AncestryDNA raw data.

### Supplementary Data (Recommended)

3. **Parent DNA kits**: If either parent has tested, phasing becomes deterministic rather than statistical. Without parent DNA, assigning Copy 1 vs. Copy 2 to maternal vs. paternal is probabilistic and requires inference from known ancestry lines. Always note this uncertainty.

4. **Known cousin matches with shared segments**: Shared segment data from DNA relatives can help confirm which chromosome copies are maternal vs. paternal.

5. **X chromosome data**: For a male subject, the X chromosome is inherited entirely from the mother, making it a clean reference point for maternal ancestry assignment. For a female subject, one X copy is maternal and one is paternal, requiring phasing.

### How to Export from 23andMe

1. Log in to 23andMe.com
2. Navigate to Ancestry > Ancestry Composition
3. Select "Scientific Details" or "Chromosome Painting"
4. Click the download/export option for the chromosome level data
5. Save the CSV file to the vault directory

### How to Use AncestryDNA Raw Data

1. Log in to AncestryDNA
2. Go to Settings > Download Raw DNA Data
3. Download the ZIP file containing the raw genotype data
4. Upload to GEDmatch or DNA Painter for segment level ancestry analysis
5. Export the resulting chromosome painting data

## Analysis Plan (For When Data Becomes Available)

Once ancestry composition data is obtained, the analysis would proceed as follows:

1. **X Chromosome First**: If the subject is male, the X chromosome is 100% maternal, providing an anchor for maternal ancestry identification.
2. **Identify Clean Separations**: Look for chromosomes where Copy 1 and Copy 2 show clearly different ancestry compositions (e.g., one copy predominantly British/Irish, the other predominantly German/French).
3. **Build Assignment Table**: For each chromosome, record the dominant ancestry per copy, the likely parent of origin, and a confidence tier.
4. **Map to Documented Lines**: Cross reference the ancestry assignments with known ancestor origins from [[Family_Tree]].
5. **Document Uncertainty**: Without parent DNA, copy assignment is probabilistic. Segments smaller than 5 cM should not be over interpreted. Genetic ancestry categories do not map directly to ethnic or national identity.

## Confidence Note

All chromosome painting analyses without parental phasing carry inherent uncertainty. Statistical phasing algorithms assign copy 1 vs. copy 2 with varying accuracy depending on population reference panels and segment size. Conclusions should be treated as Moderate Signal at best until confirmed with parent or close relative DNA data.

## Related Files

- [[Family_Tree]]
- [[Research_Log]]
- [[Open_Questions]]
