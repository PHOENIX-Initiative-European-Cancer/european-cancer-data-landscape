### Cyprus (CY)

Region: Islands. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

#### 1. National base/core FHIR IG
- None published. State of FHIR 2026 (anonymous respondent): "a national core guide exists and is used in a limited set of use cases"; FHIR advised, not mandated; NeHA appointed Digital Health Authority under EHDS Article 19; terminology server status unclear. https://packages.fhir.org/jurisdictions/CY
- Only public package: ehealth4u.package 1.0.0, FHIR R4, University of Cyprus eHealth Lab, draft prototype of the national EHR, depends on hl7.fhir.uv.ips 1.1.0. https://packages.simplifier.net/ehealth4u.package ; https://doi.org/10.1177/20552076261431813
- National EHR: NeHA designing it, development scheduled to begin late 2026. https://www.interregeurope.eu/good-practices/national-ehealth-authority-neha

#### 2. Oncology FHIR specifications
- None found.

#### 3. Cancer registry reporting standard
- Cyprus Cancer Registry (CyCR), Health Monitoring Unit, Ministry of Health; population-based; member of IACR and ENCR; registry staff code hospital notifications (public and private hospitals and clinics) using MECC/NCI coding and staging; submission format still not found (Ministry of Health site blocks automated access, checked 2026-11-19); no FHIR. https://pmc.ncbi.nlm.nih.gov/articles/PMC11168067/

