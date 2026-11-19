# Verification log for south.md and south-landscape.md

Date: 2026-11-19. Method: WebSearch in local languages, curl of primary pages and PDFs (pdftotext) into a separate download directory, Wayback Machine copies, FHIR package registry mirrors. Italy entries limited to items in my own files. Outcome codes: VERIFIED, CORRECTED, STILL NOT FOUND.

## south.md (FHIR / terminology survey)

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 1 | FR | OSIRIS named maintainer | VERIFIED (partial) | GitHub contributors to the IG repo include INCaAJobard (INCa) and nriss; no maintainer page. https://api.github.com/repos/InstitutNationalduCancer/ImplementationGuide_OsirisFHIR/contributors |
| 2 | FR | CIP on the SMT | VERIFIED (partial) | SMT FHIR CodeSystem endpoint (count 200) returns BDPM, CIM11_MMS, SNOMED_CT plus TRE/JDV code systems; no separate CIP code system returned. https://smt.esante.gouv.fr/fhir/CodeSystem?_summary=true |
| 3 | FR | TNM 9th ed. national adoption; Francim registry transmission format; CIM-O-3 sub-edition | STILL NOT FOUND | Left to the France deep-dive agent; searches on cancer.fr and santepubliquefrance.fr found no adoption decision or format spec. |
| 4 | IT | ISTAT ICD-10 version | VERIFIED | ICD-10 version 2016 with Iris from 2016 data; version 2019 from 2020 data. https://www.ISTAT.it/it/files//2023/04/NOTAINFORMATIVABridgeCoding2020.pdf |
| 5 | IT | HL7 Italia chair | CORRECTED | Old: not found (older sources named Cangioli). New: President Stefano Lotti, Vice-President Giorgio Cangioli (past chair), CTO Leonardo Alcaro, elected 26 June 2024. https://www.hl7.it/direttivo |
| 6 | IT | Italian oncology FHIR IG | STILL NOT FOUND | hl7-it GitHub, packages.fhir.org jurisdiction IT, HL7 Italia site: no oncology IG. |
| 7 | IT | National terminology server | STILL NOT FOUND | Only HL7 Italia terminology IG; Ministry/AgID/Sogei searches gave nothing. |
| 8 | ES | Registry submission format / national registry law | CORRECTED (partial) | RD 568/2024 (BOE-A-2024-12379) creates the Red Estatal de Vigilancia en Salud Pública; cancer surveillance RD still at public-consultation stage. https://www.sanidad.gob.es/normativa/docs/CPP_RD_VIGILANCIA_CANCER.pdf ; format still not found. |
| 9 | ES | Código Nacional FHIR code system; TNM edition mandate; Arturo Romero current role | STILL NOT FOUND | Ministry semantic pages, SNS terminology server page, LinkedIn-free searches. |
| 10 | PT | Portuguese Core IG package id | VERIFIED | `portuguese.core.guide` 1.0.0, canonical base https://spms.min-saude.pt/fhir-r4B/iop. https://packages2.fhir.org/xig/portuguese.core.guide|1.0.0/StructureDefinition/AllergyIntolerancePTCore |
| 11 | PT | RON submission format | STILL NOT FOUND (access rule VERIFIED) | ron.min-saude.pt unreachable, no Wayback CDX snapshot; Lei 53/2017 art. 5 defines RIS platform with role profiles. https://diariodarepublica.pt/dr/detalhe/lei/53-2017-107692693 |
| 12 | PT | SNOMED CT Portuguese national edition | STILL NOT FOUND | snomed.org member page is JS; CTC wiki and SNO-PT records mention translation work only. NEEDS BROWSER (MLDS). |
| 13 | PT | LOINC national variant | VERIFIED (partial) | TEHDAS factsheet: lab catalogues use LOINC and SNOMED CT; no national LOINC release found. https://tehdas.eu/app/uploads/2023/03/portugal-country-visit-factsheet-03-2023.pdf |
| 14 | PT | TNM edition in RON | STILL NOT FOUND | RON reports and RORENO documents do not state the edition. |
| 15 | LU | National base IG package | VERIFIED (negative) | esantelux organisation has four preview guides and no packages. https://simplifier.net/organization/esantelux/~projects |
| 16 | LU | RNC legal basis, coding | CORRECTED | Legal basis: règlement grand-ducal du 18 avril 2013, Mémorial A-79 (29 Apr 2013); coding CIM-O-3; stage TNM 7th edition (2009) in 2020 report; ENCR-JRC tumour groupings. https://gouvernement.lu/dam-assets/documents/actualites/2021/02-fevrier/04-journee-cancer/MSA-5632-20-rapport-cancer-2020-web-BAT-4-.pdf |
| 17 | LU | SNOMED national edition; LOINC variant | STILL NOT FOUND | snomed.org member page JS; no MLDS listing reachable. NEEDS BROWSER. |
| 18 | LU | Agence eSanté FHIR lead | CORRECTED (partial) | CEO Alexandre Baumeister since 15 June 2026, board chair Marc Hostert; FHIR lead still not named. https://en.paperjam.lu/article/agence-esante-is-stepping-up-to-the-european-level |
| 19 | LU | Oncology FHIR IG / mCODE | STILL NOT FOUND | Simplifier esantelux, packages.fhir.org LU. |

