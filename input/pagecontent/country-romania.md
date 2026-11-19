### Romania (RO)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** none found. Simplifier jurisdiction page has no survey content. National Digitalisation in Health Strategy 2024-2030 names HL7 FHIR; DES (Dosarul electronic de sănătate) interface specifications for providers are hosted on portal.cnas.ro (access blocked, format unverified).
   https://api.simplifier.net/jurisdictions/RO ; https://audit.ms.ro/media/documents/v.1._Strategia_Nationala_de_Digitalizare_%C3%AEn_S%C4%83n%C4%83tate_pentru_Romania_Versiune__D4WP2R0.docx ; https://portal.cnas.ro/cnas/des/docs/specificatii/Specificatie%20Interfatare%20DES%20-%20Aplicatii_de_Raportare_pentru_Furnizori.pdf
2. **Oncology FHIR specifications:** none found. mCODE reuse: not found.
3. **Cancer registry reporting standard:** Registrul Național de Cancer (RNC) created by HG 663/2023, owned by INSP (CNSBNT and CNS); Art. 5(1) mandates the WHO ICD-O-3 (CIM-O-3) multi-axial classification of topography, morphology, behaviour and grade; reportable: in situ and malignant tumours except C44 basal cell carcinoma, plus all intracranial/intraspinal tumours C70–C72, C75.1–C75.3 (verified 2026-11-19) https://management-documente.ms.ro/media/documents/HG_-REGISTRUL_NATIONAL_DE_CANCER_-_25.07.2023_2okqVrf.docx ; single case report form and coding methodology to be approved by ministerial order; case report due within 30 days; operational status still not verified (INSP May 2026 communication lists registry development as an ongoing objective, https://agerpres.ro/sanatate/2026/05/26/insp-aproximativ-40-dintre-cazurile-de-cancer-pot-fi-prevenite-printr-un-stil-de-viata-sanatos--1560130).
   https://iob.ro/wp-content/uploads/2023/09/hotararea-nr-663-2023-privind-infiintarea-registrului-national-de-cancer.pdf ; https://management-documente.ms.ro/media/documents/HG_-REGISTRUL_NATIONAL_DE_CANCER_-_25.07.2023_2okqVrf.docx
4. **Terminologies:** SNOMED CT: not a member. ICD-10-AM (3rd ed., 2002) for DRG (RO.vi.DRG / RODRG); CIM-10 for diagnoses. ICD-O-3 mandated for the national cancer registry by HG 663/2023 Art. 5 (verified 2026-11-19) ; the Cluj regional registry applies ICD-O-3.2 inclusion rules (ENCR 2021 training) https://www.encr.eu/sites/default/files/meetings/Training_2021-05/ENCR2021-S1-Cancer%20Registration.pdf . TNM edition, LOINC, ATC variant, terminology server: not found.
   https://www.snomed.org/members ; https://www.hosptm.ro/files/drg/rodrgv1/ManualGrupare_RODRG_v1_Vol_1.pdf
