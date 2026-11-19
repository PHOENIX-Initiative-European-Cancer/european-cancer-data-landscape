### Terminology versions

Which terminology, in which version, an implementer has to use for ECCDM data per country. Status 2026-11-19. Details and sources: [country pages](countries.html); raw data: [data/terminology-matrix.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/terminology-matrix.csv).

### What ECCDM binds

| Element | Code system | Strength | Value set | Note |
|---|---|---|---|---|
| Cancer diagnosis code (Condition.code) | ICD-10 or SNOMED CT expected | unbound | none | No value set; logical model gives no terminology |
| Body site / topography (Condition.bodySite) | ICD-O-3 topography recommended | unbound | none | Logical model comment: WG recommends ICD-O-3 and will monitor next versions |
| Histology and behaviour (Observation.value) | ICD-O-3 morphology recommended | unbound | none | Observation.code fixed to SNOMED 395531003 |
| Clinical or pathological stage type | SNOMED CT | required | ClinicalOrPathologicalVS | 260998006 / 261023001 |
| TNM components T N M | any (component.code and component.value are unbound CodeableConcepts) | unbound | none | No TNM code system and no element for the TNM edition |
| Treatment intent | SNOMED CT | required | CancerTreatmentIntentVS |  |
| Treatment setting | SNOMED CT | required | CancerTreatmentSettingVS |  |
| Surgery intent | SNOMED CT | required | SurgeryIntentVS |  |
| Systemic treatment type | SNOMED CT | extensible | SystemicTreatmentTypeVS | Targeted therapy code still to be confirmed |
| Radiotherapy procedure code | SNOMED CT | fixed | fixed code | 1287742003 |
| Disease status | SNOMED CT | required | DiseaseStatusVS |  |
| Extent type | SNOMED CT | required | ExtentTypeVS |  |
| Overall treatment response | SNOMED CT | required | OverallResponseVS |  |
| Vital status | SNOMED CT | required | DeadOrAliveVS |  |
| Comorbidities | SNOMED CT | extensible (inactive) | VsComorbiditiesSctI4rc (commented out) | Binding currently commented out in FSH |
| SNOMED CT expansion version | SNOMED CT International 900000000000207008 | pinned module | system-version | No release date pinned |

### Version matrix

Cells show the version in use. "*" = not backed by a primary source; "n/f" = not found; "no" = not used.

