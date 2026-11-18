### Spain (ES)

Region: Southern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National core IG:** under development; the State of FHIR 2026 summary says it is being published at unicas-fhir.sanidad.gob.es (https://packages.fhir.org/jurisdictions/ES). Existing: ÚNICAS Rare Diseases HL7 FHIR IG, package `unicas-ig`, canonical https://unicas-fhir.sanidad.gob.es, FHIR R5 (5.0.0), version 0.0.12 draft, 2026-10-13, coordinated by Ministerio de Sanidad with Cataluña leading development; depends on IPS 1.1.0. No `hl7.fhir.es.core` package found.
2. **Oncology FHIR IG:** not found. Only a 2026 "Red Nacional Interoperable" proposal (CIBERONC, VHIO, IRB Barcelona, INCLIVA, FISEVI) naming HL7 FHIR and OMOP (https://www.impacto.contraelcancer.es/wp-content/uploads/2026/08/Red-Nacional-Interoperable.pdf). mCODE reuse: not found.
3. **Registry reporting:** REDECAN (Red Española de Registros de Cáncer) federates regional population-based registries run by the autonomous communities plus RETI; follows ENCR/IARC rules, ICD-O-3, TNM edition field 5th–8th in the REDECAN/SEOM 2023 variable set (https://seom.org//images/ESTUDIO_REGISTRO_DE_CANCER_BASE_POBLACIONAL.pdf). Submission format: not found.
4. **Terminologies:** SNOMED CT member, NRC Ministerio de Sanidad; Spanish Edition released 30 April and 31 October, SNS national extension twice yearly (https://www.sanidad.gob.es/profesionales/hcdsns/areaRecursosSem/snomed-ct/areaDescarga.htm). CIE-10-ES 6.ª edición 2026, diagnósticos and procedimientos manuals (https://www.sanidad.gob.es/estadEstudios/estadisticas/normalizacion/). CIE-O-3.2 in force 2026-01-01 (https://www.sanidad.gob.es/ca/estadEstudios/estadisticas/normalizacion/CIE10/2026/Nota_edicion_CIE_O_3_2.pdf). LOINC Spain edition 2.77, Feb 2024, Servicio Extremeño de Salud (https://loinc.org/?p=7929). Drug code (Código Nacional, AEMPS) FHIR publication: not found. TNM edition: not found. Terminology server: Servidor de Terminologías de Referencia del SNS, Ministerio de Sanidad, in production (https://www.sanidad.gob.es/areas/saludDigital/semanticaClinica/factoriaRecursos/servTerm.htm).
5. **Organisations and people:** Ministerio de Sanidad (Área de Recursos Semánticos, Unidad Técnica de Codificación), HL7 Spain (chair Francisco Pérez, https://hl7.eu/affiliate_es.html), REDECAN, SEOM. Ministry SNOMED contact in 2014–2019 documents: Arturo Romero Gutiérrez (current role not confirmed).

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: regional registries run by autonomous communities, federated in REDECAN (Red Española de Registros de Cáncer), incl. RETI (childhood). https://seom.org//images/ESTUDIO_REGISTRO_DE_CANCER_BASE_POBLACIONAL.pdf
- REDECAN 2024 incidence estimates use 12 consolidated population registries. https://www.infocop.es/wp-content/uploads/2025/01/ESTIMACIONES-DE-LA-INCIDENCIA-CANCER-ESPANA-2024.pdf
- Coverage: about 25% of Spain's population (2024 study); older REDECAN figure ~20%. https://www.redaccionmedica.com/autonomias/catalunya/20150727/salud-creara-un-registro-catalan-del-cancer/340126_0.html
- ENCR: Spanish registries participate in ENCR (e.g., Registro de Madrid follows ENCR recommendations). https://www.comunidad.madrid/node/74791
- Legal basis: regional decrees (e.g., Castilla y León registry manual follows ENCR/IARC, IARC TP 40, behaviour /3 only); national registry law n/f. https://www.saludcastillayleon.es/en/enfermedades-problemas-salud/cancer/registro-poblacional-cancer.files/96813-Manual%20de%20Procedimiento%20%20Registro%20de%20Base%20Poblacional%20de%20C%C3%A1ncer%20de%20Castilla%20y%20Le%C3%B3n.pdf
- Variable dictionary: REDECAN/SEOM proposed variable set v1 (March 2023): ICD-O-3, TNM edition field 5th-8th, cT/pM/stage; first edition covers stomach, colorectal, lung, ovary, prostate. https://seom.org//images/ESTUDIO_REGISTRO_DE_CANCER_BASE_POBLACIONAL.pdf
- Submission format (XML/CSV): n/f. Hospital tumour registries: long tradition (Catalonia, Lleida, Madrid RTMAD). https://www.quironsalud.com/es/comunicacion/actualidad/hospital-universitario-quironsalud-madrid-incorpora-registr
- Catalonia population registry in development (Girona, Tarragona registries exist). https://idescat.cat/paae/2015/090901/es
- Screening registries: Red de Programas de Cribado de Cáncer; Ministry situation reports 2025 (breast, colorectal). https://www.sanidad.gob.es/areas/promocionPrevencion/cribado/cribadoCancer/cancerMama/docs/informeDeSituacionCribadoCancerMama_2025.pdf
- Researcher access: REDECAN provides results to authorities and the scientific community; formal access route n/f. https://www.ciberisciii.es/media/914374/dossier-redecan-20072017.pdf

#### (b) Public datasets
- "Las cifras del cáncer en España" (SEOM + REDECAN, annual; 2024: 286,664 new cases). https://seom.org/images/Informe_Cifras_Cancer_2024.pdf
- REDECAN website redecan.org publishes estimates; INE mortality data. https://www.infocop.es/wp-content/uploads/2025/01/ESTIMACIONES-DE-LA-INCIDENCIA-CANCER-ESPANA-2024.pdf
- Ministry BDCAP prevalence of malignant neoplasms (primary care). https://www.sanidad.gob.es/estadEstudios/estadisticas/estadisticas/estMinisterio/SIAP/Prevalencia_neoplasias_malignas_BDCAP_Series_3.pdf
- AECC "Más Datos Cáncer" platform, 69 indicators. https://www.contraelcancer.es/sites/default/files/2025-10/Comunicado_Datos_Autonomias.pdf
- Research data access body: HDAB-ES project (Ministerio de Sanidad sole beneficiary). https://www.sanidad.gob.es/areas/saludDigital/proyectoHDAB-ES/home.htm
- Espacio Nacional de Datos de Salud (ENDS): network of regional platforms, 70 M EUR, announced Jan 2026. https://digital.gob.es/content/dam/portal-mtdfp/comunicacion/comunicacion_ministro/2026/2025-01-29/NdPEspaciosdedatos.pdf
- Screening open data: ENSE 2023 early-detection monograph. https://www.sanidad.gob.es/gl/gabinete/notasPrensa.do?id=6947
- ECIS: Spanish registries contribute via ENCR; list n/f. Synthetic datasets: n/f.

#### (c) Cancer infrastructure
- Estrategia en Cáncer del SNS, updated version approved by CISNS 24 Feb 2021. https://www.sanidad.gob.es/areas/calidadAsistencial/eventosJornadas/Jornada/RANCancer.htm
- OECI: Clínica Universidad de Navarra CCC (May 2025), Bellvitge/ICO CCC (Oct 2025), Hospital 12 de Octubre CCC, IVO Cancer Centre. https://cancercenter.cun.es/en/cancer-center-clinica-european-accreditation-oncology-care ; https://idibell.cat/en/2025/10/bellvitge-health-campus-provides-comprehensive-cancer-care-to-two-million-people-following-the-model-that-europe-aims-to-deploy-by-2030/
- Genomics: IMPaCT-Genómica (7.25 M EUR 2021-2023), Plan de Medicina Personalizada 5P (100 M EUR); 1+MG signatory. https://www.sanidad.gob.es/ca/gabinete/notasPrensa.do?id=6006
- Biobanks: Spain observer in BBMRI-ERIC (2021), full membership agreement published BOE 29 May 2025; ISCIII Plataforma de Biobancos y Biomodelos as national node. https://boe.es/boe/dias/2025/05/29/pdfs/BOE-A-2025-10681.pdf
- EUCAIM: central hub technically coordinated at UPV/La Fe (Ignacio Blanquer); ~30 Spanish partners (SAS, BSC, CRG, CIBER, Clínic, ISCIII, La Fe, Quibim, SERMAS, CSIC, Univ. Valencia). https://cancerimage.eu/partners/
- EHDEN/OMOP: 27 Spanish data partners incl. Institut Català d'Oncologia, Vall d'Hebron, 12 de Octubre, La Fe, Sant Pau, Hospital del Mar, Virgen Macarena. https://www.ehden.eu/datapartners/
- Red Nacional Interoperable de datos en cáncer (CIBERONC, IRB, VHIO, INCLIVA, FISEVI), standards HL7 FHIR, OMOP, HealthDCAT-AP. https://www.impacto.contraelcancer.es/wp-content/uploads/2026/08/Red-Nacional-Interoperable.pdf
- Other EU projects (UNCAN.eu, canSERV, JANE, CraNE, EUCanScreen, TEHDAS2): n/f for Spanish partner lists.

#### (d) Digital, non-FHIR
- HCDSNS (national EHR): clinical reports (discharge, emergency, imaging) in CDA; no dedicated oncology report; CMDIC v6.0 adds pathology report. https://www.sanidad.gob.es/gl/profesionales/hcdsns/contenidoDoc/situacionActualHCDSNS.htm ; https://www.sanidad.gob.es/organizacion/sns/planCalidadSNS/docs/ARS.pdf
- SEOM: EHRs in most of the SNS do not allow automated oncology workflow; ENDS "embryonic" (2025 commentary). https://www.redaccionmedica.com/secciones/sanidad-hoy/espacio-de-datos-sanitarios-el-ministerio-de-sanidad-va-solo-tarde-y-mal-1144
- Coding: CIE-10-ES 6th ed. 2026; CIE-O-3.2 from 2026-01-01; SNOMED CT Spanish edition; LOINC Spain 2.77. https://www.sanidad.gob.es/estadEstudios/estadisticas/normalizacion/
- Terminology server: Servidor de Terminologías de Referencia del SNS. https://www.sanidad.gob.es/areas/saludDigital/semanticaClinica/factoriaRecursos/servTerm.htm
- Structured pathology (SEAP synoptic), chemotherapy e-prescribing (Oncofarm/Farmis), tumour-board software, openEHR oncology: n/f.
- Upcoming national digital health law adapting to EHDS (consultation to 20 Oct 2025). https://www.cuatrecasas.com/es/spain/farmaceutico-sanitario/art/hacia-una-digitalizacion-de-la-salud

#### Key organisations and people
- Ministerio de Sanidad (Área de Recursos Semánticos; HDAB-ES; ENDS); ISCIII (biobank platform, IMPaCT); AEMPS.
- REDECAN; SEOM; AECC Observatorio; CIBERONC; HL7 Spain (chair Francisco Pérez). https://hl7.eu/affiliate_es.html
- EUCAIM: Ignacio Blanquer (UPV / IIS La Fe). https://www.cesga.es/wp-content/uploads/2025/05/20250618-EHDS-and-RIs.pdf

---
