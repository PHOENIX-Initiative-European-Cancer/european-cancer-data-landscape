# Official terminology mappings for ECCDM implementers (as of 2026-11-19)
Live test 2026-11-19 on a local Snowstorm (SNOMED CT International plus German, Austrian, Swiss and LOINC-SNOMED editions): it serves eight implicit ConceptMaps, among them SNOMED→ICD-10 extended map (`http://snomed.info/sct?fhir_cm=447562003`), SNOMED→ICD-O simple map (`?fhir_cm=446608001`), SNOMED→ICD-10-CM complex map and the historical associations (SAME AS, REPLACED BY, POSSIBLY EQUIVALENT TO, ALTERNATIVE). `$translate` returned 254837009 Malignant neoplasm of breast → ICD-10 C50.9, and 82711006 Infiltrating duct carcinoma → ICD-O 8500/3. **Note for ECCDM:** the ICD-O map returns `system = http://hl7.org/fhir/sid/icd-o`, whereas ECCDM uses `http://terminology.hl7.org/CodeSystem/icd-o-3`; implementers translating from SNOMED must rewrite the system URI. The MII Ontoserver was unreachable (HTTP 503), so the German transition ConceptMaps were not test-loaded.

## What exists
| From → to | Publisher | Status | FHIR available? |
|---|---|---|---|
| ICD-10-GM yy → yy+1 | BfArM | official | MII SU-TermServ transition ConceptMaps (derived) |
| OPS yy → yy+1 | BfArM | official | MII SU-TermServ (derived) |
| CHOP yy → yy+1 | BFS | official | no |
| CIM-10 FR / CCAM version changes | ATIH | official change lists, not maps | no (SMT serves code systems only) |
| ICD-9-CM → ICD-10-IM and → CIPI (bidirectional) | Ministero della Salute | official, final "Delta" tables due end 2026 | no |
| ICD-9-CM ↔ ICD-10-CM (GEMs) | CMS | official, frozen 2018, US target | no |
| ICD-10 ↔ ICD-11 MMS | WHO | official, "not for direct conversion" | ICD API only |
| ICD-O-3/3.1 → 3.2; 3.2 → ICD-O-4 | IARC/WHO | official change lists | MII 2019 transition ConceptMap (derived) |
| ICD-O-2 → ICD-O-3 | SEER/IARC | official | no |
| UICC TNM 8 → 9 | UICC | official narrative, no code map | no |
| LOINC deprecated → replacement (MapTo) | Regenstrief | official | via $lookup |
| SNOMED inactive → active (historical associations) | SNOMED Intl + NRCs | official | implicit ConceptMaps on any SNOMED server |
| ATC yearly alterations | WHO CC / BfArM ATC-GM | official | MII ATC 2022 ConceptMap (derived) |
| SNOMED → ICD-10 WHO (extended map 447562003) | SNOMED Intl | official, rule-based 1:n | yes, `?fhir_cm=447562003` |
| SNOMED → ICD-10 UK and → OPCS-4.10 | NHS England | official | NHS England Ontoserver |
| SNOMED → ICD-10-CM | NLM | official | VSAC |
| DHD Diagnosethesaurus → SNOMED NL + ICD-10 | DHD/Nictiz/RIVM | validated (RIVM-authorised) | Nictiz NTS |
| SNOMED → ICD-10-BE | FPS Public Health | official | not found |
| SNOMED → ICD-O-3.1 (446608001) | SNOMED Intl | official, deprecation planned Q4 2026 | yes, `?fhir_cm=446608001` |
| SNOMED ↔ ICD-11 | SNOMED Intl / WHO | pilot draft | no |
| LOINC ↔ SNOMED (LOINC Ontology 2.82) | Regenstrief + SNOMED Intl | official | yes (Snowstorm, Ontoserver) |
| EDQM dose form → SNOMED | SNOMED Intl + EDQM | official | not found |
| ICD-O-3 → ICD-10 (IARCcrgTools) | IARC/IACR | validated registry tool | no |
| ICD-O-3 → ICCC-3 | IARC/SEER | official | no |
| ICD-10-GM → ORPHA (Alpha-ID-SE) | BfArM | official, legally mandated | CodeSystem only |
| ORPHA → ICD-10 / ICD-11 / SNOMED / OMIM | Orphanet | official, qualified links | no |
| PALGA legacy → SNOMED NL | PALGA + Nictiz | validated | Nictiz NTS |
| oBDS 3.0 value lists → SNOMED | MII KDS Onkologie | derived, preliminary | yes, 42 ConceptMaps |
| SNOMED procedures → ICHI | Belgian NRC (SNOClass) | pilot | demo ConceptMap |
| Many → OMOP standard (Athena) | OHDSI | derived-community | no (OMOP tables) |

## What does not exist
- No official SNOMED → OPS, CCAM, CHOP, NCSP or CIPI map. UK OPCS-4 is the only official SNOMED → national procedure map in Europe.
- No official SNOMED ↔ ICD-10-GM or SNOMED ↔ CIM-10 FR map from BfArM or ANS. Only the international map to WHO ICD-10 exists.
- No ADICAP → SNOMED alignment on the ANS SMT.
- No successor to the SNOMED → ICD-O-3.1 map for ICD-O-3.2 or ICD-O-4 after the planned deprecation.
- No production SNOMED ↔ ICD-11 map, and no Italian ICD-11 or SNOMED membership.
- No UICC-endorsed TNM → SNOMED/LOINC map, and no code-level TNM 8 → 9 table.
- No official oBDS → SNOMED map yet; BfArM and the Land cancer registries have announced it.
- No ATC ↔ SNOMED map; ATC ↔ EDQM is not a meaningful pairing.
- No official ICD-9-CM (Italian) → ICD-10 WHO map; Italian tables target ICD-10-IM.

## Recommendation for ECCDM
- **All countries:** rely on the SNOMED → ICD-10 WHO extended map, SNOMED historical associations, LOINC Ontology and LOINC MapTo; all are served as implicit ConceptMaps by SNOMED-capable servers.
- **DE:** use BfArM Überleitungen for ICD-10-GM/OPS (SU-TermServ ConceptMaps) and Alpha-ID-SE; treat MII oBDS → SNOMED ConceptMaps as preliminary until the BfArM/registry map appears.
- **FR:** only version change lists from ATIH exist; SNOMED ↔ CIM-10 FR, CCAM and ADICAP need community maps.
- **IT:** use the Ministry ICD-9-CM → ICD-10-IM/CIPI transcoding tables for 2027 transition; there is no SNOMED path at all.
- **NL:** use the DHD Diagnosethesaurus (SNOMED + ICD-10, RIVM-authorised) and the PALGA SNOMED refset via the Nictiz NTS.
- **PHOENIX gaps:** SNOMED ↔ national procedure classifications (OPS, CCAM, CIPI, CHOP), ICD-O-3.2/4 ↔ SNOMED after the 2026 deprecation, and TNM 9 coding; publish them as versioned FHIR ConceptMaps.
