# National FHIR, oncology and terminology survey: United Kingdom, Ireland, Cyprus, Malta

Researched 2026-11-18 for the HL7 Europe Common Cancer Data Model IG (ECCDM) editors. "Not found" means not verifiable from public sources. Items marked "not verified" come from search snippets or secondary sources because the primary site blocks automated fetches (digital.nhs.uk, hse.ie, ehealthireland.ie, dhir.gov.mt).

## United Kingdom

### 1. National base/core FHIR IG
- UK Core Implementation Guide, publisher HL7 UK with NHS England, FHIR R4 (4.0.1), canonical base https://fhir.hl7.org.uk. Published STU2 sequence 2.0.1 (16 Jul 2024, "second balloted UK Core"); the package registry also lists fhir.r4.ukcore.stu2 2.0.2 (latest tag) and 2.1.0, neither recorded in the version history page. STU3 sequence is a development build only (fhir.r4.ukcore.stu3.currentbuild 0.31.0-pre-release; Sprint 8 release 13 Feb 2026; not for implementation).
  https://simplifier.net/guide/ukcoreversionhistory ; https://packages.simplifier.net/fhir.r4.ukcore.stu2 ; https://simplifier.net/organization/hl7uk/news
- England: NHS England Implementation Guide, fhir.r4.nhsengland.stu1 1.5.0, UK Core derived. https://packages.simplifier.net/fhir.r4.nhsengland.stu1
- Wales: Wales FHIR Implementation Guide v2.7.0 STU2, package fhir.r4.wales, publisher NHS Wales (Data Standards Wales, DHCW), derived from UK Core STU2 2.0.2. https://simplifier.net/guide/fhir-standards-wales-implementation-guide
- Scotland: standards body Digital Health & Care Scotland; no Scottish core IG found; Care Reform (Scotland) Act 2025 gives powers to mandate information standards. https://packages.fhir.org/jurisdictions/GB
- Northern Ireland: Digital Health and Care NI; no NI IG found; encompass (Epic) live across all HSC Trusts May 2025. https://www.health-ni.gov.uk/news/digital-revolution-ni-patient-records

### 2. Oncology FHIR specifications
- COSD FHIR IG: none exists; the Simplifier package catalog returns no package for "cosd" and only US and international cancer IGs for "cancer" https://packages.simplifier.net/catalog?name=cancer (verified 2026-11-19).
- NHS England FHIR Genomics Implementation Guide: package uk.nhsengland.genomics.r4 0.6.11 (latest), FHIR R4, status "Draft in progress" on the NHS Standards Directory (page updated 17 Aug 2026), canonical https://fhir.nhs.uk/ImplementationGuide/FHIR-Genomics-Implementation-Guide. Package dependencies include hl7.fhir.us.mcode 4.0.0 and hl7.fhir.uv.genomics-reporting 3.0.0, so it reuses mCODE. Does not implement a cancer registry standard.
  https://standards.nhs.uk/published-standards/fhir-genomics-implementation-guide ; https://packages.simplifier.net/uk.nhsengland.genomics.r4
- Scotland, Wales, Northern Ireland oncology FHIR IGs: still not found (Simplifier catalog and fhir.r4.wales 2.7.0 contain no oncology profiles; checked 2026-11-19).

