---
type: reference
created: 2026-03-20
updated: 2026-03-20
tags: [genealogy, research, log]
---

# Research Log

Chronological record of every archive searched, every query run, and every result (positive or negative). Negative results are as important as positive ones.

## 2026-03-20: GEDCOM Import from Ancestry.com

### Full Tree Import

**Query**: Import complete family tree from Ancestry.com GEDCOM export
**Source**: Faulkner.ged (Ancestry.com Family Trees, exported 2026-03-19)
**Results**: Imported 2267 individuals across 532 families, covering 619 surnames. After deduplication, reduced from 2,834 to 2267 individuals (567 duplicates removed).
**Implication**: Baseline tree established from Ancestry.com data. All data is Tier 3 (user contributed tree) and needs verification against primary sources. Source citations from Ancestry hints are preserved but the underlying records have not been independently verified.
**Next step**: Run source citation audit (prompt 05) to identify which claims have Ancestry hint sources vs. no sources at all. Then run cross reference audit (prompt 02) to check for internal consistency.

---

## 2026-03-20: Tree Expansion (Prompt 01), Leaf Node Parent Search

### Target 1: Thomas Deacon Parke (b. 1616, Hitcham, Suffolk, England; d. 1709)

**Query**: site:wikitree.com "Thomas Parke" Hitcham Suffolk 1616
**Source**: WikiTree (Parke-8)
**Results**: POSITIVE. Thomas Parke, baptized 13 Feb 1615/6 at Hitcham, Suffolk, son of Robert Parke and Martha Chaplin. Immigrated 1630 with Winthrop Fleet.
**Implication**: Strong Signal. Parents identified with corroboration across WikiTree, Geni.com, Find a Grave, and published genealogy (The American Genealogist, vol. 82, no. 4).
**Next step**: Parents added as Robert_Parke_Sr.md and Martha_Chaplin_Parke.md.

**Query**: "Thomas Parke" parents born 1616 Hitcham Suffolk England deacon
**Source**: WikiTree, Geni.com, Find a Grave (memorial 52710240), steelefamilyhistory.net, werelate.org
**Results**: POSITIVE. All sources consistently identify parents as Robert Parke and Martha Chaplin. Marriage of parents: 9 Feb 1601/2 at Semer, Suffolk.
**Implication**: Corroborated. Published source: Clifford L. Stott, "The Chaplin Family of Co. Suffolk," TAG vol. 82, no. 4 (Oct 2007).

**Query**: site:geni.com "Thomas Parke" Hitcham Suffolk
**Source**: Geni.com (Deacon Thomas Parke of Stonington profile)
**Results**: POSITIVE. Confirms parents Robert Parke Jr and Martha Chaplin. Birth/christening 13 Feb 1614/15 at Hitcham, Suffolk.

---

### Target 2: Peter Garland (b. 1630, Devon, England; d. 1694)

**Query**: site:wikitree.com "Peter Garland" Devon England 1630 Virginia
**Source**: WikiTree (Garland-251, Garland-252)
**Results**: MIXED. Two competing parentages: (A) Ambrose Garland & Thomassin Tackle (WikiTree Garland-251), (B) Peter Garland II & Elizabeth Coles (WikiTree Garland-252, Geni.com). WikiTree notes significant confusion between multiple Peter Garlands.
**Implication**: Speculative. Parentage disputed between sources. Low confidence.
**Next step**: Created Peter_Garland_II_Mariner.md with low confidence. Noted discrepancy.

**Query**: "Peter Garland" parents born 1630 Devon England colonial Virginia
**Source**: Geni.com (multiple profiles), WikiTree, archive.org (Garland Genealogy by James Gray Garland, 1897)
**Results**: MIXED. Geni identifies father as Peter Garland "the Mariner" (b. 1595, Petworth, Sussex) married to Elizabeth Coles. WikiTree disputes this. The Garland Genealogy (1897) identifies Peter as of the Sussex branch.

**Query**: site:geni.com "Peter Garland" "Elizabeth Coles" OR "Ambrose Garland" Devon 1630 Virginia parents
**Source**: Geni.com
**Results**: MIXED. Confirms Peter Garland II married Elizabeth Coles on 3 Oct 1625 at Petworth, Sussex. Identifies 13 children. But the specific connection to the Virginia Peter Garland remains uncertain.

---

### Target 3: Thomas Buckner Sr (b. 13 May 1728, Caroline Co., Virginia; d. 1795)

**Query**: site:wikitree.com "Thomas Buckner" 1728 Caroline Virginia parents
**Source**: WikiTree (Buckner-183, Buckner-1221)
**Results**: POSITIVE. Father identified as John Buckner III (b. abt 1695, d. before 1740). Mother: Elizabeth (surname unknown). John Buckner's will probated 13 Jun 1740, Caroline County VA. Land records show widow Elizabeth divided land between sons William and Thomas in 1750.
**Implication**: Moderate Signal. Father confirmed via will and land records. Mother's maiden name unknown. Disputed by Crozier who claims father was Richard Buckner of Essex.

**Query**: "Thomas Buckner" parents born 1728 Caroline County Virginia
**Source**: WikiTree, Geni.com, FamilySearch, Find a Grave (memorial 190405672), werelate.org
**Results**: MIXED. WikiTree and land records point to John Buckner as father. Crozier's "Buckners of Virginia" (1907) attributes Thomas to Richard Buckner and Elizabeth Cooke. County records support the John Buckner attribution.

**Query**: "John Buckner" father "Thomas Buckner" 1728 Caroline Virginia wife Elizabeth will 1740
**Source**: WikiTree (Buckner-1221), frontierfolk.net
**Results**: POSITIVE. Confirms John Buckner (son of John Buckner and Ann Ballard) received deed of gift 14 Jul 1727 from Ann Buckner for lands formerly belonging to his late father in Essex County.

---

### Target 4: Emanuel Ford Faulkner Sr (b. 1725, Queen Anne's, Maryland; d. 1798)

**Query**: site:wikitree.com "Emanuel Faulkner" OR "Emanuel Forkner" Maryland 1725 parents
**Source**: WikiTree (Faulkner-1843, Faulkner-1064)
**Results**: POSITIVE. Parents identified as John Pleasant Faulkner (b. 1678, Kent County, Maryland) and Sarah Elizabeth Ford (b. 4 Apr 1688, Anne Arundel County, Maryland). John's will mentions Emanuel. Birth year corrected to 1718 (not 1725).
**Implication**: Strong Signal. Will of John Faulkner (d. 1727) mentions son Emanuel. Will of Sarah (Ford) Faulkner (probated 1731) makes provisions for Emanuel.

**Query**: site:geni.com "Emanuel Ford Faulkner" OR "Emanuel Ford Forkner" "John Faulkner" parents Maryland
**Source**: Geni.com
**Results**: POSITIVE. Confirms parents as John Pleasant Faulkner and Sarah Elizabeth Ford. Sarah's will (1731) proven in Queen Anne's County, Maryland. Multiple sibling profiles corroborate.
**Implication**: Parents already existed in vault (John_Pleasant_FalconarForknerFortnerFalknerFalconer_Jr. and Sarah_Elizabeth_Forde_Ford_Falconer_Faulkner). Updated Emanuel_Ford_Faulkner_Sr.md to link to existing parent files.

---

### Target 5: Elizabeth Jordan (b. 9 Nov 1643, Nansemond County, Virginia; d. 9 Nov 1683)

**Query**: "Elizabeth Jordan" parents 1643 Nansemond County Virginia colonial
**Source**: WikiTree (Jordan-863), FamilyCentral, Geni.com
**Results**: TENTATIVE. Some sources identify parents as Thomas Jordan II and Margaret Brasseur. However, many parent-child connections in online family trees remain unsourced and disputed.
**Implication**: Speculative. Low confidence. No primary sources cited for the parent connection.

**Query**: "Elizabeth Jordan" 1643 Nansemond Virginia "Thomas Jordan" "Margaret Brasseur" parents
**Source**: FamilyCentral, Geni.com
**Results**: TENTATIVE. Confirms Thomas Jordan II married Margaret Brasseur about 1658. Elizabeth listed as daughter. Margaret's family were Huguenots. Connection of Thomas II back to Thomas Jordan I is disputed; Samuel Jordan connection disproven by DNA.
**Next step**: Created Thomas_Jordan_II.md and Margaret_Brasseur_Jordan.md with low confidence.

---

### Target 6: Alice (Annis) Peabody (Paybody) (b. 1581, Devon, England; d. 1627)

**Query**: site:wikitree.com "Alice Peabody" OR "Alice Paybody" 1581 Devon England
**Source**: WikiTree
**Results**: NO MATCH. Only result was Alice (Peabody) Holt (1685, Massachusetts), a different person.

**Query**: "Alice Annis" OR "Anice" Paybody OR Peabody 1581 Devon married John Rouse parents
**Source**: WikiTree, Geni.com, Geneanet, bakerfamilyroots.org
**Results**: NEGATIVE for the 1581 individual. The well documented Annis Pabodie who married John Rouse was born about 1618, daughter of John Paybody (b. ~1590, St. Albans, Hertfordshire) and Isabel Harper. The 1581 date appears to be from speculative or user generated family trees that project the colonial family back into earlier English generations without documentary evidence.
**Implication**: The person in the vault (b. 1581) is likely an erroneous back projection. The real Annis Pabodie was born ~1618. No parents found for the 1581 individual because that individual probably did not exist.
**Next step**: No files created. Note discrepancy in Open Questions for future resolution.

---

### Target 7: Thomas Hyscock (b. 1547, Stratford On Avon, Warwickshire, England; d. ~1600)

**Query**: "Thomas Hyscock" OR "Thomas Hiscock" 1547 Stratford Avon Warwickshire parents
**Source**: WikiTree, WeRelate
**Results**: NO MATCH. No results for a Thomas Hyscock/Hiscock from 1547 in Stratford upon Avon. Results only matched 19th century individuals with different locations.
**Implication**: Tudor era records not well represented in online databases. Parish registers for Holy Trinity Church, Stratford upon Avon, might contain records but are not searchable online.
**Next step**: No files created. Would require archival research in Warwickshire County Record Office.

---

### Target 8: John (Darcy) Bourne (b. 1610, London, England; d. 1673)

