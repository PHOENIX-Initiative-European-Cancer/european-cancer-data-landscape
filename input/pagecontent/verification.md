### Verification pass

On 2026-11-19 every statement marked "n/f", "not verified" or sourced from a search snippet was re-checked by the agent that wrote it, using national-language searches, the organisations' own documents, archived copies of blocked pages and direct package or terminology-server queries; pages that block automated access were read in a real browser by the editor where no human check was required. Changed statements in the reports carry "(verified 2026-11-19)". Each log below records every item as VERIFIED, CORRECTED or STILL NOT FOUND, with the evidence, and ends with the pages that still need a browser or are unreachable.

### central-east

Pass date: 2026-11-19. Method: native-language web searches (PL, CZ, SK, HU, SL, HR, RO, BG), registry PDFs fetched with curl into scratchpad/dl and read with pdftotext, web.archive.org for offline pages, PubMed E-utilities for abstracts, Simplifier/dane.gov.pl APIs. Outcome codes: VERIFIED / CORRECTED / STILL NOT FOUND.

#### Counts
- VERIFIED: 32
- CORRECTED: 6
- STILL NOT FOUND: 23 (of which 10 blocked for automated fetch, see NEEDS BROWSER)

#### Poland
1. HL7 Poland GitHub contributor "sbojanowski" full name — VERIFIED: Sebastian Bojanowski, HL7 Poland Technical Lead (archived hl7.eu affiliate page). http://web.archive.org/web/2025id_/https://hl7.eu/affiliate_pl.html
2. KRN ENCR membership — VERIFIED: KRN listed in ENCR members contact list, contact Joanna Didkowska. https://www.encr.eu/encr-members-contact-list?page=10 (found via search index; page itself script-rendered)
3. KRN IACR membership — STILL NOT FOUND (IACR directory script-rendered).
4. Open cancer datasets on dane.gov.pl — VERIFIED: NFZ datasets per ICD-10 cancer code 2013–2020. https://dane.gov.pl/pl/dataset/2567 (via api.dane.gov.pl)
5. HDAB designation — VERIFIED as "not yet designated, concept presented 25 Mar 2026". https://uodo.gov.pl/pl/file/7458
6. Tumour-board software — VERIFIED: e-Konsylium platform (MoH/NIT, Wrocław pilot incl. breast oncology). https://www.gov.pl/web/cyfryzacja/e-konsylium--kolejny-wazny-etap-informatyzacji-systemu-ochrony-zdrowia-w-polsce
7. Structured pathology — VERIFIED addition: Accreditation Council pathology standards due Sept 2025 (Sejm committee transcript). https://api.sejm.gov.pl/sejm/term10/committees/ZDR04S/sittings/17/pdf
8. KRN researcher data-access procedure — STILL NOT FOUND (searched "udostępnianie danych KRN", NIO-PIB site, Dz.U. 2024/160).
9. Chemotherapy e-prescribing system, openEHR oncology, synthetic data — STILL NOT FOUND.
10. e-KRN+ hospital integration format — STILL NOT FOUND (only user manual public).
11. Poland 1+MG status — re-confirmed not signatory (2024 roadmap; no 2025/26 change found).

#### Czechia
12. HDAB — VERIFIED as proposal: NCEZ department of MoH proposed as HDAB, amendment of Act 325/2021 pending (NRez minutes 26 Feb 2026). https://ppo.mzcr.cz/upload/files/jednani-nrez-26-2-2026-zapis-nrez-26-2-2026-69d627afb0218.pdf
13. Chemotherapy system — VERIFIED: DIOS regimen database (Masaryk University). https://portal.med.muni.cz/article-449-dios-dose-intensity-as-oncology-standard.html
14. Tumour-board software, synoptic pathology tool, openEHR — STILL NOT FOUND (DASTA DS4 defines NOR report elements only).
15. SNOMED Czech national edition — STILL NOT FOUND (MLDS requires login).

#### Slovakia
16. TNM edition — CORRECTED: was "TNM 8 in 2024, 9th referenced 2026, mandate unclear"; now TNM 8 valid per 2024 methodology, TNM 9 effective 1 Jan 2026 per 2026 DGO guidance (Annex 1 TNM 9 code lists). https://www.nczisk.sk/Documents/nzr/2024/Metodicky_pokyn_NOR_SR_2024.pdf ; https://nczisk.sk/Documents/nzr/2026/MP_ZR_NOR_DGO.pdf (pdftotext)
17. HDAB — VERIFIED: NCZI project HeDAB-SK, HaDEA grant 972,587.20 EUR. https://nczisk.sk/en/International_cooperation/EHDS/Pages/Establishment-of-parts-of-the-health-data-access-body-in-the-Slovak-Republic.aspx
18. Chemotherapy software — VERIFIED: NÚDCH paediatric oncology clinic software. https://www.teraz.sk/zdravie/novy-softver-v-nudch-pomoze-zvysi/944037-clanok.html
19. ENCR/IACR membership — STILL NOT FOUND (list script-rendered).
20. 1+MG signatory, GDI node — STILL NOT FOUND (Slovak-language search returned only Slovenian/Czech results).
21. SNOMED Slovak edition/translation, researcher access route, MDT software, synoptic pathology, openEHR — STILL NOT FOUND.

#### Hungary
22. Registry variable dictionary — VERIFIED: 2019 government list of electronically transmitted data elements (BNO-10 ch. II, BNO-10 morphology annex, pTNM per separate rule, grade, OENO). https://2015-2019.kormany.hu/download/b/ea/81000/ML.pdf (pdftotext)
23. ICD-O use — CORRECTED: registry coding based on ICD-10, not ICD-O (Wéber et al. 2023, PubMed abstract via E-utilities). https://pubmed.ncbi.nlm.nih.gov/36521336/
24. TNM edition — VERIFIED: TNM 8 (prostate 7th) in 2022 registry-based study. https://www.por-journal.com/articles/10.3389/pore.2022.1610668/full
25. National cancer plan — VERIFIED: programme 2006, revised 2018; OECD 2023 target. https://infostart.hu/belfold/2018/07/30/nemzeti-egeszsegprogram
26. Tumour-board software — VERIFIED: Semmelweis onkoteam rules (MedSolution); Oncompass used by 26 onkoteams. https://semmelweis.hu/jogigfoig/files/2022/05/Onkoteam_szabalyzat_hataly_2022_V_21.pdf
27. HDAB — STILL NOT FOUND (Hungarian-language search; no designation).
28. HL7 Hungary affiliate — STILL NOT FOUND (hl7.eu index, HL7 International reports).
29. Registry operator — VERIFIED earlier as OOI (mta.hu document); unchanged.
30. Synoptic pathology, chemotherapy system, openEHR, researcher access route, SNOMED HU edition — STILL NOT FOUND.

#### Slovenia
31. HL7 Slovenia details — VERIFIED: est. 2014, 7 corporate + 10 individual members, chair Brane Leskošek (archived 2025-10-18). http://web.archive.org/web/20251018211849id_/https://hl7.eu/affiliate_si.html
32. HDAB — VERIFIED as not designated; SI-SUD project and OI/NIJZ critique of draft ZDigZ Art. 57 handling. https://ds-rs.si/sites/default/files/dogodek/dopis_oi_in_nijz_pripombe_in_predlogi_predlog_zdigz_epa_2240-ix.pdf
33. Tumour boards and chemotherapy software — VERIFIED: OI konziliji; Cypro drug-management software (Onkologija 2011). https://doaj.org/article/440523a9f08643c1bd5b8d35ebe98ad0
34. ICD-O/TNM editions in Register raka — STILL NOT FOUND: "Rak v Sloveniji 2022" (2025) not retrievable; dlib.si PDF streams return HTML; NIJZ yearbook cites only MKB-10.
35. OI Ljubljana OECI status — VERIFIED via browser capture (see item 63).
36. SI core FHIR package id — STILL NOT FOUND (packages.simplifier.net search API empty; Simplifier jurisdiction project list script-rendered).
37. Active-registration data format, synoptic pathology, SNOMED SI edition — STILL NOT FOUND.
38. hl7.si site — STILL NOT FOUND (archive.org blocked automated fetch).

#### Croatia
39. ICD-O/TNM — VERIFIED: MKB-O version 3.1; stage recorded as summary stage, not TNM (HZJZ bulletin "Rak u Hrvatskoj 2023./2024.", pdftotext). https://www.hzjz.hr/wp-content/uploads/2026/02/Bilten-2023.pdf
40. Submission format — VERIFIED (from indexed text, PDF fetch returned HTML): hospital systems send oncology hospitalisation reports as monthly files into NAJS. https://www.aem.hr/wp-content/uploads/2022/02/6.-Svaki-novi-korak-digitalizacije.pdf
41. HL7 Croatia — VERIFIED: est. 2003, chair Miroslav Koncar, 6 individual + 4 org members (archive). http://web.archive.org/web/2025id_/https://hl7.eu/affiliate_co.html
42. HDAB — VERIFIED as none designated (legal analysis). https://hrcak.srce.hr/file/494682
43. CEZIH terminology server name/URL — STILL NOT FOUND (Simplifier guide "Terminologije" page script-rendered).
44. SNOMED HR edition, synoptic pathology, MDT software, chemotherapy system, ENCR membership record — STILL NOT FOUND.

#### Romania
45. ICD-O-3 — VERIFIED: HG 663/2023 Art. 5(1) mandates CIM-O-3 (docx text extracted). https://management-documente.ms.ro/media/documents/HG_-REGISTRUL_NATIONAL_DE_CANCER_-_25.07.2023_2okqVrf.docx
46. Regional registry coding — VERIFIED: Cluj registry ICD-O-3 morphology; ICD-O-3.2 inclusion rules (ENCR 2021). https://iocn.ro/wp-content/uploads/2019/12/Cancerul_in_regiunea_nv_a_Romaniei_2010-2011.pdf
47. HL7 Romania — VERIFIED: Nov 2006, 21 members, chair Florica Moldoveanu (archive 2025-10-13). http://web.archive.org/web/20251013212616id_/https://hl7.eu/affiliate_ro.html
48. Tumour board practice — VERIFIED (press, single centre). https://adevarul.ro/stiri-interne/sanatate/tumor-board-abordarea-care-ofera-noi-sperante-1546906.html
49. RNC operational status — STILL NOT FOUND (INSP May 2026 lists development as ongoing). https://agerpres.ro/sanatate/2026/05/26/insp-aproximativ-40-dintre-cazurile-de-cancer-pot-fi-prevenite-printr-un-stil-de-viata-sanatos--1560130
50. TNM edition, HDAB, researcher access, synoptic pathology, chemotherapy system — STILL NOT FOUND.
51. CNAS DES specification content — STILL NOT FOUND (Cloudflare block).

#### Bulgaria
52. Coding standards — CORRECTED/clarified: Nov 2025 draft ordinance has no coding standards; public comment requests ICD-O-3/ICD-10 rules (consultation PDF, pdftotext). https://www.strategy.bg/bg/public-consultations/11919/export
53. BNCR data quality methods — VERIFIED: Dimitrova & Parkin 2015 (MV 87.4 percent). https://eld.bl.uk/catalog/100032457892_0x000001
54. NCPHA bulletins by МКБ-10 — VERIFIED (pdftotext). https://ncpha.government.bg/uploads/magazines/bulletins/bul_onko_2020web.pdf
55. TNM edition, HDAB, HL7 Bulgaria, submission format, researcher access, MDT/pathology/chemo systems — STILL NOT FOUND.

#### OECI (browser capture by team lead, https://accreditation.oeci.eu/ as of 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt)
60. Poland — CORRECTED: NIO-PIB (Maria Sklodowska-Curie National Research Institute of Oncology) is on the OECI certified-centres list; file previously said no accredited Polish centre.
61. Czechia — VERIFIED: Masaryk Memorial Cancer Institute on the list.
62. Hungary — VERIFIED: National Institute of Oncology (OOI) on the list.
63. Slovenia — VERIFIED: Institute of Oncology Ljubljana on the list (designation type not shown); resolves item 35.
64. Romania — CORRECTED: IOCN Cluj not on the current list; 2017 Clinical Cancer Centre certificate treated as lapsed (expiry 16 Nov 2022 per breast-unit directory).
65. Slovakia, Croatia, Bulgaria — VERIFIED: no centre on the list.

#### Cross-country
56. ECIS prevalence registry list PDF — STILL NOT FOUND by fetch (returns 244-byte stub); earlier facts rest on search-index text.
57. DARWIN EU data partners PDF — fetch returns HTML (EMA block).
58. SNOMED national editions (CZ, SK, SI, HR, HU) — STILL NOT FOUND (MLDS login).
59. OECI accredited-centres directory — resolved via browser capture, see items 60–65.

#### NEEDS BROWSER
- https://www.encr.eu/encr-members-contact-list (pages 0–18): confirm ENCR membership for SK, HU, HR, BG, RO, SI, CZ registries.
- https://ecis.jrc.ec.europa.eu/pdf/Prevalence_List_of_cancer_registries.pdf and https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- (resolved) OECI list captured; designation type per centre still to be read on each centre page at https://accreditation.oeci.eu/
- https://mlds.ihtsdotools.org/ (national SNOMED editions CZ/SK/SI/HR/HU)
- https://simplifier.net/jurisdictions/SI (projects/packages tab, Slovenian core IG package id)
- https://simplifier.net/guide/cezih-osnova (Terminologije page: Croatian terminology server)
- https://hl7.si/ and http://web.archive.org/web/20241114032631/https://hl7.si/
- https://portal.cnas.ro/cnas/des/docs/specificatii/ (Romanian DES specifications)
- https://www.onko-i.si/rrs (link to "Rak v Sloveniji 2022" PDF; methods: MKB-O/TNM editions) and https://dlib.si/stream/URN:NBN:SI:DOC-GGOFDB4Y/f7b09ce0-649b-446e-811a-a392bd8b49f2/PDF
- http://www.iacr.com.fr (membership directory)

### dach-benelux

Pass of 2026-11-19 over every item previously marked n/f, not found, not verified, snippet or secondary. Methods: German/Dutch/French web searches, direct curl of organisation pages and PDFs (pdftotext) into a separate download directory, npm package downloads from fhir.ch and axelv.github.io, GitHub API, get-ig.org package metadata. Outcomes: VERIFIED (fact with URL), CORRECTED (old vs new), STILL NOT FOUND (what was tried). Germany and Netherlands: only items in my own files were checked.

