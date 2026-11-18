# Non-FHIR digital cancer landscape: United Kingdom, Ireland, Cyprus, Malta

Companion to islands-uk.md (FHIR survey). Researched 2026-11-18 for the ECCDM editors. One source URL per fact; "n/f" = not found in public sources; "not verified" = from search snippets only because the primary site (digital.nhs.uk, hse.ie, dhir.gov.mt) blocks automated fetches. Iceland was not in the earlier file and is not covered.

## United Kingdom

### (a) Cancer registries, audits, screening registries, legal basis, submission formats, data access

England
- Population registry: National Cancer Registration and Analysis Service (NCRAS) within the National Disease Registration Service (NDRS), NHS England; full coverage of England. https://digital.nhs.uk/services/data-services-for-commissioners/datasets/national-cancer-registries-and-analysis-service-ncras
- Legal basis: National Disease Registries Directions 2021 under s254(1) and s254(6) Health and Social Care Act 2012 (in force 1 Oct 2021; treated as Directions to NHS England since 1 Feb 2023); data provision under s259; previously PHE under s2B NHS Act 2006 and COPI Regulations 2002. https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/national-disease-register-service-directions
- Data provision notice for NDRS v4.0 (2026). https://digital.nhs.uk/binaries/content/assets/website-assets/corporate-information/directions-and-data-provision-notices/data-provision-notices/national-disease-registration-service/national-disease-registration-service-dpn-v4.0-final-20262209.pdf
- Submission formats (not verified): COSD dataset v10.2.0, user guide v10.2.12 (10.2.11 dated 2 Jun 2026), submitted monthly as XML against the COSD XML schema on TRUD, due by the 25th working day after month end; COSD Pathology v5.1.x; COSD v11 in development, no timeline. https://digital.nhs.uk/ndrs/data/data-sets/cosd
- SACT dataset v4.0 live 1 Apr 2026 (DCB1533 Amd 22/2025, conformance 1 Jul 2026; 16 new items, 4 compulsory; v3.0 retired 31 Mar 2026). https://standards.nhs.uk/published-standards/systemic-anticancer-therapy-data-set
- RTDS v6.0 (DAPB0111), restructured as episode, prescription, plan, attendance, exposure; monthly upload via API portal, 20 working days after month end; Wales adopts v6 in full. https://www.standards.nhs.uk/published-standards/radiotherapy-data-set
- Coding editions: ICD-O-3 for morphology/behaviour (revision n/f); TNM 8 from 1 Jan 2018 (RCPath table); ICD-10 5th edition; OPCS-4.11 from 1 Apr 2026. https://www.rcpath.org/asset/C9C6D872-0B0C-44C1-873F2FAD7853B385 ; https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dapb0084-opcs-classification-of-interventions-and-procedures
- Clinical audits: National Cancer Audit Collaborating Centre (NATCAN, HQIP-commissioned) runs ten audits for England and Wales: lung (NLCA), bowel (NBOCA), prostate (NPCA), oesophago-gastric (NOGCA), primary breast, metastatic breast, ovarian (NOCA), pancreatic, non-Hodgkin lymphoma, kidney; State of the Nation reports 2025; data via NDRS and DARS. https://www.natcan.org.uk/wp-content/uploads/2025/12/NATCAN-Annual-Report-2025_final.pdf
- Screening IT: National Breast Screening System (NBSS, Hitachi, VB6-era, contract extended 2025-2027, covers England, Wales, Isle of Man); cervical screening on CSMS; bowel screening on a single national BCSS; Richards review found screening IT "unsafe". https://htn.co.uk/2025/04/24/two-year-36-million-extension-for-national-breast-cancer-screening-system/ ; https://www.digitalhealth.net/?p=90311
- Researcher access: NHS England Data Access Request Service (DARS) for NDRS Cancer Consolidated Data Set or inside the NHS Secure Data Environment; NDRS Office for Data Release for HES/mortality linkage; NDRS Strategic Plan 2024-27 aims to expose all COSD items through DARS/SDE. https://digital.nhs.uk/ndrs/data/access-to-data ; https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/data-set-catalogue/ndrs-cancer-consolidated-data-set ; https://digital.nhs.uk/ndrs/about/ndrs-strategic-plan-2024---27
- NHS DigiTrials: trial recruitment service being expanded under the National Cancer Plan. https://www.kingsfund.org.uk/insight-and-analysis/long-reads/delivering-national-cancer-plan-innovation-ready-services
- UK Biobank: cancer registry linkage (England/Wales via NHS England, Scotland via NHSCR), linkage guide v2.0 Jul 2023. https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/CancerLinkage.pdf
- ENCR/IACR membership of UK registries: n/f (not checked).

