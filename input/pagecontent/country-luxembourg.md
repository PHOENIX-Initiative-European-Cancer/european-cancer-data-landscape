### Luxembourg (LU)

Region: DACH and Benelux. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** Agence eSanté Luxembourg Simplifier organisation "esantelux" lists four guides (HPD, eResult, History API, ePrescription), all preview status, no packages (https://simplifier.net/organization/esantelux/~projects). The State of FHIR 2026 summary reports a national base IG "used in a limited set of cases", R4B/R5 in use, specifications drawing on HL7 Europe IGs and IHE profiles (https://packages.fhir.org/jurisdictions/LU). Package id/version of a base IG: not found.
2. **Oncology FHIR IG:** not found. mCODE: not found.
3. **Registry reporting:** RNC (Registre National du Cancer), established 2013 by the Direction de la santé, run by the Luxembourg Institute of Health (LIH); sources include LNS and hospital registries. Submission format, ICD-O and TNM rules: not found. Source: https://researchportal.lih.lu/en/projects/registre-national-du-cancer-national-cancer-regestry/
4. **Terminologies:** SNOMED CT member since May 2018, represented by Agence eSanté (https://globenewswire.com/news-release/2018/05/24/1511618/0/en/Luxembourg-Announced-as-SNOMED-International-s-Newest-Member.html); national edition: not found. Hospital coding (DCSH): ICD-10-CM diagnoses since 2016, ICD-10-PCS procedures, 2026 rules refer to the ICD-10-BE 2025 manual, APR-DRG grouping (https://santesecu.public.lu/dam-assets/fr/espace-professionnel/informations-et-donnees-de-sante/dcsh-ressources/modalits-de-codage-2026v05.pdf). ICD-O-3, LOINC variant, TNM edition: not found. Drug code: CNS positive list "numéro national" (https://cns.public.lu/en/legislations/textes-coordonnes/liste-positive-csv.html). Terminology server: in planning per State of FHIR 2026; an EBX-based eSanté terminology server was validated in 2016 (vendor source).
5. **Organisations and people:** Agence eSanté (https://www.esante.lu), LIH. RNC: Sophie Couffignal (operational director), Claudine Backes (scientific director), as of Oct 2023 (https://www.lih.lu/en/article/a-ten-year-milestone-the-national-cancer-registrys-decade-of-support-in-the-fight-against-cancer/). Agence eSanté FHIR lead: not found.

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Registre National du Cancer (RNC), hosted at Luxembourg Institute of Health (LIH, EPICAN group), covering residents and non-residents diagnosed or treated in Luxembourg; ENCR membership: n/f. https://researchportal.lih.lu/en/projects/registre-national-du-cancer-national-cancer-regestry/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12668946/
- Clinical registries, screening registries: organised breast (Programme Mammographie) and colorectal programmes run by the Direction de la santé, age lowered to 45 from 2024; LIH/EPICAN evaluates the mammography programme by linking RNC data. https://chronicle.lu/category/medical/59357-luxembourg-takes-action-to-improve-cancer-screening-and-prevention ; https://lih.lu/?p=42090
- Legal basis: n/f (règlement grand-ducal on RNC not retrieved).
- Submission format and dictionary: n/f.
- Data access: RNC data linkage scoping review (2025) names legal permission, data availability, data flow, linkage key and method as prerequisites; partners IBBL and IGSS. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12668946/

#### (b) Public datasets
- RNC reports (incidence and mortality 2014–2021, Nov 2025); OECD country cancer profile 2025. https://www.lih.lu/en/research-scope/research-department/department-of-precision-health/cancer-epidemiology-and-prevention-epican/
- Research data access: Luxembourg National Data Service (LNDS) (TEHDAS2 page); RNC is EHDEN data partner with planned OMOP conversion (2021 announcement). https://www.lnds.lu/?p=4771 ; https://www.researchluxembourg.org/en/luxembourg-to-speed-up-the-standardisation-of-clinical-data/ ; https://zenodo.org/records/6490069/files/EHDEN%20Year%203%20partner%20report_final.pdf
- ECIS contribution, synthetic datasets, catalogue: n/f.

#### (c) Cancer infrastructure
- National plan: Plan National Cancer 2 (PNC2, 2020–2026) with digitalisation priority; Institut National du Cancer (INC) created under PNC2 to coordinate cancer activities. https://chronicle.lu/category/medical/31407-luxembourg-approves-second-national-cancer-plan-based-on-digitalisation-innovation ; https://luxtoday.lu/fr/sant-et-environnement/oncologie-au-luxembourg-cancer-chez-les-jeunes-et-nouvelles-mesures-de-soutien-aux-patients
- CCCs/OECI: n/f.
- Genomics: LuxGen Genome Center (LIH); 1+MG: n/f.
- Biobanks: Integrated Biobank of Luxembourg (IBBL, LIH). https://www.lih.lu/en/news/page/6/
- EU projects: CancerWatch (LIH/RNC, Sept 2025–Aug 2028); Clinnova cross-border (LU, FR, DE, CH); Dataspace4Health oncology use case; EUCanScreen Luxembourg entry: n/f. https://www.lih.lu/wp-content/uploads/2025/09/CancerWatchPR_FR.pdf ; https://www.lih.lu/en/news/page/6/

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: Dossier de Soins Partagé (DSP, Agence eSanté); oncology content: n/f.
- Terminology, structured pathology, tumour-board software, openEHR: n/f.
- Digital strategy: PNC2 digitalisation axis incl. diagnosis-reporting tools (2025 actions). https://luxtoday.lu/fr/sant-et-environnement/oncologie-au-luxembourg-cancer-chez-les-jeunes-et-nouvelles-mesures-de-soutien-aux-patients

#### Key organisations and people
- LIH (RNC, EPICAN, IBBL, LuxGen), Direction de la santé / Ministère de la Santé (Martine Deprez, minister), Institut National du Cancer, LNDS, Agence eSanté, Laboratoire national de santé (LNS). https://www.lih.lu/en/research-scope/research-department/department-of-precision-health/cancer-epidemiology-and-prevention-epican/ ; https://www.lnds.lu/?p=4771

---

#### (a) Cancer registries
- RNC (Registre National du Cancer): population-based, established 2013 by Direction de la santé, managed by LIH; covers residents and non-residents treated in Luxembourg. https://researchportal.lih.lu/en/projects/registre-national-du-cancer-national-cancer-regestry/
- Sources: Laboratoire National de Santé and hospital cancer registries in the five hospitals (2013 launch). https://gouvernement.lu/dam-assets/fr/actualites/articles/2013/05-mai/15-dibartolomeo/cancer.pdf
- Legal basis: grand-ducal regulation on the RNC (2012 draft; Conseil d'État opinion). https://conseil-etat.public.lu/content/dam/conseil_etat/fr/avis/2012/12/49_987/49987_Texte.pdf
- Governance: multi-institutional management committee (OECD HSPA 2026). https://www.oecd.org/fr/publications/2026/03/health-system-performance-assessment-framework-for-luxembourg_8e0f4466/full-report/health-data-landscape-in-luxembourg-as-a-basis-for-the-hspa_015ca5f4.html
- Submission format, ICD-O/TNM editions, variable dictionary: n/f.
- ENCR/ECIS: RNC/LIH partner in CancerWatch (ECIS data quality). https://www.lih.lu/?p=46068
- Screening registries: Programme Mammographie (since 1992, extended 45-74 in 2024) and PDOCCR colorectal (permanent since 2021), Direction de la santé. https://gouvernement.lu/fr/actualites/toutes_actualites/communiques/2024/07-juillet/01-deprez-depistage-cancer.html
- Researcher access route: scoping review on RNC data linkage (Lima et al. 2025). https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1679408/full

#### (b) Public datasets
- RNC reports; latest RNC report released Feb 2026 by Ministry of Health. https://chronicle.lu/category/medical/59357-luxembourg-takes-action-to-improve-cancer-screening-and-prevention
- Mammography programme national evaluation report (Oct 2024, RNC + Programme Mammographie). https://santesecu.public.lu/dam-assets/fr/publications/r/rapport-programme-mammographie-2024/rapport-national-evaluation-du-programme-mammographie-vf.pdf
- Research data access: HDAB-LU project (LNDS, four years) preparing the future HDAB. https://www.lnds.lu/?p=4470
- Open data portal oncology datasets, synthetic data, national health data catalogue: n/f (HDAB-LU plans a health data catalogue).

#### (c) Cancer infrastructure
- Plan National Cancer 2020-2024, extended to 2026; priority digitalisation; INC (Institut National du Cancer) central to implementation. https://santesecu.public.lu/en/espace-professionnel/departement-sante/plans-nationaux/plan-national-cancer.html
- Genetics: Centre national de génétique humaine at LNS; MDLUX2 molecular diagnostics. https://thepathologist.com/diagnostics/mdlux2-drawing-a-fuller-picture
- Biobank: IBBL (Integrated BioBank of Luxembourg, LIH); Luxembourg not listed among BBMRI-ERIC national nodes (page checked 2026-11-18). https://www.bbmri-eric.eu/national-nodes/
- Genomics: 1+MG signatory; LNDS partner in B1MG; LNDS + LIH in Genome of Europe. https://www.lnds.lu/wp-content/uploads/2024/11/PR-Genome_of_Europe_Launch_web.pdf
- EHDEN/OMOP: RNC is the Luxembourg EHDEN data partner; LIH converting registry data to OMOP CDM. https://www.researchluxembourg.org/en/luxembourg-to-speed-up-the-standardisation-of-clinical-data/
- LIH DS4H white paper: oncology data model for colorectal and lung cancer, based on MII oncology model and OMOP (2025). https://www.lih.lu/wp-content/uploads/2025/06/DS4H_Technical-White-Paper.pdf
- EU projects: CAN.HEAL (LNDS partner, 2022-2024); CANDLE national cancer data nodes (LIH, 2025). https://chronicle.lu/category/medical/55746-lih-contributes-to-eu-project-aimed-at-improving-access-to-cancer-data
- EUCAIM Luxembourg partner: n/f. OECI centre: n/f. UNCAN.eu, canSERV, JANE, CraNE, ECHoS, EUCanScreen, TEHDAS2: n/f.

#### (d) Digital, non-FHIR
- DSP (dossier de soins partagé) on Agence eSanté platform; "DSP New Gen" aligned with EHDS planned; oncology content n/f. https://events.luxinnovation.lu/e/ehds-in-luxembourg
- Hospital coding DCSH: ICD-10-CM / ICD-10-PCS, 2026 rules use ICD-10-BE 2025 manual; APR-DRG. https://santesecu.public.lu/dam-assets/fr/espace-professionnel/informations-et-donnees-de-sante/dcsh-ressources/modalits-de-codage-2026v05.pdf
- Terminology: SNOMED CT member 2018; terminology server planned; LOINC/SNOMED/ICD-10 managed on an EBX-based server (2016 vendor case). https://www.casestudies.com/company/tibco-ebx/case-study/esante-luxembourg-customer-case-study
- Drug coding: CNS positive list "numéro national". https://cns.public.lu/en/legislations/textes-coordonnes/liste-positive-csv.html
- Tumour-board software, structured pathology, openEHR: n/f.

#### Key organisations and people
- Direction de la santé; INC; LIH (RNC: Sophie Couffignal operational director, Claudine Backes scientific director, Oct 2023). https://www.lih.lu/en/article/a-ten-year-milestone-the-national-cancer-registrys-decade-of-support-in-the-fight-against-cancer/
- LNDS (HDAB-LU, B1MG); LNS; IBBL; Agence eSanté; CNS.

---
