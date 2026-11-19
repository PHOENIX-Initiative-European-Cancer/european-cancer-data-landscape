# Germany reports: verification log (2026-11-19)

Scope: every "n/f", "snippet", "not verified" or secondary-only statement in `germany-landscape.md` and `germany-fhir.md`. Downloads in `scratchpad/dl-verify-de/` (curl + pdftotext/pandoc). Backups of the pre-edit reports in `scratchpad/verify-scripts/*.bak`.

| Status | Count |
|---|---|
| VERIFIED (n/f replaced with fact + URL) | 27 |
| CORRECTED (report text was wrong or outdated) | 4 |
| STILL NOT FOUND, re-searched | 15 |
| STILL NOT FOUND, not re-searched in this pass | 9 |

## Items

| # | File / section | Item | Status | Fact and source, or what was tried |
|---|---|---|---|---|
| 1 | landscape 1.2 | oBDS-RKI version | CORRECTED | Was "3.0.0.8_RKI" from a search snippet. Current is oBDS_v3.0.4_RKI, Zenodo 2026-05-26, https://zenodo.org/records/20397623 (supersedes 3.0.0.8a_RKI, https://zenodo.org/records/10022040). |
| 2 | landscape 1.1 | Hessen law text | CORRECTED | Abbreviation is KRG HE, not "HKRG". https://www.rv.hessenrecht.hessen.de/bshe/document/jlr-NNLHE000053D9 ; KRGV HE jlr-NNLHE000052C8 |
| 3 | fhir Part B §3 | SNOMED 2027 pin "not found" | CORRECTED | Aligned with Part A: 2027 ballot pins International 20260701 (release notes v2027.0.0-ballot). |
| 4 | fhir MV § 64e | Evaluation consortium | CORRECTED | Was "HCHE, Humangenetik Innsbruck". Also USZ Zürich Onkologie; awarded July 2025; kickoff 10.02.2026. GKV-SV MV page. |
| 5 | landscape 1.1 | Hamburg law text | VERIFIED | https://www.landesrecht-hamburg.de/bsha/document/jlr-KrebsRegGHAV6P1 ; Senate 03.03.2026 approved 6th amendment (Drs. 2026/00502) incl. § 8a FDZ linkage, transparenz.hamburg.de PDF. |
| 6 | landscape 1.1 | KrebsRG M-V | VERIFIED | https://www.landesrecht-mv.de/bsmv/document/jlr-KrebsRGMVV4P7 |
| 7 | landscape 1.1 | GKKN (Niedersachsen) | VERIFIED | voris link via https://kk-n.de/ueber-uns/rechtsgrundlagen/ |
| 8 | landscape 1.1 | SKRG (Saarland) | VERIFIED | https://recht.saarland.de/bssl/document/jlr-NNLSL00009DC3 |
| 9 | landscape 1.1 | KRG LSA | VERIFIED | Law of 05.12.2024, https://www.landesrecht.sachsen-anhalt.de/bsst/document/jlr-NNLST000041E3 |
| 10 | landscape 3.2 + 6 | FDZ Gesundheit head | VERIFIED | Dr. Steffen Heß, vdek-Magazin 06.10.2026 signed article; BMG KI-FDZ page. BfArM org chart URL 404. |
| 11 | landscape 4.2 | Total certified centres | VERIFIED | 2,245 centres / 2,324 sites on 31.12.2025; 492 hospitals, 443 in Germany. OZ-Jahresbericht 2026 §2.2, §2.4. |
| 12 | landscape 4.2 | Certification commission chairs | VERIFIED | Graeven, Fehm, Bokemeyer (OZ commission); OnkoZert Odenwald, Sommerfeldt. Same report. |
| 13 | landscape 4.5 | EUCAIM German partners | VERIFIED | 8 entries under Germany, Wayback copy 04.11.2026 of https://cancerimage.eu/partners/ |
| 14 | landscape 4.5 | ENCR German members | VERIFIED | Two "Germany" headings (pagination) with 11 registry entries, from the saved ENCR list. Added as a new bullet. |
| 15 | landscape 4.5 | OECI German centres | VERIFIED | None on https://accreditation.oeci.eu/ . Added as a new bullet. |
| 16 | landscape 4.6 | EHDEN country breakdown | VERIFIED | Germany 10 partners incl. DKG and Krebsregister RLP, https://www.ehden.eu/datapartners/ |
| 17 | landscape 4.7 + 6 | Onkopedia editors | VERIFIED | No editor named; Impressum lists DGHO board, https://www.onkopedia.com/de/impressum |
| 18 | landscape 6 | Lablans on DKTK CCP-IT page | VERIFIED | Wayback copy 23.01.2026 of the CCP-IT page. |
| 19 | landscape 6 | TMF Vorstand chair | VERIFIED | Prof. Dr. Rainer Röhrig, TMF Jahresbericht 2025. |
| 20 | landscape 3.5 | Mainzelliste versions | VERIFIED | v1.13.10 (Bitbucket tag 2026-06-15; Docker 2026-11-18); GUI v1.0.3. |
| 21 | landscape 3.5 | gPAS / E-PIX / gICS versions | VERIFIED | 2026.1.3 / 2026.1.3 / 2026.1.4 on Docker Hub mosaicgreifswald. |
| 22 | fhir FDPG | Onkologie module in FDPG ontology | VERIFIED | fhir-ontology-generator v4.1.0, 2026-05-15, PR #341. Production portal deployment not separately confirmed. |
| 23 | fhir ICD-O | bfarm ICD-O-3 canonical | VERIFIED | ZTS catalog: THO canonical maps to bfarm.terminologien.icdo3 2019.0.0; fhir.de canonical returns none. |
| 24 | fhir SNOMED | August edition release id | VERIFIED | 20260815, module 11000274103. RF2 metadata via local Snowstorm; not on BfArM pages. |
| 25 | fhir SNOMED | International dependency | VERIFIED | International 20260701 (same source). |
| 26 | fhir SNOMED | Namespace | VERIFIED | 1000274 (same source). |
| 27 | fhir SNOMED | Oncology refsets | VERIFIED | None in German Edition 20260815 (refset list from same source). |
| 28 | fhir HGNC | HGNC system URI | VERIFIED | Binding to GR hgnc-vs, system http://www.genenames.org (GR 3.0.0 JSON). |
| 29 | fhir ZTS | FHIR REST terminology endpoint | VERIFIED | Absent: /fhir/metadata 404; $lookup rejected 400. |
| 30 | fhir ZTS | ICD-11 on ZTS | VERIFIED | Absent from the 14-package catalog. |
| 31 | landscape 4.4 | MV § 64e Zwischenbericht | VERIFIED | Annual report is required; none published (GKV-SV page). Extension stays n/f (see 37). |
| 32 | landscape 1.1 | BW Krebsregistergesetz adoption | STILL NOT FOUND | Web searches for Landtag Drucksachen and the Gesetzblatt; Sozialministerium and krebsregister-bw.de pages. No adoption found; the Ministry still cites the LKrebsRG. |
| 33 | landscape 3.3 | First productive Krebsregister–FDZ linkage | STILL NOT FOUND | Kachel slides (Wayback) and GDNG searches. Only legal preparation found (Hamburg § 8a). |
| 34 | landscape 1.6 | IGES report text URL | STILL NOT FOUND | Searched for the report PDF; only the AOK and DKR statements exist. |
| 35 | landscape 2.1 | ZfKD 2024 data (secondary source) | STILL NOT FOUND | DataCite search shows records up to Stand 2025-11-11; no primary statement on 2024 data. |
| 36 | landscape 3.4 | Broad Consent counts | STILL NOT FOUND | MII AG Consent slides 09/2025 contain a chart without readable totals. |
| 37 | landscape 4.4 | genomDE extension beyond 5 years | STILL NOT FOUND | GKV-SV page and searches. |
| 38 | landscape 3.4 | "NUM-FDP" | STILL NOT FOUND | NUM site search returned 404. |
| 39 | landscape 5.4 | BDP synoptic-reporting paper | STILL NOT FOUND | Searches found only the BDP accreditation paper 05.03.2026. |
| 40 | landscape 5.5 | KIM ~1 bn messages (secondary) | STILL NOT FOUND | The gematik KIM page has no figure; the TI-Dashboard is JS-only (see NEEDS BROWSER). |
| 41 | landscape 5.6 | Mika / optimune / Pro-React Onco status | STILL NOT FOUND | DiGA FHIR API returns 401; directory is JS-only; Ärzte Zeitung pages block fetch. |
| 42 | landscape 4.1 + 6 | NCT single director | STILL NOT FOUND | Only site-level leadership exists in sources (e.g. Heidelberg, Dresden). |
| 43 | fhir terminology | oBDS→SNOMED national mapping (Landeskrebsregister + BfArM) | STILL NOT FOUND | Only the MII module's own ConceptMaps exist. |
| 44 | fhir ICD-O-4 | BfArM ICD-O-4 statement | STILL NOT FOUND | BfArM ICD-O-3 page has no ICD-O-4 mention. |
| 45 | fhir CTCAE | Official German CTCAE | STILL NOT FOUND | NCI and search; only German PRO-CTCAE exists. |
| 46 | fhir MedDRA | German MedDRA version | STILL NOT FOUND | meddra.org is JS-only; BioPortal MDRGER shows 28.0 (secondary). |
| 47 | landscape 1.4 | Registry core-software list | STILL NOT FOUND | Not re-searched in this pass. |
| 48 | landscape 3.1 | GBE cancer indicators | STILL NOT FOUND | Not re-searched in this pass. |
| 49 | landscape 4.3 | MII oncology use-case 2026 status | STILL NOT FOUND | Not re-searched beyond item 22. |
| 50 | landscape 5.1 | Market shares | STILL NOT FOUND | Not re-searched in this pass. |
| 51 | landscape 5.3 | HiGHmed oncology archetypes release | STILL NOT FOUND | Not re-searched in this pass. |
| 52 | landscape 6 | EHDS named national contact | STILL NOT FOUND | Not re-searched in this pass. |
| 53 | fhir UICC | UICC licence terms; TNM9 in SNOMED | STILL NOT FOUND | Not re-searched in this pass. |
| 54 | fhir DNPM | DNPM FHIR profiles | STILL NOT FOUND | Not re-searched in this pass. |
| 55 | fhir HL7 Europe | Other German work with HL7 Europe | STILL NOT FOUND | Not re-searched in this pass. |

## NEEDS BROWSER

- https://plattform65c.atlassian.net/wiki/x/BICdAg — the Confluence body is not retrievable by automated fetch. This is now superseded by Zenodo for the oBDS-RKI version.
- https://diga.bfarm.de/de/verzeichnis — JS-only. The API returns 401. Needed to check the status of Mika, optimune and Pro-React Onco.
- https://www.gematik.de/telematikinfrastruktur/ti-dashboard — JS-only. Needed for current KIM message counts.
- https://www.aerztezeitung.de/ articles on Mika (420611, 418315) — a bot check returns a 294-byte stub.
- https://cancerimage.eu/partners/ — the live page times out. A Wayback copy was used.
- https://dktk.dkfz.de/ CCP pages — the live pages return 404 to automated fetch. Wayback copies were used.
- https://www.meddra.org/ — JS-only.
- https://terminologien.bfarm.de/packages/bfarm.terminologien.icdo3/2019.0.0 — the download needs acceptance of the Downloadbedingungen to get a token. This was not done.