| Country | SNOMED CT | ICD-10 | ICD-O | TNM | LOINC | ATC | Procedures | Terminology server |
|---|---|---|---|---|---|---|---|---|
| [AT](country-austria.html) | AT extension 20260815 * | ICD-10 BMSGPK 2026 | ICD-O-3.2 | UICC 8 | LOINC 2.77 deAT | ATC German (WIdO) | n/f | TerminoloGit (FHIR-tx-at) |
| [BE](country-belgium.html) | BE extension 20260715 (pinned by BE Core 2.2.0) | ICD-10-BE 2025 (CM/PCS) | ICD-O-3 | UICC (edition n/f) | FPS Health LOINC subset (version n/f) | ATC (FPS ATC-to-CNK mapping) | ICD-10-BE PCS 2025 | FPS Ontoserver 6.25.1 |
| [BG](country-bulgaria.html) | no | MKB-10 (NHIS nomenclature CL011) | n/f | n/f | n/f | n/f | ICD-9 procedures (NHIS nomenclature CL054) | NHIS nomenclature API spec v1.5.36 (non-FHIR) |
| [HR](country-croatia.html) | n/f | MKB-10 (CEZIH) | MKB-O 3.1 | n/f (registry uses summary stage) | n/f | n/f | CEZIH procedure code list | national server in production (name n/f) |
| [CY](country-cyprus.html) |  |  |  |  |  |  |  |  |
| [CZ](country-czechia.html) | no national edition (CZ translation in progress) | MKN-10-CZ 2026 | MKN-O-3.2 | UICC 8 | n/f (CZ translation planned) | SÚKL DLP ATC | n/f | national server in development (NCEZ) |
| [DK](country-denmark.html) |  |  |  |  |  |  |  |  |
| [EE](country-estonia.html) |  |  |  |  |  |  |  |  |
| [FI](country-finland.html) |  |  |  |  |  |  |  |  |
| [FR](country-france.html) | FR edition 20260621 (on INT May 2026) | CIM-10 FR à usage PMSI 2026 | CIM-O-3 (revision 3.1 vs 3.2 not stated by Francim/RNC) | UICC 8 (registries, e.g. Aquitaine); UICC 7 cited in CI-SIS Fiche RCP 2025.01 | LOINC Biologie FRA 2.24 (on LOINC 2.81) | ATC 2026-02 (SMT) | CCAM v84.00 | ANS SMT FTS (Ontoserver 6.28), release 14 (Sep 2026), in HL7 tx-registry |
| [DE](country-germany.html) | DE edition 20260815 | ICD-10-GM 2026 | ICD-O-3 Zweite Revision 2019 (=ICD-O-3.2) | UICC 8 and UICC 9 (oBDS TNM-Version 6/7/8/9) | LOINC 2.83 deDE | ATC-DE amtlich 2026 (WIdO/BfArM) | OPS 2026 | BfArM ZTS Stage 1 (NPM package API, no FHIR $lookup/$expand); MII Ontoserver (mTLS, Germany only) |
| [GR](country-greece.html) |  |  |  |  |  |  |  |  |
| [HU](country-hungary.html) | n/f | BNO-10 | n/f | UICC 8 (UICC 7 for prostate) | n/f | n/f | OENO | n/f |
| [IS](country-iceland.html) |  |  |  |  |  |  |  |  |
| [IE](country-ireland.html) | IE edition 20260621 | ICD-10-AM 12th edition (HIPE) | ICD-O-3.2 | UICC 7 | n/f | WHO ATC (HSE PCRS) | ACHI 12th edition (HIPE); NCRI uses ACHI 6th edition for treatments | HSE Central Terminology Service (Ontoserver; Dedalus) |
| [IT](country-italy.html) | no | ICD-9-CM 2007 in SDO/FSE; ISTAT mortality ICD-10 v2019 | ICD-O-3 (3.1 or 3.2 accepted; Italian ed. Inferenze 2005) | any UICC/AJCC edition 1-8, edition recorded (no national mandate) | LOINC itIT variant (IIT-CNR); variant version n/f, UMLS lower bound 2.75 | ATC (AIFA) in HL7 Italia Terminology IG 0.1.2 | ICD-9-CM 2007 procedures (SDO) | no |
| [LV](country-latvia.html) |  |  |  |  |  |  |  |  |
| [LT](country-lithuania.html) |  |  |  |  |  |  |  |  |
| [LU](country-luxembourg.html) | member since 2018; national edition n/f | ICD-10-CM via ICD-10-BE 2025 manual | ICD-O-3 (revision n/f) | UICC 7 (2020 report; later edition n/f) | n/f | n/f | ICD-10-PCS via ICD-10-BE 2025 manual | n/f |
| [MT](country-malta.html) |  |  |  |  |  |  |  |  |
| [NL](country-netherlands.html) | NL edition 20261031 | ICD-10 NL 2021 + errata 2024-1 | ICD-O-3 (Flemish/Dutch translation; ICD-O-3.2 English only) | UICC 8 (since 2017) | Nederlandse Labcodeset on LOINC 2.83 | WHO ATC via G-Standaard (yearly ATC update on 1 Feb) | DHD Verrichtingenthesaurus 3.3 (SNOMED-based); NZa DBC codelijst | Nationale Terminologieserver (Ontoserver, Nictiz) |
| [NO](country-norway.html) |  |  |  |  |  |  |  |  |
| [PL](country-poland.html) | no | ICD-10 PL 2008 | ICD-O-3 PL edition | UICC 8 | LOINC 2.81 plPL | n/f | ICD-9-PL | none (planning stage) |
| [PT](country-portugal.html) |  |  |  |  |  |  |  |  |
| [RO](country-romania.html) | no | ICD-10-AM 3rd ed (DRG) and CIM-10 | ICD-O-3 (CIM-O-3) | n/f | n/f | n/f | n/f | n/f |
| [SK](country-slovakia.html) | n/f | MKCH-10 | MKCH-O-3.2 | UICC 9 | n/f | n/f | n/f | no |
| [SI](country-slovenia.html) | n/f (SI translation discussed 2024) | MKB-10-AM v11 | n/f | n/f | n/f | n/f | n/f | national FHIR terminology server in development |
| [ES](country-spain.html) |  |  |  |  |  |  |  |  |
| [SE](country-sweden.html) |  |  |  |  |  |  |  |  |
| [CH](country-switzerland.html) | CH extension 20260607 * | ICD-10-GM 2024 (coding year 2026) | ICD-O-3 (version recorded per case, NKRS var. 3.2) | UICC (edition recorded per case, NKRS var. 4.1) | n/f | n/f | CHOP 2026 | tx.fhir.ch (HL7 Switzerland) |
| [GB](country-united-kingdom.html) | UK Clinical Edition 43.0.1 | ICD-10 5th edition | ICD-O-3 (revision n/f) * | UICC 8 | no | n/f | OPCS-4.11 | NHS England Terminology Server (Ontoserver); NHS Scotland Terminology Server |

