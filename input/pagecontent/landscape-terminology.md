### Terminology landscape

Which terminologies, and which national variants and versions, are in use for oncology data. "n/f" = not found in a public source. Machine-readable copy: [data/terminology-landscape.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/terminology-landscape.csv).

| Country | SNOMED CT | ICD-10 variant (current) | ICD-O | TNM | LOINC | Terminology server |
|---|---|---|---|---|---|---|
| [Germany](country-germany.html) | member 2021, BfArM, DE edition May/Nov | ICD-10-GM 2026 | ICD-O-3 2nd rev 2019 (ICD-O-4 2026 planned in oBDS) | UICC 8, TNM 9 in oBDS 3.0.5 | deDE15 variant, LOINC 2.83 | BfArM Zentraler Terminologieserver (Dec 2024) |
| [Austria](country-austria.html) | member 2019, ELGA, AT extension Nov 2025/May 2026 | ICD-10 BMSGPK 2026 | ICD-O-3 rev 2 since 2020 | UICC 8 | LOINC DE-AT 2.77 | TerminoloGit / tergi (ELGA) |
| [Switzerland](country-switzerland.html) | member 2016, eHealth Suisse, CH ext 2026-06 | ICD-10-GM (BFS), CHOP 2026 | ICD-O-3 (ed n/f) | n/f | n/f | tx.fhir.ch (HL7 CH), no government server |
| [Netherlands](country-netherlands.html) | charter 2007, Nictiz, monthly NL edition | ICD-10 NL 2021 (RIVM) | ICD-O-3 NL | UICC 8 since 2017 | Labcodeset on 2.83 | Nationale Terminologieserver (Ontoserver) |
| [Belgium](country-belgium.html) | NRC FPS Health, monthly BE release since Nov 2024 | ICD-10-BE (CM/PCS) 2023 handbook | ICD-O-3 | n/f | n/f | FPS Ontoserver apps.health.belgium.be |
| [France](country-france.html) | member 2023, ANS, FR edition Feb 2025 annual | CIM-10 FR PMSI 2026 (ATIH) | CIM-O-3 | UICC 9 per UICC 2026, FR adoption n/f | LOINC Bio FR | SMT (ANS) |
| [Italy](country-italy.html) | not a member | ICD-9-CM 2007 (SDO), ICD-10 mortality | ICD-O-3.2 (AIRTUM) | TNM 8 (AIRTUM) | IT translation 2.75 (CNR) | none |
| [Spain](country-spain.html) | member, MoH, ES edition Apr/Oct | CIE-10-ES 6th ed 2026 | CIE-O-3.2 from 2026-01-01 | n/f | LOINC ES 2.77 | SNS Servidor de Terminologías (production) |
| [Portugal](country-portugal.html) | member 2014, SPMS CTC | ICD-10-CM/PCS since 2017 | ICD-O-3 | n/f | n/f | none (tender 2026) |
| [Luxembourg](country-luxembourg.html) | member 2018, eSanté | ICD-10-CM/PCS via ICD-10-BE manual | n/f | n/f | n/f | planning |
| [United Kingdom](country-united-kingdom.html) | founder, NHS England, UK edition (Drug ext 42.1.0 May 2026) | ICD-10 5th ed; OPCS-4.11 Apr 2026 | ICD-O-3 | TNM 8 since 2018 | none (SNOMED UTL) | NHS England Ontoserver; NHS Scotland server |
| [Ireland](country-ireland.html) | member 2016, HSE, IE edition (Jun 2026) | ICD-10-AM 12th ed (HIPE 2024) | ICD-O-3.2 since 2020 | TNM 7 since 2014 (NCRI) | on HSE CTS | HSE Central Terminology Service (beta 2025/26) |
| [Denmark](country-denmark.html) | charter 2007, SDS, DK ext Sep 2025 | SKS ICD-10 | ICD-O-3 | n/f (cTNM mandatory in LPR3) | NPU + LOINC profiles | planning; tx-nordics shared |
| [Sweden](country-sweden.html) | charter 2007, Socialstyrelsen, SE ext Nov 2025 | ICD-10-SE 2026 (13th), ICD-11 deaths 2027 | ICD-O-3.2 (2019) | latest UICC (ed n/f) | n/f | Inera Terminologitjänst (production) |
| [Norway](country-norway.html) | member 2017, Helsedirektoratet | ICD-10 NO 2026 | n/f | n/f | NPU | in development |
| [Finland](country-finland.html) | member 2018, THL, FI edition Dec | THL ICD-10, ICD-11 from 2028 | n/f | n/f | n/f | planning (Koodistopalvelu not FHIR) |
| [Iceland](country-iceland.html) | member 2011, Directorate of Health | ICD-10 IS 2014 | n/f | n/f | n/f | in development |
| [Estonia](country-estonia.html) | member 2010, TEHIK, EE edition | RHK-10 | ICD-O-3 since 2008 | n/f | EE variant 2.77 | TEHIK Ontoserver (production) |
| [Latvia](country-latvia.html) | member Jan 2026, SPKC; GPS in use | SSK-10 | n/f | n/f | planned | production (operator n/f) |
| [Lithuania](country-lithuania.html) | charter 2007, Medical Library | TLK-10-AM since 2019 | ICD-O-3 (lab IG) | pTNM in lab IG, ed n/f | yes (lab IG) | tx.hl7.lt |
| [Poland](country-poland.html) | not a member | ICD-10 PL 2008 (CeZ) | ICD-O-3 PL (KRN) | TNM 8 | PL translation in 2.81 | planning |
| [Czechia](country-czechia.html) | member 2012, ÚZIS NRC 2020, CZ translation in progress | MKN-10-CZ 2026 | MKN-O-3.2 | TNM 8; TNM 9 in NOR from 2027 | planned | in development |
| [Slovakia](country-slovakia.html) | member 2009, NCZI | MKCH-10 | MKCH-O-3.2 since 2020 | TNM 8 / 9 (2026 guidance) | n/f | none planned |
| [Hungary](country-hungary.html) | member Sep 2024, ESZFK | BNO-10 | n/f | n/f | n/f | n/f |
| [Slovenia](country-slovenia.html) | member 2010, NIJZ | MKB-10-AM v11 since 2023 | n/f | n/f | n/f | in development |
| [Croatia](country-croatia.html) | member 2023, MoH | MKB-10 | n/f | n/f | n/f | production (name n/f) |
| [Romania](country-romania.html) | not a member | ICD-10-AM 3rd ed (DRG), CIM-10 | n/f | n/f | n/f | n/f |
| [Bulgaria](country-bulgaria.html) | not a member | ICD-10 as NHIS nomenclature CL011 | n/f | n/f | n/f | n/f |
| [Greece](country-greece.html) | not a member | ICD-10-GrM 2017 v2 (from ICD-10-GM 2013), mandatory in ePrescription 2024 | ICD-O-3 implied by ENCR | n/f | none | under development |
| [Cyprus](country-cyprus.html) | member 2018, NeHA | ICD-10 mix with ICPC/CPT-4 | ICD-O-3 | ed n/f | partial | planning |
| [Malta](country-malta.html) | member 2011, MoH IMU | ICD-10 | ICD-O-3 | n/f | n/f | n/f |

Details and source URLs are on the [country pages](countries.html).
