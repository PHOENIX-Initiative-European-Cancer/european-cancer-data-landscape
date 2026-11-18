### Ireland (IE)

Region: Islands. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

#### 1. National base/core FHIR IG
- None published. State of FHIR 2026 (contributor Patrick Marren, HSE MyHealth@EU team leader): "no national base FHIR implementation guide yet"; HIQA is the national standards body; FHIR R4 in use; a national FHIR terminology server is in production; Ireland is establishing a FHIR affiliate. https://packages.fhir.org/jurisdictions/IE
- Vendor/community guides: IE (Ireland) Core Implementation Guide 1.0.0-ballot, publisher iEHR.ai, FHIR R4, canonical http://iehr.ai/fhir/ie/core/ImplementationGuide/iehr.fhir.ie.core, certified phase one by GPIT (ICGP, HSE, Department of Health). https://www.iehr.ai/fhir/ie/core/ FHIR-IRL-Core 0.1.0, draft, derived from HL7 Europe Core, not sponsored by an official body. https://github.com/HL7-Ireland-Shadow/FHIR-IRL-Core
- HL7/openEHR Ireland affiliate proposal meeting held 11 May 2026 in Dublin. https://discourse.openehr.org/t/hl7-openehr-ireland-affiliate-meeting-monday-11-may-2026/16789
- HSE FHIR use: Health App, MyHealth@EU, National Shared Care Record (event 20 Oct 2025). https://www.ehealthireland.ie/news-media/news/2025/fhir-and-the-national-shared-care-record-a-transformative-step-in-irish-healthcare

#### 2. Oncology FHIR specifications
- None found. NCRI publishes no FHIR specification; no mCODE reuse found.

#### 3. Cancer registry reporting standard
- National Cancer Registry Ireland (NCRI), statutory body, Cork. Electronic feeds: monthly or quarterly histopathology lab feeds (SNOMED-coded, converted to ICD-O by NCRI), radiotherapy unit feeds, quarterly HIPE feed, quarterly CSO death feed; about 90% of tumours created electronically; Cancer Data Registrars complete records in the NCRI Cancer Registration System. No FHIR or published CSV submission standard. Data Dictionary v2.0 (2023). https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri ; https://www.ncri.ie/en/media/145/download

#### 4. Terminologies
- SNOMED CT: member since Nov 2016; NRC is HSE Technology and Transformation (snomed@hse.ie); SNOMED CT Irish Edition with Irish Clinical and Drug Extension; production releases Oct 2025 (11th), Jan 2026, Feb 2026, Jun 2026. https://www.snomed.org/members/ireland ; https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/1003192357
- ICD-10-AM/ACHI/ACS 12th edition for HIPE from 1 Jan 2024 (10th edition 2020 to 2023); 13th edition adoption not found. https://www.hse.ie/eng/about/personalpq/pq/2025-pq-responses/july-2025/pq-35566-25-padraig-mac-lochlainn.pdf
- NCRI coding: ICD-O-3.2 from 2020; UICC TNM 7th edition from 2014 per HIQA profile (TNM 8 adoption not confirmed); ACHI 6th edition for treatments; reporting in ICD-10.
- LOINC: adopted for laboratory data; hosted on the HSE Central Terminology Service (CTS) with SNOMED CT Irish Edition (incl. medicines) and UCUM. CTS procured Jul 2025, deployed Q3 2025 to Q1 2026, in beta, FHIR terminology server; product reported as Ontoserver (not verified). https://about.hse.ie/news/the-hse-central-terminology-service-cts ; https://www.ehealthireland.ie/news-media/news/2025/fhir-central-terminology-server-for-the-hse
- ATC: not found. UICC edition in clinical use: not found.

