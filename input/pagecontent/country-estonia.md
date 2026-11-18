### Estonia (EE)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "Estonian Base Implementation Guide" (EEBase), package `ee.fhir.base` 2.0.0 (6 Nov 2025, trial-use; must-support removed), FHIR R5 (5.0.0), publisher HL7 Estonia, canonical https://fhir.ee/base, contact fhir@tehik.ee. Three-level profiling (international, Estonian base, system-specific); TIS resources also on fhir.tehik.ee.
   https://build.fhir.org/ig/HL7EE/ig-ee-base ; https://packages.fhir.org/ee.fhir.base
2. **Oncology FHIR specifications:** "VJL – Vähiandmete juhtimislaud" (cancer data dashboard), package `ee.fhir.vjl` 0.1.0, draft (2026-10-09), FHIR R5, publisher TEHIK, canonical https://fhir.ee/vjl; depends on ee.fhir.base 2.0.0, ee.fhir.mpi 1.5.0, ee.fhir.spd; no mCODE dependency; profile EEVJLCancerDiagnosis; project (Tartu University Hospital and partners) aims to automate submission to the cancer registry. Registry data standard implemented: not stated.
   https://build.fhir.org/ig/TEHIK-EE/ig-ee-vjl/ ; https://sisu.ut.ee/estcan/cancer-data-dashboard/
3. **Cancer registry reporting:** Estonian Cancer Registry (vähiregister), controller Tervise Arengu Instituut (TAI). Statutory cancer notification (vähiteatis) submitted on paper, electronically or via the X-Road data exchange layer; 2025 draft regulation sets 30-day deadline. ICD-O-3 for topography and morphology since 2008; ICD-10 for publication.
   https://www.riigiteataja.ee/akt/123052023056.pdf ; https://en.tai.ee/images/Teatise_vormistamise_juhend.pdf ; https://en.tai.ee/en/r-and-d/registers/estonian-cancer-registry
4. **Terminologies:** SNOMED CT member January 2010; NRC TEHIK; Estonian edition URI http://snomed.info/sct/11000181102. RHK-10 (Estonian ICD-10; version not found). LOINC Estonian linguistic variant (Estonian Society for Clinical Chemistry; UMLS lists v2.77, 2024-02-27). TNM, ATC: not found. National FHIR terminology server: Ontoserver hosted by TEHIK, in production, over 400 value sets plus SNOMED CT EE+INT, publishes under https://fhir.ee/; endpoint URL not found; described in ee.fhir.ts IG (draft 1.0.0).
   https://build.fhir.org/ig/TEHIK-EE/TerminologyServices ; https://www.snomed.org/members/estonia ; https://loinc.org/?p=7910
5. **Organisations and people:** TEHIK (fhir@tehik.ee, snomed@tehik.ee), HL7 Estonia (info@hl7.ee), TAI. Named IG maintainers: not found. Igor Bossenko (TalTech) publishes on Estonian CDA-to-FHIR migration; TEHIK role not confirmed.
   https://fhir.ee/base/contact.html