#### 4. Terminologies
- SNOMED CT: member since Sept 2018; NRC is the National eHealth Authority (NeHA); no national extension found; adoption "subject to a decision for adoption by all involved stakeholders". https://www.snomed.org/members/cyprus ; https://www.snomed.org/snomed-in-action/national-ehealth-authority-of-cyprus
- Current coding mix: ICD-10, LOINC, ICPC, CPT-4 (reimbursement), free text (NeHA statement). ICD-10 national modification: not found.
- Registry: ICD-O-3, ICD-10, SEER Summary Staging, TNM (edition still not found; MECC 2009 coding manual is the last public coding reference https://webarchive.library.unt.edu/web/20130213205307/http:/mecc.cancer.gov/2009_MECC_Manual_of_Coding.pdf ).
- National terminology server: in planning, not available. ATC, UICC edition: not found.

#### 5. Key organisations and people
- NeHA (https://www.neha.org.cy/): Marios Neofytou, SNOMED General Assembly and Member Forum representative; Melanie Fysentzou, Member Forum.
- eHealth4U, University of Cyprus: Prof Constantinos S. Pattichis, Prof Christos N. Schizas.
- Registry: Anna Demetriou, Statistics Officer at the Health Monitoring Unit and Health Ministry representative on the National Cancer Institute board https://en.politis.com.cy/news/health/1031893/first-board-appointed-for-national-cancer-institute (verified 2026-11-19); registry head still not found (MECC 2009 manual listed Dr Pavlos Pavlou as Cyprus coordinator, historical).

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries, audits, screening, legal basis, submission, access
- Cyprus Cancer Registry (CyCR), Health Monitoring Unit, Ministry of Health; population-based (est. 1996-1998 with MECC/NCI support); member of IACR and ENCR; codes hospital notifications from all public and private hospitals using MECC/NCI coding: ICD-O-3, ICD-10, SEER Summary Staging, TNM (edition still n/f). https://pmc.ncbi.nlm.nih.gov/articles/PMC11168067/
- ECIS: CyCR supplies incidence 1998-2022 and mortality 2004-2020 (updated Sep 2025); non-malignant CNS tumours under-recorded. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Submission format, legal basis, clinical audits, screening registry IT, researcher access route: n/f (registry data supplied pseudonymised to academic studies on request).
- Screening: breast screening expanded; national colorectal programme in final implementation stage (2025 profile); cervical screening opportunistic (2023 profile). https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-cyprus-2025_9133d835/c5a3f19e-en.pdf

#### (b) Public datasets and open statistics
- Health Monitoring Unit figures (about 4,260 new cases and 1,600 deaths a year) released via press; no open data portal found. https://www.cna.org.cy/en/article/9778948/cyprus-records-4-260-new-cancer-cases-and-1-600-deaths-annually
- EU Country Cancer Profile Cyprus 2025 (OECD/ECIR). https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/eu-country-cancer-profile-cyprus-2025_9133d835/c5a3f19e-en.pdf
- Historical progress reports (2008-2010) on GHDx. https://ghdx.healthdata.org/print/114511
- Health data access body: a national HDAB is being established under NeHA for HealthData@EU https://oecd.ai/en/dashboards/policy-initiatives/european-health-data-space-for-secondary-use-cy-cy-ehds-2nd (verified 2026-11-19); national health data catalogue, synthetic data: n/f.

#### (c) Cancer infrastructure
- National cancer strategy: first 2009, revised 2019 to EU guidelines and aligned with Europe's Beating Cancer Plan. https://www.iccp-portal.org/system/files/plans/Cyprus_National_Strategy_on_Cancer_English.pdf ; https://ecanplus.eu/downloads/eCANPlus_WP4_Policy_Mapping_Country_Factsheet_CY_updated_reviewed_final.pdf
- National Cancer Institute: bill approved Mar 2026, first board appointed, directors approved Sep 2026; remit includes updating the national strategy. https://cyprus-mail.com/2026/03/11/cyprus-to-create-national-cancer-institute ; https://cyprus-mail.com/2026/09/10/ministers-approve-directors-of-cyprus-first-national-cancer-institute
- Cancer centres: Bank of Cyprus Oncology Centre (BOCOC, not-for-profit, since 1998); German Oncology Center (Limassol, private, since 2017, the only Cypriot OECI member, Full Member, not on the OECI certified-centres list, and a EUCAIM partner) https://oeci.eu/IstitutesCountry.aspx?id=42 ; https://cancerimage.eu/partners/ (verified 2026-11-19); GOC contracted to GeSY; plans to unify oncology services of Nicosia and Limassol general hospitals with BOCOC. https://oeci.eu/IstitutesCountry.aspx?id=42 ; https://www.bococ.org.cy/en/about-us ; https://cyprusprofile.com/articles/german-oncology-centre-join-gesy
- Biobank: BBMRI.cy is the BBMRI-ERIC national node, led by the Ministry of Health, integrating biobank.cy (University of Cyprus Centre of Excellence, CY-Biobank 2019-2026, EU grant 857122, target 16,500 participants by 2027; partners include BOCOC) and the CING biobank (since 2012) https://www.bbmri-eric.eu/national-nodes/ (verified 2026-11-19). https://www.bbmri-eric.eu/national-nodes/cyprus/ ; https://www.nature.com/articles/s41598-024-78644-4
- Genomics: Cyprus Human Genome Project (biobank.cy); national genomics strategy n/f. https://biobank.cy/portfolio/cy-biobank_factsheet/
- EU projects: EUnetCCC sustainability session hosted at BOCOC 29 Apr 2026; eCAN joint action telerehabilitation trial site; Xt-EHR Joint Action (NeHA). https://www.europeancancer.org/events/421:securing-a-lasting-impact.html ; https://clinicaltrials.gov/study/NCT06007001 EUCAIM: German Oncology Center https://cancerimage.eu/partners/ ; JANE-2: Ministry of Health and BOCOC https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/ ; EUCanScreen: Ministry of Health (competent authority) and University of Cyprus https://eucanscreen.eu/partners/ ; TEHDAS2: NeHA, Karaiskakeio Foundation, CYENS https://tehdas.eu/tehdas2/partners/ ; ECHoS: Cyprus participates https://en.politis.com.cy/social-lens/1000819/cyprus-joins-eu-push-to-improve-cancer-prevention-and-care (verified 2026-11-19). canSERV: no Cypriot partner listed.
- OMOP/EHDEN: no Cypriot data partner in the EHDEN partner list (187 partners, 29 countries) https://www.ehden.eu/datapartners/ (verified 2026-11-19). Imaging infrastructure: German Oncology Center in EUCAIM (above); national imaging infrastructure n/f.
- National data space: NeHA designated Digital Health Authority (EHDS Art. 19); national EHR tender expected end 2025, development from late 2026. https://www.interregeurope.eu/good-practices/national-ehealth-authority-neha

#### (d) Other digital, non-FHIR, cancer-relevant items
- GeSY integrated information system (HIO) with beneficiary and provider portals; hospital HIS in Nicosia and Famagusta general hospitals since 2007; provider systems historically on the proprietary DASTA standard. https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/cyprus2025/organization-and-governance/health-information-systems ; https://www.xt-ehr.eu/wp-content/uploads/2026/05/Xt-EHR-D4.1.pdf
- myHealth@CY citizen app contracted Nov 2025 (NeHA, Cyta, HIO), to connect to GeSY and grow into a full EHR. https://cyprus-mail.com/2025/11/25/new-app-to-offer-access-to-health-data
- Coding environment: ICD-10, LOINC, ICPC, CPT-4 for reimbursement, free text; SNOMED CT mapping planned. https://www.snomed.org/snomed-in-action/national-ehealth-authority-of-cyprus
- MyHealth@EU: NeHA patient summary guideline; cross-border services launched with Greece (Interreg HUMAN). https://www.neha.org.cy/wp-content/uploads/2023/03/guidelines_PatientSummary.pdf ; https://www.interregeurope.eu/human/news-and-events/news/cyprus-greece-launch-cross-border-digital-health-services
- eHealth4U prototype national EHR (FHIR R4, SNOMED CT, LOINC; IPS-based). https://doi.org/10.1177/20552076261431813
- Tumour-board software, chemotherapy e-prescribing, structured pathology, PROMs, openEHR, cancer-specific strategy items: n/f.

#### Key organisations and people (Cyprus)
- Ministry of Health, Health Monitoring Unit (CyCR; Anna Demetriou, registry co-author). NeHA (Marios Neofytou; Melanie Fysentzou). HIO (GeSY). BOCOC. biobank.cy (Prof Constantinos Deltas, director, per Nature paper). University of Cyprus eHealth Lab (Prof C. S. Pattichis, Prof C. N. Schizas). National Cancer Institute board (2026).

#### (a) Cancer registries
- Cyprus Cancer Registry: population-based, Health Monitoring Unit, Ministry of Health; established 1998 with MECC/US NCI support; member of IACR and ENCR. https://pmc.ncbi.nlm.nih.gov/articles/PMC4523219
- Output: ~4,260 new cases and ~1,600 deaths per year. https://en.politis.com.cy/social-lens/985101/cyprus-records-4260-new-cancer-cases-annually
- Researcher access: pseudonymised data after National Bioethics Committee approval (study example). https://pmc.ncbi.nlm.nih.gov/articles/PMC11168067
- Coding: ICD-O-3 with CanReg4 software deriving ICD-10 codes; registry set up 1996-1998 with Middle East Cancer Consortium support (https://pmc.ncbi.nlm.nih.gov/articles/PMC4523219) (verified 2026-11-19). Legal basis, submission format, TNM edition, variable dictionary: n/f.
- Screening: breast programme since 2003; colorectal programme for GeSY beneficiaries 50-74 in final implementation; cervical pending. https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-cy-2024-1662-en.pdf
- Note: northern Cyprus 2018 Cancer Registration Law never entered into force (separate jurisdiction). https://www.cyprus-faq.com/en/north/news/vrachi-trebuyut-srochno-vosstanovit-rakovyi-registr

#### (b) Public datasets
- Registry progress reports (2008-2010) on GHDx (https://ghdx.healthdata.org/print/114511); Cyprus Cancer Registry contributes incidence 1998-2022 to ECIS (archived list, https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data) (verified 2026-11-19).
- EU Country Cancer Profile Cyprus 2025. https://read.oecd-ilibrary.org/en/publications/eu-country-cancer-profile-cyprus-2025_c5a3f19e-en
- Research data access body: national HDAB under the National eHealth Authority (NeHA, head Constantinos Pattichis); CY-EHDS-2nd project since 2022. https://oecd.ai/en/dashboards/policy-initiatives/european-health-data-space-for-secondary-use-cy-cy-ehds-2nd
- Open data portal, synthetic data, national catalogue: n/f.

#### (c) Cancer infrastructure
- National Strategy on Cancer 2009; updated 2019; a May 2024 gov.cy strategy PDF is referenced in the EU Country Cancer Profile Cyprus 2025 but the profile PDF and gov.cy file are blocked to automated fetch (NEEDS BROWSER). https://www.europeancancer.org/download-file/1864.html
- National Cancer Institute: law passed, first board appointed; mandate to prepare and update the national cancer strategy and advise on the registry (2025-2026). https://en.politis.com.cy/news/health/1031893/first-board-appointed-for-national-cancer-institute
- Biobanks: BBMRI.cy node led by Ministry of Health; biobank.cy (University of Cyprus) and CING biobanks; Genome of Europe and GDI participation. https://www.bbmri-eric.eu/national-nodes/
- Genomics in EHR: CING and Xt-EHR/EHDS2nd workshop (Sept 2025). https://berc.ucy.ac.cy/index.php/events-press/230-integrating-genomics-into-the-ehr
- EUCAIM partner: German Oncology Center. https://cancerimage.eu/partners/
- Xt-EHR Joint Action coordinated by Cyprus. https://cna.org.cy/en/article/8172916/cyprus-to-benefit-from-eu-health-data-space-regulation-says-ehealth-authority-head
- OECI: no Cypriot centre on the OECI list as of 2026-11-19 (https://accreditation.oeci.eu/) (verified 2026-11-19); Bank of Cyprus Oncology Centre holds CHKS and ISO 9001:2015 accreditation, not OECI (https://cyprus-mail.com/2026/01/21/double-international-recognition-for-bank-of-cyprus-oncology-centre) (verified 2026-11-19). CraNE partner: Ministry of Health (https://crane4health.eu/partners/); EUCanScreen: Ministry of Health and University of Cyprus (https://eucanscreen.eu/partners/); TEHDAS2: National eHealth Authority, Karaiskakeio Foundation, CYENS (https://tehdas.eu/partners/); ECHoS hub exists (https://cancermissionhubs.eu/hubs/) (verified 2026-11-19). EHDEN/OMOP (no Cypriot data partner listed), UNCAN.eu, canSERV, JANE: n/f.

#### (d) Digital, non-FHIR
- GeSY (GHS) insurance system; cancer patients access via chronic patient registries. https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/cyprus2025/provision-of-services/public-health
- myHealth@CY app (Nov 2025), to connect with GeSY and evolve into full EHR. https://cyprus-mail.com/2025/11/25/new-app-to-offer-access-to-health-data
- National eHealth Law and NeHA established. https://cyprus-mail.com/2024/06/28/gesy-to-benefit-from-eu-e-health-minister-says
- SNOMED CT: NeHA case listed by SNOMED International. https://www.snomed.org/snomed-in-action/national-ehealth-authority-of-cyprus
- Structured pathology, tumour-board software, chemo prescribing, openEHR: n/f.

#### Key organisations and people
- Ministry of Health Health Monitoring Unit (registry); NeHA (Constantinos Pattichis); National Cancer Institute (new); CING; University of Cyprus biobank.cy; German Oncology Center; Bank of Cyprus Oncology Centre (n/f details).

---