### 3. Cancer registry reporting standard
- England: COSD submitted to the National Disease Registration Service (NDRS, NHS England) as XML against the COSD XML schema published on TRUD. NHS Standards Directory: COSD v10.0 information standard DAPB1521 Amd 89/2022, published 11 Sep 2023, status Active, with COSD Pathology v5.0 supplied by pathology departments; scope all cancer patients in acute settings, excluding private and primary care https://standards.nhs.uk/published-standards/cancer-outcomes-and-services-data-set (verified 2026-11-19). Dataset v10.2.0; user guide v10.2.12 (10.2.11 dated 2 Jun 2026); Pathology v5.1.x; COSD v11 in development with no published timeline; no FHIR route. TRUD lists COSD XML Schema release 10-2-0 (released 27 Mar 2024, usable from 1 Apr 2024, information standard DAPB1521, produced by NDRS) and COSD Pathology XML Schema release 5-1-1; COSD enquiries nhsdigital.cosdenquiries@nhs.net https://isd.hscic.gov.uk/trud/users/guest/filters/0/categories/1/items/246/releases (verified 2026-11-19). User guide v10.2.12 and v11 statements remain from search snippets of digital.nhs.uk (not verified). https://digital.nhs.uk/ndrs/data/data-sets/cosd ; https://standards.nhs.uk/published-standards/cancer-outcomes-and-services-data-set
- Wales: Welsh Cancer Intelligence and Surveillance Unit (WCISU, Public Health Wales) receives pathology, MDT, inpatient (PEDW), radiology, radiotherapy and death feeds; National Cancer Data Standards for Wales DSCN 2019/09 (amended 17 Jul 2025) reference COSD v9.0 for comparability. https://publichealthwales.nhs.wales/services-and-teams/welsh-cancer-intelligence-and-surveillance-unit-wcisu/ ; https://dhcw.nhs.wales/data/information-standards/data-standards/data-standards-files/20250717-dscn-2019-09-nat-cancer-ds-core-banked-tissue-amd-docx-pdf/
- Scotland: Scottish Cancer Registry (SMR06), Public Health Scotland; about 800,000 source records a year (hospital discharge, pathology, radiotherapy, haematology/oncology, screening, prescribing, deaths) linked by probabilistic matching; SACT data from all five cancer centres feeds in weekly; file format of the submissions still not found https://www.scotpho.org.uk/methods-and-data/overview-of-key-data-sources/scottish-national-data-schemes/cancer/ ; https://htn.co.uk/2021/04/20/data-from-cancer-centres-connected-to-provide-full-population-coverage-for-scottish-nhs/ (verified 2026-11-19).
- Northern Ireland: Northern Ireland Cancer Registry (NICR) at Queen's University Belfast, funded by the Public Health Agency; electronic extracts from the four pathology labs, HSC systems and GRO death registrations; no FHIR. https://www.qub.ac.uk/research-centres/nicr/FileStore/OfficialStatistics1993-2022/July2025release/Methodology%20report.pdf