### FHIR system URIs

| Terminology | Coding.system | Countries |
|---|---|---|
| ATC | `http://fhir.de/CodeSystem/bfarm/atc` | DE |
| ATC | `http://www.whocc.no/atc` | BE, CH, GB, IE, LU, NL |
| ATC | `https://smt.esante.gouv.fr/terminologie-atc` | FR |
| ATC | `https://sukl.cz/terminology/CodeSystem/dlp-atc` | CZ |
| ATC | `https://termgit.elga.gv.at/CodeSystem/atc-deutsch-wido` | AT |
| ATC | `https://www.hl7.it/fhir/terminology/CodeSystem/aifa-atc` | IT |
| Drug code | `http://fhir.cezih.hr/specifikacije/CodeSystem/HALMED-lista-lijekova` | HR |
| Drug code | `http://fhir.de/CodeSystem/ifa/pzn` | DE |
| Drug code | `http://snomed.info/sct` | IE |
| Drug code | `https://dmd.nhs.uk` | GB |
| Drug code | `https://smt.esante.gouv.fr/terminologie-bdpm` | FR |
| Drug code | `https://sukl.cz/terminology/CodeSystem/dlp-lecivepripravky` | CZ |
| Drug code | `https://termgit.elga.gv.at/CodeSystem/asp-liste` | AT |
| Drug code | `https://www.ehealth.fgov.be/standards/fhir/medication/NamingSystem/cnk-codes` | BE |
| Drug code | `https://www.hl7.it/fhir/terminology/CodeSystem/aifa-aic` | IT |
| Drug code | `urn:oid:2.16.840.1.113883.2.4.4.8` | NL |
| Drug code | `urn:oid:2.51.1.1` | CH |
| ICD-10 | `http://fhir.cezih.hr/specifikacije/CodeSystem/icd10-hr` | HR |
| ICD-10 | `http://fhir.de/CodeSystem/bfarm/icd-10-gm` | DE |
| ICD-10 | `http://fhir.de/CodeSystem/dimdi/icd-10-gm` | CH |
| ICD-10 | `http://hl7.org.pl/fhir/CodeSystem/pl-icd10Condition-CS` | PL |
| ICD-10 | `http://hl7.org/fhir/sid/icd-10` | GB, IT |
| ICD-10 | `http://hl7.org/fhir/sid/icd-10-cm` | LU |
| ICD-10 | `http://hl7.org/fhir/sid/icd-10-nl` | NL |
| ICD-10 | `https://smt.esante.gouv.fr/terminologie-cim-10` | FR |
| ICD-10 | `https://termgit.elga.gv.at/CodeSystem/icd-10-bmsgpk-2025` | AT |
| ICD-10 | `https://uzis.cz/terminology/CodeSystem/mkn-10` | CZ |
| ICD-11 | `http://id.who.int/icd/release/11/mms` | AT, BE, BG, CH, CZ, DE, GB, HR, HU, IE, IT, LU, NL, PL, RO, SI, SK |
| ICD-11 | `https://smt.esante.gouv.fr/terminologie-cim11-mms` | FR |
| ICD-O | `http://terminology.hl7.org/CodeSystem/icd-o-3` | AT, BE, BG, CH, CZ, DE, FR, GB, HR, HU, IE, IT, LU, PL, RO, SI, SK |
| ICD-O | `urn:oid:2.16.840.1.113883.6.43.1` | NL |
| LOINC | `http://loinc.org` | AT, BE, BG, CH, CZ, DE, FR, GB, HR, HU, IE, IT, LU, NL, PL, RO, SI, SK |
| Pathology coding | `http://snomed.info/sct` | GB, IE, NL |
| Pathology coding | `http://terminology.hl7.org/CodeSystem/icd-o-3` | DE, IT |
| Procedures | `http://fhir.cezih.hr/specifikacije/CodeSystem/kodna-lista-procedura` | HR |
| Procedures | `http://fhir.de/CodeSystem/bfarm/ops` | DE |
| Procedures | `http://hl7.org.pl/fhir/CodeSystem/pl-icd9plServiceCode-CS` | PL |
| Procedures | `http://hl7.org/fhir/sid/icd-9-cm` | IT |
| Procedures | `http://snomed.info/sct` | NL |
| Procedures | `http://www.cms.gov/Medicare/Coding/ICD10` | LU |
| Procedures | `https://smt.esante.gouv.fr/terminologie-ccam` | FR |
| SNOMED CT | `http://snomed.info/sct` | AT, BE, BG, CH, CZ, DE, FR, GB, HR, HU, IE, IT, LU, NL, PL, RO, SI, SK |
| UCUM | `http://unitsofmeasure.org` | AT, BE, BG, CH, CZ, DE, FR, GB, HR, HU, IE, IT, LU, NL, PL, RO, SI, SK |

