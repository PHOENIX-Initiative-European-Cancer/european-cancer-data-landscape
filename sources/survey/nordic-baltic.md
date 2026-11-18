# National FHIR, oncology and terminology landscape: Nordic and Baltic countries

Survey for the editors of the HL7 Europe Common Cancer Data Model IG (ECCDM). Compiled 2026-11-18 from web search and direct page downloads; sources from 2024 onward preferred. Items marked "not found" could not be verified from a primary source.

## Denmark

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

## Sweden

1. **National base IG:** "Swedish Base Profiles Implementation Guide", package `hl7se.fhir.base`, FHIR R4 (4.0.1), v1.1.0 (built 2025-05-20; v2.0.0 in development), publisher HL7 Sweden, canonical http://hl7.se/fhir/ig/base. Profiles: Patient, Practitioner, PractitionerRole, Organization, HealthcareService; stated as not compatible with EU Core. E-hälsomyndigheten publishes national guides (National Medication List) on Simplifier.
   https://hl7.se/fhir/ig/base/1.1.0/ ; https://get-ig.org/hl7se.fhir.base/1.1.0 ; https://hl7europe-test.azurewebsites.net/wp-content/uploads/2025/02/01_eusni2025_sweden.pdf
2. **Oncology FHIR specifications:** not found. INCA (RCC platform for Cancer Registry, IPÖ, quality registers) uses an openEHR data store; no FHIR oncology IG located.
   https://svfp.se/media/biki5rbx/slutrapport_openehrv12.pdf ; https://packages.fhir.org/jurisdictions/SE
3. **Cancer registry reporting:** Cancerregistret at Socialstyrelsen; six Regional Cancer Centres receive A-reports (clinicians) and B-reports (laboratories) via INCA forms, Socialstyrelsen's form, or electronic transmission of lab diagnostic statements, code them in ICD-O/3 and deliver annually. Coding handbook "Kodning i cancerregistret 2026".
   https://cancercentrum.se/syd/regional-cancer-centres/knowledge-based-healthcare/cancer-registry/ ; https://www.socialstyrelsen.se/contentassets/6b4e25c21ce446f2a9d850ef43daa294/2026-5-10247.pdf
4. **Terminologies:** SNOMED CT charter member 2007; NRC Socialstyrelsen; Swedish extension May/November, latest November 2025. ICD-10-SE 13th version for 2026 (published January 2026) plus national fördjupningskoder 2026; ICD-11 for cause-of-death from 2027. ICD-O/3.2 (2019) with Socialstyrelsen modifications. TNM: latest UICC edition per Socialstyrelsen (edition number not stated). KVÅ for procedures. LOINC, ATC: not found. Terminology servers: national FHIR terminology server in production (survey), Inera Terminologitjänst (FHIR Terminology API, fhir.inera.se); Nordic tx-nordics.fhir.org/fhir hosted by HL7 Sweden.
   https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/256901154 ; https://www.socialstyrelsen.se/contentassets/b4f71ee88ef74195824e5fa9cca7cf89/2026-1-9989.pdf ; https://www.socialstyrelsen.se/contentassets/ad9a86523e93449097d5136a8989f561/2024-1-8918.pdf ; https://fhir.inera.se/ig/IneraFHIRTemplate/1.0.1/terminology.html
5. **Organisations and people:** HL7 Sweden, E-hälsomyndigheten (standards body, National Group for Standardization), Socialstyrelsen, Inera, RCC i samverkan. Arvid Thunholm (chair, HL7 Sweden WG base profiles); Mattias Colliander (HL7 Sweden board, terminology server); Daniel Karlsson (E-hälsomyndigheten, Nordic terminology cooperation). Board chair: not verified.
   https://build.fhir.org/ig/HL7Sweden/basprofiler-r4/ ; https://hl7norway.github.io/best-practice/docs/FHIR-faglig-forum/presentasjon/2025-09-10-term-servers-intro.pdf

## Norway