Scotland
- Scottish Cancer Registry (SMR06), Public Health Scotland, managed by PHS/ISD since 1997, >1.8 million records; Scottish Cancer Registry and Intelligence Service (SCRIS) dashboards for NHS users. https://www.scotpho.org.uk/methods-and-data/overview-of-key-data-sources/scottish-national-data-schemes/cancer/ ; https://publichealthscotland.scot/population-health/conditions-and-diseases/cancer/scottish-cancer-registry-and-intelligence-service-scris/scris-updates/
- Coding: ICD-O and ICD-10; TNM (edition n/f), FIGO for gynae; ICD-10 5th edition (PHS ICD-10 Consolidation 2026); OPCS-4 in SMR returns. https://publichealthscotland.scot/publications/icd-10-consolidation-2026/ ; https://publichealthscotland.scot/resources-and-tools/health-intelligence-and-data-management/terminology-services-and-clinical-coding/clinical-coding-systems/clinical-classifications/opcs-4/html
- Audit: Cancer Quality Performance Indicators (QPIs) from the Scottish cancer networks, published via SCRIS. https://publichealthscotland.scot/population-health/conditions-and-diseases/cancer/scottish-cancer-registry-and-intelligence-service-scris/scris-for-researchers/publications-and-open-data/
- Screening IT: Scottish Breast Screening System (SBSS), Scottish Cervical Call Recall System (SCCRS, NSS), data to flow into a Cancer Intelligence Platform. https://www.nss.nhs.scot/specialist-healthcare/screening-programmes/cervical-screening/national-it-system-scottish-cervical-call-recall-system-sccrs/ ; https://www.gov.scot/publications/major-review-scottish-breast-screening-programme/pages/11/
- Legal basis: Care Reform (Scotland) Act 2025 powers to mandate information standards; registry-specific statute n/f. https://packages.fhir.org/jurisdictions/GB
- Researcher access: eDRIS (PHS) and Public Benefit and Privacy Panel (PBPP), analysis in the Scottish National Safe Haven; Research Data Scotland; Safe Haven Charter refreshed Mar 2025. https://publichealthscotland.scot/population-health/conditions-and-diseases/cancer/scottish-cancer-registry-and-intelligence-service-scris/scris-for-researchers/edris-and-pbpp-process/ ; https://www.researchdata.scot/researcher-access-service/explore-datasets-for-research/scottish-safe-haven-network/

Wales
- Welsh Cancer Intelligence and Surveillance Unit (WCISU, Public Health Wales), national registry; feeds from pathology, MDT, PEDW inpatient, radiology, radiotherapy, deaths, other UK registries. https://publichealthwales.nhs.wales/services-and-teams/welsh-cancer-intelligence-and-surveillance-unit-wcisu/
- National Cancer Data Standards for Wales DSCN 2019/09 (amended 17 Jul 2025), aligned with COSD v9.0; RTDS v6 adopted in full. https://dhcw.nhs.wales/data/information-standards/data-standards/data-standards-files/20250717-dscn-2019-09-nat-cancer-ds-core-banked-tissue-amd-docx-pdf/ ; https://www.datadictionary.wales.nhs.uk/WordDocuments/scope48.htm
- Coding: TNM 8 from 2018 for most sites; OPCS-4.11 from 1 Apr 2026 (DSCN 2026/08). https://phw.nhs.wales/knowledge-article/inequalities-in-cancer-incidence-in-wales-by-socio-demographic-characteristics-2011-2020-technical-guide/ ; https://dhcw.nhs.wales/data/information-standards/data-standards/data-standards-files/20260319-dscn-2026-08-opcs-4-11-v0-1-pdf/
- Audits: NATCAN audits cover Wales. https://www.sciencedirect.com/science/article/abs/pii/S147020452400665X
- Researcher access: SAIL Databank (Swansea), WCISU data linked to Census and health data; ADR UK projects. https://www.adruk.org/our-work/our-funded-projects/projects/project/cancer-data-driven-detection-exploring-cancer-inequalities-in-wales/ ; https://healthdatagateway.org/dataset/357

Northern Ireland
- Northern Ireland Cancer Registry (NICR), Queen's University Belfast, funded by the Public Health Agency; notifications from four pathology labs, HSC systems, GRO deaths; data from 1993. https://www.qub.ac.uk/research-centres/nicr/FileStore/OfficialStatistics1993-2022/July2025release/Methodology%20report.pdf
- Coding: ICD-O-3 from 2019 (ICD-O-2 before), TNM 7 before 2018 and TNM 8 from 2018. https://www.qub.ac.uk/research-centres/nicr/FileStore/OfficialStatistics1993-2022/July2025release/Liver%20cancer%20report.pdf
- Researcher access: NICR research access policy (ethics, charging) and linkage via the Honest Broker Service (HSC Business Services Organisation, NI secure data environment) and NI Biobank. https://bso.hscni.net/directorates/digital/honest-broker-service/ ; https://www.qub.ac.uk/research-centres/nicr/FileStore/PDF/Filetoupload,914885,en.pdf
- NI Biobank (QUB and Belfast Trust, est. 2010-11, HTA-licensed, 2026-2031 approval, linked to NICR). https://www.hra.nhs.uk/planning-and-improving-research/application-summaries/research-summaries/the-northern-ireland-biobank-nib-2026-2031/
- Screening IT and legal basis: n/f.

