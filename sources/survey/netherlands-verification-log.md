# Netherlands verification log (2026-11-19)

Second pass over every "n/f" in `netherlands-fhir.md` and `netherlands-landscape.md`. Method: Dutch and English web searches, direct curl of organisation pages and PDFs (pdftotext), CORDIS project pages, the SNOMED Confluence REST API, the OECI accreditation directory. Downloads in `scratchpad/nl-verify/` (own directory; no interpreter run from inside it). Both files were edited in place; new facts carry "(verified 2026-11-19)".

Totals: 15 VERIFIED, 7 CORRECTED, 14 STILL NOT FOUND.

## VERIFIED (fact now in the files)
1. Ardon Toonstra is a Firely FHIR consultant (MedMij profiles, Simplifier support), not Nictiz staff. https://simplifier.net/user/ardon
2. No zib "Tumorkenmerken": ZIB Publicatie 2024(NL) lists only TNMTumorClassificatie-v4.1 among the 15 scores/value lists; prepublication 2026-1 (20 April 2026) repeats it. https://www.zibs.nl/wiki/ZIB_Publicatie_2024(NL)
3. No Nictiz "Verwijzing oncologie"/"MDO oncologie" standard: the Nictiz wiki index of current standards has no oncology entry beyond the third-party screening programmes and the Labcodeset. https://informatiestandaarden.nictiz.nl/wiki/Hoofdpagina
4. ICD-O is not on the Nationale Terminologieserver: the NTS manual lists licence-free (ICD-10, HPO, HGNC, ART-DECOR) and licensed (SNOMED CT, LOINC, NHG-tabellen, Labcodeset) content only. https://nictiz.nl/app/uploads/2024/07/NTS-Handleiding-voor-nieuwe-gebruikers-12-03-2024.pdf
5. No Dutch ICD-O-3.2 translation: WHO-FIC NL offers ICD-O-3.2 (15-11-2019) as English xls; the Dutch-language ICD-O-3 is the Flemish translation. https://www.whofic.nl/downloads-en-links/icd-o-3
6. Nictiz directeur-bestuurder: Leonique Niessen (since 1 January 2021; confirmed April 2025). https://nictiz.nl/app/uploads/2025/04/ICThealth_nr2_2025_74-75_Werelden-verbinden-Leonique.pdf
7. Registratie aan de bron ended 14 April 2022; tools moved to Nictiz Amigo. https://www.registratieaandebron.nl/
8. UMC Utrecht, Amsterdam UMC, LUMC, Prinses Máxima Centrum and Radboudumc are not on the OECI certified-centres list (Radboudumc is "In Accreditation"). https://accreditation.oeci.eu/ ; https://accreditation.oeci.eu/certified-centres/
9. IDEA4RC: 1 Sep 2022 to 31 Aug 2026 (closed), EUR 8,190,468. https://cordis.europa.eu/project/id/101057048
10. STRONG-AYA: 1 Oct 2022 to 30 Sep 2027, total EUR 7,292,902.50, EU EUR 7,235,023. https://cordis.europa.eu/project/id/101057482
11. CANDLE: Horizon Europe GA 101214368, EUR 2,999,547.50, 2025-2028, Health-RI coordinator, 40 organisations. https://cordis.europa.eu/projects/101214368 ; https://eatris.eu/?p=43123
12. ECHoS GA 101104587, EUR 6,096,147.50, Apr 2023 to Mar 2026; ECHoS 2 EUR 15,079,639.52, Jul 2026 to Jun 2031; NKC Hub is the Dutch mission hub. https://cordis.europa.eu/project/id/101104587 ; https://eatris.eu/?p=45014
13. TEHDAS2 Dutch partners RIVM and Nictiz https://tehdas.eu/partners/ ; JANE-2 (GA 101183265, Nov 2024 to Oct 2028) Dutch partners VWS, UMCG, IKNL, NKI-AVL per RSU list https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/ ; CraNE had no Dutch partner https://crane4health.eu/partners/
14. KWF YIG 2027: pre-proposals closed 6 Oct 2026, full proposals close 1 April 2027; FORCE joint call closed 22 Sep 2026 (EUR 5 million); PIPELINE 2027 full proposals opened 13 Oct 2026. https://www.kwf.nl/en/forresearchers/funding/young-investigator-grant-yig-call-2027 ; https://www.kwf.nl/calls
15. KWF has no 2026/2027 infrastructure call on its calls page (absence confirmed). https://www.kwf.nl/calls

