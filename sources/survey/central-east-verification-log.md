# Verification log: central-east.md and central-east-landscape.md

Pass date: 2026-11-19. Method: native-language web searches (PL, CZ, SK, HU, SL, HR, RO, BG), registry PDFs fetched with curl into scratchpad/dl and read with pdftotext, web.archive.org for offline pages, PubMed E-utilities for abstracts, Simplifier/dane.gov.pl APIs. Outcome codes: VERIFIED / CORRECTED / STILL NOT FOUND.

## Counts
- VERIFIED: 32
- CORRECTED: 6
- STILL NOT FOUND: 23 (of which 10 blocked for automated fetch, see NEEDS BROWSER)

## Poland
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

## Czechia
12. HDAB — VERIFIED as proposal: NCEZ department of MoH proposed as HDAB, amendment of Act 325/2021 pending (NRez minutes 26 Feb 2026). https://ppo.mzcr.cz/upload/files/jednani-nrez-26-2-2026-zapis-nrez-26-2-2026-69d627afb0218.pdf
13. Chemotherapy system — VERIFIED: DIOS regimen database (Masaryk University). https://portal.med.muni.cz/article-449-dios-dose-intensity-as-oncology-standard.html
14. Tumour-board software, synoptic pathology tool, openEHR — STILL NOT FOUND (DASTA DS4 defines NOR report elements only).
15. SNOMED Czech national edition — STILL NOT FOUND (MLDS requires login).

## Slovakia
16. TNM edition — CORRECTED: was "TNM 8 in 2024, 9th referenced 2026, mandate unclear"; now TNM 8 valid per 2024 methodology, TNM 9 effective 1 Jan 2026 per 2026 DGO guidance (Annex 1 TNM 9 code lists). https://www.nczisk.sk/Documents/nzr/2024/Metodicky_pokyn_NOR_SR_2024.pdf ; https://nczisk.sk/Documents/nzr/2026/MP_ZR_NOR_DGO.pdf (pdftotext)
17. HDAB — VERIFIED: NCZI project HeDAB-SK, HaDEA grant 972,587.20 EUR. https://nczisk.sk/en/International_cooperation/EHDS/Pages/Establishment-of-parts-of-the-health-data-access-body-in-the-Slovak-Republic.aspx
18. Chemotherapy software — VERIFIED: NÚDCH paediatric oncology clinic software. https://www.teraz.sk/zdravie/novy-softver-v-nudch-pomoze-zvysi/944037-clanok.html
19. ENCR/IACR membership — STILL NOT FOUND (list script-rendered).
20. 1+MG signatory, GDI node — STILL NOT FOUND (Slovak-language search returned only Slovenian/Czech results).
21. SNOMED Slovak edition/translation, researcher access route, MDT software, synoptic pathology, openEHR — STILL NOT FOUND.

## Hungary
22. Registry variable dictionary — VERIFIED: 2019 government list of electronically transmitted data elements (BNO-10 ch. II, BNO-10 morphology annex, pTNM per separate rule, grade, OENO). https://2015-2019.kormany.hu/download/b/ea/81000/ML.pdf (pdftotext)
23. ICD-O use — CORRECTED: registry coding based on ICD-10, not ICD-O (Wéber et al. 2023, PubMed abstract via E-utilities). https://pubmed.ncbi.nlm.nih.gov/36521336/
24. TNM edition — VERIFIED: TNM 8 (prostate 7th) in 2022 registry-based study. https://www.por-journal.com/articles/10.3389/pore.2022.1610668/full
25. National cancer plan — VERIFIED: programme 2006, revised 2018; OECD 2023 target. https://infostart.hu/belfold/2018/07/30/nemzeti-egeszsegprogram
26. Tumour-board software — VERIFIED: Semmelweis onkoteam rules (MedSolution); Oncompass used by 26 onkoteams. https://semmelweis.hu/jogigfoig/files/2022/05/Onkoteam_szabalyzat_hataly_2022_V_21.pdf
27. HDAB — STILL NOT FOUND (Hungarian-language search; no designation).
28. HL7 Hungary affiliate — STILL NOT FOUND (hl7.eu index, HL7 International reports).
29. Registry operator — VERIFIED earlier as OOI (mta.hu document); unchanged.
30. Synoptic pathology, chemotherapy system, openEHR, researcher access route, SNOMED HU edition — STILL NOT FOUND.

## Slovenia
31. HL7 Slovenia details — VERIFIED: est. 2014, 7 corporate + 10 individual members, chair Brane Leskošek (archived 2025-10-18). http://web.archive.org/web/20251018211849id_/https://hl7.eu/affiliate_si.html
32. HDAB — VERIFIED as not designated; SI-SUD project and OI/NIJZ critique of draft ZDigZ Art. 57 handling. https://ds-rs.si/sites/default/files/dogodek/dopis_oi_in_nijz_pripombe_in_predlogi_predlog_zdigz_epa_2240-ix.pdf
33. Tumour boards and chemotherapy software — VERIFIED: OI konziliji; Cypro drug-management software (Onkologija 2011). https://doaj.org/article/440523a9f08643c1bd5b8d35ebe98ad0
34. ICD-O/TNM editions in Register raka — STILL NOT FOUND: "Rak v Sloveniji 2022" (2025) not retrievable; dlib.si PDF streams return HTML; NIJZ yearbook cites only MKB-10.
35. OI Ljubljana OECI status — VERIFIED via browser capture (see item 63).
36. SI core FHIR package id — STILL NOT FOUND (packages.simplifier.net search API empty; Simplifier jurisdiction project list script-rendered).
37. Active-registration data format, synoptic pathology, SNOMED SI edition — STILL NOT FOUND.
38. hl7.si site — STILL NOT FOUND (archive.org blocked automated fetch).

