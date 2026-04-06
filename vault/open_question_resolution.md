---
type: audit
created: 2026-04-06
tags: [genealogy, research, open-questions]
---

# Open Question Resolution (2026-04-06 Research Pass)

Follow up research on questions 4 through 7 from [[Open_Questions]], the high solvability items discovered during the 2026-03-20 import pass.

---

## Question 4: Margaret / Nancy Catherine McDaniel Duplicate Spouse

**Status change**: OPEN to PARTIALLY RESOLVED

**Summary**: [[Margaret]] (b. ~1871) and [[Nancy_Catherine_McDaniel]] (b. 1862) are both recorded as spouses of [[George_Washington_Hale_Jr]] with the same marriage date of 31 Dec 1885 in Hardin County, TN.

**Evidence found**: A Find a Grave memorial (memorial #90237821) records a George W. Hale (b. 15 Aug 1863, d. 15 Jun 1944) buried in Crump, Hardin County, Tennessee. This individual aligns with George Washington Hale Jr in the vault by county and approximate birth year. No separate marriage record for a "Margaret" distinct from Nancy Catherine McDaniel was located in any online index of Hardin County marriages. The identical marriage date (31 Dec 1885) for both entries strongly suggests a GEDCOM import artifact: "Margaret" is most likely either a first or middle name associated with Nancy Catherine McDaniel, or a duplicate record created during data entry.

**Recommendation**: Treat Margaret and Nancy Catherine McDaniel as the same individual until a Hardin County marriage record proves otherwise. The vault entry for [[Margaret]] should be flagged as a probable duplicate of [[Nancy_Catherine_McDaniel]]. Confirmation requires pulling the original marriage register from the Hardin County Clerk's office (records available from 1864 onward).

**Sources**:
- [George W. Hale, Find a Grave memorial #90237821](https://www.findagrave.com/memorial/90237821/george-w_-hale)
- [Hardin County, Tennessee Genealogy, FamilySearch Wiki](https://www.familysearch.org/en/wiki/Hardin_County,_Tennessee_Genealogy)

**Confidence**: Moderate Signal (duplicate is the most parsimonious explanation, but no direct marriage record was accessed)

---

## Question 5: Henry T. Fletcher / Mary Melcina Boyer Marriage Date Error

**Status change**: OPEN to RESOLVED (data error confirmed)

**Summary**: The GEDCOM lists a marriage date of 1829 in Birmingham, Warwickshire, England. Henry T. Fletcher was born 1 Dec 1840 (some records say 28 Dec 1834) and Mary Melcina Boyer was born 14 Nov 1838. A marriage in 1829 is impossible for both individuals.

**Evidence found**: A Find a Grave memorial (#41740058) for Henry T Fletcher records his life as 1834 to 1907, with burial at Mount Vernon Cemetery in Hurricane, Putnam County, West Virginia. His wife is listed as Mary M. Fletcher. Their daughter [[Mary_Elizabeth_Fletcher]] (Find a Grave memorial #40912434) married George Washington Joyce on 15 Feb 1877 in Putnam County, WV, and her parents are recorded as Henry Fletcher and Mary E. Boyer. Given that Henry was born no earlier than 1834 and Mary Melcina Boyer was born in 1838, the marriage likely occurred in the late 1850s or early 1860s in Virginia (pre statehood) or West Virginia. The "1829, Birmingham, England" entry is a GEDCOM error, possibly a data entry transposition or a record belonging to a different Henry Fletcher entirely.

**Recommendation**: Remove the 1829 Birmingham marriage date from both [[Henry_T._FLETCHER]] and [[Mary_Melcina_Boyer]]. Replace with "abt. 1858 to 1863, Virginia or Putnam County, WV (estimated)" and flag the date as requiring confirmation from Putnam County marriage records.

**Sources**:
- [Henry T Fletcher, Find a Grave memorial #41740058](https://www.findagrave.com/memorial/41740058/henry-t-fletcher)
- [Mary Elizabeth Fletcher Joyce, Find a Grave memorial #40912434](https://www.findagrave.com/memorial/40912434/mary-elizabeth-joyce)
- [Putnam County, West Virginia Genealogy, FamilySearch Wiki](https://www.familysearch.org/en/wiki/Putnam_County,_West_Virginia_Genealogy)

**Confidence**: Strong Signal (the 1829 date is demonstrably impossible; the marriage occurred after both parties were born, likely late 1850s or early 1860s)

---

## Question 6: Mary Elizabeth Fletcher Duplicate Files

**Status change**: OPEN to RESOLVED

**Summary**: Two vault files exist for the same individual: [[Mary_Elizabeth_Fletcher]] (b. 5 Oct 1858) and [[Mary_Elizabeth_Fletcher_DL]] (b. 05 Oct 1859). Both are recorded as wife of [[George_Washington_JoiceJoyce]].

**Evidence found**: This is an internal data quality issue confirmed by inspecting the vault. Both files exist at `vault/Fletcher/Mary_Elizabeth_Fletcher.md` and `vault/Fletcher/Mary_Elizabeth_Fletcher_DL.md`. The DL variant contained parent links (Henry T. Fletcher and Mary Melcina Boyer) that have since been added to the primary file as well. The one year birth date discrepancy (1858 vs 1859) is a minor transcription variance common in 19th century records.

**Recommendation**: Merge the two files into a single [[Mary_Elizabeth_Fletcher]] entry. Use 5 Oct 1858 as the primary birth date (consistent with the Find a Grave memorial #40912434 which lists 1859; retain both dates as variants). Transfer any unique data from the DL file into the primary file, then delete or redirect [[Mary_Elizabeth_Fletcher_DL]].

**Sources**:
- Internal vault inspection (2026-04-06)
- [Mary Elizabeth Fletcher Joyce, Find a Grave memorial #40912434](https://www.findagrave.com/memorial/40912434/mary-elizabeth-joyce)

**Confidence**: Strong Signal (same individual confirmed by shared spouse, parents, and overlapping birth dates)

---

## Question 7: Thomas Joyce Birth Year and Birthplace Discrepancy

**Status change**: OPEN to PARTIALLY RESOLVED

**Summary**: The vault records Thomas Joyce as born 28 Jan 1811, Putnam, West Virginia. External genealogy sources say ~1803 to 1805. Census records across four decades give four different birthplaces: Virginia (1850), Pennsylvania (1860), New York (1870), and North Carolina (death certificate).

**Evidence found**: The Thomas and Alexander Joyce Association website documents the broader Joyce family as Scots Irish emigrants from Ballynahinch, County Down, Ireland, who settled in Lunenburg County, Virginia around 1735. A Genealogy.com user tree ("Thomas-Joyce") records Thomas (Tommy) Joyce as born about 1805, died 15 Jul 1879, Putnam County, WV, married to Melinda (Malinda) Turner. The death date of 1879 is consistent with his absence from the 1880 census. A Rootsweb Kanawha County project page corroborates these dates.

Regarding the birthplace conflict: the 1850 census (Virginia) is the earliest and most likely accurate, since Putnam County was part of Virginia at that time and the broader Joyce family had deep roots in colonial Virginia. The Pennsylvania and New York entries in later censuses are almost certainly enumerator errors or miscommunication. The death certificate listing North Carolina may reflect family oral tradition about an earlier Joyce migration through the Carolinas (the colonial Joyces did move through North Carolina). The vault birth year of 1811 appears to be unsourced and should be replaced with "abt. 1803 to 1805" per the Genealogy.com tree and census age calculations.

**Recommendation**: Update [[Thomas_Joyce]] birth year to "abt. 1803 to 1805." Change birthplace to "Virginia (likely)" with a note documenting the conflicting census entries. Add death date of 15 Jul 1879, Putnam County, WV. Flag the 28 Jan 1811 date as unsourced and superseded. Confirmation would require the original Putnam County death certificate or a pre 1850 record.

**Sources**:
- [Thomas-Joyce user tree, Genealogy.com](https://www.genealogy.com/ftm/j/o/y/Thomas-Joyce/BOOK-0001/0004-0001.html)
- [Thomas and Alexander Joyce Association, Documentation](https://www.thomasandalexanderjoyceassociation.com/documentation)
- [Thomas and Alexander Joyce Association, Family Trees](https://www.thomasandalexanderjoyceassociation.com/family-trees)
- [Thomas Joyce, MyHeritage](https://www.myheritage.com/names/thomas_joyce)

**Confidence**: Moderate Signal (birth year of ~1803 to 1805 is better supported than 1811, but no primary source has been accessed; birthplace of Virginia is the strongest single answer but remains unconfirmed by a primary document)

---

## Remaining OPEN Questions (Subscription Database Access Required)

The following questions from [[Open_Questions]] remain OPEN. Web searches during both the 2026-03-20 and 2026-04-06 research passes returned no actionable results for these individuals. Resolution requires subscription database access (Ancestry.com, FamilySearch indexed records) or direct contact with county archives.

| Individual | Location | Needed Resource |
|---|---|---|
| [[Ruby_D_Faulkner]] | Hatley, Monroe Co., MS | 1920 census (Ancestry.com, Roll T625_886) |
| [[Clent_B_Faulkner]] | Hatley, Monroe Co., MS | Same 1920 census record as Ruby |
| [[May_Lee_Howell]] | Monroe Co., MS | Subscription database research |
| [[Ollie_Gertrude_Watkins]] | McNairy Co., TN | Tennessee Death Records 1908 to 1965 |
| [[Martha_Elizabeth_Griffin-wilkins]] | Unknown | Subscription database research |
| [[Author_Faulkner]] | McNairy Co., TN | 1930/1940 census (Ancestry.com) |
| [[Henry_T._FLETCHER]] (parents) | Virginia | Virginia vital records, census research |
| [[Mary_Melcina_Boyer]] (parents) | Fayette, Virginia | Virginia vital records |
| [[Lyda_Mae_Lafon]] | Pearisburg, Giles Co., VA | Giles County vital records |
| [[Holland_M_Ray]] | Red Sulphur, Monroe Co., WV | 1950 census (Roll 3504) |
| [[Homer_A_Anderson]] | Mississippi | 1930 census (Ancestry.com) |
| [[Joel_Joseph_JJ_Griffin_Corp.]] | Anson Co., NC | Civil War service records, county vital records |
| [[Robert_Lee_GRAHAM]] | Wyoming, WV | FamilySearch/Ancestry direct search |
| [[Rachel_Elizabeth_Hampton]] | Tishomingo, MS | Mississippi vital records |
| [[Wilhelm_Kind]] | Liebling, Timis, Hungary | Donauschwaben Familienbuch, dvhh.org, matricula-online.eu |
| Hedrich/Koller immigration | Chicago, IL | Ancestry.com Illinois naturalization records, NARA M1285 |
| [[Charles_C_Faulkner]] passenger list | New York | Ancestry.com hint verification (NARA M237) |
| [[Johan_George_Seybold]] immigration | Philadelphia | Philadelphia passenger records 1770s to 1780s |
