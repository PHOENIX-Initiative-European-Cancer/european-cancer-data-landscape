# Rerun of failed steps (2026-11-19, afternoon)

| Item | Outcome | Evidence |
|---|---|---|
| Belgian SNOMED CT translation totals | VERIFIED: Belgian Edition 20261115 (packaged with Nov 2026 International): French 292,415 preferred terms, 75.29 % of active concepts; Dutch 306,827, 79.00 %; German 118,272, 30.45 %; 24 new Belgian concepts | https://conf.spaces.snomed.org/wiki/spaces/RMT/pages/1468334117 (read in browser) |
| Translation totals for SE, AT, IE, NO, EE, ES, CH | STILL NOT FOUND, now confirmed from primary pages: the November 2026 release notes give per-release changes only, not running totals (e.g. AT 20261115 on International Oct 2026 lists 7,310 changed translations, 6,176 of them clinical findings) | SNOMED RMT wiki pages 1413316748, 1468858405, 1500053541, 1414201388, 1455718444, 1441431619, 926416899 |
| ANS CI-SIS cancer volets (esante.gouv.fr was in maintenance) | VERIFIED live, page updated 2026-11-10: CANCER-FRCP 2025.01 and CANCER-PPS 2025.01 validated 2025-08-27; CANCER-CR-GM 2022.01 validated 2022-12-06; CANCER-D2LM 2022.01 validated 2025-03-12; CANCER-CR-ACP obsolete; all CDA. No FHIR cancer volet | https://esante.gouv.fr/offres-services/ci-sis/espace-publication |
| Whole-edition and clinical-finding SNOMED translation counts on local Snowstorm | STILL OPEN: the query exceeds Elasticsearch's 500,000-term limit; splitting by hierarchy double-counts polyhierarchy concepts. Published total for the German edition: 130,795 translated concepts | local Snowstorm error "number of terms [675964] … exceeded the allowed maximum of [500000]" |
| MII Ontoserver $translate (German ICD-10-GM, OPS, ICD-O transition ConceptMaps) | STILL OPEN: server unreachable from this machine (mTLS, offline) | HTTP 503 from the Blaze fallback |
| Lithuanian terminology server tx.hl7.lt | STILL OPEN: DNS resolves (193.40.252.122), no TCP response within 20 s | curl |
| loinc.org linguistic variant pages, digital.nhs.uk COSD, legifrance circular DGS/SP5/2026/161 | NOT RETRIED: Cloudflare or bot checks, which are not bypassed | — |