### (b) Public datasets and open statistics
- NDRS Cancer Data Hub: survival dashboards (31 cancers, 1 to 5 year), prevalence, Get Data Out anonymised tumour-level tables, outputs catalogue. https://digital.nhs.uk/ndrs/data/data-outputs/cancer-data-hub/cancer-survival ; https://digital.nhs.uk/ndrs/data/data-outputs/cancer-data-hub/get-data-out
- Cancer registration statistics, England (annual, NHS England) and ONS cancer survival rates on data.gov.uk. https://digital.nhs.uk/data-and-information/publications/statistical/cancer-registration-statistics/england-2023/links-to-related-statistics ; https://www.data.gov.uk/dataset/cancer_survival_rates
- Simulacrum synthetic NDRS data: v1.2.0 (2013-2017, 2.2m patients) and v2.1.0 (Apr 2023; 2016-2019, 1.87m patients; adds RTDS and genomic testing), Health Data Insight CiC with AstraZeneca and IQVIA; no v3 found. https://simulacrum.healthdatainsight.org.uk/available-data/
- HDR UK Innovation Gateway cancer collection (NCRAS dataset entry, NATCAN audits in the Research SDE Network). https://healthdatagateway.org/collectioncategories/cancer ; https://healthdatagateway.org/en/data-custodian-network/3
- DATA-CAN, the HDR UK health data research hub for cancer, hosted by Leeds Teaching Hospitals, all four nations; Arcturis partnership Feb 2025. https://www.arcturisdata.com/media/data-can-and-arcturis-enter-oncology-health-data-partnership-agreement/
- Scotland: PHS cancer publications and open data, ScotPHO cancer pages, opendata.nhs.scot cancer mortality. https://publichealthscotland.scot/population-health/conditions-and-diseases/cancer/scottish-cancer-registry-and-intelligence-service-scris/scris-for-researchers/publications-and-open-data/ ; https://www.opendata.nhs.scot/dataset/cancer-mortality
- Wales: WCISU Cancer Reporting Tool and official statistics tables. https://phw.nhs.wales/services-and-teams/welsh-cancer-intelligence-and-surveillance-unit-wcisu/cancer-reporting-tool/official-statistics-data-tables/cancer-reporting-tool-technical-guide-docx/
- Northern Ireland: NICR official statistics 1993-2022 (July 2025 release), also on data.gov.uk. https://www.qub.ac.uk/research-centres/nicr/CancerInformation/official-statistics ; https://ckan.publishing.service.gov.uk/dataset/activity/northern_ireland_annual_cancer_incidence_and_survival_statistics
- ECIS contribution by UK registries: n/f (UK not in the EU27 estimates).
- Cancer Research UK statistics portal: n/f in this search (not verified).

### (c) Cancer infrastructure
- National Cancer Plan for England 2026-2035, published Feb 2026 (goal: 3 in 4 survive 5 years by 2035; Cancer Alliances strengthened, £200m in 2026/27). https://www.gov.uk/government/publications/national-cancer-plan-for-england/the-national-cancer-plan-for-england-delivering-world-class-cancer-care-accessible-version
- Scotland: Cancer Strategy 2023-2033 and Cancer Action Plan 2023-2026 (136 actions), Scottish Cancer Strategic Board. https://www.gov.scot/publications/cancer-strategy-scotland-2023-2033/pages/1/ ; https://gov.scot/isbn/9781805255451
- Wales: Cancer Improvement Plan for NHS Wales 2023-2026; Wales Cancer Network. https://performanceandimprovement.nhs.wales/our-work/cancer/cancer-improvement-plan-docs/full-plan/
- Northern Ireland: Cancer Strategy for Northern Ireland 2022-2032 (launched 22 Mar 2022); DoH "Cancer Data: Moving Forward" proposes an HSC Data Institute and DATA-CAN-based real-time data network. https://www.health-ni.gov.uk/publications/cancer-strategy-northern-ireland-2022-2032 ; https://www.health-ni.gov.uk/sites/default/files/publications/health/doh-cancer-data-moving-forward.PDF
- OECI accreditation: The Christie (first UK comprehensive cancer centre, re-accredited to Jul 2030); Cambridge (CUH/CRUK Cambridge Cancer Centre, OECI accredited Mar 2020). Royal Marsden, Leeds, Oxford: n/f. https://christie.nhs.uk/about-us/news-at-the-christie/latest-news-stories/the-christie-receives-re-accreditation-from-the-organisation-of-european-cancer-institutes ; https://www.cuh.nhs.uk/our-services/cancer-services/about-cancer-services/accreditation-and-certification/organisation-of-european-cancer-institutes-accreditation/
- Genomics: NHS Genomic Medicine Service (launched Oct 2018; WGS service and seven GMS Alliances from 2020; National Genomic Test Directory with >200 cancer indications); Genomics England National Genomic Research Library (>110,000 genomes; 13,880 solid tumours in the 100,000 Genomes cancer cohort) accessed via the Research Environment. https://www.genomicsengland.co.uk/news/ngrl-grows-to-110000-genomes ; https://www.genomicsengland.co.uk/news/landmark-national-study-supports-use-of-whole-genome-sequencing-in-standard-cancer-care ; https://www.rcpath.org/discover-pathology/news/a-call-for-collaboration-in-shaping-the-future-of-genomic-cancer-diagnostics.html
- Genome UK 2022-2025 plan: £26m Cancer 2.0 programme (Genomics England, NHS England, NPIC). https://www.gov.uk/government/publications/genome-uk-2022-to-2025-implementation-plan-for-england/genome-uk-2022-to-2025-implementation-plan-for-england
- Scotland: Genomic Medicine Strategy 2024-2029; Scottish Strategic Network for Genomic Medicine funded 11 cancer genomic pathways (Apr 2023); SG-TAG Cancer advisory group; Scottish Genomes Partnership research programme ended Feb 2020. https://www.gov.scot/publications/scotlands-genomic-medicine-strategy-2024-2029/pages/6 ; https://www.genomics.nhs.scot/wp-content/uploads/2024-2025-SSNGM-Annual-Report-v1.0.pdf
- Wales: All Wales Medical Genomics Service; Genomics Delivery Plan for Wales 2026-2029 (draft, cancer genomics first pillar); Wales Cancer Biobank (20 years, 184 projects, WCB Digital links to AWMGS). https://genomicspartnership.wales/wp-content/uploads/2025/11/Genomics-Delivery-Plan-for-Wales-2026-2029-DRAFT-ENG.pdf ; https://walescancerbank.com/wp-content/uploads/2025/11/Wales-Cancer-Biobank-Autumn-Newsletter-2025-1.pdf
- Biobanks: UK Biobank (cancer linkage above); UKCRC Tissue Directory, BBMRI-ERIC UK status: n/f.
- Imaging: NCIMI (Oxford, Innovate UK, multi-modality imaging datasets, HDR UK Alliance member); National Pathology Imaging Co-operative (NPIC, Leeds, >30 hospitals, London trusts live Aug 2025, AI tool register Feb 2025); NHS England National Imaging Registry listed as upcoming FHIR project. https://gtr.ukri.org/project/ECAF67E0-65D2-464D-85E2-08AFDF76C978 ; https://npic.ac.uk/2025/08/18/three-leading-london-nhs-trusts-go-live-on-npic-digital-pathology-network-pioneering-digital-collaboration-across-england/
- EU projects: EOSC4Cancer partners University of Manchester (eScience Lab) and Instruct-ERIC (UK), funded via the UKRI Horizon Europe guarantee. https://esciencelab.org.uk/projects/eosc4cancer/ EUCAIM, UNCAN.eu, canSERV, JANE-2, CraNE, ECHoS, EUnetCCC, EUCanScreen, TEHDAS2 UK participation: n/f (EU4Health joint actions are not open to the UK).
- OMOP CDM: 17 to 22 EHDEN UK data partners; University of Edinburgh cancer data group is an EHDEN partner focused on the OMOP Oncology Module; CPRD prostate cancer OMOP dataset linked to cancer registry; London SDE/AI Centre OMOP federated cancer platform (GSTT, KCH, 20+ cancers). https://www.hdruk.ac.uk/news/call-for-uk-data-custodians-to-map-health-data-for-global-benefit/ ; https://cancer-data.ecrc.ed.ac.uk/?p=2707 ; https://ukhealthdata.org/wp-content/uploads/2025/09/ohdsi-2025-poster-pipeline.pdf
- National data spaces: NHS Federated Data Platform (Cancer 360 and shared patient tracking list products); NHS Research Secure Data Environment Network (national plus sub-national SDEs). https://www.mkuh.nhs.uk/wp-content/uploads/2025/06/Federated-data-platform-FDP-Response-952-FDP-Stakeholder-Engagement-Pack-BLMK.pdf ; https://healthdatagateway.org/en/data-custodian-network/3