1. **National base IG:** no-basis, package `hl7.fhir.no.basis`, FHIR R4, v2.2.2 (bugfix 2025-03-26), publisher HL7 Norway, canonical http://hl7.no/fhir/; 19 approved base profiles (Feb 2025), no must-support; recommended standard in Helsedirektoratet's Referansekatalogen; survey rates it "widely used".
   https://simplifier.net/hl7norwayno-basis ; https://packages.fhir.org/hl7.fhir.no.basis ; https://www.helsedirektoratet.no/standarder/norske-basisprofiler-for-hl7-fhir ; https://hl7europe-test.azurewebsites.net/wp-content/uploads/2025/02/05_eusni2025_norway.pdf
2. **Oncology FHIR specifications:** not found. No Kreftregisteret FHIR IG located.
   https://packages.fhir.org/jurisdictions/NO
3. **Cancer registry reporting:** Kreftregisteret, part of Folkehelseinstituttet (FHI) since 1 January 2024. Clinical reporting via the KREMT web service or EHR systems built on the registry's message specifications; paper abolished spring 2017. Pathology: copies of over 350,000 pathology reports per year as e-helse "Svar" messages v1.3/v1.4 (AppRec 1.0/1.1), selected by NORPAT codes; spec revised 04.12.2025.
   https://www.fhi.no/en/cancer/reporting/kremt-cancer-registrys-electronic-reporting-service/ ; https://www.fhi.no/contentassets/bb8d17623751483099eb6321111b868b/spesifikasjon---elektronisk-innsending-av-patologiremisser-1.pdf ; https://fhi.no/om/fhi/omrader/kreftregisteret
4. **Terminologies:** SNOMED CT member since 1 January 2017 (30th member); NRC Helsedirektoratet; about 10 extension releases per year. ICD-10 Norwegian edition updated annually ("Nytt i 2026", FinnKode); ICD-11 upgrade strategy drafted; NCSP/NCMP/NCRP. NORPAT for pathology. ICD-O-3, TNM edition, LOINC (NPU in use, to be published on tx-nordics), ATC: not found. National FHIR terminology server: in development.
   https://www.snomed.org/news/norway-joins-snomed-international-as-our-30th-member ; https://www.helsedirektoratet.no/digitalisering-og-e-helse/helsefaglige-kodeverk/snomed-ct/snomed-ct-i-norge ; https://www.helsedirektoratet.no/veiledere/kodeveiledning-regler-og-veiledning-for-klinisk-koding-i-spesialisthelsetjenesten
5. **Organisations and people:** Helsedirektoratet (standards body, absorbed Direktoratet for e-helse 2024), HL7 Norway (best-practice site), FHI/Kreftregisteret. Øyvind Aassve (HL7 Norway, Sykehuspartner, affiliate presenter, profile portal contact); Line Andreassen Sæle (styreleder HL7 Norge, 2025).
   https://hl7norway.github.io/best-practice/ ; https://www.helsedirektoratet.no/om-oss/rad-og-utvalg/standardiseringsutvalet/_/attachment/inline/03002456-798d-4951-b803-d003f50171b5:75bfd5a71b2a2e8d9edc1ad5ca2524a4ef3d51c3/M%C3%B8te%202-25%20Referat.pdf

## Finland

1. **National base IG:** "Finnish Base Profiles", package `hl7.fhir.fi.base` (also `.r4`/`.r4b`), v2.0.0 STU 2, FHIR R4, active 2025-10-05, official HL7 Finland standard (OID 1.2.246.777.11.2025.4), publisher HL7 Finland, canonical https://hl7.fi/fhir/finnish-base-profiles; no must-support; no R5 plan.
   https://hl7.fi/fhir/finnish-base-profiles/ ; https://get-ig.org/hl7.fhir.fi.base/2.0.0
2. **Oncology FHIR specifications:** not found. Kanta FHIR profiles (PHR, medication list) on Simplifier; no oncology profile set.
   https://www.kanta.fi/en/fhir-technology-and-kanta
3. **Cancer registry reporting:** Finnish Cancer Registry is THL's register maintained by the Cancer Society of Finland; statutory notification of every case or strong suspicion by hospitals, physicians and pathology, cytology and haematology laboratories. Current transmission format: not found (older literature: electronic transfers from large hospitals and labs plus manual forms). Variables include ICD-O-3 topography, morphology, behaviour, stage.
   https://cancerregistry.fi/cancer-information-notification/ ; https://finngen.gitbook.io/finngen-handbook/finngen-data-specifics/red-library-data-individual-level-data/what-phenotype-files-are-available-in-sandbox-1/other-registers/finnish-cancer-registry-detailed-cancer-data
