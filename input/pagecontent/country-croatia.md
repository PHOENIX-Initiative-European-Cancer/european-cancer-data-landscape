### Croatia (HR)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** "CEZIH osnova" (CEZIH Base Guide) on Simplifier; the guide shows package cezih.hr.base#1.1 based on FHIR R4; registry packages cezih.hr.cezih-osnova 0.2.9, 1.0.0–1.0.2 (deprecated flags) and 1.0.3-beta, FHIR R4, canonical base http://fhir.cezih.hr/specifikacije/. CEZIH operated under Ministry of Health and HZZO; FHIR messaging, documents and REST used; national terminology server "in production".
   https://simplifier.net/guide/cezih-osnova ; https://packages.simplifier.net/cezih.hr.cezih-osnova ; https://packages2.fhir.org/xig/resource/cezih.hr.cezih-osnova%7C1.0.2/StructureDefinition/StructureDefinition-hr-message-header.json ; https://api.simplifier.net/jurisdictions/HR
2. **Oncology FHIR specifications:** none found. A unified ONKO+ message (upgrade of the existing CEZIH malignant-neoplasm notification message, to be aligned with European cancer-reporting standards) was developed and tested on the central system but not implemented in hospital systems; format not stated. mCODE reuse: not found.
   https://hrcak.srce.hr/file/355760
3. **Cancer registry reporting standard:** Registar za rak at HZJZ (since 1959). Sources: hospital Onko-tip form (JZ-ONK), outpatient "Prijava maligne neoplazme" (JZ-NEO), copies of histology/cytology/autopsy findings; electronic reporting of cancer hospitalisations via CEZIH since 2017; legal basis Law on Official Statistics.
   https://hrcak.srce.hr/file/429874 ; https://hrcak.srce.hr/file/355760
4. **Terminologies:** SNOMED CT: member since June 2023 (Croatian Ministry of Health; GA rep Srebrenka Mesić, Member Forum Andreja Matkun, Višnja Antolković Ilić); national edition: not found. National terminology server: "available and in production" per State of FHIR 2026, name/URL/operator not found. MKB-10 version: not found. Cancer registry codes morphology/topography with MKB-O (ICD-O) version 3.1 and records stage as summary stage (localised/regional/distant), not TNM, per HZJZ bulletin "Rak u Hrvatskoj 2023./2024." (verified 2026-11-19) https://www.hzjz.hr/wp-content/uploads/2026/02/Bilten-2023.pdf . LOINC, ATC variant: not found.
   https://www.snomed.org/members/croatia ; https://api.simplifier.net/jurisdictions/HR
5. **Organisations and people:** Ministry of Health, HZZO (CEZIH), HZJZ (registry). HL7 Croatia (established 2003, 6 individual and 4 organisational members) chair Miroslav Koncar per archived HL7 Europe affiliate page (verified 2026-11-19) http://web.archive.org/web/2025id_/https://hl7.eu/affiliate_co.html State of FHIR contributors Siniša Koščina (IN2), Krešimir Kerš (Ericsson Nikola Tesla); registry head Ariana Znaor (HZJZ, per hrcak article).
   https://hl7.eu/affiliate_co.html ; https://api.simplifier.net/jurisdictions/HR ; https://hrcak.srce.hr/file/429874

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Registar za rak, HZJZ (since 1959; IACR member since 1994); coverage 100% (ECIS); legal basis Law on Official Statistics (NN 103/2003) and annual programme. https://hrcak.srce.hr/file/429874 ; https://ecis.jrc.ec.europa.eu/pdf/Prevalence_List_of_cancer_registries.pdf
- Submission: hospital Onko-tip form (JZ-ONK), outpatient "Prijava maligne neoplazme" (JZ-NEO), pathology/cytology copies; electronic hospitalisation reporting via CEZIH since 2017; unified ONKO+ message developed/tested but not implemented in hospital systems. https://hrcak.srce.hr/file/355760
- Variable dictionary: morphology/topography coded with MKB-O (ICD-O) version 3.1; stage recorded as summary stage (localised / regional / distant metastases), not TNM; registry follows ENCR rules on incidence date and multiple primaries (verified 2026-11-19) https://www.hzjz.hr/wp-content/uploads/2026/02/Bilten-2023.pdf
- Submission format: hospital information systems send oncology hospitalisation reports as monthly files into NAJS (verified 2026-11-19) https://www.aem.hr/wp-content/uploads/2022/02/6.-Svaki-novi-korak-digitalizacije.pdf
- New registry platform within NAJS (National Public Health Information System). https://www.hzjz.hr/wp-content/uploads/2021/12/Bilten_2019.pdf
- Screening registries: breast, colorectal, cervical programmes linked to CEZIH and ZOROH. https://hrcak.srce.hr/file/462086
- Researcher access: confidential data request form on registry website (aggregated vs individual-level); public data with quality indicators. https://hrcak.srce.hr/file/284364