### Upcoming changes

| Country | Terminology | Change |
|---|---|---|
| DE | ATC | ATC-DE 2027 from 2027-01-01 |
| NL | ATC | ATC update 2027-02-01 |
| FR | Drug code | monthly UCD/CIP and BDPM releases |
| GB | Drug code | GTINs added in Monolith 43.1.0 (2026-10-28) |
| NL | Drug code | monthly G-Standaard release |
| AT | ICD-10 | ICD-10 BMSGPK 2027 from 2027-01-01 |
| CH | ICD-10 | ICD-10-GM 2026 from 2027-01-01 (Swiss supplement 2026-10-27) |
| DE | ICD-10 | none before ICD-10-GM 2029 (three-year cycle; no 2027 edition) |
| FR | ICD-10 | annual ATIH edition (CIM-10 FR 2027, date n/f) |
| IE | ICD-10 | 13th edition adoption n/f |
| IT | ICD-10 | ICD-10-IM replaces ICD-9-CM in all flows from 2027-01-01 (DM 23 Oct 2025) |
| FR | ICD-11 | CIM-11 switch horizon 2031 (ATIH) |
| NL | ICD-11 | no adoption date found (RIVM 2023 plan targeted completion 2027) |
| DE | ICD-O | ICD-O-4 in oBDS 3.1.0, accepted by registries from 2027-04-01 |
| IT | ICD-O | EdizioneICD-O field foresees value 4 'in futuro' (no date) |
| NL | ICD-O | ICD-O-4 introduced in the NKR during 2026 (IKNL Jaarplan) |
| DE | LOINC | monthly LOINC releases from March 2027 |
| FR | LOINC | semi-annual LOINC Bio FR update (next n/f) |
| IT | LOINC | semi-annual Italian update by IIT-CNR |
| NL | LOINC | monthly LOINC releases from March 2027 |
| DE | Pathology coding | ICD-O-4 morphology in oBDS 3.1.0 from 2027-04-01 |
| NL | Pathology coding | monthly Nictiz pathology change lists |
| CH | Procedures | CHOP 2027 from 2027-01-01 (published 2026-07-30) |
| DE | Procedures | OPS 2027 from 2027-01-01 (final 2026-10-28) |
| FR | Procedures | next CCAM version (CNAM, date n/f) |
| IT | Procedures | CIPI replaces ICD-9-CM procedures from 2027-01-01 (DM 23 Oct 2025) |
| AT | SNOMED CT | next AT release n/f (Managed Service; Nov and May releases seen) |
| BE | SNOMED CT | monthly BE releases on the 15th (except Jan and Aug) |
| CH | SNOMED CT | next CH release Dec 2026 (June and December cycle) |
| DE | SNOMED CT | next National Edition 15 Nov (semi-annual 15 May/15 Nov) |
| FR | SNOMED CT | next annual FR edition (June cycle; date n/f) |
| GB | SNOMED CT | monthly minor releases; next major 44.0.0 n/f |
| IT | SNOMED CT | accession foreseen by FSE decree 2022, not done |
| NL | SNOMED CT | monthly NL release (November 2026 notes not yet published) |
| CZ | TNM | UICC 9 in NOR from 2027-01-01 |
| DE | TNM | TNM 9 additions (LV, B, IB3) in oBDS 3.1.0 from 2027-04-01 |
| FR | TNM | UICC 9 (effective 2026-01-01 per UICC; French adoption n/f) |
| IE | TNM | no move to TNM 8 announced |
| IT | TNM | TNM 9 not admitted in PN REG field design (1-8 or 99) |
| NL | TNM | TNM 9 prescribed for lung cancer (guideline); NKR-wide switch date n/f |
| CH | Terminology server | national government server recommended by eHealth Suisse (no date) |
| DE | Terminology server | ZTS Stage 2 (medication/ePA code systems), FHIR operations at Stage 3+ |
| LU | Terminology server | in planning (State of FHIR 2026) |

