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

## Logging Convention

Every search gets logged, positive or negative. Use this format:

- **Date**: When the search was performed
- **Query**: Exact search terms (so you can avoid repeating the same search)
- **Source**: The database, website, or archive
- **Results**: What was found. "No results" is a valid and important entry.
- **Implication**: What the result (or lack thereof) means for the research
- **Next step**: What to do next based on this result
