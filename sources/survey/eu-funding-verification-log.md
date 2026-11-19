# EU funding report: verification log (2026-11-19)

**Counts:** 14 VERIFIED · 4 CORRECTED · 25 STILL NOT FOUND (43 items checked; two VERIFIED items also carry title corrections).

Method: Funding & Tenders SEDIA search API (filtered by programme: EU4Health 43332642, Digital Europe 43152860, IHI 43108390), topicDetails JSON per topic, CORDIS XML per project (standards grep for FHIR/OMOP/mCODE/OHDSI/HL7/openEHR/GA4GH), Zenodo deliverables, web search. Downloads: /private/tmp/claude-501/-Users-thome-code-fhir-profiling-cancer-common/3cc04596-744d-4990-addb-ce34993d093b/scratchpad/euv-dl/. Pre-edit backup of the report: /private/tmp/claude-501/-Users-thome-code-fhir-profiling-cancer-common/3cc04596-744d-4990-addb-ce34993d093b/scratchpad/euv-scripts/eu-funding.backup.md.

| # | item | status | finding | source / what was tried |
|---|---|---|---|---|
| 1 | EU4H-2027-SANTE-OG deadline (was n/f) | VERIFIED | Deadline 2027-01-19, opened 2026-11-04, EUR 1.8 M. Row moved to sorted position. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/EU4H-2027-SANTE-OG |
| 2 | HORIZON-RAISE-2027-01-04 type, budget, total | VERIFIED (+ title CORRECTED) | CSA lump sum, EUR 1.0 M, 1 project. Title is "Developing a model for a Data Lab for Science ... (RAISE pilot)". | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-RAISE-2027-01-04 |
| 3 | HORIZON-CL4-2027-04-DATA-03 type, budget, total | VERIFIED (+ title CORRECTED) | RIA, EUR 17.5 M per project, EUR 35 M, 2 projects. Title "New approaches for decentralized, federated and sustainable AI data processing". | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-CL4-2027-04-DATA-03 |
| 4 | IHI call 13 budget per project and total | VERIFIED | EUR 53.2 M; topics 35.0 / 9.0 / 9.2 M, 1 project each; opened 2026-07-02; stages 8 Oct 2026 and 21 Apr 2027. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-JU-IHI-2026-13-two-stage-01 |
| 5 | IHI call 13 stage 1 total (recently-closed table) | VERIFIED | EUR 53.2 M. | same |
| 6 | HORIZON-INFRA-2027-01-EOSC-01 per-project budget | VERIFIED | EUR 40 M, 1 grant. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-INFRA-2027-01-EOSC-01 |
| 7 | HORIZON-INFRA-2027-01-EOSC-01 action type | CORRECTED | "Cofund/CSA-type" to "COFUND". | same |
| 8 | HORIZON-INFRA-2027-SERV-01-02 dates and budget | VERIFIED | Opens 9 Mar 2027, closes 15 Jun 2027, EUR 6 M x 6 = 35 M. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-INFRA-2027-SERV-01-02 |
| 9 | HORIZON-HLTH-2026-03-DISEASE-13 dates and budget | VERIFIED | Opens 10 Feb 2027, closes 13 Apr 2027, EUR 63 M (30 + 33). | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-HLTH-2026-03-DISEASE-13 |
| 10 | HLTH-2027-03-TOOL-04 and TOOL-08 deadline | CORRECTED | Report said French NCP shows 22 Sep 2027 "on the portal". Portal shows 16 Sep 2027 for both. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-HLTH-2027-03-TOOL-04 ; https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-HLTH-2027-03-TOOL-08 |
| 11 | EU4H-2026-SANTE-PJ-08 total | VERIFIED | EUR 14,386,810; open 23 Sep 2025, closed 6 Jan 2026. | https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/EU4H-2026-SANTE-PJ-08 |
| 12 | ECHoS 2 EU share ("not separated") | CORRECTED | CORDIS gives EU contribution EUR 15,079,639.52. | https://cordis.europa.eu/project/id/101288304 |
| 13 | HealthData@EU Pilot FHIR/OMOP | VERIFIED | D8.1: some HDABs and teams converted the COVID-coagulopathy use case to OMOP CDM; others analysed native data. FHIR only in glossary. No mandatory CDM. | https://zenodo.org/records/15096755 |
| 14 | GDI FHIR/OMOP | VERIFIED (partial) | D8.7 surveys OMOP CDM, Phenopackets and HL7 FHIR (via ART-DECOR) without mandating one clinical CDM. EU share still n/f. | https://zenodo.org/records/11550316 |
| 15 | EuCanImage OMOP (n/f) | CORRECTED | OMOP was evaluated, not adopted. CORDIS lists the publication "Evaluation of OMOP CDM, i2b2 and ICGC ARGO for supporting data harmonization in a breast cancer use case". | https://cordis.europa.eu/project/id/952103 |
| 16 | OPTIMA OMOP | VERIFIED | CORDIS record names OMOP and OHDSI. FHIR/mCODE still n/f. | https://cordis.europa.eu/project/id/101034347 |
| 17 | TRANSCAN-4 cofund budget/period (context for JTC 2027) | VERIFIED | EU contribution EUR 5,836,584; 2026-04-01 to 2031-03-31. | https://cordis.europa.eu/project/id/101288225 |
| 18 | CORDIS dates/budgets of QUANTUM, CCI4EU, EUonQoL, PANCAIM, canSERV, CANDLE, 4.UNCAN.eu, B1MG, ECHoS | VERIFIED | All match the report within rounding. | CORDIS XML per id |
| 19 | EU4Health WP 2026 call ids and deadlines (DI-g-26-23, -24, -25, HS-g-26-16, CR/CV&NCD-g-26-13, -14) | STILL NOT FOUND | No EU4Health topic from WP 2026 on the portal. Newest EU4Health topic is EU4H-2027-SANTE-OG. Row annotated. | SEDIA filtered by EU4Health, sorted by opening date |
| 20 | DP-g-26-11 ERN per-grant budget | STILL NOT FOUND | Direct grants, not on portal. | SEDIA |
| 21 | Digital Europe 2027 topic ids (VHT/AI incubator, Apply AI testing, MCP support) | STILL NOT FOUND | Only DIGITAL-ECCC-2027 cyber topics published. Web search failed. | SEDIA filtered by Digital Europe; web search |
| 22 | IHI call 14 deadlines | STILL NOT FOUND | Draft topics only; launch "early 2027". | SEDIA (IHI); ihi.europa.eu future opportunities; web search |
| 23 | IHI call 15 deadlines | STILL NOT FOUND | Same. | same |
| 24 | TRANSCAN-4 JTC 2027 topic and dates | STILL NOT FOUND | No pre-announcement found. | web search; CORDIS |
| 25 | TRANSCAN-4 JTC 2026 total | STILL NOT FOUND | Only national shares (Polish NCBR EUR 1.2 M; INCa cap 300 k per partner). Note added. | https://www.gov.pl/attachment/1f0c6796-93ba-43c5-8300-173bdffa4de1 |
| 26 | EIT Health Innovation Validation 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 27 | ERA4Health IICS4all 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 28 | ERA4Health NanoDiagNCD 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 29 | THCS JTC 2027 total | STILL NOT FOUND | Not retried in depth. | — |
| 30 | COST Open Call 2027 dates | STILL NOT FOUND | Only 2026 announcement found. | web search; cost.eu |
| 31 | EP PerMed RIT call 2027 | STILL NOT FOUND | Only JTC2027 CGT4PM found. | web search |
| 32 | SCOPE-AI grant id, start, end, admin coordinator, standards | STILL NOT FOUND | No project record in SEDIA. Press release confirms only scientific coordination by IIS La Fe. | SEDIA free text; web search |
| 33 | DARWIN EU successor contract award, value, end | STILL NOT FOUND | TED returns empty pages to scripted access. Second notice 366419-2026 (28 May 2026) unread. | ted.europa.eu |
| 34 | HealthData@EU central platform tender award (TED 533039-2026) | STILL NOT FOUND | TED blocked. | ted.europa.eu |
| 35 | QUANTUM FHIR/OMOP | STILL NOT FOUND | CORDIS record and deliverable titles name no standard. Label builds on TEHDAS/EMA/EOSC frameworks. Row annotated. | CORDIS XML; web search |
| 36 | CCI4EU FHIR/OMOP | STILL NOT FOUND | No standard in CORDIS or project pages. | CORDIS XML; web search |
| 37 | EUonQoL FHIR/OMOP | STILL NOT FOUND | Web platform and app deliverables name no standard. | CORDIS XML; web search |
| 38 | PANCAIM FHIR/OMOP | STILL NOT FOUND | Collective Minds platform; no standard named. | CORDIS XML; web search |
| 39 | canSERV FHIR/OMOP | STILL NOT FOUND | Service catalogues only. | CORDIS XML; web search |
| 40 | CANDLE FHIR/OMOP | STILL NOT FOUND | Only "harmonisation and standardisation"; FHIR/OMOP is UNCAN-Connect. | CORDIS XML; web search |
| 41 | JANE-2 FHIR/OMOP | STILL NOT FOUND | Not on CORDIS; omics interoperability WP named, no standard. | web search |
| 42 | EUnetCCC FHIR/OMOP | STILL NOT FOUND | Not on CORDIS; only a participant post linking EUnetCCC to QUANTUM labels. | web search |
| 43 | JRC ECIS/ENCR budget line; Cancer Mission 2028+ allocation; FP10 health allocation | STILL NOT FOUND | No published amount. Only advocacy and the ECA report. | web search |

