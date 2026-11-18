### FHIR landscape

National base or core FHIR guides, oncology FHIR specifications and the format in which the national cancer registry receives data today. "none" = nothing published; "n/f" = not found in a public source. Package versions as published on packages.fhir.org / Simplifier on 2026-11-18. Machine-readable copy: [data/fhir-landscape.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/fhir-landscape.csv).

| Country | National base/core IG (package, version, FHIR) | Oncology FHIR specification | Cancer registry input format today |
|---|---|---|---|
| [Germany](country-germany.html) | de.basisprofil.r4 1.6.0, R4 (HL7 DE) | MII KDS Onkologie 2026.0.3, R4, 2027.0.0-ballot; implements oBDS 3.0.x; mCODE influence only | oBDS XML 3.0.5 (Oct 2025), 3.1.0 (Oct 2026), 16 state registries |
| [Austria](country-austria.html) | hl7.at.fhir.core.r5 2.0.0 STU2 (R5) and .r4 2.0.0 | none | Statistik Austria secured interface, structured electronic, schema n/f |
| [Switzerland](country-switzerland.html) | ch.fhir.ig.ch-core 6.0.0 STU6, 7.0.0-ballot, R4 | CH CRL 0.9.0 draft, R4, BAG "Austauschformat KRG", FHIR document, no mCODE | FHIR (CH CRL) voluntary, cantonal registries + NKRS |
| [Netherlands](country-netherlands.html) | nictiz.fhir.nl.r4.nl-core 0.12.1-beta.1, R4 (never non-beta) | IKNL NKR IG iknl.fhir.nl.r4.ncr-ehr 1.4.2, R4; mCODE dependency commented out | IKNL abstraction + nightly FHIR extraction from 20 hospitals |
| [Belgium](country-belgium.html) | hl7.fhir.be.core 2.2.0, R4; core-clinical 1.4.0 | Belgian Cancer Registry on FHIR be.fhir.bcr 0.1.0 draft (Jun 2026), R4, Bijlage 55 logical models; no mCODE | WBCR web app / batch, form Bijlage 55; healthdata.be CSV v1.1 |
| [France](country-france.html) | hl7.fhir.fr.core 2.2.0 trial-use, 3.0.0-ballot (Nov 2026), R4 | INCa OSIRIS inca.fhir.uv.osiris 1.1.0, R4, 45 profiles; SNOMED + ICD-O-3 morphology; mCODE radiotherapy value sets | Francim registries, CIM-O-3; national registry (law Jun 2025, INCa) format n/f |
| [Italy](country-italy.html) | hl7.fhir.it.base 0.1.0 PC ballot (2020), IT Core under dev, R4 | none | AIRTUM flat files (tracciati A–E, 2020 protocol); national RNT format n/f |
| [Spain](country-spain.html) | none national; UNICAS rare-disease IG 0.0.12 draft, R5 | none (2026 "Red Nacional Interoperable" proposal names FHIR+OMOP) | REDECAN regional registries, ENCR rules, format n/f |
| [Portugal](country-portugal.html) | SPMS Portuguese Core IG 1.0.0, R4B; hl7.fhir.pt.core 0.0.1 CI | none (RON platform contract 2025) | RON platform, Law 53/2017, format n/f |
| [Luxembourg](country-luxembourg.html) | eSanté preview guides only, no base package | none | RNC (LIH), format n/f |
| [United Kingdom](country-united-kingdom.html) | fhir.r4.ukcore.stu2 2.0.1 (2.0.2/2.1.0 on registry), R4; STU3 dev; Wales 2.7.0 | no COSD FHIR IG; NHS Genomics IG 0.6.11 depends on mCODE 4.0.0 | COSD XML v10.2 to NDRS (England); WCISU, SMR06, NICR |
| [Ireland](country-ireland.html) | none (HIQA/HSE); iEHR.ai IE Core 1.0.0-ballot (vendor) | none | NCRI electronic lab/HIPE/RT feeds, no FHIR |
| [Denmark](country-denmark.html) | hl7.fhir.dk.core 3.7.0, R4; medcom.fhir.dk.core 4.0.0 | none | LPR3 + Patobank EDI (MEDRPT), SDS |
| [Sweden](country-sweden.html) | hl7se.fhir.base 1.1.0, R4 (not EU Core compatible) | none (INCA on openEHR) | INCA forms A/B reports to RCC, Socialstyrelsen |
| [Norway](country-norway.html) | hl7.fhir.no.basis 2.2.2, R4 | none | KREMT web/EHR messages + pathology "Svar" messages, Kreftregisteret (FHI) |
| [Finland](country-finland.html) | hl7.fhir.fi.base 2.0.0 STU2, R4 | none | statutory notification, format n/f, THL/Cancer Society |
| [Iceland](country-iceland.html) | none | none | mandatory notification, IARC/ENCR rules |
| [Estonia](country-estonia.html) | ee.fhir.base 2.0.0 trial-use, R5 (TEHIK) | VJL cancer dashboard ee.fhir.vjl 0.1.0 draft (Oct 2026), R5, no mCODE | X-Road / electronic notification to TAI |
| [Latvia](country-latvia.html) | none | none (cancer patient card in e-veselība since 2024) | e-veselība card to SPKC |
| [Lithuania](country-lithuania.html) | lt.hl7.fhir.base 0.3.0 draft, R5 | 5 screening IGs (lung, colorectal, cervical, breast, prostate) 0.0.1, R5; lab IG with ICD-O-3 and pTNM; no mCODE | form 090/a, fully electronic (NVI) |
| [Poland](country-poland.html) | hl7.fhir.pl.base.r5 0.2.0 ci / .r4 0.1.1, under dev | none (e-DiLO oncology card on IHE XDS.b from Aug 2026) | e-KRN+ web app since Oct 2024 (NIO-PIB) |
| [Czechia](country-czechia.html) | hl7.fhir.cz.core 1.0.0 STU1 (Jul 2026), R4, on EU Base 2.0 | none (SZZ screening observations only) | DASTA interfaces to NOR (ÚZIS) |
| [Slovakia](country-slovakia.html) | none (ISO 13606 mandated) | none | ISZI: system link, XML upload or web form (NCZI) |
| [Hungary](country-hungary.html) | none | none | quarterly provider reports, format by agreement (nrr.hu upload) |
| [Slovenia](country-slovenia.html) | limited core IG, not public, R4 | none | active registration from HIS lists, Register raka (OI Ljubljana) |
| [Croatia](country-croatia.html) | cezih.hr.cezih-osnova 1.0.x, R4 | none (ONKO+ message piloted, not deployed) | CEZIH messages + forms to HZJZ |
| [Romania](country-romania.html) | none | none | RNC created 2023 (INSP), format n/f |
| [Bulgaria](country-bulgaria.html) | none (NHIS XML/XSD APIs) | none | NHIS cancer database (draft ordinance 2025) |
| [Greece](country-greece.html) | hl7.fhir.gr.base-and-core-r5 0.0.1-draft, R5 (HL7 Hellas / Gnomon) | none; oncology registry hub by Gnomon, ENCR spec | National Registry of Neoplastic Diseases (IDIKA, Feb 2025), ENCR/ECIS aligned |
| [Cyprus](country-cyprus.html) | none (eHealth4U prototype package) | none | Cyprus Cancer Registry (MoH), MECC coding |
| [Malta](country-malta.html) | none (openEHR national EHR) | none | DHIR registry, ENCR |

Details and source URLs are on the [country pages](countries.html).