### Value set completeness

ECCDM's nine value sets contain 25 SNOMED CT concepts. All 25 are active in SNOMED CT International 2026-10-01. Each value set matches the "Choice" list in the working group's logical model (Cancer_Common_Logical_Model_20260521.xlsx) one-to-one, so nothing the model intended is missing. The table compares them with what a national registry dataset records, using the German oBDS 3.0.5 schema as the reference. NKR, OSIRIS and ENCR value lists were not compared.

| Value set (strength) | ECCDM codes | Values in oBDS 3.0.5 that ECCDM cannot express | Semantic issues |
|---|---|---|---|
| CancerTreatmentIntentVS (required) | Curative, Palliative | Radiotherapy: local curative in oligometastasis; all modalities: other, not stated | Model says "Definitive", the code says "Curative" |
| SurgeryIntentVS (required) | Curative, Palliative | Diagnostic, revision/complication, other, not stated | Same |
| CancerTreatmentSettingVS (required) | Single episode, Preoperative, Postoperative period, Simultaneous | Intraoperative, additive, other | "Single episode" does not mean "without relation to surgery"; "Preoperative" and "Postoperative period" are timing qualifiers, not neoadjuvant/adjuvant intent |
| SystemicTreatmentTypeVS (extensible) | Chemotherapy, Immunotherapy, Hormone therapy | Targeted therapy (noted as to-do in the FSH), combinations (chemo+immuno, chemo+targeted, …), stem-cell transplantation, active surveillance, wait and see, watchful waiting, other | Extensible strength lets implementers add codes, but nothing standardises them |
| OverallResponseVS (required) | Full remission, Partial remission, Tumour progression, Patient condition unchanged | Divergent response, clinical improvement, complete remission with residual findings, recurrence, not assessable, not stated | "Stable disease" is coded as a general finding, not a response concept |
| DiseaseStatusVS (required) | Recurrent episode, Full remission, Partial remission, Tumour progression, Patient condition unchanged | No tumour detectable, residual tumour, questionable finding, unknown (oBDS records these separately for local, nodal and distant status) | Mixes qualifier values and findings |
| ExtentTypeVS (required) | Regional, Local, Neoplasm metastatic | Unknown | Model says "Loco-regional", the code is "Regional"; "Metastatic" is a morphologic abnormality, the others are qualifier values |
| ClinicalOrPathologicalVS (required) | Clinical staging, Pathological staging | Post-therapy (y) and recurrence (r) staging, which TNM and oBDS record | |
| DeadOrAliveVS (required) | Alive, Dead | Unknown / lost to follow-up | |