### (d) Other digital, non-FHIR, cancer-relevant items
- National datasets not in FHIR: COSD (XML), SACT v4.0, RTDS v6.0, Cancer Waiting Times (version n/f), National Cancer Patient Experience Survey (Picker, since 2010, revised 2021), cancer PROMs (EQ-5D based pilots; PROMs used routinely in 18% of trusts). https://standards.nhs.uk/published-standards/national-cancer-patient-experience-survey ; https://www.hqip.org.uk/wp-content/uploads/2026/03/PROMs-Feasibility-Study-Final.pdf
- MDT and pathway software: Civica Clinical Pathways (formerly InfoFlex, 130+ trusts) and Somerset Cancer Register, used for MDT recording and cancer tracking. https://www.civica.com/en-us/product-pages/clinical-pathways-software/ ; https://www.somersetft.nhs.uk/somerset-cancer-register/wp-content/uploads/sites/37/2021/01/Cancer-follow-up-Digital-RMS-guide-V1.0-Jan21.pdf
- Chemotherapy e-prescribing (ChemoCare, Aria, iQemo market shares): n/f.
- Structured pathology: RCPath cancer datasets (ICCR-aligned); England requires 95% of reports to contain structured data; Genomics England synoptic pathology dataset. https://www.rcpath.org/profession/guidelines/cancer-datasets-and-tissue-pathways.html ; https://re-docs.genomicsengland.co.uk/synoptic/
- Pathology messaging: SNOMED CT Unified Test List under the Pathology Test and Results Standard; Read PBCL withdrawn. https://standards.nhs.uk/published-standards/pathology-test-and-results-standard
- Wales: CaNISC decommissioned 2025, replaced by the Cancer Informatics Solution (electronic cancer care record and outcomes repository, surfaced in Welsh Clinical Portal; electronic cancer forms live Jan 2025). https://www.gov.wales/sites/default/files/publications/2026-03/public-accountability-meeting-evidence-from-digital-health-and-care-wales.pdf
- Northern Ireland: encompass (Epic) single care record across all five HSC Trusts (May 2025); Rhapsody integration engine; oncology module details n/f. https://www.health-ni.gov.uk/news/digital-revolution-ni-patient-records
- Scotland: national chemotherapy e-prescribing system n/f; SCRIS dashboards as above.
- openEHR oncology archetypes in UK use: n/f.
- Document/exchange formats: HL7 v2 and ITK historically for pathology (UK Core predecessor CareConnect STU3 deprecated 19 Sep 2023). https://simplifier.net/organization/hl7uk/news

