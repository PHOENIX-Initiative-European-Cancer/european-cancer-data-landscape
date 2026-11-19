# European national FHIR, oncology FHIR and terminology landscape

Survey for the ECCDM editors, compiled 2026-11-18 from five regional research passes plus the Greece deep-dive. Per-country detail with source URLs is in the sibling files (dach-benelux.md, south.md, nordic-baltic.md, central-east.md, islands-uk.md). "none" = nothing published; "n/f" = not found in a public source.

## A. National FHIR base IGs and oncology FHIR work

| Country | National base/core IG (package, version, FHIR) | Oncology FHIR specification | Cancer registry input format today |
|---|---|---|---|
| Germany | de.basisprofil.r4 1.6.0 (2026-06-29), R4 only, no R5/R6 plan; AddressDeBasis aligned with HL7 EU Base | MII KDS Onkologie 2026.0.3 (oBDS 3.0.2) and 2027.0.0-ballot.1 (2026-09-15, 98 profiles, oBDS 3.0.5 numbering), R4, no mCODE; DKTK de.dktk.oncology 1.8.0 (2024) | oBDS XML v3 only (3.0.1–3.0.4 in production, 3.0.5 Oct 2025, 3.1.0 accepted from Apr 2027), 15 Landeskrebsregister, no FHIR channel |
| Austria | hl7.at.fhir.core.r5 2.0.0 STU2 (R5) and .r4 2.0.0 | none | Statistik Austria secured interface, structured electronic, schema n/f |
| Switzerland | ch.fhir.ig.ch-core 6.0.0 STU6, 7.0.0-ballot, R4 | CH CRL 0.9.0 draft, R4, BAG "Austauschformat KRG", FHIR document, no mCODE | FHIR (CH CRL) voluntary, cantonal registries + NKRS |
| Netherlands | nictiz.fhir.nl.r4.nl-core 0.12.1-beta.1, R4 (no non-beta roadmap; dependants pin 0.12.0-beta.4) | IKNL NKR IG iknl.fhir.nl.r4.ncr-ehr 1.4.2 (draft, 2026-01-22): 10 profiles + 2 trial document profiles, 3 bundle types; mCODE only a commented template remnant; IKNL PZP IG 1.0.0; MedMij pathology 1.0.0-alpha.3 | R(H)ONDA FHIR R4 bundles via Performation Datagateway (15 hospitals Jul 2025) plus PALGA and LBZ feeds; 2026: about 200k tumours automatic, 130k partly manual |
| Belgium | hl7.fhir.be.core 2.2.0, R4; core-clinical 1.4.0 | Belgian Cancer Registry on FHIR be.fhir.bcr 0.1.0 draft (Jun 2026), R4, Bijlage 55 logical models; no mCODE | WBCR web app / batch, form Bijlage 55; healthdata.be CSV v1.1 |
| France | hl7.fhir.fr.core 2.2.0 trial-use, 3.0.0-ballot (Nov 2026), R4 | INCa OSIRIS inca.fhir.uv.osiris 1.1.0, R4, 45 profiles; SNOMED + ICD-O-3 morphology; mCODE radiotherapy value sets | Francim registries, CIM-O-3; national registry (law Jun 2025, INCa) format n/f |
| Italy | IT Core hl7.fhir.it.core 0.2.0 STU (2026-05-25, canonical hl7.it/fhir/itcore), R4, no EU Base dependency (Lab Report IG has one); hl7.fhir.it.base legacy | none; FSE 2.0 oncology documents are CDA R2; OMOP at 26 EHDEN partners | National registry XML (PN REG tracciati v2.2, Jan 2025, 4 flows) fed by 21 regional centres; AIRTUM flat tracciati A–E |
| Spain | none national; UNICAS rare-disease IG 0.0.12 draft, R5 | none (2026 "Red Nacional Interoperable" proposal names FHIR+OMOP) | REDECAN regional registries, ENCR rules, format n/f |
| Portugal | SPMS Portuguese Core IG 1.0.0, R4B; hl7.fhir.pt.core 0.0.1 CI | none (RON platform contract 2025) | RON platform, Law 53/2017, format n/f |
| Luxembourg | eSanté preview guides only, no base package | none | RNC (LIH), format n/f |
| UK | fhir.r4.ukcore.stu2 2.0.1 (2.0.2/2.1.0 on registry), R4; STU3 dev; Wales 2.7.0 | no COSD FHIR IG; NHS Genomics IG 0.6.11 depends on mCODE 4.0.0 | COSD XML v10.2 to NDRS (England); WCISU, SMR06, NICR |
| Ireland | none (HIQA/HSE); iEHR.ai IE Core 1.0.0-ballot (vendor) | none | NCRI electronic lab/HIPE/RT feeds, no FHIR |
| Denmark | hl7.fhir.dk.core 3.7.0, R4; medcom.fhir.dk.core 4.0.0 | none | LPR3 + Patobank EDI (MEDRPT), SDS |
| Sweden | hl7se.fhir.base 1.1.0, R4 (not EU Core compatible) | none (INCA on openEHR) | INCA forms A/B reports to RCC, Socialstyrelsen |
| Norway | hl7.fhir.no.basis 2.2.2, R4 | none | KREMT web/EHR messages + pathology "Svar" messages, Kreftregisteret (FHI) |
| Finland | hl7.fhir.fi.base 2.0.0 STU2, R4 | none | statutory notification, format n/f, THL/Cancer Society |
| Iceland | none | none | mandatory notification, IARC/ENCR rules |
| Estonia | ee.fhir.base 2.0.0 trial-use, R5 (TEHIK) | VJL cancer dashboard ee.fhir.vjl 0.1.0 draft (Oct 2026), R5, no mCODE | X-Road / electronic notification to TAI |
| Latvia | none | none (cancer patient card in e-veselība since 2024) | e-veselība card to SPKC |
| Lithuania | lt.hl7.fhir.base 0.3.0 draft, R5 | 5 screening IGs (lung, colorectal, cervical, breast, prostate) 0.0.1, R5; lab IG with ICD-O-3 and pTNM; no mCODE | form 090/a, fully electronic (NVI) |
| Poland | hl7.fhir.pl.base.r5 0.2.0 ci / .r4 0.1.1, under dev | none (e-DiLO oncology card on IHE XDS.b from Aug 2026) | e-KRN+ web app since Oct 2024 (NIO-PIB) |
| Czechia | hl7.fhir.cz.core 1.0.0 STU1 (Jul 2026), R4, on EU Base 2.0 | none (SZZ screening observations only) | DASTA interfaces to NOR (ÚZIS) |
| Slovakia | none (ISO 13606 mandated) | none | ISZI: system link, XML upload or web form (NCZI) |
| Hungary | none | none | quarterly provider reports, format by agreement (nrr.hu upload) |
| Slovenia | limited core IG, not public, R4 | none | active registration from HIS lists, Register raka (OI Ljubljana) |
| Croatia | cezih.hr.cezih-osnova 1.0.x, R4 | none (ONKO+ message piloted, not deployed) | CEZIH messages + forms to HZJZ |
| Romania | none | none | RNC created 2023 (INSP), format n/f |
| Bulgaria | none (NHIS XML/XSD APIs) | none | NHIS cancer database (draft ordinance 2025) |
| Greece | hl7.fhir.gr.base-and-core-r5 0.0.1-draft, R5 (HL7 Hellas / Gnomon) | none; oncology registry hub by Gnomon, ENCR spec | National Registry of Neoplastic Diseases (IDIKA, Feb 2025), ENCR/ECIS aligned |
| Cyprus | none (eHealth4U prototype package) | none | Cyprus Cancer Registry (MoH), MECC coding |
| Malta | none (openEHR national EHR) | none | DHIR registry, ENCR |