**Query**: "John Bourne" 1610 London England parents colonial Virginia married Rouse
**Source**: WikiTree, Geni.com, Find a Grave
**Results**: POSITIVE (but for Massachusetts, not Virginia). John Bourne (b. ~1618, d. 1684) of Marshfield, Plymouth Colony, son of Thomas Bourne and Elizabeth (unknown). Married Alice Besbeech 18 Jul 1645 at Marshfield. The Rouse connection was through grandson Thomas Bourne who married Elizabeth Rouse.

**Query**: site:wikitree.com "John Bourne" 1610 Marshfield Plymouth married Alice Bisbee parents
**Source**: WikiTree (Bourne-248)
**Results**: POSITIVE. John Bourne, son of Thomas Bourne and Elizabeth (unknown surname). Origin of family not definitively determined but probably from Kent, England.

**Query**: "Thomas Bourne" 1581 1664 Marshfield Plymouth parents wife Elizabeth "John Bourne" father Kent
**Source**: WikiTree (Bourne-2), Geni.com, stanleyhistory.net
**Results**: POSITIVE. Thomas Bourne (b. 1581, probably Frittenden, Kent; d. 11 May 1664, Marshfield, MA). Deputy from Marshfield to Plymouth General Court. His will names "my son John" as heir and executor.
**Implication**: Moderate Signal. Father Thomas Bourne confirmed via will. Created Thomas_Bourne_Sr.md.

---

### Target 9: Thomas White (b. 22 Mar 1600, Millbrook, Bedfordshire, England; d. 1641)

**Query**: "Thomas White" 1600 Millbrook Bedfordshire parents England
**Source**: WikiTree, FamilySearch, archive.org
**Results**: NO CONFIRMED MATCH. Closest geographic match: Thomas White (bef. 1583, d. 1661) of Hulcote, Bedfordshire (adjacent to Millbrook). Origins unknown per published genealogist Elizabeth French Bartlett. A lengthy unsourced pedigree has been disconnected.
**Implication**: No parents found. The name Thomas White is too common for this era, and no specific Millbrook records are available online.
**Next step**: No files created. Would require research in Bedfordshire parish registers.

---

### Target 10: John Snr Faulkner (b. 1633, Sussex, England; d. 1729)

**Query**: "John Faulkner" 1633 Sussex England parents married Filmer Kent
**Source**: WikiTree (Faulkner-1144, Filmer-52, Filmer-66, Faulkner-1146), Geni.com
**Results**: POSITIVE. Parents identified as William Faulkner (b. 1590, London; d. 1638, Beddingham, Sussex) and Elizabeth Filmer (b. 1592, East Sutton, Kent). Married 6 Feb 1620 at Saint Benet Church, Paul's Wharf, London. John baptized 2 Feb 1633 in Wivelsfield, Sussex. Elizabeth was daughter of Sir Edward Filmer.

**Query**: "William Faulkner" 1590 London "Elizabeth Filmer" East Sutton Kent parents John Faulkner Sussex
**Source**: WikiTree, Geni.com, FamilyTreeCircles, Genealogy Online
**Results**: POSITIVE. William Faulkner was a wealthy draper in London. His father in law Sir Edward Filmer's will named "Elizabeth Faulkner daughter of Dame Elizabeth Filmer and wife of William Faulkner." Multiple sources corroborate.
**Implication**: Strong Signal. Both parents already existed in vault as Sir_William_Faulkner.md and Lady_Elizabeth_Filmer.md. Updated John_Snr_Faulkner.md to link to existing parent files.

---

## 2026-03-20: Find a Grave Sweep (Prompt 03)

### Systematic Search of 20 Deceased Individuals

