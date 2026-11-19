# Non-FHIR digital cancer landscape: Italy, Spain, Portugal, Luxembourg, Greece, Malta, Cyprus

Survey date: 2026-11-18; verification pass 2026-11-19 (see south-verification-log.md). Bullet facts with one source URL each; "n/f" = not found in this survey. France is excluded (handled separately). Cross-country sources used for several countries: EUCAIM partner list https://cancerimage.eu/partners/ ; EHDEN data partners https://www.ehden.eu/datapartners/ ; BBMRI-ERIC national nodes https://www.bbmri-eric.eu/national-nodes/ ; ECIS data protocol 2026 https://www.encr.eu/sites/default/files/Data_call/ECIS-data-protocol_2026.pdf ; 1+MG policy page (25 EU countries plus UK and Norway signed the 2018 declaration) https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes .

---

## Italy

### (a) Cancer registries
- Population-based registries: AIRTUM network (Associazione Italiana Registri Tumori) of regional/provincial registries; 35 registries covering >44 million people, about 80% of the population (AIRTUM president, Dec 2024). https://quifinanza.it/salute/tumori-numeri-italia-2024/871401/
- AIRTUM states network coverage of about 84% of residents (2024 preliminary estimates). https://www.quotidianosanita.it/?p=134643
- National: Registro Nazionale Tumori at the Ministero della Salute, established by DPCM 3 March 2017, governed by DM 1 Aug 2023 (GU 203 of 31 Aug 2023); fed by regional registries; Ministry is data controller. https://certifico.com/sicurezza-lavoro/357-news-sicurezza/20298-decreto-1-agosto-2023
- Legal basis: Law 29/2019 "Rete nazionale dei registri dei tumori e dei sistemi di sorveglianza" (GU 5 Apr 2019). https://www.normattiva.it/eli/id/2019/04/05/19G00036/ORIGINAL
- Data submission format: AIRTUM Banca Dati protocol 2020, flat record layouts (tracciati A patient, B tumour, C optional, D population, E mortality), keys IDPZ/IDCASO; ICD-O-3 topography (ICDOT) and morphology (ICDOM), ICD-10 cause of death, ICCC-3, TNM edition field with AJCC/UICC codes. https://www.registri-tumori.it/cms/system/files/Protocollo%20Banca%20dati%20AIRTUM%202020.pdf
- Coding editions in current AIRTUM materials: ICD-O-3.2 and TNM 8th edition (course programme). https://www.registri-tumori.it/cms/system/files/PROGRAMMA%20PRELIMINARE_12_11.pdf
- Data centre: AIRTUM national database (since May 2005); each registry remains owner of its data; queried through the ITACAN interactive platform. https://registri-tumori.it/cms/system/files/NotaAirtum.pdf
- ENCR/IACR membership: Italian registries are ENCR members (rules hierarchy IARC > IACR > ENCR in AIRTUM handbook); the ENCR member contact list is JavaScript-rendered and could not be read (NEEDS BROWSER). https://www.registri-tumori.it/PDF/AIRTUM2009HANDBOOK/Chapter_3.pdf
- Hospital/clinical registries: n/f at national level. Screening registries: Osservatorio Nazionale Screening (ONS) co-authors "I numeri del cancro". https://tg24.sky.it/salute-e-benessere/2024/12/19/tumori-casi-italia-stime-sopravvivenza-dati
- Researcher data access route: via AIRTUM database rules (registry directors own data); formal national procedure n/f. https://registri-tumori.it/cms/system/files/NotaAirtum.pdf

### (b) Public datasets
- "I numeri del cancro in Italia" annual report (AIOM, AIRTUM, Fondazione AIOM, ONS, PASSI, SIAPeC-IAP); 2025 edition published Dec 2025, 362,100 new cases estimated for 2025. https://www.epicentro.iss.it/tumori/registri
- ITACAN: AIRTUM interactive query/analysis platform on the national database (almost 3 million cases, >1 million deaths). https://registri-tumori.it/cms/system/files/NotaAirtum.pdf
- ISS EpiCentro regional incidence/mortality/prevalence estimates. https://www.iss.it/en/tumori/-/asset_publisher/QFACMpQtWq3G/content/stime-regionali-di-incidenza-mortalit%C3%A0-e-prevalenza-per-tumore
- Mortality: ISTAT "Decessi e cause di morte", ICD-10 coded with Iris (ICD-10 version 2016 from 2016 data, version 2019 from 2020 data, https://www.ISTAT.it/it/files//2023/04/NOTAINFORMATIVABridgeCoding2020.pdf) (verified 2026-11-19); 2023 report. https://www.istat.it/wp-content/uploads/2026/05/Report-cause-di-morte_Anno-2023.pdf
- ECIS contribution: 41 Italian registries contribute incidence data to ECIS (e.g. Friuli Venezia Giulia 1995-2020, Puglia 2013-2018, Milan 2013-2017, Bergamo 2007-2018), per the ECIS contributing-registries list (archived copy, data as of 2025-09) https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19).
- Research data access body: Ecosistema dei Dati Sanitari (EDS) introduced by DM 31 Dec 2024; HDAB designation pending (Minister indicated Agenas; due by March 2027). https://en.ilsole24ore.com/art/from-paris-to-barcelona-with-health-pass-so-italy-prepares-eu-health-space-AIE73n9B
- Synthetic datasets: n/f. National health data catalogue: n/f.