## B. Terminologies in use (versions where published)

| Country | SNOMED CT | ICD-10 variant (current) | ICD-O | TNM | LOINC | Terminology server |
|---|---|---|---|---|---|---|
| Germany | member 2021, BfArM; DE edition 11000274103, releases 20251115, 2026-05-18, extra 2026-08-18 (130,795 translations); MII pins INT 20260701 | ICD-10-GM 2026, valid through 2028 (three-year cycle, no 2027 edition) | ICD-O-3 2nd rev 2019 (THO URL); ICD-O-4 in oBDS 3.1.0, accepted from 2027-04-01 | oBDS TNM-Version 6/7/8/9; TNM 9 codes in MII 2027 | deDE variant, LOINC 2.83 on ZTS (MII Ontoserver 2.81) | BfArM ZTS (NPM packages, 69 CodeSystems, no FHIR operations); MII Ontoserver (mTLS) |
| Austria | member 2019, ELGA, AT extension Nov 2025/May 2026 | ICD-10 BMSGPK 2026 | ICD-O-3 rev 2 since 2020 | UICC 8 | LOINC DE-AT 2.77 | TerminoloGit / tergi (ELGA) |
| Switzerland | member 2016, eHealth Suisse, CH ext 2026-06 | ICD-10-GM (BFS), CHOP 2026 | ICD-O-3 (ed n/f) | n/f | n/f | tx.fhir.ch (HL7 CH), no government server |
| Netherlands | charter 2007, Nictiz, monthly; NL June 2026 release 396,147 active concepts | ICD-10 NL 2021 plus errata 2024-1 (required by NKR) | ICD-O-3; IKNL introduces ICD-O-4 in the NKR during 2026 | UICC 8 since 2017; TNM 9 in the Dutch lung guideline, NKR-wide date n/f | Labcodeset on 2.83; LOINC-Implementatieadvies 1.0 (May 2026) | Nationale Terminologieserver (Ontoserver) terminologieserver.nl/fhir, authenticated content |
| Belgium | NRC FPS Health, monthly BE release since Nov 2024 | ICD-10-BE (CM/PCS) 2023 handbook | ICD-O-3 | n/f | n/f | FPS Ontoserver apps.health.belgium.be |
| France | member 2023, ANS; FR edition 20260621 (translations only, 58.8% translated), annual, SMT-only | CIM-10 FR PMSI 2026 (ATIH), CIM-11 switch horizon 2031 | CIM-O-3 (revision n/f; OSIRIS-RWD uses 3.2) | UICC 7 in CI-SIS Fiche RCP 2025.01, OSIRIS lists eds 5–7; TNM 9 adoption n/f | LOINC Biologie FRA 2.24 on 2.81 (Apr 2026) | SMT (ANS, Ontoserver 6.28, in HL7 tx-registry) |
| Italy | not a member (accession foreseen by the 2022 FSE decree, not done) | ICD-9-CM 2007 (SDO); ICD-10-IM and CIPI from 2027-01-01 (DM 2025-10-23); ISTAT ICD-10 v2019 | ICD-O-3 Italian edition (Inferenze 2005); registries accept 3.1/3.2 | any UICC/AJCC edition, edition recorded (1–8), no national mandate | IT variant 2.75 (CNR, Aug 2023), mandated by DPCM 178/2015 | none (gateway CSV dictionaries; HL7 Italia Terminology IG 0.1.2) |
| Spain | member, MoH, ES edition Apr/Oct | CIE-10-ES 6th ed 2026 | CIE-O-3.2 from 2026-01-01 | n/f | LOINC ES 2.77 | SNS Servidor de Terminologías (production) |
| Portugal | member 2014, SPMS CTC | ICD-10-CM/PCS since 2017 | ICD-O-3 | n/f | n/f | none (tender 2026) |
| Luxembourg | member 2018, eSanté | ICD-10-CM/PCS via ICD-10-BE manual | n/f | n/f | n/f | planning |
| UK | founder, NHS England, UK edition (Drug ext 42.1.0 May 2026) | ICD-10 5th ed; OPCS-4.11 Apr 2026 | ICD-O-3 | TNM 8 since 2018 | none (SNOMED UTL) | NHS England Ontoserver; NHS Scotland server |
| Ireland | member 2016, HSE, IE edition (Jun 2026) | ICD-10-AM 12th ed (HIPE 2024) | ICD-O-3.2 since 2020 | TNM 7 since 2014 (NCRI) | on HSE CTS | HSE Central Terminology Service (beta 2025/26) |
| Denmark | charter 2007, SDS, DK ext Sep 2025 | SKS ICD-10 | ICD-O-3 | n/f (cTNM mandatory in LPR3) | NPU + LOINC profiles | planning; tx-nordics shared |
| Sweden | charter 2007, Socialstyrelsen, SE ext Nov 2025 | ICD-10-SE 2026 (13th), ICD-11 deaths 2027 | ICD-O-3.2 (2019) | latest UICC (ed n/f) | n/f | Inera Terminologitjänst (production) |
| Norway | member 2017, Helsedirektoratet | ICD-10 NO 2026 | n/f | n/f | NPU | in development |
| Finland | member 2018, THL, FI edition Dec | THL ICD-10, ICD-11 from 2028 | n/f | n/f | n/f | planning (Koodistopalvelu not FHIR) |
| Iceland | member 2011, Directorate of Health | ICD-10 IS 2014 | n/f | n/f | n/f | in development |
| Estonia | member 2010, TEHIK, EE edition | RHK-10 | ICD-O-3 since 2008 | n/f | EE variant 2.77 | TEHIK Ontoserver (production) |
| Latvia | member Jan 2026, SPKC; GPS in use | SSK-10 | n/f | n/f | planned | production (operator n/f) |
| Lithuania | charter 2007, Medical Library | TLK-10-AM since 2019 | ICD-O-3 (lab IG) | pTNM in lab IG, ed n/f | yes (lab IG) | tx.hl7.lt |
| Poland | not a member | ICD-10 PL 2008 (CeZ) | ICD-O-3 PL (KRN) | TNM 8 | PL translation in 2.81 | planning |
| Czechia | member 2012, ÚZIS NRC 2020, CZ translation in progress | MKN-10-CZ 2026 | MKN-O-3.2 | TNM 8; TNM 9 in NOR from 2027 | planned | in development |
| Slovakia | member 2009, NCZI | MKCH-10 | MKCH-O-3.2 since 2020 | TNM 8 / 9 (2026 guidance) | n/f | none planned |
| Hungary | member Sep 2024, ESZFK | BNO-10 | n/f | n/f | n/f | n/f |
| Slovenia | member 2010, NIJZ | MKB-10-AM v11 since 2023 | n/f | n/f | n/f | in development |
| Croatia | member 2023, MoH | MKB-10 | n/f | n/f | n/f | production (name n/f) |
| Romania | not a member | ICD-10-AM 3rd ed (DRG), CIM-10 | n/f | n/f | n/f | n/f |
| Bulgaria | not a member | ICD-10 as NHIS nomenclature CL011 | n/f | n/f | n/f | n/f |
| Greece | not a member | ICD-10-GrM 2017 v2 (from ICD-10-GM 2013), mandatory in ePrescription 2024 | ICD-O-3 implied by ENCR | n/f | none | under development |
| Cyprus | member 2018, NeHA | ICD-10 mix with ICPC/CPT-4 | ICD-O-3 | ed n/f | partial | planning |
| Malta | member 2011, MoH IMU | ICD-10 | ICD-O-3 | n/f | n/f | n/f |

