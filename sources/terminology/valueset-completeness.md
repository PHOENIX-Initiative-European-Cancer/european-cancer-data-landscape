# Value set completeness

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