### (c) Cancer infrastructure
- National plan: Piano Oncologico Nazionale 2023-2027, adopted 26 Jan 2023 (State-Regions agreement), 10 M EUR per year 2023-2027; point 4.6 digitalisation in oncology. https://www.regione.calabria.it/wp-content/uploads/2023/12/piano-oncologico-nazionale.pdf
- Plan steering body (Cabina di Regia) reported not operational (FAVO 2025). https://www.quotidianosanita.it/studi-e-analisi/tumori-in-italia-4-milioni-di-persone-vivono-dopo-la-diagnosi-ma-diritti-a-rischio-per-i-ritardi-della-burocrazia-il-xviii-rapporto-favo/
- National oncology network: Alleanza Contro il Cancro (ACC), Ministry of Health network founded 2002; National Cancer Mission Hub (ECHoS) 2025; partner in EUnetCCC. https://alleanzacontroilcancro.it/category/news/
- OECI accreditation: 16 Italian centres on the OECI accredited/designated list as of 2026-11-19: INT Milano, IEO Milano, INOC Candiolo, IOV Veneto, INT Pascale Napoli, Regina Elena Roma, San Matteo Pavia, Spedali Civili Brescia, San Martino Genova, AUSL Reggio Emilia, CRO Aviano, Humanitas, San Raffaele, CROB Basilicata, Sacro Cuore Don Calabria, Giovanni Paolo II Bari (https://accreditation.oeci.eu/); the ACC network ran a Ministry-funded OECI programme (https://read.qxmd.com/read/27098181/participation-of-italian-cancer-centres-of-the-alleanza-contro-il-cancro-acc-in-the-organisation-of-european-cancer-institutes-oeci-accreditation-and-designation-program-a-successful-first-national-initiative) (verified 2026-11-19).
- Biobanks: BBMRI.it national node (est. 2013), 62 qualified biobanks, ISS, CNR, 19 universities, 33 research hospitals. https://www.bbmri-eric.eu/national-nodes/
- Genomics / 1+MG: Italy among 1+MG signatories (25 EU countries); national programme details n/f. https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes
- EUCAIM partners: Gemelli, IFOM, IEO, IFO-Regina Elena, CNR, Maggioli, Neuromed, San Donato, Sapienza, SYNLAB, Univ. Bari, Univ. Pisa. https://cancerimage.eu/partners/
- EHDEN/OMOP: 26 Italian data partners incl. Basilicata Cancer Registry, Fondazione Istituto Nazionale dei Tumori, Policlinico Sant'Orsola, Parma, Bambino Gesù, Ca' Granda, Besta, San Matteo, Poliambulanza, San Donato. https://www.ehden.eu/datapartners/
- Health data space: EDS (DM 31 Dec 2024), to be implemented by June 2026, joining MyHealth@EU and HealthData@EU. https://www.noze.it/insights/ehds-secondary-use-2027/
- CraNE partners: Alleanza Contro il Cancro, Ministry of Health, IDI (https://crane4health.eu/partners/); EUCanScreen: ISS and CPO Turin (https://eucanscreen.eu/partners/); TEHDAS2: Ministry of Health, Univ. Bologna, AOU Parma, Bologna University Hospital, ACC, ULSS 4 Veneto, Regione Emilia-Romagna, Università Cattolica (https://tehdas.eu/partners/); ECHoS National Cancer Mission Hub: ACC (https://cancermissionhubs.eu/hubs/) (verified 2026-11-19). EOSC4Cancer, UNCAN.eu, canSERV, JANE partner lists: pages blocked or 404 (NEEDS BROWSER).

### (d) Digital, non-FHIR
- FSE 2.0: DM 7 Sept 2023 (amended DM 11 Nov 2025) defines documents incl. anatomia patologica reports; FHIR gateway run by Sogei; CDA R2 documents. https://www.noze.it/insights/fse-2-0-gateway-sogei/
- Structured pathology reporting: Emilia-Romagna regional project for structured oncology pathology/biomolecular report in HL7 CDA R2 with shared checklists (2015). https://bur.regione.emilia-romagna.it/area-bollettini/bollettini-in-lavorazione/novembre-periodico-parte-seconda-1a-quindicina.2015-11-03.1285922986/approvazione-del-progetto-referto-strutturato-di-anatomia-patologica-e-biomolecolare-relativo-alle-malattie-neoplastiche/allegati.pdf
- Pathology report preservation format: PDF or HL7 CDA2 (Emilia-Romagna). https://poloarchivistico.regione.emilia-romagna.it/conservazione/documentazione/modelli-per-la-realizzazione-dei-sip/documenti/sanitari/referto_v1-0.pdf/@@download/file
- Tumour board software: Gemelli rectal-cancer MDT platform integrated with hospital IT (2022). https://publires.unicatt.it/en/publications/an-it-platform-supporting-rectal-cancer-tumor-board-activities-im/
- Regional oncology network platform: Rete Oncologica Campana web platform tracking GOM (multidisciplinary) take-in-charge and molecular tests. https://agendadigitale.eu/sanita/salute-femminile-lesperienza-della-rete-oncologica-campana
- Teleconsultation: INT Milano "Ambulatorio Virtuale" (Ticuro Reply), >2,000 oncology teleconsultations by 2023. https://www.reply.com/it/newsroom/news/premio-innovazione-digitale-sanita-2023
- Drug coding: AIC (AIFA) codes; chemotherapy prescription systems n/f. https://build.fhir.org/ig/hl7-it/dossier-pharma/CodeSystem-aifa-aic.html
- Hospital discharge coding ICD-9-CM 2007; ICD-10 for mortality; LOINC Italian translation by CNR (UMLS edition 2.75, Aug 2023). https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/LNC-IT-IT/metadata.html
- openEHR oncology archetypes: n/f. Patient portal oncology content: n/f.

### Key organisations and people
- Ministero della Salute (Registro Nazionale Tumori, EDS); AgID; Sogei (FSE gateway); Agenas (likely HDAB); ISS; ISTAT.
- AIRTUM (registri-tumori.it); AIOM; ONS; FAVO; Alleanza Contro il Cancro (president Ruggero De Maria per ACC site). https://alleanzacontroilcancro.it/en/category/news/page/7/
- BBMRI.it; CNR (LOINC Italia); HL7 Italia: President Stefano Lotti, Vice-President Giorgio Cangioli, CTO Leonardo Alcaro (board elected 26 June 2024, https://www.hl7.it/direttivo) (verified 2026-11-19); terminology IG authors Cangioli, Sicuranza, Alcaro https://build.fhir.org/ig/hl7-it/terminology

---

## Spain

### (a) Cancer registries
- Population-based: regional registries run by autonomous communities, federated in REDECAN (Red Española de Registros de Cáncer), incl. RETI (childhood). https://seom.org//images/ESTUDIO_REGISTRO_DE_CANCER_BASE_POBLACIONAL.pdf
- REDECAN 2024 incidence estimates use 12 consolidated population registries. https://www.infocop.es/wp-content/uploads/2025/01/ESTIMACIONES-DE-LA-INCIDENCIA-CANCER-ESPANA-2024.pdf
- Coverage: about 25% of Spain's population (2024 study); older REDECAN figure ~20%. https://www.redaccionmedica.com/autonomias/catalunya/20150727/salud-creara-un-registro-catalan-del-cancer/340126_0.html
- ENCR: Spanish registries participate in ENCR (e.g., Registro de Madrid follows ENCR recommendations). https://www.comunidad.madrid/node/74791
- Legal basis: regional decrees (e.g., Castilla y León registry manual follows ENCR/IARC, IARC TP 40, behaviour /3 only; Catalonia: Decret 11/2017 for Lleida, decree for a Catalonia-wide registry in prior public consultation March 2025, https://www.catalannews.com/society-science/item/estimated-42851-malignant-tumors-diagnosed-in-catalonia-in-2024). National: Real Decreto 568/2024 (BOE-A-2024-12379) creates the Red Estatal de Vigilancia en Salud Pública; the royal decree for a Sistema de Vigilancia del Cáncer was in public consultation and not yet published (https://www.sanidad.gob.es/normativa/docs/CPP_RD_VIGILANCIA_CANCER.pdf ; https://www.sanidad.gob.es/fr/gabinete/notasPrensa.do?id=6458) (verified 2026-11-19). https://www.saludcastillayleon.es/en/enfermedades-problemas-salud/cancer/registro-poblacional-cancer.files/96813-Manual%20de%20Procedimiento%20%20Registro%20de%20Base%20Poblacional%20de%20C%C3%A1ncer%20de%20Castilla%20y%20Le%C3%B3n.pdf
- Variable dictionary: REDECAN/SEOM proposed variable set v1 (March 2023): ICD-O-3, TNM edition field 5th-8th, cT/pM/stage; first edition covers stomach, colorectal, lung, ovary, prostate. https://seom.org//images/ESTUDIO_REGISTRO_DE_CANCER_BASE_POBLACIONAL.pdf
- Submission format (XML/CSV): n/f. Hospital tumour registries: long tradition (Catalonia, Lleida, Madrid RTMAD). https://www.quironsalud.com/es/comunicacion/actualidad/hospital-universitario-quironsalud-madrid-incorpora-registr
- Catalonia: population registries in Girona, Tarragona and Lleida (2017) are used to estimate Catalonia-wide incidence (42,851 cases estimated for 2024); a Catalonia-wide registry decree was in prior public consultation in March 2025. https://wsm.ics.gencat.cat/epicancerlleida/assets/pdf/estadistiques-cancer-catalunya-2024-2025.pdf (verified 2026-11-19)
- Screening registries: Red de Programas de Cribado de Cáncer; Ministry situation reports 2025 (breast, colorectal). https://www.sanidad.gob.es/areas/promocionPrevencion/cribado/cribadoCancer/cancerMama/docs/informeDeSituacionCribadoCancerMama_2025.pdf
- Researcher access: REDECAN provides results to authorities and the scientific community; formal access route n/f. https://www.ciberisciii.es/media/914374/dossier-redecan-20072017.pdf

### (b) Public datasets
- "Las cifras del cáncer en España" (SEOM + REDECAN, annual; 2024: 286,664 new cases). https://seom.org/images/Informe_Cifras_Cancer_2024.pdf
- REDECAN website redecan.org publishes estimates; INE mortality data. https://www.infocop.es/wp-content/uploads/2025/01/ESTIMACIONES-DE-LA-INCIDENCIA-CANCER-ESPANA-2024.pdf
- Ministry BDCAP prevalence of malignant neoplasms (primary care). https://www.sanidad.gob.es/estadEstudios/estadisticas/estadisticas/estMinisterio/SIAP/Prevalencia_neoplasias_malignas_BDCAP_Series_3.pdf
- AECC "Más Datos Cáncer" platform, 69 indicators. https://www.contraelcancer.es/sites/default/files/2025-10/Comunicado_Datos_Autonomias.pdf
- Research data access body: HDAB-ES project (Ministerio de Sanidad sole beneficiary). https://www.sanidad.gob.es/areas/saludDigital/proyectoHDAB-ES/home.htm
- Espacio Nacional de Datos de Salud (ENDS): network of regional platforms, 70 M EUR, announced Jan 2026. https://digital.gob.es/content/dam/portal-mtdfp/comunicacion/comunicacion_ministro/2026/2025-01-29/NdPEspaciosdedatos.pdf
- Screening open data: ENSE 2023 early-detection monograph. https://www.sanidad.gob.es/gl/gabinete/notasPrensa.do?id=6947
- ECIS: 15 Spanish registries contribute incidence (Albacete, Asturias, Balearic Islands, Basque Country 1986-2019, Canary Islands, Castellón 2004-2020, Ciudad Real, Cuenca, Girona 1994-2020, Granada, La Rioja, Murcia 1990-2020, Navarra, Tarragona 1980-2019, Castilla y León-Salamanca), archived ECIS list https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19). Synthetic datasets: n/f.

### (c) Cancer infrastructure
- Estrategia en Cáncer del SNS, updated version approved by CISNS 24 Feb 2021. https://www.sanidad.gob.es/areas/calidadAsistencial/eventosJornadas/Jornada/RANCancer.htm
- OECI accredited/designated centres in Spain as of 2026-11-19: 12 de Octubre, Clínica Universidad de Navarra, ICO, Clínic Barcelona, IVO Valencia, Fundación Jiménez Díaz, IOCS Sant Joan de Reus, Vall d'Hebron (https://accreditation.oeci.eu/) (verified 2026-11-19); CUN accredited May 2025, Bellvitge/ICO Oct 2025. https://cancercenter.cun.es/en/cancer-center-clinica-european-accreditation-oncology-care ; https://idibell.cat/en/2025/10/bellvitge-health-campus-provides-comprehensive-cancer-care-to-two-million-people-following-the-model-that-europe-aims-to-deploy-by-2030/
- Genomics: IMPaCT-Genómica (7.25 M EUR 2021-2023), Plan de Medicina Personalizada 5P (100 M EUR); 1+MG signatory. https://www.sanidad.gob.es/ca/gabinete/notasPrensa.do?id=6006
- Biobanks: Spain observer in BBMRI-ERIC (2021), full membership agreement published BOE 29 May 2025; ISCIII Plataforma de Biobancos y Biomodelos as national node. https://boe.es/boe/dias/2025/05/29/pdfs/BOE-A-2025-10681.pdf
- EUCAIM: central hub technically coordinated at UPV/La Fe (Ignacio Blanquer); ~30 Spanish partners (SAS, BSC, CRG, CIBER, Clínic, ISCIII, La Fe, Quibim, SERMAS, CSIC, Univ. Valencia). https://cancerimage.eu/partners/
- EHDEN/OMOP: 27 Spanish data partners incl. Institut Català d'Oncologia, Vall d'Hebron, 12 de Octubre, La Fe, Sant Pau, Hospital del Mar, Virgen Macarena. https://www.ehden.eu/datapartners/
- Red Nacional Interoperable de datos en cáncer (CIBERONC, IRB, VHIO, INCLIVA, FISEVI), standards HL7 FHIR, OMOP, HealthDCAT-AP. https://www.impacto.contraelcancer.es/wp-content/uploads/2026/08/Red-Nacional-Interoperable.pdf
- CraNE partner: Institut Català d'Oncologia (https://crane4health.eu/partners/); ECHoS National Cancer Mission Hub exists for Spain (https://cancermissionhubs.eu/hubs/); canSERV lists EurOPDX nodes in Spain (https://www.canserv.eu/partners/) (verified 2026-11-19). EUCanScreen and TEHDAS2 Spanish partners not shown in fetched text; UNCAN.eu, JANE: pages blocked (NEEDS BROWSER).

### (d) Digital, non-FHIR
- HCDSNS (national EHR): clinical reports (discharge, emergency, imaging) in CDA; no dedicated oncology report; CMDIC v6.0 adds pathology report. https://www.sanidad.gob.es/gl/profesionales/hcdsns/contenidoDoc/situacionActualHCDSNS.htm ; https://www.sanidad.gob.es/organizacion/sns/planCalidadSNS/docs/ARS.pdf
- SEOM: EHRs in most of the SNS do not allow automated oncology workflow; ENDS "embryonic" (2025 commentary). https://www.redaccionmedica.com/secciones/sanidad-hoy/espacio-de-datos-sanitarios-el-ministerio-de-sanidad-va-solo-tarde-y-mal-1144
- Coding: CIE-10-ES 6th ed. 2026; CIE-O-3.2 from 2026-01-01; SNOMED CT Spanish edition; LOINC Spain 2.77. https://www.sanidad.gob.es/estadEstudios/estadisticas/normalizacion/
- Terminology server: Servidor de Terminologías de Referencia del SNS. https://www.sanidad.gob.es/areas/saludDigital/semanticaClinica/factoriaRecursos/servTerm.htm
- Structured pathology: SEAP publishes consensus reporting protocols (e.g. colorectal carcinoma, https://www.seap.es/documents/Publicaciones/Protocolos/guias-clinicas/consenso-recomendaciones/Carcinoma_colo_rectal.pdf) and ICCR datasets exist in Spanish (lung v3 2017, kidney v1.1 2018, https://www.iccr-cancer.org/wp-content/uploads/2022/02/ICCR-Lung-3rd-edn-v3-0-bookmarkform-ES.pdf); national adoption figures n/f (verified 2026-11-19). Chemotherapy e-prescribing (Oncofarm/Farmis) deployment data, tumour-board software, openEHR oncology: n/f.
- Upcoming national digital health law adapting to EHDS (consultation to 20 Oct 2025). https://www.cuatrecasas.com/es/spain/farmaceutico-sanitario/art/hacia-una-digitalizacion-de-la-salud

### Key organisations and people
- Ministerio de Sanidad (Área de Recursos Semánticos; HDAB-ES; ENDS); ISCIII (biobank platform, IMPaCT); AEMPS.
- REDECAN; SEOM; AECC Observatorio; CIBERONC; HL7 Spain (chair Francisco Pérez). https://hl7.eu/affiliate_es.html
- EUCAIM: Ignacio Blanquer (UPV / IIS La Fe). https://www.cesga.es/wp-content/uploads/2025/05/20250618-EHDS-and-RIs.pdf

---

## Portugal

### (a) Cancer registries
- RON (Registo Oncológico Nacional): single national electronic platform created by Lei 53/2017, in force 1 Jan 2018; mandatory registration of all new diagnoses (public, social, private) within 9 months; annual updates on stage, treatment, vital status; diagnoses coded with ICD version in force. https://diariodarepublica.pt/dr/detalhe/lei/53-2017-107692693
- Former regional registries ROR-Sul, ROR-Centro, RORENO, RORA (Azores) and the paediatric registry integrated into RON. https://comum.rcaap.pt/bitstream/10400.26/29608/1/Ron%2002.07.2019.pdf
- Coverage: all tumours in the resident population (national, 100%). https://recipp.ipp.pt/bitstreams/2d6bfbcf-bde1-4e0f-bd69-ee3a79381f07/download
- Coordinator: Maria José Bento (IPO Porto, Epidemiology Service). https://observador.pt/2025/12/29/portugal-registou-mais-de-60-mil-novos-casos-de-cancro-em-2022/
- Coding: ICD-O-3 (RORENO; IPO Porto registry listed in EMA catalogue). https://catalogues.ema.europa.eu/print/pdf/node/966
- Submission format and variable dictionary: n/f (ron.min-saude.pt unreachable, no Wayback snapshot; no portaria found in Diário da República); access is via a platform on the Rede Informática da Saúde with role profiles per Lei 53/2017 art. 5 (https://diariodarepublica.pt/dr/detalhe/lei/53-2017-107692693) (verified 2026-11-19); SPMS procured a new RON solution under PRR, awarded 2 May 2025. https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/a3e1ea2f-e50d-3f30-815e-c6a058d260d7
- Timeliness: 2022 incidence published Dec 2025; backlog reported (some hospitals years behind). https://24noticias.sapo.pt/tecnologia/artigos/auroramed-a-ia-portuguesa-que-quer-por-o-registo-oncologico-em-dia
- ENCR/IACR: RON designated as Portugal's representative in a European joint action on registry harmonisation (2024). https://www.noticiasaominuto.com/pais/2092628/registados-2685-casos-de-cancro-pediatrico-em-10-anos
- Screening registries: SiiMA Rastreios, the SPMS screening information system (maintenance tender 2026, https://ted.europa.eu/en/notice/238605-2026/pdf), plus BI-CSP (verified 2026-11-19); 2024 report: breast coverage 61%, colorectal 32.5%. https://www.dnoticias.pt/2026/2/4/480090-cobertura-do-rastreio-dos-cancros-colon-e-recto-e-colo-do-utero-ainda-longe-da-meta/
- Researcher access route: Lei 53/2017 limits access to defined profiles; regional registrars may extract aggregated non-identified reports; no public researcher application procedure found (verified 2026-11-19).

### (b) Public datasets
- RON incidence report (2022 data: 60,954 cases, 579.6/100,000) and survival report (2019 cohort, 66% five-year survival, May 2026). https://www.rtp.pt/noticias/pais/sobrevivencia-ao-cancro-em-portugal-atinge-66-mas-desigualdades-persistem_n1742152
- DGS planned an electronic tool to publish screening activity data (2024). https://theportugalnews.com/news/2024-02-04/standardising-cancer-screening-costs/85696
- Research data access body: HealthData@PT (SPMS, EU4Health, from 1 Nov 2023, 48 months) preparing the national HDAB and dataset catalogue (D6.1, Oct 2025). https://www.spms.min-saude.pt/wp-content/uploads/2025/10/D6.1-National-dataset-catalogue-requirements-and-specifications.pdf
- ECIS contribution: four regional registries (Azores 1997-2016, Central region 2008-2010, North region 2000-2010, South region 2000-2012); no RON national series yet in ECIS (archived list) https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19). Open data portal (Transparência SNS) oncology datasets: n/f. Synthetic data: n/f.

### (c) Cancer infrastructure
- Estratégia Nacional de Luta contra o Cancro, horizonte 2030, approved by Despacho 13227/2023, prepared by DGS/PNDO; four pillars. https://vlex.pt/vid/despacho-n-13227-2023-973680823
- OECI accredited centres in Portugal as of 2026-11-19: IPO Coimbra, IPO Lisboa, IPO Porto (https://accreditation.oeci.eu/) (verified 2026-11-19); Porto.CCC (IPO Porto + i3S) re-accredited Comprehensive Cancer Centre to 2027; IPO Lisboa hosts the national Tumour Biobank. https://www.i3s.up.pt/pccc.php ; https://core.ac.uk/download/427722367.pdf
- CCI4EU consultancy at IPO Porto (OECI-led). https://oncodaily.com/voices/373816
- Biobanks: Portugal joined BBMRI-ERIC; GIMM national node, coordinating Biobanco.pt network (GIMM, Champalimaud, Católica, INSA, CHAIN|NMS). https://gimm.pt/?p=12407
- Genomics: 1+MG signatory; INSA (Astrid Vicente) co-authored 1+MG maturity model pilot. https://zenodo.org/records/8135894/files/ESHG%2023_Poster%20MLM_Final.pdf
- EUCAIM partners: Champalimaud Foundation, CHU Santo António, Liga Portuguesa Contra o Cancro (Centro). https://cancerimage.eu/partners/
- EHDEN/OMOP: 11 Portuguese data partners incl. Hospital do Espírito Santo Évora, CHU Coimbra, Hospital da Luz, Hospital de Santarém. https://www.ehden.eu/datapartners/
- EUnetCCC: Portugal has a pilot centre (Nov 2025). https://observador.pt/2025/11/13/rede-europeia-de-centros-de-cancro-vai-garantir-acesso-aos-mesmos-tratamentos-em-todos-os-paises-da-ue-incluindo-portugal/
- CraNE partner: Ministry of Health (https://crane4health.eu/partners/); EUCanScreen: Ministry of Health and IPO Porto (https://eucanscreen.eu/partners/); ECHoS: Portugal recognised as National Cancer Mission Hub (https://cancermissionhubs.eu/hubs/) (verified 2026-11-19). EOSC4Cancer, UNCAN.eu, canSERV, JANE, TEHDAS2 Portuguese partners: n/f (pages blocked or not listed).

### (d) Digital, non-FHIR
- E-prescription: PEM (Prescrição Eletrónica Médica); hospital PEMH and BDNP-H database; INFARMED/ACSS/SPMS technical norms for hospital outpatient prescribing (2021). https://www.infarmed.pt/documents/15786/4183417/Normas+t%C3%A9cnicas%2C+especifica%C3%A7%C3%B5es+e+requisitos+t%C3%A9cnicos+dos+sistemas+inform%C3%A1ticos+de+prescri%C3%A7%C3%A3o+e+dispensa+de+medicamentos+a+utentes+em+regime+de+ambulat%C3%B3rio+hospitalar+pelos+servi%C3%A7os+farmac%C3%AAuticos+hospitalares+do+Servi%C3%A7o+Nacional+de+Sa%C3%BAde+%28SNS%29/281ebc9d-00e3-cc31-dcd4-fa61f71ecfd5
- Patient portal SNS 24 (prescriptions, exams). https://www.deco.proteste.pt/saude/medicamentos/noticias/receita-medica-eletronica-funciona-precisa-saber
- Coding: ICD-10-CM/PCS since 2017-01-01; CHNM drug code (INFARMED); SNOMED CT (SPMS CTC, member 2014). https://interop-pt.atlassian.net/wiki/spaces/CTCPT/pages/58884368
- Structured pathology: Portuguese study converting ICCR colorectal dataset to FHIR SDC (research, 2025). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12463337/
- Tumour-board software, openEHR oncology archetypes, RSE oncology content: n/f.

### Key organisations and people
- SPMS (HealthData@PT, RON procurement, CTC); DGS / PNDO; INSA; INFARMED; ACSS.
- RON coordinator Maria José Bento (IPO Porto); IPO Lisboa; Porto.CCC / i3S; GIMM (BBMRI.pt). https://gimm.pt/?p=12407
- HL7 Portugal chair João Almeida. https://hl7.eu/affiliate_pt.html

---

## Luxembourg

### (a) Cancer registries
- RNC (Registre National du Cancer): population-based, established 2013 by Direction de la santé, managed by LIH; covers residents and non-residents treated in Luxembourg. https://researchportal.lih.lu/en/projects/registre-national-du-cancer-national-cancer-regestry/
- Sources: Laboratoire National de Santé and hospital cancer registries in the five hospitals (2013 launch). https://gouvernement.lu/dam-assets/fr/actualites/articles/2013/05-mai/15-dibartolomeo/cancer.pdf
- Legal basis: règlement grand-ducal du 18 avril 2013 déterminant les modalités et conditions de fonctionnement du registre national du cancer, Mémorial A-79 of 29 April 2013; registry launched 15 May 2013. https://gouvernement.lu/dam-assets/fr/actualites/articles/2013/05-mai/15-dibartolomeo/cancer.pdf (verified 2026-11-19)
- Governance: multi-institutional management committee (OECD HSPA 2026). https://www.oecd.org/fr/publications/2026/03/health-system-performance-assessment-framework-for-luxembourg_8e0f4466/full-report/health-data-landscape-in-luxembourg-as-a-basis-for-the-hspa_015ca5f4.html
- Coding: CIM-O-3 for topography/morphology; stage per TNM 7th edition (2009); tumour groupings per ENCR-JRC definitions (2020 national cancer report, https://gouvernement.lu/dam-assets/documents/actualites/2021/02-fevrier/04-journee-cancer/MSA-5632-20-rapport-cancer-2020-web-BAT-4-.pdf) (verified 2026-11-19). Submission format and variable dictionary: n/f.
- ENCR/ECIS: RNC/LIH partner in CancerWatch (ECIS data quality). https://www.lih.lu/?p=46068 . Luxembourg does not appear in the ECIS list of contributing registries (archived list) https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19).
- Screening registries: Programme Mammographie (since 1992, extended 45-74 in 2024) and PDOCCR colorectal (permanent since 2021), Direction de la santé. https://gouvernement.lu/fr/actualites/toutes_actualites/communiques/2024/07-juillet/01-deprez-depistage-cancer.html
- Researcher access route: scoping review on RNC data linkage (Lima et al. 2025). https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1679408/full

### (b) Public datasets
- RNC reports; latest RNC report released Feb 2026 covers 23,660 cancers diagnosed 2014-2021 (https://www.lesfrontaliers.lu/?p=1216650) (verified 2026-11-19). https://chronicle.lu/category/medical/59357-luxembourg-takes-action-to-improve-cancer-screening-and-prevention
- Mammography programme national evaluation report (Oct 2024, RNC + Programme Mammographie). https://santesecu.public.lu/dam-assets/fr/publications/r/rapport-programme-mammographie-2024/rapport-national-evaluation-du-programme-mammographie-vf.pdf
- Research data access: HDAB-LU project (LNDS, four years) preparing the future HDAB. https://www.lnds.lu/?p=4470
- Open data portal oncology datasets, synthetic data, national health data catalogue: n/f (HDAB-LU plans a health data catalogue).

### (c) Cancer infrastructure
- Plan National Cancer 2020-2024, extended to 2026; priority digitalisation; INC (Institut National du Cancer) central to implementation. https://santesecu.public.lu/en/espace-professionnel/departement-sante/plans-nationaux/plan-national-cancer.html
- Genetics: Centre national de génétique humaine at LNS; MDLUX2 molecular diagnostics. https://thepathologist.com/diagnostics/mdlux2-drawing-a-fuller-picture
- Biobank: IBBL (Integrated BioBank of Luxembourg, LIH); Luxembourg not listed among BBMRI-ERIC national nodes (page checked 2026-11-18). https://www.bbmri-eric.eu/national-nodes/
- Genomics: 1+MG signatory; LNDS partner in B1MG; LNDS + LIH in Genome of Europe. https://www.lnds.lu/wp-content/uploads/2024/11/PR-Genome_of_Europe_Launch_web.pdf
- EHDEN/OMOP: RNC is the Luxembourg EHDEN data partner; LIH converting registry data to OMOP CDM. https://www.researchluxembourg.org/en/luxembourg-to-speed-up-the-standardisation-of-clinical-data/
- LIH DS4H white paper: oncology data model for colorectal and lung cancer, based on MII oncology model and OMOP (2025). https://www.lih.lu/wp-content/uploads/2025/06/DS4H_Technical-White-Paper.pdf
- EU projects: CAN.HEAL (LNDS partner, 2022-2024); CANDLE national cancer data nodes (LIH, 2025). https://chronicle.lu/category/medical/55746-lih-contributes-to-eu-project-aimed-at-improving-access-to-cancer-data
- EUCAIM: no Luxembourg partner on the consortium list (https://cancerimage.eu/partners/) (verified 2026-11-19). OECI centre: none, no Luxembourg centre on https://accreditation.oeci.eu/ (verified 2026-11-19). CraNE partners: INC and LIH (https://crane4health.eu/partners/); ECHoS: Luxembourg recognised as National Cancer Mission Hub (https://cancermissionhubs.eu/hubs/); TEHDAS2 lists Luxembourg (partner names truncated) (https://tehdas.eu/partners/) (verified 2026-11-19). UNCAN.eu, canSERV, JANE, EUCanScreen: n/f.

### (d) Digital, non-FHIR
- DSP (dossier de soins partagé) on Agence eSanté platform; "DSP New Gen" aligned with EHDS planned; oncology content n/f. https://events.luxinnovation.lu/e/ehds-in-luxembourg
- Hospital coding DCSH: ICD-10-CM / ICD-10-PCS, 2026 rules use ICD-10-BE 2025 manual; APR-DRG. https://santesecu.public.lu/dam-assets/fr/espace-professionnel/informations-et-donnees-de-sante/dcsh-ressources/modalits-de-codage-2026v05.pdf
- Terminology: SNOMED CT member 2018; terminology server planned; LOINC/SNOMED/ICD-10 managed on an EBX-based server (2016 vendor case). https://www.casestudies.com/company/tibco-ebx/case-study/esante-luxembourg-customer-case-study
- Drug coding: CNS positive list "numéro national". https://cns.public.lu/en/legislations/textes-coordonnes/liste-positive-csv.html
- Tumour-board software, structured pathology, openEHR: n/f.

### Key organisations and people
- Direction de la santé; INC; LIH (RNC: Sophie Couffignal operational director, Claudine Backes scientific director, Oct 2023). Agence eSanté: CEO Alexandre Baumeister since 15 June 2026, board chair Marc Hostert (https://en.paperjam.lu/article/agence-esante-is-stepping-up-to-the-european-level) (verified 2026-11-19). https://www.lih.lu/en/article/a-ten-year-milestone-the-national-cancer-registrys-decade-of-support-in-the-fight-against-cancer/
- LNDS (HDAB-LU, B1MG); LNS; IBBL; Agence eSanté; CNS.

---

## Greece

### (a) Cancer registries
- No population-based cancer registry historically (OECD cancer inequalities report). https://www.oecd.org/en/publications/beating-cancer-inequalities-in-the-eu_14fdc89a-en/full-report/component-6.html
- National Registry of Patients with Neoplastic Diseases (Εθνικό Μητρώο Ασθενών με Νεοπλασματικές Ασθένειες): created by ministerial decision 6197/2024, ΦΕΚ Β' 950/09.02.2024, under law 4600/2019 arts. 82-84; registration mandatory for all patients diagnosed after launch or treated after launch; data fields include diagnosis/histological type/grade, mode and date of diagnosis, diagnosing facility, stage at diagnosis, prognostic/predictive biomarkers; HDIKA is processor; interoperates with AMKA registry, the paediatric neoplasm registry and the national EHR (https://www.dsanet.gr/Epikairothta/Nomothesia/950.PDF) (verified 2026-11-19); in production since 24 Feb 2025; platform by IDIKA under the RRF-funded "Integrated Information System for Oncology and Haematology Patients"; states interoperability with ECIS. https://news4health.gr/politiki-ygeias/idika-enarksi-leitourgias-tou-ethnikoy-mitroou-neoplasmatikon-astheneion
- Earlier pathology-based registry 2009-2013 (>95% population). https://springerlink.bibliotecabuap.elogim.com/10.1007/s00428-017-2287-8
- Paediatric: NARECHEM-ST (University of Athens, Prof. Eleni Petridou), ENCR-listed site-specific registry. https://www.encr.eu/node/209
- ENCR membership of the new national registry: n/f (ENCR list NEEDS BROWSER); Greece absent from the ECIS contributing-registries list (archived) https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19). Submission format: web platform by HDIKA; ICD-O/TNM editions: not specified in the decree (n/f).
- Screening: national free preventive examinations (breast, cervical, colorectal) via e-referral on the e-health record portal. https://ehealthrecord.gov.gr/en/citizens-services
- Researcher access route: decree provides a "statistical information users" role; INAB/CERTH designated National Cancer Data Node for Greece in CANDLE (https://www.inab.certh.gr/wp-content/uploads/2025/07/PRESS-RELEASE-CANDLE.pdf) (verified 2026-11-19); public procedure n/f.

### (b) Public datasets
- No national incidence data from a population registry; ECIS estimates used. https://www.oecd.org/en/publications/beating-cancer-inequalities-in-the-eu_14fdc89a-en/full-report/component-6.html
- Research data access body: GR-HDAB (GRNET, 1 Dec 2023 to 30 Nov 2027, Ministries of Digital Governance and Health). https://grnet.gr/en/business-directory/gr-hdab-en
- Open cancer statistics portal, screening data, synthetic data, national catalogue: n/f.

### (c) Cancer infrastructure
- National Cancer Plan 2024-2028 announced with EKPA; still being drafted mid-2024. https://europeancancer.org/policy/ellok-leads-discussions-on-new-cancer-plan-for-greece.html
- ELLOK (Hellenic Cancer Federation) named National Cancer Mission Hub. https://oncodaily.com/blog/19522
- Precision medicine: National Network of Precision Medicine for cancer (2018), PMUs in Attica, Thessaloniki, Crete; molecular oncology network EDIMO stopped accepting samples pending funding. https://ereuna.minedu.gov.gr/index.php/en/slideshow-c-m-2/1787-national-network-of-personalized-medicine-for-cancer-prevention-and-treatment ; https://www.tovima.com/society/greeces-molecular-oncology-network-faces-uncertain-future/
- Biobanks: BBMRI.gr national node (BRFAA, director Dimitris Thanos), Greek Genome Center; 2025 funding proposal aligned with 1+MG. https://www.bbmri-eric.eu/national-nodes/
- Genomics: Genome of Greece (Hellenic Pasteur Institute). https://www.pasteur.gr/en/node/29990
- EUCAIM partners: Aristotle University of Thessaloniki, FORTH, Hellenic Cancer Society, NKUA, NHRF. https://cancerimage.eu/partners/
- EHDEN/OMOP: 5 Greek data partners incl. Papageorgiou General Hospital (OMOP, refreshed Jul 2025), General Hospital of Kavala. https://www.ehden.eu/datapartners/ ; https://catalogues.ema.europa.eu/print/pdf/node/4597
- OECI: General Oncology Hospital of Athens Saint Savvas is the only Greek centre on the OECI list as of 2026-11-19 (https://accreditation.oeci.eu/), accredited June 2025 (https://en.protothema.gr/2025/06/13/saint-savas-was-certified-by-the-organization-of-european-oncology-institutes/) (verified 2026-11-19). CraNE partners: 1st Regional Health Authority of Attica, Agios Savvas, Laiko General Hospital (https://crane4health.eu/partners/); EUCanScreen: 6th Regional Health Authority DYPEDE (https://eucanscreen.eu/partners/); TEHDAS2: Ministry of Health, GRNET, IDIKA (https://tehdas.eu/partners/) (verified 2026-11-19). UNCAN.eu, canSERV, JANE: n/f.

### (d) Digital, non-FHIR
- National EHR (ΕΗΦΥ) launched 2025 (IDIKA); myHealth app (2021) with prescriptions, results, preventive exams; cancer registries planned in next phase. https://origin01-en.protothema.gr/2025/03/10/greek-healthcare-national-electronic-health-record-how-will-it-work
- IDIKA: NCPeH for Patient Summary and ePrescription cross-border. https://fsa.gr/wp-content/uploads/2024/05/ΗΔΙΚΑ-ΔΙΑΣΥΝΟΡΙΑΚΕΣ-2024.pdf
- Cross-border exchange Cyprus-Greece activated. https://www.interregeurope.eu/human/news-and-events/news/cyprus-greece-launch-cross-border-digital-health-services
- Structured pathology, tumour-board software, chemotherapy prescribing, openEHR oncology: n/f.

### Key organisations and people
- Ministry of Health (Minister Adonis Georgiadis; Deputy Minister M. Themistokleous signed registry decision); IDIKA; GRNET (GR-HDAB); EKPA.
- ELLOK (Mission Hub); BBMRI.gr (Dimitris Thanos); NARECHEM (Eleni Petridou); Hellenic Pasteur Institute (Georgios Patrinos, Genome of Greece). https://www.pasteur.gr/en/node/29990

---

## Malta

### (a) Cancer registries
- Malta National Cancer Registry: population-based since 1991 (hospital-based before), within the Directorate for Health Information and Research (DHIR); ENCR member since 1995, IACR voting member. https://um.edu.mt/library/oar/bitstream/123456789/44319/1/CANCER%20INCIDENCE%20AND%20MORTALITY.PDF
- Coverage: whole population (~400,000); ENCR contact list names director Neville Calleja. https://encr.eu/encr-members-contact-list?page=9
- Clinical tumour registry: joint clinical tumour registry created for cancer care tracking (WHO OBS-PACE). https://eurohealthobservatory.who.int/monitors/pace/analyses/pace/integrated-governance-digital-solutions-and-stakeholder-collaboration-lessons-on-improving-cancer-care-from-malta-and-upper-austria
- Screening: BreastScreen, colorectal, cervical programmes (healthscreening.gov.mt). https://healthscreening.gov.mt/en/?p=5486
- Legal basis: Notification of Cancer Act, Cap. 154 (1957), obliging medical practitioners attending a cancer patient to notify the Superintendent of Public Health (https://legislation.mt/eli/cap/154/eng/pdf) (verified 2026-11-19). Submission format, ICD-O/TNM editions, variable dictionary: n/f (ICD-O-3 listed for paediatric dataset, https://ghdx.healthdata.org/node/373740; dhir.gov.mt returns HTTP 403 to automated fetch and deputyprimeminister.gov.mt returned a Cloudflare origin DNS error in a browser on 2026-11-19, so the DHIR registry pages could not be verified).
- Researcher access: via DHIR; formal route n/f.

### (b) Public datasets
- Registry datasets on GHDx (1995-present; 1998-2007; 1999-2010; paediatric 1995-2015). https://ghdx.healthmetricsandevaluation.org/organizations/malta-national-cancer-registry
- OECD/EU Country Cancer Profile Malta 2025. https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-mt-2024-1677-en.pdf
- Research data access body: Malta Health Data Access Body under DHIR, with national metadata catalogue of public health registries. https://dhir.gov.mt/en/?p=7508
- ECIS: National Cancer Registry of Malta contributes incidence 1993-2013 only (archived ECIS list) https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19). Synthetic data: n/f.

### (c) Cancer infrastructure
- National Cancer Plan 2017-2021 (latest found); no successor cancer plan found in 2024-2026 searches; related: National Palliative Care Strategy 2025-2035, NCD Prevention Framework 2025-2035, Digital Health and Health Data Strategy 2025-2030 (https://health.gov.mt/resources/) (verified 2026-11-19). https://www.iccp-portal.org/system/files/plans/MinistryForHealth-Cancer%20Plan.pdf
- Sir Anthony Mamo Oncology Centre (Mater Dei): oncology centre of excellence; nurse navigation, fast-track referrals. https://eurohealthobservatory.who.int/monitors/pace/case-studies/pace/pace-malta-2025/a-dedicated-directorate-to-improve-cancer-care-pathways
- National Cancer Mission Hub preparation (Nov 2024). https://www.independent.com.mt/articles/2024-11-23/local-news/Second-meeting-held-in-preparation-for-Cancer-Mission-Hub-in-Malta-6736265992
- Biobank: BBMRI.mt node = DwarnaBio (University of Malta, Nikolai Pace, Gillian Martin); first 200 WGS under 1+MG-linked programme. https://www.bbmri-eric.eu/national-nodes/
- Genomics: national genomic record system under market research (3,500 tests). https://maltatoday.com.mt/news/national/130779/public_health_service_to_create_national_genomic_databank_as_tests_grow_to_3500
- EUCAIM: Maltese breast screening project linked to EUCAIM/Cancer Image Europe (BreastSCan). https://healthscreening.gov.mt/en/?p=5486
- Mater Dei: national hub for 24 ERNs. https://maltatoday.com.mt/news/national/123844/study_plans_to_unlock_secrets_of_maltese_genetic_makeup_
- CraNE partner: Ministry for Health (https://crane4health.eu/partners/); EUCanScreen: Ministry for Health and Active Ageing (https://eucanscreen.eu/partners/); ECHoS hub: Cancer Research and Innovation Hub Malta (CRIHM) (https://cancermissionhubs.eu/hubs/) (verified 2026-11-19). OECI: no Maltese centre on https://accreditation.oeci.eu/ (verified 2026-11-19). EHDEN/OMOP (no Maltese data partner listed), UNCAN.eu, canSERV, JANE, TEHDAS2: n/f.

### (d) Digital, non-FHIR
- myHealth portal; fast-track cancer referrals for doctors. https://digitalhealth.gov.mt/?p=2150
- University of Malta digital imaging bank and imaging/genomics datasets planned. https://www.um.edu.mt/clusters/disc/pillarsandprojects/
- Structured pathology, tumour-board software, e-prescribing oncology, openEHR: n/f.

### Key organisations and people
- Ministry for Health; DHIR (Neville Calleja; HDAB); SAMOC / Mater Dei; University of Malta (Nikolai Pace, Gillian Martin, DwarnaBio). https://www.openspecimen.org/uni-malta-dwarnabio-population-based-biobank/

---

## Cyprus

### (a) Cancer registries
- Cyprus Cancer Registry: population-based, Health Monitoring Unit, Ministry of Health; established 1998 with MECC/US NCI support; member of IACR and ENCR. https://pmc.ncbi.nlm.nih.gov/articles/PMC4523219
- Output: ~4,260 new cases and ~1,600 deaths per year. https://en.politis.com.cy/social-lens/985101/cyprus-records-4260-new-cancer-cases-annually
- Researcher access: pseudonymised data after National Bioethics Committee approval (study example). https://pmc.ncbi.nlm.nih.gov/articles/PMC11168067
- Coding: ICD-O-3 with CanReg4 software deriving ICD-10 codes; registry set up 1996-1998 with Middle East Cancer Consortium support (https://pmc.ncbi.nlm.nih.gov/articles/PMC4523219) (verified 2026-11-19). Legal basis, submission format, TNM edition, variable dictionary: n/f.
- Screening: breast programme since 2003; colorectal programme for GeSY beneficiaries 50-74 in final implementation; cervical pending. https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-cy-2024-1662-en.pdf
- Note: northern Cyprus 2018 Cancer Registration Law never entered into force (separate jurisdiction). https://www.cyprus-faq.com/en/north/news/vrachi-trebuyut-srochno-vosstanovit-rakovyi-registr

### (b) Public datasets
- Registry progress reports (2008-2010) on GHDx (https://ghdx.healthdata.org/print/114511); Cyprus Cancer Registry contributes incidence 1998-2022 to ECIS (archived list, https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data) (verified 2026-11-19).
- EU Country Cancer Profile Cyprus 2025. https://read.oecd-ilibrary.org/en/publications/eu-country-cancer-profile-cyprus-2025_c5a3f19e-en
- Research data access body: national HDAB under the National eHealth Authority (NeHA, head Constantinos Pattichis); CY-EHDS-2nd project since 2022. https://oecd.ai/en/dashboards/policy-initiatives/european-health-data-space-for-secondary-use-cy-cy-ehds-2nd
- Open data portal, synthetic data, national catalogue: n/f.

### (c) Cancer infrastructure
- National Strategy on Cancer 2009; updated 2019; a May 2024 gov.cy strategy PDF is referenced in the EU Country Cancer Profile Cyprus 2025 but the profile PDF and gov.cy file are blocked to automated fetch (NEEDS BROWSER). https://www.europeancancer.org/download-file/1864.html
- National Cancer Institute: law passed, first board appointed; mandate to prepare and update the national cancer strategy and advise on the registry (2025-2026). https://en.politis.com.cy/news/health/1031893/first-board-appointed-for-national-cancer-institute
- Biobanks: BBMRI.cy node led by Ministry of Health; biobank.cy (University of Cyprus) and CING biobanks; Genome of Europe and GDI participation. https://www.bbmri-eric.eu/national-nodes/
- Genomics in EHR: CING and Xt-EHR/EHDS2nd workshop (Sept 2025). https://berc.ucy.ac.cy/index.php/events-press/230-integrating-genomics-into-the-ehr
- EUCAIM partner: German Oncology Center. https://cancerimage.eu/partners/
- Xt-EHR Joint Action coordinated by Cyprus. https://cna.org.cy/en/article/8172916/cyprus-to-benefit-from-eu-health-data-space-regulation-says-ehealth-authority-head
- OECI: no Cypriot centre on the OECI list as of 2026-11-19 (https://accreditation.oeci.eu/) (verified 2026-11-19); Bank of Cyprus Oncology Centre holds CHKS and ISO 9001:2015 accreditation, not OECI (https://cyprus-mail.com/2026/01/21/double-international-recognition-for-bank-of-cyprus-oncology-centre) (verified 2026-11-19). CraNE partner: Ministry of Health (https://crane4health.eu/partners/); EUCanScreen: Ministry of Health and University of Cyprus (https://eucanscreen.eu/partners/); TEHDAS2: National eHealth Authority, Karaiskakeio Foundation, CYENS (https://tehdas.eu/partners/); ECHoS hub exists (https://cancermissionhubs.eu/hubs/) (verified 2026-11-19). EHDEN/OMOP (no Cypriot data partner listed), UNCAN.eu, canSERV, JANE: n/f.

### (d) Digital, non-FHIR
- GeSY (GHS) insurance system; cancer patients access via chronic patient registries. https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/cyprus2025/provision-of-services/public-health
- myHealth@CY app (Nov 2025), to connect with GeSY and evolve into full EHR. https://cyprus-mail.com/2025/11/25/new-app-to-offer-access-to-health-data
- National eHealth Law and NeHA established. https://cyprus-mail.com/2024/06/28/gesy-to-benefit-from-eu-e-health-minister-says
- SNOMED CT: NeHA case listed by SNOMED International. https://www.snomed.org/snomed-in-action/national-ehealth-authority-of-cyprus
- Structured pathology, tumour-board software, chemo prescribing, openEHR: n/f.

### Key organisations and people
- Ministry of Health Health Monitoring Unit (registry); NeHA (Constantinos Pattichis); National Cancer Institute (new); CING; University of Cyprus biobank.cy; German Oncology Center; Bank of Cyprus Oncology Centre (n/f details).

---

## Cross-country notes
- EHDEN data partner counts: Italy 26, Spain 27, Portugal 11, Greece 5, Luxembourg 1 (RNC), Malta 0, Cyprus 0. https://www.ehden.eu/datapartners/
- BBMRI-ERIC national nodes exist for Italy, Greece, Malta, Cyprus, Portugal (GIMM) and Spain (full member 2025); Luxembourg n/f. https://www.bbmri-eric.eu/national-nodes/
- EUCAIM partner countries among the seven: Italy, Spain, Portugal, Greece, Cyprus; Malta via BreastSCan link; Luxembourg not on the partner list. https://cancerimage.eu/partners/ (verified 2026-11-19)
- HDAB preparation projects: HDAB-ES (ES), HealthData@PT (PT), HDAB-LU (LU), GR-HDAB (GR), Malta HDAB (DHIR), CY-EHDS-2nd (NeHA); Italy designation pending.
- ECIS contributing registries (archived list, 2025): Italy 41, Spain 15, Portugal 4 regional (to 2016), Cyprus 1 (1998-2022), Malta 1 (1993-2013), Greece 0, Luxembourg 0. https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (verified 2026-11-19)
- CraNE (Comprehensive Cancer Infrastructures) partners exist in all seven countries; ECHoS National Cancer Mission Hubs exist in all seven. https://crane4health.eu/partners/ ; https://cancermissionhubs.eu/hubs/ (verified 2026-11-19)
