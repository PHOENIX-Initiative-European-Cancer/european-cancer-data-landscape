# Verification log: nordic-baltic.md and nordic-baltic-landscape.md

Pass date: 2026-11-19. Method: local-language web searches; direct curl of registry PDFs into a dedicated download directory with pdftotext (Danish register declaration and LPR3 guide 2025 v5.1, Swedish "Kodning i cancerregistret 2026", Cancer in Norway 2023 and 2025, Estonian TAI notification guide and 2026 cancer-plan mid-term evaluation, Latvian SPKC cancer-card lecture and instruction, Lithuanian NVI 2025 activity report, EUnetCCC grant data sheet); direct fetch of ENCR registry pages, Genome of Europe partner page, Sundhedsdatastyrelsen reorganisation page, term.tehik.ee FHIR metadata. Outcomes: VERIFIED (fact confirmed with URL), CORRECTED (old statement replaced), STILL NOT FOUND (attempts listed).

Counts after browser follow-up on OECI: VERIFIED 20, CORRECTED 19, STILL NOT FOUND 23 (of which 8 need a browser).

## Priority 1: TNM editions in current registry use

| Country | Outcome | Detail |
|---|---|---|
| Denmark | VERIFIED (edition number not fixed) | Register declaration: extent coded "efter den gældende TNM-klassifikation"; LPR3 v5.1 §10.4.2.4.1 requires a qualified cTNM at first notification and refers to disease-specific clinical guidelines. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf |
| Sweden | CORRECTED | Old: "latest UICC edition". New: UICC TNM versions 8 and 9 currently in use ("för närvarande används version åtta och nio"), Kodning i cancerregistret 2026. https://www.socialstyrelsen.se/contentassets/6b4e25c21ce446f2a9d850ef43daa294/2026-5-10247.pdf |
| Norway | CORRECTED | Old: n/f. New: UICC 8th edition, Helsedirektoratet handlingsprogram states this matches Kreftregisteret routines; CiN 2025 derives stage from cTNM/pTNM. https://www.helsedirektoratet.no/retningslinjer/kreft-i-tykktarm-og-endetarm-handlingsprogram/patologi/uicc-tnm-klassifisering-og-stadieinndeling ; https://www.fhi.no/Content/cancer-in-norway-2025.pdf . Kreftregisteret kodebok itself not located. |
| Finland | STILL NOT FOUND | Tried Finnish searches ("TNM 8. painos", "levinneisyys", "laatuseloste"), cancerregistry.fi quality page (script-rendered, empty via curl). Found only that stage information is available for 42% of 2024 cases. https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ |
| Iceland | STILL NOT FOUND | Tried Icelandic searches ("TNM", "skráningarreglur", "gæðaskráning"); only ICD-O rules confirmed in Læknablaðið 2024. krabb.is variable list not located. |
| Estonia | CORRECTED | Old: n/f (study used 7th). New: TAI notification guide requires stage with TNM values per the 8th edition (pTNM, else cTNM). https://tai.ee/sites/default/files/2021-03/Teatise_vormistamise_juhend.pdf . Pathology templates being updated to TNM 9 (2026 mid-term evaluation). |
| Latvia | CORRECTED | Old: n/f. New: TNM 8th edition field in the cancer patient card; ICCC and TNM 8 added to data-entry algorithm by 1 Jan 2024. https://www.spkc.gov.lv/lv/media/19929/download ; https://spkc.gov.lv/lv/media/19977/download |
| Lithuania | STILL NOT FOUND | Tried Lithuanian searches ("TNM 8 leidimas", "forma 090/a pildymo taisyklės"), NVI 2025 report (no TNM statement). |

## Priority 2: ICD-O editions

| Country | Outcome | Detail |
|---|---|---|
| Denmark | VERIFIED | ICD-O-3 morphology, ICD-10 topography/diagnosis since 2004 (register declaration). |
| Sweden | VERIFIED | ICD-O/3.2 applied since 2019 (2026 handbook). |
| Norway | VERIFIED | Codes registered in ICD-O-3, converted to ICD-10 for reporting (CiN 2025). |
| Finland | VERIFIED (edition 3) | ICD-O-3 topography/morphology/behaviour variables in registry data description (FinnGen documentation); official registry coding manual not located. |
| Iceland | VERIFIED (edition not stated) | Registry follows ICD-O rules (Læknablaðið 2024). https://www.laeknabladid.is/media/2024-06/f02.pdf |
| Estonia | VERIFIED | RHK-O-3 (ICD-O-3) since 2008 (TAI page and notification guide). |
| Latvia | CORRECTED | Old: n/f. New: SSK-O-3.2 topography and morphology in cancer patient card (SPKC lecture Dec 2023). |
| Lithuania | VERIFIED (older source) | ICD-O-3 for topography/morphology per 2012 registry report; no newer manual. |

## Priority 3: Icelandic and Baltic genomics participation