### 4. Terminologies
- SNOMED CT: UK is a founder member; NHS England is the National Release Centre for the SNOMED CT UK Edition (UK Clinical, Drug and Pathology extensions, maps to ICD-10 and OPCS-4) via TRUD. Latest SNOMED CT UK Clinical Edition release 43.0.1, released 20 Oct 2026 (replaces 43.0.0 of 6 Oct 2026; monthly minor releases such as 42.4.0 on 5 Aug 2026; major release 42.0.0 on 15 Apr 2026); UK Monolith Edition 43.1.0 on 28 Oct 2026; UK Drug Extension 42.1.0 released 13 May 2026, GTINs added in 43.1.0 on 28 Oct 2026 https://isd.hscic.gov.uk/trud/users/guest/filters/0/categories/26/items/101/releases ; https://isd.hscic.gov.uk/trud3/user/guest/group/0/pack/26 (verified 2026-11-19). https://www.snomed.org/members/united-kingdom
- ICD-10: ICD-10 5th edition (England NCCS 2026; Scotland PHS ICD-10 v5 consolidation 2026). https://classbrowser.nhs.uk/ ; https://publichealthscotland.scot/publications/icd-10-consolidation-2026/
- OPCS-4: OPCS-4.10 from 1 Apr 2023; OPCS-4.11 mandatory in England (DAPB0084) and Wales (DSCN 2026/08) from 1 Apr 2026. https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dapb0084-opcs-classification-of-interventions-and-procedures
- ICD-O-3 for morphology/topography in all four registries (NI switched from ICD-O-2 to ICD-O-3 in 2019; the ICD-O-3 revision used in England still not found; the gov.uk NCRAS methodology page names only ICD-10 and TNM https://www.gov.uk/government/publications/ncras-statistical-publications-quality-and-methodology-information/cancer-registration-methodology , checked 2026-11-19).
- TNM: UICC/AJCC TNM 8 from 1 Jan 2018 (confirmed for Wales and NI; RCPath table for England).
- LOINC: no national use; pathology uses the SNOMED CT Unified Test List (Pathology Test and Results Standard). https://standards.nhs.uk/published-standards/pathology-test-and-results-standard
- Medicines: dm+d (code system https://dmd.nhs.uk).
- Terminology servers: NHS England Terminology Server (Ontoserver), https://ontology.nhs.uk/production1/fhir (SNOMED CT, dm+d, ICD-10 4.0 and 5.0, OPCS-4.8 to 4.11); NHS Scotland Terminology Server, NHS National Services Scotland, live Jul 2022, https://www.snomed.nhs.scot/?p=51

### 5. Key organisations and people
- HL7 UK: chair Ben McAlister; technical committee chair Rik Smithies. UK Core maintained by the NHS England Interoperability Standards team (interoperabilityteam@nhs.net); release posts by Ryan May, Adam Page, John George. https://simplifier.net/organization/hl7uk/news ; https://hl7.eu/affiliate_uk.html
- Genomics IG: NHS England Genomics Unit (Genomic Medicine Service interoperability team).
- COSD: NDRS COSD team, mailbox nhsdigital.cosdenquiries@nhs.net https://isd.hscic.gov.uk/trud/users/guest/filters/0/categories/1/items/246/releases (verified 2026-11-19); named lead still not found.
- Registries: NICR director Dr Damien Bennett; Scottish Cancer Registry director Prof David Morrison (PHS). https://publichealthscotland.scot/our-blog/2025/june/increasing-cancer-prevalence-the-story-behind-the-projections/

## Ireland

### 1. National base/core FHIR IG
- None published. State of FHIR 2026 (contributor Patrick Marren, HSE MyHealth@EU team leader): "no national base FHIR implementation guide yet"; HIQA is the national standards body; FHIR R4 in use; a national FHIR terminology server is in production; Ireland is establishing a FHIR affiliate. https://packages.fhir.org/jurisdictions/IE
- Vendor/community guides: IE (Ireland) Core Implementation Guide 1.0.0-ballot, publisher iEHR.ai, FHIR R4, canonical http://iehr.ai/fhir/ie/core/ImplementationGuide/iehr.fhir.ie.core, certified phase one by GPIT (ICGP, HSE, Department of Health). https://www.iehr.ai/fhir/ie/core/ FHIR-IRL-Core 0.1.0, draft, derived from HL7 Europe Core, not sponsored by an official body. https://github.com/HL7-Ireland-Shadow/FHIR-IRL-Core
- HL7/openEHR Ireland affiliate proposal meeting held 11 May 2026 in Dublin. https://discourse.openehr.org/t/hl7-openehr-ireland-affiliate-meeting-monday-11-may-2026/16789
- HSE FHIR use: Health App, MyHealth@EU, National Shared Care Record (event 20 Oct 2025). https://www.ehealthireland.ie/news-media/news/2025/fhir-and-the-national-shared-care-record-a-transformative-step-in-irish-healthcare

### 2. Oncology FHIR specifications
- None found. NCRI publishes no FHIR specification; no mCODE reuse found.

### 3. Cancer registry reporting standard
- National Cancer Registry Ireland (NCRI), statutory body, Cork. Electronic feeds: monthly or quarterly histopathology lab feeds (SNOMED-coded, converted to ICD-O by NCRI), radiotherapy unit feeds, quarterly HIPE feed, quarterly CSO death feed; about 90% of tumours created electronically; Cancer Data Registrars complete records in the NCRI Cancer Registration System. No FHIR or published CSV submission standard. Data Dictionary v2.0 (2023). https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri ; https://www.ncri.ie/en/media/145/download

### 4. Terminologies
- SNOMED CT: member since Nov 2016; NRC is HSE Technology and Transformation (snomed@hse.ie); SNOMED CT Irish Edition with Irish Clinical and Drug Extension; production releases Oct 2025 (11th), Jan 2026, Feb 2026, Jun 2026. https://www.snomed.org/members/ireland ; https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/1003192357
- ICD-10-AM/ACHI/ACS 12th edition for HIPE from 1 Jan 2024 (10th edition 2020 to 2023); 13th edition adoption still not found; the HPO 2025 activity report, published Sep 2026, still describes the 10th to 12th edition change https://www.drugsandalcohol.ie/47018/1/HIPE_2025_Activity_in_Acute_Public_Hospitals_.pdf (checked 2026-11-19). https://www.hse.ie/eng/about/personalpq/pq/2025-pq-responses/july-2025/pq-35566-25-padraig-mac-lochlainn.pdf
- NCRI coding: ICD-O-3.2 from 2020 (ICD-O-3.1 2012-2019); UICC TNM 7th edition from 2014, with 1994-2013 cases recoded to TNM7 and no move to TNM 8 (NCRI Data Dictionary v2.0 and Cancer in Ireland 1994-2023 report, section "TNM staging"); ACHI 6th edition for treatments; reporting in ICD-10 https://www.ncri.ie/en/media/145/download ; https://www.drugsandalcohol.ie/46716/1/NCRI_AnnualStatReport_2026.pdf (verified 2026-11-19).
- LOINC: adopted for laboratory data; hosted on the HSE Central Terminology Service (CTS) with SNOMED CT Irish Edition (incl. medicines) and UCUM. CTS procured Jul 2025, deployed Q3 2025 to Q1 2026, FHIR terminology server run by the HSE Data Standards Team (National Release Centre for SNOMED, CDAO); built on CSIRO Ontoserver, delivered and managed by Dedalus; HSE press release (29 Jun 2026) dates procurement to July 2025, eHealth Ireland (16 Dec 2025) to September 2025; contact DataAndInformationStandards@hse.ie https://about.hse.ie/news/the-hse-central-terminology-service-cts (verified 2026-11-19). ; https://www.ehealthireland.ie/news-media/news/2025/fhir-central-terminology-server-for-the-hse
- ATC: WHO ATC classification used by the HSE Primary Care Reimbursement Service for dispensing data https://www.hse.ie/eng/staff/pcrs/pcrs-publications/annual-report-2018.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5662670 (verified 2026-11-19). UICC edition in clinical use: still not found.

### 5. Key organisations and people
- HSE Technology and Transformation, Enterprise Architecture: Theresa Barry, Clinical Terminology Architect, SNOMED Member Forum representative; Niall Sinnott, Department of Health, SNOMED General Assembly representative; Patrick Marren, HSE MyHealth@EU team leader. https://www.snomed.org/members/ireland
- NCRI: Dr Theresa Redaniel, acting director (2026), after Prof Deirdre Murray's five-year term. https://ncri.ie/en/news/news-from-ncri/dr-theresa-redaniel-appointed-acting-director-of-the-national-cancer-registry

## Cyprus

### 1. National base/core FHIR IG
- None published. State of FHIR 2026 (anonymous respondent): "a national core guide exists and is used in a limited set of use cases"; FHIR advised, not mandated; NeHA appointed Digital Health Authority under EHDS Article 19; terminology server status unclear. https://packages.fhir.org/jurisdictions/CY
- Only public package: ehealth4u.package 1.0.0, FHIR R4, University of Cyprus eHealth Lab, draft prototype of the national EHR, depends on hl7.fhir.uv.ips 1.1.0. https://packages.simplifier.net/ehealth4u.package ; https://doi.org/10.1177/20552076261431813
- National EHR: NeHA designing it, development scheduled to begin late 2026. https://www.interregeurope.eu/good-practices/national-ehealth-authority-neha

### 2. Oncology FHIR specifications
- None found.

### 3. Cancer registry reporting standard
- Cyprus Cancer Registry (CyCR), Health Monitoring Unit, Ministry of Health; population-based; member of IACR and ENCR; registry staff code hospital notifications (public and private hospitals and clinics) using MECC/NCI coding and staging; submission format still not found (Ministry of Health site blocks automated access, checked 2026-11-19); no FHIR. https://pmc.ncbi.nlm.nih.gov/articles/PMC11168067/

### 4. Terminologies
- SNOMED CT: member since Sept 2018; NRC is the National eHealth Authority (NeHA); no national extension found; adoption "subject to a decision for adoption by all involved stakeholders". https://www.snomed.org/members/cyprus ; https://www.snomed.org/snomed-in-action/national-ehealth-authority-of-cyprus
- Current coding mix: ICD-10, LOINC, ICPC, CPT-4 (reimbursement), free text (NeHA statement). ICD-10 national modification: not found.
- Registry: ICD-O-3, ICD-10, SEER Summary Staging, TNM (edition still not found; MECC 2009 coding manual is the last public coding reference https://webarchive.library.unt.edu/web/20130213205307/http:/mecc.cancer.gov/2009_MECC_Manual_of_Coding.pdf ).
- National terminology server: in planning, not available. ATC, UICC edition: not found.

### 5. Key organisations and people
- NeHA (https://www.neha.org.cy/): Marios Neofytou, SNOMED General Assembly and Member Forum representative; Melanie Fysentzou, Member Forum.
- eHealth4U, University of Cyprus: Prof Constantinos S. Pattichis, Prof Christos N. Schizas.
- Registry: Anna Demetriou, Statistics Officer at the Health Monitoring Unit and Health Ministry representative on the National Cancer Institute board https://en.politis.com.cy/news/health/1031893/first-board-appointed-for-national-cancer-institute (verified 2026-11-19); registry head still not found (MECC 2009 manual listed Dr Pavlos Pavlou as Cyprus coordinator, historical).

## Malta

### 1. National base/core FHIR IG
- None. Simplifier jurisdiction MT lists 0 projects and no survey response. https://packages.fhir.org/jurisdictions/MT
- National EHR (Ministry for Health, myHealth portal) runs on openEHR (Better platform, deployed May 2019). https://www.openEHR.org/deployments/provider_deployments_detail/34
- Digital Health and Health Data Strategy 2030 (consultation 21 Nov 2025 to 21 Jan 2026) names interoperability as an aim; no FHIR profile set found. https://www.gov.mt/en/publicconsultation/Pages/2025/NL-0041-2025.aspx

### 2. Oncology FHIR specifications
- None found.

### 3. Cancer registry reporting standard
- Malta National Cancer Registry, Directorate for Health Information and Research (DHIR), Ministry for Health; population-based since 1991; listed in the ENCR members contact list as Malta National Cancer Register, Department of Health Information and Research, director Dr Neville Calleja https://www.encr.eu/encr-members-contact-list?page=12 (verified 2026-11-19); national submission format still not found (European reporting via ENCR/ECIS data protocol). https://ghdx.healthdata.org/node/113711 ; https://www.encr.eu/sites/default/files/Data_call/ECIS-data-protocol_2026.pdf

### 4. Terminologies
- SNOMED CT: member since Oct 2011; NRC is the Information Management Unit, Ministry for Health; SNOMED CT is the "terminology of choice" for EHRs; no Maltese translation; used in the National Patient Summary and MyHealth@EU value set mapping; Malta hosts SNOMED CT Expo 2027. https://www.snomed.org/members/malta ; https://health.gov.mt/national-level-service/snomed-national-release-centre-malta/
- ICD-10 used for cause-of-death data since 1995 and for hospital discharge diagnoses in the DHIR National Hospital Information System; procedures coded in ICD-9-CM, no national ICD-10 modification https://ec.europa.eu/eurostat/cache/metadata/en/hlth_res_esms_mt.htm (verified 2026-11-19). https://ec.europa.eu/eurostat/cache/metadata/en/hlth_cdeath_simscd_mt.htm
- Registry datasets coded in ICD-O-3. TNM edition, LOINC, ATC, national terminology server: still not found (checked 2026-11-19).

### 5. Key organisations and people
- Ivan Cacciottolo, Ministry for Health, SNOMED General Assembly and Member Forum representative (ivan.cacciottolo@gov.mt).
- DHIR (https://dhir.gov.mt/, blocks automated access) runs the registry; registry director Dr Neville Calleja per the ENCR members contact list https://www.encr.eu/encr-members-contact-list?page=12 (verified 2026-11-19).
