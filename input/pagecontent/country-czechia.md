### Czechia (CZ)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** "Czech National FHIR R4 Core and Base Implementation Guide STU 1" (HL7 Czech Base and Core FHIR IG), package hl7.fhir.cz.core, canonical https://hl7.cz/fhir/core, FHIR 4.0.1. Published 1.0.0 (STU 1, trial-use) 2026-07-29, "based on EU Base R4 v2.0.0"; earlier 0.3.0 2026-03-06; ci-build 1.1.0 (draft 2026-08-06, depends on hl7.fhir.eu.base 2.0.1, hl7.fhir.eu.extensions.r4 1.3.1, hl7.fhir.eu.laboratory 2.0.0, hl7.fhir.eu.mpd 1.0.0, ihe.pharm.mpd.r4). Publisher HL7 Czech Republic; national standards body NCEZ (Národní centrum elektronického zdravotnictví). Companion hl7.fhir.cz.terminology 0.3.0 (release, 2026-07-27; ci 0.4.0).
   https://hl7.cz/fhir/core/package-list.json ; https://hl7.cz/fhir/ ; https://build.fhir.org/ig/HL7-cz/cz-core/en/index.html ; https://raw.githubusercontent.com/HL7-cz/cz-core/main/sushi-config.yaml ; https://hl7.cz/terminology/package-list.json ; https://api.simplifier.net/jurisdictions/CZ
2. **Oncology FHIR specifications:** no oncology IG. hl7.cz lists Base/Core, Terminology, imaging and lab reports and orders, general order, HDR, patient summary, ambulatory report, EMS record, eHealth API. The Shared Health Record (SZZ) ci-build (0.0.1) contains screening artefacts (lung-cancer interpretation code system, mammography, colorectal screening, prostate MRI observations). No mCODE dependency.
   https://hl7.cz/fhir/ ; https://build.fhir.org/ig/HL7-cz/szz/artifacts.html ; https://build.fhir.org/ig/HL7-cz/szz/CodeSystem-cz-lung-cancer-interpretation-cs.html
3. **Cancer registry reporting standard:** Národní onkologický registr (NOR), run by ÚZIS ČR. Reporting via DASTA data interfaces: clinical "Incidence novotvaru" report and pathology/cytology report; a July 2026 ÚZIS methodology on automated NOR record completion still references the DASTA interfaces. Clinical report carries MKN-O-3 topography/morphology and pTNM values.
   https://www.uzis.cz/res/file/projekty/ui/metodika-automaticke-doplnovani-zaznamu-nor.pdf ; https://www.uzis.cz/res/file/registry/nor/nor-metodika-010-20180817-1.pdf ; https://kozni.lf1.cuni.cz/file/5664/NOR.pdf
