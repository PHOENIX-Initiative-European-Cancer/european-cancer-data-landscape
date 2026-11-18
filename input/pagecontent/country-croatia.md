### Croatia (HR)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** "CEZIH osnova" (CEZIH Base Guide) on Simplifier; the guide shows package cezih.hr.base#1.1 based on FHIR R4; registry packages cezih.hr.cezih-osnova 0.2.9, 1.0.0–1.0.2 (deprecated flags) and 1.0.3-beta, FHIR R4, canonical base http://fhir.cezih.hr/specifikacije/. CEZIH operated under Ministry of Health and HZZO; FHIR messaging, documents and REST used; national terminology server "in production".
   https://simplifier.net/guide/cezih-osnova ; https://packages.simplifier.net/cezih.hr.cezih-osnova ; https://packages2.fhir.org/xig/resource/cezih.hr.cezih-osnova%7C1.0.2/StructureDefinition/StructureDefinition-hr-message-header.json ; https://api.simplifier.net/jurisdictions/HR
2. **Oncology FHIR specifications:** none found. A unified ONKO+ message (upgrade of the existing CEZIH malignant-neoplasm notification message, to be aligned with European cancer-reporting standards) was developed and tested on the central system but not implemented in hospital systems; format not stated. mCODE reuse: not found.
   https://hrcak.srce.hr/file/355760
3. **Cancer registry reporting standard:** Registar za rak at HZJZ (since 1959). Sources: hospital Onko-tip form (JZ-ONK), outpatient "Prijava maligne neoplazme" (JZ-NEO), copies of histology/cytology/autopsy findings; electronic reporting of cancer hospitalisations via CEZIH since 2017; legal basis Law on Official Statistics.
   https://hrcak.srce.hr/file/429874 ; https://hrcak.srce.hr/file/355760
4. **Terminologies:** SNOMED CT: member since June 2023 (Croatian Ministry of Health; GA rep Srebrenka Mesić, Member Forum Andreja Matkun, Višnja Antolković Ilić); national edition: not found. National terminology server: "available and in production" per State of FHIR 2026, name/URL/operator not found. MKB-10 version, ICD-O-3, TNM, LOINC, ATC variant: not found.
   https://www.snomed.org/members/croatia ; https://api.simplifier.net/jurisdictions/HR
5. **Organisations and people:** Ministry of Health, HZZO (CEZIH), HZJZ (registry). HL7 Croatia chair Miroslav Koncar per HL7 Europe affiliate page (page offline at survey time). State of FHIR contributors Siniša Koščina (IN2), Krešimir Kerš (Ericsson Nikola Tesla); registry head Ariana Znaor (HZJZ, per hrcak article).
   https://hl7.eu/affiliate_co.html ; https://api.simplifier.net/jurisdictions/HR ; https://hrcak.srce.hr/file/429874