### Key organisations and people (UK)
- NDRS/NCRAS (NHS England): COSD, SACT, RTDS teams; named leads n/f. NATCAN: Healthcare Quality Improvement Partnership. DATA-CAN: Leeds Teaching Hospitals, Prof Mark Lawler (QUB, DATA-CAN scientific lead, AICRI co-lead). https://hecate.qub.ac.uk/home/News/Allnews/2025/island-ireland-punches-above-weight-cancer-research.html
- Scotland: Prof David Morrison, Director Scottish Cancer Registry (PHS); NSS SNOMED CT team (nss.snomed@nhs.scot). Wales: WCISU (Public Health Wales), Data Standards Wales (DHCW). NI: Dr Damien Bennett, NICR director; Prof Manuel Salto-Tellez, Precision Medicine Centre QUB.
- Genomics: Genomics England; NHS England Genomics Unit. Imaging: NPIC (Leeds), NCIMI (Oxford).

## Ireland

### (a) Cancer registries, audits, screening, legal basis, submission, access
- National Cancer Registry Ireland (NCRI), statutory registry (established 1991, nationwide from 1994), Republic of Ireland; reports to IARC and ECIS. https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri
- Submission: electronic feeds from histopathology labs (monthly/quarterly, SNOMED-coded, converted to ICD-O), radiotherapy units, HIPE (quarterly), CSO deaths; ~90% of tumours created electronically; registered by Cancer Data Registrars in the Cancer Registration System; NCRI Data Dictionary v2.0 (2023). https://www.ncri.ie/en/media/145/download
- Coding: ICD-O-3.2 from 2020; UICC TNM 7th from 2014 (HIQA profile; TNM 8 not confirmed); ACHI 6th for treatments; reporting in ICD-10. https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri
- Clinical audits: n/f (NCCP KPIs exist but no national audit programme found).
- Screening registries: National Screening Service (HSE, since 1 Jan 2014) runs BreastCheck (register from Department of Social Protection), CervicalCheck, BowelScreen (population register age 59-70, awaiting IHI field); HIQA catalogues them as national collections. https://www.hiqa.ie/areas-we-work/health-information/data-collections/breastcheck-national-breast-screening-programme ; https://www.hiqa.ie/areas-we-work/health-information/data-collections/bowelscreen-national-bowel-screening-programme
- Legal basis: Health Research Regulations 2018 (consent declaration committee) govern research use; Health Information Bill pending; EHDS applies from 2029. https://www.cso.ie/en/aboutus/lgdp/csodatapolicies/dataforresearchers/healthresearchdatacentrerdc/faq/ ; https://packages.fhir.org/jurisdictions/IE
- Researcher access: NCRI data access page and open data portal; NCRI and Aridhia Secure Data Environment for pseudonymised clinical and genomic data; CSO Health Research Data Centre (remote secure access); HRB DASSL model (trusted third party, virtual safe haven). https://aridhia.com/blog/national-cancer-registry-ireland-aridhia-announce-partnership-to-deliver-a-secure-data-environment/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9351012/
- ENCR membership: NCRI is an ENCR member (ENCR data protocol 2026). https://www.encr.eu/sites/default/files/Data_call/ECIS-data-protocol_2026.pdf

