### Denmark (DK)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "HL7 FHIR Implementation Guide: DK Core" (DkCore), package `hl7.fhir.dk.core`, FHIR R4 (4.0.1), latest release 3.7.0 (IG dated 2026-05-30; 3.5.0 published 2025-12-19), published by HL7 Denmark with MedCom as steward, released twice a year. Canonical http://hl7.dk/fhir/core. MedCom layers `medcom.fhir.dk.core` 4.0.0 (R4) on top.
   https://hl7.dk/fhir/core/index.html ; https://packages.fhir.org/hl7.fhir.dk.core ; https://build.fhir.org/ig/medcomdk/dk-medcom-core
2. **Oncology FHIR specifications:** not found. No DMCG, RKKP or Cancerregisteret FHIR IG located; Danish FHIR work covers referrals, diagnostics, documents and telemedicine (FUT eHealth Infrastructure).
   https://packages.fhir.org/jurisdictions/DK ; https://ehealth.sundhed.dk/fhir
3. **Cancer registry reporting:** Cancerregisteret is run by Sundhedsdatastyrelsen (unit Klassifikationer og Inddata). Fully electronic since 2004; fed from Landspatientregisteret LPR3 (diagnoses, mandatory cTNM, optional pTNM; LPR3 reporting guide 2025 v5.1) and from Patobank (pathology departments, MEDRPT EDI messages via daily FTP). Coded in ICD-10 (diagnosis) plus ICD-O-3 (morphology) since 2004.
   https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf
4. **Terminologies:** SNOMED CT charter member 2007; NRC Sundhedsdatastyrelsen; Danish extension bi-annual (March/September), latest September 2025 on the August 2025 International Edition. ICD-10 via SKS (Sundhedsvæsenets Klassifikations System, Sundhedsdatastyrelsen; version numbering not found). ICD-O-3 for morphology. LOINC: DK Core has LOINC and NPU observation profiles; NPU is the lab terminology (NPU CodeSystem INT 2026-03-27 published by SDS). ATC: not found. TNM edition: not found (LPR3 requires cTNM; Nordic studies used UICC 7th). National FHIR terminology server: not yet available, in planning; Nordic shared server tx-nordics.fhir.org/fhir (HL7 Sweden-hosted, not for production).
   https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/148406293 ; https://packages.fhir.org/jurisdictions/DK ; https://hl7norway.github.io/best-practice/referat/2025-09-10-referat.html
5. **Organisations and people:** HL7 Denmark (dk-affiliate@hl7.dk, secretariat Dansk Standard), MedCom, Sundhedsdatastyrelsen. Chair sources conflict: Thea Mentz Sørensen (chair from 1 Jan 2024 per MedCom; listed 2025) and Jens Kristian Villadsen (HL7 Europe pages). Kirstine Rosenbeck Gøeg (MedCom) leads hackathon tracks.
   https://fhir.fi/en/demo2025/hl7-denmark/ ; https://hl7.eu/affiliate_dk.html ; https://hl7.dk/