4. **Terminologies:** SNOMED CT member 2018 (THL, 36th member); Finnish edition published each December (year of latest not stated); subset translation only. ICD-10: THL Tautiluokitus ICD-10 on the national code server (version not found); ICD-11 planned from 2028. National code server (Koodistopalvelu, content THL, operations Kela; SOAP/XML retired 13.1.2026 with v9.2), not available in FHIR. LOINC, ATC, ICD-O edition, TNM edition: not found. National FHIR terminology server: not yet available, in planning.
   https://www.snomed.org/members/finland ; https://conf.spaces.snomed.org/wiki/spaces/MCC/pages/131343642/Finland ; https://hl7.fi/fhir/finnish-base-profiles/terminology.html ; https://www.kanta.fi/documents/d/guest/koodistopalvelun-rajapinnat-ja-liittymisohje-1_8 ; https://packages.fhir.org/jurisdictions/FI
5. **Organisations and people:** HL7 Finland (technical committee), THL, Kela/Kanta, Cancer Society of Finland. Mikael Rinnetmäki (contact on fi.base IG, mikael@sensotrend.com).
   https://hl7.fi/fhir/finnish-base-profiles/ImplementationGuide-hl7.fhir.fi.base.json

## Iceland

1. **National base IG:** none ("not yet available"). Standards body Stafræn heilsa (Digital Health, under Ministry of Health, operational 2 January 2026). FHIR R4 and R5 in limited use; specifications in development for prescriptions/pharmacy and allergy intolerance, based on European IGs.
   https://packages.fhir.org/jurisdictions/IS ; https://island.is/s/stafraen-heilsa
2. **Oncology FHIR specifications:** not found.
3. **Cancer registry reporting:** Icelandic Cancer Registry (Krabbameinsskrá), founded 1954, operated by the Icelandic Cancer Society's research centre as one of the Directorate of Health's (Embætti landlæknis) health registries under Act 41/2007; mandatory reporting; coding follows IARC/ENCR rules. Transmission format: not found.
   https://www.krabb.is/rannsoknasetur/en/activities/about-icr/ ; https://www.laeknabladid.is/media/2024-06/f02.pdf
4. **Terminologies:** SNOMED CT member since September 2011; Directorate of Health holds national licence; used in pathology, microbiology, virology, immunology. ICD-10 Icelandic translation (1996), current editions 2014, published on SKAFL.is; NCSP listed. ICD-O-3 (NORDCAN recoding), TNM, LOINC, ATC: not found. National FHIR terminology server: in development.
   https://www.snomed.org/members/iceland ; https://island.is/en/classification-system-in-health-services/icd-10 ; https://island.is/flokkunarkerfi-i-heilbrigdisthjonustu/skafl.is
5. **Organisations and people:** Stafræn heilsa (director Sigurður Þórarinsson), Embætti landlæknis, Krabbameinsfélagið (Laufey Tryggvadóttir, registry). HL7 affiliate or FHIR maintainer: not found.
   https://island.is/s/stafraen-heilsa/frett/sigurdur-thorarinsson-skipadur-forstoedumadur-stafraennar-heilsu ; https://medicaljournalssweden.se/actaoncologica/article/view/24912

## Estonia

1. **National base IG:** "Estonian Base Implementation Guide" (EEBase), package `ee.fhir.base` 2.0.0 (6 Nov 2025, trial-use; must-support removed), FHIR R5 (5.0.0), publisher HL7 Estonia, canonical https://fhir.ee/base, contact fhir@tehik.ee. Three-level profiling (international, Estonian base, system-specific); TIS resources also on fhir.tehik.ee.
   https://build.fhir.org/ig/HL7EE/ig-ee-base ; https://packages.fhir.org/ee.fhir.base
