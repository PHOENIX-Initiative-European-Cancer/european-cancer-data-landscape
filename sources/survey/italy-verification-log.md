# Italy deep dive: verification log (2026-11-19)

Scope: every item in italy-fhir.md and italy-landscape.md that was marked n/f or rested on Noze, press or Wikipedia. Method: Italian and English web search, Gazzetta Ufficiale ELI pages and issue PDFs, Ministero/AgID/AIRTUM/HL7 Italia/LOINC Italia sites, GitHub, CORDIS, curl plus pdftotext into italy-dl/. Both report files were edited in place; edited passages carry "(verified 2026-11-19)".

## VERIFIED (primary source found, fact confirmed)
1. DM 31 Dec 2024 "Istituzione dell'Ecosistema dati sanitari": 25A01321, GU 53 of 5 Mar 2025; Ministero controller, Agenas processor; 21 regional clear-data units + SASN + pseudonymised + anonymous units (art. 4); FHIR cited in recitals; sub-investment 1.3.1 EUR 200 M. https://www.gazzettaufficiale.it/eli/id/2025/03/05/25A01321/sg (italy-dl/gu53.pdf)
2. DM 1 Aug 2023 "Registro nazionale tumori": 23A04839, GU 203 of 31 Aug 2023; ICD-9/ICD-10/ICD-O definitions, data sources, 180-day regional centre deadline, annual bulk feed, Allegato A tracciati A-D in XML. https://www.gazzettaufficiale.it/eli/gu/2023/08/31/203/sg/pdf (italy-dl/gu203.pdf)
3. DM 23 Oct 2025 ICD-10-IM and CIPI: 25A06571, GU 286 of 10 Dec 2025. https://www.gazzettaufficiale.it/eli/id/2025/12/10/25A06571/sg
4. DM 11 Nov 2025 amending DM 7 Sep 2023: 25A06570, GU 286 of 10 Dec 2025. https://www.gazzettaufficiale.it/eli/id/2025/12/10/25A06570/sg
5. EUCAIM Italian partners (10 of 95, 17 countries) from the official consortium page. https://cancerimage.eu/partners/
6. AIRTUM participating registries: 35 named registries and 44,459,587 inhabitants (about 80 %) in "I numeri del cancro 2025". https://www.legatumori.mi.it/wp-content/uploads/2025/12/2025_NDC_web.pdf (italy-dl/ndc2025.pdf)
7. AIRTUM registry tools: CheckRT, SALI, INCAS-AIRTUM, SEER*Prep/Stat (AIRTUM handbook). https://www.registri-tumori.it/PDF/AIRTUM2009HANDBOOK/Chapter_Appendix3.pdf
8. AIRTUM past presidents (Rugge 2019-2021 etc.). https://www.registri-tumori.it/cms/pagine/past-president
9. LOINC Italia governance: IIT-CNR official Regenstrief partner, MoU 2014, semiannual Italian update, legal basis DPCM 178/2015. https://www.loinc.it/chi-siamo/ , https://www.loinc.it/la-normativa/
10. ICD-11: no Italian MMS in the WHO browser (/mms/it 404, /mms/en 200, release 2026-01); Italian WHO-FIC CC hosted by Regione FVG. https://icd.who.int/browse/2026-01/mms/en , https://www.reteclassificazioni.it/
11. EHDS Cabina di regia composition and dates (DM 20 Feb 2026, DM 15 Apr 2026, installed 5 May 2026; includes ISTAT, DTD, AgID, Conferenza Regioni, EU EHDS Board delegate). https://www.osborneclarke.com/it/insights/digital-health-telemedicina-e-ia-le-novita-del-ii-trimestre-2026 (quotes the Ministry notice; the salute.gov.it page itself is client-rendered)
12. HL7 Italia Terminology IG declares no terminology server; FSE Gateway dictionary microservice exists (it-fse-srv-dictionary). https://github.com/hl7-it/terminology/blob/master/sushi-config.yaml , https://github.com/ministero-salute/it-fse-srv-dictionary
13. PNRR sub-investment 1.3.1 EUR 200 M (from DM 31 Dec 2024 recitals). Same GU source as item 1.