Totals after browser follow-up: VERIFIED 36, CORRECTED 17, STILL NOT FOUND 10 (61 items; six OECI items and the BCR IG status resolved by the team lead's browser read on 2026-11-19).

#### dach-benelux.md (FHIR survey)

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 1 | AT | Cancer registry FHIR profile set | STILL NOT FOUND | Three searches (EN/DE, "Krebsregister FHIR Österreich", Tumorregister Tirol FHIR); HL7 Austria registry lists no oncology IG. https://fhir.hl7.at/ |
| 2 | AT | Registry submission schema/file format | CORRECTED | Old: "not found". New: three channels, web form via eQuest, file upload via eQuest, SFTP file transfer; XML/CSV schema name still n/f. https://www.statistik.at/fileadmin/shared/QM/Standarddokumentationen/B_2/std_b_krebsstatistik.pdf (§2.1.7) |
| 3 | AT | ATC / national drug code | VERIFIED | ELGA e-Medikation uses PZN from the ASP-Liste and ATC codes; BASG register of authorised products. https://fhir.hl7.at/r4-ELGA-e-Medikation-main/StructureDefinition-at-elga-emed-medication-medikation-definitions.html |
| 4 | AT | TC FHIR authors (dev-build page) | STILL NOT FOUND | Published R5 2.0.0 IG has no authors page (toc checked); dev-tergi and fhir.hl7.at template-branch pages return 404 or redirect. Names kept with caveat. NEEDS BROWSER. |
| 5 | CH | CH CRL mCODE reuse | VERIFIED | ch.fhir.ig.ch-crl 0.9.0 npm package: zero occurrences of "mcode"; deps hl7.fhir.r4.core 4.0.1, ch-core 2.0.0; author/maintainer BAG. https://fhir.ch/ig/ch-crl/package.tgz |
| 6 | CH | ICD-10-GM current year in CH | CORRECTED | Old: not found. New (BFS page read in browser by team lead): coding year 2026 = ICD-10-GM 2024 (Swiss supplement 2024-10-31); coding year 2027 = ICD-10-GM 2026 (supplement 2026-10-27); one-year lag from ICD-10-GM 2026 for FR/IT translation. https://statistik.admin.ch/de/daten-statistiken-verstehen/nomenklaturen/medkk/instrumente-medizinischen-kodierung |
| 7 | CH | ICD-O-3 edition / TNM edition at NKRS | CORRECTED | Old: "not found". New: NKRS Data Dictionary Basic Variables v1.5 (01.01.2026) records ICD-O version (var. 3.2) and UICC TNM edition (var. 4.1) per case. https://www.nkrs.ch/upload/downloads/Forschende/Datenstruktur/Datenstrukturv15/Basisdatenv15/A_DataDictionary_BasicVariables_v1.5_01.01.2026.pdf |
| 8 | CH | LOINC use | VERIFIED | CH LAB-Order 3.0.0 (2025-12-16) and CH LAB-Report (1.0.0 trial-use; 3.0.0 ballot) bind LOINC. https://fhir.ch/ig/ch-lab-order/index.html ; https://fhir.ch/ig/ch-lab-report/usecases-en.html |
| 9 | CH | CH CRL named editors | STILL NOT FOUND | package.json author/maintainers: BAG only; GitHub repo hl7ch/ch-crl returns 404. |
| 10 | NL | PALGA FHIR specification | CORRECTED | Old: "not found". New: IKNL package iknl.fhir.nl.r4.palga 1.0.1 (FHIR R4), profiles for PALGA incidence notifications and protocol data to the NKR. https://get-ig.org/iknl.fhir.nl.r4.palga |
| 11 | NL | National drug code | VERIFIED | G-Standaard (Z-Index). https://www.z-index.nl/g-standaard |
| 12 | NL | nl-core maintainers | CORRECTED | Old: "not found". New: GitHub Nictiz/Nictiz-R4-zib2020 top contributors pieter-edelman-nictiz, jd-nictiz, ArdonToonstra. https://github.com/Nictiz/Nictiz-R4-zib2020 |
| 13 | BE | BCR IG mCODE reuse | VERIFIED | be.fhir.bcr 0.1.0 npm package: zero "mcode" occurrences; deps r4 core 4.0.1, hl7.terminology.r4 7.1.0, extensions 5.2.0. https://axelv.github.io/bcr/package.tgz |
| 14 | BE | TNM edition at BCR | STILL NOT FOUND | kankerregister.org menu "registration" page returns 404 via curl; Dutch searches for registratiehandleiding found nothing. NEEDS BROWSER. |
| 15 | BE | WBCR batch file specification | STILL NOT FOUND | Same as 14. NEEDS BROWSER. |
| 16 | BE | SNOMED join year | CORRECTED | Old: "not found". New: Belgium joined IHTSDO in 2013 (CliniSys slide, secondary) and is listed as member by Dec 2016 (Wikipedia). https://wiki.ihe.net/uploads/2/23/LAB_Tokyo_Semantic_Migom.pdf ; https://en.wikipedia.org/wiki/International_Health_Terminology_Standards_Development_Organisation |
| 17 | BE | LOINC national variant | VERIFIED | HL7 Belgium lab IG: LOINC per the FPS Health subset. https://build.fhir.org/ig/hl7-be/lab/qa-ipreview.html |
| 18 | BE | ATC / drug code | VERIFIED | SAM, CNK codes (NamingSystem be-ns-cnk-codes), FPS ATC-to-CNK mapping. https://www.ehealth.fgov.be/standards/fhir/medication/en/NamingSystem-be-ns-cnk-codes.html ; https://www.ehealth.fgov.be/standards/kmehr/en/tables/atc-codes |

#### dach-benelux-landscape.md

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 19 | DE | Per-state completeness | VERIFIED | Krebs in Deutschland 2023, ch. 2.1: diagnosis year 2020, 13 of 16 registries >95%, one 90–95%, two 80–90%. https://edoc.rki.de/bitstream/176904/11438/1/krebs_in_deutschland_2023-1.pdf |
| 20 | DE | ECIS contribution | VERIFIED | ECIS list (Sept 2024): Brandenburg, Bremen, Hamburg, Mecklenburg-Vorpommern, Munich, NRW, Saarland, Saxony (23%). https://ecis.jrc.ec.europa.eu/sites/default/files/2024-09/List_of_cancer_registries.pdf |
| 21 | DE | Synthetic datasets | STILL NOT FOUND | DE/EN searches ("synthetische Krebsregisterdaten", ZfKD Testdatensatz). |
| 22 | DE | OECI accredited centres | VERIFIED (absent) | No German centre on the OECI certified-centres list (browser read by team lead, 2026-11-19). https://accreditation.oeci.eu/ |
| 23 | DE | EHDEN oncology partners | VERIFIED | 10 German partners incl. Charité, DKG, GermanOncology, Krebsregister RLP, UM Dresden, MHH, InGef, Ulm. https://ehden.eu/datapartners/ |
| 24 | DE | MIO oncology | STILL NOT FOUND | KBV MIO page and mio42 checked; no oncology MIO. https://www.kbv.de/praxis/digitalisierung/anwendungen/elektronische-patientenakte/mio |
| 25 | DE | ICCR structured pathology | CORRECTED | Old: n/f. New: German ICCR dataset pilot (TUR-B) with SNOMED CT, reports mostly free text. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11861236/ |
| 26 | DE | openEHR oncology | CORRECTED | Old: n/f. New: HiGHmed CKM 8 oncology templates / 35 archetypes for oBDS, MTB recommendation archetype, ICD-O cluster. https://ebooks.iospress.nl/pdf/doi/10.3233/SHTI240655 ; https://discourse.openehr.org/t/modeling-of-multidisciplinary-tumor-board-meetings/6092 |
| 27 | DE | JANE-2 / EUCanScreen / TEHDAS2 partners | VERIFIED | JANE-2: BMG, Charité, DKFZ, DKG, BZgA, MSB; EUCanScreen: RKI, DKFZ, DKG; TEHDAS2: BMG, BfArM. https://sigarra.up.pt/fmup/en/PROJECTOS_GERAL.MOSTRA_PROJECTO?p_id=83039 ; https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://tehdas.eu/partners/ |
| 28 | DE | Modellvorhaben 25,000 records (secondary) | STILL NOT FOUND | No BfArM/GKV-SV/BMG figure; GKV-SV lists participating providers only. https://www.gkv-spitzenverband.de/krankenversicherung/forschung_modellvorhaben/mv_genomsequenzierung/genomsequenzierung.jsp |
| 29 | AT | Breast screening register | CORRECTED | Old: n/f. New: uniform documentation system, pseudonymised via Dachverband, coordination at ÖGK, GÖG evaluation, bPK linkage under § 15c GÖGG. https://www.parlament.gv.at/dokument/XXVIII/AB/1880/imfname_1701525.pdf ; https://www.jusline.at/gesetz/goegg/paragraf/15c.pdf |
| 30 | AT | AMDC and cancer registry | CORRECTED (partial) | AMDC remote access and catalogue confirmed; Vorarlberg registry operator accredited; cancer registry dataset in catalogue still n/f. https://www.statistik.at/en/services/tools/data-access/center-for-science/austrian-micro-data-center-amdc |
| 31 | AT | ECIS / ENCR | VERIFIED | Austria National registry in ECIS list (100%); Statistik Austria states ENCR and IACR membership. URLs as in #20 and #2 |
| 32 | AT | EUCAIM / TEHDAS2 / JANE-2 | VERIFIED (JANE-2 n/f) | EUCAIM: Medical University of Vienna; TEHDAS2: GÖG. https://cancerimage.eu/partners/ ; https://tehdas.eu/partners/ |
| 33 | AT | Oncology CDA guide | STILL NOT FOUND | ELGA guides list (Labor, Befund bildgebende Diagnostik, Entlassungsbrief, e-Medikation); pathology guide announced 2013, status unknown. |
| 34 | AT | Tumour-board software, structured pathology, openEHR | STILL NOT FOUND | DE searches. |
| 35 | CH | ECIS contribution | VERIFIED | Basel, Geneva, Grisons, St. Gallen, Ticino, Valais (30%). URL as #20 |
| 36 | CH | OECI | VERIFIED | CCC Zürich is an OECI member and DKG-certified; no Swiss centre on the OECI certified-centres list. https://www.usz.ch/en/?p=99220 ; https://accreditation.oeci.eu/ |
| 37 | CH | SPHN funding (Wikipedia mirror) | VERIFIED | SBFI: max CHF 20.7 M for the DCC 2025–2028. https://www.sbfi.admin.ch/de/datenkoordinationszentrum-des-swiss-personalized-health-network |
| 38 | CH | EU projects | VERIFIED (partial) | No Swiss partner on EUCAIM or TEHDAS2 partner pages; EUnetCCC/JANE-2 Swiss role n/f (eunetccc.eu fetch returns 135 bytes). NEEDS BROWSER. |
| 39 | CH | EPD oncology content | STILL NOT FOUND | — |
| 40 | CH | Registry software failure (heise) | CORRECTED to primary | BAG press release 24 Jan 2025; BAG review 10 June 2025; GDK successor project. https://www.bag.admin.ch/dam/fr/sd-web/si4u6qVqFCNn/Projektanalyse_Aufarbeitung_Projekt_IT-Architektur_KRG_RSW.pdf |
| 41 | CH | Tumour-board software etc. | STILL NOT FOUND | — |
| 42 | NL | ENCR membership | VERIFIED | "The Netherlands National" in ECIS list of ENCR-affiliated registries (100%). URL as #20 |
| 43 | NL | ScreenIT | VERIFIED | RIVM: ScreenIT for breast/cervical/colorectal, owned by Bevolkingsonderzoek Nederland, code on GitHub. https://www.rivm.nl/bevolkingsonderzoeken-en-screeningen/bevolkingsonderzoek-organisatie/broncode-vrijgegeven |
| 44 | NL | OECI centres | CORRECTED | Old: NKI, Maastricht, Erasmus MC, Radboudumc, UMCG (secondary). New: list shows Erasmus MC, Maastricht UMC+, NKI, OncoZON, Rijnstate, UMCG; Radboudumc not listed. https://accreditation.oeci.eu/ |
| 45 | NL | Hartwig access; 1+MG | VERIFIED | Hartwig DR guide; Health-RI coordinates GDI, Erasmus MC co-leads Genome of Europe. https://hartwigmedical.github.io/documentation/data-access-request-guide.html ; https://health-ri.atlassian.net/wiki/spaces/HNG/pages/608312395 |
| 46 | NL | BBMRI-NL | VERIFIED | https://www.bbmri-eric.eu/?p=6325 |
| 47 | NL | EUCAIM partners | VERIFIED | Erasmus MC, Maastricht University, Radboudumc, NKI. https://cancerimage.eu/partners/ |
| 48 | NL | Oncoguide | VERIFIED | https://iknl.nl/getmedia/351d2826-cc3a-49a4-81a1-827c7ed5f3e1/faq-oncoguide_oktober2018_iknl.pdf |
| 49 | BE | CvKO screening register | CORRECTED | eHealth ISC decisions: CvKO–BCR invitation file exchange; BCR runs cytohistopathology and Flemish cervical screening registers. URLs in file |
| 50 | BE | ECIS | VERIFIED | Flanders (58%). URL as #20 |
| 51 | BE | Cancer plan 2025 | CORRECTED | Belgian Cancer Plan 2025–2030 (Sciensano, draft Q4 2025); 34-measure plan presented 2026. https://www.sciensano.be/sites/default/files/16062025_kankerplan_2025-2030_1.pdf |
| 52 | BE | OECI centres | VERIFIED | List shows Institut Jules Bordet (renewed 22 June 2026), Leuven Cancer Institute, AZ Groeninge Kortrijk. https://accreditation.oeci.eu/ ; https://www.bordet.be/en/news/mon-06222026-1100/jules-bordet-institute-accredited-comprehensive-cancer-centre-oeci |
| 53 | BE | KMEHR oncology | STILL NOT FOUND | — |
| 54 | BE | EUCAIM / EUCanScreen partners | VERIFIED | KU Leuven, Sciensano (EUCAIM); Sciensano, CvKO, Stichting Kankerregister, UZA, Bordet (EUCanScreen). |
| 55 | LU | ENCR | VERIFIED | ENCR contact list; Backes on steering committee. https://encr.eu/encr-members-contact-list?page=9 |
| 56 | LU | Legal basis | VERIFIED | RGD 18 April 2013 (Mémorial A 79). https://conseil-etat.public.lu/content/dam/conseil_etat/fr/avis/2013/03/50_029/50029_Texte.pdf |
| 57 | LU | Submission format | VERIFIED (partial) | Annex-1 variables via annexed declaration form; electronic format n/f. |
| 58 | LU | ECIS | VERIFIED (absent) | Not in ECIS list. |
| 59 | LU | 1+MG | VERIFIED | LNDS co-leads GoE ELSI WP; LIH contributes cohorts. https://lnds.lu/?p=3918 |
| 60 | LU | EUCanScreen / TEHDAS2 | VERIFIED | Not in EUCanScreen list; LNDS in TEHDAS2. |
| 62 | AT/LU | OECI centres | VERIFIED (absent) | No Austrian or Luxembourg centre on the OECI certified-centres list. https://accreditation.oeci.eu/ |
| 63 | BE | Status of be.fhir.bcr IG | CORRECTED | Old: presented as eHealth Platform-published draft. New: individual developer's local development build (Axel Vanraes, Tiro.health); canonical returns 404, not on Simplifier/packages.fhir.org, not in hl7-be GitHub (browser check by team lead). https://axelv.github.io/bcr/ |
| 61 | LU | DSP oncology | CORRECTED (partial) | IdeoRCP tumour-board app hosted on eSanté (2015). https://paperjam.lu/article/communique-signature-de-conventions-de-partenariat |

#### NEEDS BROWSER

- RESOLVED 2026-11-19: oeci.eu certified-centres list read by team lead; see items 22, 36, 44, 52, 62.
- kankerregister.org: registration pages (WBCR, batch extraction specification, coding manual with TNM/ICD-O edition); EN menu link "registration" returns 404 via curl.
- dev-tergi.elga.gv.at/r5-core-main/authors.html and fhir.hl7.at template branch authors page: confirm HL7 Austria TC FHIR authors (Anna Lin, Reinhard Egelkraut, Oliver Krauss).
- RESOLVED 2026-11-19: BFS ICD-10-GM validity read by team lead; see item 6.
- eunetccc.eu partners page (returns 135 bytes to curl): Swiss, Austrian, Luxembourg partners.
- eosc4cancer.eu partners/consortium (returns empty to curl): German, Dutch, Belgian partners.
- legilux.public.lu (JavaScript only): full text of RGD 18 April 2013 incl. annex 1 variable list and declaration form.
- statistik.at AMDC Mikrodatenkatalog: whether the Krebsstatistik dataset is listed.
- hl7belgium.org: invalid TLS certificate (team lead, 2026-11-19); use HL7 Belgium GitHub (hl7-be) and Simplifier instead.
- gkv-spitzenverband.de Modellvorhaben page / BfArM: any official count of transmitted genome datasets.

### eu-funding

**Counts:** 14 VERIFIED · 4 CORRECTED · 25 STILL NOT FOUND (43 items checked; two VERIFIED items also carry title corrections).

Method: Funding & Tenders SEDIA search API (filtered by programme: EU4Health 43332642, Digital Europe 43152860, IHI 43108390), topicDetails JSON per topic, CORDIS XML per project (standards grep for FHIR/OMOP/mCODE/OHDSI/HL7/openEHR/GA4GH), Zenodo deliverables, web search. Downloads: /private/tmp/claude-501/-Users-thome-code-fhir-profiling-cancer-common/3cc04596-744d-4990-addb-ce34993d093b/scratchpad/euv-dl/. Pre-edit backup of the report: /private/tmp/claude-501/-Users-thome-code-fhir-profiling-cancer-common/3cc04596-744d-4990-addb-ce34993d093b/scratchpad/euv-scripts/eu-funding.backup.md.

| # | item | status | finding | source / what was tried |
|---|---|---|---|---|
| 1 | EU4H-2027-SANTE-OG deadline (was n/f) | VERIFIED | Deadline 2027-01-19, opened 2026-11-04, EUR 1.8 M. Row moved to sorted position. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/EU4H-2027-SANTE-OG |
| 2 | HORIZON-RAISE-2027-01-04 type, budget, total | VERIFIED (+ title CORRECTED) | CSA lump sum, EUR 1.0 M, 1 project. Title is "Developing a model for a Data Lab for Science ... (RAISE pilot)". | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-RAISE-2027-01-04 |
| 3 | HORIZON-CL4-2027-04-DATA-03 type, budget, total | VERIFIED (+ title CORRECTED) | RIA, EUR 17.5 M per project, EUR 35 M, 2 projects. Title "New approaches for decentralized, federated and sustainable AI data processing". | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-CL4-2027-04-DATA-03 |
| 4 | IHI call 13 budget per project and total | VERIFIED | EUR 53.2 M; topics 35.0 / 9.0 / 9.2 M, 1 project each; opened 2026-07-02; stages 8 Oct 2026 and 21 Apr 2027. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-JU-IHI-2026-13-two-stage-01 |
| 5 | IHI call 13 stage 1 total (recently-closed table) | VERIFIED | EUR 53.2 M. | same |
| 6 | HORIZON-INFRA-2027-01-EOSC-01 per-project budget | VERIFIED | EUR 40 M, 1 grant. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-INFRA-2027-01-EOSC-01 |
| 7 | HORIZON-INFRA-2027-01-EOSC-01 action type | CORRECTED | "Cofund/CSA-type" to "COFUND". | same |
| 8 | HORIZON-INFRA-2027-SERV-01-02 dates and budget | VERIFIED | Opens 9 Mar 2027, closes 15 Jun 2027, EUR 6 M x 6 = 35 M. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-INFRA-2027-SERV-01-02 |
| 9 | HORIZON-HLTH-2026-03-DISEASE-13 dates and budget | VERIFIED | Opens 10 Feb 2027, closes 13 Apr 2027, EUR 63 M (30 + 33). | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-HLTH-2026-03-DISEASE-13 |
| 10 | HLTH-2027-03-TOOL-04 and TOOL-08 deadline | CORRECTED | Report said French NCP shows 22 Sep 2027 "on the portal". Portal shows 16 Sep 2027 for both. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-HLTH-2027-03-TOOL-04 ; https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-HLTH-2027-03-TOOL-08 |
| 11 | EU4H-2026-SANTE-PJ-08 total | VERIFIED | EUR 14,386,810; open 23 Sep 2025, closed 6 Jan 2026. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/EU4H-2026-SANTE-PJ-08 |
| 12 | ECHoS 2 EU share ("not separated") | CORRECTED | CORDIS gives EU contribution EUR 15,079,639.52. | https://cordis.europa.eu/project/id/101288304 |
| 13 | HealthData@EU Pilot FHIR/OMOP | VERIFIED | D8.1: some HDABs and teams converted the COVID-coagulopathy use case to OMOP CDM; others analysed native data. FHIR only in glossary. No mandatory CDM. | https://zenodo.org/records/15096755 |
| 14 | GDI FHIR/OMOP | VERIFIED (partial) | D8.7 surveys OMOP CDM, Phenopackets and HL7 FHIR (via ART-DECOR) without mandating one clinical CDM. EU share still n/f. | https://zenodo.org/records/11550316 |
| 15 | EuCanImage OMOP (n/f) | CORRECTED | OMOP was evaluated, not adopted. CORDIS lists the publication "Evaluation of OMOP CDM, i2b2 and ICGC ARGO for supporting data harmonization in a breast cancer use case". | https://cordis.europa.eu/project/id/952103 |
| 16 | OPTIMA OMOP | VERIFIED | CORDIS record names OMOP and OHDSI. FHIR/mCODE still n/f. | https://cordis.europa.eu/project/id/101034347 |
| 17 | TRANSCAN-4 cofund budget/period (context for JTC 2027) | VERIFIED | EU contribution EUR 5,836,584; 2026-04-01 to 2031-03-31. | https://cordis.europa.eu/project/id/101288225 |
| 18 | CORDIS dates/budgets of QUANTUM, CCI4EU, EUonQoL, PANCAIM, canSERV, CANDLE, 4.UNCAN.eu, B1MG, ECHoS | VERIFIED | All match the report within rounding. | CORDIS XML per id |
| 19 | EU4Health WP 2026 call ids and deadlines (DI-g-26-23, -24, -25, HS-g-26-16, CR/CV&NCD-g-26-13, -14) | STILL NOT FOUND | No EU4Health topic from WP 2026 on the portal. Newest EU4Health topic is EU4H-2027-SANTE-OG. Row annotated. | SEDIA filtered by EU4Health, sorted by opening date |
| 20 | DP-g-26-11 ERN per-grant budget | STILL NOT FOUND | Direct grants, not on portal. | SEDIA |
| 21 | Digital Europe 2027 topic ids (VHT/AI incubator, Apply AI testing, MCP support) | STILL NOT FOUND | Only DIGITAL-ECCC-2027 cyber topics published. Web search failed. | SEDIA filtered by Digital Europe; web search |
| 22 | IHI call 14 deadlines | STILL NOT FOUND | Draft topics only; launch "early 2027". | SEDIA (IHI); ihi.europa.eu future opportunities; web search |
| 23 | IHI call 15 deadlines | STILL NOT FOUND | Same. | same |
| 24 | TRANSCAN-4 JTC 2027 topic and dates | STILL NOT FOUND | No pre-announcement found. | web search; CORDIS |
| 25 | TRANSCAN-4 JTC 2026 total | STILL NOT FOUND | Only national shares (Polish NCBR EUR 1.2 M; INCa cap 300 k per partner). Note added. | https://www.gov.pl/attachment/1f0c6796-93ba-43c5-8300-173bdffa4de1 |
| 26 | EIT Health Innovation Validation 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 27 | ERA4Health IICS4all 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 28 | ERA4Health NanoDiagNCD 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 29 | THCS JTC 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 30 | COST Open Call 2027 dates | STILL NOT FOUND | Only 2026 announcement found. | web search; cost.eu |
| 31 | EP PerMed RIT call 2027 | STILL NOT FOUND | Only JTC2027 CGT4PM found. | web search |
| 32 | SCOPE-AI grant id, start, end, admin coordinator, standards | STILL NOT FOUND | No project record in SEDIA. Press release confirms only scientific coordination by IIS La Fe. | SEDIA free text; web search |
| 33 | DARWIN EU successor contract award, value, end | STILL NOT FOUND | TED returns empty pages to scripted access. Second notice 366419-2026 (28 May 2026) unread. | ted.europa.eu |
| 34 | HealthData@EU central platform tender award (TED 533039-2026) | STILL NOT FOUND | TED blocked. | ted.europa.eu |
| 35 | QUANTUM FHIR/OMOP | STILL NOT FOUND | CORDIS record and deliverable titles name no standard. Label builds on TEHDAS/EMA/EOSC frameworks. Row annotated. | CORDIS XML; web search |
| 36 | CCI4EU FHIR/OMOP | STILL NOT FOUND | No standard in CORDIS or project pages. | CORDIS XML; web search |
| 37 | EUonQoL FHIR/OMOP | STILL NOT FOUND | Web platform and app deliverables name no standard. | CORDIS XML; web search |
| 38 | PANCAIM FHIR/OMOP | STILL NOT FOUND | Collective Minds platform; no standard named. | CORDIS XML; web search |
| 39 | canSERV FHIR/OMOP | STILL NOT FOUND | Service catalogues only. | CORDIS XML; web search |
| 40 | CANDLE FHIR/OMOP | STILL NOT FOUND | Only "harmonisation and standardisation"; FHIR/OMOP is UNCAN-Connect. | CORDIS XML; web search |
| 41 | JANE-2 FHIR/OMOP | STILL NOT FOUND | Not on CORDIS; omics interoperability WP named, no standard. | web search |
| 42 | EUnetCCC FHIR/OMOP | STILL NOT FOUND | Not on CORDIS; only a participant post linking EUnetCCC to QUANTUM labels. | web search |
| 43 | JRC ECIS/ENCR budget line; Cancer Mission 2028+ allocation; FP10 health allocation | STILL NOT FOUND | No published amount. Only advocacy and the ECA report. | web search |

Items not retried individually (n/f in report, lower priority, unchanged): BreastSCan, 4.UNCAN.eu, B1MG, B1MGplus budget and coordinator, Xt-EHR budget, JANE, CraNE, ECHoS, PCM4EU, EU-CAYAS-NET standards, EHDEN Foundation figures, EP PerMed RITC2026 total, EIT Health 2026 total. Several are EU4Health or Digital Europe projects without CORDIS records.

#### NEEDS BROWSER

- **DARWIN EU successor:** read TED notices 330958-2026 and 366419-2026 for value, duration and any award. https://ted.europa.eu/en/notice/366419-2026/html
- **HealthData@EU central platform tender:** check for an award notice following TED 533039-2026.
- **SCOPE-AI:** find the grant number and legal coordinator on the portal project search, or on cancerimage.eu and eucaim.cancerimage.eu.
- **EU4Health WP 2026 calls:** watch the HaDEA calls page for EU4H-2026/2027 project-grant topics (DI-g-26-23 etc.). https://hadea.ec.europa.eu/calls-proposals_en
- **Digital Europe 2027:** watch the portal for DIGITAL-2027 health topics, expected to open Q1 2027.
- **IHI calls 14 and 15:** https://www.ihi.europa.eu/apply-funding/future-opportunities
- **TRANSCAN-4 JTC 2027 and JTC 2026 total:** https://transcan.eu
- **Partnership call totals (ERA4Health, THCS, EIT Health):** read the call texts on the partnership sites.

### france-fhir

Method: French and English web searches, Wayback Machine copies (`web.archive.org/web/<ts>id_/<url>`) of JS-rendered or WAF-protected pages, curl + pdftotext into `fr-dl/` (no interpreter run from inside it), GitHub API (`gh api`), Simplifier HTML. Every item that was marked n/f, "not verified", "snippet" or "unverified" in the first version of the file is listed below with its outcome.

| # | Item | Outcome | Evidence |
|---|------|---------|----------|
| 1 | PSCC ↔ PHOENIX relationship | **VERIFIED** | PHOENIX (Patient Health Oncological Expertise Network for International eXchange) officially launched 2025-10-02 at the Paris-Saclay Cancer Cluster, Villejuif; founding members PSCC, INCa, BIH, IKNL, InterSystems "among others"; speakers Cangioli, Delanchy (PHOENIX), Lablans (DKFZ), Rance (CARPEM), Warnon (CHU Charleroi), Guérin (Curie), Sieswerda (IKNL), Deloger (Gustave Roussy), Debertshaeuser (BIH) — https://www.fluteproject.eu/eventi/official-launch-of-the-european-acceleration-initiative-phoenix/ . HL7 Europe Annual Report 2024 p.20-22: core team Institut Paoli-Calmettes (FR), INCa (FR), BIH@Charité (DE), PSCC (FR), IKNL (NL); Common Cancer Data Model is the first PHOENIX project — https://hl7europe.org/wp-content/uploads/2025/12/Annual-Report-2024-Fin_.pdf . Opening at WGM Lisbon Feb 2025 — https://hl7europe.eu/wp-content/uploads/2025/02/hl7euwgm2025_opening_all.pdf . IC deck Sept 2025 (agreement to be signed by 2 Oct) — https://confluence.hl7.org/download/attachments/358272045/HL7EU-IC-WGM-09-2025-1.pdf?version=1&modificationDate=1757796418371&api=v2 . IDEA4RC 2026-06-11 — https://www.idea4rc.eu/2026/06/11/the-european-cancer-common-data-model-gains-momentum/ . GitHub org https://github.com/PHOENIX-Initiative-European-Cancer |
| 2 | PSCC Data partner hospitals (was "search snippet") | **VERIFIED** | "This project already brings together Gustave Roussy, Institut Curie, AP-HP and Hôpital Foch ... joining forces with Unicancer ... and Cancer Core Europe"; federated data network — https://parissaclaycancercluster.org/en/patient-insight |
| 3 | Isabelle Fernandez (INCa) role in PHOENIX / PSCC | **STILL NOT FOUND** | Searched "Isabelle Fernandez" + INCa / PSCC / HL7 / Phoenix; GitHub profile INCaIFernandez has no name/company; not among launch speakers or Annual Report names. |
| 4 | CGTS head (ANS) | **STILL NOT FOUND** (partial) | No named head of CGTS on esante.gouv.fr, smt.esante.gouv.fr, gnius. Found: SNOMED International France page lists ANS appointed representatives Thierry Dart (General Assembly), Elisabeth Serrot-Damatte and Maël Le Gall (Member Forum), contact ans-terminologies@esante.gouv.fr — https://www.snomed.org/members/france ; undated CGTS webinar deck: Thierry Dart "Directeur du Pôle Affaires Médicales et Labellisation", Yann Briand "Expert sémantique" — https://industriels.esante.gouv.fr/sites/default/files/media/document/Webinaire_CGTS.pdf (PDF blocked for curl; title from search index). |
| 5 | OSIRIS25 call content (was "JS challenge, snippets") | **VERIFIED** | Wayback copy of the call PDF read with pdftotext: opened 2025-05-02, deadline 2025-09-04, results Dec 2025, 48 months, max 200 kEUR, 5 OSIRIS domains, HL7 FHIR conformance objective, OMOP/mCODE mapping eligible, use of ig-osiris.cancer.fr — https://web.archive.org/web/2025/https://www.cancer.fr/content/download/117019/file/INCa_AAP_OSIRIS25_Appel%20%C3%A0%20projets_VF.pdf?version=2 |
| 6 | OSIRIS25 laureates | **PARTIALLY VERIFIED / NEEDS BROWSER** | Search index excerpt of the INCa call page: "3 projets financés", incl. "Développement d'un cadre d'interopérabilité FHIR pour la structuration pérenne et le partage des données oncologiques en vie réelle", coordinator Bastien Rance (Université Paris Cité). Page returns a 315-byte WAF challenge to curl; Wayback has no capture (620-byte error) — https://www.cancer.fr/professionnels-de-la-recherche/appels-a-projets-et-a-candidatures/nos-appels-a-projets/osiris25 ; projets.e-cancer.fr/files/workflow/3194 also returned HTML only. |
| 7 | OSIRIS FHIR IG 2.0 / R5 roadmap | **STILL NOT FOUND** | GitHub: one open issue (#334, 2024-12-10, translate to French), three undated milestones (Radiomic / Radiotherapy / Imagery Implementation), no roadmap, no R5 branch — https://github.com/InstitutNationalduCancer/ImplementationGuide_OsirisFHIR/issues ; /milestones . OSIRIS25 call refers only to IG 1.1.0. |
| 8 | CLIP2 use of OSIRIS | **STILL NOT FOUND** | French searches; INCa scientific reports 2022/2024 list CLIP² and OSIRIS as separate programmes — https://www.cancer.fr/content/download/132645/file/RAPSCFR24_Rapport_scientifique24.pdf?version=1 |
| 9 | "OSIRIS data portal" | **STILL NOT FOUND as such** | Nearest real objects: PSCC Data federated portal (OSIRIS-RWD + FHIR; tenders 25-105178, 26-46260) and INCa PDC (SNDS warehouse). No INCa "portail OSIRIS". |
| 10 | CI-SIS cancer volet statuses (was "JS-rendered, snippet") | **VERIFIED** | Wayback snapshot 2026-01-01 of the publication space, table "Couche métier": CANCER-CR-ACP Obsolète; CANCER-CR-GM 2022.01 Validé 06/12/2022; CANCER-D2LM 2022.01 Validé 12/03/2025; CANCER-FRCP 2025.01 Validé 27/08/2025; CANCER-PPS 2025.01 Validé 27/08/2025 (all "Volet CDA") — https://web.archive.org/web/20260101/https://esante.gouv.fr/offres-services/ci-sis/espace-publication . Snapshots dated 2026-06 and 2026-10 are not available (620-byte errors). |
| 11 | FHIR migration plan for cancer volets | **STILL NOT FOUND (specific)**, generic doctrine **VERIFIED** | ANS doctrine (Wayback copy): "A terme, l'ensemble des volets du Cadre d'Interopérabilité des Systèmes d'Information de Santé (CI-SIS) seront basés sur le standard FHIR"; FHIR = "standard socle" for EEHRxF priority categories — https://esante.gouv.fr/doctrine/interoperabilite . No oncology FHIR guide in https://interop.esante.gouv.fr/ig/fhir/ ; no RCP/PPS FHIR roadmap in searches (incl. "fiche RCP FHIR", "DCC FHIR 2026"). |
| 12 | DCC call laureates | **CORRECTED** | Wayback copy of the ANS page lists six laureate projects; first version of the file missed "Production et Diffusion du PPS Cancer dans e-RCP" (Grand Est / BFC / PACA: GRADeS Pulsy, GRADeS ieSS, DSRC OncoPaca-Corse, GRADeS BFC) and the detailed beneficiaries of the Pays de la Loire / Occitanie / Réunion / Martinique and Corse / Guyane / Guadeloupe projects; "Task Force Cancérologie (DNS-INCa-ANS)"; reference docs "REM DCC ERRATUM version 23062026" — https://web.archive.org/web/2026/https://esante.gouv.fr/appel-projets-evolution-du-dossier-communicant-de-cancerologie-dcc |
| 13 | EUCAIM French partners / French node FHIR use | **VERIFIED (partners)** / **STILL NOT FOUND (FHIR)** | Official partner page, France: AP-HP, CNRS, Collège des Enseignants en Radiologie de France, INRIA, LIMICS, Medexprim, Owkin (left Dec 2023) — https://cancerimage.eu/partners/ . No French-node FHIR documentation found (searches "EUCAIM national node France", architecture gitbook). |
| 14 | CraNE French node FHIR | **VERIFIED (negative)** | CraNE = EU4Health JA (NIJZ, 46 partners, 2022-11 to 2024-10); INCa leads WP5 and WP7, Unicancer affiliated entity, FHF and Inserm partners — https://www.unicancer.fr/wp-content/uploads/2023/10/crane-leaflet.pdf ; https://sciensano.be/en/projects/joint-action-network-comprehensive-cancer-centres . Only FHIR artefact: CraNE CCCN Patient Pathway IG (WP6 Task 6.4, NIJZ) — https://simplifier.net/guide/crane-cccn-pw-ig/Home . No French FHIR role. |
| 15 | CodeX membership of French organisations | **VERIFIED (none)** — browser check by team lead 2026-11-19 | CodeX Membership page (last updated 2026-08-12) lists only US/Canadian members (premier: HL7 International, Pfizer, UBC, UnitedHealthcare; principal: ACC, Myriad Genetics, Varian; benefactor/developer tiers North American), Wemedoo and Elekta the only Europe-headquartered developer members; no French organisation — https://confluence.hl7.org/spaces/COD/pages/66940241/CodeX+Membership . (curl: codex.hl7.org member URLs 404; old Confluence "CodeX Members" page gone.) |
| 16 | HL7 France chair 2026 | **VERIFIED (as of Nov 2025)** / election **STILL NOT FOUND** | Wayback 2025-11-15 snapshot of hl7.eu/affiliate_fr.html: "The current chair (interim) is Nicolas Riss PharmD"; HL7 France est. 2007, 34 members; technical lead/WGs François Macary (PHAST), Eric Dufour (SELIC), Isabelle Gibaud (HAS) — https://web.archive.org/web/20251115033408/https://hl7.eu/affiliate_fr.html . GitHub profile nriss: company "Agence du Numérique en Santé" — https://github.com/nriss . Dec 2021 election — https://groups.google.com/g/ihe-france-laboratoire/c/qND-9lYpyvE . No 2024/2026 election notice found (live hl7.eu page 404; interopsante.org/association requires login). |
| 17 | Institut Curie FHIR layer | **STILL NOT FOUND** | Only 2019 Teratec deck on Curie Data Resource (i2b2/tranSMART) listing FHIR as an issue — https://teratec.eu/library/pdf/forum/2019/presentations/Forum_Teratec_2019_A4_02_Alain_LIVARTOWSKI_Institut_Curie.pdf |
| 18 | Harmonie (Unicancer) data model | **STILL NOT FOUND** | Sept 2025 press release and July 2026 LOT-LuCA release name no FHIR/OMOP/OSIRIS — https://www.unicancer.fr/wp-content/uploads/2026/07/juillet-2026-cp-aap-data-challenge-lot-luca-vf-1-1-1.pdf |
| 19 | HCL oncology FHIR specifics | **STILL NOT FOUND** | No new source beyond the Alliance SIH article. |
| 20 | ANS or Interop'Santé cancer FHIR working group | **STILL NOT FOUND** | Interop'Santé GT page (2026) lists no cancer GT — https://www.interopsante.org/groupe-de-travail |

Counts after the team lead's browser check (2026-11-19): VERIFIED 9 (items 1, 2, 5, 10, 11-generic, 13-partners, 14, 15, 16-as-of-2025) · CORRECTED 1 (item 12) · PARTIAL 2 (items 4, 6) · STILL NOT FOUND 8 distinct items (3, 7, 8, 9, 17, 18, 19, 20) plus the sub-items 11-specific, 13-FHIR, 16-election.

Unverifiable today (2026-11-19, browser): the cancer.fr OSIRIS25 page and hl7.eu/affiliate_fr.html return 404; esante.gouv.fr is in maintenance. These are recorded in france-fhir.md as "unverifiable today", not n/f.

#### NEEDS BROWSER (remaining, re-check on a later day)

- https://www.cancer.fr/professionnels-de-la-recherche/appels-a-projets-et-a-candidatures/nos-appels-a-projets/osiris25 — "Résultats" tab: the three funded OSIRIS25 projects. 404 in browser on 2026-11-19; WAF challenge for curl; no Wayback capture.
- https://hl7.eu/affiliate_fr.html — 404 in browser on 2026-11-19; confirm whether HL7 Europe now lists a non-interim HL7 France chair.
- https://www.interopsante.org/association — login-protected; may list HL7 France chair and 2026 board.
- https://esante.gouv.fr/offres-services/ci-sis/espace-publication — site in maintenance on 2026-11-19; confirm the cancer volet rows as of today (last Wayback copy used is 2026-01-01).
- https://industriels.esante.gouv.fr/sites/default/files/media/document/Webinaire_CGTS.pdf and https://industriels.esante.gouv.fr/sites/default/files/media/document/webinaire_nrc_feuille_route.pdf — ANS CGTS/NRC decks (server returns HTML to curl); may name the CGTS lead and date.
- https://www.cancer.fr/content/download/124863/file/Cahier%20des%20charges%20fonctionnel_PDE-MES-PPS-CANCER_2026.04_ERRATUM_VF.pdf?version=3 — functional spec of the DCC / Mon espace santé programme (WAF); check for any FHIR element.
- https://esante.gouv.fr/appel-projets-evolution-du-dossier-communicant-de-cancerologie-dcc — live page (Incapsula); confirm laureate table and any 2026 update beyond the Wayback copy.

### france-landscape

Method: French/English web searches, curl with browser user-agent into `scratchpad/survey/fr-nonfhir-dl/`, HTML-to-text with a script kept in `scratchpad/survey/scripts/` (run with `python3 -I`), `pdftotext -layout` for PDFs, web.archive.org for blocked sites (no archived copies existed for oeci.eu/Accreditation or cancer.fr/Media/files).

#### VERIFIED (n/f replaced by fact + URL)

1. **ENCR membership of French registries**: 25 French entries with directors obtained from the ENCR contact list filtered on France (`field_country_target_id=12`, pages 0–2). https://encr.eu/encr-members-contact-list?field_country_target_id=12 (and `&page=1`, `&page=2`).
2. **OECI-accredited French centres**: full list with designation levels from the OECI accreditation site (browser cross-check by team lead 2026-11-19 confirmed the same 18 certified French centres, capture at scratchpad/verify/oeci-centres-2026-11-19.txt; the home page does not show designation types, the certified-centres page does): 15 "Comprehensive Cancer Centre with Research Excellence", 1 CCC (IUCT Oncopole), 1 Comprehensive Cancer Network (ATOP Toulouse), 1 Cancer Centre (Antoine Lacassagne), 7 "In Accreditation". https://accreditation.oeci.eu/certified-centres/ ; dated confirmations: Jean Perrin 22 Apr 2026 https://www.cjp.fr/a-la-une/actualites/actualite/le-centre-jean-perrin-accredite-comprehensive-cancer-center-par-loeci ; Baclesse https://www.baclesse.fr/en/baclesse-accredited-by-the-organization-of-european-cancer-institutes-oeci/ ; OECI Warsaw 2026 programme https://www.oeci.eu/Attachments/Warsaw_26/OECI_Warsaw_2026_Final_15_MAY.pdf
3. **CLIP² list 2024–2029**: 16 CLIP² (8 adult+paediatric) from the INCa deck presented at the phases-précoces meeting (Feb 2025), plus 2025 wave (IPC) giving 19 adult structures. https://www.phases-precoces.fr/wp-content/uploads/2025/02/3-2024_PPC_Diaporama_Actualisation.pdf ; https://alliance-cancer.org/clip2-2/ ; https://institutpaolicalmettes.fr/wp-content/uploads/2025/03/CP-IPC-labellise-CLIP2-par-l-INCa.pdf
4. **Francim base commune common variables and coding**: mandatory and complementary variables, CIM-O-3 + UICC TNM, ENCR/Francim rules, annual integration at HCL. https://www.chu-dijon.fr/registre-bourguignon-des-cancers-digestifs ; history/size (1999, 1.7 M cases 1975–2017) https://www.edimark.fr/revues/correspondances-en-onco-hematologie/n-4-septembre-2020/le-reseau-francais-des-registres-descancers-francim-un-acteur-majeur-de-lepidemiologie-des-cancers-en-france ; 32 registries evaluated by CER at 31 Dec 2023, 27 in the partnership https://registre-tumeurs-29.fr/Accueil/les-registres-des-cancers-en-france/
5. **EUCAIM French partners** confirmed on the official partner page (AP-HP, CNRS, CERF, Inria, LIMICS, Medexprim; Owkin left Dec 2023). https://cancerimage.eu/partners/
6. **canSERV French participants**: IARC/CIRC Lyon, ECRIN, EMBRC-ERIC. https://cordis.europa.eu/project/id/101058620
7. **UNCAN-Connect French partner**: Alia Santé (no French cancer centre or INCa). https://www.srdc.com.tr/rndprojects/uncan-connect/
9. **Décret 2025-1366 full text** (browser check by team lead 2026-11-19): https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053177576 ; confirmed articles R. 1415-2-1 to R. 1415-2-6, nine sources, 11 data categories, NIR/IPP/episode identifiers, retention 24 months / 20 years / 8 months logs, scientific and ethics committee, INCa-run information system for local registries with annual transmission to the base commune, no data format or interoperability standard named. Report updated; the decree now replaces the CNIL mirror as primary source for decree facts.
8. **HDAB (ORAD) designation under EHDS**: none yet; PDS expected, legislative vehicle 2026, EHDS applies 26 Mar 2027. https://gnius.esante.gouv.fr/sites/default/files/2025-11/English%20version_The%20French%20National%20Strategy%20for%20Artificial%20Intelligence%20and%20Health%20Data.pdf ; https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cenum/l17cenum2526033_compte-rendu.pdf ; https://www.donneespersonnelles.fr/espace-europeen-donnees-sante ; https://esante.gouv.fr/doctrine/usage-secondaire-donnees-sante

#### CORRECTED (old vs new)

1. **Unicancer OMOP**: old "n/f" → new: no production OMOP conversion exists; the 2024 ConSoRe paper names bridging the ConSoRe common data model to OMOP-CDM as a planned next step, and the Centre Léon Bérard 2024 paper states the goal to align OSIRIS with OMOP and FHIR. https://pdfs.semanticscholar.org/9d0a/3840b7bdf51ba2869686e1b438c2099e1294.pdf ; https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0000415
2. **OECI**: old partial list (6 names, status uncertain) → new full list of 25 French entries with designation levels (see VERIFIED 2). Gustave Roussy, Curie, Léon Bérard, Paoli-Calmettes, Bergonié, ICO etc. are "CCC with Research Excellence"; Lacassagne is "Cancer Centre"; CGFL is "In Accreditation" (earlier search result said "Cancer Centre").
3. **CLIP²**: old "list not retrievable, 2024–2029 labels e.g. Lacassagne, IPC" → new: 16 CLIP² labelled July 2024 (named), 19 adult structures after the 2025 wave, 8 paediatric.
4. **Screening IS ("Siden")**: old plain n/f → new: regulatory architecture from the arrêté of 16 Jan 2024 (one regional business software + one regional database per CRCDC; national INCa IS for cervical screening), vendor example OSI Santé Zeus; the name "Siden" itself remains unfound. https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049025564 ; https://www.osi-sante.fr/Depistage/
5. **"Oncodata"**: old n/f → new: no French platform of that name; nearest is Unicancer/Roche Onco Data Hub (ODH). https://www.unicancer.fr/en/programs/onco-data-hub/
6. **SeqOIA report**: old n/f → new (partial): dematerialised pathway via SPICE e-prescription tool (spice.aphp.fr), result returned as a "compte-rendu d'examen de biologie médicale" to downstream RCPs. Machine-readable format still unfound. https://laboratoire-seqoia.fr/nos-activites/ ; https://fimarad.org/wp-content/uploads/2021/10/Pre%CC%81sentation-SeqOIA-Michel-Vidaud.pdf

#### STILL NOT FOUND

1. **Francim base commune file format / ICD-O-3 edition / multiple-primary rule version**: tried francim-reseau.org (subpages 404), Wikipedia FRANCIM, Edimark 2020 article, registry sites (Dijon, Finistère, Bas-Rhin methodology page 404), cancer.fr readme 2018, searches on "dictionnaire des variables" Francim. Only the common-variable list (Dijon) exists publicly.
2. **IACR membership of French registries**: IACR member directory requires login (cinportal.iarc.fr); iacr.com.fr shows only publications; searches returned nothing.
3. **Francim president / bureau**: not on francim-reseau.org, Wikipedia, Edimark, registry sites; searches with candidate names returned nothing.
4. **"Siden"**: no hit in any French source (searches with CRCDC, Assurance maladie, vendor names).
5. **"Oncodata"** as a named French platform: no hit beyond Onco Data Hub.
6. **SeqOIA/AURAGEN machine-readable report format**: SeqOIA site, Vidaud deck, PFMG2025 documents describe process only.
7. **French cancer centres as EUCAIM data holders**: cancerimage.eu partner page lists no cancer centre; data-holder roster not public.
8. **ECHoS French consortium partner**: not confirmed (INCa runs "Hub Cancer France" but the ECHoS partner list was not retrieved).

#### NEEDS BROWSER (blocked or JS-rendered for automated fetch)

- esante.gouv.fr was in maintenance on 2026-11-19 ("Page de maintenance ANS"), so none of the ANS pages below could be verified in the browser either; retry later.
- https://esante.gouv.fr/interoperabilite/ci-sis/espace-publication (CI-SIS publication space, cancer volets status table) — curl returns 776-byte challenge page.
- https://esante.gouv.fr/volet-frcp-fiche-de-reunion-de-concertation-pluridisciplinaire and https://esante.gouv.fr/volet-cancer-pps-programme-personnalise-de-soins-en-cancerologie — same block.
- https://esante.gouv.fr/sites/default/files/media/document/20260519%20-%20support%20HDH.pdf (PDS presentation May 2026 on ORAD/EHDS) — not fetched.
- https://gnius.esante.gouv.fr/sites/default/files/2025-11/English%20version_The%20French%20National%20Strategy%20for%20Artificial%20Intelligence%20and%20Health%20Data.pdf — returns HTML instead of PDF via curl.
- https://www.cancer.fr/Media/files/liste-des-centres (CLIP² list), https://www.e-cancer.fr/Professionnels-de-sante/Les-therapies-ciblees/Essais-cliniques-et-therapies-ciblees/Les-CLIP2 , https://www.e-cancer.fr/Institut-national-du-cancer/Appels-a-projets/Appels-a-projets-en-cours/CLIP2-2025-2029 , https://www.cancer.fr/content/download/141527/file/PANOKFR2026_Panorama%20des%20cancers%202026.pdf?version=3 , https://www.cancer.fr/content/download/124863/file/Cahier%20des%20charges%20fonctionnel_PDE-MES-PPS-CANCER_2026.04_ERRATUM_VF.pdf?version=3 — cancer.fr returns 315-byte challenge page to curl (the HDH and Senate PDFs were fetched fine).
- RESOLVED 2026-11-19: decree full text verified in the browser at https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053177576 (the id 052859580 tried by curl was wrong; aphp returned nothing).
- https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049025564 (arrêté 16 Jan 2024 on screening programmes, annex on information systems).
- https://www.oeci.eu/MemberList.aspx (fetched, 1.4 MB, not parsed; the accreditation site sufficed) and oeci.eu/Accreditation/* (404 / not archived).
- https://cinportal.iarc.fr (IACR registry portal, login).
- https://www.sciencedirect.com/science/article/pii/S2949820125005442 (CDISC-SDTM to OMOP conversion of a French oncology RWD database; affiliation unknown) — text not extractable.
- https://www.esante-occitanie.fr/app/uploads/2025/12/Presentation-DCC-ATs.pdf (404) and https://www.francim-reseau.org/le-reseau , /la-base-commune (404).

### france-terminology

Scope: every item marked "n/f" in the report of 2026-11-18, plus a re-check of the four priority items (ICD-O-3 revision used by Francim and the RNC, TNM edition policy, French SNOMED edition required vs optional, national chemotherapy thesaurus). Methods: French-language web searches, direct queries of the ANS FHIR terminology endpoint `https://smt.esante.gouv.fr/fhir`, web.archive.org copies of JavaScript-rendered or Incapsula-protected esante.gouv.fr pages and PDFs, curl plus pdftotext into `/private/tmp/claude-501/-Users-thome-code-fhir-profiling-cancer-common/3cc04596-744d-4990-addb-ce34993d093b/scratchpad/fr-term-dl/verif/`. One attempt to re-fetch esante.gouv.fr with a browser-like User-Agent was refused by the tool permission layer and was not repeated; archived copies were used instead.

Counts: **VERIFIED 9 · CORRECTED 8 · STILL NOT FOUND 9**.

#### VERIFIED (fact confirmed, with URL)

1. **SNOMED CT licence is free** — archived ANS page: "A noter que l'accès et l'utilisation de cette terminologie sont soumis à l'acceptation et au respect d'une licence gratuite." http://web.archive.org/web/20260513141142/https://esante.gouv.fr/produits-services/cgts/snomed-ct
2. **No France package on SNOMED MLDS** — the public release-package API lists no French edition (SMT-only distribution). https://mlds.ihtsdotools.org/api/releasePackages
3. **National registry decree names no terminology** — art. R. 1415-2-2 CSP (créé par décret 2025-1366): "5° Les données concernant les caractéristiques et la classification des tumeurs et la date de diagnostic du cancer" and sources "2° Les registres locaux des cancers ... ainsi que leur base de données commune dont l'Institut national du cancer assure l'hébergement". https://kohenavocats.fr/?p=1791911 and http://web.archive.org/web/20260407080804/https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053177576
4. **SMT has no ADICAP↔SNOMED alignment** — `ConceptMap` search returns total 4: BDPM↔CIP_UCD (2026-11), NUVA↔ATC, NUVA↔BDPM, NUVA↔CIP_UCD (1.0.1175). https://smt.esante.gouv.fr/fhir/ConceptMap?_elements=url,version
5. **PPS 2025.01 binds no tumour or drug terminology** — bindings are jdv-type-traitement-pps-cisis (1.2.250.1.213.1.1.5.478), jdv-mode-administration-cisis (.5.75), jdv-gestion-effet-secondaire-cisis (.5.477), jdv-mesure-associee-cisis (.5.476), jdv-type-de-suivi-cisis (.5.76), jdv-soin-onco-de-support-cisis (.5.79), jdv-type-accompagnement-sociopro-cisis (.5.81); templateId 1.2.250.1.213.1.1.1.26; 2025.01 history: JDV renaming, setId/versionNumber [1..1], new sections. http://web.archive.org/web/20260420085656/https://esante.gouv.fr/sites/default/files/media_entity/documents/CI-SIS_VOLET_CONTENUS_CANCER-PPS_SFD_2025.01_20250827.pdf
6. **ICD-O-4 status at IARC** — "the fifth edition of the WHO Blue Books would be followed by a new (fourth) edition of the International Classification of Diseases for Oncology (ICD-O-4) ... five-digit morphology codes". https://tumourclassification.iarc.who.int/icd-o-4/
7. **Mon espace santé PPS programme** — results published 9 April 2026; "lancement effectif en mars 2026"; "En 2029, date prévisionnelle de fin du déploiement ... près de 5 millions de PPS"; RCP and PPS data will feed the national registry. http://web.archive.org/web/20260720163351/https://esante.gouv.fr/espace-presse/l-institut-national-du-cancer-et-l-agence-du-numerique-en-sante-publient-les-resultats-de-l-appel
8. **Instruction ministérielle on RNC data transmission exists** — n° DGS/SP5/2026/161 of 16 Nov 2026, Bulletin officiel Santé; INCa: "Le rythme, la date ainsi que le format d'envoi pourront être précisés lors d'ateliers dédiés"; interoperable RCP/PPS framework "publié en avril 2026 ... 13 régions". https://toute-la.veille-acteurs-sante.fr/247016/publication-de-linstruction-ministerielle-sur-les-modalites-de-transmission-des-donnees-au-registre-national-des-cancers-une-etape-majeure-dans-le-deploiement-operationnel-du-registre-comm/
9. **ENCR rule followed by French registries** — "Selon la dernière version de la CIM-O"; "Un registre doit enregistrer l'édition de la classification TNM utilisée pour chaque année" (French translation by Registre du Tarn). https://encr.eu/sites/default/files/Recommendations/ENCR-Recommendation-standard-dataset_Mar2023_FR.pdf

#### CORRECTED (old → new, with URL)

1. **SNOMED CT required vs optional in CI-SIS** — old: n/f. New: SNOMED CT is a CI-SIS "terminologie de référence" for anatomy, microbiology results, drugs, ophthalmology and statuses (CGTS list of Nov 2023: CIM-10 pathologies, CIM-11 allergies, CCAM acts, SNOMED anatomy/microbiology, LOINC biology/radiology, EMDN devices, EDQM routes; "137 JDV utilisent la SNOMED CT"); the 2022 decision chose SNOMED for anatomical localisations; for microbiology labs may choose NCBI Taxonomy or SNOMED and double coding is "pas attendu des éditeurs et laboratoires" under Ségur. Neither SNOMED in general nor the French edition is mandated by a text found. http://web.archive.org/web/2026/https://esante.gouv.fr/sites/default/files/media_entity/documents/5a---utilisation-de-la-snomed-ct-dans-le-ci-sis.pdf ; http://web.archive.org/web/2026/https://esante.gouv.fr/espace-presse/interoperabilite-semantique-la-france-choisit-la-snomed-ct-pour-la-description-des-localisations-anatomiques ; http://web.archive.org/web/2026/https://esante.gouv.fr/espace-presse/le-ncbi-taxonomy-et-la-snomed-ct-deviennent-les-deux-terminologies-de-reference-pour-le-ci-sis
2. **SNOMED affiliate licence** — old: standard affiliate + national licence. New: ANS RETEX 25 June 2026 adds "Grâce aux négociations menées par l'ANS, la licence d'affiliation a été modifiée pour tous les pays membres" (reversibility, open alignments, IP protection of ANS content, French text prevails). http://web.archive.org/web/20260812093333/https://esante.gouv.fr/sites/default/files/media/document/ANS_RETEX_implementation_SNOMEDCT-ANS-260625.pdf
3. **LOINC Bio FR maintenance consortium** — old: AP-HP, Vidal, Mondeca, SFIL, Phast, CHU de Rouen. New (ANS page updated 21 Nov 2025): "un consortium regroupant ONAOS, PHAST, la Société Française de Biologie Clinique et PixLib"; the older list is the 2020 consortium. http://web.archive.org/web/20260514011604/https://esante.gouv.fr/jeu-de-valeurs-loinc
4. **LOINC linguistic variant fr-FR** — old: partially n/f. New: UMLS source LNC-FR-FR "LOINC Linguistic Variant - French, France", version 2.77 (Feb 2024), producer ASIP Santé; Regenstrief credits ASIP Santé with AP-HP, SFIL, Vidal, Mondeca; 49 437 concepts in the France variant (2020). https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/LNC-FR-FR/metadata.html ; https://loinc.org/international/french/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC8075467 (facts from search snippets; pages themselves block automated fetch)
5. **OSIRIS drug coding** — old: n/f for UCD/ATC use. New: OSIRIS Oncology-related Medication Statement binds `medication[x]` to WHO ATC (IPS value set `http://hl7.org/fhir/uv/ips/ValueSet/whoatc-uv-ips`, extensible) with SNOMED CT medication codes as example binding. https://ig-osiris.cancer.fr/ig/osiris/StructureDefinition-onco-medication-statement.html
6. **National chemotherapy thesaurus** — old: n/f. New: INCa publishes a national "Recommandations et référentiels / Thésaurus" collection of systemic-treatment recommendations (sein RE+/HER2- Oct 2025; CBNPC 1re ligne 2025), coordinated with learned societies; these are recommendation texts, not UCD/ATC-coded protocol records; a coded national protocol base remains not found. https://www.onconormandie.fr/wp-content/uploads/nr-files/INCa_RBP_Sein_RHHER2-_ThesaurusQ1_2025.pdf ; https://www.onco-hdf.fr/app/uploads/2025/02/THCBNPC25_Th_CBNPC_metastatique-sans_addiction_onco-2.pdf ; https://www.hauts-de-france.ars.sante.fr/media/100053/download
7. **TNM edition in French registries** — old: n/f. New: Registre des cancers d'Aquitaine colon-rectum sheet: "La classification TNM de l'Union international contre le Cancer (UICC) 8ème édition" (single registry; network policy still not found). https://sites.bph.u-bordeaux.fr/REGISTRES-CANCERS-AQUITAINE/Rg/document/Colon_rectum_fiche_descriptive.pdf
8. **SMT / CGTS 2026 roadmap** — old: n/f. New (SantExpo 22 May 2026 deck): 48 terminologies, 314 FHIR CodeSystems (250 MOS/NOS), 810 ValueSets, 4 ConceptMaps, 8 alignments; Oct 2026 features (download of previous versions, mapping search, AI EN→FR translator); EHDS terminology orientation "LOINC, SNOMED CT, ICD10, CIM-O, orphanet (discussion en cours; actes d'exécution non encore publiés)", CI-SIS to be updated accordingly; doctrine 2026: SMT interface with Sesali; Comité ENS Apr 2026: terminology choices left to eHN Semantic. http://web.archive.org/web/20260712150558/https://esante.gouv.fr/sites/default/files/media/document/202605_SantExpo_Prez_SMT%20FTS_VF.pdf ; http://web.archive.org/web/20260411210421/https://esante.gouv.fr/sites/default/files/media_entity/documents/doctrine-2026_modifications_20251125.pdf ; http://web.archive.org/web/20260514114810/https://esante.gouv.fr/sites/default/files/media/document/20260422_Comit%C3%A9ENS_VF.pdf

#### STILL NOT FOUND (what was tried)

1. **ICD-O-3 revision (3.1 vs 3.2) used by Francim / the RNC base commune** — tried: French searches (Francim, HCL, SpF, "CIM-O-3.2", "deuxième révision", "base commune"), ODISSE dataset pages, 2021 survival report, ENCR dataset, decree text, INCa designation procedure (404 to curl), SpF incidence 2019 vol. 1 and BEH 2023 (JS download pages), IACR ICD-O-3.2 page (403). Only "CIM-O3" without revision is stated anywhere.
2. **French translation of ICD-O-3.2 and its publisher** — tried: IARC publications (404 on two French-translation PDFs), ICCP portal (French 3rd ed. 2008 only), IACR (403), searches on Québec/Suisse/Belgique translations.
3. **INCa/Francim plans for ICD-O-4** — tried: cancer.fr searches, IARC ICD-O-4 page (status only).
4. **French national position on UICC TNM 9th edition** — tried: INCa (only Nota Bene veille items), SFP, AFAQAP, SFRO, Unicancer, TNCD 2026, SpF Enquêtes Stade fiche (JS download). Only regional AURA 2026 lung guideline and UK/German positions found.
5. **Formal AJCC vs UICC preference statement in French practice** — tried: searches on INCa/SFP minimum data (2011 only), TNCD (cites "AJCC et UICC").
6. **Mandate of the French SNOMED edition or SNOMED-specific requirement for Mon espace santé** — tried: doctrine 2026 PDF (no SNOMED mention), Ségur webinar, décret 2026-153 (Légifrance 403; ANS news page not archived as text), PPS call documents (cancer.fr 404 to curl).
7. **Coded national chemotherapy protocol database (ResOMEDIT) with UCD/ATC versions** — tried: resomedit.fr homepage (no protocol section visible), OMEDIT/INCa searches, ARS Hauts-de-France 2022 deck (mentions "mutualisation à l'échelle nationale" as work in progress).
8. **CCAM use in cancer registries** — tried: Francim/registry searches; no source.
9. **Terminology versions pinned by Mon espace santé itself** — tried: PPS call presentation (cancer.fr 404), Ségur vague 2 webinar; Mon espace santé consumes CI-SIS documents whose volets carry the versions.

#### NEEDS BROWSER (block automated fetch; please read with a real browser)

- https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053177576 (décret 2025-1366 full text; archived copy used) and https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000053199368/2026-07-24 (section R. 1415-2-1 à -6) — 403.
- Décret n° 2026-153 du 3 mars 2026 (JORF 4 mars 2026) on sanctions for non-compliance with interoperability referentials — Légifrance 403; check whether any SNOMED-bearing CI-SIS volet is listed.
- Instruction ministérielle n° DGS/SP5/2026/161 du 16 novembre 2026 (Bulletin officiel Santé) — not located; may state coding/format rules for RNC transmissions.
- https://www.cancer.fr/Media/documents/registre-national-des-cancers/volet-2-dossier-evaluation-du-dossier-de-candidature-pour-la-designation-et-l-evaluation-des-organismes-mettant-en-aeuvre-des-registres-locaux-des and the matching "volet-1" and "procedure-de-designation" documents — 404 to curl; may list coding standards (CIM-O, TNM, ENCR) required of local registries.
- https://www.cancer.fr/content/download/116974/file/PDE-MES-PPS-CANCER%202025_Pr%C3%A9sentation%20appels%20%C3%A0projets.pdf?version=2 and https://www.cancer.fr/content/download/141527/file/PANOKFR2026_Panorama%20des%20cancers%202026.pdf?version=3 — 404 to curl.
- https://santepubliquefrance.fr/content/download/190597/2335082 (incidence 1990–2018 vol. 1, methods), https://santepubliquefrance.fr/content/download/545862/3958555?version=1 (BEH 2023 incidence article), https://santepubliquefrance.fr/content/download/35124/674513?version=1 (Enquêtes Stade fiche) — JavaScript download pages.
- https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/LNC-FR-FR/metadata.html and https://loinc.org/international/french/ — 403 / JS; confirm current LNC-FR-FR version and producer.
- http://www.iacr.com.fr/index.php?option=com_content&view=article&id=149&Itemid=662 (ICD-O-3.2 tables and translations) — 403.
- https://esante.gouv.fr/sites/default/files/media/document/Comit%C3%A9ENS_09072026.pdf , https://esante.gouv.fr/sites/default/files/media/document/ComiteENS_30092026.pdf , https://esante.gouv.fr/sites/default/files/media/document/20260618_CNS_presentation_VF_0.pdf — Incapsula, not archived.
- https://industriels.esante.gouv.fr/sites/default/files/media/document/4-Retour_experience_implementation_SNOMED-ANS-20250918.pdf — returns HTML stub to curl.
- https://esante.gouv.fr/interoperabilite/ci-sis/espace-publication — only a 2022 archive exists; live page needed for the current volet list.
- Francim network site (no stable URL found) — for any coding manual naming the CIM-O revision and TNM edition.

### germany

Scope: every "n/f", "snippet", "not verified" or secondary-only statement in `germany-landscape.md` and `germany-fhir.md`. Downloads in `scratchpad/dl-verify-de/` (curl + pdftotext/pandoc). Backups of the pre-edit reports in `scratchpad/verify-scripts/*.bak`.

| Status | Count |
|---|---|
| VERIFIED (n/f replaced with fact + URL) | 27 |
| CORRECTED (report text was wrong or outdated) | 4 |
| STILL NOT FOUND, re-searched | 15 |
| STILL NOT FOUND, not re-searched in this pass | 9 |

#### Items

| # | File / section | Item | Status | Fact and source, or what was tried |
|---|---|---|---|---|
| 1 | landscape 1.2 | oBDS-RKI version | CORRECTED | Was "3.0.0.8_RKI" from a search snippet. Current is oBDS_v3.0.4_RKI, Zenodo 2026-05-26, https://zenodo.org/records/20397623 (supersedes 3.0.0.8a_RKI, https://zenodo.org/records/10022040). |
| 2 | landscape 1.1 | Hessen law text | CORRECTED | Abbreviation is KRG HE, not "HKRG". https://www.rv.hessenrecht.hessen.de/bshe/document/jlr-NNLHE000053D9 ; KRGV HE jlr-NNLHE000052C8 |
| 3 | fhir Part B §3 | SNOMED 2027 pin "not found" | CORRECTED | Aligned with Part A: 2027 ballot pins International 20260701 (release notes v2027.0.0-ballot). |
| 4 | fhir MV § 64e | Evaluation consortium | CORRECTED | Was "HCHE, Humangenetik Innsbruck". Also USZ Zürich Onkologie; awarded July 2025; kickoff 10.02.2026. GKV-SV MV page. |
| 5 | landscape 1.1 | Hamburg law text | VERIFIED | https://www.landesrecht-hamburg.de/bsha/document/jlr-KrebsRegGHAV6P1 ; Senate 03.03.2026 approved 6th amendment (Drs. 2026/00502) incl. § 8a FDZ linkage, transparenz.hamburg.de PDF. |
| 6 | landscape 1.1 | KrebsRG M-V | VERIFIED | https://www.landesrecht-mv.de/bsmv/document/jlr-KrebsRGMVV4P7 |
| 7 | landscape 1.1 | GKKN (Niedersachsen) | VERIFIED | voris link via https://kk-n.de/ueber-uns/rechtsgrundlagen/ |
| 8 | landscape 1.1 | SKRG (Saarland) | VERIFIED | https://recht.saarland.de/bssl/document/jlr-NNLSL00009DC3 |
| 9 | landscape 1.1 | KRG LSA | VERIFIED | Law of 05.12.2024, https://www.landesrecht.sachsen-anhalt.de/bsst/document/jlr-NNLST000041E3 |
| 10 | landscape 3.2 + 6 | FDZ Gesundheit head | VERIFIED | Dr. Steffen Heß, vdek-Magazin 06.10.2026 signed article; BMG KI-FDZ page. BfArM org chart URL 404. |
| 11 | landscape 4.2 | Total certified centres | VERIFIED | 2,245 centres / 2,324 sites on 31.12.2025; 492 hospitals, 443 in Germany. OZ-Jahresbericht 2026 §2.2, §2.4. |
| 12 | landscape 4.2 | Certification commission chairs | VERIFIED | Graeven, Fehm, Bokemeyer (OZ commission); OnkoZert Odenwald, Sommerfeldt. Same report. |
| 13 | landscape 4.5 | EUCAIM German partners | VERIFIED | 8 entries under Germany, Wayback copy 04.11.2026 of https://cancerimage.eu/partners/ |
| 14 | landscape 4.5 | ENCR German members | VERIFIED | Two "Germany" headings (pagination) with 11 registry entries, from the saved ENCR list. Added as a new bullet. |
| 15 | landscape 4.5 | OECI German centres | VERIFIED | None on https://accreditation.oeci.eu/ . Added as a new bullet. |
| 16 | landscape 4.6 | EHDEN country breakdown | VERIFIED | Germany 10 partners incl. DKG and Krebsregister RLP, https://www.ehden.eu/datapartners/ |
| 17 | landscape 4.7 + 6 | Onkopedia editors | VERIFIED | No editor named; Impressum lists DGHO board, https://www.onkopedia.com/de/impressum |
| 18 | landscape 6 | Lablans on DKTK CCP-IT page | VERIFIED | Wayback copy 23.01.2026 of the CCP-IT page. |
| 19 | landscape 6 | TMF Vorstand chair | VERIFIED | Prof. Dr. Rainer Röhrig, TMF Jahresbericht 2025. |
| 20 | landscape 3.5 | Mainzelliste versions | VERIFIED | v1.13.10 (Bitbucket tag 2026-06-15; Docker 2026-11-18); GUI v1.0.3. |
| 21 | landscape 3.5 | gPAS / E-PIX / gICS versions | VERIFIED | 2026.1.3 / 2026.1.3 / 2026.1.4 on Docker Hub mosaicgreifswald. |
| 22 | fhir FDPG | Onkologie module in FDPG ontology | VERIFIED | fhir-ontology-generator v4.1.0, 2026-05-15, PR #341. Production portal deployment not separately confirmed. |
| 23 | fhir ICD-O | bfarm ICD-O-3 canonical | VERIFIED | ZTS catalog: THO canonical maps to bfarm.terminologien.icdo3 2019.0.0; fhir.de canonical returns none. |
| 24 | fhir SNOMED | August edition release id | VERIFIED | 20260815, module 11000274103. RF2 metadata via local Snowstorm; not on BfArM pages. |
| 25 | fhir SNOMED | International dependency | VERIFIED | International 20260701 (same source). |
| 26 | fhir SNOMED | Namespace | VERIFIED | 1000274 (same source). |
| 27 | fhir SNOMED | Oncology refsets | VERIFIED | None in German Edition 20260815 (refset list from same source). |
| 28 | fhir HGNC | HGNC system URI | VERIFIED | Binding to GR hgnc-vs, system http://www.genenames.org (GR 3.0.0 JSON). |
| 29 | fhir ZTS | FHIR REST terminology endpoint | VERIFIED | Absent: /fhir/metadata 404; $lookup rejected 400. |
| 30 | fhir ZTS | ICD-11 on ZTS | VERIFIED | Absent from the 14-package catalog. |
| 31 | landscape 4.4 | MV § 64e Zwischenbericht | VERIFIED | Annual report is required; none published (GKV-SV page). Extension stays n/f (see 37). |
| 32 | landscape 1.1 | BW Krebsregistergesetz adoption | STILL NOT FOUND | Web searches for Landtag Drucksachen and the Gesetzblatt; Sozialministerium and krebsregister-bw.de pages. No adoption found; the Ministry still cites the LKrebsRG. |
| 33 | landscape 3.3 | First productive Krebsregister–FDZ linkage | STILL NOT FOUND | Kachel slides (Wayback) and GDNG searches. Only legal preparation found (Hamburg § 8a). |
| 34 | landscape 1.6 | IGES report text URL | STILL NOT FOUND | Searched for the report PDF; only the AOK and DKR statements exist. |
| 35 | landscape 2.1 | ZfKD 2024 data (secondary source) | STILL NOT FOUND | DataCite search shows records up to Stand 2025-11-11; no primary statement on 2024 data. |
| 36 | landscape 3.4 | Broad Consent counts | STILL NOT FOUND | MII AG Consent slides 09/2025 contain a chart without readable totals. |
| 37 | landscape 4.4 | genomDE extension beyond 5 years | STILL NOT FOUND | GKV-SV page and searches. |
| 38 | landscape 3.4 | "NUM-FDP" | STILL NOT FOUND | NUM site search returned 404. |
| 39 | landscape 5.4 | BDP synoptic-reporting paper | STILL NOT FOUND | Searches found only the BDP accreditation paper 05.03.2026. |
| 40 | landscape 5.5 | KIM ~1 bn messages (secondary) | STILL NOT FOUND | The gematik KIM page has no figure; the TI-Dashboard is JS-only (see NEEDS BROWSER). |
| 41 | landscape 5.6 | Mika / optimune / Pro-React Onco status | STILL NOT FOUND | DiGA FHIR API returns 401; directory is JS-only; Ärzte Zeitung pages block fetch. |
| 42 | landscape 4.1 + 6 | NCT single director | STILL NOT FOUND | Only site-level leadership exists in sources (e.g. Heidelberg, Dresden). |
| 43 | fhir terminology | oBDS→SNOMED national mapping (Landeskrebsregister + BfArM) | STILL NOT FOUND | Only the MII module's own ConceptMaps exist. |
| 44 | fhir ICD-O-4 | BfArM ICD-O-4 statement | STILL NOT FOUND | BfArM ICD-O-3 page has no ICD-O-4 mention. |
| 45 | fhir CTCAE | Official German CTCAE | STILL NOT FOUND | NCI and search; only German PRO-CTCAE exists. |
| 46 | fhir MedDRA | German MedDRA version | STILL NOT FOUND | meddra.org is JS-only; BioPortal MDRGER shows 28.0 (secondary). |
| 47 | landscape 1.4 | Registry core-software list | STILL NOT FOUND | Not re-searched in this pass. |
| 48 | landscape 3.1 | GBE cancer indicators | STILL NOT FOUND | Not re-searched in this pass. |
| 49 | landscape 4.3 | MII oncology use-case 2026 status | STILL NOT FOUND | Not re-searched beyond item 22. |
| 50 | landscape 5.1 | Market shares | STILL NOT FOUND | Not re-searched in this pass. |
| 51 | landscape 5.3 | HiGHmed oncology archetypes release | STILL NOT FOUND | Not re-searched in this pass. |
| 52 | landscape 6 | EHDS named national contact | STILL NOT FOUND | Not re-searched in this pass. |
| 53 | fhir UICC | UICC licence terms; TNM9 in SNOMED | STILL NOT FOUND | Not re-searched in this pass. |
| 54 | fhir DNPM | DNPM FHIR profiles | STILL NOT FOUND | Not re-searched in this pass. |
| 55 | fhir HL7 Europe | Other German work with HL7 Europe | STILL NOT FOUND | Not re-searched in this pass. |

#### NEEDS BROWSER

- https://plattform65c.atlassian.net/wiki/x/BICdAg — the Confluence body is not retrievable by automated fetch. This is now superseded by Zenodo for the oBDS-RKI version.
- https://diga.bfarm.de/de/verzeichnis — JS-only. The API returns 401. Needed to check the status of Mika, optimune and Pro-React Onco.
- https://www.gematik.de/telematikinfrastruktur/ti-dashboard — JS-only. Needed for current KIM message counts.
- https://www.aerztezeitung.de/ articles on Mika (420611, 418315) — a bot check returns a 294-byte stub.
- https://cancerimage.eu/partners/ — the live page times out. A Wayback copy was used.
- https://dktk.dkfz.de/ CCP pages — the live pages return 404 to automated fetch. Wayback copies were used.
- https://www.meddra.org/ — JS-only.
- https://terminologien.bfarm.de/packages/bfarm.terminologien.icdo3/2019.0.0 — the download needs acceptance of the Downloadbedingungen to get a token. This was not done.

### islands-uk

Pass run 2026-11-19. Method: direct curl of organisation pages and PDFs (pdftotext), Simplifier package catalog, TRUD guest pages, OECI/BBMRI-ERIC/EHDEN/EUCAIM/EUCanScreen/TEHDAS2/JANE partner pages, Wayback Machine (rate-limited after one request), targeted English and Greek searches. Outcomes: VERIFIED (fact now sourced), CORRECTED (old statement replaced), STILL NOT FOUND (what was tried). Edited statements in the two report files carry "(verified 2026-11-19)".

#### United Kingdom

1. COSD FHIR IG exists? VERIFIED negative. Simplifier catalog has no "cosd" package; "cancer" returns only US/international IGs. https://packages.simplifier.net/catalog?name=cancer
2. Oncology FHIR IGs Scotland/Wales/NI. STILL NOT FOUND. Tried Simplifier catalog, fhir.r4.wales 2.7.0 profile list.
3. COSD submission format and version. VERIFIED/CORRECTED: TRUD "Cancer Outcomes and Services Data Set XML Schema" release 10-2-0 released 27 Mar 2024, usable from 1 Apr 2024 (DAPB1521, produced by NDRS), Pathology XML Schema 5-1-1; enquiries nhsdigital.cosdenquiries@nhs.net. https://isd.hscic.gov.uk/trud/users/guest/filters/0/categories/1/items/246/releases . Team lead (browser, 2026-11-19): NHS Standards Directory confirms COSD v10.0, DAPB1521 Amd 89/2022, published 2023-09-11, Active, Pathology v5.0, acute-setting scope https://standards.nhs.uk/published-standards/cancer-outcomes-and-services-data-set (VERIFIED). User guide v10.2.x minor versions / v11 statements: STILL NOT VERIFIED (digital.nhs.uk Cloudflare check; PDF blocked; Wayback rate-limited; openprescribing mirror denied by permission classifier).
4. SNOMED CT UK Clinical Edition latest release. VERIFIED (was not found): 43.0.1 released 20 Oct 2026 (replaces 43.0.0 of 6 Oct 2026); 42.0.0 major 15 Apr 2026; monthly minors; Monolith 43.1.0 on 28 Oct 2026; Drug Extension GTINs in 43.1.0. https://isd.hscic.gov.uk/trud/users/guest/filters/0/categories/26/items/101/releases ; https://isd.hscic.gov.uk/trud3/user/guest/group/0/pack/26
5. ICD-O-3 revision used by NCRAS. STILL NOT FOUND. gov.uk NCRAS methodology page names ICD-10 and TNM only; UKLLC guidebook says ICD-O-3 without revision; CTYA report mentions revisions 1 and 2 being accommodated. https://www.gov.uk/government/publications/ncras-statistical-publications-quality-and-methodology-information/cancer-registration-methodology
6. COSD named lead. STILL NOT FOUND; mailbox nhsdigital.cosdenquiries@nhs.net recorded instead.
7. Scotland SMR06 submission format. PARTLY VERIFIED: ~800,000 source records/year, probabilistic linkage, SACT weekly feed (ScotPHO, HTN). File format: STILL NOT FOUND (PHS National Data Catalogue page is JavaScript-only; NDC archive behind MirrorWeb bot check).
8. Scotland ICD-O/TNM. VERIFIED ICD-O-2 from 1997, ICD-O-3 from incidence year 2006 (ScotPHO key data sources). TNM edition: STILL NOT FOUND (PHS staging releases use QPI audit data; cervical FIGO 2018 change noted).
9. Scotland registry legal basis. VERIFIED partial: PHS public task under Public Health Scotland Order 2019 and s2 NHS (Scotland) Act 1978. https://publichealthscotland.scot/our-privacy-notice/our-legal-gateway . Registry-specific statute: STILL NOT FOUND.
10. NI legal basis and screening IT. VERIFIED: NICR public task UK GDPR 6(1)(e), QUB registration, ORECNI approval; NBSS for breast; BSIMS (Wales-built) since Apr 2010; regional cervical call/recall since 1988. URLs in file.
11. Wales screening IT. VERIFIED partial: BSIMS (DHCW) for bowel; NBSS (three instances) for Breast Test Wales (PHW board papers). Cervical Screening Wales IT: STILL NOT FOUND.
12. WCISU legal basis. STILL NOT FOUND (PHW privacy policy text not retrievable via search; patient leaflet 2016 only).
13. ENCR/IACR membership. VERIFIED ENCR: NCRAS, Scottish Cancer Registry (Dr David Morrison), WCISU (Prof Dyfed Wyn Huws), NICR in ENCR contact list. IACR: STILL NOT FOUND (iacr.com.fr returns 403).
14. ECIS UK contribution. STILL NOT FOUND (UK not in EU27 estimates; ECIS registry list page rejects automated access).
15. CRUK statistics portal. VERIFIED. https://www.cancerresearchuk.org/health-professional/cancer-statistics-for-the-uk ; team lead confirmed https://www.cancerresearchuk.org/health-professional/cancer-statistics (HTTP 200).
16. OECI UK members. CORRECTED: directory lists The Christie, CRUK Cambridge Centre and Velindre Cancer Service, all "Associate Member"; Royal Marsden, Leeds, Oxford absent. https://oeci.eu/IstitutesCountry.aspx?id=21 . Team lead (browser): certified-centres list at https://accreditation.oeci.eu/ names only The Christie and CRUK Cambridge Centre for the UK; Ireland: Beaumont RCSI, CUH/UCC, HSE West North West Galway, St Vincent's UCD, TSJCI; no Cypriot or Maltese centre (saved at verify/oeci-centres-2026-11-19.txt).
17. UKCRC Tissue Directory / BBMRI-ERIC UK. CORRECTED: UK not among BBMRI-ERIC member states or observers (nodes page); UKCRC TDCC registers UK biobanks in the BBMRI-ERIC Directory. https://www.bbmri-eric.eu/national-nodes/ ; https://biobankinguk.org/uk-biobanks-bbmri-eric-directory/
18. UK in EU cancer projects. VERIFIED negative for EUCAIM, JANE, TEHDAS2, EUCanScreen, canSERV partner lists. UNCAN.eu, CraNE, ECHoS, EUnetCCC: STILL NOT FOUND (CORDIS partner lists not fetched).
19. CWT dataset version. VERIFIED: guidance v12.0 (17 Aug 2023) and v12.1 (8 Apr 2025), Dataset 2.1 format, DCB0147. https://www.england.nhs.uk/publication/national-cancer-waiting-times-monitoring-dataset-guidance/
20. Chemotherapy e-prescribing shares. PARTLY VERIFIED: ChemoCare vendor claim 80% of NHS cancer centres (System C G-Cloud listing). Aria/iQemo: STILL NOT FOUND.
21. Scotland chemo system. CORRECTED: ChemoCare is the national CEPAS across 14 boards; NSS re-procurement PIN 31 May 2024. https://www.scan.scot.nhs.uk/?p=63 ; https://www.find-tender.service.gov.uk/Notice/017040-2024
22. openEHR oncology in UK. CORRECTED: Genomics England 100,000 Genomes cancer models in openEHR (99 archetypes, 26 templates, 2019; COSD-based; Apperta CKM project); NHS Wales evaluation. https://discourse.openehr.org/t/new-oncology-archetypes/1308
23. NI encompass oncology module. STILL NOT FOUND.
24. NDRS named leads. STILL NOT FOUND.

#### Ireland

25. HSE CTS product/vendor. VERIFIED (team lead read the live press release 2026-11-19; "in beta" removed, it referred to the about.hse.ie site banner): CSIRO Ontoserver, delivered and managed by Dedalus; procurement dated July 2025 (HSE press release 29 Jun 2026) vs September 2025 (eHealth Ireland 16 Dec 2025), conflict recorded. https://about.hse.ie/news/the-hse-central-terminology-service-cts (Wayback copy) ; https://www.ehealthireland.ie/news-media/news/2025/fhir-central-terminology-server-for-the-hse
26. NCRI TNM edition. VERIFIED: TNM7 since 2014, earlier TNM4/5, 1994-2013 recoded to TNM7; ICD-O-3.2 from 2020 (Data Dictionary v2.0; 2026 statistical report "TNM staging"). https://www.ncri.ie/en/media/145/download ; https://www.drugsandalcohol.ie/46716/1/NCRI_AnnualStatReport_2026.pdf
27. ICD-10-AM 13th edition adoption. STILL NOT FOUND (HPO 2025 report, Sep 2026, still references 10th to 12th edition change).
28. ATC. VERIFIED: WHO ATC used by HSE PCRS. https://pmc.ncbi.nlm.nih.gov/articles/PMC5662670
29. UICC edition in clinical use. STILL NOT FOUND.
30. Clinical audits. STILL NOT FOUND.
31. Synthetic datasets. STILL NOT FOUND.
32. BBMRI-ERIC Irish node. CORRECTED: Ireland not among member states or observers. https://www.bbmri-eric.eu/national-nodes/
33. Cancer Trials Ireland. VERIFIED: ICORG 1996, HRB network, 117 open trials Dec 2025. https://www.hrb.ie/grant-approved/cancer-trials-ireland-network/
34. OECI Ireland. CORRECTED: eight Full Members listed. https://oeci.eu/IstitutesCountry.aspx?id=34
35. EU projects Ireland. CORRECTED: JANE-2 (RCSI, Children's Health Ireland), ECHoS (NCCP, Prof Risteárd Ó Laoide), TEHDAS2 (DoH, Maynooth). EUnetCCC, EUCAIM, canSERV: STILL NOT FOUND / no Irish partner listed.
36. Structured pathology, PROMs, openEHR, tumour-board software beyond NCIS. STILL NOT FOUND.

#### Cyprus

37. Registry submission format, legal basis, audits, screening IT, access route. STILL NOT FOUND (moh.gov.cy blocks; Greek-language search returned no registry documents).
38. ICD-10 national modification. STILL NOT FOUND (GeSY coding manual not public).
39. Registry TNM edition. STILL NOT FOUND (MECC 2009 manual last public reference).
40. ATC, UICC, terminology server. STILL NOT FOUND.
41. Registry head. STILL NOT FOUND; Anna Demetriou confirmed as HMU Statistics Officer and NCI board member (Politis); Dr Pavlos Pavlou historical coordinator (MECC 2009).
42. OECI Cyprus. CORRECTED: German Oncology Center is the only Cypriot member (Full Member); BOCOC is not listed. https://oeci.eu/IstitutesCountry.aspx?id=42
43. BBMRI node. CORRECTED: BBMRI.cy led by Ministry of Health, integrating biobank.cy and CING. https://www.bbmri-eric.eu/national-nodes/
44. EU projects. CORRECTED: EUCAIM (German Oncology Center), JANE-2 (MoH, BOCOC), EUCanScreen (MoH, UCY), TEHDAS2 (NeHA, Karaiskakeio, CYENS), ECHoS participant. canSERV: none. EUnetCCC membership: STILL NOT FOUND.
45. HDAB. VERIFIED planned under NeHA (OECD.AI).
46. OMOP/EHDEN. VERIFIED negative (no Cypriot partner). Imaging: GOC in EUCAIM.
47. Genomics strategy, tumour-board software, chemo e-prescribing, structured pathology, PROMs, openEHR. STILL NOT FOUND.
48. ENCR contact list entry for Cyprus. STILL NOT FOUND in search snippets (encr.eu rejects curl).

#### Malta

49. Registry head. CORRECTED: Dr Neville Calleja, director, Malta National Cancer Register (ENCR contact list). https://www.encr.eu/encr-members-contact-list?page=12
50. Hospital coding. VERIFIED: ICD-10 diagnoses, ICD-9-CM procedures in DHIR National Hospital Information System. https://ec.europa.eu/eurostat/cache/metadata/en/hlth_res_esms_mt.htm
51. Registry TNM, LOINC, ATC, terminology server. STILL NOT FOUND.
52. Submission format, legal basis, audits, screening IT, open data portal. STILL NOT FOUND (dhir.gov.mt Cloudflare; Wayback rate-limited).
53. ECIS registry row. STILL NOT FOUND (ECIS page rejects automated access).
54. National Cancer Plan 2025-2030. STILL NOT FOUND published (confirmed via health.gov.mt publications search, Nov 2026).
55. OECI Malta. VERIFIED negative (no Malta country page in OECI directory).
56. BBMRI node. CORRECTED: node represents DwarnaBio (University of Malta). https://www.bbmri-eric.eu/national-nodes/
57. EU projects. CORRECTED: EUnetCCC WP3 co-lead (MHAA), JANE (Ministry for Health), EUCanScreen (MHAA), TEHDAS2 (MHAA), ECHoS hub (inception 10 Jul 2024). JANE-2 Maltese partner: STILL NOT FOUND. EUCAIM and EHDEN: no Maltese partner (verified negative).
58. Digital strategy cancer items, oncology prescribing software, tumour-board software, structured pathology, PROMs, openEHR. STILL NOT FOUND (strategy PDF URL served HTML, not the document).

#### Totals
- VERIFIED (fact or confirmed negative now sourced): 23
- CORRECTED (earlier statement replaced): 12 (items 16, 17, 21, 22, 32, 34, 35, 42, 43, 44, 49, 56, 57 counted as 12 distinct report statements)
- STILL NOT FOUND: 30 (items or sub-items above)

#### NEEDS BROWSER
Pages that block automated fetch; please read with a real browser:
1. https://digital.nhs.uk/ndrs/data/data-sets/cosd and https://digital.nhs.uk/ndrs/data/data-sets/cosd/cosd-user-guide-v10 (team lead: Cloudflare human check, not completed; standards.nhs.uk used instead; user guide v10.2.12 date, v10.2.0 dataset version, submission deadline and v11 timeline remain unverified).
2. https://digital.nhs.uk/ndrs/data/data-sets/cosd/cosd-user-guide-v10/introduction---clinical-terminology-integration-within-cosd (SNOMED CT edition and ICD-O-3 revision mandated by COSD).
3. https://digital.nhs.uk/data-and-information/publications/statistical/cancer-registration-statistics/england-2023/cancer-registration-data-collection-quality-and-methodology (ICD-O-3 revision used by NCRAS).
4. https://digital.nhs.uk/binaries/content/assets/website-assets/national-disease-registration-service/cosd/cosd_user_guide_v10.2.12-final.pdf (download the PDF).
5. https://www.hse.ie/eng/about/who/strategic-programmes-office-overview/ and https://about.hse.ie/news/ (any ICD-10-AM 13th edition announcement; HIPE coding notices on hpo.ie).
6. https://www.ehealthireland.ie/technology-and-transformation-functions/chief-data-and-analytics-office-cdao/standards-and-terminologies/central-terminology-server (CTS go-live status and hosted code systems).
7. https://dhir.gov.mt/en/malta-national-cancer-registry/ and https://dhir.gov.mt/en/ (team lead: Cloudflare origin DNS error on 2026-11-19, retry later) (registry methods, coding editions, reports, MHDAB status, Hospital Activity Analysis classification).
8. DONE by team lead: https://accreditation.oeci.eu/ certified-centres list read 2026-11-19.
9. https://www.encr.eu/encr-members-contact-list (find the Cyprus Cancer Registry entry and director; confirm Malta entry details).
10. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (Malta and UK registry rows and years).
11. https://www.moh.gov.cy/ Health Monitoring Unit pages (Cyprus registry head, TNM edition, notification procedure).
12. https://publichealthscotland.scot/services/national-data-catalogue/national-datasets/a-to-z-of-datasets/scottish-cancer-registry-smr06/ (JavaScript page; SMR06 submission format and dataset definition).
13. https://www.iacr.com.fr/ membership directory (IACR membership of UK, Irish, Cypriot and Maltese registries).
14. hl7belgium.org and esante.gouv.fr: not relevant to these four countries; nothing needed.

### italy

Scope: every item in italy-fhir.md and italy-landscape.md that was marked n/f or rested on Noze, press or Wikipedia. Method: Italian and English web search, Gazzetta Ufficiale ELI pages and issue PDFs, Ministero/AgID/AIRTUM/HL7 Italia/LOINC Italia sites, GitHub, CORDIS, curl plus pdftotext into italy-dl/. Both report files were edited in place; edited passages carry "(verified 2026-11-19)".

#### VERIFIED (primary source found, fact confirmed)
1. DM 31 Dec 2024 "Istituzione dell'Ecosistema dati sanitari": 25A01321, GU 53 of 5 Mar 2025; Ministero controller, Agenas processor; 21 regional clear-data units + SASN + pseudonymised + anonymous units (art. 4); FHIR cited in recitals; sub-investment 1.3.1 EUR 200 M. https://www.gazzettaufficiale.it/eli/id/2025/03/05/25A01321/sg (italy-dl/gu53.pdf)
2. DM 1 Aug 2023 "Registro nazionale tumori": 23A04839, GU 203 of 31 Aug 2023; ICD-9/ICD-10/ICD-O definitions, data sources, 180-day regional centre deadline, annual bulk feed, Allegato A tracciati A-D in XML. https://www.gazzettaufficiale.it/eli/gu/2023/08/31/203/sg/pdf (italy-dl/gu203.pdf)
3. DM 23 Oct 2025 ICD-10-IM and CIPI: 25A06571, GU 286 of 10 Dec 2025. https://www.gazzettaufficiale.it/eli/id/2025/12/10/25A06571/sg
4. DM 11 Nov 2025 amending DM 7 Sep 2023: 25A06570, GU 286 of 10 Dec 2025. https://www.gazzettaufficiale.it/eli/id/2025/12/10/25A06570/sg
5. EUCAIM Italian partners (10 of 95, 17 countries) from the official consortium page. https://cancerimage.eu/partners/
6. AIRTUM participating registries: 35 named registries and 44,459,587 inhabitants (about 80 %) in "I numeri del cancro 2025". https://www.legatumori.mi.it/wp-content/uploads/2025/12/2025_NDC_web.pdf (italy-dl/ndc2025.pdf)
7. AIRTUM registry tools: CheckRT, SALI, INCAS-AIRTUM, SEER*Prep/Stat (AIRTUM handbook). https://www.registri-tumori.it/PDF/AIRTUM2009HANDBOOK/Chapter_Appendix3.pdf
8. AIRTUM past presidents (Rugge 2019-2021 etc.). https://www.registri-tumori.it/cms/pagine/past-president
9. LOINC Italia governance: IIT-CNR official Regenstrief partner, MoU 2014, semiannual Italian update, legal basis DPCM 178/2015. https://www.loinc.it/chi-siamo/ , https://www.loinc.it/la-normativa/
10. ICD-11: no Italian MMS in the WHO browser (/mms/it 404, /mms/en 200, release 2026-01); Italian WHO-FIC CC hosted by Regione FVG. https://icd.who.int/browse/2026-01/mms/en , https://www.reteclassificazioni.it/
11. EHDS Cabina di regia composition and dates (DM 20 Feb 2026, DM 15 Apr 2026, installed 5 May 2026; includes ISTAT, DTD, AgID, Conferenza Regioni, EU EHDS Board delegate). https://www.osborneclarke.com/it/insights/digital-health-telemedicina-e-ia-le-novita-del-ii-trimestre-2026 (quotes the Ministry notice; the salute.gov.it page itself is client-rendered)
12. HL7 Italia Terminology IG declares no terminology server; FSE Gateway dictionary microservice exists (it-fse-srv-dictionary). https://github.com/hl7-it/terminology/blob/master/sushi-config.yaml , https://github.com/ministero-salute/it-fse-srv-dictionary
13. PNRR sub-investment 1.3.1 EUR 200 M (from DM 31 Dec 2024 recitals). Same GU source as item 1.
14. ENCR membership: 51 Italian entries on the ENCR full-member contact list, including childhood, mesothelioma and colorectal registries; Fabrizio Stracci listed as director of the Umbrian Tumor Registry; applied to italy-landscape.md C1. https://www.encr.eu/encr-members-contact-list (read 2026-11-19)

#### CORRECTED (old vs new)
0. OECI Italian centres: old Wikipedia-derived list (9 CCC + 2 CCC-clinical + 8 other members) -> new live list of 16 certified Italian centres from https://accreditation.oeci.eu/ read with a browser by the team lead on 2026-11-19 (adds ASST Spedali Civili di Brescia, Policlinico San Matteo Pavia, INOC Candiolo, IRCCS Sacro Cuore Don Calabria, IRCCS San Raffaele; designation type per centre not shown). Snapshot: scratchpad/verify/oeci-centres-2026-11-19.txt
1. DM 7 Sep 2023 publication: old "GU 225 of 26 Sep 2023" (Noze) -> new "GU Serie Generale n. 249 of 24 Oct 2023, code 23A05829". https://www.gazzettaufficiale.it/eli/id/2023/10/24/23A05829/sg
2. DM 7 Sep 2023 content: old "decree explicitly references the Italian FHIR IGs; FHIR R4 with Italian IGs plus CDA R2" (Noze) -> new: the GU text names no FHIR/HL7/CDA; it refers to the standard formats of art. 12 c.15-octies and AgID guidelines; art. 3 c.1 lists 13 content types (a-m) detailed in Allegato A. The FHIR reference in primary law appears in the EDS decree recitals instead. italy-dl/gu249.pdf
3. EUCAIM Italian partners: old "press list" with "INT Milano not confirmed" -> new official list; INT Milano and Humanitas are not partners. https://cancerimage.eu/partners/
4. Massimo Rugge: old "named to lead Italian registries (Zaia statement)" -> new "AIRTUM president 2019-2021 (past president page)". https://www.registri-tumori.it/cms/pagine/past-president
5. AIRTUM coverage: old "35 registries, >44 M, about 80 %" (press) -> new same figures but from the primary report, with the full list of 35 registries. ndc2025.pdf
6. Ricerca Corrente total: old "annual total n/f" -> new EUR 187 M availability 2024 (192 M 2023, 231 M 2022), effective 179 M to 54 IRCCS, from the Ministry's 27 Feb 2025 presentation as reported by Quotidiano Sanità (still secondary; decree not retrievable). https://www.quotidianosanita.it/?p=141863
7. Registry software: old "n/f" -> new AIRTUM toolset (CheckRT, SALI, INCAS-AIRTUM) plus SEER tools; still no national management software.
8. EHDS Cabina di regia membership: old five members -> new full composition incl. ISTAT, DTD, AgID, Conferenza Regioni, EU Board delegate.

#### STILL NOT FOUND (what was tried)
1. INT Milan "breast codes" (PHOENIX source): searched INT + breast + data dictionary/FHIR/OMOP/minimum data set, author names Trama/Gatta/Mariani, Italian terms "mammella dizionario dati"; nearest items are the ENCR 2024 Lasalvia slides (OMOP oncology MDS, PDF blocked) and the 2015 INT breast registry paper.
2. mCODE adoption in Italy: three search rounds (Italian/English, GSTeP, Gemelli, IRCCS, "profili oncologici"); only the IRST Meldola FHIR+RDF pipeline (not mCODE) surfaced.
3. Health Data Access Body designation: searched GU, salute.gov.it (client-rendered), Osborne Clarke Q2 2026, regioni.it, press; no act found.
4. Referto epidemiologico implementing decree (art. 4 L. 29/2019) and art. 6 annual report to Parliament: searched normattiva, GU, Senate/Chamber document portals, press; nothing after 2019.
5. Current LOINC Italian variant version number: loinc.it has no version; loinc.org 403; Wayback offline. Lower bound 2.75 (UMLS 2023).
6. Lombardia / Piemonte / Veneto / Lazio regional oncology EHR ("cartella oncologica"): Regione Lombardia ROL page and decrees 2022-2026, DGR 6609/2022 (general CCE), reteoncologica.it, Veneto/Lazio searches; only Campania ROC/Sinfonia is documented.
7. ICD-11 Italian translation: WHO browser has no Italian MMS; Ministry and FVG CC publish nothing on a translation.
8. National FHIR terminology server / AgID "Catalogo delle terminologie": DNS checks, HL7 Italia IG config, FSE repos; only the Gateway dictionary microservice and a 2017 CNR-ICAR prototype exist.
9. Ricerca Corrente riparto decree (primary): salute.gov.it pages client-rendered; CIPESS deliberations cover other IRCCS contributions.
10. FSE 2.0 implementation status (primary numbers): fascicolosanitario.gov.it dashboards are client-rendered Liferay data sets.

#### NEEDS BROWSER (blocked for automated fetch)
- OECI accredited centres: RESOLVED by the team lead with a browser on 2026-11-19 (https://accreditation.oeci.eu/, 16 Italian centres); still open: designation type per Italian centre, which the home page does not show.
- LOINC Italian linguistic variant version: https://loinc.org/international/italian/ and https://loinc.org/downloads/ (403; Wayback snapshot 2026-02-11 exists at http://web.archive.org/web/20260211095451/https://loinc.org/international/italian/).
- INT Milano ENCR 2024 slides (OMOP oncology minimum data set): https://encr.eu/sites/default/files/Events/Workshops/Workshop-software-AI-2024/ENCR2024-Paolo%20Lasalvia.pdf (server returns HTML to curl).
- FSE 2.0 monitoring dashboard: https://www.fascicolosanitario.gov.it/it/monitoraggio (Liferay client-side data sets).
- Ministero della Salute research pages (Ricerca Corrente, fondi ordinari, Cabina di regia EHDS news): https://www.salute.gov.it/new/it/tema/sistema-ricerca-del-ssn-enti-e-finanziamenti/la-ricerca-corrente/ and https://www.salute.gov.it/new/it/tema/sistema-ricerca-del-ssn-enti-e-finanziamenti/investimenti-la-ricerca-con-fondi-ordinari/ (client-rendered, only a timestamp is returned).
- Gazzetta Ufficiale "atto originario" HTML views (e.g. https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2023-10-24&atto.codiceRedazionale=23A05829) return only the header to curl; the issue PDFs were used instead and are saved in italy-dl/ (gu249.pdf, gu203.pdf, gu53.pdf).
- ACC member list (names are images): https://alleanzacontroilcancro.it/soci/
- CORDIS EUCAIM page 101100633 (404 via curl; the consortium page was used instead).

### netherlands

Second pass over every "n/f" in `netherlands-fhir.md` and `netherlands-landscape.md`. Method: Dutch and English web searches, direct curl of organisation pages and PDFs (pdftotext), CORDIS project pages, the SNOMED Confluence REST API, the OECI accreditation directory. Downloads in `scratchpad/nl-verify/` (own directory; no interpreter run from inside it). Both files were edited in place; new facts carry "(verified 2026-11-19)".

Totals: 15 VERIFIED, 7 CORRECTED, 14 STILL NOT FOUND.

#### VERIFIED (fact now in the files)
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

#### CORRECTED (old vs new)
1. IKNL leadership. Old: Thijs Merkx sole board member. New: since the 1 Jan 2026 governance merger the DICA-IKNL board is chaired by prof. dr. Ernst Kuipers (from 1 May 2026), with Bente Jorritsma (vice-chair) and Suzanne Verboort; supervisory board chair Marlies van Elst; Merkx has left IKNL. https://dica.nl/over-ons/ ; https://www.oncologie.nu/nieuws/fusieorganisatie-dica-iknl-kiest-voor-ernst-kuipers/
2. OECI accreditation. Old: Erasmus MC and Radboudumc status unknown, only NKI, MUMC+, UMCG confirmed. New (live site read by the team lead in a browser on 2026-11-19, https://accreditation.oeci.eu/ , saved at scratchpad/verify/oeci-centres-2026-11-19.txt): six certified Dutch centres, Erasmus MC Cancer Institute, Maastricht UMC+, Netherlands Cancer Institute, OncoZON Cancer Network, Rijnstate, UMCG CCC. Radboudumc is not certified; the directory page lists it under "In Accreditation" (https://accreditation.oeci.eu/certified-centres/). Designation types from the directory: NKI, Erasmus MC, UMCG-CCC, MUMC+ = CCC with Research Excellence; Rijnstate = CCC; OncoZON = Comprehensive Cancer Network.
3. EUCAIM. Old: only Erasmus MC confirmed. New: nine Dutch partners (Amsterdam UMC, EATRIS, Erasmus MC, Health-RI, Maastricht University, Philips, Radboudumc, EGI Foundation, NKI). https://cancerimage.eu/partners/
4. SNOMED CT NL. Old: latest notes June 2026. New: August (20260831), September (20260930) and October 2026 (20261031; 34 new NL concepts, 298,826 translated active concepts) release notes exist. https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/1436188716
5. CancerWatch. Old: budget n/f, 92 organisations. New: overall budget EUR 16,249,841, EU EUR 12,999,873, 95 institutions from 30 countries, GA CR-g-24-40. https://health.ec.europa.eu/non-communicable-diseases/cancer/europes-beating-cancer-plan-eu4health-financed-projects/projects/cancerwatch-ja_en
6. canSERV end date. Old: 31 Aug 2026. New: 28 Feb 2027, total EUR 14,866,440.50. https://cordis.europa.eu/project/id/101058620
7. Nedap. Old: hospital EHR/openEHR share n/f. New: Nedap Healthcare serves long-term, disability and home care only, no hospital EHR share. https://europeanpurpose.com/nl/alternatief-voor/europese-alternatieven-voor-epic
Also added: PALGA director Aletta Debernardi and board chair Iris Nagtegaal (oncologie.nu); DHD board chair L. de Beukelaar (dhd.nl/over-ons).

#### STILL NOT FOUND (what was tried)
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

#### NEEDS BROWSER
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

### nordic-baltic

Pass date: 2026-11-19. Method: local-language web searches; direct curl of registry PDFs into a dedicated download directory with pdftotext (Danish register declaration and LPR3 guide 2025 v5.1, Swedish "Kodning i cancerregistret 2026", Cancer in Norway 2023 and 2025, Estonian TAI notification guide and 2026 cancer-plan mid-term evaluation, Latvian SPKC cancer-card lecture and instruction, Lithuanian NVI 2025 activity report, EUnetCCC grant data sheet); direct fetch of ENCR registry pages, Genome of Europe partner page, Sundhedsdatastyrelsen reorganisation page, term.tehik.ee FHIR metadata. Outcomes: VERIFIED (fact confirmed with URL), CORRECTED (old statement replaced), STILL NOT FOUND (attempts listed).

Counts after browser follow-up on OECI and the ENCR member list (2026-11-19): VERIFIED 21, CORRECTED 23, STILL NOT FOUND 20.

#### Priority 1: TNM editions in current registry use

| Country | Outcome | Detail |
|---|---|---|
| Denmark | VERIFIED (edition number not fixed) | Register declaration: extent coded "efter den gældende TNM-klassifikation"; LPR3 v5.1 §10.4.2.4.1 requires a qualified cTNM at first notification and refers to disease-specific clinical guidelines. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf |
| Sweden | CORRECTED | Old: "latest UICC edition". New: UICC TNM versions 8 and 9 currently in use ("för närvarande används version åtta och nio"), Kodning i cancerregistret 2026. https://www.socialstyrelsen.se/contentassets/6b4e25c21ce446f2a9d850ef43daa294/2026-5-10247.pdf |
| Norway | CORRECTED | Old: n/f. New: UICC 8th edition, Helsedirektoratet handlingsprogram states this matches Kreftregisteret routines; CiN 2025 derives stage from cTNM/pTNM. https://www.helsedirektoratet.no/retningslinjer/kreft-i-tykktarm-og-endetarm-handlingsprogram/patologi/uicc-tnm-klassifisering-og-stadieinndeling ; https://www.fhi.no/Content/cancer-in-norway-2025.pdf . Kreftregisteret kodebok itself not located. |
| Finland | STILL NOT FOUND | Tried Finnish searches ("TNM 8. painos", "levinneisyys", "laatuseloste"), cancerregistry.fi quality page (script-rendered, empty via curl). Found only that stage information is available for 42% of 2024 cases. https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ |
| Iceland | STILL NOT FOUND | Tried Icelandic searches ("TNM", "skráningarreglur", "gæðaskráning"); only ICD-O rules confirmed in Læknablaðið 2024. krabb.is variable list not located. |
| Estonia | CORRECTED | Old: n/f (study used 7th). New: TAI notification guide requires stage with TNM values per the 8th edition (pTNM, else cTNM). https://tai.ee/sites/default/files/2021-03/Teatise_vormistamise_juhend.pdf . Pathology templates being updated to TNM 9 (2026 mid-term evaluation). |
| Latvia | CORRECTED | Old: n/f. New: TNM 8th edition field in the cancer patient card; ICCC and TNM 8 added to data-entry algorithm by 1 Jan 2024. https://www.spkc.gov.lv/lv/media/19929/download ; https://spkc.gov.lv/lv/media/19977/download |
| Lithuania | STILL NOT FOUND | Tried Lithuanian searches ("TNM 8 leidimas", "forma 090/a pildymo taisyklės"), NVI 2025 report (no TNM statement). |

#### Priority 2: ICD-O editions

| Country | Outcome | Detail |
|---|---|---|
| Denmark | VERIFIED | ICD-O-3 morphology, ICD-10 topography/diagnosis since 2004 (register declaration). |
| Sweden | VERIFIED | ICD-O/3.2 applied since 2019 (2026 handbook). |
| Norway | VERIFIED | Codes registered in ICD-O-3, converted to ICD-10 for reporting (CiN 2025). |
| Finland | VERIFIED (edition 3) | ICD-O-3 topography/morphology/behaviour variables in registry data description (FinnGen documentation); official registry coding manual not located. |
| Iceland | VERIFIED (edition not stated) | Registry follows ICD-O rules (Læknablaðið 2024). https://www.laeknabladid.is/media/2024-06/f02.pdf |
| Estonia | VERIFIED | RHK-O-3 (ICD-O-3) since 2008 (TAI page and notification guide). |
| Latvia | CORRECTED | Old: n/f. New: SSK-O-3.2 topography and morphology in cancer patient card (SPKC lecture Dec 2023). |
| Lithuania | VERIFIED (older source) | ICD-O-3 for topography/morphology per 2012 registry report; no newer manual. |

#### Priority 3: Icelandic and Baltic genomics participation

| Item | Outcome | Detail |
|---|---|---|
| Genome of Europe partners (all 8) | CORRECTED | Partner page lists Denmark (Danish National Genome Center, 1,414 samples), Estonia (University of Tartu, 368), Finland (University of Helsinki 1,462; CSC), Latvia (BMC, 476), Lithuania (Santaros Klinikos, 816), Norway (University of Oslo, 1,346), Sweden (Uppsala University, 2,591). Iceland absent. https://genomeofeurope.eu/partners/ |
| 1+MG signatories | VERIFIED | 25 EU states plus UK and Norway signed; Denmark listed as observer in 2018-era sources; Iceland not a signatory. https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7115898 |
| Iceland GDI / 1+MG node | STILL NOT FOUND | Searched Icelandic and English; no Icelandic GDI or 1+MG participation found; treated as not participating. |
| Lithuania 1+MG | VERIFIED | Santaros Klinikos biobank responsible organisation, €7.6M GDI 2023–2026 (OECD.AI). |
| Finland Genome Center | CORRECTED | Old: status n/f. New: genome act removed from government programme; Genomikeskus not established. https://stm.fi/-/genomilain-antaminen-siirtyy-eteenpain-genomikeskuksen-valmistelu-jatkuu |
| Denmark genome governance | CORRECTED (added) | Nationalt Genom Center merged into Sundhedsdatastyrelsen 1 July 2025. https://www.altinget.dk/sundhed/artikel/styrelse-og-nationalt-genom-center-laegges-sammen-centerdirektoer-fortsaetter |

#### Priority 4: Named registry leads

| Country | Outcome | Detail |
|---|---|---|
| Denmark | VERIFIED | Maya Christel Milter, Director, Danish Cancer Registry (ENCR). https://www.encr.eu/node/169 . ENCR lists the institute as "National Institute for Health Data and Disease Control", Artillerivej 5 (SSI address); the ENCR member list (https://www.encr.eu/encr-members-contact-list (read 2026-11-19)) shows the same label; it could not be matched to a current Danish agency name. |
| Sweden | CORRECTED | Old: n/f. New: Dr. David Pettersson, director, Swedish Cancer Registry (National Board of Health and Welfare). https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| Norway | VERIFIED | Giske Ursin, Director Kreftregisteret (FHI 2026 release, CiN 2025). https://www.fhi.no/nyheter/2026/40364-nye-krefttilfeller-i-2025/ |
| Finland | VERIFIED | Janne Pitkäniemi, Director Finnish Cancer Registry (Syöpä 2024 report coverage). |
| Iceland | VERIFIED | Sigríður Gunnarsdóttir, head of Rannsóknasetur – Krabbameinsskrá (Krabbameinsfélagið annual report 2025). https://www.krabb.is/media/arsskyrsla-krabbameinsfelagsins-2025.pdf |
| Estonia | CORRECTED | Old: n/f. New: Dr. Margit Mägi, director, Estonian Cancer Registry (National Institute for Health Development). https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| Latvia | CORRECTED | Old: n/f. New: Dr. Elina Liepina, director, Latvian Cancer Register (Centre for Disease Prevention and Control). https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| Lithuania | VERIFIED | Giedrė Smailytė, Director Lithuanian Cancer Registry (ENCR). https://encr.eu/node/262 |

#### Other items

| Item | Outcome | Detail |
|---|---|---|
| Danish registry coverage | VERIFIED | Above 95% (register declaration). |
| Danish screening registries | CORRECTED | DKMS, DKLS, DTS (RKKP) with annual-report URLs. |
| Kræftplan V | CORRECTED | Published 23 May 2025 (36 initiatives); implementation agreement 27 Nov 2025. https://medcom.dk/wp-content/uploads/2026/08/Bilag-2-Udmoentningsaftale-om-Kraeftplan-V-2026-og-frem.pdf |
| Digital Sundhed Danmark | CORRECTED (added) | SDS, MedCom, sundhed.dk, Nationalt Genom Center merge into Digital Sundhed Danmark 1 Jan 2027. https://english.sundhedsdatastyrelsen.dk/about-us/digital-health-denmark |
| Rigshospitalet / Odense OECI | CORRECTED (browser) | OECI list 2026-11-19: Aarhus University Hospital CCC, Copenhagen CCC Rigshospitalet and Herlev-Gentofte, Vejle Cancer Centre Lillebaelt Hospital; Odense not listed. https://accreditation.oeci.eu/ |
| EUnetCCC participants (all 8) | CORRECTED | Grant data sheet lists DK (Region H, AU, Region Syddanmark, Region Sjælland, AUH), SE (Socialstyrelsen, SKR, KI, Region Stockholm, VGR, Östergötland, Skåne, Uppsala), NO (OUS, UNN, FHI, St Olavs, Helse Bergen), FI (HUS), EE (SoM, Tartu UH, TAI, PERH), LV (University of Latvia, RSU, two hospitals), LT (Ministry, Kaunas, Šiauliai, Santaros, NVI, others), IS (Landspítali). https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf |
| EU-Designated CCCs (first 30, 23 Feb 2026) | CORRECTED | Norway: St. Olav, UNN. Lithuania: Klaipėda UH, Santaros with National Cancer Centre, LSMU Kaunas. No DK, SE, FI, EE, LV, IS centre in the first wave; the earlier search summary claiming Riga East was included was wrong (eight countries, Latvia not among them). https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ |
| Estonia OECI | CORRECTED (browser) | Tartu University Hospital is on the OECI accredited-centres list (level not shown); East Tallinn Central Hospital is a full OECI member. https://accreditation.oeci.eu/ ; https://www.itk.ee/en/news/east-tallinn-central-hospital-gains-full-oeci-membership |
| Iceland OECI / BBMRI / ECHoS | VERIFIED (absence) / STILL NOT FOUND | Not BBMRI member or observer (2025 report); no Icelandic centre on the OECI accredited list 2026-11-19 (browser); membership n/f; ECHoS n/f. |
| OECI accredited centres, all 8 countries | VERIFIED (browser) | DK: Aarhus, Copenhagen CCC (Rigshospitalet and Herlev-Gentofte), Vejle. SE: Karolinska, Linköping, Sahlgrenska, Skåne, Uppsala. NO: Haukeland Bergen, Oslo University Hospital. FI: Kuopio, Helsinki, TAYS Tampere, Turku. EE: Tartu. LV: Riga East. LT: 'National Cancer Institute' (country not shown, consistent with NVI Vilnius). IS: none. https://accreditation.oeci.eu/ |
| Estonia terminology server endpoint | VERIFIED | https://term.tehik.ee/fhir/metadata returns a FHIR CapabilityStatement (ontoserver mode); UI requires login. |
| Estonian pathology templates | CORRECTED (added) | ICCR/CAP-based standard templates updated to TNM 9 (2026 mid-term evaluation). |
| Latvia SSK-10 version | STILL NOT FOUND | Still the basis of Cabinet Regulation No. 6 of 13 Jan 2026; no version number. https://likumi.lv/ta/id/365793 |
| Lithuania TLK-10-AM edition | STILL NOT FOUND | Introduced by order V-164 (23 Feb 2011); in use 2026; ICD-10-AM edition not stated. https://e-seimas.lrs.lt/rs/legalact/TAD/TAIS.211963/ |
| Estonia RHK-10 version | STILL NOT FOUND | Published via TEHIK Publitseerimiskeskus; no version page found. |
| Finnish SNOMED edition date | STILL NOT FOUND | SNOMED page says "published in December" without year; module id 11000229106. |
| Danish SKS version, DK/SE/NO LOINC and ATC usage | STILL NOT FOUND | Low priority; not pursued further. |
| HL7 Denmark chair | STILL NOT FOUND | hl7.dk has no board page; conflicting secondary sources. |
| HL7 Sweden chair | STILL NOT FOUND | hl7.se blocks automated fetch (Loopia block page); archive copy empty. |
| Danish/Swedish/Norwegian/Finnish/Icelandic MDT, chemo module, openEHR oncology items | STILL NOT FOUND | Not pursued beyond earlier searches. |
| ENCR membership (DK, SE, NO, FI, EE, LT) | VERIFIED | All six national registries on the ENCR member list; Denmark also lists the Faroese Cancer Registry. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| ENCR membership (IS, LV) | CORRECTED | Old: n/f (list script-rendered). New: Icelandic Cancer Registry and Latvian Cancer Register are ENCR members. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| Synthetic datasets (all countries) | STILL NOT FOUND | No national synthetic cancer dataset found. |
| DARWIN EU Swedish partner | STILL NOT FOUND | EMA PDF returns HTML block page. |
| ECIS contributing registries (IS, EE, LV, LT) | STILL NOT FOUND | ECIS list page is script-rendered. |
| Finnish registry current submission format | STILL NOT FOUND | cancerregistry.fi pages script-rendered. |

#### NEEDS BROWSER

Pages that block or script-render for automated fetch; please open in a real browser:

1. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (ECIS contribution of IS, EE, LV, LT).
2. https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf (DARWIN EU partners for SE, NO, EE).
3. https://hl7.se/ (board / ordförande page) and https://hl7.dk/ members area or https://confluence.hl7.org/display/HD (HL7 Denmark chair).
4. https://cancerregistry.fi/statistics/description-of-statistics-and-their-quality/ and https://syoparekisteri.fi/ilmoittaminen/ (Finnish TNM edition and current notification format).
5. https://www.fhi.no/kreft/ search for "kodebok" (Kreftregisteret codebook, TNM/ICD-O statement).
6. https://www.krabb.is/rannsoknasetur/ (Icelandic registry variable list / TNM).
7. https://term.tehik.ee/ (login-protected UI; FHIR endpoint already verified).
8. (resolved 2026-11-19 by team lead with a browser) https://accreditation.oeci.eu/ accredited-centres list; results applied above. Open point: the 'National Cancer Institute' entry shows no country; confirm it is NVI Vilnius, and check Tartu's accreditation level.

### rerun-2026-11-19

| Item | Outcome | Evidence |
|---|---|---|
| Belgian SNOMED CT translation totals | VERIFIED: Belgian Edition 20261115 (packaged with Nov 2026 International): French 292,415 preferred terms, 75.29 % of active concepts; Dutch 306,827, 79.00 %; German 118,272, 30.45 %; 24 new Belgian concepts | https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/1468334117 (read in browser) |
| Translation totals for SE, AT, IE, NO, EE, ES, CH | STILL NOT FOUND, now confirmed from primary pages: the November 2026 release notes give per-release changes only, not running totals (e.g. AT 20261115 on International Oct 2026 lists 7,310 changed translations, 6,176 of them clinical findings) | SNOMED RMT wiki pages 1413316748, 1468858405, 1500053541, 1414201388, 1455718444, 1441431619, 926416899 |
| ANS CI-SIS cancer volets (esante.gouv.fr was in maintenance) | VERIFIED live, page updated 2026-11-10: CANCER-FRCP 2025.01 and CANCER-PPS 2025.01 validated 2025-08-27; CANCER-CR-GM 2022.01 validated 2022-12-06; CANCER-D2LM 2022.01 validated 2025-03-12; CANCER-CR-ACP obsolete; all CDA. No FHIR cancer volet | https://esante.gouv.fr/offres-services/ci-sis/espace-publication |
| Whole-edition and clinical-finding SNOMED translation counts on local Snowstorm | STILL OPEN: the query exceeds Elasticsearch's 500,000-term limit; splitting by hierarchy double-counts polyhierarchy concepts. Published total for the German edition: 130,795 translated concepts | local Snowstorm error "number of terms [675964] … exceeded the allowed maximum of [500000]" |
| MII Ontoserver $translate (German ICD-10-GM, OPS, ICD-O transition ConceptMaps) | STILL OPEN: server unreachable from this machine (mTLS, offline) | HTTP 503 from the Blaze fallback |
| Lithuanian terminology server tx.hl7.lt | STILL OPEN: DNS resolves (193.40.252.122), no TCP response within 20 s | curl |
| loinc.org linguistic variant pages, digital.nhs.uk COSD, legifrance circular DGS/SP5/2026/161 | NOT RETRIED: Cloudflare or bot checks, which are not bypassed | — |

### south

Date: 2026-11-19. Method: WebSearch in local languages, curl of primary pages and PDFs (pdftotext) into a separate download directory, Wayback Machine copies, FHIR package registry mirrors. Italy entries limited to items in my own files. Outcome codes: VERIFIED, CORRECTED, STILL NOT FOUND.

#### south.md (FHIR / terminology survey)

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 1 | FR | OSIRIS named maintainer | VERIFIED (partial) | GitHub contributors to the IG repo include INCaAJobard (INCa) and nriss; no maintainer page. https://api.github.com/repos/InstitutNationalduCancer/ImplementationGuide_OsirisFHIR/contributors |
| 2 | FR | CIP on the SMT | VERIFIED (partial) | SMT FHIR CodeSystem endpoint (count 200) returns BDPM, CIM11_MMS, SNOMED_CT plus TRE/JDV code systems; no separate CIP code system returned. https://smt.esante.gouv.fr/fhir/CodeSystem?_summary=true |
| 3 | FR | TNM 9th ed. national adoption; Francim registry transmission format; CIM-O-3 sub-edition | STILL NOT FOUND | Left to the France deep-dive agent; searches on cancer.fr and santepubliquefrance.fr found no adoption decision or format spec. |
| 4 | IT | ISTAT ICD-10 version | VERIFIED | ICD-10 version 2016 with Iris from 2016 data; version 2019 from 2020 data. https://www.ISTAT.it/it/files//2023/04/NOTAINFORMATIVABridgeCoding2020.pdf |
| 5 | IT | HL7 Italia chair | CORRECTED | Old: not found (older sources named Cangioli). New: President Stefano Lotti, Vice-President Giorgio Cangioli (past chair), CTO Leonardo Alcaro, elected 26 June 2024. https://www.hl7.it/direttivo |
| 6 | IT | Italian oncology FHIR IG | STILL NOT FOUND | hl7-it GitHub, packages.fhir.org jurisdiction IT, HL7 Italia site: no oncology IG. |
| 7 | IT | National terminology server | STILL NOT FOUND | Only HL7 Italia terminology IG; Ministry/AgID/Sogei searches gave nothing. |
| 8 | ES | Registry submission format / national registry law | CORRECTED (partial) | RD 568/2024 (BOE-A-2024-12379) creates the Red Estatal de Vigilancia en Salud Pública; cancer surveillance RD still at public-consultation stage. https://www.sanidad.gob.es/normativa/docs/CPP_RD_VIGILANCIA_CANCER.pdf ; format still not found. |
| 9 | ES | Código Nacional FHIR code system; TNM edition mandate; Arturo Romero current role | STILL NOT FOUND | Ministry semantic pages, SNS terminology server page, LinkedIn-free searches. |
| 10 | PT | Portuguese Core IG package id | VERIFIED | `portuguese.core.guide` 1.0.0, canonical base https://spms.min-saude.pt/fhir-r4B/iop. https://packages2.fhir.org/xig/portuguese.core.guide|1.0.0/StructureDefinition/AllergyIntolerancePTCore |
| 11 | PT | RON submission format | STILL NOT FOUND (access rule VERIFIED) | ron.min-saude.pt unreachable, no Wayback CDX snapshot; Lei 53/2017 art. 5 defines RIS platform with role profiles. https://diariodarepublica.pt/dr/detalhe/lei/53-2017-107692693 |
| 12 | PT | SNOMED CT Portuguese national edition | STILL NOT FOUND | snomed.org member page is JS; CTC wiki and SNO-PT records mention translation work only. NEEDS BROWSER (MLDS). |
| 13 | PT | LOINC national variant | VERIFIED (partial) | TEHDAS factsheet: lab catalogues use LOINC and SNOMED CT; no national LOINC release found. https://tehdas.eu/app/uploads/2023/03/portugal-country-visit-factsheet-03-2023.pdf |
| 14 | PT | TNM edition in RON | STILL NOT FOUND | RON reports and RORENO documents do not state the edition. |
| 15 | LU | National base IG package | VERIFIED (negative) | esantelux organisation has four preview guides and no packages. https://simplifier.net/organization/esantelux/~projects |
| 16 | LU | RNC legal basis, coding | CORRECTED | Legal basis: règlement grand-ducal du 18 avril 2013, Mémorial A-79 (29 Apr 2013); coding CIM-O-3; stage TNM 7th edition (2009) in 2020 report; ENCR-JRC tumour groupings. https://gouvernement.lu/dam-assets/documents/actualites/2021/02-fevrier/04-journee-cancer/MSA-5632-20-rapport-cancer-2020-web-BAT-4-.pdf |
| 17 | LU | SNOMED national edition; LOINC variant | STILL NOT FOUND | snomed.org member page JS; no MLDS listing reachable. NEEDS BROWSER. |
| 18 | LU | Agence eSanté FHIR lead | CORRECTED (partial) | CEO Alexandre Baumeister since 15 June 2026, board chair Marc Hostert; FHIR lead still not named. https://en.paperjam.lu/article/agence-esante-is-stepping-up-to-the-european-level |
| 19 | LU | Oncology FHIR IG / mCODE | STILL NOT FOUND | Simplifier esantelux, packages.fhir.org LU. |

#### south-landscape.md (non-FHIR landscape)

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 20 | IT | ECIS contributing registries | VERIFIED | 41 Italian registries in archived ECIS list. https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data |
| 21 | IT | ENCR member list | VERIFIED | 51 Italian entries on the ENCR full-member contact list (population and specialised registries, with directors); applied to south-landscape.md. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| 22 | IT | OECI centres | VERIFIED | 16 Italian centres on the OECI list read in a browser by the team lead on 2026-11-19 (saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://accreditation.oeci.eu/ |
| 23 | IT | EU project partners | VERIFIED | CraNE: ACC, MoH, IDI; EUCanScreen: ISS, CPO Turin; TEHDAS2: MoH, UniBo, Parma, ACC, ULSS4, RER, UCSC; ECHoS hub ACC. https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/ ; https://tehdas.eu/partners/ ; https://cancermissionhubs.eu/hubs/ |
| 24 | IT | 1+MG national programme; chemo prescribing; openEHR; patient portal oncology; hospital registries; synthetic data | STILL NOT FOUND | Left n/f; Italy deep-dive agent covers these. |
| 25 | ES | National registry legal basis | CORRECTED | RD 568/2024 framework; cancer surveillance RD pending; Catalonia-wide registry decree in prior consultation Mar 2025. https://www.sanidad.gob.es/fr/gabinete/notasPrensa.do?id=6458 ; https://www.catalannews.com/society-science/item/estimated-42851-malignant-tumors-diagnosed-in-catalonia-in-2024 |
| 26 | ES | ECIS registries | VERIFIED | 15 Spanish registries (archived ECIS list). |
| 27 | ES | EU project partners | VERIFIED (partial) | CraNE: ICO; canSERV: EurOPDX nodes in Spain; ECHoS hub exists. EUCanScreen/TEHDAS2 Spanish names not in fetched text. |
| 28 | ES | Structured pathology (SEAP) | VERIFIED (partial) | SEAP consensus protocols (colorectal) and Spanish ICCR datasets exist; adoption figures n/f. https://www.seap.es/documents/Publicaciones/Protocolos/guias-clinicas/consenso-recomendaciones/Carcinoma_colo_rectal.pdf |
| 29 | ES | Oncofarm/Farmis deployment; tumour-board software; openEHR; REDECAN submission format; researcher access; synthetic data | STILL NOT FOUND | SEFH and vendor searches returned no deployment data. |
| 30 | PT | SIIMA screening system | VERIFIED | SiiMA Rastreios is the SPMS screening system (2026 maintenance tender). https://ted.europa.eu/en/notice/238605-2026/pdf |
| 31 | PT | ECIS registries | VERIFIED | Azores, Central, North, South regional registries only, latest 2016; no RON national series. |
| 32 | PT | EU project partners | VERIFIED | CraNE: MS; EUCanScreen: MS, IPO Porto; ECHoS hub recognised. |
| 33 | PT | RON portaria / variable dictionary; Transparência SNS oncology datasets; tumour-board; openEHR; RSE oncology | STILL NOT FOUND | Diário da República search for RON portaria/despacho: none; ron.min-saude.pt down. |
| 34 | LU | RNC legal basis and coding | CORRECTED | See item 16. |
| 35 | LU | ECIS | CORRECTED | Luxembourg absent from the ECIS contributing-registries list (archived 2025). |
| 36 | LU | Latest RNC report | VERIFIED | Feb 2026 release covers 23,660 cancers 2014-2021. https://www.lesfrontaliers.lu/?p=1216650 |
| 37 | LU | EUCAIM partner | VERIFIED (negative) | No Luxembourg partner on https://cancerimage.eu/partners/ |
| 38 | LU | EU projects | VERIFIED | CraNE: INC, LIH; ECHoS hub; TEHDAS2 lists Luxembourg. |
| 39 | LU | DSP oncology content; OECI; terminology server status beyond "planned"; openEHR | STILL NOT FOUND | Agence eSanté cahiers statistiques have no document-type breakdown for oncology. |
| 40 | GR | Registry legal basis and data fields | VERIFIED | ΥΑ 6197/2024, ΦΕΚ Β' 950/09.02.2024: mandatory registration, fields (diagnosis/histology/grade, date, facility, stage, biomarkers), HDIKA processor, interoperability with AMKA, paediatric registry, EHR. https://www.dsanet.gr/Epikairothta/Nomothesia/950.PDF |
| 41 | GR | ECIS | VERIFIED (negative) | Greece absent from ECIS contributing list. |
| 42 | GR | OECI | CORRECTED | Agios Savvas completed OECI accreditation June 2025. https://en.protothema.gr/2025/06/13/saint-savas-was-certified-by-the-organization-of-european-oncology-institutes/ |
| 43 | GR | Researcher access | VERIFIED (partial) | Decree role "statistical information users"; INAB/CERTH National Cancer Data Node (CANDLE). https://www.inab.certh.gr/wp-content/uploads/2025/07/PRESS-RELEASE-CANDLE.pdf |
| 44 | GR | EU projects | VERIFIED | CraNE: 1st YPE Attica, Agios Savvas, Laiko; EUCanScreen: DYPEDE; TEHDAS2: MoH, GRNET, IDIKA. |
| 45 | GR | ENCR membership of national registry; ICD-O/TNM editions; open data portal; structured pathology; tumour board; openEHR | STILL NOT FOUND (ENCR part CORRECTED) | Decree does not name coding systems. ENCR: Hellenic Cancer Registry (director Evangelia Tzala, KEELPNO, i.e. pre-2024 entry) and NARECHEM (childhood haematological malignancies, Eleni Petridou) are listed; the report's "NARECHEM-ST ENCR-listed" claim was corrected; membership of the 2024 HDIKA registry not shown. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| 46 | MT | Legal basis | VERIFIED | Notification of Cancer Act, Cap. 154 (1957). https://legislation.mt/eli/cap/154/eng/pdf |
| 47 | MT | ECIS | CORRECTED | Malta contributes incidence 1993-2013 only (archived ECIS list). |
| 48 | MT | Cancer plan after 2021 | VERIFIED (negative) | No successor plan found; Digital Health and Health Data Strategy 2025-2030 listed. https://health.gov.mt/resources/ |
| 49 | MT | EU projects | VERIFIED | CraNE: MFH; EUCanScreen: MAH; ECHoS hub CRIHM. |
| 50 | MT | Registry format, ICD-O/TNM editions, data request route, latest cancer registry report | STILL NOT FOUND | dhir.gov.mt HTTP 403 to curl; deputyprimeminister.gov.mt gave a Cloudflare origin DNS error in a browser on 2026-11-19. Retry later. |
| 51 | CY | Registry coding | VERIFIED | ICD-O-3 with CanReg4 deriving ICD-10; MECC-supported set-up 1996-1998. https://pmc.ncbi.nlm.nih.gov/articles/PMC4523219 |
| 52 | CY | ECIS | VERIFIED | Cyprus Cancer Registry incidence 1998-2022. |
| 53 | CY | OECI | CORRECTED | No Cypriot or Maltese centre on https://accreditation.oeci.eu/ (browser, 2026-11-19); BOCOC holds CHKS/ISO 9001, not OECI. https://cyprus-mail.com/2026/01/21/double-international-recognition-for-bank-of-cyprus-oncology-centre |
| 54 | CY | EU projects | VERIFIED | CraNE: MOH; EUCanScreen: MOH, UCY; TEHDAS2: NeHA, Karaiskakeio, CYENS; ECHoS hub. |
| 55 | CY | Registry legal basis; 2024 strategy content; researcher access route; open data | STILL NOT FOUND | EU Country Cancer Profile PDF (cancer-inequalities.jrc) served HTML to curl; gov.cy strategy URL not retrievable. NEEDS BROWSER. |
| 56 | ALL | BBMRI Luxembourg | VERIFIED (negative) | Not among national nodes; members page blocked by cookie banner JS. https://www.bbmri-eric.eu/national-nodes/ |
| 57 | ALL | UNCAN.eu, JANE-2, EOSC4Cancer, EUnetCCC partner pages | STILL NOT FOUND | HTTP 000/404 to curl. NEEDS BROWSER. |

| 58 | ES/PT/GR/LU | OECI centres | VERIFIED | Spain 8 (12 Octubre, CUN, ICO, Clínic, IVO, FJD, IOCS Reus, Vall d'Hebron), Portugal 3 (IPO Coimbra, Lisboa, Porto), Greece 1 (Saint Savvas), Luxembourg 0. https://accreditation.oeci.eu/ (browser, 2026-11-19) |
| 59 | FR | SMT/ANS pages | NOTE | esante.gouv.fr was in maintenance on 2026-11-19; SMT FHIR endpoint answered. |

| 60 | ES | ENCR membership | CORRECTED | Old: "Spanish registries participate in ENCR" with Madrid as example of following ENCR recommendations. New: 19 Spanish ENCR member entries listed; Madrid appears only as its childhood and adolescent registry. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| 61 | PT | ENCR membership | VERIFIED | 7 entries: RON, former regional registries (North, Central, ROR-SUL, Azores, Madeira) and ROPP. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| 62 | LU | ENCR membership | VERIFIED | Cancer Registry of Luxembourg (LIH; Couffignal/Backes) and Morphological Tumour Registry (LNS; Hammer). https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| 63 | MT | ENCR membership | VERIFIED | Malta National Cancer Register, director Neville Calleja; join year 1995 not shown. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |
| 64 | CY | ENCR membership | VERIFIED | Cyprus Cancer Registry, director Vasos Scoutellas. https://www.encr.eu/encr-members-contact-list (read 2026-11-19) |

Totals: VERIFIED 37 (incl. partial and negative), CORRECTED 11, STILL NOT FOUND 15 (several items bundle multiple sub-items).

#### NEEDS BROWSER
- https://dhir.gov.mt/ and https://deputyprimeminister.gov.mt/ – Malta National Cancer Registry page, data request procedure, latest cancer report (HTTP 403 to curl; Cloudflare origin DNS error in browser on 2026-11-19; retry later).
- https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-cy-2024-1662-en.pdf – EU Country Cancer Profile Cyprus 2025, to extract the gov.cy May 2024 national cancer strategy URL and read that PDF.
- https://ron.min-saude.pt/ – Portugal RON platform documentation (site unreachable, no archive).
- https://mlds.ihtsdotools.org/#/landing/PT and /LU – whether Portugal or Luxembourg publish a SNOMED CT national edition/extension.
- https://www.snomed.org/member/portugal , /luxembourg , /spain – JS member pages (NRC, representatives).
- https://uncan.eu/partners/ , https://jane-2.eu/ , https://eosc4cancer.eu/partners/ , https://eunetccc.eu/ – partner lists per country (blocked/404).
- https://www.bbmri-eric.eu/about/members-observers/ – confirm Luxembourg and Spain membership status (cookie-banner JS).
- https://legilux.public.lu/eli/etat/leg/rgd/2013/04/18/n1/jo – full text of the 2013 RNC regulation (JS viewer).
- https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data – live version (curl gets "Request Rejected"; archived copy used).
