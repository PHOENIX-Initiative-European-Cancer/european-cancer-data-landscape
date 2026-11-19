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

The version matrix is being compiled.