## CORRECTED (old vs new)
0. OECI Italian centres: old Wikipedia-derived list (9 CCC + 2 CCC-clinical + 8 other members) -> new live list of 16 certified Italian centres from https://accreditation.oeci.eu/ read with a browser by the team lead on 2026-11-19 (adds ASST Spedali Civili di Brescia, Policlinico San Matteo Pavia, INOC Candiolo, IRCCS Sacro Cuore Don Calabria, IRCCS San Raffaele; designation type per centre not shown). Snapshot: scratchpad/verify/oeci-centres-2026-11-19.txt
1. DM 7 Sep 2023 publication: old "GU 225 of 26 Sep 2023" (Noze) -> new "GU Serie Generale n. 249 of 24 Oct 2023, code 23A05829". https://www.gazzettaufficiale.it/eli/id/2023/10/24/23A05829/sg
2. DM 7 Sep 2023 content: old "decree explicitly references the Italian FHIR IGs; FHIR R4 with Italian IGs plus CDA R2" (Noze) -> new: the GU text names no FHIR/HL7/CDA; it refers to the standard formats of art. 12 c.15-octies and AgID guidelines; art. 3 c.1 lists 13 content types (a-m) detailed in Allegato A. The FHIR reference in primary law appears in the EDS decree recitals instead. italy-dl/gu249.pdf
3. EUCAIM Italian partners: old "press list" with "INT Milano not confirmed" -> new official list; INT Milano and Humanitas are not partners. https://cancerimage.eu/partners/
4. Massimo Rugge: old "named to lead Italian registries (Zaia statement)" -> new "AIRTUM president 2019-2021 (past president page)". https://www.registri-tumori.it/cms/pagine/past-president
5. AIRTUM coverage: old "35 registries, >44 M, about 80 %" (press) -> new same figures but from the primary report, with the full list of 35 registries. ndc2025.pdf
6. Ricerca Corrente total: old "annual total n/f" -> new EUR 187 M availability 2024 (192 M 2023, 231 M 2022), effective 179 M to 54 IRCCS, from the Ministry's 27 Feb 2025 presentation as reported by Quotidiano Sanità (still secondary; decree not retrievable). https://www.quotidianosanita.it/?p=141863
7. Registry software: old "n/f" -> new AIRTUM toolset (CheckRT, SALI, INCAS-AIRTUM) plus SEER tools; still no national management software.
8. EHDS Cabina di regia membership: old five members -> new full composition incl. ISTAT, DTD, AgID, Conferenza Regioni, EU Board delegate.

## STILL NOT FOUND (what was tried)
1. INT Milan "breast codes" (PHOENIX source): searched INT + breast + data dictionary/FHIR/OMOP/minimum data set, author names Trama/Gatta/Mariani, Italian terms "mammella dizionario dati"; nearest items are the ENCR 2024 Lasalvia slides (OMOP oncology MDS, PDF blocked) and the 2015 INT breast registry paper.
2. mCODE adoption in Italy: three search rounds (Italian/English, GSTeP, Gemelli, IRCCS, "profili oncologici"); only the IRST Meldola FHIR+RDF pipeline (not mCODE) surfaced.
3. Health Data Access Body designation: searched GU, salute.gov.it (client-rendered), Osborne Clarke Q2 2026, regioni.it, press; no act found.
4. Referto epidemiologico implementing decree (art. 4 L. 29/2019) and art. 6 annual report to Parliament: searched normattiva, GU, Senate/Chamber document portals, press; nothing after 2019.
5. Current LOINC Italian variant version number: loinc.it has no version; loinc.org 403; Wayback offline. Lower bound 2.75 (UMLS 2023).
6. Lombardia / Piemonte / Veneto / Lazio regional oncology EHR ("cartella oncologica"): Regione Lombardia ROL page and decrees 2022-2026, DGR 6609/2022 (general CCE), reteoncologica.it, Veneto/Lazio searches; only Campania ROC/Sinfonia is documented.
7. ICD-11 Italian translation: WHO browser has no Italian MMS; Ministry and FVG CC publish nothing on a translation.
8. National FHIR terminology server / AgID "Catalogo delle terminologie": DNS checks, HL7 Italia IG config, FSE repos; only the Gateway dictionary microservice and a 2017 CNR-ICAR prototype exist.
9. Ricerca Corrente riparto decree (primary): salute.gov.it pages client-rendered; CIPESS deliberations cover other IRCCS contributions.
10. FSE 2.0 implementation status (primary numbers): fascicolosanitario.gov.it dashboards are client-rendered Liferay data sets.

## NEEDS BROWSER (blocked for automated fetch)
- OECI accredited centres: RESOLVED by the team lead with a browser on 2026-11-19 (https://accreditation.oeci.eu/, 16 Italian centres); still open: designation type per Italian centre, which the home page does not show.
- LOINC Italian linguistic variant version: https://loinc.org/international/italian/ and https://loinc.org/downloads/ (403; Wayback snapshot 2026-02-11 exists at http://web.archive.org/web/20260211095451/https://loinc.org/international/italian/).
- INT Milano ENCR 2024 slides (OMOP oncology minimum data set): https://encr.eu/sites/default/files/Events/Workshops/Workshop-software-AI-2024/ENCR2024-Paolo%20Lasalvia.pdf (server returns HTML to curl).
- FSE 2.0 monitoring dashboard: https://www.fascicolosanitario.gov.it/it/monitoraggio (Liferay client-side data sets).
- Ministero della Salute research pages (Ricerca Corrente, fondi ordinari, Cabina di regia EHDS news): https://www.salute.gov.it/new/it/tema/sistema-ricerca-del-ssn-enti-e-finanziamenti/la-ricerca-corrente/ and https://www.salute.gov.it/new/it/tema/sistema-ricerca-del-ssn-enti-e-finanziamenti/investimenti-la-ricerca-con-fondi-ordinari/ (client-rendered, only a timestamp is returned).
- Gazzetta Ufficiale "atto originario" HTML views (e.g. https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2023-10-24&atto.codiceRedazionale=23A05829) return only the header to curl; the issue PDFs were used instead and are saved in italy-dl/ (gu249.pdf, gu203.pdf, gu53.pdf).
- ACC member list (names are images): https://alleanzacontroilcancro.it/soci/
- CORDIS EUCAIM page 101100633 (404 via curl; the consortium page was used instead).
