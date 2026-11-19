### Malta (MT)

Region: Islands. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

#### 1. National base/core FHIR IG
- None. Simplifier jurisdiction MT lists 0 projects and no survey response. https://packages.fhir.org/jurisdictions/MT
- National EHR (Ministry for Health, myHealth portal) runs on openEHR (Better platform, deployed May 2019). https://www.openEHR.org/deployments/provider_deployments_detail/34
- Digital Health and Health Data Strategy 2030 (consultation 21 Nov 2025 to 21 Jan 2026) names interoperability as an aim; no FHIR profile set found. https://www.gov.mt/en/publicconsultation/Pages/2025/NL-0041-2025.aspx

#### 2. Oncology FHIR specifications
- None found.

#### 3. Cancer registry reporting standard
- Malta National Cancer Registry, Directorate for Health Information and Research (DHIR), Ministry for Health; population-based since 1991; listed in the ENCR members contact list as Malta National Cancer Register, Department of Health Information and Research, director Dr Neville Calleja https://www.encr.eu/encr-members-contact-list?page=12 (verified 2026-11-19); national submission format still not found (European reporting via ENCR/ECIS data protocol). https://ghdx.healthdata.org/node/113711 ; https://www.encr.eu/sites/default/files/Data_call/ECIS-data-protocol_2026.pdf

#### 4. Terminologies
- SNOMED CT: member since Oct 2011; NRC is the Information Management Unit, Ministry for Health; SNOMED CT is the "terminology of choice" for EHRs; no Maltese translation; used in the National Patient Summary and MyHealth@EU value set mapping; Malta hosts SNOMED CT Expo 2027. https://www.snomed.org/members/malta ; https://health.gov.mt/national-level-service/snomed-national-release-centre-malta/
- ICD-10 used for cause-of-death data since 1995 and for hospital discharge diagnoses in the DHIR National Hospital Information System; procedures coded in ICD-9-CM, no national ICD-10 modification https://ec.europa.eu/eurostat/cache/metadata/en/hlth_res_esms_mt.htm (verified 2026-11-19). https://ec.europa.eu/eurostat/cache/metadata/en/hlth_cdeath_simscd_mt.htm
- Registry datasets coded in ICD-O-3. TNM edition, LOINC, ATC, national terminology server: still not found (checked 2026-11-19).

