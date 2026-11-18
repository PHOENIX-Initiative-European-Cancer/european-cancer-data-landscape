### Lithuania (LT)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "Lithuanian Base Implementation Guide" (LTBase), package `lt.hl7.fhir.base` 0.3.0 (DSTU 1 draft, "not ready for production"), FHIR R5 (5.0.0), canonical https://hl7.lt/fhir/base, published via HL7 Lithuania registry (hl7.lt, GitHub HL7LT) by the Lithuanian Medical Library. Legacy national ESPBI system (Registrų centras) uses DSTU1 Atom feeds (SKL01–03) and an eLab FHIR IG with ESPBI identifiers.
   https://hl7.lt/fhir/base/0.3.0/en/index.html ; https://hl7.lt/ ; https://specialistas-pub.esveikata.lt/dp/elab/iframe/fhir-ig/StructureDefinition-lt-patient-definitions.html
2. **Oncology FHIR specifications:** ADP early-diagnosis programme IGs: `lt.hl7.fhir.lung` (LDCT screening, Lung-RADS v2022), `lt.hl7.fhir.colorectal`, `lt.hl7.fhir.cervical`, `lt.hl7.fhir.breast`, `lt.hl7.fhir.prostate`; all 0.0.1 CI-build drafts (2026-09), FHIR R5, publisher Lithuanian Medical Library; depend on lt.hl7.fhir.base, lt.hl7.fhir.lab (pathology report, ICD-O-3 morphology, prostate pTNM, AJCC grade), lt.hl7.fhir.eu and hl7.fhir.eu.base-r5 0.1.0. No mCODE dependency. They implement national screening datasets, not the cancer registry standard.
   https://build.fhir.org/ig/HL7LT/ig-lt-lung/en/index.html ; https://build.fhir.org/ig/HL7LT/ig-lt-colorectal/en/terminology.html ; https://build.fhir.org/ig/HL7LT/ig-lt-lab/en/terminology.html
3. **Cancer registry reporting:** Lithuanian Cancer Registry (Vėžio registras) run by Nacionalinis vėžio institutas (NVI); primary source is form Nr. 090/a (notice of first-diagnosed oncological disease); NVI's 2025 report states registration is now fully electronic after system integrations; ICD-O-3 for topography/morphology.
   https://nvi.lt/wp-content/uploads/2026/04/2-priedas.-NVI_Ataskaita_2025_26-02-26.pdf ; https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
4. **Terminologies:** SNOMED CT charter member 2007; NRC Lithuanian Library of Medicine (Ministry of Health); 40,000 concepts translated 2015. TLK-10-AM (ICD-10-AM) used since 2019 as interim; edition not found; TLK-11 mapping planned. LOINC and ICD-O-3 used in lab IG; ATC: not found; TNM edition: not found. Terminology server: https://tx.hl7.lt/fhir/ (HL7 Lithuania); national terminology server adaptation for TLK-11 planned.
   https://snomed.org/snomed-in-action/lithuanian-nrc-library-of-medicine ; https://e-seimas.lrs.lt/rs/legalact/TAD/e1ba28a055e911f0a19dcea0bcc863ad/ ; https://build.fhir.org/ig/HL7LT/ig-lt-lab/en/terminology.html
5. **Organisations and people:** Lithuanian Medical Library (IG publisher, SNOMED NRC), HL7 Lithuania (hl7.lt), Registrų centras (ESPBI), NVI. Named maintainers: not found.