2. **Oncology FHIR specifications:** "VJL – Vähiandmete juhtimislaud" (cancer data dashboard), package `ee.fhir.vjl` 0.1.0, draft (2026-10-09), FHIR R5, publisher TEHIK, canonical https://fhir.ee/vjl; depends on ee.fhir.base 2.0.0, ee.fhir.mpi 1.5.0, ee.fhir.spd; no mCODE dependency; profile EEVJLCancerDiagnosis; project (Tartu University Hospital and partners) aims to automate submission to the cancer registry. Registry data standard implemented: not stated.
   https://build.fhir.org/ig/TEHIK-EE/ig-ee-vjl/ ; https://sisu.ut.ee/estcan/cancer-data-dashboard/
3. **Cancer registry reporting:** Estonian Cancer Registry (vähiregister), controller Tervise Arengu Instituut (TAI). Statutory cancer notification (vähiteatis) submitted on paper, electronically or via the X-Road data exchange layer; 2025 draft regulation sets 30-day deadline. ICD-O-3 for topography and morphology since 2008; ICD-10 for publication.
   https://www.riigiteataja.ee/akt/123052023056.pdf ; https://en.tai.ee/images/Teatise_vormistamise_juhend.pdf ; https://en.tai.ee/en/r-and-d/registers/estonian-cancer-registry
4. **Terminologies:** SNOMED CT member January 2010; NRC TEHIK; Estonian edition URI http://snomed.info/sct/11000181102. RHK-10 (Estonian ICD-10; version not found). LOINC Estonian linguistic variant (Estonian Society for Clinical Chemistry; UMLS lists v2.77, 2024-02-27). TNM, ATC: not found. National FHIR terminology server: Ontoserver hosted by TEHIK, in production, over 400 value sets plus SNOMED CT EE+INT, publishes under https://fhir.ee/; endpoint URL not found; described in ee.fhir.ts IG (draft 1.0.0).
   https://build.fhir.org/ig/TEHIK-EE/TerminologyServices ; https://www.snomed.org/members/estonia ; https://loinc.org/?p=7910
5. **Organisations and people:** TEHIK (fhir@tehik.ee, snomed@tehik.ee), HL7 Estonia (info@hl7.ee), TAI. Named IG maintainers: not found. Igor Bossenko (TalTech) publishes on Estonian CDA-to-FHIR migration; TEHIK role not confirmed.
   https://fhir.ee/base/contact.html

## Latvia

1. **National base IG:** none. Ministry of Health decides standards; SPKC maintains ICD-10; Latvijas Digitālās veselības centrs (LDVC) established 2025 as digital health authority; NVD operates e-veselība (Cabinet Regulation No. 134). FHIR R4B primary; systems use generic FHIR without IGs; discharge summary spec is CDA (NVD.EVK.CDA.3.09 v1.1).
   https://packages.fhir.org/jurisdictions/LV ; https://lvportals.lv/dienaskartiba/385601-latvijas-digitalas-veselibas-centrs-pirmaja-darbibas-gada-paveikts-butisks-darbs-digitalas-veselibas-attistiba-2026 ; https://www.varam.gov.lv/lv/media/46103/download
2. **Oncology FHIR specifications:** not found. Survey cites "oncology registry" as a FHIR use case without a published spec. Since 1 January 2024 institutions must submit the cancer patient card in e-veselība.
   https://packages.fhir.org/jurisdictions/LV ; https://vmnvd.gov.lv/lv/media/28572/download
3. **Cancer registry reporting:** oncology part of "Ar noteiktām slimībām slimojošu pacientu reģistrs", run by SPKC; data from NVD/e-veselība (cancer patient card) and monthly transfers; ICD-10 C00–C97; reporting to ENCR/IARC; manual collection reported in 2024. Technical format: not found.
   https://statistika.spkc.gov.lv/Resources/PX/Databases/Health/Metadati/ONKO_Registra_metadati_en.html ; https://www.lsm.lv/raksts/zinas/latvija/20.08.2024-veza-registrs-vel-nepabeigts-un-nepilnigs.a565719/
4. **Terminologies:** SNOMED CT member since January 2026; NRC SPKC; roadmap to 2030; SNOMED GPS used for cross-border and lab exchange. SSK-10 (ICD-10, SPKC; version not found; SSK-11 under consideration). LOINC and UCUM planned. ICD-O-3, TNM, ATC: not found. National FHIR terminology server: in production per survey; operator and URL not found.
   https://www.snomed.org/members/latvia ; https://lvportals.lv/dienaskartiba/395031-snomed-ct-palidzes-veidot-vienotu-klinisko-zinasanu-telpu-latvija-2026 ; https://likumi.lv/ta/id/264943
