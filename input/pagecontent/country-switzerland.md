### Switzerland (CH)

Region: DACH and Benelux. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **Base IG.** CH Core (R4), package `ch.fhir.ig.ch-core`, FHIR 4.0.1, canonical http://fhir.ch/ig/ch-core/ImplementationGuide/ch.fhir.ig.ch-core. Last STU release 6.0.0 (STU 6, 2025-12-16); 7.0.0-ballot published 2026-06-10, STU ballot 4 Aug to 30 Sep 2026. Publisher HL7 Switzerland. https://fhir.ch/ig/ch-core/6.0.0/index.html ; https://fhir.ch/ig/ch-core/index.html
2. **Oncology.** CH CRL (Cancer Registration Law) IG, package `ch.fhir.ig.ch-crl` 0.9.0, STU Draft, FHIR R4, publisher Bundesamt für Gesundheit (BAG), generated 2022-02-04; specifies the "Austauschformat KRG" exchange format (cancer report logical model, FHIR document, profiles for patient, diagnosis, TNM, procedures), built on CH Core; terminology page lists NKRS code systems (ICD-O-3 behaviour, grade, laterality, TNM stage group, Ann Arbor, Binet). mCODE reference: not found. https://fhir.ch/ig/ch-crl/index.html ; https://fhir.ch/ig/ch-crl/terminology.html . No other oncology IG on fhir.ch found.
3. **Registry standard.** Krebsregistrierungsgesetz in force 1 Jan 2020; reports go to the cantonal cancer registries and the Kinderkrebsregister; the Nationale Krebsregistrierungsstelle (NKRS) is run by the NICER foundation, Zurich, mandated since 2018. Format: "Austauschformat KRG", FHIR-based, developed by BAG; normative spec released 8 Jan 2020 (PDF 10 Jan 2020), use case 1a (embedded PDF plus minimal data) and 1b (structured data, first tranche of 30 variables); adoption voluntary; BAG offers FHIR test-file validation. NKRS data structure: variable lists v1.5, "Einführung Datenstruktur" v1.1. https://www.bag.admin.ch/de/datenformat-krebsregistermeldung ; https://www.nkrs.ch/de/meldepflicht/informationen-fuer-it-partner ; https://www.nkrs.ch/de/ueber-uns ; https://www.nkrs.ch/de/downloads
4. **Terminologies.** SNOMED CT member since January 2016, NRC eHealth Suisse; Swiss Extension released each June/July and December (June 2025, Dec 2025) (https://www.snomed.org/members/switzerland ; https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/424738850). ICD-10-GM used for hospital coding, maintained by BFS; current year version: not found. CHOP 2026 in force 1 Jan 2026 (https://ckan.opendata.swiss/dataset/schweizerische-operationsklassifikation-chop10). ICD-O-3 used by NKRS; edition: not found. TNM edition: not found. LOINC: not found. CH Term 3.4.0 (STU, 2026-06-10) carries Swiss code systems and value sets (https://fhir.ch/ig/ch-term/index.html). Terminology server: https://tx.fhir.ch/r4 , HL7 Switzerland (listed in the FHIR tx-servers registry https://fhir.github.io/ig-registry/tx-servers.json); no national government terminology server, eHealth Suisse position paper recommends one (https://www.e-health-suisse.ch/payload/api/documents/file/Positionspapier_Basisterminologien_V1.pdf).
5. **People.** CH Core managed by HL7 Switzerland TC FHIR (tc@hl7.ch); top GitHub contributors Oliver Egger (ahdis) and Michaela Ziegler (https://github.com/hl7ch/ch-core). CH CRL owner BAG, Abteilung Prävention nichtübertragbarer Krankheiten (krebsregistrierung@bag.admin.ch); named editors: not found.

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: cantonal/regional cancer registries (13 per 2025 report; 15 covering about 94% in 2015) plus the Kinderkrebsregister (founded 1976, Bern); coordinated nationally by the Nationale Krebsregistrierungsstelle (NKRS), run by the NICER foundation (Zurich) under EDI mandate since 2018; full coverage mandatory since the KRG took effect 1 Jan 2020. https://www.nkrs.ch/de/ueber-uns ; https://heise.de/-10269136 ; https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/switzerland-2015/organization-and-governance/health-information-management
- ENCR members: cantonal registries incl. Graubünden/Glarus, Neuchâtel/Jura, Ostschweiz, Ticino, Valais, Vaud. https://encr.eu/encr-members-contact-list?page=17
- Screening registries: cantonal screening programmes (mammography, colorectal) coordinated by Swiss Cancer Screening; registry data linked with screening programmes per NKRS. https://www.nkrs.ch/de/die-krebsregistrierung-kurz-erklaert/registrierte-daten
- Legal basis: Krebsregistrierungsgesetz (KRG) and Krebsregistrierungsverordnung (KRV), in force 1 Jan 2020; reporting within 4 weeks. https://www.bag.admin.ch/de/krebserkrankungen-meldepflicht-und-informationspflicht ; https://www.swissinfo.ch/eng/sci-tech/health_swiss-to-register-all-cancer-cases-from-2020/45459952
- Submission format: "Austauschformat KRG" (BAG, FHIR-based, released 8 Jan 2020, 30 structured variables, voluntary) alongside PDF/paper reporting; NKRS national data structure v1.5 variable lists (Basisdaten, Zusatzdaten Erwachsene, Zusatzdaten Kinder), "Einführung Datenstruktur v1.1"; ICD-O-3 and TNM editions: n/f. https://www.bag.admin.ch/de/datenformat-krebsregistermeldung ; https://www.nkrs.ch/de/downloads
- Data access: NKRS provides anonymised basic data and authorisation-requiring data to researchers (pages "Anfrage anonymisierte Daten", "Anfrage bewilligungspflichtige Daten"); NKRS also delivers data to BFS. https://www.nkrs.ch/de/forschung/anfordern-anonymisierter-grundlagendaten ; https://www.nkrs.ch/de/forschung/zugang-zu-bewilligungspflichtigen-daten

#### (b) Public datasets
- Open statistics: NKRS "Statistiken zu Krebs", Krebsmonitoring/Krebsbericht, Kennzahlen zu Diagnose und Therapie (e.g. breast 2020–2022, prostate 2020–2023); BFS cancer statistics. https://www.nkrs.ch/ ; https://www.bfs.admin.ch/bfs/en/home/statistics/health/surveys/ke.html
- Research data access: SPHN/BioMedIT federated dataset of >800,000 patients incl. oncology; Swiss Cancer Institute (ex SAKK) onboarded to SPHN 2025. https://sphn.ch/2026/02/03/new-institutions-onboarded_2025/ ; https://bioalps.org/sphn-releases-clinical-data-from-800000-patients/
- ECIS contribution, synthetic datasets, national health data catalogue: n/f (DigiSanté programme working on secondary-use data space). https://www.digisante.admin.ch/dam/de/sd-web/hbuj5RvqfFlY/20250501_Case%20study%20Health%20services%20research_UniSant%C3%A9%20V1.0.pdf

#### (c) Cancer infrastructure
- National plan/institute: Nationale Strategie gegen Krebs (ended), NCD strategy; Swiss Cancer Institute (formerly SAKK) runs the clinical trial network (22 centres) and SCORED real-world data. https://sphn.ch/network/projects/driver-projects/project-page_swiss-personalized-oncology/
- CCCs/OECI: n/f.
- Genomics/personalised health: SPHN (phase 3, 2025–2028, CHF 20.7 M per Wikipedia mirror), driver project Swiss Personalized Oncology (SPO), SVIP-O variant platform. https://sphn.ch/network/projects/driver-projects/project-page_swiss-personalized-oncology/ ; https://isb-sib.ch/news/a-key-ingredient-of-swiss-precision-oncology-svip-o-goes-live
- Biobanks: Swiss Biobanking Platform (SBP) is BBMRI-ERIC national node; Switzerland full member since June 2023 (SERI). https://www.bbmri-eric.eu/national-nodes/switzerland/
- Paediatrics: SwissPedHealth (national data stream) with nested SwissPedCancer project testing automated transfer from clinical data warehouses to the registry. https://www.researchprotocols.org/2026/1/e87007
- OMOP: five Swiss EHDEN data partners (Basel, Bern, Geneva, Vaud incl. Unisanté). https://ehden.eu/datapartners/
- EU projects (EUCAIM, EUnetCCC, JANE-2, TEHDAS2): Swiss participation n/f; Switzerland is in Clinnova with Luxembourg, France, Germany. https://www.lih.lu/en/news/page/6/
- Research data infrastructure: SPHN/BioMedIT; DigiSanté (federal digital health programme 2025–2034) and planned Swiss Health Data Space. https://www.digisante.admin.ch/dam/de/sd-web/9zrTcNIxTGda/Schlussbericht%20Standardisierung%20im%20SwissHDS%20mit%20FHIR.pdf

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: EPD (elektronisches Patientendossier), IHE XDS based, CDA documents; oncology content: n/f. https://www.e-health-suisse.ch/
- Registry exchange: BAG "Austauschformat KRG" (FHIR); legacy PDF-based reporting (use case 1a embeds PDF reports). https://www.bag.admin.ch/de/datenformat-krebsregistermeldung
- Registry software: cantonal registries' joint software project failed (secondary source: heise 2025). https://heise.de/-10269136
- Coding: ICD-10-GM and CHOP (BFS Medizinische Klassifikationen), CHOP 2026 in force 1 Jan 2026. https://ckan.opendata.swiss/dataset/schweizerische-operationsklassifikation-chop10
- Semantic framework: SPHN semantic interoperability framework (RDF-based) used by Swiss Personalized Oncology core dataset. https://sphn.ch/network/projects/driver-projects/project-page_swiss-personalized-oncology/
- Tumour-board software, structured pathology, openEHR: n/f.

#### Key organisations and people
- BAG Abteilung Prävention nichtübertragbarer Krankheiten (KRG, Austauschformat; krebsregistrierung@bag.admin.ch); NKRS/NICER (Zurich, info@nkrs.ch); Kinderkrebsregister (Bern); BFS; Swiss Cancer Institute; SPHN; SBP (Christine Currat / Christine Joye named by BBMRI-ERIC); eHealth Suisse (SNOMED NRC); HL7 Switzerland (Oliver Egger, Michaela Ziegler, ahdis). https://www.nkrs.ch/de/ueber-uns ; https://www.bbmri-eric.eu/national-nodes/switzerland/ ; https://github.com/hl7ch/ch-core

---
