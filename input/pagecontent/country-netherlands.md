### Netherlands (NL)

Region: DACH and Benelux. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **Base IG.** nl-core (FHIR R4 profiles for zib release 2020), package `nictiz.fhir.nl.r4.nl-core`, FHIR 4.0.1, publisher Nictiz, CC0. No non-beta release exists; latest 0.12.1-beta.1 (2026-08-25), 0.12.0-labtrial.1 (2025-12-12), 0.12.0-beta.4 (2025-09-30). Companion package `nictiz.fhir.nl.r4.zib2020`. Nictiz FHIR R4 IG 1.0.4. https://get-ig.org/nictiz.fhir.nl.r4.nl-core ; https://informatiestandaarden.nictiz.nl/wiki/FHIR:V1.0_FHIR_IG_R4
2. **Oncology.** IKNL "FHIR Implementatiegids voor de Nederlandse Kankerregistratie", package `iknl.fhir.nl.r4.ncr-ehr`, FHIR 4.0.1, latest 1.4.2, author Integraal Kankercentrum Nederland; CI build https://build.fhir.org/ig/IKNL/NkrIG/ ; source https://github.com/IKNL/NkrIG ; package https://get-ig.org/iknl.fhir.nl.r4.ncr-ehr . Depends on nl-core/zib2020 0.12.0-beta.4; the `hl7.fhir.us.mcode` dependency is commented out in sushi-config, so mCODE is not reused (https://build.fhir.org/ig/IKNL/NkrIG/branches/main/failure/sushi-config.yaml). Implements the NKR EHR submission dataset (nl-core Patient, EpisodeOfCare, Procedure, Problem, lab result linked to tumour). zib TNMTumorClassificatie v4.1 (2025-04-25) (https://www.zibs.nl/wiki/TNMTumorClassificatie-v4.1(2024NL)). PALGA FHIR specification: not found.
3. **Registry standard.** Nederlandse Kankerregistratie (NKR), run by IKNL since 1989; data collected by IKNL data managers from hospital records after signalling via PALGA and hospital registrations (DHD); automated nightly EHR extraction via the FHIR IG in 20 hospitals; 2024 figures about 125,000 partly manual and 60,000 fully automated records. No mandated XML format; per-diagnosis "NKR-itemset". Coding ICD-O-3 and UICC TNM 8th edition. https://iknl.nl/nkr ; https://iknl.nl/en/ncr ; https://www.oncologie.nu/nieuws/validatie-van-geautomatiseerde-realtime-gegevensuitwisseling-van-epds-naar-nkr/ ; https://richtlijnendatabase.nl/richtlijn/colorectaal_carcinoom_crc/pathologie_bij_crc/tnm_bij_crc.html
4. **Terminologies.** SNOMED CT charter member 2007, NRC Nictiz, monthly NL Edition (Nov 2025 release: 391,305 active concepts) (https://www.snomed.org/members/netherlands ; https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/353370340). ICD-10: Dutch translation by WHO-FIC Collaborating Centre at RIVM, latest book edition ICD-10 2021 (https://whofic.nl/downloads-en-links/icd-10). ICD-O-3 Dutch translation hosted by RIVM (https://www.rivm.nl/media/WHO-FIC/ICD-O-3.pdf). LOINC via Nederlandse Labcodeset, currently on LOINC 2.83 (2026-08-19) (https://labterminologie.nl/). National drug code: not found. Terminology server: Nationale Terminologieserver (NTS), Nictiz, Ontoserver, hosting SNOMED, LOINC, ICD-10, Labcodeset (https://ontoserver.csiro.au/site/nictiz-national-terminology-server/ ; https://www.nictiz.nl/document/beginnershandleiding-nationale-terminologieserver-nts-10-definitiefpdf).
5. **People.** IKNL NkrIG GitHub contributors jeroen-trompetter, basharmsen, Harmke Koning (https://github.com/IKNL/NkrIG). Nictiz nl-core maintainers by name: not found.

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Nederlandse Kankerregistratie (NKR), run by IKNL since 1989, nationwide; data collected by IKNL data managers from hospital records after notification via PALGA and DHD; about 125,000 partly manual and 60,000 fully automated records (2024). https://iknl.nl/nkr ; https://iknl.nl/getmedia/5e2b2905-4cf4-465c-985f-7eaa037febee/IKNL-Jaarverslag-2024.pdf
- ENCR membership: n/f in the contact-list pages retrieved; NKR contributes to ECIS. https://www.icthealth.org/news/ecis-update-improves-understanding-of-european-cancer-trends
- Pathology registry: PALGA (since 1991, all 64 pathology laboratories), 40–60 data applications per year. https://onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn/doi/abs/10.1155/2007/971816 ; https://iknl.nl/en/ncr/apply-for-data/data-linkage-iknl-palga
- Screening: Bevolkingsonderzoek Nederland runs the breast, cervical and colorectal programmes (screening IT "ScreenIT"): n/f.
- Legal basis: NKR operates on legal basis of scientific research and statistics in the public health interest (no individual consent). https://iknl.nl/nkr
- Submission format and dictionary: per-diagnosis NKR itemset; automated EHR extraction via IKNL FHIR IG (R(H)ONDA, 20 hospitals); linkage files in CSV or fixed-width ASCII; coding ICD-O-3 and UICC TNM 8; tumour-type file "RANK Bestandsindeling tumorsoort" 2025/2026. https://www.oncologie.nu/nieuws/validatie-van-geautomatiseerde-realtime-gegevensuitwisseling-van-epds-naar-nkr/ ; https://iknl.nl/getmedia/185b0869-edc9-4f5a-84b2-12d8716bc074/Instructie-aanvrager-format-koppeling.pdf ; https://iknl.nl/getmedia/b7276fdb-be51-4f1d-aa3a-e20311af8c4f/RANK-Bestandsindeling-tumorsoort-2025.pdf
- Data access: IKNL data request reviewed by privacy board (CvT) and scientific committee; turnaround 2 weeks (basic figures) to 4 months (complex/linkage with CBS, PALGA, cohorts). https://iknl.nl/en/NCR/Apply-for-data

#### (b) Public datasets
- Open statistics: NKR cijfers (1989–2024, 2023/2024 preliminary). https://iknl.nl/en/ncr/ncr-data-figures
- Synthetic dataset mimicking part of the NKR, free for researchers. https://iknl.nl/en/ncr/synthetic-dataset
- OMOP: NKR data available in OMOP CDM as EHDEN data partner, listed in EHDEN Data Catalogue. https://iknl.nl/en/news/ncr-data-in-omop-cdm
- Research data access bodies: CBS microdata (remote access, output checking); HDAB-NL (national Health Data Access Body) in preparation; Health-RI and IKNL MoU on research data availability; Health-RI coordinates EU project CANDLE on cancer data nodes. https://www.cbs.nl/en-gb/our-services/customised-services-microdata/microdata-conducting-your-own-research ; https://iknl.nl/getmedia/67eb1c67-8910-433b-b6df-6081b37a63eb/IKNL-Jaarplan-2025.pdf ; https://iknl.nl/en/news/iknl-ehds-en
- Screening data: n/f.

#### (c) Cancer infrastructure
- National plan: Nederlandse Kankeragenda (20 goals) by the Nederlands Kanker Collectief; NKC Hub is the national cancer mission hub in ECHoS. https://iknl.nl/en/news/echos-2
- OECI: NKI-AVL (Amsterdam) comprehensive cancer centre; Maastricht UMC+ CCC re-accredited with Research Excellence; Erasmus MC Cancer Institute and Radboudumc listed as OECI cancer centres; UMCG listed as CCC (secondary sources). https://www.maastrichtuniversity.nl/news/maastricht-umc-comprehensive-cancer-center-re-accredited-oeci-research-excellence-designation ; https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: Hartwig Medical Foundation (WGS database): access details n/f; 1+MG participation: n/f.
- Biobanks: BBMRI-NL: n/f in this survey.
- Imaging: EUCAIM Dutch partners: n/f.
- EU projects: CancerWatch (Sept 2025–Aug 2028, IKNL partner); ECHoS (NKC Hub); EUCanScreen (Ministry of VWS associated partner); TEHDAS2 (RIVM). https://www.icthealth.org/news/eu-launches-cancerwatch-for-better-and-faster-cancer-data ; https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://www.rivm.nl/en/international-projects/tehdas2
- Research data infrastructure: Health-RI (national health data infrastructure); Oncode Institute. https://iknl.nl/en/news/iknl-ehds-en

#### (d) Digital, non-FHIR, cancer-relevant
- Information standards: Informatiestandaard Mammacarcinoom (IKNL with NABON, ART-DECOR, zib 2017), Gegevensset Oncologie Algemeen plus tumour-specific datasets (Zorginstituut: >80% of colorectal dataset generic); uptake still low (Nictiz 2024). https://nictiz.nl/app/uploads/2024/08/ICThealth_nr4_2024_10-11.pdf ; https://wpn.nen.nl/app/uploads/sites/16/2024/09/Zorginstituut-Nederland-Sterk_datafundament_voor_kwaliteit_van_zorg-def.pdf
- zibs: TNMTumorClassificatie v4.1 (2025) and related oncology zibs on zibs.nl. https://www.zibs.nl/wiki/TNMTumorClassificatie-v4.1(2024NL)
- Regional oncology networks: IHE-NL guideline MDO (multidisciplinary consultation) 2021; OncoNext data re-use initiative. https://ihe-nl.org/wp-content/uploads/2022/07/IHE-Guideline-MDO-and-Addendum-2021-English-Final.pdf ; https://oncologie.nu/nieuws/onconext-de-volgende-stap-naar-betere-beschikbaarheid-en-hergebruik-van-medische-gegevens
- Pathology: PALGA protocol module (PPM) for synoptic reporting, national PALGA protocols approved by NVVP; PALGA codes aligned to SNOMED. https://richtlijnendatabase.nl/richtlijn/schildkliercarcinoom_2024/pathologie_bij_rl_schildkliercarcinoom/pathologie_-_protocollaire_verslaglegging_palga.html ; https://wiki.hl7.org/Pathology_Report-abstracts_Request_Use_Case_(Linda_Mook)
- Lab coding: Nederlandse Labcodeset (LOINC 2.83). https://labterminologie.nl/
- Palliative/advance care planning: IKNL PZP IG (STU3/R4). https://api.iknl.nl/docs/pzp/r4/1.0.0-rc2/index.html
- Patient portals, Oncoguide, chemotherapy ePrescription, openEHR: n/f.

#### Key organisations and people
- IKNL (NKR; NkrIG contributors jeroen-trompetter, basharmsen, Harmke Koning), PALGA, Nictiz (zibs, NTS, SNOMED NRC), Health-RI, Nederlands Kanker Collectief, RIVM (WHO-FIC, TEHDAS2), CBS, Bevolkingsonderzoek Nederland. https://github.com/IKNL/NkrIG ; https://iknl.nl/en/news/iknl-ehds-en

---