| Item | Outcome | Detail |
|---|---|---|
| Genome of Europe partners (all 8) | CORRECTED | Partner page lists Denmark (Danish National Genome Center, 1,414 samples), Estonia (University of Tartu, 368), Finland (University of Helsinki 1,462; CSC), Latvia (BMC, 476), Lithuania (Santaros Klinikos, 816), Norway (University of Oslo, 1,346), Sweden (Uppsala University, 2,591). Iceland absent. https://genomeofeurope.eu/partners/ |
| 1+MG signatories | VERIFIED | 25 EU states plus UK and Norway signed; Denmark listed as observer in 2018-era sources; Iceland not a signatory. https://digital-strategy.ec.europa.eu/en/policies/1-million-genomes ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7115898 |
| Iceland GDI / 1+MG node | STILL NOT FOUND | Searched Icelandic and English; no Icelandic GDI or 1+MG participation found; treated as not participating. |
| Lithuania 1+MG | VERIFIED | Santaros Klinikos biobank responsible organisation, €7.6M GDI 2023–2026 (OECD.AI). |
| Finland Genome Center | CORRECTED | Old: status n/f. New: genome act removed from government programme; Genomikeskus not established. https://stm.fi/-/genomilain-antaminen-siirtyy-eteenpain-genomikeskuksen-valmistelu-jatkuu |
| Denmark genome governance | CORRECTED (added) | Nationalt Genom Center merged into Sundhedsdatastyrelsen 1 July 2025. https://www.altinget.dk/sundhed/artikel/styrelse-og-nationalt-genom-center-laegges-sammen-centerdirektoer-fortsaetter |

## Priority 4: Named registry leads

| Country | Outcome | Detail |
|---|---|---|
| Denmark | VERIFIED | Maya Christel Milter, Director, Danish Cancer Registry (ENCR). https://www.encr.eu/node/169 . ENCR lists the institute as "National Institute for Health Data and Disease Control", Artillerivej 5 (SSI address); this label could not be matched to any Danish agency name; see NEEDS BROWSER. |
| Sweden | STILL NOT FOUND | No national Cancerregistret head named; ENCR member list is script-rendered. |
| Norway | VERIFIED | Giske Ursin, Director Kreftregisteret (FHI 2026 release, CiN 2025). https://www.fhi.no/nyheter/2026/40364-nye-krefttilfeller-i-2025/ |
| Finland | VERIFIED | Janne Pitkäniemi, Director Finnish Cancer Registry (Syöpä 2024 report coverage). |
| Iceland | VERIFIED | Sigríður Gunnarsdóttir, head of Rannsóknasetur – Krabbameinsskrá (Krabbameinsfélagið annual report 2025). https://www.krabb.is/media/arsskyrsla-krabbameinsfelagsins-2025.pdf |
| Estonia | STILL NOT FOUND | TAI page gives phone only; report authors Mägi, Härmaorg, Innos. |
| Latvia | STILL NOT FOUND | SPKC Reģistru pārraudzības nodaļa named, no person. |
| Lithuania | VERIFIED | Giedrė Smailytė, Director Lithuanian Cancer Registry (ENCR). https://encr.eu/node/262 |

## Other items

