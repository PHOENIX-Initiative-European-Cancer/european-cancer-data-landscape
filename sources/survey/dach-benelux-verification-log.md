# Verification log: dach-benelux.md and dach-benelux-landscape.md

Pass of 2026-11-19 over every item previously marked n/f, not found, not verified, snippet or secondary. Methods: German/Dutch/French web searches, direct curl of organisation pages and PDFs (pdftotext) into a separate download directory, npm package downloads from fhir.ch and axelv.github.io, GitHub API, get-ig.org package metadata. Outcomes: VERIFIED (fact with URL), CORRECTED (old vs new), STILL NOT FOUND (what was tried). Germany and Netherlands: only items in my own files were checked.

Totals after browser follow-up: VERIFIED 36, CORRECTED 17, STILL NOT FOUND 10 (61 items; six OECI items and the BCR IG status resolved by the team lead's browser read on 2026-11-19).

## dach-benelux.md (FHIR survey)

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 1 | AT | Cancer registry FHIR profile set | STILL NOT FOUND | Three searches (EN/DE, "Krebsregister FHIR Österreich", Tumorregister Tirol FHIR); HL7 Austria registry lists no oncology IG. https://fhir.hl7.at/ |
| 2 | AT | Registry submission schema/file format | CORRECTED | Old: "not found". New: three channels, web form via eQuest, file upload via eQuest, SFTP file transfer; XML/CSV schema name still n/f. https://www.statistik.at/fileadmin/shared/QM/Standarddokumentationen/B_2/std_b_krebsstatistik.pdf (§2.1.7) |
| 3 | AT | ATC / national drug code | VERIFIED | ELGA e-Medikation uses PZN from the ASP-Liste and ATC codes; BASG register of authorised products. https://fhir.hl7.at/r4-ELGA-e-Medikation-main/StructureDefinition-at-elga-emed-medication-medikation-definitions.html |
| 4 | AT | TC FHIR authors (dev-build page) | STILL NOT FOUND | Published R5 2.0.0 IG has no authors page (toc checked); dev-tergi and fhir.hl7.at template-branch pages return 404 or redirect. Names kept with caveat. NEEDS BROWSER. |
| 5 | CH | CH CRL mCODE reuse | VERIFIED | ch.fhir.ig.ch-crl 0.9.0 npm package: zero occurrences of "mcode"; deps hl7.fhir.r4.core 4.0.1, ch-core 2.0.0; author/maintainer BAG. https://fhir.ch/ig/ch-crl/package.tgz |
| 6 | CH | ICD-10-GM current year in CH | CORRECTED | Old: not found. New (BFS page read in browser by team lead): coding year 2026 = ICD-10-GM 2024 (Swiss supplement 2024-10-31); coding year 2027 = ICD-10-GM 2026 (supplement 2026-10-27); one-year lag from ICD-10-GM 2026 for FR/IT translation. https://statistik.admin.ch/de/daten-statistiken-verstehen/nomenklaturen/medkk/instrumente-medizinischen-kodierung |
| 7 | CH | ICD-O-3 edition / TNM edition at NKRS | CORRECTED | Old: "not found". New: NKRS Data Dictionary Basic Variables v1.5 (01.01.2026) records ICD-O version (var. 3.2) and UICC TNM edition (var. 4.1) per case. https://www.nkrs.ch/upload/downloads/Forschende/Datenstruktur/Datenstrukturv15/Basisdatenv15/A_DataDictionary_BasicVariables_v1.5_01.01.2026.pdf |
| 8 | CH | LOINC use | VERIFIED | CH LAB-Order 3.0.0 (2025-12-16) and CH LAB-Report (1.0.0 trial-use; 3.0.0 ballot) bind LOINC. https://fhir.ch/ig/ch-lab-order/index.html ; https://fhir.ch/ig/ch-lab-report/usecases-en.html |
| 9 | CH | CH CRL named editors | STILL NOT FOUND | package.json author/maintainers: BAG only; GitHub repo hl7ch/ch-crl returns 404. |
| 10 | NL | PALGA FHIR specification | CORRECTED | Old: "not found". New: IKNL package iknl.fhir.nl.r4.palga 1.0.1 (FHIR R4), profiles for PALGA incidence notifications and protocol data to the NKR. https://get-ig.org/iknl.fhir.nl.r4.palga |
| 11 | NL | National drug code | VERIFIED | G-Standaard (Z-Index). https://www.z-index.nl/g-standaard |
| 12 | NL | nl-core maintainers | CORRECTED | Old: "not found". New: GitHub Nictiz/Nictiz-R4-zib2020 top contributors pieter-edelman-nictiz, jd-nictiz, ArdonToonstra. https://github.com/Nictiz/Nictiz-R4-zib2020 |
| 13 | BE | BCR IG mCODE reuse | VERIFIED | be.fhir.bcr 0.1.0 npm package: zero "mcode" occurrences; deps r4 core 4.0.1, hl7.terminology.r4 7.1.0, extensions 5.2.0. https://axelv.github.io/bcr/package.tgz |
| 14 | BE | TNM edition at BCR | STILL NOT FOUND | kankerregister.org menu "registration" page returns 404 via curl; Dutch searches for registratiehandleiding found nothing. NEEDS BROWSER. |
| 15 | BE | WBCR batch file specification | STILL NOT FOUND | Same as 14. NEEDS BROWSER. |
| 16 | BE | SNOMED join year | CORRECTED | Old: "not found". New: Belgium joined IHTSDO in 2013 (CliniSys slide, secondary) and is listed as member by Dec 2016 (Wikipedia). https://wiki.ihe.net/uploads/2/23/LAB_Tokyo_Semantic_Migom.pdf ; https://en.wikipedia.org/wiki/International_Health_Terminology_Standards_Development_Organisation |
| 17 | BE | LOINC national variant | VERIFIED | HL7 Belgium lab IG: LOINC per the FPS Health subset. https://build.fhir.org/ig/hl7-be/lab/qa-ipreview.html |
| 18 | BE | ATC / drug code | VERIFIED | SAM, CNK codes (NamingSystem be-ns-cnk-codes), FPS ATC-to-CNK mapping. https://www.ehealth.fgov.be/standards/fhir/medication/en/NamingSystem-be-ns-cnk-codes.html ; https://www.ehealth.fgov.be/standards/kmehr/en/tables/atc-codes |

## dach-benelux-landscape.md

| # | Country | Item | Outcome | Detail / URL |
|---|---|---|---|---|
| 19 | DE | Per-state completeness | VERIFIED | Krebs in Deutschland 2023, ch. 2.1: diagnosis year 2020, 13 of 16 registries >95%, one 90–95%, two 80–90%. https://edoc.rki.de/bitstream/176904/11438/1/krebs_in_deutschland_2023-1.pdf |
| 20 | DE | ECIS contribution | VERIFIED | ECIS list (Sept 2024): Brandenburg, Bremen, Hamburg, Mecklenburg-Vorpommern, Munich, NRW, Saarland, Saxony (23%). https://ecis.jrc.ec.europa.eu/sites/default/files/2024-09/List_of_cancer_registries.pdf |
| 21 | DE | Synthetic datasets | STILL NOT FOUND | DE/EN searches ("synthetische Krebsregisterdaten", ZfKD Testdatensatz). |
| 22 | DE | OECI accredited centres | VERIFIED (absent) | No German centre on the OECI certified-centres list (browser read by team lead, 2026-11-19). https://accreditation.oeci.eu/ |
| 23 | DE | EHDEN oncology partners | VERIFIED | 10 German partners incl. Charité, DKG, GermanOncology, Krebsregister RLP, UM Dresden, MHH, InGef, Ulm. https://ehden.eu/datapartners/ |
| 24 | DE | MIO oncology | STILL NOT FOUND | KBV MIO page and mio42 checked; no oncology MIO. https://www.kbv.de/praxis/digitalisierung/anwendungen/elektronische-patientenakte/mio |
| 25 | DE | ICCR structured pathology | CORRECTED | Old: n/f. New: German ICCR dataset pilot (TUR-B) with SNOMED CT, reports mostly free text. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11861236/ |
| 26 | DE | openEHR oncology | CORRECTED | Old: n/f. New: HiGHmed CKM 8 oncology templates / 35 archetypes for oBDS, MTB recommendation archetype, ICD-O cluster. https://ebooks.iospress.nl/pdf/doi/10.3233/SHTI240655 ; https://discourse.openehr.org/t/modeling-of-multidisciplinary-tumor-board-meetings/6092 |
| 27 | DE | JANE-2 / EUCanScreen / TEHDAS2 partners | VERIFIED | JANE-2: BMG, Charité, DKFZ, DKG, BZgA, MSB; EUCanScreen: RKI, DKFZ, DKG; TEHDAS2: BMG, BfArM. https://sigarra.up.pt/fmup/en/PROJECTOS_GERAL.MOSTRA_PROJECTO?p_id=83039 ; https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://tehdas.eu/partners/ |
| 28 | DE | Modellvorhaben 25,000 records (secondary) | STILL NOT FOUND | No BfArM/GKV-SV/BMG figure; GKV-SV lists participating providers only. https://www.gkv-spitzenverband.de/krankenversicherung/forschung_modellvorhaben/mv_genomsequenzierung/genomsequenzierung.jsp |
| 29 | AT | Breast screening register | CORRECTED | Old: n/f. New: uniform documentation system, pseudonymised via Dachverband, coordination at ÖGK, GÖG evaluation, bPK linkage under § 15c GÖGG. https://www.parlament.gv.at/dokument/XXVIII/AB/1880/imfname_1701525.pdf ; https://www.jusline.at/gesetz/goegg/paragraf/15c.pdf |
| 30 | AT | AMDC and cancer registry | CORRECTED (partial) | AMDC remote access and catalogue confirmed; Vorarlberg registry operator accredited; cancer registry dataset in catalogue still n/f. https://www.statistik.at/en/services/tools/data-access/center-for-science/austrian-micro-data-center-amdc |
| 31 | AT | ECIS / ENCR | VERIFIED | Austria National registry in ECIS list (100%); Statistik Austria states ENCR and IACR membership. URLs as in #20 and #2 |
| 32 | AT | EUCAIM / TEHDAS2 / JANE-2 | VERIFIED (JANE-2 n/f) | EUCAIM: Medical University of Vienna; TEHDAS2: GÖG. https://cancerimage.eu/partners/ ; https://tehdas.eu/partners/ |
| 33 | AT | Oncology CDA guide | STILL NOT FOUND | ELGA guides list (Labor, Befund bildgebende Diagnostik, Entlassungsbrief, e-Medikation); pathology guide announced 2013, status unknown. |
| 34 | AT | Tumour-board software, structured pathology, openEHR | STILL NOT FOUND | DE searches. |
| 35 | CH | ECIS contribution | VERIFIED | Basel, Geneva, Grisons, St. Gallen, Ticino, Valais (30%). URL as #20 |
| 36 | CH | OECI | VERIFIED | CCC Zürich is an OECI member and DKG-certified; no Swiss centre on the OECI certified-centres list. https://www.usz.ch/en/?p=99220 ; https://accreditation.oeci.eu/ |
| 37 | CH | SPHN funding (Wikipedia mirror) | VERIFIED | SBFI: max CHF 20.7 M for the DCC 2025–2028. https://www.sbfi.admin.ch/de/datenkoordinationszentrum-des-swiss-personalized-health-network |
| 38 | CH | EU projects | VERIFIED (partial) | No Swiss partner on EUCAIM or TEHDAS2 partner pages; EUnetCCC/JANE-2 Swiss role n/f (eunetccc.eu fetch returns 135 bytes). NEEDS BROWSER. |
| 39 | CH | EPD oncology content | STILL NOT FOUND | — |
| 40 | CH | Registry software failure (heise) | CORRECTED to primary | BAG press release 24 Jan 2025; BAG review 10 June 2025; GDK successor project. https://www.bag.admin.ch/dam/fr/sd-web/si4u6qVqFCNn/Projektanalyse_Aufarbeitung_Projekt_IT-Architektur_KRG_RSW.pdf |
| 41 | CH | Tumour-board software etc. | STILL NOT FOUND | — |
| 42 | NL | ENCR membership | VERIFIED | "The Netherlands National" in ECIS list of ENCR-affiliated registries (100%). URL as #20 |
| 43 | NL | ScreenIT | VERIFIED | RIVM: ScreenIT for breast/cervical/colorectal, owned by Bevolkingsonderzoek Nederland, code on GitHub. https://www.rivm.nl/bevolkingsonderzoeken-en-screeningen/bevolkingsonderzoek-organisatie/broncode-vrijgegeven |
| 44 | NL | OECI centres | CORRECTED | Old: NKI, Maastricht, Erasmus MC, Radboudumc, UMCG (secondary). New: list shows Erasmus MC, Maastricht UMC+, NKI, OncoZON, Rijnstate, UMCG; Radboudumc not listed. https://accreditation.oeci.eu/ |
| 45 | NL | Hartwig access; 1+MG | VERIFIED | Hartwig DR guide; Health-RI coordinates GDI, Erasmus MC co-leads Genome of Europe. https://hartwigmedical.github.io/documentation/data-access-request-guide.html ; https://health-ri.atlassian.net/wiki/spaces/HNG/pages/608312395 |
| 46 | NL | BBMRI-NL | VERIFIED | https://www.bbmri-eric.eu/?p=6325 |
| 47 | NL | EUCAIM partners | VERIFIED | Erasmus MC, Maastricht University, Radboudumc, NKI. https://cancerimage.eu/partners/ |
| 48 | NL | Oncoguide | VERIFIED | https://iknl.nl/getmedia/351d2826-cc3a-49a4-81a1-827c7ed5f3e1/faq-oncoguide_oktober2018_iknl.pdf |
| 49 | BE | CvKO screening register | CORRECTED | eHealth ISC decisions: CvKO–BCR invitation file exchange; BCR runs cytohistopathology and Flemish cervical screening registers. URLs in file |
| 50 | BE | ECIS | VERIFIED | Flanders (58%). URL as #20 |
| 51 | BE | Cancer plan 2025 | CORRECTED | Belgian Cancer Plan 2025–2030 (Sciensano, draft Q4 2025); 34-measure plan presented 2026. https://www.sciensano.be/sites/default/files/16062025_kankerplan_2025-2030_1.pdf |
| 52 | BE | OECI centres | VERIFIED | List shows Institut Jules Bordet (renewed 22 June 2026), Leuven Cancer Institute, AZ Groeninge Kortrijk. https://accreditation.oeci.eu/ ; https://www.bordet.be/en/news/mon-06222026-1100/jules-bordet-institute-accredited-comprehensive-cancer-centre-oeci |
| 53 | BE | KMEHR oncology | STILL NOT FOUND | — |
| 54 | BE | EUCAIM / EUCanScreen partners | VERIFIED | KU Leuven, Sciensano (EUCAIM); Sciensano, CvKO, Stichting Kankerregister, UZA, Bordet (EUCanScreen). |
| 55 | LU | ENCR | VERIFIED | ENCR contact list; Backes on steering committee. https://encr.eu/encr-members-contact-list?page=9 |
| 56 | LU | Legal basis | VERIFIED | RGD 18 April 2013 (Mémorial A 79). https://conseil-etat.public.lu/content/dam/conseil_etat/fr/avis/2013/03/50_029/50029_Texte.pdf |
| 57 | LU | Submission format | VERIFIED (partial) | Annex-1 variables via annexed declaration form; electronic format n/f. |
| 58 | LU | ECIS | VERIFIED (absent) | Not in ECIS list. |
| 59 | LU | 1+MG | VERIFIED | LNDS co-leads GoE ELSI WP; LIH contributes cohorts. https://lnds.lu/?p=3918 |
| 60 | LU | EUCanScreen / TEHDAS2 | VERIFIED | Not in EUCanScreen list; LNDS in TEHDAS2. |
| 62 | AT/LU | OECI centres | VERIFIED (absent) | No Austrian or Luxembourg centre on the OECI certified-centres list. https://accreditation.oeci.eu/ |
| 63 | BE | Status of be.fhir.bcr IG | CORRECTED | Old: presented as eHealth Platform-published draft. New: individual developer's local development build (Axel Vanraes, Tiro.health); canonical returns 404, not on Simplifier/packages.fhir.org, not in hl7-be GitHub (browser check by team lead). https://axelv.github.io/bcr/ |
| 61 | LU | DSP oncology | CORRECTED (partial) | IdeoRCP tumour-board app hosted on eSanté (2015). https://paperjam.lu/article/communique-signature-de-conventions-de-partenariat |

## NEEDS BROWSER

- RESOLVED 2026-11-19: oeci.eu certified-centres list read by team lead; see items 22, 36, 44, 52, 62.
- kankerregister.org: registration pages (WBCR, batch extraction specification, coding manual with TNM/ICD-O edition); EN menu link "registration" returns 404 via curl.
- dev-tergi.elga.gv.at/r5-core-main/authors.html and fhir.hl7.at template branch authors page: confirm HL7 Austria TC FHIR authors (Anna Lin, Reinhard Egelkraut, Oliver Krauss).
- RESOLVED 2026-11-19: BFS ICD-10-GM validity read by team lead; see item 6.
- eunetccc.eu partners page (returns 135 bytes to curl): Swiss, Austrian, Luxembourg partners.
- eosc4cancer.eu partners/consortium (returns empty to curl): German, Dutch, Belgian partners.
- legilux.public.lu (JavaScript only): full text of RGD 18 April 2013 incl. annex 1 variable list and declaration form.
- statistik.at AMDC Mikrodatenkatalog: whether the Krebsstatistik dataset is listed.
- hl7belgium.org: invalid TLS certificate (team lead, 2026-11-19); use HL7 Belgium GitHub (hl7-be) and Simplifier instead.
- gkv-spitzenverband.de Modellvorhaben page / BfArM: any official count of transmitted genome datasets.
