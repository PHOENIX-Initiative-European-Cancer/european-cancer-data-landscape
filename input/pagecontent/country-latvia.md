### Latvia (LV)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** none. Ministry of Health decides standards; SPKC maintains ICD-10; Latvijas Digitālās veselības centrs (LDVC) established 2025 as digital health authority; NVD operates e-veselība (Cabinet Regulation No. 134). FHIR R4B primary; systems use generic FHIR without IGs; discharge summary spec is CDA (NVD.EVK.CDA.3.09 v1.1).
   https://packages.fhir.org/jurisdictions/LV ; https://lvportals.lv/dienaskartiba/385601-latvijas-digitalas-veselibas-centrs-pirmaja-darbibas-gada-paveikts-butisks-darbs-digitalas-veselibas-attistiba-2026 ; https://www.varam.gov.lv/lv/media/46103/download
2. **Oncology FHIR specifications:** not found. Survey cites "oncology registry" as a FHIR use case without a published spec. Since 1 January 2024 institutions must submit the cancer patient card in e-veselība.
   https://packages.fhir.org/jurisdictions/LV ; https://vmnvd.gov.lv/lv/media/28572/download
3. **Cancer registry reporting:** oncology part of "Ar noteiktām slimībām slimojošu pacientu reģistrs", run by SPKC; data from NVD/e-veselība (cancer patient card) and monthly transfers; ICD-10 C00–C97; reporting to ENCR/IARC; manual collection reported in 2024. Technical format: not found.
   https://statistika.spkc.gov.lv/Resources/PX/Databases/Health/Metadati/ONKO_Registra_metadati_en.html ; https://www.lsm.lv/raksts/zinas/latvija/20.08.2024-veza-registrs-vel-nepabeigts-un-nepilnigs.a565719/
4. **Terminologies:** SNOMED CT member since January 2026; NRC SPKC; roadmap to 2030; SNOMED GPS used for cross-border and lab exchange. SSK-10 (ICD-10, SPKC; version not found; SSK-11 under consideration). LOINC and UCUM planned. ICD-O-3, TNM, ATC: not found. National FHIR terminology server: in production per survey; operator and URL not found.
   https://www.snomed.org/members/latvia ; https://lvportals.lv/dienaskartiba/395031-snomed-ct-palidzes-veidot-vienotu-klinisko-zinasanu-telpu-latvija-2026 ; https://likumi.lv/ta/id/264943
5. **Organisations and people:** Ministry of Health, SPKC, NVD, LDVC. Named FHIR or oncology spec maintainers: not found.
