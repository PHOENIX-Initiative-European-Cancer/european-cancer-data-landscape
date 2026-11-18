### Italy (IT)

Region: Southern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** HL7 Italia FHIR Implementation Guide (base), package `hl7.fhir.it.base`, canonical http://hl7.it/fhir, FHIR 4.0.1. Last published version 0.1.0, Public Comment ballot, 2020-06-15; CI build 0.1.1 (not authorised). Publisher HL7 Italia. Sources: https://hl7.it/fhir/base/package-list.json , https://github.com/hl7-it/base . Companion: HL7 Italia Terminology IG `hl7.fhir.it.terminology` 0.1.2, active 2025-06-16 (https://build.fhir.org/ig/hl7-it/terminology). FSE 2.0 domain IGs (lab report 0.2.0 trial-use, dossier-pharma) are built with Ministero della Salute, AgID and Sogei.
2. **Oncology FHIR IG:** not found. No HL7 Italia oncology IG, no AIRTUM FHIR work, no Italian mCODE adoption found.
3. **Registry reporting:** AIRTUM regional/provincial registries; the AIRTUM Banca Dati protocol 2020 defines flat record layouts (tracciati A–E) with ICD-O-3 topography/morphology, ICD-10 cause of death, ICCC-3 and a TNM edition field. National Registro Nazionale Tumori at the Ministry of Health (Law 29/2019; DM 1 Aug 2023), fed by regional registries; national flow format: not found. Sources: https://www.registri-tumori.it/cms/system/files/Protocollo%20Banca%20dati%20AIRTUM%202020.pdf , https://www.normattiva.it/eli/id/2019/04/05/19G00036/ORIGINAL
4. **Terminologies:** SNOMED CT: Italy not listed on https://www.snomed.org/members (checked 2026-11-18); EU co-funding for membership exists. ICD-9-CM (Italian 2007 version) for hospital discharge records (SDO); ICD-10 for ISTAT mortality (version not confirmed); ICD-O-3.2 in AIRTUM materials; TNM 8th edition in AIRTUM training (national mandate not found). LOINC Italian translation by CNR (LOINC Italia, IIT-CNR); UMLS lists Italian edition 2.75 (Aug 2023). Drug code AIC (AIFA), FHIR CodeSystem in the dossier-pharma IG (https://build.fhir.org/ig/hl7-it/dossier-pharma/CodeSystem-aifa-aic.html). National terminology server: not found.
5. **Organisations and people:** HL7 Italia, Ministero della Salute, AgID, Sogei, AIRTUM. Giorgio Cangioli (HL7 Italia, author of base and terminology IGs), Mario Sicuranza, Leonardo Alcaro (terminology IG). HL7 Italia chair: not found.

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based registries: AIRTUM network (Associazione Italiana Registri Tumori) of regional/provincial registries; 35 registries covering >44 million people, about 80% of the population (AIRTUM president, Dec 2024). https://quifinanza.it/salute/tumori-numeri-italia-2024/871401/
- AIRTUM states network coverage of about 84% of residents (2024 preliminary estimates). https://www.quotidianosanita.it/?p=134643
- National: Registro Nazionale Tumori at the Ministero della Salute, established by DPCM 3 March 2017, governed by DM 1 Aug 2023 (GU 203 of 31 Aug 2023); fed by regional registries; Ministry is data controller. https://certifico.com/sicurezza-lavoro/357-news-sicurezza/20298-decreto-1-agosto-2023
- Legal basis: Law 29/2019 "Rete nazionale dei registri dei tumori e dei sistemi di sorveglianza" (GU 5 Apr 2019). https://www.normattiva.it/eli/id/2019/04/05/19G00036/ORIGINAL
- Data submission format: AIRTUM Banca Dati protocol 2020, flat record layouts (tracciati A patient, B tumour, C optional, D population, E mortality), keys IDPZ/IDCASO; ICD-O-3 topography (ICDOT) and morphology (ICDOM), ICD-10 cause of death, ICCC-3, TNM edition field with AJCC/UICC codes. https://www.registri-tumori.it/cms/system/files/Protocollo%20Banca%20dati%20AIRTUM%202020.pdf
- Coding editions in current AIRTUM materials: ICD-O-3.2 and TNM 8th edition (course programme). https://www.registri-tumori.it/cms/system/files/PROGRAMMA%20PRELIMINARE_12_11.pdf
- Data centre: AIRTUM national database (since May 2005); each registry remains owner of its data; queried through the ITACAN interactive platform. https://registri-tumori.it/cms/system/files/NotaAirtum.pdf
- ENCR/IACR membership: Italian registries are ENCR members (rules hierarchy IARC > IACR > ENCR in AIRTUM handbook); per-registry list n/f. https://www.registri-tumori.it/PDF/AIRTUM2009HANDBOOK/Chapter_3.pdf
- Hospital/clinical registries: n/f at national level. Screening registries: Osservatorio Nazionale Screening (ONS) co-authors "I numeri del cancro". https://tg24.sky.it/salute-e-benessere/2024/12/19/tumori-casi-italia-stime-sopravvivenza-dati
- Researcher data access route: via AIRTUM database rules (registry directors own data); formal national procedure n/f. https://registri-tumori.it/cms/system/files/NotaAirtum.pdf

