# Translation coverage per code system (2026-11-19). Rows and URLs: translation-coverage.csv. DE/AT/CH counts from a local Snowstorm
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