## south-landscape.md (non-FHIR landscape)

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 20 | IT | ECIS contributing registries | VERIFIED | 41 Italian registries in archived ECIS list. https://web.archive.org/web/2025/https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data |
| 21 | IT | ENCR member list | STILL NOT FOUND | encr.eu contact list is JS-rendered; Wayback copy empty. NEEDS BROWSER. |
| 22 | IT | OECI centres | VERIFIED | 16 Italian centres on the OECI list read in a browser by the team lead on 2026-11-19 (saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://accreditation.oeci.eu/ |
| 23 | IT | EU project partners | VERIFIED | CraNE: ACC, MoH, IDI; EUCanScreen: ISS, CPO Turin; TEHDAS2: MoH, UniBo, Parma, ACC, ULSS4, RER, UCSC; ECHoS hub ACC. https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/ ; https://tehdas.eu/partners/ ; https://cancermissionhubs.eu/hubs/ |
| 24 | IT | 1+MG national programme; chemo prescribing; openEHR; patient portal oncology; hospital registries; synthetic data | STILL NOT FOUND | Left n/f; Italy deep-dive agent covers these. |
| 25 | ES | National registry legal basis | CORRECTED | RD 568/2024 framework; cancer surveillance RD pending; Catalonia-wide registry decree in prior consultation Mar 2025. https://www.sanidad.gob.es/fr/gabinete/notasPrensa.do?id=6458 ; https://www.catalannews.com/society-science/item/estimated-42851-malignant-tumors-diagnosed-in-catalonia-in-2024 |
| 26 | ES | ECIS registries | VERIFIED | 15 Spanish registries (archived ECIS list). |
| 27 | ES | EU project partners | VERIFIED (partial) | CraNE: ICO; canSERV: EurOPDX nodes in Spain; ECHoS hub exists. EUCanScreen/TEHDAS2 Spanish names not in fetched text. |
| 28 | ES | Structured pathology (SEAP) | VERIFIED (partial) | SEAP consensus protocols (colorectal) and Spanish ICCR datasets exist; adoption figures n/f. https://www.seap.es/documents/Publicaciones/Protocolos/guias-clinicas/consenso-recomendaciones/Carcinoma_colo_rectal.pdf |
| 29 | ES | Oncofarm/Farmis deployment; tumour-board software; openEHR; REDECAN submission format; researcher access; synthetic data | STILL NOT FOUND | SEFH and vendor searches returned no deployment data. |
| 30 | PT | SIIMA screening system | VERIFIED | SiiMA Rastreios is the SPMS screening system (2026 maintenance tender). https://ted.europa.eu/en/notice/238605-2026/pdf |
| 31 | PT | ECIS registries | VERIFIED | Azores, Central, North, South regional registries only, latest 2016; no RON national series. |
| 32 | PT | EU project partners | VERIFIED | CraNE: MS; EUCanScreen: MS, IPO Porto; ECHoS hub recognised. |
| 33 | PT | RON portaria / variable dictionary; Transparência SNS oncology datasets; tumour-board; openEHR; RSE oncology | STILL NOT FOUND | Diário da República search for RON portaria/despacho: none; ron.min-saude.pt down. |
| 34 | LU | RNC legal basis and coding | CORRECTED | See item 16. |
| 35 | LU | ECIS | CORRECTED | Luxembourg absent from the ECIS contributing-registries list (archived 2025). |
| 36 | LU | Latest RNC report | VERIFIED | Feb 2026 release covers 23,660 cancers 2014-2021. https://www.lesfrontaliers.lu/?p=1216650 |
| 37 | LU | EUCAIM partner | VERIFIED (negative) | No Luxembourg partner on https://cancerimage.eu/partners/ |
| 38 | LU | EU projects | VERIFIED | CraNE: INC, LIH; ECHoS hub; TEHDAS2 lists Luxembourg. |
| 39 | LU | DSP oncology content; OECI; terminology server status beyond "planned"; openEHR | STILL NOT FOUND | Agence eSanté cahiers statistiques have no document-type breakdown for oncology. |
| 40 | GR | Registry legal basis and data fields | VERIFIED | ΥΑ 6197/2024, ΦΕΚ Β' 950/09.02.2024: mandatory registration, fields (diagnosis/histology/grade, date, facility, stage, biomarkers), HDIKA processor, interoperability with AMKA, paediatric registry, EHR. https://www.dsanet.gr/Epikairothta/Nomothesia/950.PDF |
| 41 | GR | ECIS | VERIFIED (negative) | Greece absent from ECIS contributing list. |
| 42 | GR | OECI | CORRECTED | Agios Savvas completed OECI accreditation June 2025. https://en.protothema.gr/2025/06/13/saint-savas-was-certified-by-the-organization-of-european-oncology-institutes/ |
| 43 | GR | Researcher access | VERIFIED (partial) | Decree role "statistical information users"; INAB/CERTH National Cancer Data Node (CANDLE). https://www.inab.certh.gr/wp-content/uploads/2025/07/PRESS-RELEASE-CANDLE.pdf |
| 44 | GR | EU projects | VERIFIED | CraNE: 1st YPE Attica, Agios Savvas, Laiko; EUCanScreen: DYPEDE; TEHDAS2: MoH, GRNET, IDIKA. |
| 45 | GR | ENCR membership of national registry; ICD-O/TNM editions; open data portal; structured pathology; tumour board; openEHR | STILL NOT FOUND | Decree does not name coding systems; ENCR list NEEDS BROWSER. |
| 46 | MT | Legal basis | VERIFIED | Notification of Cancer Act, Cap. 154 (1957). https://legislation.mt/eli/cap/154/eng/pdf |
| 47 | MT | ECIS | CORRECTED | Malta contributes incidence 1993-2013 only (archived ECIS list). |
| 48 | MT | Cancer plan after 2021 | VERIFIED (negative) | No successor plan found; Digital Health and Health Data Strategy 2025-2030 listed. https://health.gov.mt/resources/ |
| 49 | MT | EU projects | VERIFIED | CraNE: MFH; EUCanScreen: MAH; ECHoS hub CRIHM. |
| 50 | MT | Registry format, ICD-O/TNM editions, data request route, latest cancer registry report | STILL NOT FOUND | dhir.gov.mt HTTP 403 to curl; deputyprimeminister.gov.mt gave a Cloudflare origin DNS error in a browser on 2026-11-19. Retry later. |
| 51 | CY | Registry coding | VERIFIED | ICD-O-3 with CanReg4 deriving ICD-10; MECC-supported set-up 1996-1998. https://pmc.ncbi.nlm.nih.gov/articles/PMC4523219 |
| 52 | CY | ECIS | VERIFIED | Cyprus Cancer Registry incidence 1998-2022. |
| 53 | CY | OECI | CORRECTED | No Cypriot or Maltese centre on https://accreditation.oeci.eu/ (browser, 2026-11-19); BOCOC holds CHKS/ISO 9001, not OECI. https://cyprus-mail.com/2026/01/21/double-international-recognition-for-bank-of-cyprus-oncology-centre |
| 54 | CY | EU projects | VERIFIED | CraNE: MOH; EUCanScreen: MOH, UCY; TEHDAS2: NeHA, Karaiskakeio, CYENS; ECHoS hub. |
| 55 | CY | Registry legal basis; 2024 strategy content; researcher access route; open data | STILL NOT FOUND | EU Country Cancer Profile PDF (cancer-inequalities.jrc) served HTML to curl; gov.cy strategy URL not retrievable. NEEDS BROWSER. |
| 56 | ALL | BBMRI Luxembourg | VERIFIED (negative) | Not among national nodes; members page blocked by cookie banner JS. https://www.bbmri-eric.eu/national-nodes/ |
| 57 | ALL | UNCAN.eu, JANE-2, EOSC4Cancer, EUnetCCC partner pages | STILL NOT FOUND | HTTP 000/404 to curl. NEEDS BROWSER. |

| 58 | ES/PT/GR/LU | OECI centres | VERIFIED | Spain 8 (12 Octubre, CUN, ICO, Clínic, IVO, FJD, IOCS Reus, Vall d'Hebron), Portugal 3 (IPO Coimbra, Lisboa, Porto), Greece 1 (Saint Savvas), Luxembourg 0. https://accreditation.oeci.eu/ (browser, 2026-11-19) |
| 59 | FR | SMT/ANS pages | NOTE | esante.gouv.fr was in maintenance on 2026-11-19; SMT FHIR endpoint answered. |

Totals: VERIFIED 32 (incl. partial and negative), CORRECTED 10, STILL NOT FOUND 16 (several items bundle multiple sub-items).

## NEEDS BROWSER
- https://encr.eu/encr-members-contact-list (all pages) – ENCR member registries for IT, ES, PT, GR, MT, CY, LU; JS-rendered.
- https://dhir.gov.mt/ and https://deputyprimeminister.gov.mt/ – Malta National Cancer Registry page, data request procedure, latest cancer report (HTTP 403 to curl; Cloudflare origin DNS error in browser on 2026-11-19; retry later).
- https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-cy-2024-1662-en.pdf – EU Country Cancer Profile Cyprus 2025, to extract the gov.cy May 2024 national cancer strategy URL and read that PDF.
- https://ron.min-saude.pt/ – Portugal RON platform documentation (site unreachable, no archive).
- https://mlds.ihtsdotools.org/#/landing/PT and /LU – whether Portugal or Luxembourg publish a SNOMED CT national edition/extension.
- https://www.snomed.org/member/portugal , /luxembourg , /spain – JS member pages (NRC, representatives).
- https://uncan.eu/partners/ , https://jane-2.eu/ , https://eosc4cancer.eu/partners/ , https://eunetccc.eu/ – partner lists per country (blocked/404).
- https://www.bbmri-eric.eu/about/members-observers/ – confirm Luxembourg and Spain membership status (cookie-banner JS).
- https://legilux.public.lu/eli/etat/leg/rgd/2013/04/18/n1/jo – full text of the 2013 RNC regulation (JS viewer).
- https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data – live version (curl gets "Request Rejected"; archived copy used).