Items not retried individually (n/f in report, lower priority, unchanged): BreastSCan, 4.UNCAN.eu, B1MG, B1MGplus budget and coordinator, Xt-EHR budget, JANE, CraNE, ECHoS, PCM4EU, EU-CAYAS-NET standards, EHDEN Foundation figures, EP PerMed RITC2026 total, EIT Health 2026 total. Several are EU4Health or Digital Europe projects without CORDIS records.

## NEEDS BROWSER

- **DARWIN EU successor:** read TED notices 330958-2026 and 366419-2026 for value, duration and any award. https://ted.europa.eu/en/notice/366419-2026/html
- **HealthData@EU central platform tender:** check for an award notice following TED 533039-2026.
- **SCOPE-AI:** find the grant number and legal coordinator on the portal project search, or on cancerimage.eu and eucaim.cancerimage.eu.
- **EU4Health WP 2026 calls:** watch the HaDEA calls page for EU4H-2026/2027 project-grant topics (DI-g-26-23 etc.). https://hadea.ec.europa.eu/calls-proposals_en
- **Digital Europe 2027:** watch the portal for DIGITAL-2027 health topics, expected to open Q1 2027.
- **IHI calls 14 and 15:** https://www.ihi.europa.eu/apply-funding/future-opportunities
- **TRANSCAN-4 JTC 2027 and JTC 2026 total:** https://transcan.eu
- **Partnership call totals (ERA4Health, THCS, EIT Health):** read the call texts on the partnership sites.