| Item | Outcome | Detail |
|---|---|---|
| Danish registry coverage | VERIFIED | Above 95% (register declaration). |
| Danish screening registries | CORRECTED | DKMS, DKLS, DTS (RKKP) with annual-report URLs. |
| Kræftplan V | CORRECTED | Published 23 May 2025 (36 initiatives); implementation agreement 27 Nov 2025. https://medcom.dk/wp-content/uploads/2026/08/Bilag-2-Udmoentningsaftale-om-Kraeftplan-V-2026-og-frem.pdf |
| Digital Sundhed Danmark | CORRECTED (added) | SDS, MedCom, sundhed.dk, Nationalt Genom Center merge into Digital Sundhed Danmark 1 Jan 2027. https://english.sundhedsdatastyrelsen.dk/about-us/digital-health-denmark |
| Rigshospitalet / Odense OECI | CORRECTED (browser) | OECI list 2026-11-19: Aarhus University Hospital CCC, Copenhagen CCC Rigshospitalet and Herlev-Gentofte, Vejle Cancer Centre Lillebaelt Hospital; Odense not listed. https://accreditation.oeci.eu/ |
| EUnetCCC participants (all 8) | CORRECTED | Grant data sheet lists DK (Region H, AU, Region Syddanmark, Region Sjælland, AUH), SE (Socialstyrelsen, SKR, KI, Region Stockholm, VGR, Östergötland, Skåne, Uppsala), NO (OUS, UNN, FHI, St Olavs, Helse Bergen), FI (HUS), EE (SoM, Tartu UH, TAI, PERH), LV (University of Latvia, RSU, two hospitals), LT (Ministry, Kaunas, Šiauliai, Santaros, NVI, others), IS (Landspítali). https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf |
| EU-Designated CCCs (first 30, 23 Feb 2026) | CORRECTED | Norway: St. Olav, UNN. Lithuania: Klaipėda UH, Santaros with National Cancer Centre, LSMU Kaunas. No DK, SE, FI, EE, LV, IS centre in the first wave; the earlier search summary claiming Riga East was included was wrong (eight countries, Latvia not among them). https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ |
| Estonia OECI | CORRECTED (browser) | Tartu University Hospital is on the OECI accredited-centres list (level not shown); East Tallinn Central Hospital is a full OECI member. https://accreditation.oeci.eu/ ; https://www.itk.ee/en/news/east-tallinn-central-hospital-gains-full-oeci-membership |
| Iceland OECI / BBMRI / ECHoS | VERIFIED (absence) / STILL NOT FOUND | Not BBMRI member or observer (2025 report); no Icelandic centre on the OECI accredited list 2026-11-19 (browser); membership n/f; ECHoS n/f. |
| OECI accredited centres, all 8 countries | VERIFIED (browser) | DK: Aarhus, Copenhagen CCC (Rigshospitalet and Herlev-Gentofte), Vejle. SE: Karolinska, Linköping, Sahlgrenska, Skåne, Uppsala. NO: Haukeland Bergen, Oslo University Hospital. FI: Kuopio, Helsinki, TAYS Tampere, Turku. EE: Tartu. LV: Riga East. LT: 'National Cancer Institute' (country not shown, consistent with NVI Vilnius). IS: none. https://accreditation.oeci.eu/ |
| Estonia terminology server endpoint | VERIFIED | https://term.tehik.ee/fhir/metadata returns a FHIR CapabilityStatement (ontoserver mode); UI requires login. |
| Estonian pathology templates | CORRECTED (added) | ICCR/CAP-based standard templates updated to TNM 9 (2026 mid-term evaluation). |
| Latvia SSK-10 version | STILL NOT FOUND | Still the basis of Cabinet Regulation No. 6 of 13 Jan 2026; no version number. https://likumi.lv/ta/id/365793 |
| Lithuania TLK-10-AM edition | STILL NOT FOUND | Introduced by order V-164 (23 Feb 2011); in use 2026; ICD-10-AM edition not stated. https://e-seimas.lrs.lt/rs/legalact/TAD/TAIS.211963/ |
| Estonia RHK-10 version | STILL NOT FOUND | Published via TEHIK Publitseerimiskeskus; no version page found. |
| Finnish SNOMED edition date | STILL NOT FOUND | SNOMED page says "published in December" without year; module id 11000229106. |
| Danish SKS version, DK/SE/NO LOINC and ATC usage | STILL NOT FOUND | Low priority; not pursued further. |
| HL7 Denmark chair | STILL NOT FOUND | hl7.dk has no board page; conflicting secondary sources. |
| HL7 Sweden chair | STILL NOT FOUND | hl7.se blocks automated fetch (Loopia block page); archive copy empty. |
| Danish/Swedish/Norwegian/Finnish/Icelandic MDT, chemo module, openEHR oncology items | STILL NOT FOUND | Not pursued beyond earlier searches. |
| Synthetic datasets (all countries) | STILL NOT FOUND | No national synthetic cancer dataset found. |
| DARWIN EU Swedish partner | STILL NOT FOUND | EMA PDF returns HTML block page. |
| ECIS contributing registries (IS, EE, LV, LT) | STILL NOT FOUND | ECIS list page is script-rendered. |
| Finnish registry current submission format | STILL NOT FOUND | cancerregistry.fi pages script-rendered. |

## NEEDS BROWSER

Pages that block or script-render for automated fetch; please open in a real browser:

1. https://www.encr.eu/encr-members-contact-list and https://www.encr.eu/cancer-registries (registry directors for SE, FI, IS, EE, LV; ENCR membership of IS, EE, LV). Also confirm the institute label "National Institute for Health Data and Disease Control" on https://www.encr.eu/node/169 against the current Danish agency name.
2. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data (ECIS contribution of IS, EE, LV, LT).
3. https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf (DARWIN EU partners for SE, NO, EE).
4. https://hl7.se/ (board / ordförande page) and https://hl7.dk/ members area or https://confluence.hl7.org/display/HD (HL7 Denmark chair).
5. https://cancerregistry.fi/statistics/description-of-statistics-and-their-quality/ and https://syoparekisteri.fi/ilmoittaminen/ (Finnish TNM edition and current notification format).
6. https://www.fhi.no/kreft/ search for "kodebok" (Kreftregisteret codebook, TNM/ICD-O statement).
7. https://www.krabb.is/rannsoknasetur/ (Icelandic registry variable list / TNM).
8. https://term.tehik.ee/ (login-protected UI; FHIR endpoint already verified).
9. (resolved 2026-11-19 by team lead with a browser) https://accreditation.oeci.eu/ accredited-centres list; results applied above. Open point: the 'National Cancer Institute' entry shows no country; confirm it is NVI Vilnius, and check Tartu's accreditation level.