#### (b) Public datasets
- HZJZ annual bulletin "Incidencija raka u Hrvatskoj" (2023 data published Feb 2026). https://www.hzjz.hr/wp-content/uploads/2026/02/Bilten-2023.pdf
- ECIS: Croatian registry contributes. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Open data portal (data.gov.hr) cancer datasets, synthetic data: n/f. HDAB: no body designated; Croatian legal analysis finds the secondary-use framework fragmented with no single body (verified 2026-11-19) https://hrcak.srce.hr/file/494682 . TEHDAS2 partner: HZJZ. https://tehdas.eu/tehdas2/partners/

#### (c) Cancer infrastructure
- Plan: Nacionalni strateški okvir protiv raka do 2030 (NN 141/20, Dec 2020); action plan adopted later (3-year); ENO project for National Oncology Network and National Oncology Database (equipment ~10.6 m EUR extra). https://www.iccp-portal.org/system/files/plans/NPPR_program_HR_2020_17-01.pdf ; https://www.novilist.hr/?p=1396506
- OECI: no Croatian centre on the OECI certified-centres list as of 2026-11-19 (verified 2026-11-19) https://accreditation.oeci.eu/ ; KBC Sestre milosrdnice (Klinika za tumore) listed as member not in accreditation. https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: 1+MG signatory (17th, 2018); GDI and Genome of Europe led by Ruđer Bošković Institute. https://www.irb.hr/eng/Research/Projects/Genomic-Data-Infrastructure-GDI
- Biobank: not a BBMRI-ERIC member; TransMedRi biobank Rijeka, "10,001 Dalmatians". https://www.bbmri-eric.eu/national-nodes/ ; https://biobank.uniri.hr/
- Imaging/EUCAIM: none listed. EU projects: CraNE (HZJZ), EUCanScreen (HZJZ, KBC Zagreb), TEHDAS2 (HZJZ), ECHoS hub planned. https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/
- OMOP: EHDEN partners KBC Osijek (IN2), KB Dubrava, KBC Zagreb, Primorje-Gorski Kotar health centre, KBC Sestre milosrdnice (IGEA). https://www.ehden.eu/datapartners/

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: CEZIH (HL7 v3 and CDA prevalent on national network; HL7 v2 in hospitals); Portal zdravlja via e-Građani. https://hl7.eu/affiliate_co.html ; https://gov.hr/hr/portal-zdravlja-dostupan-i-na-mobilnim-uredjacima/2340
- Registry exchange: CEZIH malignant-neoplasm notification message; planned ONKO+ message. https://hrcak.srce.hr/file/355760
- Structured pathology, tumour-board software, chemotherapy system, openEHR: still n/f after Croatian-language search (hospital systems described as fragmented, https://www.aem.hr/wp-content/uploads/2022/02/9.-Hrvatska-je-mala.pdf).
- Strategy items: National Health Development Plan 2021–2027 (eHealth priority). https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/HRV_Croatia_National-Health-Development-Plan_2021-2027.pdf

#### Key organisations and people
- HZJZ Registar za rak (Mario Šekerija, Ariana Znaor as registry leads in cited articles). https://www.aem.hr/wp-content/uploads/2022/01/2.-Doc.-dr.-Mario-Sekerija.pdf ; https://hrcak.srce.hr/file/429874
- Ministry of Health / HZZO (CEZIH); Ericsson Nikola Tesla, IN2, IGEA (vendors); IRB (genomics); HL7 Croatia (Miroslav Koncar).

---