#### 5. Key organisations and people
- HSE Technology and Transformation, Enterprise Architecture: Theresa Barry, Clinical Terminology Architect, SNOMED Member Forum representative; Niall Sinnott, Department of Health, SNOMED General Assembly representative; Patrick Marren, HSE MyHealth@EU team leader. https://www.snomed.org/members/ireland
- NCRI: Dr Theresa Redaniel, acting director (2026), after Prof Deirdre Murray's five-year term. https://ncri.ie/en/news/news-from-ncri/dr-theresa-redaniel-appointed-acting-director-of-the-national-cancer-registry

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries, audits, screening, legal basis, submission, access
- National Cancer Registry Ireland (NCRI), statutory registry (established 1991, nationwide from 1994), Republic of Ireland; reports to IARC and ECIS. https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri
- Submission: electronic feeds from histopathology labs (monthly/quarterly, SNOMED-coded, converted to ICD-O), radiotherapy units, HIPE (quarterly), CSO deaths; ~90% of tumours created electronically; registered by Cancer Data Registrars in the Cancer Registration System; NCRI Data Dictionary v2.0 (2023). https://www.ncri.ie/en/media/145/download
- Coding: ICD-O-3.2 from 2020; UICC TNM 7th from 2014 (HIQA profile; TNM 8 not confirmed); ACHI 6th for treatments; reporting in ICD-10. https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri
- Clinical audits: n/f (NCCP KPIs exist but no national audit programme found).
- Screening registries: National Screening Service (HSE, since 1 Jan 2014) runs BreastCheck (register from Department of Social Protection), CervicalCheck, BowelScreen (population register age 59-70, awaiting IHI field); HIQA catalogues them as national collections. https://www.hiqa.ie/areas-we-work/health-information/data-collections/breastcheck-national-breast-screening-programme ; https://www.hiqa.ie/areas-we-work/health-information/data-collections/bowelscreen-national-bowel-screening-programme
- Legal basis: Health Research Regulations 2018 (consent declaration committee) govern research use; Health Information Bill pending; EHDS applies from 2029. https://www.cso.ie/en/aboutus/lgdp/csodatapolicies/dataforresearchers/healthresearchdatacentrerdc/faq/ ; https://packages.fhir.org/jurisdictions/IE
- Researcher access: NCRI data access page and open data portal; NCRI and Aridhia Secure Data Environment for pseudonymised clinical and genomic data; CSO Health Research Data Centre (remote secure access); HRB DASSL model (trusted third party, virtual safe haven). https://aridhia.com/blog/national-cancer-registry-ireland-aridhia-announce-partnership-to-deliver-a-secure-data-environment/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9351012/
- ENCR membership: NCRI is an ENCR member (ENCR data protocol 2026). https://www.encr.eu/sites/default/files/Data_call/ECIS-data-protocol_2026.pdf