#### (b) Public datasets
- "I numeri del cancro in Italia" annual report (AIOM, AIRTUM, Fondazione AIOM, ONS, PASSI, SIAPeC-IAP); 2025 edition published Dec 2025, 362,100 new cases estimated for 2025. https://www.epicentro.iss.it/tumori/registri
- ITACAN: AIRTUM interactive query/analysis platform on the national database (almost 3 million cases, >1 million deaths). https://registri-tumori.it/cms/system/files/NotaAirtum.pdf
- ISS EpiCentro regional incidence/mortality/prevalence estimates. https://www.iss.it/en/tumori/-/asset_publisher/QFACMpQtWq3G/content/stime-regionali-di-incidenza-mortalit%C3%A0-e-prevalenza-per-tumore
- Mortality: ISTAT "Decessi e cause di morte", ICD-10 coded (Iris automated coding); 2023 report. https://www.istat.it/wp-content/uploads/2026/05/Report-cause-di-morte_Anno-2023.pdf
- ECIS contribution: ECIS draws on 127 registries in 32 countries (Mar 2025); Italian registry list n/f. https://ecis.jrc.ec.europa.eu/database-description
- Research data access body: Ecosistema dei Dati Sanitari (EDS) introduced by DM 31 Dec 2024; HDAB designation pending (Minister indicated Agenas; due by March 2027). https://en.ilsole24ore.com/art/from-paris-to-barcelona-with-health-pass-so-italy-prepares-eu-health-space-AIE73n9B
- Synthetic datasets: n/f. National health data catalogue: n/f.

#### (c) Cancer infrastructure
- National plan: Piano Oncologico Nazionale 2023-2027, adopted 26 Jan 2023 (State-Regions agreement), 10 M EUR per year 2023-2027; point 4.6 digitalisation in oncology. https://www.regione.calabria.it/wp-content/uploads/2023/12/piano-oncologico-nazionale.pdf
- Plan steering body (Cabina di Regia) reported not operational (FAVO 2025). https://www.quotidianosanita.it/studi-e-analisi/tumori-in-italia-4-milioni-di-persone-vivono-dopo-la-diagnosi-ma-diritti-a-rischio-per-i-ritardi-della-burocrazia-il-xviii-rapporto-favo/
- National oncology network: Alleanza Contro il Cancro (ACC), Ministry of Health network founded 2002; National Cancer Mission Hub (ECHoS) 2025; partner in EUnetCCC. https://alleanzacontroilcancro.it/category/news/
- OECI accreditation: Italian centre list n/f (61 OECI-accredited centres in Europe per undated Finnish source). https://www.tuni.fi/en/news/tays-cancer-centre-meets-rigorous-european-quality-standards
- Biobanks: BBMRI.it national node (est. 2013), 62 qualified biobanks, ISS, CNR, 19 universities, 33 research hospitals. https://www.bbmri-eric.eu/national-nodes/
- Genomics / 1+MG: Italy among 1+MG signatories (25 EU countries); national programme details n/f. https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes
- EUCAIM partners: Gemelli, IFOM, IEO, IFO-Regina Elena, CNR, Maggioli, Neuromed, San Donato, Sapienza, SYNLAB, Univ. Bari, Univ. Pisa. https://cancerimage.eu/partners/
- EHDEN/OMOP: 26 Italian data partners incl. Basilicata Cancer Registry, Fondazione Istituto Nazionale dei Tumori, Policlinico Sant'Orsola, Parma, Bambino Gesù, Ca' Granda, Besta, San Matteo, Poliambulanza, San Donato. https://www.ehden.eu/datapartners/
- Health data space: EDS (DM 31 Dec 2024), to be implemented by June 2026, joining MyHealth@EU and HealthData@EU. https://www.noze.it/insights/ehds-secondary-use-2027/
- Other EU projects (EOSC4Cancer, UNCAN.eu, canSERV, JANE, CraNE, EUCanScreen, TEHDAS2): n/f for Italian partner lists.