### (b) Public datasets and open statistics
- NCRI annual statistical report (Cancer in Ireland 1994-2022, 2024; 2026 report), online incidence and survival statistics, open data portal (eGovernment award shortlist). https://www.ncri.ie/node/346 ; https://www.ncri.ie/en/news/news-from-ncri/ncri-shortlisted-for-egovernment-award-in-open-data-category
- HIQA national data collections catalogue (NCRI, HIPE, screening). https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri
- HIPE annual activity reports (Healthcare Pricing Office; ICD-10-AM 12th edition from 2024). https://www.drugsandalcohol.ie/47018/1/HIPE_2025_Activity_in_Acute_Public_Hospitals_.pdf
- Catalogue of Irish health data resources for primary care cancer research (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12408799/
- ECIS: NCRI data in ECIS (Ireland in EU27 estimates). https://ecis.jrc.ec.europa.eu/sites/default/files/2026-04/ECIS_methods_EU27_updated_final_28042026.pdf
- Synthetic datasets: n/f.

### (c) Cancer infrastructure
- National Cancer Strategy 2017-2026, delivered by the HSE National Cancer Control Programme (NCCP). https://ehealthireland.ie/ehealth-functions/acute-delivery/national-cancer-information-system
- OECI: Trinity St James's Cancer Institute accredited 2019, Comprehensive Cancer Centre 2025 (first in Ireland); Beaumont RCSI Cancer Centre accredited 2023; CUH/UCC Cancer Centre accredited May 2025; HSE West and North West cancer network accredited Jul 2025. https://www.tcd.ie/news_events/articles/2025/prestigious-comprehensive-cancer-centre-status-for-tsjci/ ; https://www.hse.ie/eng/about/our-health-service/making-it-better/hse-west-and-north-west-cancer-network-receives-oeci-cancer-centre-certificate-of-accreditation.html
- Genomics: National Strategy for Accelerating Genetic and Genomic Medicine in Ireland (HSE, Dec 2022; implementation plan 2023; national office for genetics and genomics); NCCP Genomics Test Directory for Cancer (Jul 2024). https://www.hse.ie/eng/about/who/strategic-programmes-office-overview/national-strategy-for-accelerating-genetic-and-genomic-medicine-in-ireland/national-strategy-for-accelerating-genetic-and-genomic-medicine-in-ireland.pdf ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12272048/
- Biobanks: BBMRI-ERIC Irish node: n/f. Cancer Trials Ireland: n/f in this search.
- All-island: eHealth Hub for Cancer (QUB and University of Limerick); All-Island Cancer Research Institute (AICRI, UCD and QUB); 2025 all-island cancer research landscape report; "Harnessing Cancer Data for Better Health" seven-point roadmap endorsed at the All-Island Cancer Data Forum 2026 (Belfast), with a proposed All-Island Cancer Data Innovation Co-Centre. https://www.health-ni.gov.uk/news/cancer-leaders-launch-new-plans-build-all-island-digital-cancer-research-powerhouse ; https://t4test.ucd.ie/research/news/2025/all-islandcancerresearchlandscapereport2025/
- EU projects: EUCanScreen (Department of Health, RCSI, HSE National Screening Service). https://www2.healthservice.hse.ie/organisation/nss/news/one-year-of-eucanscreen-working-together-to-strengthen-cancer-screening-across-europe/ EUnetCCC, JANE-2, EUCAIM, canSERV, ECHoS, TEHDAS2: n/f.
- OMOP CDM: Trinity St James's Cancer Institute is an EHDEN data partner (fifth call, first Irish partner). https://www.ehden.eu/?p=4179
- National data space: HSE National Shared Care Record (deploying); HSE One Health Record national EHR procurement approved Feb 2026 (market consultation Jun 2025). https://about.hse.ie/news/procurement-launched-for-hse-one-health-record/ ; https://www.digitalhealth.net/2026/02/ireland-to-begin-procurement-for-a-national-electronic-health-record/

### (d) Other digital, non-FHIR, cancer-relevant items
- National Cancer Information System (NCIS): national electronic record for cancer diagnosis, SACT prescribing/preparation/administration and MDT decisions; BD Cato, Celsius37 TumorBoard and CancerCenter, Orchestra messaging; first site 2019, 26 SACT hospitals planned; underpinned by NCCP national SACT regimen library. https://ehealthireland.ie/ehealth-functions/acute-delivery/national-cancer-information-system ; https://www.saolta.ie/news/new-innovative-information-system-cancer-treatment-implemented-uhg
- HSE Health App (Feb 2025: appointments, referrals, vaccinations; no cancer feature found). https://www.digitalhealth.net/2026/02/ireland-to-begin-procurement-for-a-national-electronic-health-record/
- MyHealth@EU national contact point run by HSE. https://ehealthireland.ie/technology-and-transformation-functions/standards-and-shared-care-records-sscr/myhealth-eu/my-health-eu-team
- Standards policy: HIQA messaging standards guidance and terminology guidance (SNOMED CT, LOINC); Data for Care webinar (Mar 2026) names FHIR, SNOMED CT, LOINC, ICD-10-AM. https://www.hiqa.ie/ga/node/45505 ; https://about.hse.ie/news/data-for-care-webinar-highlights-progress-on-standards-interoperability-and-health-information-legislation/
- Structured pathology reporting, PROMs programme, openEHR oncology, tumour-board software beyond NCIS: n/f.

### Key organisations and people (Ireland)
- NCRI: Dr Theresa Redaniel, acting director (2026); board chair Dr Paul Kavanagh (chair designate). https://ncri.ie/en/news/news-from-ncri/dr-paul-kavanagh-appointed-chair-designate-of-the-national-cancer-registry
- HSE NCCP (NCIS owner); HSE Technology and Transformation (Theresa Barry, terminology; Patrick Marren, MyHealth@EU). HIQA (standards). HRB (DASSL). AICRI co-leads Prof William Gallagher (UCD) and Prof Mark Lawler (QUB). TSJCI (OECI CCC). EHDEN partner: TSJCI.

## Cyprus

### (a) Cancer registries, audits, screening, legal basis, submission, access
- Cyprus Cancer Registry (CyCR), Health Monitoring Unit, Ministry of Health; population-based (est. 1996-1998 with MECC/NCI support); member of IACR and ENCR; codes hospital notifications from all public and private hospitals using MECC/NCI coding: ICD-O-3, ICD-10, SEER Summary Staging, TNM (edition n/f). https://pmc.ncbi.nlm.nih.gov/articles/PMC11168067/
- ECIS: CyCR supplies incidence 1998-2022 and mortality 2004-2020 (updated Sep 2025); non-malignant CNS tumours under-recorded. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Submission format, legal basis, clinical audits, screening registry IT, researcher access route: n/f (registry data supplied pseudonymised to academic studies on request).
- Screening: breast screening expanded; national colorectal programme in final implementation stage (2025 profile); cervical screening opportunistic (2023 profile). https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-cyprus-2025_9133d835/c5a3f19e-en.pdf

### (b) Public datasets and open statistics
- Health Monitoring Unit figures (about 4,260 new cases and 1,600 deaths a year) released via press; no open data portal found. https://www.cna.org.cy/en/article/9778948/cyprus-records-4-260-new-cancer-cases-and-1-600-deaths-annually
- EU Country Cancer Profile Cyprus 2025 (OECD/ECIR). https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-cyprus-2025_9133d835/c5a3f19e-en.pdf
- Historical progress reports (2008-2010) on GHDx. https://ghdx.healthdata.org/print/114511
- Health data access body, national health data catalogue, synthetic data: n/f.

### (c) Cancer infrastructure
- National cancer strategy: first 2009, revised 2019 to EU guidelines and aligned with Europe's Beating Cancer Plan. https://www.iccp-portal.org/system/files/plans/Cyprus_National_Strategy_on_Cancer_English.pdf ; https://ecanplus.eu/downloads/eCANPlus_WP4_Policy_Mapping_Country_Factsheet_CY_updated_reviewed_final.pdf
- National Cancer Institute: bill approved Mar 2026, first board appointed, directors approved Sep 2026; remit includes updating the national strategy. https://cyprus-mail.com/2026/03/11/cyprus-to-create-national-cancer-institute ; https://cyprus-mail.com/2026/09/10/ministers-approve-directors-of-cyprus-first-national-cancer-institute
- Cancer centres: Bank of Cyprus Oncology Centre (BOCOC, not-for-profit, since 1998, OECI member listing for Cyprus); German Oncology Center (Limassol, trial site, contracted to GeSY); plans to unify oncology services of Nicosia and Limassol general hospitals with BOCOC. https://oeci.eu/IstitutesCountry.aspx?id=42 ; https://www.bococ.org.cy/en/about-us ; https://cyprusprofile.com/articles/german-oncology-centre-join-gesy
- Biobank: biobank.cy Centre of Excellence (University of Cyprus, CY-Biobank 2019-2026, EU grant 857122, target 16,500 participants by 2027, BBMRI-ERIC national node; partners include BOCOC); CING biobank (since 2012). https://www.bbmri-eric.eu/national-nodes/cyprus/ ; https://www.nature.com/articles/s41598-024-78644-4
- Genomics: Cyprus Human Genome Project (biobank.cy); national genomics strategy n/f. https://biobank.cy/portfolio/cy-biobank_factsheet/
- EU projects: EUnetCCC sustainability session hosted at BOCOC 29 Apr 2026; eCAN joint action telerehabilitation trial site; Xt-EHR Joint Action (NeHA). https://www.europeancancer.org/events/421:securing-a-lasting-impact.html ; https://clinicaltrials.gov/study/NCT06007001 EUCAIM, JANE-2, canSERV, ECHoS, EUCanScreen: n/f.
- OMOP/EHDEN data partners in Cyprus: n/f. Imaging infrastructure: n/f.
- National data space: NeHA designated Digital Health Authority (EHDS Art. 19); national EHR tender expected end 2025, development from late 2026. https://www.interregeurope.eu/good-practices/national-ehealth-authority-neha

### (d) Other digital, non-FHIR, cancer-relevant items
- GeSY integrated information system (HIO) with beneficiary and provider portals; hospital HIS in Nicosia and Famagusta general hospitals since 2007; provider systems historically on the proprietary DASTA standard. https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/cyprus2025/organization-and-governance/health-information-systems ; https://www.xt-ehr.eu/wp-content/uploads/2026/05/Xt-EHR-D4.1.pdf
- myHealth@CY citizen app contracted Nov 2025 (NeHA, Cyta, HIO), to connect to GeSY and grow into a full EHR. https://cyprus-mail.com/2025/11/25/new-app-to-offer-access-to-health-data
- Coding environment: ICD-10, LOINC, ICPC, CPT-4 for reimbursement, free text; SNOMED CT mapping planned. https://www.snomed.org/snomed-in-action/national-ehealth-authority-of-cyprus
- MyHealth@EU: NeHA patient summary guideline; cross-border services launched with Greece (Interreg HUMAN). https://www.neha.org.cy/wp-content/uploads/2023/03/guidelines_PatientSummary.pdf ; https://www.interregeurope.eu/human/news-and-events/news/cyprus-greece-launch-cross-border-digital-health-services
- eHealth4U prototype national EHR (FHIR R4, SNOMED CT, LOINC; IPS-based). https://doi.org/10.1177/20552076261431813
- Tumour-board software, chemotherapy e-prescribing, structured pathology, PROMs, openEHR, cancer-specific strategy items: n/f.

### Key organisations and people (Cyprus)
- Ministry of Health, Health Monitoring Unit (CyCR; Anna Demetriou, registry co-author). NeHA (Marios Neofytou; Melanie Fysentzou). HIO (GeSY). BOCOC. biobank.cy (Prof Constantinos Deltas, director, per Nature paper). University of Cyprus eHealth Lab (Prof C. S. Pattichis, Prof C. N. Schizas). National Cancer Institute board (2026).

## Malta

### (a) Cancer registries, audits, screening, legal basis, submission, access
- Malta National Cancer Registry, Directorate for Health Information and Research (DHIR), Ministry for Health; population-based since 1991 (hospital-based before); ENCR associate member since 1995; multiple primaries per IARC/IACR rules. https://www.um.edu.mt/library/oar/bitstream/123456789/33194/1/Cancer_in_the_Maltese_Islands_1998-2000.PDF
- Coding: ICD-O-3 (dataset tags; ICD-O-2 in 1998-2000 report); TNM edition n/f. https://ghdx.healthdata.org/node/113711
- ECIS: Malta estimates projected from national rates 2008-2017 and 2012-2021; registry contribution row n/f. https://ecis.jrc.ec.europa.eu/sites/default/files/2026-04/ECIS_methods_EU27_updated_final_28042026.pdf
- Screening: national breast, cervical and colorectal programmes exist; low public uptake because of private screening (16% cervical participation 2022); next cancer plan to widen age groups and add genetic testing. https://maltatoday.com.mt/news/national/134405/malta_records_lowest_cancer_mortality_in_eu ; https://health.ec.europa.eu/document/download/0de41e77-3509-4a58-8853-3d1a562685d0_en?filename=2025_chp_mt_english.pdf
- Researcher access: Malta Health Data Access Body (MHDAB, DHIR) being set up under EHDS with a planned cross-border digital gateway. https://dhir.gov.mt/en/malta-health-data-access-body/
- Submission format, legal basis, clinical audits, screening registry IT: n/f.

### (b) Public datasets and open statistics
- Registry publications: Malta Cancer Incidence and Mortality 1999-2010 (DHIR, 2012), 1998-2007, paediatric 1995-2015 (GHDx). https://ghdx.healthdata.org/print/113711
- EU Country Cancer Profile Malta 2025 (OECD/ECIR) and State of Health in the EU Malta 2025. https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-malta-2025_9cf04830/8ea60e3a-en.pdf
- Eurostat causes-of-death metadata (ICD-10 since 1995). https://ec.europa.eu/eurostat/cache/metadata/EN/hlth_cdeath_simscd_mt.htm
- Open data portal, national health data catalogue, synthetic data: n/f.

### (c) Cancer infrastructure
- National Cancer Plan 2017-2021 (second plan); third plan for 2025-2030 announced, not found published; aligned with Europe's Beating Cancer Plan. https://www.iccp-portal.org/system/files/plans/Malta_National_Cancer_Plan_English.pdf ; https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-malta-2025_9cf04830/8ea60e3a-en.pdf
- Sir Anthony Mamo Oncology Centre (opened Dec 2014, linked to Mater Dei Hospital); dedicated cancer care pathways directorate (OBS-PACE 2025 case study). https://publicservice.gov.mt/en/news/an-oncology-centre-of-excellence-for-cancer-care ; https://eurohealthobservatory.who.int/monitors/pace/case-studies/pace/pace-malta-2025/a-dedicated-directorate-to-improve-cancer-care-pathways
- OECI accredited centre in Malta: n/f.
- Biobanks: Malta BioBank (BBMRI.mt, University of Malta with Department of Health; BBMRI-ERIC national node; colorectal cancer data to BBMRI ADOPT); DwarnaBio population biobank (University of Malta). https://www.bbmri-eric.eu/national-nodes/malta/ ; https://www.openspecimen.org/uni-malta-dwarnabio-population-based-biobank/
- Genomics: National Genomic Infrastructure launched 29 Sep 2023 (1+ Million Genomes); public health service market research for a national genomic record (about 3,500 tests a year). https://www.um.edu.mt/newspoint/news/2023/10/national-genomic-infrastructure-launch-event ; https://maltatoday.com.mt/news/national/130779/public_health_service_to_create_national_genomic_databank_as_tests_grow_to_3500
- Research funding: Xjenza Malta Cancer Research Programme (second call, €1.05m) with the Cancer Research and Innovation Hub Malta, aligned with ECHoS (Cancer Mission national hub); Malta hosted the 2nd Inception Dialogue of the National Cancer Mission Hub. https://lovinmalta.com/lifestyle/health/malta-invests-e1-05-million-in-cancer-research-as-new-funding-call-is-launched/ ; https://lovinmalta.com/malta/driving-cancer-research-forward-malta-hosts-2nd-inception-dialogue-of-the-national-cancer-mission-hub
- EU projects: EUnetCCC, JANE-2, EUCAIM, EUCanScreen, TEHDAS2 Maltese partners: n/f. OMOP/EHDEN partners: n/f. Imaging infrastructure: n/f.
- National data space: openEHR-based national EHR platform (Better, May 2019) as the national infrastructure for documents and structured data; MHDAB for secondary use. https://www.openEHR.org/deployments/provider_deployments_detail/34

### (d) Other digital, non-FHIR, cancer-relevant items
- myHealth patient portal (results and reports visible to linked doctors, eID login) and eHealth portal; Mater Dei RIS, LIS and pharmacy systems since 2007. https://myhealth.gov.mt/ ; https://core.ac.uk/download/268898562.pdf
- MyHealth@EU: Malta among first integrated countries; ePrescription country B operations early 2026 (MHEME project). https://health.gov.mt/services/eu-projects/mheme-eu-project/
- Digital Health and Health Data Strategy 2030 (consultation 21 Nov 2025 to 21 Jan 2026) with an interoperability and data security chapter; cancer-specific items n/f. https://digitalhealth.gov.mt/wp-content/uploads/2025/11/Digital-Health-Strategy-Cover-2025-FINAL-WEB-181125.pdf
- Primary care e-prescribing since 2016 (Pharmacy of Your Choice). https://www.um.edu.mt/library/oar/bitstream/123456789/120356/1/The_electronic_prescription_system_in_development_step_2.pdf
- SNOMED CT in National Patient Summary and MyHealth@EU value set mapping (Information Management Unit). https://www.snomed.org/members/malta
- Oncology chemotherapy prescribing software, tumour-board software, structured pathology reporting, PROMs, openEHR oncology archetypes: n/f.

### Key organisations and people (Malta)
- DHIR (registry, MHDAB; named registry head n/f). Ministry for Health Information Management Unit (Ivan Cacciottolo, SNOMED). Sir Anthony Mamo Oncology Centre. University of Malta (BBMRI.mt, DwarnaBio). Xjenza Malta and Cancer Research and Innovation Hub Malta (ECHoS). Vendor: Better (openEHR platform).