#### (b) Public datasets and open statistics
- NCRI annual statistical report (Cancer in Ireland 1994-2022, 2024; 2026 report), online incidence and survival statistics, open data portal (eGovernment award shortlist). https://www.ncri.ie/node/346 ; https://www.ncri.ie/en/news/news-from-ncri/ncri-shortlisted-for-egovernment-award-in-open-data-category
- HIQA national data collections catalogue (NCRI, HIPE, screening). https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-cancer-registry-ireland-ncri
- HIPE annual activity reports (Healthcare Pricing Office; ICD-10-AM 12th edition from 2024). https://www.drugsandalcohol.ie/47018/1/HIPE_2025_Activity_in_Acute_Public_Hospitals_.pdf
- Catalogue of Irish health data resources for primary care cancer research (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12408799/
- ECIS: NCRI data in ECIS (Ireland in EU27 estimates). https://ecis.jrc.ec.europa.eu/sites/default/files/2026-04/ECIS_methods_EU27_updated_final_28042026.pdf
- Synthetic datasets: n/f.

#### (c) Cancer infrastructure
- National Cancer Strategy 2017-2026, delivered by the HSE National Cancer Control Programme (NCCP). https://ehealthireland.ie/ehealth-functions/acute-delivery/national-cancer-information-system
- OECI: Trinity St James's Cancer Institute accredited 2019, Comprehensive Cancer Centre 2025 (first in Ireland); Beaumont RCSI Cancer Centre accredited 2023; CUH/UCC Cancer Centre accredited May 2025; HSE West and North West cancer network accredited Jul 2025. https://www.tcd.ie/news_events/articles/2025/prestigious-comprehensive-cancer-centre-status-for-tsjci/ ; https://www.hse.ie/eng/about/our-health-service/making-it-better/hse-west-and-north-west-cancer-network-receives-oeci-cancer-centre-certificate-of-accreditation.html
- Genomics: National Strategy for Accelerating Genetic and Genomic Medicine in Ireland (HSE, Dec 2022; implementation plan 2023; national office for genetics and genomics); NCCP Genomics Test Directory for Cancer (Jul 2024). https://www.hse.ie/eng/about/who/strategic-programmes-office-overview/national-strategy-for-accelerating-genetic-and-genomic-medicine-in-ireland/national-strategy-for-accelerating-genetic-and-genomic-medicine-in-ireland.pdf ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12272048/
- Biobanks: BBMRI-ERIC Irish node: n/f. Cancer Trials Ireland: n/f in this search.
- All-island: eHealth Hub for Cancer (QUB and University of Limerick); All-Island Cancer Research Institute (AICRI, UCD and QUB); 2025 all-island cancer research landscape report; "Harnessing Cancer Data for Better Health" seven-point roadmap endorsed at the All-Island Cancer Data Forum 2026 (Belfast), with a proposed All-Island Cancer Data Innovation Co-Centre. https://www.health-ni.gov.uk/news/cancer-leaders-launch-new-plans-build-all-island-digital-cancer-research-powerhouse ; https://t4test.ucd.ie/research/news/2025/all-islandcancerresearchlandscapereport2025/
- EU projects: EUCanScreen (Department of Health, RCSI, HSE National Screening Service). https://www2.healthservice.hse.ie/organisation/nss/news/one-year-of-eucanscreen-working-together-to-strengthen-cancer-screening-across-europe/ EUnetCCC, JANE-2, EUCAIM, canSERV, ECHoS, TEHDAS2: n/f.
- OMOP CDM: Trinity St James's Cancer Institute is an EHDEN data partner (fifth call, first Irish partner). https://www.ehden.eu/?p=4179
- National data space: HSE National Shared Care Record (deploying); HSE One Health Record national EHR procurement approved Feb 2026 (market consultation Jun 2025). https://about.hse.ie/news/procurement-launched-for-hse-one-health-record/ ; https://www.digitalhealth.net/2026/02/ireland-to-begin-procurement-for-a-national-electronic-health-record/

#### (d) Other digital, non-FHIR, cancer-relevant items
- National Cancer Information System (NCIS): national electronic record for cancer diagnosis, SACT prescribing/preparation/administration and MDT decisions; BD Cato, Celsius37 TumorBoard and CancerCenter, Orchestra messaging; first site 2019, 26 SACT hospitals planned; underpinned by NCCP national SACT regimen library. https://ehealthireland.ie/ehealth-functions/acute-delivery/national-cancer-information-system ; https://www.saolta.ie/news/new-innovative-information-system-cancer-treatment-implemented-uhg
- HSE Health App (Feb 2025: appointments, referrals, vaccinations; no cancer feature found). https://www.digitalhealth.net/2026/02/ireland-to-begin-procurement-for-a-national-electronic-health-record/
- MyHealth@EU national contact point run by HSE. https://ehealthireland.ie/technology-and-transformation-functions/standards-and-shared-care-records-sscr/myhealth-eu/my-health-eu-team
- Standards policy: HIQA messaging standards guidance and terminology guidance (SNOMED CT, LOINC); Data for Care webinar (Mar 2026) names FHIR, SNOMED CT, LOINC, ICD-10-AM. https://www.hiqa.ie/ga/node/45505 ; https://about.hse.ie/news/data-for-care-webinar-highlights-progress-on-standards-interoperability-and-health-information-legislation/
- Structured pathology reporting, PROMs programme, openEHR oncology, tumour-board software beyond NCIS: n/f.

#### Key organisations and people (Ireland)
- NCRI: Dr Theresa Redaniel, acting director (2026); board chair Dr Paul Kavanagh (chair designate). https://ncri.ie/en/news/news-from-ncri/dr-paul-kavanagh-appointed-chair-designate-of-the-national-cancer-registry
- HSE NCCP (NCIS owner); HSE Technology and Transformation (Theresa Barry, terminology; Patrick Marren, MyHealth@EU). HIQA (standards). HRB (DASSL). AICRI co-leads Prof William Gallagher (UCD) and Prof Mark Lawler (QUB). TSJCI (OECI CCC). EHDEN partner: TSJCI.