Elements with no value set at all: cancer diagnosis code, body site (ICD-O-3 topography recommended in a comment), histology and behaviour (ICD-O-3 morphology recommended), tumour grade system, sex at diagnosis, comorbidities (binding commented out), stage classification type, TNM components, imaging type and body site, cause of death, loco-regional and metastatic sites, surgery and radiotherapy body site.

What this means:

* None of the required value sets has an "other" or "unknown" code. Registry data with these values can only use `dataAbsentReason`, which loses the distinction between "not done", "unknown" and "other".
* With required strength, every oBDS value outside the list fails validation. Seven of nine value sets would need either more codes or extensible strength to carry German registry data without loss.
* The largest content gaps are targeted therapy and therapy combinations, intraoperative and additive treatment setting, and the y/r staging prefixes.

### SNOMED CT translation coverage (measured)

Active concepts with at least one term in the language reference set, counted on 2026-11-19 with ECL description filters (`<<X {{ D dialectId = <refset> }}`) on a local Snowstorm holding the International edition 20261001 and the German (20260815), Austrian (20260815) and Swiss (20260607) editions. "ECCDM SNOMED codes" are the 25 SNOMED concepts used in ECCDM value sets and fixed codes.

| Hierarchy | de-DE | de-AT | de-CH | fr-CH | it-CH |
|---|---|---|---|---|---|
| malignant neoplastic disease | 5,379 / 6,176 (87 %) | 5,379 / 6,176 (87 %) | 2,605 / 6,177 (42 %) | 4,571 / 6,177 (74 %) | 373 / 6,177 (6 %) |
| morphologic abnormality | 28 / 5,279 (1 %) | 28 / 5,279 (1 %) | 28 / 5,269 (1 %) | 238 / 5,269 (5 %) | 17 / 5,269 (0 %) |
| body structure | 68 / 45,089 (0 %) | 68 / 45,089 (0 %) | 62 / 43,637 (0 %) | 6,966 / 43,637 (16 %) | 23 / 43,637 (0 %) |
| procedure | 23,174 / 60,698 (38 %) | 23,175 / 60,699 (38 %) | 22,705 / 59,975 (38 %) | 33,171 / 59,975 (55 %) | 1,205 / 59,975 (2 %) |
| observable entity | 203 / 11,052 (2 %) | 205 / 11,052 (2 %) | 199 / 11,033 (2 %) | 4,169 / 11,033 (38 %) | 122 / 11,033 (1 %) |
| qualifier value | 861 / 12,469 (7 %) | 861 / 12,469 (7 %) | 934 / 12,461 (7 %) | 3,964 / 12,461 (32 %) | 409 / 12,461 (3 %) |
| ECCDM SNOMED codes | 6 / 25 (24 %) | 6 / 25 (24 %) | 6 / 25 (24 %) | 21 / 25 (84 %) | 2 / 25 (8 %) |

ECCDM SNOMED codes without a term, per language ("x" = missing):

| Code | Preferred term (en) | de-DE | de-AT | de-CH | fr-CH | it-CH |
|---|---|---|---|---|---|---|
| 255470001 | Local | x | x | x | x | x |
| 14799000 | Neoplasm, metastatic | x | x | x | x | x |
| 410674003 | Regional | x | x | x | x | x |
| 438949009 | Alive | x | x | x |  | x |
| 413744002 | Cancer screening follow up | x | x | x |  | x |
| 260998006 | Clinical staging | x | x | x |  | x |
| 373808002 | Curative - procedure intent | x | x | x |  | x |
| 169413002 | Hormone therapy | x | x | x |  | x |
| 360037004 | Imaging - action | x | x | x |  | x |
| 103338009 | In full remission | x | x | x |  | x |
| 103337004 | In partial remission | x | x | x |  | x |
| 395531003 | Neoplasm observable | x | x | x |  | x |
| 363676003 | Palliative intent | x | x | x |  | x |
| 261023001 | Pathological staging | x | x | x |  | x |
| 359748005 | Patient condition unchanged | x | x | x |  | x |
| 263853000 | Recurrent episode | x | x | x |  | x |
| 79970003 | Simultaneous | x | x | x |  | x |
| 229803000 | Single episode | x | x | x |  | x |
| 419835002 | Tumor progression | x | x | x |  | x |
| 262061000 | Postoperative period |  |  |  | x | x |
| 76334006 | Immunological therapy |  |  |  |  | x |
| 262068006 | Preoperative |  |  |  |  | x |
| 1287742003 | Radiotherapy |  |  |  |  | x |

