### Denmark (DK)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "HL7 FHIR Implementation Guide: DK Core" (DkCore), package `hl7.fhir.dk.core`, FHIR R4 (4.0.1), latest release 3.7.0 (IG dated 2026-05-30; 3.5.0 published 2025-12-19), published by HL7 Denmark with MedCom as steward, released twice a year. Canonical http://hl7.dk/fhir/core. MedCom layers `medcom.fhir.dk.core` 4.0.0 (R4) on top.
   https://hl7.dk/fhir/core/index.html ; https://packages.fhir.org/hl7.fhir.dk.core ; https://build.fhir.org/ig/medcomdk/dk-medcom-core
2. **Oncology FHIR specifications:** not found. No DMCG, RKKP or Cancerregisteret FHIR IG located; Danish FHIR work covers referrals, diagnostics, documents and telemedicine (FUT eHealth Infrastructure).
   https://packages.fhir.org/jurisdictions/DK ; https://ehealth.sundhed.dk/fhir
3. **Cancer registry reporting:** Cancerregisteret is run by Sundhedsdatastyrelsen (unit Klassifikationer og Inddata). Fully electronic since 2004; fed from Landspatientregisteret LPR3 (diagnoses, mandatory cTNM, optional pTNM; LPR3 reporting guide 2025 v5.1) and from Patobank (pathology departments, MEDRPT EDI messages via daily FTP). Coded in ICD-10 (diagnosis) plus ICD-O-3 (morphology) since 2004.
   https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf
4. **Terminologies:** SNOMED CT charter member 2007; NRC Sundhedsdatastyrelsen; Danish extension bi-annual (March/September), latest September 2025 on the August 2025 International Edition. ICD-10 via SKS (Sundhedsvæsenets Klassifikations System, Sundhedsdatastyrelsen; version numbering not found). ICD-O-3 for morphology. LOINC: DK Core has LOINC and NPU observation profiles; NPU is the lab terminology (NPU CodeSystem INT 2026-03-27 published by SDS). ATC: not found. TNM edition: not found (LPR3 requires cTNM; Nordic studies used UICC 7th). National FHIR terminology server: not yet available, in planning; Nordic shared server tx-nordics.fhir.org/fhir (HL7 Sweden-hosted, not for production).
   https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/148406293 ; https://packages.fhir.org/jurisdictions/DK ; https://hl7norway.github.io/best-practice/referat/2025-09-10-referat.html
5. **Organisations and people:** HL7 Denmark (dk-affiliate@hl7.dk, secretariat Dansk Standard), MedCom, Sundhedsdatastyrelsen. Chair sources conflict: Thea Mentz Sørensen (chair from 1 Jan 2024 per MedCom; listed 2025) and Jens Kristian Villadsen (HL7 Europe pages). Kirstine Rosenbeck Gøeg (MedCom) leads hackathon tracks.
   https://fhir.fi/en/demo2025/hl7-denmark/ ; https://hl7.eu/affiliate_dk.html ; https://hl7.dk/

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Cancerregisteret (Danish Cancer Registry), founded 1942/43, controller Sundhedsdatastyrelsen (Danish Health Data Authority), mandatory reporting since 1987; electronic since 2004. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://www.encr.eu/node/169
- Coverage: Nordic overview reports close to 100% completeness of incident solid malignancies in all Nordic registries; Danish coverage percent not separately stated (n/f). https://medicaljournalssweden.se/actaoncologica/article/view/24912
- ENCR/IACR: listed on encr.eu; member of Association of Nordic Cancer Registries (ANCR). https://www.encr.eu/node/169 ; https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: DMCG (Danske Multidisciplinære Cancer Grupper, est. 2005) run cancer-specific quality databases hosted by RKKP (Regionernes Kliniske Kvalitetsudviklingsprogram); 25 diagnosis-specific registries; annual reports published on sundhed.dk (e.g. DCCG colorectal, DBCR childhood cancer, DGCD gynaecological). https://cdn2.gopublic.dk/indenrigssundhedsmin/Media/638415267703842146/Danske%20Multidisciplin%C3%A6re%20Cancer%20Grupper.pdf ; https://informahealthcare.com/doi/full/10.1080/0284186X.2020.1820573 ; https://www.sundhed.dk/content/cms/81/4681_dccg-aarsrapport-2022_offentliggjort-version.pdf
- Screening registries: n/f as separate registries; screening data flow through RKKP databases and Patobank (pathology). n/f
- Submission format: hospital data via Landspatientregisteret LPR3 (mandatory cTNM, optional pTNM; LPR3 reporting guide 2025 v5.1); pathology via Patobank using MEDRPT EDI messages, daily FTP. https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf ; https://www.retsinformation.dk/eli/lta/2018/1049/pdf
- Variable dictionary / coding: ICD-10 diagnosis plus ICD-O-3 morphology since 2004 (1978–2003 converted); TNM mandatory since 2004, coded by clinicians under UICC 5/6/7 in 2004–2016 period; current UICC edition n/f. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://medicaljournalssweden.se/actaoncologica/article/download/24253/28421/74284
- Legal basis: Sundhedsloven and the reporting order (Bekendtgørelse om lægers anmeldelse til Cancerregisteret, 2018). https://www.retsinformation.dk/eli/lta/2018/1049/pdf
- Researcher access: Sundhedsdatastyrelsen Forskerservice (Research Services), data delivered on the Secure Research Platform (no internet); foreign researchers need a Danish data-responsible partner; Statistics Denmark hosts linked microdata. https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/research-services ; https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/research-services/the-secure-research-platform ; https://www.dst.dk/en/TilSalg/Forskningsservice/Data/Andre_Styrelser

