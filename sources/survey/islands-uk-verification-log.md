# Verification log for islands-uk.md and islands-uk-landscape.md

Pass run 2026-11-19. Method: direct curl of organisation pages and PDFs (pdftotext), Simplifier package catalog, TRUD guest pages, OECI/BBMRI-ERIC/EHDEN/EUCAIM/EUCanScreen/TEHDAS2/JANE partner pages, Wayback Machine (rate-limited after one request), targeted English and Greek searches. Outcomes: VERIFIED (fact now sourced), CORRECTED (old statement replaced), STILL NOT FOUND (what was tried). Edited statements in the two report files carry "(verified 2026-11-19)".

## United Kingdom

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

## Ireland

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

## Cyprus

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

## Malta

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

## Totals
- VERIFIED (fact or confirmed negative now sourced): 23
- CORRECTED (earlier statement replaced): 12 (items 16, 17, 21, 22, 32, 34, 35, 42, 43, 44, 49, 56, 57 counted as 12 distinct report statements)
- STILL NOT FOUND: 30 (items or sub-items above)

## NEEDS BROWSER
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