#### 5. Key organisations and people
- Ivan Cacciottolo, Ministry for Health, SNOMED General Assembly and Member Forum representative (ivan.cacciottolo@gov.mt).
- DHIR (https://dhir.gov.mt/, blocks automated access) runs the registry; registry director Dr Neville Calleja per the ENCR members contact list https://www.encr.eu/encr-members-contact-list?page=12 (verified 2026-11-19).

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries, audits, screening, legal basis, submission, access
- Malta National Cancer Registry, Directorate for Health Information and Research (DHIR), Ministry for Health; population-based since 1991 (hospital-based before); ENCR associate member since 1995; multiple primaries per IARC/IACR rules. https://www.um.edu.mt/library/oar/bitstream/123456789/33194/1/Cancer_in_the_Maltese_Islands_1998-2000.PDF
- Coding: ICD-O-3 (dataset tags; ICD-O-2 in 1998-2000 report); hospital discharges in ICD-10, procedures in ICD-9-CM (DHIR National Hospital Information System) https://ec.europa.eu/eurostat/cache/metadata/en/hlth_res_esms_mt.htm (verified 2026-11-19); TNM edition still n/f. https://ghdx.healthdata.org/node/113711
- ECIS: Malta estimates projected from national rates 2008-2017 and 2012-2021; registry contribution row still n/f (ECIS registry list page rejects automated access). https://ecis.jrc.ec.europa.eu/sites/default/files/2026-04/ECIS_methods_EU27_updated_final_28042026.pdf
- Screening: national breast, cervical and colorectal programmes exist; low public uptake because of private screening (16% cervical participation 2022); next cancer plan to widen age groups and add genetic testing. https://maltatoday.com.mt/news/national/134405/malta_records_lowest_cancer_mortality_in_eu ; https://health.ec.europa.eu/document/download/0de41e77-3509-4a58-8853-3d1a562685d0_en?filename=2025_chp_mt_english.pdf
- Researcher access: Malta Health Data Access Body (MHDAB, DHIR) being set up under EHDS with a planned cross-border digital gateway. https://dhir.gov.mt/en/malta-health-data-access-body/
- Submission format, legal basis, clinical audits, screening registry IT: n/f.

#### (b) Public datasets and open statistics
- Registry publications: Malta Cancer Incidence and Mortality 1999-2010 (DHIR, 2012), 1998-2007, paediatric 1995-2015 (GHDx). https://ghdx.healthdata.org/print/113711
- EU Country Cancer Profile Malta 2025 (OECD/ECIR) and State of Health in the EU Malta 2025. https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-malta-2025_9cf04830/8ea60e3a-en.pdf
- Eurostat causes-of-death metadata (ICD-10 since 1995). https://ec.europa.eu/eurostat/cache/metadata/EN/hlth_cdeath_simscd_mt.htm
- Open data portal, national health data catalogue, synthetic data: n/f.

#### (c) Cancer infrastructure
- National Cancer Plan 2017-2021 (second plan); third plan for 2025-2030 announced, still not published as of Nov 2026 (health.gov.mt publications list checked via search); aligned with Europe's Beating Cancer Plan. https://www.iccp-portal.org/system/files/plans/Malta_National_Cancer_Plan_English.pdf ; https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-malta-2025_9cf04830/8ea60e3a-en.pdf
- Sir Anthony Mamo Oncology Centre (opened Dec 2014, linked to Mater Dei Hospital); dedicated cancer care pathways directorate (OBS-PACE 2025 case study). https://publicservice.gov.mt/en/news/an-oncology-centre-of-excellence-for-cancer-care ; https://eurohealthobservatory.who.int/monitors/pace/case-studies/pace/pace-malta-2025/a-dedicated-directorate-to-improve-cancer-care-pathways
- OECI: Malta has no member in the OECI directory and no centre on the OECI certified-centres list https://oeci.eu/IstitutesCountry.aspx?id=42 ; https://accreditation.oeci.eu/ (verified 2026-11-19).
- Biobanks: Malta's BBMRI-ERIC national node now represents DwarnaBio, the national population genomic biobank led by the University of Malta https://www.bbmri-eric.eu/national-nodes/ (verified 2026-11-19); the older Malta BioBank (BBMRI.mt, University of Malta with Department of Health) contributed colorectal cancer data to BBMRI ADOPT. https://www.bbmri-eric.eu/national-nodes/malta/ ; https://www.openspecimen.org/uni-malta-dwarnabio-population-based-biobank/
- Genomics: National Genomic Infrastructure launched 29 Sep 2023 (1+ Million Genomes); public health service market research for a national genomic record (about 3,500 tests a year). https://www.um.edu.mt/newspoint/news/2023/10/national-genomic-infrastructure-launch-event ; https://maltatoday.com.mt/news/national/130779/public_health_service_to_create_national_genomic_databank_as_tests_grow_to_3500
- Research funding: Xjenza Malta Cancer Research Programme (second call, €1.05m) with the Cancer Research and Innovation Hub Malta, aligned with ECHoS (Cancer Mission national hub); Malta hosted the 2nd Inception Dialogue of the National Cancer Mission Hub. https://lovinmalta.com/lifestyle/health/malta-invests-e1-05-million-in-cancer-research-as-new-funding-call-is-launched/ ; https://lovinmalta.com/malta/driving-cancer-research-forward-malta-hosts-2nd-inception-dialogue-of-the-national-cancer-mission-hub
- EU projects: EUnetCCC: Ministry for Health and Active Ageing co-leads WP3 (Evaluation) https://eunetccc.eu/ ; JANE (2022-2025): Ministry for Health, WP1, WP4, WP9 https://www.jane-project.eu/the-jane-team/ ; EUCanScreen: Ministry for Health and Active Ageing (competent authority) https://eucanscreen.eu/partners/ ; TEHDAS2: Ministry of Health and Active Ageing https://tehdas.eu/tehdas2/partners/ ; ECHoS: Malta national cancer mission hub (inception dialogue 10 Jul 2024, cited as a model at the 2025 Town Hall) https://cancerworld.net/europes-national-cancer-mission-hubs-from-a-vision-to-sustainable-infrastructures/ (verified 2026-11-19). JANE-2 Maltese partner: n/f. OMOP/EHDEN: no Maltese data partner https://www.ehden.eu/datapartners/ . EUCAIM: no Maltese partner https://cancerimage.eu/partners/ (verified 2026-11-19).
- National data space: openEHR-based national EHR platform (Better, May 2019) as the national infrastructure for documents and structured data; MHDAB for secondary use. https://www.openEHR.org/deployments/provider_deployments_detail/34

#### (d) Other digital, non-FHIR, cancer-relevant items
- myHealth patient portal (results and reports visible to linked doctors, eID login) and eHealth portal; Mater Dei RIS, LIS and pharmacy systems since 2007. https://myhealth.gov.mt/ ; https://core.ac.uk/download/268898562.pdf
- MyHealth@EU: Malta among first integrated countries; ePrescription country B operations early 2026 (MHEME project). https://health.gov.mt/services/eu-projects/mheme-eu-project/
- Digital Health and Health Data Strategy 2030 (consultation 21 Nov 2025 to 21 Jan 2026) with an interoperability and data security chapter; cancer-specific items n/f. https://digitalhealth.gov.mt/wp-content/uploads/2025/11/Digital-Health-Strategy-Cover-2025-FINAL-WEB-181125.pdf
- Primary care e-prescribing since 2016 (Pharmacy of Your Choice). https://www.um.edu.mt/library/oar/bitstream/123456789/120356/1/The_electronic_prescription_system_in_development_step_2.pdf
- SNOMED CT in National Patient Summary and MyHealth@EU value set mapping (Information Management Unit). https://www.snomed.org/members/malta
- Oncology chemotherapy prescribing software, tumour-board software, structured pathology reporting, PROMs, openEHR oncology archetypes: n/f.

#### Key organisations and people (Malta)
- DHIR (registry, MHDAB; registry director Dr Neville Calleja per the ENCR members contact list https://www.encr.eu/encr-members-contact-list?page=12 (verified 2026-11-19)). Ministry for Health Information Management Unit (Ivan Cacciottolo, SNOMED). Sir Anthony Mamo Oncology Centre. University of Malta (BBMRI.mt, DwarnaBio). Xjenza Malta and Cancer Research and Innovation Hub Malta (ECHoS). Vendor: Better (openEHR platform).

#### (a) Cancer registries
- Malta National Cancer Registry: population-based since 1991 (hospital-based before), within the Directorate for Health Information and Research (DHIR); ENCR member since 1995, IACR voting member. https://um.edu.mt/library/oar/bitstream/123456789/44319/1/CANCER%20INCIDENCE%20AND%20MORTALITY.PDF
- ENCR member registries: Malta National Cancer Register (director Dr. Neville Calleja). Confirms the earlier membership statement; the join year 1995 is not shown on the list. Source: https://www.encr.eu/encr-members-contact-list (read 2026-11-19) (verified 2026-11-19)
- Coverage: whole population (~400,000); ENCR contact list names director Neville Calleja. https://encr.eu/encr-members-contact-list?page=9
- Clinical tumour registry: joint clinical tumour registry created for cancer care tracking (WHO OBS-PACE). https://eurohealthobservatory.who.int/monitors/pace/analyses/pace/integrated-governance-digital-solutions-and-stakeholder-collaboration-lessons-on-improving-cancer-care-from-malta-and-upper-austria
- Screening: BreastScreen, colorectal, cervical programmes (healthscreening.gov.mt). https://healthscreening.gov.mt/en/?p=5486
- Legal basis: Notification of Cancer Act, Cap. 154 (1957), obliging medical practitioners attending a cancer patient to notify the Superintendent of Public Health (https://legislation.mt/eli/cap/154/eng/pdf) (verified 2026-11-19). Submission format, ICD-O/TNM editions, variable dictionary: n/f (ICD-O-3 listed for paediatric dataset, https://ghdx.healthdata.org/node/373740; dhir.gov.mt returns HTTP 403 to automated fetch and deputyprimeminister.gov.mt returned a Cloudflare origin DNS error in a browser on 2026-11-19, so the DHIR registry pages could not be verified).
- Researcher access: via DHIR; formal route n/f.

#### (b) Public datasets
- Registry datasets on GHDx (1995-present; 1998-2007; 1999-2010; paediatric 1995-2015). https://ghdx.healthmetricsandevaluation.org/organizations/malta-national-cancer-registry
- OECD/EU Country Cancer Profile Malta 2025. https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-mt-2024-1677-en.pdf
- Research data access body: Malta Health Data Access Body under DHIR, with national metadata catalogue of public health registries. https://dhir.gov.mt/en/?p=7508
- ECIS: National Cancer Registry of Malta contributes incidence 1993-2013 only (archived ECIS list) https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19). Synthetic data: n/f.

#### (c) Cancer infrastructure
- National Cancer Plan 2017-2021 (latest found); no successor cancer plan found in 2024-2026 searches; related: National Palliative Care Strategy 2025-2035, NCD Prevention Framework 2025-2035, Digital Health and Health Data Strategy 2025-2030 (https://health.gov.mt/resources/) (verified 2026-11-19). https://www.iccp-portal.org/system/files/plans/MinistryForHealth-Cancer%20Plan.pdf
- Sir Anthony Mamo Oncology Centre (Mater Dei): oncology centre of excellence; nurse navigation, fast-track referrals. https://eurohealthobservatory.who.int/monitors/pace/case-studies/pace/pace-malta-2025/a-dedicated-directorate-to-improve-cancer-care-pathways
- National Cancer Mission Hub preparation (Nov 2024). https://www.independent.com.mt/articles/2024-11-23/local-news/Second-meeting-held-in-preparation-for-Cancer-Mission-Hub-in-Malta-6736265992
- Biobank: BBMRI.mt node = DwarnaBio (University of Malta, Nikolai Pace, Gillian Martin); first 200 WGS under 1+MG-linked programme. https://www.bbmri-eric.eu/national-nodes/
- Genomics: national genomic record system under market research (3,500 tests). https://maltatoday.com.mt/news/national/130779/public_health_service_to_create_national_genomic_databank_as_tests_grow_to_3500
- EUCAIM: Maltese breast screening project linked to EUCAIM/Cancer Image Europe (BreastSCan). https://healthscreening.gov.mt/en/?p=5486
- Mater Dei: national hub for 24 ERNs. https://maltatoday.com.mt/news/national/123844/study_plans_to_unlock_secrets_of_maltese_genetic_makeup_
- CraNE partner: Ministry for Health (https://crane4health.eu/partners/); EUCanScreen: Ministry for Health and Active Ageing (https://eucanscreen.eu/partners/); ECHoS hub: Cancer Research and Innovation Hub Malta (CRIHM) (https://cancermissionhubs.eu/hubs/) (verified 2026-11-19). OECI: no Maltese centre on https://accreditation.oeci.eu/ (verified 2026-11-19). EHDEN/OMOP (no Maltese data partner listed), UNCAN.eu, canSERV, JANE, TEHDAS2: n/f.

#### (d) Digital, non-FHIR
- myHealth portal; fast-track cancer referrals for doctors. https://digitalhealth.gov.mt/?p=2150
- University of Malta digital imaging bank and imaging/genomics datasets planned. https://www.um.edu.mt/clusters/disc/pillarsandprojects/
- Structured pathology, tumour-board software, e-prescribing oncology, openEHR: n/f.

#### Key organisations and people
- Ministry for Health; DHIR (Neville Calleja; HDAB); SAMOC / Mater Dei; University of Malta (Nikolai Pace, Gillian Martin, DwarnaBio). https://www.openspecimen.org/uni-malta-dwarnabio-population-based-biobank/

---
