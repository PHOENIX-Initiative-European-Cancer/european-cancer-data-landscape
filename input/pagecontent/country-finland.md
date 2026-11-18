### Finland (FI)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "Finnish Base Profiles", package `hl7.fhir.fi.base` (also `.r4`/`.r4b`), v2.0.0 STU 2, FHIR R4, active 2025-10-05, official HL7 Finland standard (OID 1.2.246.777.11.2025.4), publisher HL7 Finland, canonical https://hl7.fi/fhir/finnish-base-profiles; no must-support; no R5 plan.
   https://hl7.fi/fhir/finnish-base-profiles/ ; https://get-ig.org/hl7.fhir.fi.base/2.0.0
2. **Oncology FHIR specifications:** not found. Kanta FHIR profiles (PHR, medication list) on Simplifier; no oncology profile set.
   https://www.kanta.fi/en/fhir-technology-and-kanta
3. **Cancer registry reporting:** Finnish Cancer Registry is THL's register maintained by the Cancer Society of Finland; statutory notification of every case or strong suspicion by hospitals, physicians and pathology, cytology and haematology laboratories. Current transmission format: not found (older literature: electronic transfers from large hospitals and labs plus manual forms). Variables include ICD-O-3 topography, morphology, behaviour, stage.
   https://cancerregistry.fi/cancer-information-notification/ ; https://finngen.gitbook.io/finngen-handbook/finngen-data-specifics/red-library-data-individual-level-data/what-phenotype-files-are-available-in-sandbox-1/other-registers/finnish-cancer-registry-detailed-cancer-data
4. **Terminologies:** SNOMED CT member 2018 (THL, 36th member); Finnish edition published each December (year of latest not stated); subset translation only. ICD-10: THL Tautiluokitus ICD-10 on the national code server (version not found); ICD-11 planned from 2028. National code server (Koodistopalvelu, content THL, operations Kela; SOAP/XML retired 13.1.2026 with v9.2), not available in FHIR. LOINC, ATC, ICD-O edition, TNM edition: not found. National FHIR terminology server: not yet available, in planning.
   https://www.snomed.org/members/finland ; https://conf.spaces.snomed.org/wiki/spaces/MCC/pages/131343642/Finland ; https://hl7.fi/fhir/finnish-base-profiles/terminology.html ; https://www.kanta.fi/documents/d/guest/koodistopalvelun-rajapinnat-ja-liittymisohje-1_8 ; https://packages.fhir.org/jurisdictions/FI
5. **Organisations and people:** HL7 Finland (technical committee), THL, Kela/Kanta, Cancer Society of Finland. Mikael Rinnetmäki (contact on fi.base IG, mikael@sensotrend.com).
   https://hl7.fi/fhir/finnish-base-profiles/ImplementationGuide-hl7.fhir.fi.base.json