## Croatia
39. ICD-O/TNM — VERIFIED: MKB-O version 3.1; stage recorded as summary stage, not TNM (HZJZ bulletin "Rak u Hrvatskoj 2023./2024.", pdftotext). https://www.hzjz.hr/wp-content/uploads/2026/02/Bilten-2023.pdf
40. Submission format — VERIFIED (from indexed text, PDF fetch returned HTML): hospital systems send oncology hospitalisation reports as monthly files into NAJS. https://www.aem.hr/wp-content/uploads/2022/02/6.-Svaki-novi-korak-digitalizacije.pdf
41. HL7 Croatia — VERIFIED: est. 2003, chair Miroslav Koncar, 6 individual + 4 org members (archive). http://web.archive.org/web/2025id_/https://hl7.eu/affiliate_co.html
42. HDAB — VERIFIED as none designated (legal analysis). https://hrcak.srce.hr/file/494682
43. CEZIH terminology server name/URL — STILL NOT FOUND (Simplifier guide "Terminologije" page script-rendered).
44. SNOMED HR edition, synoptic pathology, MDT software, chemotherapy system, ENCR membership record — STILL NOT FOUND.

## Romania
45. ICD-O-3 — VERIFIED: HG 663/2023 Art. 5(1) mandates CIM-O-3 (docx text extracted). https://management-documente.ms.ro/media/documents/HG_-REGISTRUL_NATIONAL_DE_CANCER_-_25.07.2023_2okqVrf.docx
46. Regional registry coding — VERIFIED: Cluj registry ICD-O-3 morphology; ICD-O-3.2 inclusion rules (ENCR 2021). https://iocn.ro/wp-content/uploads/2019/12/Cancerul_in_regiunea_nv_a_Romaniei_2010-2011.pdf
47. HL7 Romania — VERIFIED: Nov 2006, 21 members, chair Florica Moldoveanu (archive 2025-10-13). http://web.archive.org/web/20251013212616id_/https://hl7.eu/affiliate_ro.html
48. Tumour board practice — VERIFIED (press, single centre). https://adevarul.ro/stiri-interne/sanatate/tumor-board-abordarea-care-ofera-noi-sperante-1546906.html
49. RNC operational status — STILL NOT FOUND (INSP May 2026 lists development as ongoing). https://agerpres.ro/sanatate/2026/05/26/insp-aproximativ-40-dintre-cazurile-de-cancer-pot-fi-prevenite-printr-un-stil-de-viata-sanatos--1560130
50. TNM edition, HDAB, researcher access, synoptic pathology, chemotherapy system — STILL NOT FOUND.
51. CNAS DES specification content — STILL NOT FOUND (Cloudflare block).

## Bulgaria
52. Coding standards — CORRECTED/clarified: Nov 2025 draft ordinance has no coding standards; public comment requests ICD-O-3/ICD-10 rules (consultation PDF, pdftotext). https://www.strategy.bg/bg/public-consultations/11919/export
53. BNCR data quality methods — VERIFIED: Dimitrova & Parkin 2015 (MV 87.4 percent). https://eld.bl.uk/catalog/100032457892_0x000001
54. NCPHA bulletins by МКБ-10 — VERIFIED (pdftotext). https://ncpha.government.bg/uploads/magazines/bulletins/bul_onko_2020web.pdf
55. TNM edition, HDAB, HL7 Bulgaria, submission format, researcher access, MDT/pathology/chemo systems — STILL NOT FOUND.

## OECI (browser capture by team lead, https://accreditation.oeci.eu/ as of 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt)
60. Poland — CORRECTED: NIO-PIB (Maria Sklodowska-Curie National Research Institute of Oncology) is on the OECI certified-centres list; file previously said no accredited Polish centre.
61. Czechia — VERIFIED: Masaryk Memorial Cancer Institute on the list.
62. Hungary — VERIFIED: National Institute of Oncology (OOI) on the list.
63. Slovenia — VERIFIED: Institute of Oncology Ljubljana on the list (designation type not shown); resolves item 35.
64. Romania — CORRECTED: IOCN Cluj not on the current list; 2017 Clinical Cancer Centre certificate treated as lapsed (expiry 16 Nov 2022 per breast-unit directory).
65. Slovakia, Croatia, Bulgaria — VERIFIED: no centre on the list.

## Cross-country
56. ECIS prevalence registry list PDF — STILL NOT FOUND by fetch (returns 244-byte stub); earlier facts rest on search-index text.
57. DARWIN EU data partners PDF — fetch returns HTML (EMA block).
58. SNOMED national editions (CZ, SK, SI, HR, HU) — STILL NOT FOUND (MLDS login).
59. OECI accredited-centres directory — resolved via browser capture, see items 60–65.

## NEEDS BROWSER
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