#### (b) Public datasets
- Open statistics: eSundhed.dk cancer topic; annual report "Nye kræfttilfælde i Danmark 2024" (published 25 June 2025) with municipality tables. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638938615398782138/Nye%20kr%C3%A6fttilf%C3%A6lde%202024,%20fordelt%20p%C3%A5%20kommuner%20(udgivet%2025.%20juni%202025).pdf ; https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/media/16526/Kraefttilfaelde%202023.pdf
- NORDCAN 2.0 participant (incidence, mortality, survival, prevalence since 1943). https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- ECIS contributor: Danish Cancer Registry among ENCR registries contributing to ECIS. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Research data access body (EHDS): Sundhedsdatastyrelsen; TEHDAS2 partners: Danish Health Data Agency, Aarhus University Hospital, Central Denmark Region. https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/european-health-data-space ; https://tehdas.eu/partners/
- Quality database annual reports (RKKP/DMCG) are public on sundhed.dk. https://www.sundhed.dk/content/cms/87/16287_dbcr-aarsrapport-2022.pdf
- Synthetic datasets: n/f
- National health data catalogue: n/f (EMA catalogue lists "Danish Health Data Registries"). https://catalogues.ema.europa.eu/node/1145/data-flows-and-management

#### (c) Cancer infrastructure
- National plan: Kræftplan IV (2016, "Styrket indsats på kræftområdet"); Kræftplan V status n/f. https://www.sst.dk/-/media/Udgivelser/2016/Styrket-indsats-på-kræftområdet-–-et-fagligt-oplæg-til-Kræftplan-IV/styrket-indsats-paa-kraeftomraadet-2016-fagligt-oplaegt-til-kraeftplan-IV-2016.ashx
- Danish Comprehensive Cancer Center (DCCC), national network of regions and DMCG. https://www.regioner.dk/media/3849/danish-comprehensive-cancer-center-modelpapir.pdf
- OECI: Aarhus University Hospital joined OECI June 2023; final report and notification certificate as "Aarhus University Hospital Comprehensive Cancer Centre" (2026). Rigshospitalet, Odense: n/f. https://www.fagperson.auh.dk/siteassets/04-forskning-og-udvikling/aarhus-comprehensive-cancer-centre/nyt-fra-ccc/nyheder/2026/vigtig-international-anerkendelse/aarhus-final-report-and-notification-certificate.signed.pdf
- Genomics: Nationalt Genom Center (National Genome Center) runs national WGS programme incl. oncology patient groups (QIAGEN interpretation adopted 2023; data must stay in Denmark); national personalised medicine strategy 2021–2022. https://www.selectscience.net/article/danish-national-genome-center-selects-qiagen-for-variant-interpretation-in-oncology-genome-sequencing ; https://admin.ism.dk/Media/637616833229549022/Danish%20Strategy%20for%20personalised%20medicine%202021%202022.pdf
- 1+MG / Genome of Europe: Danish participation n/f.
- Biobank: Danish National Biobank (SSI); Denmark is BBMRI-ERIC observer, not full member (2025 report). https://www.bbmri-eric.eu/annual_report_2025_singlepages/
- Imaging infrastructure: EUCAIM Danish partner n/f (partner page lists none). https://cancerimage.eu/partners/
- EU projects: TEHDAS2 (Danish Health Data Agency, AUH, Central Denmark Region); EUCanScreen (Region Syddanmark); ECHoS Danish partner n/f; EUnetCCC Danish partner n/f; JANE-2 n/f. https://tehdas.eu/partners/ ; https://www.fhi.no/en/projects/eucanscreen/eucanscreen-list-of-participants/
- OMOP/EHDEN: EHDEN data partners Center for Surgical Science (Region Hovedstaden) and University of Southern Denmark; DARWIN EU onboarded "Danish Health Data Registries". https://www.ehden.eu/datapartners/ ; https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: Sundhedsdatastyrelsen leads EHDS implementation (regulation in force 25 March 2025; four supporting projects). https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/european-health-data-space

#### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: sundhed.dk (national portal, hosts quality database reports; patient access to records). https://www.sundhed.dk/
- EHR: Sundhedsplatformen (Epic) in Region Hovedstaden and Sjælland; other regions use Systematic Columna; chemotherapy module details n/f. n/f
- Exchange formats: MedCom EDIFACT/XML messages; pathology to Patobank via MEDRPT EDI; LPR3 reporting via SEI/XML. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/media/15228/SEI_LPR_Manual.pdf
- Structured pathology: Patobank, SNOMED-coded (Danish SNOMED pathology codes, converted to ICD-O-3 by conversion tables). https://cdn1.gopublic.dk/sundhedsdatastyrelsen/media/15733/FI%20Registrering%20Patologi.pdf
- Tumour-board/MDT software: n/f
- National cancer datasets not in FHIR: DMCG/RKKP database variable sets; LPR3 cancer-specific reporting rules. https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf
- Chemotherapy / ePrescription: FMK (Fælles Medicinkort) national medication record; hospital chemo systems n/f. n/f
- openEHR oncology: n/f
- Digital health strategy naming cancer: DMCG.dk calls for a national cancer data platform. https://cdn2.gopublic.dk/indenrigssundhedsmin/Media/638415267703842146/Danske%20Multidisciplin%C3%A6re%20Cancer%20Grupper.pdf

#### Key organisations and people
- Sundhedsdatastyrelsen (Cancerregisteret, Forskerservice, EHDS); RKKP; DMCG.dk; DCCC; Nationalt Genom Center; Kræftens Bekæmpelse (Danish Cancer Society, Registry Core Function); MedCom; Aarhus University Hospital CCC. People: n/f for named registry leads.

---