## C. What this means for ECCDM

1. **Six countries have oncology FHIR artefacts** to align or map against: Germany (MII Onkologie / oBDS), Switzerland (CH CRL), Netherlands (IKNL NKR), Belgium (BCR on FHIR), France (OSIRIS) and, at draft level, Estonia (VJL) and Lithuania (screening IGs). Only two of these touch mCODE (UK Genomics as a dependency, OSIRIS via radiotherapy value sets); none builds on it. This supports the mCODE decoupling already done in ECCDM.
2. **Registry data standards dominate.** Where oncology FHIR exists it wraps a registry dataset (oBDS, KRG, NKR itemset, Bijlage 55). ECCDM's logical models map most naturally to these registry datasets, and the ENCR variable set is the common denominator for the 20+ countries without FHIR oncology work.
3. **SNOMED CT coverage is not universal.** Italy, Poland, Romania, Bulgaria and Greece are not members; Latvia and Hungary joined only in 2024 to 2026 and have no national content yet. ECCDM bindings that are SNOMED-only need an ICD-O-3 / ICD-10 fallback or an "example" strength for these jurisdictions.
4. **ICD-O-3 is the one oncology code system in use everywhere**, but editions differ: 3.1 (older registries) vs 3.2 (Spain, Sweden, Czechia, Slovakia, Ireland from 2020 to 2026) and Germany's 2019 revision, with ICD-O-4 (2026) already scheduled in oBDS from April 2027. ECCDM should state the ICD-O edition in its bindings.
5. **TNM edition is in transition.** Most registries still code UICC 8; Germany (oBDS 3.0.5), Czechia (NOR 2027), Slovakia (2026 guidance) are moving to TNM 9; France still cites UICC 7 in CI-SIS 2025.01. ECCDM's CancerStage model should carry the edition explicitly.
6. **LOINC is thin outside DACH/Benelux/Nordics.** National LOINC variants exist for DE, AT, NL, FR, IT, ES, PL, EE; the UK uses the SNOMED Unified Test List; Nordics use NPU. Observation-type bindings in ECCDM should not assume LOINC availability.
7. **FHIR version split:** R4 everywhere established (DE, CH, NL, BE, FR, UK, DK, SE, NO, FI, CZ, HR), R5 in the newer EU-Core-aligned guides (AT, EE, LT, PL, GR, ES UNICAS). ECCDM is published on FHIR 4.0.1 with cross-version extensions, matching the established guides; an R5 rendering would match the newer ones.
