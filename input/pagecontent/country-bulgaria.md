### Bulgaria (BG)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** none. NHIS (НЗИС, his.bg; Ministry of Health; integrator Information Services AD) exposes XML/XSD-based APIs (NHIS-C001 nomenclature request etc., NHIS-X003, Swagger at https://ptest-api.his.bg/index.html; e-prescription API v1.5.1, e-referral v1.4.4, e-hospitalisation v1.1.2); no FHIR mentioned. Governed by Ordinance H-6 of 21 Dec 2022.
   https://his.bg/bg/dev/specifications ; https://www.mh.government.bg/upload/3994/naredban-6-21-12-2022.pdf
2. **Oncology FHIR specifications:** none found. mCODE reuse: not found.
3. **Cancer registry reporting standard:** National Cancer Registry; draft amendment to Ordinance No. 6/2018 "Medical oncology" (public consultation 14 Nov–15 Dec 2025) restructures it as an "information database for persons with malignant neoplasms and carcinoma in situ" functioning as part of NHIS. Ministry of Health reports 302,450 malignant cases registered in NHIS as of 2025. Current submission format: not found.
   https://www.strategy.bg/bg/public-consultations/11919/export ; https://www.bta.bg/en/news/1057238-over-300-000-cancer-cases-registered-in-bulgaria-s-national-health-information-s
4. **Terminologies:** SNOMED CT: not a member. ICD-10 as NHIS nomenclature CL011 ("Заболяване по МКБ 10"), ICD-9 procedures as CL054; NHIS nomenclature spec v1.5.36 (3 Nov 2026). ICD-O-3/TNM: the Nov 2025 draft ordinance restructuring the cancer registry does not specify coding standards; a public comment (K. Kostadinov, 21 Nov 2025) explicitly requests ICD-O-3 and ICD-10 coding rules be added (verified 2026-11-19) https://www.strategy.bg/bg/public-consultations/11919/export ; NCPHA bulletins tabulate by МКБ-10 localisation https://ncpha.government.bg/uploads/magazines/bulletins/bul_onko_2020web.pdf . TNM edition, LOINC, ATC variant, terminology server: not found.
   https://his.bg/bg/dev/nomenclatures ; https://his.bg/bg/dev/specifications ; https://www.snomed.org/members
5. **Organisations and people:** Ministry of Health, Information Services AD (system integrator). HL7 Bulgaria affiliate: not found (not in hl7.eu affiliate index). Named maintainers: not found.
   https://his.bg/en/news/198

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Bulgarian National Cancer Registry (BNCR), started 1952, hosted at USHATO Sofia, fed by 13 regional complex oncology centres; coverage 100% (ECIS); contributes to IARC EUREG. https://view.pagetiger.com/CancerControl2014/issue1/page135.htm ; https://ghdx.healthdata.org/record/bulgaria-eureg-cancer-incidence-tables-rates-age
- Restructuring: draft amendment to Ordinance 6/2018 (consultation Nov–Dec 2025) makes the registry a database inside NHIS; new national oncology database (120+ indicators) administered by NCPHA, intended for EHDS and ECIS. https://www.strategy.bg/bg/public-consultations/11919/export ; https://fakti.bg/en/bulgaria/1052747-ministerstvoto-na-zdraveopazvaneto-sazdava-nacionalna-baza-danni-za-onkologichnite-zabolavania
- Status 2025/26: 302,450 malignant cases in NHIS; no official new-case data yet. https://www.bta.bg/en/news/1057238-over-300-000-cancer-cases-registered-in-bulgaria-s-national-health-information-s ; https://bntnews.bg/news/more-than-300000-bulgarians-are-battling-cancer-1377489news.html
- Submission format, researcher access: n/f. Variable dictionary: BNCR data-quality assessment (Dimitrova & Parkin 2015, Cancer Epidemiology 39(3)) checked topography/morphology coding; MV 87.4 percent (verified 2026-11-19) https://eld.bl.uk/catalog/100032457892_0x000001 ; the Nov 2025 draft ordinance does not specify coding standards and a public comment requests ICD-O-3/ICD-10 rules (verified 2026-11-19) https://www.strategy.bg/bg/public-consultations/11919/export ; TNM edition: n/f.