4. **Terminologies:** SNOMED CT: member since 2012 (Ministry of Health / ÚZIS; licensing https://mlds.ihtsdotools.org/cz), National Release Centre at ÚZIS NCMNK since July 2020; Czech translation in progress (100,602 concepts in group 1 as of Aug 2025, translation milestones to Dec 2025); national edition release: not found. ICD-10: MKN-10-CZ update effective 1 Jan 2026 (ÚZIS). ICD-O: MKN-O-3.2 (2018 update) used in NOR (cases from 2019/2020). TNM: 8th edition (CZ translation 2017); Czech TNM 9 edition planned mid-2026, NOR reporting per TNM 9 from 1 Jan 2027. LOINC: Czech translation is a goal in the NCEZ interoperability strategy (June 2025). ATC / national drug code: not found (SÚKL not verified). Terminology server: national server "in development" (NCEZ strategy; Simplifier survey).
   https://www.snomed.org/members/czech-republic ; https://www.uzis.cz/res/file/klasifikace/ncmnk/snomed-ct-cr-analyticka-zprava.pdf ; https://www.uzis.cz/res/file/akce/20250923-klasifikon/1-06-kruzik.pdf ; https://www.uzis.cz/res/file/klasifikace/mkn/mkn-10-rozdilovy-listek-tabelarni-2020-2026.pdf ; https://www.uzis.cz/res/file/akce/20250923-klasifikon/1-05-zvolsky.pdf ; https://ncez.mzcr.cz/sites/default/files/media-documents/02%20EZ_Strategie%20Interoperability_v2_6.2025.pdf
5. **Organisations and people:** NCEZ (national standards body), HL7 Czech Republic, ÚZIS ČR (NOR, NCMNK, SNOMED NRC). Hynek Kružík (Technical Lead HL7 CZ, main cz-core GitHub contributor); SNOMED appointed representatives Irena Molinari, Miroslav Zvolský (ÚZIS).
   https://api.simplifier.net/jurisdictions/CZ ; https://api.github.com/repos/HL7-cz/cz-core/contributors ; https://www.snomed.org/members/czech-republic

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Národní onkologický registr (NOR), run by ÚZIS ČR since 1976, within NZIS (Act 372/2011); member of IACR, cooperates with ENCR; coverage 100% (ECIS). https://www.uzis.cz/res/file/registry/nor/nor-metodika-010-20180817-1.pdf ; https://ecis.jrc.ec.europa.eu/pdf/Prevalence_List_of_cancer_registries.pdf
- Submission: DASTA data interfaces (clinical "Incidence novotvaru" report; pathology/cytology report); 2026 methodology on automated completion of NOR records from NRHZS and other NZIS data. https://www.uzis.cz/res/file/projekty/ui/metodika-automaticke-doplnovani-zaznamu-nor.pdf
- Variable dictionary: MKN-10 (CZ update effective 1 Jan 2026), MKN-O-3.2 (2018 update) for cases from 2019/2020, TNM 8 (CZ 2017); TNM 9 CZ edition planned mid-2026 with NOR reporting from 1 Jan 2027. https://www.uzis.cz/res/file/akce/20250923-klasifikon/1-05-zvolsky.pdf ; https://kozni.lf1.cuni.cz/file/5664/NOR.pdf
- Screening registries: National Screening Centre (NSC, ÚZIS) data portal built on NRHZS plus NOR and programme registers (mammography, colorectal, cervical); lung-cancer early detection register planned in PREV-IS; screening-unit status via eSTATUS in eREG. https://www.nzip.cz/data/media/20251001-integrace-dat/majek.pdf ; https://prevon.uzis.cz/res/file/prezentace/2024-10/16-chloupkova.pdf
- Clinical/other: "centrová léčba" data interface v1.1 (Nov 2025) for specialised (centre) cancer treatment; Czech Myeloma Group registry (EHDEN partner). https://www.uzis.cz/res/file/registry/centrova-lecba/centrova-lecba-datove-rozhrani-1-1.pdf ; https://www.ehden.eu/datapartners/
- Researcher access: NZIS data requests via ÚZIS (analyzy@uzis.cz), one-off analyses list and synthetic-data request form on NZIP; NZIS data-sharing concept document. https://www.nzip.cz/data/nzis-open/koncepce-sdileni-dat-nzis.pdf ; https://www.nzip.cz/data/nzis-open/synteticka-data-zadost-vystup.docx

#### (b) Public datasets
- SVOD portal (svod.cz) for cancer epidemiology visualisation; NZIP open data on neoplasms (incidence by region, survival dataset from anonymised NOR records, 2026 edition). https://www.nzip.cz/data/nor/metodicke-popisy/Otevrena-data-NR-07-03-novotvary-preziti-2026-01.pdf ; https://www.nzip.cz/data/nor/metodicke-popisy/Datovy-souhrn-NR-07-05-novotvary-kraje-incidence-2026-01.pdf
- Synthetic datasets: ÚZIS synthetic NZIS data service (request form, published outputs). https://www.nzip.cz/data/nzis-open/synteticka-data-popis-sablona.docx
- Screening data: NSC data portal nsc.uzis.cz/data; data.nsc@uzis.cz. https://nzis-open.uzis.cz/prezentace-2022/chloupkova-nzis-open-12_2022.pdf
- ECIS: Czech national registry contributes (1994–2018 incidence listed). https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Research data access body: ÚZIS (NZIS); TEHDAS2 partners MoH and Masaryk University. https://tehdas.eu/tehdas2/partners/

#### (c) Cancer infrastructure
- Plan: Národní onkologický plán ČR 2030 (approved 22 Jun 2022), action plans 2022–24 and 2025–27; RRF component 6.2 (8.54 bn CZK) incl. Czech Oncology Institute. https://mzd.gov.cz/narodni-onkologicky-plan-cr-2030/
- Network: Komplexní onkologická centra (KOC) plus HOC/DOC; summary list of highly specialised centres valid 23 Jul 2025; KOC in all regions from Jan 2026; care coordinators mandatory from 2026 (Věstník MZ 11/2025). https://mzd.gov.cz/category/agendy-ministerstva/zdravotni-sluzby-agendy-ministerstva/centra-vysoce-specializovane-pece/seznam-center-vysoce-specializovane-pece-v-cr/ ; https://mzd.gov.cz/?p=226325
- OECI: Masarykův onkologický ústav (MOÚ, Brno) OECI-accredited (Clinical Cancer Centre 2017; reported top-tier accreditation); South Moravian oncology network aiming at OECI CCN. https://mou.cz/en/about-mmci/t1632 ; https://www.mou.cz/en/south-moravian-oncology-network/t2248
- Genomics: 1+MG original signatory (2018); GDI node work at Masaryk University (ÚVT/CEITEC, 2022–2026); Czech Genomic Platform oversees 1+MG; NCMG complementary to ELIXIR-CZ. https://www.muni.cz/en/research/projects/68918 ; https://www.vyzkumne-infrastruktury.cz/en/?p=8148
- Biobank: BBMRI.cz, 9 biobanks, coordinated by MOÚ, director Roman Hrstka; oncology-focused; digital pathology expertise; all biobanks on BBMRI-ERIC Federated Platform. https://www.bbmri-eric.eu/national-nodes/czech-republic/
- Imaging/EUCAIM: Masaryk University. https://cancerimage.eu/partners/
- EU projects: CraNE (FN Motol), EUCanScreen (ÚZIS), TEHDAS2 (MoH, Masaryk University), ECHoS hub planned. https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/
- OMOP: EHDEN partners Institute of Rheumatology, OAKS Consulting, Czech Myeloma Group. https://www.ehden.eu/datapartners/
- National health data space: NZIS (ÚZIS) as national hub; NCEZ e-health strategy 2025–2035. https://mzd.gov.cz/tiskove-centrum-mz/narodni-strategie-elektronickeho-zdravotnictvi-cr-2025-2035-prinese-moderni-propojeny-a-bezpecny-e-health-system/

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR/portal: Act 325/2021 on electronic healthcare; NCEZ portal eZdraví / NPEZ and EZKarta app (EZKarta 2.0 planned May 2026); eRecept (SÚKL) accepted in 10 EU countries; eŽádanka since Jan 2026 (voluntary). https://www.e15.cz/finexpert/servis/stat-spustil-portal-ezdravi-pacienti-uvidi-dokumentaci-lekari-vystavi-ezadanky-1429882 ; https://ppo.mzcr.cz/upload/files/jednani-nrez-22-4-2026-zapis-nrez-22-4-2026-6a05501390948.pdf
- Exchange formats: DASTA (national data standard) for NOR and lab/pathology reports; NOR DASTA code tables. https://ciselniky.dasta.mzcr.cz/hypertext/200940/hypertext/m61nor.pdf
- Structured pathology: pathology/cytology NOR report via DASTA; digital pathology in BBMRI.cz. https://www.bbmri-eric.eu/national-nodes/czech-republic/
- Tumour-board/MDT software: n/f. Chemotherapy prescribing: centre-treatment data interface (ÚZIS). openEHR oncology: n/f.
- Strategy items naming cancer: NOP 2030 reform "quality of screening programmes"; NSC; AI methodology for NOR automation. https://mzd.gov.cz/wp-content/uploads/2024/12/Akcni-plan-implementace-NOPL-2025-2027_P1_vvyhodnocem-2023.pdf

#### Key organisations and people
- ÚZIS ČR: Ladislav Dušek (director; NOR and NOP presentations), Jan Mužík (NOR), Ondřej Májek (NSC screening), Miroslav Zvolský (classifications, SNOMED). https://www.linkos.cz/files/pro_odborniky/napl_onko_prog/sled_predikce_onko/Forum/2025-04/2-Prednaska_Du-scaron-ek_OnkoForum.pdf ; https://www.uzis.cz/res/file/akce/20250923-klasifikon/1-05-zvolsky.pdf
- NCEZ: Petr Foltýn (director). https://mzd.gov.cz/budoucnost-ezkarty-zpravy-zadanky-i-komunikace-s-lekarem-rika-reditel-narodniho-centra-elektronickeho-zdravotnictvi-petr-foltyn/
- MOÚ Brno (OECI, BBMRI.cz: Roman Hrstka); Masaryk University (GDI, EUCAIM, TEHDAS2); HL7 CZ (Hynek Kružík).

---