**Query**: Searched Find a Grave for memorials of 20 deceased persons from the family tree, prioritizing most recent deaths (2019 back to 2000). Used web searches with queries including "Find a Grave" + full name + death year + location, site:findagrave.com + name + dates, and name variations. Multiple query variations tried per individual (2 to 5 searches each).
**Source**: Find a Grave (findagrave.com), via web search indexing. Also incidentally found obituary data on dignitymemorial.com, westvirginia.funeral.com, tyreefuneralhome.com, and alternativefuneralcremation.com.
**Individuals Searched**: Catherine Virginia Anderson (d. 2019), Maggie Kathleen Bolden (d. 2019), Elsie Marie Bowles (d. 2019), Maria Koller (d. 2018), Julia C Hale (d. 2017), Donnie Franklin Bowles (d. 2014), Martha Faulkner (d. 2012), Robert E "Bobby" Hale (d. 2012), Alvin Arnold "Buddy" Hale (d. 2010), Ilean Welch Rice (d. 2010), Rubena Welch (d. 2010), Doney Mae Faulkner (d. 2009), R C Faulkner (d. 2008), Ruth L. Savage Ockerhausen (d. 2008), Lowell Dee Moffett (d. 2005), Lelia Beta Hale (d. 2005), Frances Bernice Gilmore (d. 2005), Arthur Ray Anderson (d. 2004), Clyde C Faulkner (d. 2003), Raymond Lee Faulkner (d. 2000).
**Results**: 1 confirmed Find a Grave memorial found out of 20 searched.
- FOUND: Maggie Kathleen Bolden as "Kathleen Bolden King" (Memorial #203697023), buried at High Knob Cemetery, Iaeger, McDowell County, WV. New data: parents Thomas "Tom" Bolden (1894-1931) and Lydia Steel-Bolden (1889-1975); second marriage to Earl D. King; Pentecostal faith.
- NOT FOUND via web search: 19 individuals. Obituary data found for Donnie Franklin Bowles (burial at Kanawha Valley Memorial Gardens), Robert E "Bobby" Hale (burial at Henry Cemetery, Corinth), and Gracie McKinney Harris (parents Jesse and Amanda McKinney).
**Implication**: The low hit rate (5%) reflects limitations of web search engine indexing of Find a Grave content, not actual memorial coverage. Find a Grave blocks automated access (HTTP 403). Rural areas of McNairy County TN, Alcorn County MS, and WV counties have moderate coverage with documented cemeteries but incomplete individual memorial creation.
**Next step**: Manual search on findagrave.com for all 19 "not found" individuals. Full audit saved to [[findagrave_audit]].

---

## 2026-03-20: DNA Chromosome Analysis (Prompt 12)

### Search for DNA Ancestry Composition Data

**Query**: Searched vault for any DNA ancestry composition data, including CSV/TSV/JSON files, and any files mentioning 23andMe, AncestryDNA, chromosome, haplogroup, admixture, segment, or composition in a genetic context.
**Source**: Full vault search (file names, file contents, all file types)
**Results**: NEGATIVE. No DNA data of any kind found in the vault. One person file (Corp. Richard HAIL/HALE) contains "DNA" in the name field but holds no genetic data. One Research_Log entry mentions DNA ("Samuel Jordan connection disproven by DNA") but no raw data is attached.
**Implication**: Chromosome painting analysis cannot proceed without ancestry composition data. The vault currently contains only documentary genealogical records (GEDCOM import from Ancestry.com, Find a Grave results, and web source cross references). No genetic testing data has been imported.
**Next step**: Obtain a 23andMe Ancestry Composition CSV export or AncestryDNA raw data file. If a parent has also tested, include their kit for deterministic phasing. See [[chromosome_painting]] for detailed data acquisition instructions and the analysis plan for when data becomes available.

---

## 2026-03-20: Open Question Resolution (Prompt 08)

### Systematic Search of 20 Individuals With Unknown Parents

**Query**: Web searches for 20 individuals listed in Open_Questions.md as having vital records but no parent links. Multiple search strategies per individual: name + dates + location + "parents" + "genealogy"; site-specific searches (WikiTree, FamilySearch, Geni.com, Find a Grave); surname + location + broader family context searches.
**Source**: Web search engines indexing WikiTree, FamilySearch, Geni.com, Find a Grave, genealogy.com, rootsweb, thomasandalexanderjoyceassociation.com, dvhh.org, banatbooks.com.

---

### Target 1: Mary Elizabeth Fletcher (b. 1858/1859, Putnam Co., WV)

**Query**: "Mary Elizabeth Fletcher" born 1859 Putnam West Virginia parents genealogy
**Source**: Find a Grave (memorial #40912434), vault duplicate file (Mary_Elizabeth_Fletcher_DL.md)
**Results**: POSITIVE. Parents confirmed as Henry Fletcher (Henry T. Fletcher) and Mary E. Boyer (Mary Melcina Boyer). Find a Grave memorial for Mary Elizabeth Fletcher Joyce (1859-1949), buried at Mount Vernon Cemetery, Hurricane, Putnam County, WV, explicitly names parents. The DL version of her vault file already listed these parents from GEDCOM data.
**Implication**: Strong Signal. Two independent sources (Find a Grave memorial and GEDCOM data in DL file) confirm parentage. Updated Mary_Elizabeth_Fletcher.md to add parent links. Henry T. Fletcher and Mary Melcina Boyer already exist in vault.
**Next step**: Merge duplicate files Mary_Elizabeth_Fletcher.md and Mary_Elizabeth_Fletcher_DL.md.

---

### Target 2: Thomas Joyce (b. ~1803-1811, VA/NC?; d. 15 Jul 1879, Putnam Co., WV)

**Query**: Multiple searches: "Thomas Joyce" born 1811 Putnam Virginia married "Malinda Turner" parents; Thomas Joyce Putnam County Virginia parents Alexander Joyce genealogy; site:genealogy.com Thomas Joyce Putnam Virginia Malinda Turner
**Source**: genealogy.com (Thomas Joyce user tree), thomasandalexanderjoyceassociation.com, rootsweb (Kanawha County project, cwbush/genealogy/joyce.htm)
**Results**: MIXED. Birth year likely ~1803-1805, not 1811 as in vault. Occupation listed as Laborer (1850) and Chair Maker (1870). Census records give contradictory birthplaces across four censuses: VA (1850), PA (1860), NY (1870), NC (death certificate, informant: widow). Family tradition says he came to Putnam County "running from the local sheriff." He is part of the broader Joyce lineage descending from Thomas Joyce (1722-1780) and Alexander Joyce (1719-1778) of Lunenburg County, VA (Scots Irish from County Down, Ireland). However, specific parentage for the Putnam County Thomas Joyce remains unidentified.
**Implication**: Moderate Signal for broader family connection; Speculative for specific parents. The contradictory birthplaces suggest either deliberate evasion or census enumerator errors. A genealogy.com forum post titled "Unknown Joyce, father of Thomas" confirms that his parentage is an active research question in the Joyce genealogy community.
**Next step**: Access original census images for 1850, 1860, 1870 to check household context. Obtain death certificate from Putnam County, WV. Check Stokes County, NC marriage records for 1843 (marriage to Malinda Turner was recorded there, per genealogy.com).

---

### Target 3: Malinda Turner (b. ~1812, VA; d. 9 Dec 1890, Putnam Co., WV)

**Query**: "Malinda Turner" mother "Mary Turner" Virginia Putnam parents genealogy
**Source**: genealogy.com (Thomas Joyce user tree), Geni.com
**Results**: TENTATIVE. One user tree identifies mother as Mary (Unknown) Turner (b. ~1775). Father not identified. A Geni.com profile for Minerva Malinda Turner (b. 1873, Kanawha Co., WV) with parents Obadiah D Turner and Nancy Jane Dent is a different person. No primary source confirmation.
**Implication**: Speculative. Single unsourced user tree claim for mother.
**Next step**: Search Virginia marriage and census records for Turner families with daughter Malinda, b. ~1812.

---

### Target 4: Margaret (b. ~1871, TN)

**Query**: "George Washington Hale" married Margaret 1885 Hardin Tennessee genealogy
**Source**: WikiTree, FamilySearch, Geni.com
**Results**: NEGATIVE for parent identification. However, discovered data quality issue: Margaret and Nancy Catherine McDaniel both listed as spouses of George Washington Hale Jr with identical marriage date (31 Dec 1885, Hardin Co., TN). These are likely the same person or a GEDCOM artifact.
**Implication**: Data cleanup needed. No parent data found.
**Next step**: Access Hardin County, TN marriage records (available from 1864) to verify whether one or two marriages occurred on that date.

---

### Target 5: Ruby D Faulkner (b. ~1917, MS) and Clent B Faulkner (b. ~1919, MS)

**Query**: "Ruby D Faulkner" OR "Clent B Faulkner" 1920 census Hatley Monroe Mississippi parents
**Source**: Web search
**Results**: NEGATIVE. No specific results from web search. Both share the same 1920 census citation (Hatley, Monroe County, MS; Roll T625_886; Page 2A; ED 56), indicating they were in the same household and likely siblings.
**Implication**: Requires subscription database (Ancestry.com or FamilySearch) to view the actual 1920 census image and identify the head of household (likely a parent).
**Next step**: Access 1920 census image directly.

---

### Target 6: Author Faulkner (b. ~1880, TN)

**Query**: "Author Faulkner" OR "Arthur Faulkner" McNairy Tennessee 1880 parents census
**Source**: Web search
**Results**: NEGATIVE. No specific results. "Author" is likely a phonetic census enumerator spelling of "Arthur."
**Implication**: 1930 census (District 5, McNairy, TN; Page 3A; ED 0006) and 1940 census available on subscription databases.
**Next step**: Access census images to identify parents or other household members.

---

### Target 7: May Lee Howell (b. 8 Nov 1888, Monroe Co., MS)

**Query**: "May Lee Howell" Monroe Mississippi 1888 parents genealogy
**Source**: Web search
**Results**: NEGATIVE. No results.
**Implication**: Requires subscription database or county records research.
**Next step**: Search FamilySearch/Ancestry for Howell families in Monroe County, MS in 1900/1910 censuses.

---

### Target 8: Wilhelm Kind (b. 14 Jul 1858, Liebling, Timis, Hungary)

**Query**: "Wilhelm Kind" Liebling Timis Hungary 1858 parents genealogy; Kind family Liebling Banat Donauschwaben genealogy
**Source**: Web search; dvhh.org, banatbooks.com references
**Results**: NEGATIVE for specific parent data. Identified specialized Donauschwaben genealogy resources: Familienbuch for Liebling (if exists), Stefan Stader's Sammelwerk Teil IV (covers surnames Kar through L), matricula-online.eu for Catholic parish registers, and the AKdFF research society.
**Implication**: Banat German genealogy requires specialized resources not indexed by general web search engines. Liebling church records (Catholic) may be available on matricula-online.eu or through the Romanian National Archives in Timisoara.
**Next step**: Check matricula-online.eu for Liebling parish registers. Check banatbooks.com for a Liebling Familienbuch.

---

### Target 9: Ollie Gertrude Watkins (b. May 1890, TN; d. Oct 1981)

**Query**: "Ollie Gertrude Watkins" OR "Ollie Gertrude Faulkner" parents father "W Watkins" Tennessee McNairy
**Source**: Web search
**Results**: NEGATIVE. Vault already lists parents as [[W_Watkins]] (father) and [[J_Watkins]] (mother) but only by initials. Tennessee Death Records (1908-1965) may list full parent names.
**Next step**: Access Tennessee death record for Ollie Gertrude to obtain full parent names.

---

### Target 10: Henry T. Fletcher (b. 1 Dec 1840, VA) and Mary Melcina Boyer (b. 14 Nov 1838, Fayette, VA)

**Query**: "Henry T Fletcher" born 1840 Virginia parents genealogy wife "Mary Melcina Boyer"
**Source**: Web search
**Results**: NEGATIVE. No specific results. Noted GEDCOM error: marriage date listed as 1829, which predates both their births. Find a Grave memorial #40912529 (George Washington Joyce) confirms their daughter's marriage took place "at the home of Henry Fletcher," placing the family in Putnam County, WV.
**Implication**: Marriage date is erroneous and should be corrected (likely 1858-1860 range).
**Next step**: Search Putnam County, WV or Virginia marriage records for Fletcher-Boyer marriage. Check 1850-1860 Virginia census for Fletcher and Boyer families.

---

### Targets 11-16: Lyda Mae Lafon, Holland M Ray, Homer A Anderson, Joel Joseph Griffin, Robert Lee Graham, Rachel Elizabeth Hampton

**Queries**: Individual searches for each person using name, birth year, location, and genealogy terms.
**Source**: Web search, FamilySearch, WikiTree
**Results**: NEGATIVE for all six individuals. No specific parent data found through web searches. Robert Lee Graham appears on FamilySearch with multiple records but no exact match confirmed. Rachel Elizabeth Hampton: multiple Hampton families found but no confirmed connection.
**Implication**: All six require subscription database research (Ancestry.com, FamilySearch direct search) or county-level vital records.
**Next step**: Systematic search on FamilySearch.org for each individual using their known vital data.

---

### Target 17: Nancy Catherine McDaniel (b. 15 Aug 1862, Hardin Co., TN)

**Query**: "Nancy Catherine McDaniel" born 1862 Hardin County Tennessee parents genealogy married Hale
**Source**: Web search
**Results**: NEGATIVE. No results. See Margaret entry above for related data quality issue.
**Next step**: Access Hardin County, TN vital records.

---

### Target 18: Martha Elizabeth Griffin-wilkins

**Query**: "Martha Elizabeth Griffin" Wilkins parents genealogy
**Source**: Web search
**Results**: NEGATIVE. No results.
**Next step**: Check Tishomingo County, MS records (parents Joel Joseph Griffin and Rachel Elizabeth Hampton are from that area).

---

### George Washington Joyce Burial Confirmation (incidental finding)

**Query**: "George Washington Joyce" 1856 Putnam West Virginia parents "Thomas Joyce" "Malinda Turner"
**Source**: Find a Grave (memorial #40912529), genealogy.com
**Results**: POSITIVE. George Washington Joyce (b. 6 Nov 1856, Scott Depot, Putnam Co., WV; d. 12 Jan 1929). Parents: Thomas (Tommy) Joyce and Melinda Turner. Married Mary Elizabeth Fletcher on 15 Feb 1877 at the home of Henry Fletcher. Cause of death: influenza and pneumonia. Buried at Mount Vernon Cemetery, Hurricane, Putnam Co., WV.
**Implication**: Confirms existing vault data for George Washington Joyce's parents. Also provides burial location not previously recorded.

---

## 2026-03-20: Timeline Gap Analysis (Prompt 07)

### Overview

Analyzed 25 priority persons from Family_Tree.md across 9 core family lines (Faulkner, Hale, Bowles, Monroe, Crum, McKinney, Moffett, Welch, Meador). Generated 251 expected life events; 216 OPEN gaps, 29 FOUND, 6 NOT_APPLICABLE. Full results saved to [[timeline_gaps]].

---

### Target 1: Ola Faulkner (b. 1891, Tennessee; d. 20 Jan 1947)

**Query**: "Ola Faulkner" Capooth married Ramer McNairy Tennessee
**Source**: Find a Grave (memorial #80541896, Gillion Marie Capooth Clark)
**Results**: POSITIVE. Ola Faulkner married Edd Capooth and was known as "Ola Faulkner Capooth." Their daughter Gillion Marie Capooth (1920 to 1946) married Johnie D Clark, buried at Olive Hill Church Cemetery, Chewalla, McNairy County, Tennessee.
**Implication**: Moderate Signal. Married name identified via daughter's burial record. Confirms Ramer, McNairy County connection.
**Next step**: Updated Ola_Faulkner.md with spouse and child information. Search for Ola Faulkner Capooth death record in Tennessee death index.

---

### Target 2: Raymond Lee Faulkner (b. 2 Nov 1938, Guys, McNairy Co., TN; d. 4 May 2000)

**Query**: Raymond Lee Faulkner 1938 Guys McNairy County Tennessee obituary death 2000
**Source**: Web search (alternativefuneralcremation.com, legacy.com, deathindexes.com)
**Results**: TENTATIVE. An obituary page exists at alternativefuneralcremation.com (obId=46812610) but the site returned HTTP 403 when fetched. Could not verify content. The 1940 Census source was already in the vault file.
**Implication**: Person file already contains 1940 Census reference. Obituary may exist but could not be accessed.
**Next step**: Manual check of alternativefuneralcremation.com obituary page. Search Tennessee death index at tslaindexes.tn.gov.

---

### Target 3: Joel Harvey Crum (b. 10/9/1841, Scottsburg, Scott, IN; d. 1911)

**Query**: "Joel Harvey Crum" Civil War Indiana; site:wikitree.com "Joel Crum" Scott County Indiana; NPS Civil War soldiers "Joel Crum" Indiana; "Joel Harvey Crum" Shelby County Indiana
**Source**: WikiTree (Crum-1026), shelbycountyindiana.org, NPS Civil War database (via web search)
**Results**: NEGATIVE for this specific individual. Found Joel Crum of Shelby County (b. 1816, Pennsylvania), a different person. Found Harvey Crum Jr. (1847 to 1867) buried in Lorain County, Ohio, also different. No match on NPS Civil War soldier search. No Find a Grave memorial found.
**Implication**: Joel Harvey Crum (b. 1841) does not appear in online indexed sources. May require direct searches on Ancestry.com, FamilySearch, or Fold3 for Indiana Civil War records, or contact with Scott County historical society.
**Next step**: Search Ancestry.com Indiana Civil War Soldier Database Index (1861 to 1865) directly. Check 1870 and 1880 census on FamilySearch for Scott County, Indiana.

---

### Target 4: John Fielden Hale (b. 28 Jun 1847, Grayson County, VA; d. 21 Feb 1928)

**Query**: "John Fielden Hale" 1847 Virginia Alabama Find a Grave; "Fielden Lewis Hale" children sons Grayson Virginia wikitree; "Rufus Marion Hale" Grayson Virginia "Margaret Isom"
**Source**: Find a Grave (memorial #137542862, Fielden Lewis Hale), WikiTree (Hale-614, Hale-5791), New River Notes, vtcrewcat.wordpress.com
**Results**: NEGATIVE for John Fielden Hale specifically. Found extensive documentation on Fielden Lewis Hale (1814 to 1894), Captain of Company D, 29th Virginia Infantry (CSA). His brother Chapman G. Hale married Margaret Isom. The vault file lists John Fielden Hale's mother as "Margaret Isom," suggesting John Fielden Hale may be a son of Chapman G. Hale (not Fielden Lewis Hale or Rufus Marion Hale).
**Implication**: Speculative. The "Fielden" middle name plus the "Margaret Isom" mother strongly suggests a connection to Chapman G. Hale's family. The father listed in the vault ("Rufus Marion Hale") needs verification.
**Next step**: Search 1850 and 1860 census for Chapman G. Hale household in Grayson County, Virginia. Verify whether "Rufus Marion Hale" is a son of Chapman G. Hale.

---

### Target 5: Frances "Fanny" Monroe (b. 14 Apr 1824, New York; d. 1906)

**Query**: "Frances Monroe" 1824 "New York" death 1906 census obituary
**Source**: Web search
**Results**: NEGATIVE. No results returned. Name too common for the era.
**Implication**: Census records (1850 through 1900) should exist but require direct database searches with additional household identifiers.
**Next step**: Search FamilySearch or Ancestry using spouse/household members from Family_Tree.md.

---

### Target 6: Walter Bowles (b. 5 Aug 1884, WV; d. 1937)

**Query**: Walter Bowles 1884 West Virginia 1937 census obituary death
**Source**: Web search (deathindexes.com, WV Division of Culture and History)
**Results**: NEGATIVE. General WV death record portals identified but no specific record found.
**Implication**: WV death records searchable at archive.wvculture.org. Census records (1900 through 1930) should exist.
**Next step**: Search WV Vital Records at archive.wvculture.org. Search FamilySearch for census records.

---

### Target 7: Seldon Welch Sr (b. 12 Feb 1890, Hardin Co., TN; d. 1960)

**Query**: "Seldon Welch" 1890 "Red Sulphur Springs" Tennessee census death 1960
**Source**: Web search
**Results**: NEGATIVE. No results returned.
**Next step**: Search Tennessee State Library death records index. Search FamilySearch for census records.

---

### Target 8: John Otis Moffett (b. 30 Mar 1892, Brinkley, AR; d. 1948)

**Query**: "John Otis Moffett" 1892 Brinkley Arkansas McNairy Tennessee death 1948
**Source**: Web search
**Results**: NEGATIVE. No results returned.
**Next step**: Search FamilySearch for WWI draft registration card. Search census records.

---

### Target 9: Arlie McKinney (b. 10 Jun 1914, Sandstone, WV; d. 1992)

**Query**: "Arlie McKinney" 1914 Sandstone Summers "West Virginia" obituary death 1992
**Source**: Web search
**Results**: NEGATIVE. No results returned.
**Next step**: Search FamilySearch for 1920, 1930, 1940 census and WWII draft card.

---

### Target 10: Remaining Persons (Negative Results Summary)

**Persons searched**: Nancy Rosebelle McKinney (b. 1877, WV), Polly McKinney (b. 1792, NC), James Christian Crum (b. 1797, KY), Joseph Bowles (b. 1795, VA), Grady George Moffett (b. 1921, TN), Evelyn Welch (b. 1921, MS), Melba Louise Moffett (b. 1929, AR), Rubena Welch (b. 1929, MS), Jessie Bowles (b. 1934, WV), Robert E Bobby Hale (b. 1940, MS), Margaret Catherine Faulkner (b. 1942, FL)
**Source**: Web search (various queries per individual)
**Results**: NEGATIVE for all. None produced specific census, vital, or burial records through web search alone.
**Implication**: These individuals require direct searches on FamilySearch.org, Ancestry.com, or Fold3.com, which have digitized census and vital record collections that are not fully indexed by general web search engines.
**Next step**: Prioritize FamilySearch direct searches for 1940 census (fully indexed and free), then 1930 and 1920.

---

### Bulk Search: McNairy County, TN Faulkner Family Census Availability

**Query**: Faulkner family Guys McNairy County Tennessee 1920 1930 census
**Source**: FamilySearch wiki, Ancestry.com, TNGenWeb
**Results**: POSITIVE for general availability. 1920, 1930, and 1940 federal census records for McNairy County are digitized and indexed. Found reference to Eddie Faulkner (1905 to 1933), son of Joseph Marcus Faulkner and Heneritta Climintine Crum Faulkner, in the 1930 census.
**Implication**: Census records for all Faulkner family members in McNairy County should be findable via FamilySearch or Ancestry direct search.
**Next step**: Systematically search each priority Faulkner individual in census records on FamilySearch.

---

## 2026-03-20: Unresolved Persons Audit (Prompt 06)

### Overview

Extracted all named individuals mentioned across 2,274 person files, Family_Tree.md, and the Research Log. Cross referenced against existing person files. Identified 40 unresolved persons: 27 "Likely family," 12 "Community connection," and 1 "Cannot identify." Full results saved to [[unresolved_persons]].

---

### Search 1: Ann Ballard, wife of John Buckner, Virginia

**Query**: Ann Ballard wife John Buckner Virginia colonial 1690s genealogy
**Source**: WikiTree (Ballard-1916, Buckner-129), Geni.com, genealogy.com, ballardofvirginia.com
**Results**: POSITIVE. Ann Ballard (b. ~1686, d. ~1727). Married John Buckner ~1700 in Virginia. Deed dated 17 Jul 1727, Essex Co., in which she gave 500 acres in St. Mary's Parish to son John Buckner Jr. Possible daughter of Thomas Ballard and Katherine Hubbard, but this parentage is marked uncertain on WikiTree. Siblings may include Katherine (Ballard) Buckner, William Ballard Sr, Elizabeth (Ballard) Smith, John Ballard Sr, Robert Ballard.
**Implication**: Moderate Signal. The deed confirms her existence and role. Parents remain disputed.
**Next step**: No person file created. Logged in unresolved_persons.md. Would need Ballard family Bible records or Essex County deed abstracts to confirm parentage.

---

### Search 2: "The Longs," neighbors of Elizabeth Buckner, Caroline County, VA

**Query**: "the Longs" neighbors Elizabeth Buckner Caroline County Virginia 1740s genealogy
**Source**: WikiTree (Buckner-1221, Buckner-1247), buckbd.com (Corrections to Crozier), FamilySearch
**Results**: POSITIVE for land records context. A 6 May 1713 indenture identifies Richard Long of St. Mary's Parish, Essex Co., as a neighbor with land bounding on John Buckner. John Long also named as a neighbor. Elizabeth Buckner's maiden name remains unknown, but the Longs are "leading candidates for her birth family" per WikiTree Buckner-1221. Two widow Elizabeth Buckners may have existed in Caroline Co. simultaneously.
**Implication**: Community connection; possibly family. Not enough evidence to establish a maiden name.
**Next step**: Investigate Caroline County deed books and order books (1728 to 1760) for Long family documents naming Elizabeth.

---

### Search 3: Thomas Jordan III and siblings (sons of Thomas Jordan II)

**Query**: Thomas Jordan III son Thomas Jordan II Nansemond County Virginia Quaker genealogy
**Source**: WikiTree (Jordan-192), Geni.com, Find a Grave (memorial 98348055), Boddie's "Seventeenth Century Isle of Wight, Virginia," Hinshaw's "Encyclopedia of American Quaker Genealogy"
**Results**: POSITIVE. All ten sons identified with birth years, spouses, and death dates. Thomas III (1660/61 to 1759) married Elizabeth Burgh. John (1663 to ~1712) married Margaret Burgh. James (1665/66 to 1732) married Elizabeth Ratcliff, then Anne Roseter. Robert (1668 to 1728) married Christian Taberer, then Mary Belser, then Dorothy Cary. Richard (1670 to 1739) married Rebecca Ratcliff. Joseph (1672 to ~1752) married Holia Christian (Philochristi Akehurst). Benjamin (1674 to 1715/16) married Sarah Ratcliff. Matthew (1676/77 to 1747) married Dorothy Newby, then Susanna Bressie. Samuel (1679 to aft. 1724) married Elizabeth Fleming. Joshua (1681 to 1716/17) married Elizabeth Sanbourne. Two daughters (Elizabeth and Margaret) also recorded.
**Implication**: Strong Signal. Published genealogies (Boddie, Hinshaw) corroborate online databases. All ten sons are siblings of the existing [[Elizabeth_Jordan]] in the vault.
**Next step**: Logged in unresolved_persons.md. Person files recommended as high priority. These would extend the Jordan branch of the tree significantly.

---

### Search 4: Robert Parke Jr and siblings (children of Robert Parke and Martha Chaplin)

**Query**: Robert Parke Jr son Robert Parke Martha Chaplin Winthrop Fleet 1630 Connecticut genealogy
**Source**: WikiTree (Parke-9), Geni.com, archive.org (Genealogy of the Parke Families of Connecticut), TAG vol. 82, no. 4 (2007)
**Results**: POSITIVE. Children identified: Martha Parke (b. ~1603, Semer), Robert Parke Jr (bapt. 4 Jun 1605, Semer), William Parke (bapt. 21 Apr 1607, Semer, d. 11 May 1685, Roxbury; called "oldest son" in father's will; married Martha Holgrave), Thomas Parke (b. 13 Feb 1615/6, Hitcham; already in vault), Anne Parke (bapt. 3 Dec 1618, Hitcham), Samuel Parke (bapt. 20 Jun 1621, Bildeston; named in father's will; married Hannah, surname unknown). Robert Parke's will (14 May 1660, probated 14 Mar 1664/5) mentions only three children: William, Samuel, and Thomas. Robert Jr may have stayed in England.
**Implication**: Strong Signal. Published genealogy and WikiTree agree. William Parke and Samuel Parke have Strong Signal confidence.
**Next step**: Logged in unresolved_persons.md. Person files recommended for William Parke and Samuel Parke as second priority (siblings of [[Thomas_Deacon_Parke]]).

---

### Search 5: Ambrose Garland, Thomassin Tackle, and Peter Garland parentage

**Query**: "Ambrose Garland" "Thomassin Tackle" Peter Garland Virginia genealogy
**Source**: WikiTree (Garland-1079, Garland-251), Geni.com
**Results**: MIXED. WikiTree lists Ambrose Garland (b. ~1601) as husband of Thomassin (Tackle) Garland and father of Peter Garland. Geni.com profile has a note "Do not see evidence for Ambrose Garland & Thomasin Tackle as parents," disconnected in Jun 2015. The alternative lineage (Peter Garland II "the Mariner" and Elizabeth Coles) also exists. WikiTree notes: "Ancestry genealogies have confused Peter the son of Peter and Elizabeth Coles with Peter the son of Ambrose."
**Implication**: Disputed. Low confidence. No primary sources found for either parentage claim.
**Next step**: No action. This dispute cannot be resolved with currently available online sources.

---

### Search 6: Elizabeth Bassenden, wife of Thomas Bourne Sr

**Query**: "Elizabeth Bassenden" OR "Elizabeth Bisbee" wife Thomas Bourne Marshfield Plymouth Massachusetts genealogy
**Source**: stanleyhistory.net (Bourne narrative), Geni.com
**Results**: POSITIVE. Elizabeth Bassenden (b. 1590, Biddenden, Kent; d. 18 Jul 1660, Marshfield, MA). Married Thomas Bourne ~1614. All children born in England. Sons in law: John Bradford (married Martha Bourne), Josiah Winslow (married Margaret Bourne), Robert Waterman (married Elizabeth Bourne), Nehemiah Smith (married Ann Bourne), Nathaniel Tilden (married Lydia Bourne). Thomas Bourne's will (1664) names bequests to all daughters by married names. Connection between Bassenden/Baseden surnames noted: Alice Besbege (daughter in law)'s mother was Anne Baseden of Frittenden, Kent.
**Implication**: Moderate Signal. The stanleyhistory.net narrative is secondary but cites will records. The "Bassenden" surname is speculative per WikiTree Bourne-2 which says "sometimes speculatively given as Bassenden." The Bassenden/Baseden overlap with the Bisbee family is intriguing but unconfirmed.
**Next step**: Logged in unresolved_persons.md. Kent parish registers needed to confirm maiden name.

---

### Search 7: Thomas Bourne's daughters (Martha, Margaret, Elizabeth, Ann, Lydia)

**Query**: Thomas Bourne Marshfield children daughters Martha Bradford Margaret Winslow Elizabeth Waterman Ann Smith Plymouth Colony
**Source**: WikiTree (Bourne-2, Bourne-387, Bourne-1), stanleyhistory.net, minerdescent.com, Find a Grave (memorial 34321698)
**Results**: POSITIVE. All five daughters identified with marriage dates and spouses. Martha married John Bradford (son of Governor William Bradford); later married Thomas Tracy; died 1689 at Norwich, CT. Margaret married Josiah Winslow ~1636; on Marshfield founder's monument. Elizabeth married Robert Waterman 9 Dec 1638; died before father's will. Ann married Nehemiah Smith 21 Jan 1639/40. Lydia married Nathaniel Tilden. Thomas Bourne's will details bequests: daughter Bradford (20 pounds, wife's gold ring), daughter Smith (9 pounds), daughter Winslow (2 cows), son Tilden (5 shillings), granddaughter Lydia Tilden (2 pounds), grandsons Waterman (2 pounds each), minister Mr. Arnold (20 shillings).
**Implication**: Strong Signal. Will records corroborate online databases. Family_Tree.md currently says "and daughters" without naming them.
**Next step**: Logged in unresolved_persons.md. These are not direct ancestors (the line continues through son John Bourne), so person files are lower priority unless tree scope expands to include collateral lines.

---

### Search 8: Alice Chaplin, mother of Robert Parke Sr

**Query**: "Alice Chaplin" mother "Robert Parke" Poslingford Suffolk England genealogy WikiTree
**Source**: WikiTree (Parke-16), TAG vol. 82 no. 4 (Oct 2007), Brouwer Genealogy blog
**Results**: POSITIVE. Alice Chaplin, daughter of William Chaplin of Long Melford, Suffolk. Married Robert Parke 27 Sep 1579 at All Saints, Sudbury, Suffolk. Left land in Acton in her father's will. Her husband Robert Parke of Acton was buried 27 Feb 1592/3 at Acton; will dated 12 Feb 1592/3, proved 3 Apr 1593. Three sons: (1) Robert (b. 3 Jun 1580, the immigrant to New England), (2) Edmund (called second son in will, given land in Gestingthorpe), (3) William (youngest son). Published correction: Robert Parke of Acton is NOT the son of William Parke of Gestingthorpe (previously assumed).
**Implication**: Strong Signal. Published genealogy in The American Genealogist confirms. Alice Chaplin is the paternal grandmother of [[Thomas_Deacon_Parke]].
**Next step**: Logged in unresolved_persons.md. Person file for Alice Chaplin recommended; she extends the Parke line one generation further back.

---

### Search 9: George Coles, Alice Sergeant, and Elizabeth Coles (Garland connection)

**Query**: "George Coles" "Alice Sergeant" parents "Elizabeth Coles" Petworth Sussex England genealogy
**Source**: Geni.com (profiles for Elizabeth Garland and Peter the Mariner Garland)
**Results**: TENTATIVE. Geni.com identifies Elizabeth Coles (b. 1602, Petworth, Sussex; d. 16 Feb 1688, Hampton, NH) as daughter of George Coles and Alice Sergeant. She married Peter Garland II on 3 Oct 1625. However, one profile note states he "married Elizabeth [likely not Coles (daughter of George Coles & Alice Sergeant)]," indicating doubt within the genealogical community.
**Implication**: Speculative. Single source (Geni.com user trees) with noted skepticism. No parish register confirmation found.
**Next step**: No action. Requires Petworth parish registers to confirm.

---

### Search 10: Robert Brasseur, father of Margaret Brasseur Jordan

**Query**: "Robert Brasseur" Huguenot Nansemond Virginia father Margaret Brasseur Jordan genealogy
**Source**: WikiTree (Brasseur-19, Brasseur-39), Geni.com, Find a Grave (memorial 260395126), genealogy.com, martygrant.com
**Results**: POSITIVE. Robert Brasseur (bapt. ~1595, Bouches du Rhone, France; d. ~1659/60, Nansemond Co., VA). French Huguenot. Fled to Isle of Thanet, Kent, England. Five children registered there 1622 to 1632. Arrived Virginia ~1635. Patented 600 acres in Nansemond Co. (1636, 1638). 1,200 acre land grant 12 Apr 1653. Married Florence (surname unknown). Daughter Margaret Brasseur (b. Sep 1642) married Thomas Jordan II and became a Quaker elder. Robert moved family to Maryland ~1658. Debate exists whether the Robert Brasseur of Nansemond and the Robert Brasseur who died in Calvert Co., MD in 1665 are the same person.
**Implication**: Strong Signal for existence and daughter connection. Identity question (one Robert or two) remains open.
**Next step**: Logged in unresolved_persons.md. Person file recommended; would connect Jordan line to Huguenot origins. The two-Roberts question requires Maryland probate records.

---

### Search 11: Long family, Caroline County, VA (Buckner neighbor connection)

**Query**: Long family Caroline County Virginia 1740 1750 neighbors Buckner genealogy
**Source**: WikiTree (Buckner-1221, Buckner-183), buckbd.com, FamilySearch
**Results**: POSITIVE for context. Richard Long and John Long documented as neighbors in St. Mary's Parish, Essex/Caroline Co. Richard Long appears in a 6 May 1713 indenture with land bounding on John Buckner. The Long family frequently witnessed legal documents for Elizabeth Buckner (widow). Leading theory: Elizabeth Buckner was born Elizabeth Long. No documentary proof found.
**Implication**: Moderate Signal for neighborly connection. Speculative for family tie.
**Next step**: Would require Caroline County deed books and order books research (J.F. Dorman, "Caroline County, Virginia Order Book 1732-1740 Part 1").

---

## 2026-03-20: Colonial Records Search (Prompt 10)

### Overview

Identified 787 unique colonial era ancestors (born before 1800) in colonial America across the family tree. Prioritized 10 ancestors for deep record searches across land, probate, military, church, tax, and court record types. Created 9 transcription notes and updated 8 person files.

---

### Target 1: Lewis Burwell I (b. 1621, Ampthill, Bedfordshire; d. 1653, Gloucester Co., VA)

**Query**: Lewis Burwell I land patent Gloucester County Virginia colonial 1640s
**Source**: Encyclopedia Virginia, WikiTree (Burwell-20), Geni.com, Wikipedia (Fairfield Plantation)
**Results**: POSITIVE. Three major land patents: 18 Apr 1648 (2,300 acres, south side York River, with Thomas Vaulx); 12 Jun 1648 (2,350 acres, north side York River, became Fairfield); 1650 (1,600 acres Northumberland County plus 1,000 acres on Potomac). Total: at least 7,250 acres.
**Implication**: Strong Signal. Virginia land patents are primary sources at the Library of Virginia.
**Next step**: Created [[Lewis_Burwell_I_Land_Patents_1648]].

---

### Target 2: Lewis Burwell II (b. 1649/1651, Gloucester Co., VA; d. 19 Dec 1710)

**Query**: Lewis Burwell II will probate Gloucester County Virginia 1710
**Source**: Encyclopedia Virginia, WikiTree (Burwell-20), colonial-settlers-md-va.us, Find a Grave (Memorial 18764228)
**Results**: POSITIVE. Will dated 11 Oct 1710, proved 10 Feb 1710/11 in York County. Names sons Nathaniel, James, Lewis; grandson Lewis (son of Nathaniel); son in law Henry Seaton; daughters Joanna, Elizabeth, Lucy, Martha, Jane, Martha junior; godson William Burwell. Tombstone at Abingdon Church confirms two marriages.
**Implication**: Moderate Signal. GEDCOM birth year (1649) contradicts Encyclopedia Virginia (1651/1652). Mother identified as Lucy Higginson.
**Next step**: Created [[Lewis_Burwell_II_Will_1710]]. Updated person file.

---

### Target 3: William Monroe (b. 1666, Westmoreland Co., VA; d. 30 Mar 1737)

**Query**: William Monroe Westmoreland County Virginia land colonial 1690s will probate
**Source**: WikiTree (Monroe-461), colonial-settlers-md-va.us, Fothergill *Wills of Westmoreland County*
**Results**: POSITIVE. Will recorded 30 Mar 1737, Westmoreland County. Names sons Thomas, George, William, Andrew; daughters Sarah Stone, Mary Stone; grandson Spence (son of Andrew, future father of President James Monroe).

**Query**: Spence Monroe father William Monroe Westmoreland Virginia colonial land records
**Source**: WikiTree (Monroe-431), HMDB, colonial-settlers-md-va.us
**Results**: POSITIVE. Father Andrew Monroe (d. 1668) patented 200 acres 8 Jun 1650 in Northumberland County. Emigrated from Scotland (son of David Munro of Katewell).
**Implication**: Moderate Signal. Father identification corrects GEDCOM (listed as Unknown).
**Next step**: Created [[William_Monroe_Will_1737]] and [[Andrew_Monroe_Land_Patent_1650]]. Updated person file.

---

### Target 4: Thomas Parke, Deacon (b. 13 Feb 1615/16, Hitcham, Suffolk; d. 30 Jul 1709, Preston, CT)

**Query**: Thomas Parke Deacon Stonington Connecticut will probate 1709
**Source**: WikiTree (Parke-8), Geni.com, Ancestry.com Connecticut Wills and Probate Records
**Results**: POSITIVE. Will dated 5 Sep 1707, proved 9 Aug 1709. Found in New London Probate Records vol. A-B, image 226 and Hartford Probate Packets images 606-13. Names wife Dorothy; sons John, Nathaniel, William; grandsons Samuel and James (sons of deceased sons Thomas and Robert); daughters Martha, Dorothy, Alice. GEDCOM listed only one child; will reveals at least seven.
**Implication**: Strong Signal. Original probate records digitized on Ancestry.com.
**Next step**: Created [[Thomas_Parke_Will_1707]]. Updated person file.

---

### Target 5: Henry Clay "The Elder" (b. 3 Aug 1672, Dale Parish, VA; d. 3 Aug 1760)

**Query**: Henry Clay Chesterfield County Virginia colonial land dale parish 1672 1760
**Source**: WikiTree (Clay-84), Geni.com, Find a Grave (Memorial 7711025), FamilySearch
**Results**: POSITIVE. Will signed 28 Mar 1749, probated Sep 1760 at Chesterfield Court. Father identified as Charles Clay (not in GEDCOM). Published in *Adventurers of Purse and Person* (3rd ed., pp. 193-197). Tombstone: "died at dinner with his children and grandchildren at an annual festival."
**Implication**: Moderate Signal. GEDCOM name misleading ("Secretary of State" refers to great grandson Henry Clay the statesman).
**Next step**: Created [[Henry_Clay_Will_1749]]. Updated person file.

---

### Target 6: John Meador (Meadows) Sr. (b. 31 Jul 1658, Charles Parish, York Co., VA; d. 21 Nov 1721)

**Query**: John Meadows Meador probate will Rappahannock Essex County Virginia 1721
**Source**: WikiTree (Meador-3), Geni.com, JEM Genealogy, published genealogies
**Results**: POSITIVE. Will proved ca. 1721 in Essex County. 13 children by two wives: (1) Elizabeth White (d. 1694) and (2) Mary Awbrey. Will divided 450 acre property. Son John Jr.'s nuncupative will (18 May 1720) names William Bourne as executor, establishing Bourne/Meador connection.
**Implication**: Moderate Signal. GEDCOM lists only one child and wrong spouse. Major data discrepancies.
**Next step**: Created [[John_Meador_Sr_Will_1721]]. Updated person file.

---

### Target 7: Thomas Ford, Immigrant (b. 1629, Hindon, Wiltshire; d. ca. 1682, Anne Arundel Co., MD)

**Query**: Thomas Ford immigrant Anne Arundel Maryland colonial land probate 1688
**Source**: Geni.com, WeRelate, Maryland State Archives, Skordas *Early Settlers of Maryland*
**Results**: POSITIVE. Immigration ca. 1650. Servant "Thos Ford" transported before June 1652. Land survey "Fordstone" tract 17 Nov 1659. Estate inventoried ca. Oct 1682. GEDCOM death date (1688) likely incorrect.
**Implication**: Moderate Signal. Land survey and inventory are primary sources.
**Next step**: Created [[Thomas_Ford_Anne_Arundel_Land_Records]]. Updated person file.

---

### Target 8: Edmund Faulkner (b. 1623, Kingsclere, Hampshire; d. 18 Jan 1686/87, Andover, MA)

**Query**: Edmund Faulkner Andover Massachusetts militia King Philip's War 1675 colonial records
**Source**: Internet Archive (Bodge, *Soldiers in King Philip's War*), Academia.edu, devintimber.org
**Results**: MIXED. Edmund confirmed in Andover during King Philip's War; town was attacked. No individual militia roll found in web search. Bodge's *Soldiers in King Philip's War* and Doreski's compilation are best leads for specific service records.
**Implication**: Speculative for military service. Presence confirmed but enrollment not verified.
**Next step**: No transcription note created (insufficient evidence). Would require examination of Bodge's book on Internet Archive.

---

### Target 9: Richard Kirby (b. ca. 1614, Rowington, Warwickshire; d. 21 Jul 1688, Dartmouth, MA)

**Query**: Richard Kirby Sandwich Barnstable Massachusetts colonial church records Quaker
**Source**: Caskey Family genealogy, WikiTree (Kirby-103), Geni.com, WeRelate, HMDB
**Results**: POSITIVE. One of first eleven male church members in Sandwich (1637). On militia list (Aug 1643). Presented for non attendance (1651). Complained against for Quaker meetings (Feb 1657). Fined 57 pounds 12 shillings. Took oath of fidelity 1684 (possibly not formally Quaker). Moved to Dartmouth ca. 1662; land purchases 1670 and 1683.
**Implication**: Strong Signal. Church and court records accessed through secondary compilations. Birth year discrepancy (GEDCOM 1614 vs WikiTree ca. 1603).
**Next step**: Created [[Richard_Kirby_Sandwich_Church_Records]]. Updated person file.

---

### Target 10: Barnabas Arthur (b. 1735/36, Bedford Co., VA; d. bef. 2 Mar 1815)

**Query**: Barnabas Arthur Bedford County Virginia militia Revolutionary War DAR Patriot
**Source**: Genealogy Trails, Virginia SAR, Dunn *Bedford County, Virginia Militia 1774-1783*
**Results**: POSITIVE (partial). "Barnabus Arthur Jr." on Bedford County militia rolls as soldier in Indian/French/British warfare and Revolutionary War. No DAR Patriot Index number found.
**Implication**: Moderate Signal. Militia listing confirmed; specific company and dates need Dunn's book.
**Next step**: Created [[Barnabas_Arthur_Bedford_Militia]]. Updated person file.

---

### Target 11: William Bourne II Land Grant (1719)

**Query**: William Bourne II land grant Louisa County Virginia 1719 Spotswood patent colonial
**Source**: WikiTree (Bourne-559), McCarter Family site, Library of Virginia
**Results**: POSITIVE. Patent 11 Jul 1719 by Lt. Gov. Spotswood. 300 acres on Neck Creek, south of South Anna River. Originally New Kent County, later Hanover (1721), then Louisa (1742). Land in Bourne family for nearly 100 years. Grandsons became Grayson County pioneers.
**Implication**: Strong Signal. Virginia land patents are primary government records.
**Next step**: Created [[William_Bourne_II_Land_Grant_1719]].

---

### Target 12: Stephen Bourne, Tax Records (1780s)

**Query**: Stephen Bourne land Grayson County Virginia colonial tax tithable 1780s
**Source**: Virginia tax list references, New River Notes, Library of Virginia guides
**Results**: NEGATIVE for specific tax listing. Grayson County not formed until 1792. Records under Montgomery or Wythe County. Montgomery County militia list (undated, 1777-1790) includes Stephen Bourn. 1800 deed (Deed Book I, pp. 338-339) for 260 acres on Elk Creek from William to Stephen Bourn.
**Implication**: Negative for 1780s tax records online. Need Montgomery County personal property tax lists at Library of Virginia.
**Next step**: No transcription note created. Key reference: Nuckolls, *Pioneer Settlers of Grayson County* (1914).

---

### Target 13: John Faulkner, Queen Anne's Co., MD (d. 1727)

**Query**: John Faulkner will probate Queen Anne's County Maryland 1708 1729 colonial
**Source**: WikiTree (Faulkner-1064), Geni.com, Maryland State Archives, Findmypast
**Results**: MIXED. Confirmed John Faulkner (b. 1678, Kent Co., MD; d. 1727, Queen Anne's Co.). Children: Temperance, Thomas, Ann, James, Francis. Will exists but text not found online. Maryland Colonial Probate Records available at MSA and Findmypast. Baldwin's *Maryland Calendar of Wills* is key published source.
**Implication**: Moderate Signal for biographical details. Will text needs archival search.
**Next step**: No transcription note. Would need Maryland State Archives digital collection or Findmypast.

---

### Summary of Negative Results

| Ancestor | Record Type Sought | Result |
|---|---|---|
| Stephen Bourne | Tax/tithable lists, 1780s | Grayson Co. not yet formed; need Montgomery Co. records at Library of Virginia |
| Edmund Faulkner | King Philip's War militia roll | Presence in Andover confirmed; individual enrollment not found online; need Bodge's book |
| John Faulkner (MD) | Will text | Will exists per secondary sources; text not found online; need MD State Archives |

---

## 2026-03-20: Immigration Search (Prompt 11)

### Immigrant Inventory

Identified the following categories of immigrants in the family tree:

**Category A: Post-WWII Displaced Persons (Donauschwaben from Liebling, Romania)**
- Friedrich Hedrich (b. 1903, Liebling, Timis, Hungary/Romania; d. 1981, Chicago, IL)
- Philippina Hedrich nee Kind (b. 1906, Liebling; d. 1995, Chicago, IL)
- Friedrich "Fredrich" Hedrich Jr (b. 1927, Liebling, Romania; settled Chicago, IL)
- Maria Koller Hedrich (b. 1929, Liebling, Romania; d. 2018, Kouts, Porter Co., IN)
- Georg Koller (b. 1902, Liebling; d. 1949)
- Elisabetha Koller (b. 1906, Liebling; d. 1993)
- Johann Koller (b. 1896, Liebling; d. 1953, Chicago, IL)
- Elisabetha Koller (b. 1927, Liebling; settled Chicago, IL)

**Category B: Colonial Era (1620s-1660s), England to American Colonies**
- Robert Parke Sr (b. 1580, Suffolk; ship Arbella, Winthrop Fleet 1630; d. 1665, CT)
- Thomas Deacon Parke (b. 1616, Hitcham, Suffolk; Winthrop Fleet 1630; d. 1709, CT)
- Edmund Faulkner (b. ~1623, Kingsclere, Hampshire; ship Joan and Ann 1639; d. 1687, Andover, MA)
- Lewis Burwell (b. 1621, Ampthill, Bedfordshire; arrived Virginia by 1641; d. 1653, Gloucester Co., VA)
- Lady Elizabeth Filmer (b. 1593, Kent; emigrated to Maryland; d. 1662, Kent Co., MD)
- Sir William Faulkner (b. 1590, Kent; emigrated to Maryland; d. 1636, Kent Co., MD)
- William Billings (b. 1602, Taunton, Somerset; d. 1683, Dorchester, MA)
- Thomas Bourne Sr (b. 1581, Frittenden, Kent; arrived Marshfield, Plymouth Colony; d. 1664, MA)
- Thomas C Ford Sr (b. 1629, Hindon, Wiltshire; d. 1688, Anne Arundel, MD)
- Many Faulkner/Falconer/Filmer family members (see family files)

**Category C: Scotch-Irish (early 1700s), Northern Ireland to Virginia**
- Sir Thomas Barnabas Arthur (b. 1658, Cullybackey, County Antrim; d. 1725, Bedford Co., VA)
- Benjamin Arthur (b. 1701, Cullybackey; d. 1783, Bedford Co., VA)
- Thomas Arthur (b. 1705, Antrim; d. 1782, Bedford, VA)
- John Arthur Sr (b. ~1710, Cullybackey; d. 1793, Bedford, VA)
- Henry Arthur (b. 1709, Cullybackey; d. 1793, Bedford, VA)

**Category D: 18th Century German Immigration**
- Johan George Seybold/Seabolt (b. 1752, Stuttgart, Germany; d. 1824, Jefferson Co., KY)
- Elizabeth Seebolt (b. 1762, Germany; d. 1836, Jefferson Co., KY)
- Mary Catherine Ferree (b. 1683, Steinweiler, Germany; d. 1745, PA)

---

### Passenger Manifest Searches

#### Target 1: Hedrich/Koller Family (Liebling, Romania to Chicago, IL)

**Query**: "Friedrich Hedrich" passenger manifest Liebling Romania Chicago immigration
**Source**: Web search (general)
**Results**: NEGATIVE for specific passenger manifest.

**Query**: "Hedrich" "Liebling" passenger manifest ship Ellis Island immigration
**Source**: Web search, Ellis Island Foundation
**Results**: NEGATIVE for direct hit.

**Query**: "Maria Koller" OR "Georg Koller" Liebling Romania passenger manifest immigration Chicago
**Source**: Web search
**Results**: NEGATIVE for specific manifest.

**Query**: "Hedrich" Liebling ship list Banat immigration passenger
**Source**: David Dreyer's Banat Ship List (rootsweb.com/~banatdata)
**Results**: POSITIVE for related Hedrich individuals (pre-WWI):
1. Hedrich Baltasar, age 29, arrived 4 Apr 1929, Winnipeg via Cherbourg/Quebec, ship Carinthia, with wife Elisabeth (21). Mother Maria Hedrich in Liebling.
2. Blum family member, arrived 6 Feb 1907, St. Louis via Bremen/Baltimore, ship Oldenburg, son of Jakob Blum and Barbara Hedrich.
3. Christ family member, arrived 1 Sep 1923, Chicago via Bremen/NY, ship America, sister Magdalena Hedrich in Liebling. Previously in Chicago 1913-1919.
**Implication**: Moderate Signal. Confirms Hedrich emigration from Liebling, including to Chicago before WWII.

**Query**: "Koller" Liebling ship list Banat immigration passenger Dreyer
**Source**: David Dreyer's Banat Ship List
**Results**: POSITIVE for related Koller individuals:
1. Passenger (25), arrived 14 Apr 1929, Winnipeg via Hamburg/Saint John, ship Metagama, with wife Maria (22) and daughter Maria (4). Father: Andreas Koller in Liebling.
2. Passenger (25), arrived 8 Oct 1912, Chicago via Antwerp/NY, ship Finland. Going to join cousin Andreas Koller.
**Implication**: Moderate Signal. Confirms Koller emigration from Liebling to Chicago.

---

#### Target 2: Martin Hedrich Sr (Obituary Discovery)

**Query**: "Martin Hedrich" obituary Liebling Romania Crystal Lake Illinois 1950 family Heisler
**Source**: Legacy.com; Ancestry.com
**Results**: POSITIVE.
1. Martin Hedrich Sr (d. 8 May 2015, age 95, Crystal Lake, IL). Born in Liebling, Romania. Brought family through Austria to US in 1950 via uncles George, John, Jake Heisler. Married Rosina (74 years). Parents: Martin and Phillipine Hedrich.
2. Martin Hedrich (b. 9 Dec 1894, Liebling; son of Martin Hedrich and Maria Geiger; d. 21 Dec 1965, Crystal Lake, McHenry, IL).
**Implication**: Strong Signal for 1950 arrival of Liebling Hedrich families.

---

#### Target 3: Philippina Hedrich Obituary

**Query**: "Philippina Hedrich" obituary Chicago 1995
**Source**: Chicago Tribune (1 Aug 1995)
**Results**: POSITIVE. Age 88. Wife of late Frederich. Mother of Fred (Maria) and Katherina (Stefan) Just. Interment at Rosehill Cemetery.
**Implication**: Strong Signal. Confirms family structure.

---

#### Target 4: Fredrich Hedrich Jr Obituary

**Query**: "Frederick Hedrich" OR "Fred Hedrich" Chicago naturalization immigration Romania 1950s
**Source**: Dignity Memorial
**Results**: POSITIVE. Preceded in death by wife of 69 years, Maria Koller Hedrich. Father of Maria Rink, Betty (Tom) Rogers, Fred Hedrich, Kathrine (Ron) Faulkner, Eric (Katie) Hedrich. Brother of Katarina Just.
**Implication**: Strong Signal. Confirms family structure and Faulkner connection.

---

### Naturalization Record Searches

**Query**: "Friedrich Hedrich" naturalization Illinois Chicago petition
**Source**: Web search
**Results**: NEGATIVE.

**Query**: site:familysearch.org "Illinois, Federal Naturalization Records" Hedrich
**Source**: FamilySearch.org
**Results**: NEGATIVE. Only general wiki page returned.

**Query**: "Elisabetha Koller" OR "Elisabeth Koller" Liebling Banat Romania Chicago naturalization
**Source**: Web search
**Results**: NEGATIVE.

**Query**: "Koller" "Liebling" Banat immigration Chicago naturalization
**Source**: Web search; NARA; Cook County Clerk
**Results**: NEGATIVE for indexed records. Found institutional resources (500,000+ petitions at Cook County, NARA M1285).
**Next step**: Access records via Ancestry.com subscription or in-person at NARA Chicago.

---

### Colonial Era Immigration Searches

#### Robert Parke (Winthrop Fleet, 1630)

**Query**: "Thomas Parke" OR "Robert Parke" 1630 Winthrop Fleet Hitcham Suffolk passenger list ship
**Source**: WikiTree; Geni.com; FamilySearch; Find a Grave; published genealogy
**Results**: POSITIVE. Robert Parke sailed from Cowes, Isle of Wight, 29 March 1630 aboard ship Arbella (Winthrop Fleet). Arrived Boston, MA, 17 June 1630. Served as Secretary to Governor Winthrop.
**Implication**: Strong Signal.

#### Edmund Faulkner (Joan and Ann, 1639)

**Query**: "Edmund Faulkner" 1623 Kingsclere Hampshire England Andover Massachusetts immigration ship
**Source**: WikiTree; Find a Grave; Geni.com; NH Historical Society
**Results**: POSITIVE. Sailed 1639 from England to Salem aboard ship "Joan and Ann." Founding settler of Andover, MA (1644-45). Parents: Richard Faulkner and Joan (Unknown).
**Implication**: Strong Signal.

#### Lewis Burwell (Virginia, ~1641)

**Query**: "Lewis Burwell" 1621 Ampthill Bedfordshire England Virginia immigration ship 1640s
**Source**: Encyclopedia Virginia; WikiTree; Geni.com
**Results**: POSITIVE for immigration, NEGATIVE for ship. Baptized 5 March 1622, Ampthill. In Virginia by January 1641. Stepfather Roger Wingate on governor's Council 1640-1642.
**Implication**: Moderate Signal. No ship name recorded.

#### Arthur Family (Cullybackey, County Antrim to Bedford Co., VA)

**Query**: "Arthur" Cullybackey "County Antrim" Ireland immigration Virginia 1700s ship passenger
**Source**: WikiTree; Ancestry; Wikipedia
**Results**: MIXED. Thomas Barnabas Arthur and John Arthur Sr confirmed. No specific ship or passenger list found.
**Implication**: Moderate Signal for identity; Speculative for ship.

#### Johan George Seybold/Seabolt (Stuttgart to Kentucky)

**Query**: "Johan George Seybold" OR "John George Seabolt" Stuttgart Germany immigration Kentucky
**Source**: Genealogy.com; WikiTree; Ancestry
**Results**: NEGATIVE for specific individual. Found broader pattern: Johannes Seyboldt and Philip Seybolt arrived 21 Oct 1754 at Philadelphia aboard ship "Friendship" from Gosport under Capt. C. Ross.
**Implication**: Speculative for the vault individual. The 1754 arrivals could be relatives.

---

### Charles C Faulkner Passenger List

**Query**: "Charles C Faulkner" passenger manifest New York North Carolina
**Source**: Web search
**Results**: NEGATIVE. No manifest found. Born in NC (1830), died in MS (1897). Ancestry hints for NY passenger lists may be false positive; he appears to be US-born.
**Implication**: Speculative. Ancestry hint needs direct verification.

---

### Contextual: Donauschwaben Community

**Query**: Liebling Banat Donauschwaben families emigration 1944 1950 Chicago
**Source**: Wikipedia; lieblingerchicago.com; dvhh.org; David Dreyer
**Results**: POSITIVE.
1. Lieblinger Verein Chicago (lieblingerchicago.com): active organization of ethnic Germans from Liebling in Chicago area.
2. Donauschwaben displaced beginning 1944, emigrated under DP Act 1948.
3. 393,542 DPs admitted to US by 30 June 1952 cutoff.
4. Citizenship class for Donauschwaben sponsored by Chicago Board of Education in 1956.
**Implication**: Strong Signal for community context.
**Next step**: Contact Lieblinger Verein Chicago. Check dvhh.org immigration index.

---

## 2026-03-20: Local History Extraction (Prompt 09)

### Geographic Cluster Analysis

**Query**: Analyzed Family_Tree.md to identify ancestral families and their geographic origins for local history research.
**Source**: Vault Family_Tree.md (7,500+ lines, 2,267 individuals)
**Results**: POSITIVE. Identified six major geographic clusters:
1. Grayson County, Virginia: Bourne, Hale/Hail/Haile, McKinney, Cornett families
2. Bedford County, Virginia: Arthur, Bowles, Meador/Meadows families
3. Westmoreland County, Virginia: Monroe family (colonial, ancestor of President James Monroe)
4. Kent/Sussex, England: Filmer, Argall families (East Sutton manor)
5. Liebling, Banat (Hungary/Romania): Hedrich, Kind, Koller, Ohlhausen, Schäfer, Roth, Leber, Horwath families (Donauschwaben)
6. Neumagen, Bernkastel-Wittlich, Rheinland-Pfalz, Germany: Klokgieters, Willems, Wintrich, Schue families
**Implication**: No Scandinavian families identified. Focus on American county histories, Central European Ortsfamilienbücher, and English parish histories.

---

### Search 1: Bedford County, Virginia Local History

**Query**: "Bedford County Virginia history biographical sketches" on Google Books, HathiTrust, Archive.org
**Source**: HathiTrust, Archive.org, Library of Congress, Google Books
**Results**: POSITIVE. Found *Historical Sketch of Bedford County, Virginia, 1753-1907* (Lynchburg, VA: J.P. Bell Co., 1907), 121 pages. Available at Archive.org (archive.org/details/historicalsketch00lyn). Public domain. Contains county history but not individual biographical sketches for target families.
**Implication**: The book provides context for Bedford County families but does not contain individual family biographical sketches.
**Next step**: Search for dedicated Bedford County family genealogies.

---

### Search 2: Grayson County, Virginia Local History (Bourne, Hale families)

**Query**: "Grayson County Virginia history genealogy Hale Bourne digitized"
**Source**: Archive.org, HathiTrust, Library of Congress, New River Notes
**Results**: POSITIVE. Found B.F. Nuckolls, *Pioneer Settlers of Grayson County, Virginia* (Bristol, TN: King Printing Co., 1914). Freely available at Archive.org and Library of Congress. Dedicated chapters on Bourne (Ch. II), Hale (Ch. V), and other families. ~4,000 individuals referenced.
**Extracted Data**:
- William Bourne (b. 1743, Louisa County, VA): first clerk of Grayson County court. First court held 21 May 1798 at his house. Son of Stephen and Hannah Bourne of Louisa County.
- Elizabeth Bourne (b. 20 March 1785) married Capt. Lewis Hale. CONFIRMS vault data.
- Frances Bourne (b. 5 June 1788) married Stephen Hale Sr. CONFIRMS vault birth date; identifies parents (previously Unknown).
- Capt. Peyton N. Hale commanded "Dare Devil Company." Killed at First Manassas, 21 July 1861. CONFIRMS vault death date.
**Cross-reference**: 3 confirmations, 1 new parent identification, 1 discrepancy flagged (Stephen BOURNE death date).
**Files Updated**: [[William_F_Bourne_Sr]], [[Elizabeth_Bourne]], [[Frances_Rosamond_Rosa_Bourne_-_Hale_1]], [[Peyton_Nathan_Hale]], [[Stephen_BOURNE]]

---

### Search 3: Westmoreland County, Virginia (Monroe family)

**Query**: "Westmoreland County Virginia Monroe family colonial history William Monroe 1666 wills"
**Source**: WikiTree, colonial-settlers-md-va.us, Geni.com, published sources
**Results**: POSITIVE. William Monroe I will found in *Westmoreland County, Virginia Wills 1654-1800*, p. 102. Details bequests, gentleman status, second marriage to Susanna White. Father: Capt. Andrew Monroe, emigrated from Scotland 1650.
**Cross-reference**: Birth/death dates confirmed. New will details and second marriage documented.
**Files Updated**: [[William_Line_to_pres_Monroe_6th_Gt_Monroe]]

---

### Search 4: Liebling, Banat (Hedrich, Kind, Koller families)

**Query**: "Liebling Banat Ortsfamilienbuch Hedrich Kind Koller"
**Source**: GenWiki, AKdFF, banatbooks.com, Dreyer Database
**Results**: POSITIVE for source identification; PARTIAL for data extraction.
**Key Sources**: Möhler, *Ortssippenbuch Liebling im Banat* (1979), 836pp, 6,303 families. Arnold, *Lieblinger Familienbuch* (1994/2001 CD-ROM). Neither freely digitized online.
**Emigration Data (Dreyer Database)**: Hedrich Baltasar (1929, to Winnipeg); Koller emigration to Chicago (1903, 1912).
**Files Updated**: [[Martin_Hedrich_1846]], [[Johann_Koller]]
**Next step**: Request lookups from St. Louis County Library for Hedrich, Kind, Koller in Möhler 1979.

---

### Search 5: Neumagen, Rheinland-Pfalz (Willems, Klokgieters families)

**Query**: "Neumagen Bernkastel kirchenbuch familienbuch Willems Klokgieters Wintrich"
**Source**: GenWiki, Archion.de, Bistumsarchiv Trier, WGfF Köln
**Results**: PARTIAL. Identified Wagner, *Familienbuch Pfarrei St. Stephanus Wintrich* (1990), 1607-1858. Bistumsarchiv Trier holds Neumagen parish records. Archion.de subscription required.
**Next step**: Check Archion.de or request lookups from Bistumsarchiv Trier.

---

### Search 6: East Sutton, Kent, England (Filmer, Argall families)

**Query**: "Hasted Kent East Sutton Filmer Argall genealogy"
**Source**: Hasted, *History and Topographical Survey of the County of Kent*, vol. 5 (1798); British History Online; WikiTree; Allen (2005)
**Results**: POSITIVE. Detailed Filmer/Argall descent from published parish history. Major Henry Filmer: Burgess for James City County 1642-43, Justice of Warwick 1647, plantation "Laus Deo" on Mulberry Island.
**Files Updated**: [[Major_Henry_Filmer]]

---

### Search 7: McNairy County, Tennessee (Faulkner, Hale families)

**Query**: "McNairy County Tennessee history biographical Faulkner Hale genealogy digitized"
**Source**: TNGenWeb, Tennessee State Library, FamilySearch
**Results**: PARTIAL. Identified Goodspeed, *History of Tennessee: Henderson, Chester, McNairy, Decatur, Hardin Counties* (1887), pp. 819-880. 168 biographical sketches. Could not access full text for McNairy section.
**Next step**: Search FamilySearch Digital Library; check TNGenWeb transcriptions.

---

### Search 8: Summers County, West Virginia (Meador/Meadows families)

**Query**: "Summers County West Virginia history McKinney Basham Meador genealogy"
**Source**: Miller, *History of Summers County, West Virginia* (1908), pp. 403-404
**Results**: POSITIVE. Josiah Meador: first settler, wife Juda Lilly, Revolutionary War service with Clark's Illinois expedition, founded Bluestone Baptist Church 1798.
**DISCREPANCY**: Vault lists wife as [[Lavina_LILLY_MOODY_Meador]]; Miller identifies her as "Juda Lilly."
**Files Updated**: [[Josiah_Francis_Meadows_Sr]]

---

### Negative Results

**Scandinavian sources**: NOT APPLICABLE. No Scandinavian families in vault.
**Matricula Online / GenTeam.at for Liebling**: NEGATIVE. Liebling parish records not on these platforms; held at Bistumsarchiv Temeswar or local parish.

---

## Logging Convention

Every search gets logged, positive or negative. Use this format:

- **Date**: When the search was performed
- **Query**: Exact search terms (so you can avoid repeating the same search)
- **Source**: The database, website, or archive
- **Results**: What was found. "No results" is a valid and important entry.
- **Implication**: What the result (or lack thereof) means for the research
- **Next step**: What to do next based on this result