#### (d) Digital, non-FHIR
- FSE 2.0: DM 7 Sept 2023 (amended DM 11 Nov 2025) defines documents incl. anatomia patologica reports; FHIR gateway run by Sogei; CDA R2 documents. https://www.noze.it/insights/fse-2-0-gateway-sogei/
- Structured pathology reporting: Emilia-Romagna regional project for structured oncology pathology/biomolecular report in HL7 CDA R2 with shared checklists (2015). https://bur.regione.emilia-romagna.it/area-bollettini/bollettini-in-lavorazione/novembre-periodico-parte-seconda-1a-quindicina.2015-11-03.1285922986/approvazione-del-progetto-referto-strutturato-di-anatomia-patologica-e-biomolecolare-relativo-alle-malattie-neoplastiche/allegati.pdf
- Pathology report preservation format: PDF or HL7 CDA2 (Emilia-Romagna). https://poloarchivistico.regione.emilia-romagna.it/conservazione/documentazione/modelli-per-la-realizzazione-dei-sip/documenti/sanitari/referto_v1-0.pdf/@@download/file
- Tumour board software: Gemelli rectal-cancer MDT platform integrated with hospital IT (2022). https://publires.unicatt.it/en/publications/an-it-platform-supporting-rectal-cancer-tumor-board-activities-im/
- Regional oncology network platform: Rete Oncologica Campana web platform tracking GOM (multidisciplinary) take-in-charge and molecular tests. https://agendadigitale.eu/sanita/salute-femminile-lesperienza-della-rete-oncologica-campana
- Teleconsultation: INT Milano "Ambulatorio Virtuale" (Ticuro Reply), >2,000 oncology teleconsultations by 2023. https://www.reply.com/it/newsroom/news/premio-innovazione-digitale-sanita-2023
- Drug coding: AIC (AIFA) codes; chemotherapy prescription systems n/f. https://build.fhir.org/ig/hl7-it/dossier-pharma/CodeSystem-aifa-aic.html
- Hospital discharge coding ICD-9-CM 2007; ICD-10 for mortality; LOINC Italian translation by CNR (UMLS edition 2.75, Aug 2023). https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/LNC-IT-IT/metadata.html
- openEHR oncology archetypes: n/f. Patient portal oncology content: n/f.

#### Key organisations and people
- Ministero della Salute (Registro Nazionale Tumori, EDS); AgID; Sogei (FSE gateway); Agenas (likely HDAB); ISS; ISTAT.
- AIRTUM (registri-tumori.it); AIOM; ONS; FAVO; Alleanza Contro il Cancro (president Ruggero De Maria per ACC site). https://alleanzacontroilcancro.it/en/category/news/page/7/
- BBMRI.it; CNR (LOINC Italia); HL7 Italia (Giorgio Cangioli, Mario Sicuranza, Leonardo Alcaro). https://build.fhir.org/ig/hl7-it/terminology

---