#### (b) Public datasets
- NCPHA bulletins "Registered diseases and deaths from malignant neoplasms 2005–2021". https://ncpha.government.bg/uploads/magazines/bulletins/bul_onko_2020web.pdf
- NHIS statistical reports section (2025). https://his.bg/en/info/roadmap
- ECIS: Bulgarian registry contributes. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Synthetic data: n/f. HDAB: no designation found (Nov 2026). TEHDAS2 partner: Ministry of Health. https://tehdas.eu/tehdas2/partners/

#### (c) Cancer infrastructure
- Plan: National Cancer Control Plan 2027 (RMS decision 3/2023, 9 Jan 2023); colorectal screening programme 2026–2027 draft; cervical and colorectal screening campaigns 2026–2030. https://www.strategy.bg/bg/strategy-documents/1588/export ; https://www.mh.government.bg/upload/19369/%D0%9D%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%BD%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B0%20%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3_%D0%A0%D0%94%D0%A7_07.05.2026.pdf
- OECI: no Bulgarian centre on the OECI certified-centres list as of 2026-11-19 (verified 2026-11-19) https://accreditation.oeci.eu/
- Genomics: 1+MG original signatory (2018); Genome of Bulgaria (MU Sofia, MU Plovdiv) within Genome of Europe; GDI national hub storage. https://nucbtr.mu-sofia.bg/en/news/genomat-na-balgaria ; https://www.bbmri-eric.eu/national-nodes/
- Biobank: BBMRI.bg (Molecular Medicine Center, MU Sofia; member since 2018; director Radka Kaneva). https://www.bbmri-eric.eu/national-nodes/
- Imaging/EUCAIM: none listed. EU projects: CraNE (USHATO), TEHDAS2 (MoH), ECHoS National Cancer Mission Hub (established 11 Mar 2026, BJCN-driven, СОНМ network); EUCanScreen: not listed. https://crane4health.eu/partners/ ; https://bjcn.bg/en/bncmh/
- OMOP: EHDEN partners Technical University of Sofia, SAT Health. https://www.ehden.eu/datapartners/
- Radiotherapy/diagnostic equipment for 14 hospitals under RRP. https://www.bta.bg/en/news/1057238-over-300-000-cancer-cases-registered-in-bulgaria-s-national-health-information-s

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: NHIS (his.bg), XML/XSD APIs (e-prescription, e-referral, e-examination, e-hospitalisation, nomenclatures), 2D barcode spec, pen-tablet e-signing; patient portal my.his.bg and eZdrave app; rare diseases module (Orphanet) and patient summary planned 2026. https://his.bg/bg/dev/specifications ; https://his.bg/en/info/roadmap
- Cancer in NHIS: cancer registry becomes NHIS functional component; high-cost medicinal product protocols module (2025). https://www.strategy.bg/bg/public-consultations/11919/export
- Structured pathology, tumour-board software, chemotherapy e-prescribing, openEHR: still n/f after Bulgarian-language search; National Cancer Plan flags lack of integrated oncology databases https://www.iccp-portal.org/system/files/plans/bg_national_cancer_plan_2030_-_site.pdf
- Strategy: National Cancer Control Plan 2027 digital goals (new technologies, innovation). https://www.iccp-portal.org/system/files/plans/23rh003pr.pdf

#### Key organisations and people
- Ministry of Health; NCPHA (new oncology database); USHATO (BNCR, CraNE); Information Services AD (NHIS); BJCN / National Cancer Mission Hub (Kostadin Kostadinov commented on registry draft); BBMRI.bg (Radka Kaneva). https://www.strategy.bg/bg/public-consultations/11919/export