### Translations per code system (published figures)

| SNOMED CT | Release | Translated | % of active |
|---|---|---|---|
| nl-BE / fr-BE / de-BE | 20261115 | 306,827 / 292,415 / 118,272 PT | 79.0 / 75.3 / 30.5 |
| sv (SE) | 20261130 | 333,228 concepts (count from 2018) | near-full |
| nl (NL) | 20261031 | 298,826 concepts | ~75 |
| fr (FR) / fr (CH) | 20260621 / 20260607 | 224,102 / 210,678 concepts | 58.8 / 55.4 |
| es (Spanish Edition) | 20261110 | full edition (446,009 UMLS concepts) | ~100 |
| de (DE / AT / CH) | 20260815 / 20260815 / 20260607 | 130,795 / 130,880 / 118,922 concepts | 34 / 34 / 31 |
| cs / lt / it (CH) | in progress / 2015 / 20260607 | 100,602 / 40,000 / 18,380 concepts | n/f / n/f / 4.8 |
| da, nb/nn, et, fi; pt, sk, sl, hr, lv, hu, is | 2026 releases; no release for the second group | n/f (DK PT only; EE, FI subsets); 0 | n/f; 0 |

| LOINC 2.83 variant | UMLS concepts | LOINC 2.83 variant | UMLS concepts |
|---|---|---|---|
| it-IT | 97,188 | fr-BE | 43,783 |
| el-GR | 92,664 | et-EE | 29,857 |
| es-ES | 67,093 | de-DE | 18,716 |
| fr-FR | 65,973 | de-AT | 7,206 |
| nl-NL | 63,729 | cs-CZ / pl-PL | 62,976 / 45,495 |
| base LOINC (en) | 254,788 | Nordic, pt-PT, other CEE | no variant |

| ICD / ICD-O | Languages and status |
|---|---|
| ICD-11 MMS 2026-01 | cs, de (prerelease), en, es, fr, pt, sk, sv full. et, fi, it partial (ICF only, foundation partial). Others pending |
| ICD-10 | National versions in all 31 countries. EN originals used in UK, IE, PT, LU, MT |
| ICD-O-3.x | WHO lists cs, de, en, es, fi, fr, nl, pt, ro (+non-EU). 3.2 nationally: de, es, cs, sk, lv, sv. fr only 3.0 |
| ICD-O-4 | English tables only (IARC 2026). No translations yet. oBDS 3.1 already carries it |

| Other | Languages |
|---|---|
| EDQM Standard Terms / MedDRA 29.0 | EDQM 35 languages, all EU official plus is, no. MedDRA 20 EU/EEA languages at full parity |
| ATC / UCUM | WHO English. ATC-GM (de) official. UCUM has no translations; BfArM deDE covers common units only |
| HPO / ORPHAcodes / OncoTree | HPO 18 language profiles. ORPHA multilingual, list n/f. OncoTree English only |
| UICC TNM | 9th ed. English only so far. Czech TNM 9 planned. 8th ed. has unnamed translations |

**What it means for ECCDM**
- Counts hide the hierarchy skew. German covers 61 % of findings but 6.9 % of qualifier values, 0.6 % of staging and scales and 0.2 % of body structures. ECCDM bindings sit mostly in those three hierarchies.
- The check was run on ECCDM's 32 SNOMED codes. German has 10 of 32, Swiss French 28, Swiss Italian 5. Remission status, treatment intent, clinical vs pathological staging, local vs regional, episode qualifiers and "Alive" lack German terms (eccdm-sct-check.tsv in this folder).
- Suggested check: expand every ECCDM SNOMED value set against each national edition with `displayLanguage=<lang>` and count codes whose display falls back to English. Use the FR SMT, Nictiz NTS, BE, SE, DK and NO servers to extend it.
- LOINC, ICD-O-4 and TNM 9 translations are the hard gaps. There are no Nordic LOINC variants, ICD-O-4 is English only and TNM 9 has no translations. ECCDM should ship English displays plus designation slots and not assume national display text.