5. **Organisations and people:** Ministry of Health, SPKC, NVD, LDVC. Named FHIR or oncology spec maintainers: not found.

## Lithuania

1. **National base IG:** "Lithuanian Base Implementation Guide" (LTBase), package `lt.hl7.fhir.base` 0.3.0 (DSTU 1 draft, "not ready for production"), FHIR R5 (5.0.0), canonical https://hl7.lt/fhir/base, published via HL7 Lithuania registry (hl7.lt, GitHub HL7LT) by the Lithuanian Medical Library. Legacy national ESPBI system (Registrų centras) uses DSTU1 Atom feeds (SKL01–03) and an eLab FHIR IG with ESPBI identifiers.
   https://hl7.lt/fhir/base/0.3.0/en/index.html ; https://hl7.lt/ ; https://specialistas-pub.esveikata.lt/dp/elab/iframe/fhir-ig/StructureDefinition-lt-patient-definitions.html
2. **Oncology FHIR specifications:** ADP early-diagnosis programme IGs: `lt.hl7.fhir.lung` (LDCT screening, Lung-RADS v2022), `lt.hl7.fhir.colorectal`, `lt.hl7.fhir.cervical`, `lt.hl7.fhir.breast`, `lt.hl7.fhir.prostate`; all 0.0.1 CI-build drafts (2026-09), FHIR R5, publisher Lithuanian Medical Library; depend on lt.hl7.fhir.base, lt.hl7.fhir.lab (pathology report, ICD-O-3 morphology, prostate pTNM, AJCC grade), lt.hl7.fhir.eu and hl7.fhir.eu.base-r5 0.1.0. No mCODE dependency. They implement national screening datasets, not the cancer registry standard.
   https://build.fhir.org/ig/HL7LT/ig-lt-lung/en/index.html ; https://build.fhir.org/ig/HL7LT/ig-lt-colorectal/en/terminology.html ; https://build.fhir.org/ig/HL7LT/ig-lt-lab/en/terminology.html
3. **Cancer registry reporting:** Lithuanian Cancer Registry (Vėžio registras) run by Nacionalinis vėžio institutas (NVI); primary source is form Nr. 090/a (notice of first-diagnosed oncological disease); NVI's 2025 report states registration is now fully electronic after system integrations; ICD-O-3 for topography/morphology.
   https://nvi.lt/wp-content/uploads/2026/04/2-priedas.-NVI_Ataskaita_2025_26-02-26.pdf ; https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
4. **Terminologies:** SNOMED CT charter member 2007; NRC Lithuanian Library of Medicine (Ministry of Health); 40,000 concepts translated 2015. TLK-10-AM (ICD-10-AM) used since 2019 as interim; edition not found; TLK-11 mapping planned. LOINC and ICD-O-3 used in lab IG; ATC: not found; TNM edition: not found. Terminology server: https://tx.hl7.lt/fhir/ (HL7 Lithuania); national terminology server adaptation for TLK-11 planned.
   https://snomed.org/snomed-in-action/lithuanian-nrc-library-of-medicine ; https://e-seimas.lrs.lt/rs/legalact/TAD/e1ba28a055e911f0a19dcea0bcc863ad/ ; https://build.fhir.org/ig/HL7LT/ig-lt-lab/en/terminology.html
5. **Organisations and people:** Lithuanian Medical Library (IG publisher, SNOMED NRC), HL7 Lithuania (hl7.lt), Registrų centras (ESPBI), NVI. Named maintainers: not found.

## Method note

Web-fetch subagents returned no reports; page content came from direct curl downloads (packages.fhir.org jurisdiction pages, package registry, IG JSON/HTML) and web search. The packages.fhir.org jurisdiction pages reflect the Firely/HL7 State of FHIR surveys 2025/2026. Raw downloads are in `/private/tmp/claude-501/-Users-thome-code-fhir-profiling-cancer-common/3cc04596-744d-4990-addb-ce34993d093b/scratchpad/fetched/`.