## CORRECTED (old vs new)
1. IKNL leadership. Old: Thijs Merkx sole board member. New: since the 1 Jan 2026 governance merger the DICA-IKNL board is chaired by prof. dr. Ernst Kuipers (from 1 May 2026), with Bente Jorritsma (vice-chair) and Suzanne Verboort; supervisory board chair Marlies van Elst; Merkx has left IKNL. https://dica.nl/over-ons/ ; https://www.oncologie.nu/nieuws/fusieorganisatie-dica-iknl-kiest-voor-ernst-kuipers/
2. OECI accreditation. Old: Erasmus MC and Radboudumc status unknown, only NKI, MUMC+, UMCG confirmed. New (live site read by the team lead in a browser on 2026-11-19, https://accreditation.oeci.eu/ , saved at scratchpad/verify/oeci-centres-2026-11-19.txt): six certified Dutch centres, Erasmus MC Cancer Institute, Maastricht UMC+, Netherlands Cancer Institute, OncoZON Cancer Network, Rijnstate, UMCG CCC. Radboudumc is not certified; the directory page lists it under "In Accreditation" (https://accreditation.oeci.eu/certified-centres/). Designation types from the directory: NKI, Erasmus MC, UMCG-CCC, MUMC+ = CCC with Research Excellence; Rijnstate = CCC; OncoZON = Comprehensive Cancer Network.
3. EUCAIM. Old: only Erasmus MC confirmed. New: nine Dutch partners (Amsterdam UMC, EATRIS, Erasmus MC, Health-RI, Maastricht University, Philips, Radboudumc, EGI Foundation, NKI). https://cancerimage.eu/partners/
4. SNOMED CT NL. Old: latest notes June 2026. New: August (20260831), September (20260930) and October 2026 (20261031; 34 new NL concepts, 298,826 translated active concepts) release notes exist. https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/1436188716
5. CancerWatch. Old: budget n/f, 92 organisations. New: overall budget EUR 16,249,841, EU EUR 12,999,873, 95 institutions from 30 countries, GA CR-g-24-40. https://health.ec.europa.eu/non-communicable-diseases/cancer/europes-beating-cancer-plan-eu4health-financed-projects/projects/cancerwatch-ja_en
6. canSERV end date. Old: 31 Aug 2026. New: 28 Feb 2027, total EUR 14,866,440.50. https://cordis.europa.eu/project/id/101058620
7. Nedap. Old: hospital EHR/openEHR share n/f. New: Nedap Healthcare serves long-term, disability and home care only, no hospital EHR share. https://europeanpurpose.com/nl/alternatief-voor/europese-alternatieven-voor-epic
Also added: PALGA director Aletta Debernardi and board chair Iris Nagtegaal (oncologie.nu); DHD board chair L. de Beukelaar (dhd.nl/over-ons).

## STILL NOT FOUND (what was tried)
1. EHR vendor connectors (Epic/HiX/Nexus) of the NKR pipeline: IKNL pages, R(H)ONDA validation article, performation.com (HTTP 403).
2. FHIR R5/R6 plan for the NKR IG: iknl.nl, GitHub IKNL, build.fhir.org, web search.
3. "PZO" data standard: oncologienetwerken.nl, IKNL Jaarplan 2026, Dutch web search.
4. IKNL participation in ECCDM/PHOENIX: hl7.eu (affiliate page 404), Lisbon 2025 and Málaga 2026 WGM material (Málaga programme only in the event app), IKNL news.
5. nl-core non-beta roadmap: Simplifier, packages2.fhir.org, Nictiz wiki, Nictiz Releasebeleid.
6. nl-core derivation from HL7 Europe Base: Nictiz April 2026 EU plan, HL7 Europe base IG.
7. NKR-wide TNM 9 switch date: IKNL item sets 2026, RANK layouts, tumorindeling page, Standaardteksten PDF (404).
8. Health-RI director on health-ri.nl: organisation page lists teams only; secondary sources name Leone Flikweert (undated).
9. DHD managing director: dhd.nl/over-ons lists board only.
10. PALGA data-request fees and turnaround: palga.nl times out for automated fetch.
11. Health-RI "ELSA" guidance: only the ELSI Servicedesk and the ELSI metadata standard consultation exist.
12. Formal national Health-RI OMOP network: Health-RI wiki, OHDSI Europe material.
13. EUnetCCC Dutch partners: members directory requires login.
14. Zorginstituut 2026 progress document on oncology networks; ZonMw "Onderzoeksprogramma Kankerzorg": Zorginstituut site, Staatscourant notices, zonmw.nl.

## NEEDS BROWSER
- https://www.palga.nl/over-ons/bestuur.html and https://www.palga.nl/onderzoekers/ (site times out for curl; fees, procedure, current board).
- https://www.performation.com/datagateway (HTTP 403; EHR vendor compatibility of the Datagateway).
- https://www.bevolkingsonderzoeknederland.nl/media/i5vpa0en/bvo-nl-organogram-februari-2026.pdf (HTTP 403; BVO NL director).
- https://eunetccc.eu/members (redirects to login; Dutch EUnetCCC partners).
- HL7 Europe WGM Málaga 16-20 Nov 2026 programme (event app only) and https://hl7.eu/affiliate_nl.html (404 on curl); check for PHOENIX/cancer sessions and HL7 NL representatives.
- https://jane-2.eu or jane-cancer.eu (DNS failure from this host; official JANE-2 partner list).
- https://www.health-ri.nl team/leadership page (none found; alternatively KvK register for Stichting Health-RI bestuurders).
- https://iknl.nl/getmedia/33117624-693d-447c-9cf0-b86ccd3a275f/Standaardteksten-publicaties-NKR-data.pdf (404 now; may state TNM/ICD-O editions).
- https://www.zonmw.nl/nl/financiering-vinden (open calls overview; the old Open Competitie URL returns 404).
- https://nictiz.nl/over-nictiz/ organisation/management page (sub-pages return 404; confirm 2026 directie).
- web.archive.org (connection refused from this host) for historical Nictiz pages. OECI: resolved by the team lead's browser read on 2026-11-19.