5. **Organisations and people:** CNAS (DES/PIAS), INSP (RNC), Ministry of Health. HL7 Romania (founded Nov 2006, 21 members), chair Florica Moldoveanu (Politehnica University of Bucharest) per archived HL7 Europe affiliate page (verified 2026-11-19) http://web.archive.org/web/20251013212616id_/https://hl7.eu/affiliate_ro.html
   https://hl7.eu/affiliate_ro.html

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- National: Registrul Național de Cancer (RNC), HG 663/2023 (in force 4 Aug 2023), owned by INSP (CNSBNT, CNSSP); single reporting form by ministerial order; operational status still n/f (INSP May 2026 lists registry development as ongoing, https://agerpres.ro/sanatate/2026/05/26/insp-aproximativ-40-dintre-cazurile-de-cancer-pot-fi-prevenite-printr-un-stil-de-viata-sanatos--1560130). https://iob.ro/wp-content/uploads/2023/09/hotararea-nr-663-2023-privind-infiintarea-registrului-national-de-cancer.pdf
- Regional registries: created under Order 2027/2007; Cluj Regional Cancer Registry at IOCN (head Daniela Coza, ENCR member) publishing reports since 2008; Timișoara data used by ECIS estimates; national coverage not 100%. https://www.encr.eu/sites/default/files/meetings/Training_2021-05/ENCR2021-S1-Cancer%20Registration.pdf ; https://encr.eu/news/new-cancer-report-north-western-region-romania
- Paediatric: Romanian National Pediatric Oncology and Hematology Registry. https://www.frontiersin.org/journals/cancer-control-and-society/articles/10.3389/fcacs.2025.1546879/pdf
- Screening registries: draft HG (Nov 2025) for cervical, colorectal, breast screening registries at INSP. https://agerpres.ro/sanatate/2025/11/28/update-ministerul-sanatatii-anunta-registre-nationale-de-screening-rogobete-o-singura-baza-de-date-u--1507242
- Submission format and variable dictionary: electronic form and nominal registration application to be built by MoH/INSP (HG 663/2023 Art. 8); HG 663/2023 Art. 5(1) mandates WHO ICD-O-3 (CIM-O-3) for topography, morphology, behaviour and grade (verified 2026-11-19) https://management-documente.ms.ro/media/documents/HG_-REGISTRUL_NATIONAL_DE_CANCER_-_25.07.2023_2okqVrf.docx ; Cluj regional registry reports use ICD-O-3 morphology and ICD-O-3.2 inclusion rules https://iocn.ro/wp-content/uploads/2019/12/Cancerul_in_regiunea_nv_a_Romaniei_2010-2011.pdf ; TNM edition: n/f.
- Researcher access: n/f.

#### (b) Public datasets
- Open statistics portal: n/f; Cluj regional reports; national 2008–2017 dataset obtained from National School of Public Health. https://www.proquest.com/docview/2881871812
- ECIS: Romania in estimates (regional inputs). https://ecis.jrc.ec.europa.eu/pdf/Estimates_2022_methods.pdf
- Synthetic data: n/f. HDAB: no designation found (Romanian-language search, Nov 2026). TEHDAS2 partner: INMSS. https://tehdas.eu/tehdas2/partners/

#### (c) Cancer infrastructure
- Plan: Planul Național de Combatere a Cancerului (launched Jan 2022; Law 293/2022). https://www.romania-insider.com/society/ro-national-cancer-plan-jan-2022 ; https://www.anm.ro/_/LEGI%20ORDONANTE/Lege%20293-2022.pdf
- OECI: CORRECTED: IOCN Cluj received an OECI Clinical Cancer Centre certificate in 2017 (member since 2008), but no Romanian centre appears on the OECI certified-centres list as of 2026-11-19; a breast-unit directory gave the IOCN certificate expiry as 16 Nov 2022, so the accreditation is treated as lapsed (verified 2026-11-19) https://accreditation.oeci.eu/ ; https://www.breastcentresnetwork.org/breast-units/directory/Romania/%E2%80%9DProf.+Dr.+Ion+Chiricuta%E2%80%9D+Institute+of+Oncology/4,9,1765, ; Amethyst Radiotherapy listed as member. https://positivenewsromania.com/2017/11/25/cluj-cancer-centre-receives-european-recognition ; https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: 1+MG signatory and GDI member since April 2024 (Genomics R&D Institute, ADR; national network coordinated by UMF Carol Davila). https://agerpres.ro/educatie-stiinta/2024/05/27/mcid-romania-a-aderat-la-proiectul-european-pentru-infrastructura-de-date-genomice--1301941
- Biobank: not a BBMRI-ERIC member. https://www.bbmri-eric.eu/national-nodes/
- Imaging/EUCAIM: none listed. EU projects: CraNE (IOCN), EUCanScreen (INSP; Fundeni, IOCN; Iași RIO associated), CancerWatch (IOCN competent authority), TEHDAS2 (INMSS), ECHoS hub planned. https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/ ; https://iocn.ro/?p=4877
- OMOP: no EHDEN partner listed. https://www.ehden.eu/datapartners/

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: DES (Dosarul Electronic de Sănătate, CNAS) with HL7 CDA interface spec v1.0 (2014); eSănătateaMea platform from 1 Sep 2026; PIAS insurance platform. https://portal.cnas.ro/cnas/des/docs/specificatii/Specificatie%20Interfatare%20DES%20-%20Aplicatii_de_Raportare_pentru_Furnizori.pdf ; https://www.wall-street.ro/articol/sanatate/cnas-cere-actualizarea-aplicatiilor-medicale
- Integration of DES with RNC announced. https://www.stiripesurse.ro/integrarea-dosarului-electronic-cu-registrul-national-de-cancer_3881674
- Tumour boards: multidisciplinary tumour board practice reported at Amethyst radiotherapy centre Bucharest (press) https://adevarul.ro/stiri-interne/sanatate/tumor-board-abordarea-care-ofera-noi-sperante-1546906.html . Structured pathology, chemotherapy system, openEHR: n/f.
- Strategy: National Digitalisation in Health Strategy 2024–2030. https://audit.ms.ro/media/documents/v.1._Strategia_Nationala_de_Digitalizare_%C3%AEn_S%C4%83n%C4%83tate_pentru_Romania_Versiune__D4WP2R0.docx

#### Key organisations and people
- INSP (RNC); IOCN Cluj (Daniela Coza, regional registry); CNAS (DES); UMF Carol Davila (genomics); HL7 Romania (Florica Moldoveanu).

---