Note: the measured table above counts the 25 SNOMED codes in ECCDM's profiles and value sets (6 with a German term). A separate check of 32 codes, which adds 7 codes used only in ECCDM example instances, found 10 with a German term; both show the same gap.

### Official mappings between terminologies

Live test 2026-11-19 on a local Snowstorm (SNOMED CT International plus German, Austrian, Swiss and LOINC-SNOMED editions): it serves eight implicit ConceptMaps, among them SNOMED→ICD-10 extended map (`http://snomed.info/sct?fhir_cm=447562003`), SNOMED→ICD-O simple map (`?fhir_cm=446608001`), SNOMED→ICD-10-CM complex map and the historical associations (SAME AS, REPLACED BY, POSSIBLY EQUIVALENT TO, ALTERNATIVE). `$translate` returned 254837009 Malignant neoplasm of breast → ICD-10 C50.9, and 82711006 Infiltrating duct carcinoma → ICD-O 8500/3. **Note for ECCDM:** the ICD-O map returns `system = http://hl7.org/fhir/sid/icd-o`, whereas ECCDM uses `http://terminology.hl7.org/CodeSystem/icd-o-3`; implementers translating from SNOMED must rewrite the system URI. The MII Ontoserver was unreachable (HTTP 503), so the German transition ConceptMaps were not test-loaded.

### What exists
| From → to | Publisher | Status | FHIR available? |
|---|---|---|---|
| ICD-10-GM edition → next edition (yearly until 2026, then three-yearly: next 2029) | BfArM | official | MII SU-TermServ transition ConceptMaps (derived) |
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

### What does not exist
- No official SNOMED → OPS, CCAM, CHOP, NCSP or CIPI map. UK OPCS-4 is the only official SNOMED → national procedure map in Europe.
- No official SNOMED ↔ ICD-10-GM or SNOMED ↔ CIM-10 FR map from BfArM or ANS. Only the international map to WHO ICD-10 exists.
- No ADICAP → SNOMED alignment on the ANS SMT.
- No successor to the SNOMED → ICD-O-3.1 map for ICD-O-3.2 or ICD-O-4 after the planned deprecation.
- No production SNOMED ↔ ICD-11 map, and no Italian ICD-11 or SNOMED membership.
- No UICC-endorsed TNM → SNOMED/LOINC map, and no code-level TNM 8 → 9 table.
- No official oBDS → SNOMED map yet; BfArM and the Land cancer registries have announced it.
- No ATC ↔ SNOMED map; ATC ↔ EDQM is not a meaningful pairing.
- No official ICD-9-CM (Italian) → ICD-10 WHO map; Italian tables target ICD-10-IM.

### Recommendation for ECCDM
- **All countries:** rely on the SNOMED → ICD-10 WHO extended map, SNOMED historical associations, LOINC Ontology and LOINC MapTo; all are served as implicit ConceptMaps by SNOMED-capable servers.
- **DE:** use BfArM Überleitungen for ICD-10-GM/OPS (SU-TermServ ConceptMaps) and Alpha-ID-SE; treat MII oBDS → SNOMED ConceptMaps as preliminary until the BfArM/registry map appears.
- **FR:** only version change lists from ATIH exist; SNOMED ↔ CIM-10 FR, CCAM and ADICAP need community maps.
- **IT:** use the Ministry ICD-9-CM → ICD-10-IM/CIPI transcoding tables for 2027 transition; there is no SNOMED path at all.
- **NL:** use the DHD Diagnosethesaurus (SNOMED + ICD-10, RIVM-authorised) and the PALGA SNOMED refset via the Nictiz NTS.
- **PHOENIX gaps:** SNOMED ↔ national procedure classifications (OPS, CCAM, CIPI, CHOP), ICD-O-3.2/4 ↔ SNOMED after the 2026 deprecation, and TNM 9 coding; publish them as versioned FHIR ConceptMaps.

Full list: [data/terminology-mappings.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/terminology-mappings.csv).
