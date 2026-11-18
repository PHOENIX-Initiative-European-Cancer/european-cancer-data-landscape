# Non-FHIR digital cancer landscape: Germany, Austria, Switzerland, Netherlands, Belgium, Luxembourg

Companion to `dach-benelux.md` (FHIR, oncology IGs, terminologies). Facts only, each with a source URL; "n/f" = not found in a primary source during this survey (2026-11-18). Where a fact comes from a secondary source (news, conference slide, Wikipedia mirror) this is stated.

---

## Germany

### (a) Cancer registries
- Population-based and clinical registration is combined in the 16 Landeskrebsregister (state cancer registries, clinical registries under § 65c SGB V); all state registries are members of Deutsche Krebsregister e.V. (DKR), founded May 2024 as successor of GEKID. https://www.hamburg.de/politik-und-verwaltung/behoerden/bwfg/einrichtungen/hamburgisches-krebsregister/bundesweite-krebsregisterdaten-zeigen-erste-positive-effekte-des-neuen-gebaermutterhalskrebs-screenings-1217540 ; https://basisdatensatz.de/
- ENCR membership: state registries listed in the ENCR member contact list include North Rhine-Westphalia, Rhineland-Palatinate, Saxony, Thuringia, Mecklenburg-Vorpommern, Baden-Württemberg, Brandenburg-Berlin and the German Childhood Cancer Registry (DKKR). https://encr.eu/encr-members-contact-list?page=3
- Coverage: nationwide registration by law; ZfKD estimates completeness per state using IARC-type methods; per-state completeness figures: n/f. https://edoc.rki.de/handle/176904/1145
- Childhood cancer: Deutsches Kinderkrebsregister (DKKR), Mainz; reporting via oBDS with a DKKR module (oBDS 3.1.0 splits it into two parts). https://kinderkrebsregister.de/fileadmin/kliniken/dkkr/files/2026-11-05_Meldehandbuch_DKKR_V1.1.pdf ; https://basisdatensatz.de/xml-schnittstelle
- Screening registries: no separate screening registry; organised programmes (colorectal, cervical) under the G-BA oKFE-Richtlinie send quarterly documentation to the Kassenärztliche Vereinigungen as Datenannahmestelle, with linkage to cancer registry data (G-BA decision 12 May 2023); mammography screening data are collected by the Referenzzentren and evaluated by the Kooperationsgemeinschaft Mammographie (KBV + GKV-Spitzenverband). https://www.g-ba.de/downloads/39-261-6012/2023-05-12_oKFE-RL_Anbindung-Krebsregisterdaten.pdf ; https://www.kvbawue.de/praxis/qualitaetssicherung/krebsfrueherkennungsprogramme ; https://www.g-ba.de/downloads/17-98-5975/KOOPMAMMO_Jahresbericht_Eval_2023_web.pdf
- Legal basis: Bundeskrebsregisterdatengesetz (BKRG) for the federal pooling at ZfKD; § 65c SGB V for clinical registries; state cancer registry laws (e.g. Krebsregistergesetz NRW 2023). https://www.bundesgesundheitsministerium.de/service/begriffe-von-a-z/b/bundeskrebsregisterdatengesetz ; https://recht.nrw.de/lrgv/gesetz/18112023-gesetz-ueber-die-klinische-und-epidemiologische-krebsregistrierung-im-land/
- Submission format and dictionary: einheitlicher onkologischer Basisdatensatz (oBDS) XML interface; schema V3.0.5 (24.10.2025, adds TNM 9th ed.), V3.1.0 (14.10.2026), next version adds ICD-O-4 2026 and CTCAE 6.0; ICD-O-3 2nd revision (2019) in force since 2020; published in Bundesanzeiger 12.07.2021; maintained by ADT, DKR and Plattform § 65c (AG Daten). https://basisdatensatz.de/xml-schnittstelle ; https://www.bfarm.de/DE/Kodiersysteme/Klassifikationen/ICD/ICD-O-3/_node.html
- National data centre: Zentrum für Krebsregisterdaten (ZfKD) at Robert Koch-Institut; annual pooling of clinical data from all state registries (Stufe 1); PLATO 2 concept for Stufe 2 (platform for linked oncology data) delivered May 2025; a uniform nationwide application form for registry data (v2.0.0, 01.04.2025) is used by all state registries, and § 10 BKRG creates a central application office at ZfKD for multi-state requests. https://www.bundesgesundheitsministerium.de/service/publikationen/details/plato-2 ; https://nlga.niedersachsen.de/download/217246 ; https://www.hamburg.de/politik-und-verwaltung/behoerden/bwfg/einrichtungen/hamburgisches-krebsregister/publikationen-datennutzung-196584

### (b) Public datasets
- Open statistics: ZfKD interactive database and reports at krebsdaten.de (Krebs in Deutschland). https://krebsdaten.de/
- Research data access body: Forschungsdatenzentrum Gesundheit (FDZ Gesundheit) at BfArM, opened 9 Oct 2025; GKV claims data 2009–2023 for all insured; GDNG allows linkage of FDZ data with state clinical cancer registry data; ePA data to be added from end 2026; public register of approved projects. https://www.bundesgesundheitsministerium.de/presse/pressemitteilungen/forschungsdatenzentrum-gesundheit-eroeffnet
- Screening programme data: anonymised aggregated data of the oKFE colorectal and cervical programmes available to researchers since April 2025 (G-BA). https://www.g-ba.de/service/fachnews/186/
- ECIS contribution: n/f (ZfKD contribution to ECIS not verified in this survey).
- Synthetic datasets: n/f.
- Data catalogues: NUM/MII Forschungsdatenportal für Gesundheit (feasibility and data use requests across university hospitals). https://forschen-fuer-gesundheit.de/

### (c) Cancer infrastructure
- National plan: Nationale Dekade gegen Krebs (launched 2019 by BMBF with partners). https://www.bmftr.bund.de/SharedDocs/Pressemitteilungen/DE/2023/11/221123-NCT.html
- Comprehensive Cancer Centres: 14 Onkologische Spitzenzentren funded by Deutsche Krebshilfe (incl. 10 CCC consortia at 29 university sites, per TU Dresden 2026; other sources give 14 CCCs at 26 sites). https://tu-dresden.de/tu-dresden/newsportal/news/deutsche-krebshilfe-bestaetigt-onkologisches-spitzenzentrum-in-dresden ; https://www.aerzteblatt.de/nachrichten/136117/Krebshilfe-foerdert-weitere-Exzellenzzentren
- NCT (Nationales Centrum für Tumorerkrankungen): expanded from Heidelberg and Dresden to six sites (incl. Tübingen/Stuttgart-Ulm, Berlin, Essen/Köln) with up to EUR 98 M per year federal funding. https://www.bmftr.bund.de/SharedDocs/Pressemitteilungen/DE/2023/11/221123-NCT.html
- DKTK (Deutsches Konsortium für Translationale Krebsforschung) sites: see DKFZ site list. https://dkfz.de/en/dkfz/standorte.html
- OECI accredited German centres: n/f.
- Genomics: genomDE pilot funded to end 2025; Modellvorhaben Genomsequenzierung under § 64e SGB V (cancer and rare diseases, started 2024/2025, five years, insurer-funded); Germany contributes to 1+MG via genomDE. https://ghga.de/Downloads/Factsheet_Modellvorhaben.pdf ; https://idw-online.de/de/pdfnews849993
- Biobanks: BBMRI.de / German Biobank Node (GBN). https://www.bbmri.de/
- Imaging: Germany is among the 12 countries in EUCAIM (Cancer Image Europe); DKFZ is a partner; TMF and Siemens Healthineers were EuCanImage partners. https://digital-strategy.ec.europa.eu/en/policies/cancer-imaging ; https://dkfz.de/en/federated-information-systems ; https://www.bbmri-eric.eu/news-events/eucanimage-will-launch-in-october-2020-with-bbmri-eric-on-board/
- EU projects: EUnetCCC (Joint Action Oct 2024–Sep 2028, 166 partners/35 countries; Deutsche Krebsgesellschaft project page); UNCAN-Connect partners include DKFZ, KIT, UKSH, Uni Lübeck, NEC Labs Europe; EOSC4Cancer: EMBL Heidelberg participant; canSERV ended 31 Aug 2025 (BBMRI-ERIC coordinated); JANE-2, EUCanScreen, TEHDAS2 German partners: n/f. https://www.krebsgesellschaft.de/en/projects/eunetccc ; https://www.srdc.com.tr/rndprojects/uncan-connect/ ; https://cordis.europa.eu/project/id/101058427/de?format=pdf ; https://cordis.europa.eu/project/id/101058620
- OMOP: DKTK/BZKF oncology real-world data platform plans on MII FHIR core data sets; German EHDEN oncology data partners: n/f. https://www.krebsregister-rlp.de/fileadmin/user_upload/Prokosch_BZKF_ORWDP_2023-07-12.pdf
- Research data infrastructure: Medizininformatik-Initiative (MII) Kerndatensatz incl. Modul Onkologie; Netzwerk Universitätsmedizin (NUM) Routinedatenplattform; Modellvorhaben data platform with 25,000 records reported (secondary source). https://www.medizininformatik-initiative.de/Kerndatensatz/KDS_Onkologie/MIIIGModulOnkologie.html ; https://forschen-fuer-gesundheit.de/ ; https://pflege-helfer24.de/nachrichten/durchbruch-in-der-genommedizin-neue-datenbank-erreicht-25-000-datensaetze

### (d) Digital, non-FHIR, cancer-relevant
- National EHR: ePA (elektronische Patientenakte); ePA care data to flow into FDZ Gesundheit from end 2026; MIO for oncology: n/f. https://www.bundesgesundheitsministerium.de/ministerium/meldungen/rahmenbedingungen-bremsen-onkologische-versorgung-und-forschung.html
- Oncology exchange format: oBDS XML schema (3.0.5 / 3.1.0) is the national cancer registry message format; predecessor ADT/GEKID XML 2.2.1. https://basisdatensatz.de/xml-schnittstelle ; https://www.krebsregister-rlp.de/fileadmin/user_upload/2022-03-01_Presseinfo_oBDS_v3_0_0_Umsetzungsleitfaden.pdf
- oBDS logical model on FHIR for senology (BIH, oBDS 3.0.5) and oBDS-SNOMED mapping in MII Onkologie. https://bih-cei.github.io/SenologieOnFHIR/0.9.0/StructureDefinition-obds-meldung-definitions.html ; https://www.medizininformatik-initiative.de/Kerndatensatz/KDS_Onkologie/MIIIGModulOnkologie.html
- Tumour-board software: Tumorboard guideline knowledge base to be connected to established tumour-board software via an interface tool (pilot); BD CATO named as therapy planning software; VisioPA-X (Mainz, based on Krebsregister RLP VisioPA). https://www.aerztezeitung.de/Kongresse/Krebsmediziner-wuenschen-sich-mehr-digitale-Angebote-434162.html ; https://www.aerztezeitung.de/Wirtschaft/KI-Zweitmeinung-soll-Tumorboards-bei-Therapieentscheidungen-unterstuetzen-432573.html
- Screening documentation: oKFE-RL Anlage III (colorectal) and VII (cervical) electronic documentation specifications (annual spec, e.g. Spez EJ 2026). https://www.g-ba.de/downloads/40-268-11505/2025-05-15_oKFE-RL_Anpassung_Spez-EJ-2026_TrG.pdf
- Structured pathology reporting (ICCR), openEHR oncology archetypes: n/f.
- Terminology: Zentraler Terminologieserver (BfArM/gematik) hosts ICD-10-GM, OPS, ATC, SNOMED CT DE; LOINC German translation. https://www.bfarm.de/EN/Code-systems/Services/Terminologyserver/_node.html
- Digital strategy: GDNG (Gesundheitsdatennutzungsgesetz) names cancer registry linkage; PLATO 2 oncology data platform concept. https://www.bundesgesundheitsministerium.de/service/publikationen/details/plato-2

### Key organisations and people
- ZfKD at RKI (krebsdaten@rki.de); Deutsche Krebsregister e.V.; ADT; Plattform § 65c; AG Daten (oBDS). https://basisdatensatz.de/
- BfArM (FDZ Gesundheit, ZTS, classifications); gematik (KIG, ePA). https://www.bundesgesundheitsministerium.de/presse/pressemitteilungen/forschungsdatenzentrum-eroeffnet
- Deutsche Krebshilfe, Deutsche Krebsgesellschaft (EUnetCCC), DKFZ/NCT/DKTK, BZKF, TMF, MII/NUM.
- Named: Thomas Debertshäuser and Sylvia Thun (BIH at Charité, MII Onkologie); Simone Heckmann (HL7 DE TC FHIR). https://www.medizininformatik-initiative.de/Kerndatensatz/KDS_Onkologie/MIIIGModulOnkologie.html ; https://hl7.de/technische-komitees/fhir/

---

## Austria

### (a) Cancer registries
- Population-based: Österreichisches Nationales Krebsregister, run by Statistik Austria since 1969, nationwide coverage (mandatory hospital reporting); ENCR members listed historically include Statistik Austria, Tyrol and Carinthia registries. https://www.statistik.at/statistiken/bevoelkerung-und-soziales/gesundheit/krebserkrankungen ; https://publications.iarc.fr/_publications/media/download/3789/c59f506329fb5e54d3a355edbb825388ed440e50.pdf
- Clinical/regional tumour registries: Tumorregister Tirol (1986), Vorarlberg (1981), Salzburg (1985), Kärnten (1988), Tumorzentrum Oberösterreich, Onkologisches Informationssystem; regional registries act as service providers for hospitals in most Länder (not Burgenland, Styria, Vienna). https://irihs.ihs.ac.at/id/eprint/6054/1/ihs-report-2021-stacherl-czypionka-hobodites-krankheitsverlaufsbezogene-krebsregister-oesterreich-europa.pdf ; https://epidownload.i-med.ac.at/download/public/ROeS/lectures/9_Analysis%20of%20Registries/Oberaigner_W.pdf
- Screening registries: breast cancer screening programme (national, since 2014) – dedicated screening register: n/f; no national organised colorectal programme (pilots Vienna, Styria, 2026). https://www.oesterreich.gv.at/themen/gesundheit/medizinische_versorgung/screening-programm_brustkrebs-frueherkennung.html ; https://www.salzburg24.at/news/oesterreich/salzburg-muss-warten-darmkrebs-screening-in-wien-und-steiermark-ausgerollt-art-327523
- Legal basis: Krebsstatistikgesetz 1969; Krebsstatistikverordnung 2019 (BGBl. II Nr. 124/2019). https://ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2019_II_124/BGBLA_2019_II_124.pdf
- Submission format: exclusively electronic, structured, via Statistik Austria's secured interface with vbPK-AS pseudonym, within 3 months; variable groups (diagnosis, TNM, other classifications) in the ordinance annex; schema name: n/f. Coding: ICD-O-3 Revision 2 since 2020, TNM UICC 8th edition. https://www.statistik.at/fileadmin/publications/Krebserkrankungen_Berichtsjahr-2024_bf.pdf
- Data access: via Statistik Austria request form; since January 2026 records pseudonymised with bPK-AS enabling linkage with other official statistics (e.g. employment and cancer study 2025). https://www.statistik.at/en/about-us/surveys/educational-cultural-research-and-health-institutions/cancer-registry-notification ; https://www.statistik.at/fileadmin/announcement/2026/01/20260129Krebsstatistik.pdf ; https://www.statistik.at/en/statistics/labour-market/labour-and-health/employment-and-cancer

### (b) Public datasets
- Open statistics: STATcube and open.data Krebsstatistik (incidence, mortality, prevalence, survival from 1983). https://www.statistik.at/statistiken/bevoelkerung-und-soziales/gesundheit/krebserkrankungen
- Research microdata: Austrian Micro Data Center (AMDC) at Statistik Austria (registry linkage) – cancer registry in AMDC: n/f.
- ECIS: Statistik Austria contributes to ECIS (ENCR member) – explicit confirmation: n/f.
- Screening data, synthetic datasets, national data catalogue: n/f.

### (c) Cancer infrastructure
- National plan: Nationales Krebsrahmenprogramm 2026–2035 (BMASGPK with Gesundheit Österreich GmbH), successor of 2014–2025 programme. https://www.sozialministerium.gv.at/Services/Aktuelles/archiv-2026/Nationales-Krebsrahmenprogramm-2026%E2%80%932035.html
- CCCs: Austrian Comprehensive Cancer Network (ACCN) links the three university CCCs Vienna, Graz, Innsbruck; cooperation with Bayerisches Zentrum für Krebsforschung signed July 2025; OECI accreditation of Austrian CCCs in progress (ministry slide). https://ccc.meduniwien.ac.at/en/austrian-comprehensive-cancer-network-accn ; https://www.ffg.at/sites/default/files/2026-10/Barbara%20Fr%C3%B6schl_Projektvorstellung_EUnetCCC.pdf
- Genomics: Austria contributes 2,150 citizens' genomes to the 1+MG Genome of Europe reference dataset. https://www.ffg.at/europa/heu/missions/nationale-umsetzung/krebs
- Biobanks: BBMRI.at (Biobank Graz, MedUni Wien Biobank); BBMRI-ERIC headquarters in Graz. https://forschungsinfrastruktur.bmfwf.gv.at/en/eufi/bbmri-eric_2?id=4924
- EU projects: EUnetCCC (Austrian presentation by GÖG); EUCanScreen partner Gesundheit Österreich GmbH; Plattform Klinische Studien Onkologie (national trial information point). https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://www.gesundheit.gv.at/service/professional/plattform-klinische-studien-onkologie/plattform-klinische-studien-faq.html
- OMOP: EHDEN data partners Medical University of Vienna and Syndena; MedUni Wien converted national ELGA e-Medikation CDA records to OMOP. https://zenodo.org/records/6490069/files/EHDEN%20Year%203%20partner%20report_final.pdf ; https://ebooks.iospress.nl/pdf/doi/10.3233/SHTI230300
- EUCAIM, JANE-2, TEHDAS2 Austrian partners: n/f.

### (d) Digital, non-FHIR, cancer-relevant
- National EHR: ELGA, mainly HL7 CDA (e-Befund, e-Medikation, Patient Summary); oncology-specific CDA guide: n/f. https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/
- Terminology: TerminoloGit (termgit.elga.gv.at), ICD-10 BMSGPK 2026, LOINC guideline for ELGA lab reports. https://www.gesundheit.gv.at/service/professional/it-services/terminologieserver.html
- Outpatient diagnosis coding with ICD-10 mandatory from 1 July 2026 (relevant to cancer epidemiology). https://www.sozialministerium.gv.at/Themen/Gesundheit/Gesundheitssystem/Gesundheitssystem-und-Qualitaetssicherung/Dokumentation/Ambulante-Leistungs--und-Diagnosendokumentation.html
- Screening IT: e-card based automatic enrolment for breast screening. https://www.oesterreich.gv.at/themen/gesundheit/medizinische_versorgung/screening-programm_brustkrebs-frueherkennung.html
- Tumour-board software, structured pathology, openEHR: n/f.

### Key organisations and people
- Statistik Austria (cancer registry); BMASGPK and Gesundheit Österreich GmbH (Krebsrahmenprogramm, screening committee); ELGA GmbH (ELGA, SNOMED NRC, TerminoloGit); ACCN (MedUni Wien/Graz/Innsbruck); BBMRI.at; HL7 Austria (Alexander Mense chair; TC FHIR lead Anna Lin). https://www.sozialministerium.gv.at/Themen/Gesundheit/Nicht-uebertragbare-Krankheiten/Krebs/Nationales-Screening-Komitee-auf-Krebserkrankungen.html ; https://hl7.eu/affiliate_at.html

---

## Switzerland

### (a) Cancer registries
- Population-based: cantonal/regional cancer registries (13 per 2025 report; 15 covering about 94% in 2015) plus the Kinderkrebsregister (founded 1976, Bern); coordinated nationally by the Nationale Krebsregistrierungsstelle (NKRS), run by the NICER foundation (Zurich) under EDI mandate since 2018; full coverage mandatory since the KRG took effect 1 Jan 2020. https://www.nkrs.ch/de/ueber-uns ; https://heise.de/-10269136 ; https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/switzerland-2015/organization-and-governance/health-information-management
- ENCR members: cantonal registries incl. Graubünden/Glarus, Neuchâtel/Jura, Ostschweiz, Ticino, Valais, Vaud. https://encr.eu/encr-members-contact-list?page=17
- Screening registries: cantonal screening programmes (mammography, colorectal) coordinated by Swiss Cancer Screening; registry data linked with screening programmes per NKRS. https://www.nkrs.ch/de/die-krebsregistrierung-kurz-erklaert/registrierte-daten
- Legal basis: Krebsregistrierungsgesetz (KRG) and Krebsregistrierungsverordnung (KRV), in force 1 Jan 2020; reporting within 4 weeks. https://www.bag.admin.ch/de/krebserkrankungen-meldepflicht-und-informationspflicht ; https://www.swissinfo.ch/eng/sci-tech/health_swiss-to-register-all-cancer-cases-from-2020/45459952
- Submission format: "Austauschformat KRG" (BAG, FHIR-based, released 8 Jan 2020, 30 structured variables, voluntary) alongside PDF/paper reporting; NKRS national data structure v1.5 variable lists (Basisdaten, Zusatzdaten Erwachsene, Zusatzdaten Kinder), "Einführung Datenstruktur v1.1"; ICD-O-3 and TNM editions: n/f. https://www.bag.admin.ch/de/datenformat-krebsregistermeldung ; https://www.nkrs.ch/de/downloads
- Data access: NKRS provides anonymised basic data and authorisation-requiring data to researchers (pages "Anfrage anonymisierte Daten", "Anfrage bewilligungspflichtige Daten"); NKRS also delivers data to BFS. https://www.nkrs.ch/de/forschung/anfordern-anonymisierter-grundlagendaten ; https://www.nkrs.ch/de/forschung/zugang-zu-bewilligungspflichtigen-daten

### (b) Public datasets
- Open statistics: NKRS "Statistiken zu Krebs", Krebsmonitoring/Krebsbericht, Kennzahlen zu Diagnose und Therapie (e.g. breast 2020–2022, prostate 2020–2023); BFS cancer statistics. https://www.nkrs.ch/ ; https://www.bfs.admin.ch/bfs/en/home/statistics/health/surveys/ke.html
- Research data access: SPHN/BioMedIT federated dataset of >800,000 patients incl. oncology; Swiss Cancer Institute (ex SAKK) onboarded to SPHN 2025. https://sphn.ch/2026/02/03/new-institutions-onboarded_2025/ ; https://bioalps.org/sphn-releases-clinical-data-from-800000-patients/
- ECIS contribution, synthetic datasets, national health data catalogue: n/f (DigiSanté programme working on secondary-use data space). https://www.digisante.admin.ch/dam/de/sd-web/hbuj5RvqfFlY/20250501_Case%20study%20Health%20services%20research_UniSant%C3%A9%20V1.0.pdf

### (c) Cancer infrastructure
- National plan/institute: Nationale Strategie gegen Krebs (ended), NCD strategy; Swiss Cancer Institute (formerly SAKK) runs the clinical trial network (22 centres) and SCORED real-world data. https://sphn.ch/network/projects/driver-projects/project-page_swiss-personalized-oncology/
- CCCs/OECI: n/f.
- Genomics/personalised health: SPHN (phase 3, 2025–2028, CHF 20.7 M per Wikipedia mirror), driver project Swiss Personalized Oncology (SPO), SVIP-O variant platform. https://sphn.ch/network/projects/driver-projects/project-page_swiss-personalized-oncology/ ; https://isb-sib.ch/news/a-key-ingredient-of-swiss-precision-oncology-svip-o-goes-live
- Biobanks: Swiss Biobanking Platform (SBP) is BBMRI-ERIC national node; Switzerland full member since June 2023 (SERI). https://www.bbmri-eric.eu/national-nodes/switzerland/
- Paediatrics: SwissPedHealth (national data stream) with nested SwissPedCancer project testing automated transfer from clinical data warehouses to the registry. https://www.researchprotocols.org/2026/1/e87007
- OMOP: five Swiss EHDEN data partners (Basel, Bern, Geneva, Vaud incl. Unisanté). https://ehden.eu/datapartners/
- EU projects (EUCAIM, EUnetCCC, JANE-2, TEHDAS2): Swiss participation n/f; Switzerland is in Clinnova with Luxembourg, France, Germany. https://www.lih.lu/en/news/page/6/
- Research data infrastructure: SPHN/BioMedIT; DigiSanté (federal digital health programme 2025–2034) and planned Swiss Health Data Space. https://www.digisante.admin.ch/dam/de/sd-web/9zrTcNIxTGda/Schlussbericht%20Standardisierung%20im%20SwissHDS%20mit%20FHIR.pdf

### (d) Digital, non-FHIR, cancer-relevant
- National EHR: EPD (elektronisches Patientendossier), IHE XDS based, CDA documents; oncology content: n/f. https://www.e-health-suisse.ch/
- Registry exchange: BAG "Austauschformat KRG" (FHIR); legacy PDF-based reporting (use case 1a embeds PDF reports). https://www.bag.admin.ch/de/datenformat-krebsregistermeldung
- Registry software: cantonal registries' joint software project failed (secondary source: heise 2025). https://heise.de/-10269136
- Coding: ICD-10-GM and CHOP (BFS Medizinische Klassifikationen), CHOP 2026 in force 1 Jan 2026. https://ckan.opendata.swiss/dataset/schweizerische-operationsklassifikation-chop10
- Semantic framework: SPHN semantic interoperability framework (RDF-based) used by Swiss Personalized Oncology core dataset. https://sphn.ch/network/projects/driver-projects/project-page_swiss-personalized-oncology/
- Tumour-board software, structured pathology, openEHR: n/f.

### Key organisations and people
- BAG Abteilung Prävention nichtübertragbarer Krankheiten (KRG, Austauschformat; krebsregistrierung@bag.admin.ch); NKRS/NICER (Zurich, info@nkrs.ch); Kinderkrebsregister (Bern); BFS; Swiss Cancer Institute; SPHN; SBP (Christine Currat / Christine Joye named by BBMRI-ERIC); eHealth Suisse (SNOMED NRC); HL7 Switzerland (Oliver Egger, Michaela Ziegler, ahdis). https://www.nkrs.ch/de/ueber-uns ; https://www.bbmri-eric.eu/national-nodes/switzerland/ ; https://github.com/hl7ch/ch-core

---

## Netherlands

### (a) Cancer registries
- Population-based: Nederlandse Kankerregistratie (NKR), run by IKNL since 1989, nationwide; data collected by IKNL data managers from hospital records after notification via PALGA and DHD; about 125,000 partly manual and 60,000 fully automated records (2024). https://iknl.nl/nkr ; https://iknl.nl/getmedia/5e2b2905-4cf4-465c-985f-7eaa037febee/IKNL-Jaarverslag-2024.pdf
- ENCR membership: n/f in the contact-list pages retrieved; NKR contributes to ECIS. https://www.icthealth.org/news/ecis-update-improves-understanding-of-european-cancer-trends
- Pathology registry: PALGA (since 1991, all 64 pathology laboratories), 40–60 data applications per year. https://onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn/doi/abs/10.1155/2007/971816 ; https://iknl.nl/en/ncr/apply-for-data/data-linkage-iknl-palga
- Screening: Bevolkingsonderzoek Nederland runs the breast, cervical and colorectal programmes (screening IT "ScreenIT"): n/f.
- Legal basis: NKR operates on legal basis of scientific research and statistics in the public health interest (no individual consent). https://iknl.nl/nkr
- Submission format and dictionary: per-diagnosis NKR itemset; automated EHR extraction via IKNL FHIR IG (R(H)ONDA, 20 hospitals); linkage files in CSV or fixed-width ASCII; coding ICD-O-3 and UICC TNM 8; tumour-type file "RANK Bestandsindeling tumorsoort" 2025/2026. https://www.oncologie.nu/nieuws/validatie-van-geautomatiseerde-realtime-gegevensuitwisseling-van-epds-naar-nkr/ ; https://iknl.nl/getmedia/185b0869-edc9-4f5a-84b2-12d8716bc074/Instructie-aanvrager-format-koppeling.pdf ; https://iknl.nl/getmedia/b7276fdb-be51-4f1d-aa3a-e20311af8c4f/RANK-Bestandsindeling-tumorsoort-2025.pdf
- Data access: IKNL data request reviewed by privacy board (CvT) and scientific committee; turnaround 2 weeks (basic figures) to 4 months (complex/linkage with CBS, PALGA, cohorts). https://iknl.nl/en/NCR/Apply-for-data

### (b) Public datasets
- Open statistics: NKR cijfers (1989–2024, 2023/2024 preliminary). https://iknl.nl/en/ncr/ncr-data-figures
- Synthetic dataset mimicking part of the NKR, free for researchers. https://iknl.nl/en/ncr/synthetic-dataset
- OMOP: NKR data available in OMOP CDM as EHDEN data partner, listed in EHDEN Data Catalogue. https://iknl.nl/en/news/ncr-data-in-omop-cdm
- Research data access bodies: CBS microdata (remote access, output checking); HDAB-NL (national Health Data Access Body) in preparation; Health-RI and IKNL MoU on research data availability; Health-RI coordinates EU project CANDLE on cancer data nodes. https://www.cbs.nl/en-gb/our-services/customised-services-microdata/microdata-conducting-your-own-research ; https://iknl.nl/getmedia/67eb1c67-8910-433b-b6df-6081b37a63eb/IKNL-Jaarplan-2025.pdf ; https://iknl.nl/en/news/iknl-ehds-en
- Screening data: n/f.

### (c) Cancer infrastructure
- National plan: Nederlandse Kankeragenda (20 goals) by the Nederlands Kanker Collectief; NKC Hub is the national cancer mission hub in ECHoS. https://iknl.nl/en/news/echos-2
- OECI: NKI-AVL (Amsterdam) comprehensive cancer centre; Maastricht UMC+ CCC re-accredited with Research Excellence; Erasmus MC Cancer Institute and Radboudumc listed as OECI cancer centres; UMCG listed as CCC (secondary sources). https://www.maastrichtuniversity.nl/news/maastricht-umc-comprehensive-cancer-center-re-accredited-oeci-research-excellence-designation ; https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: Hartwig Medical Foundation (WGS database): access details n/f; 1+MG participation: n/f.
- Biobanks: BBMRI-NL: n/f in this survey.
- Imaging: EUCAIM Dutch partners: n/f.
- EU projects: CancerWatch (Sept 2025–Aug 2028, IKNL partner); ECHoS (NKC Hub); EUCanScreen (Ministry of VWS associated partner); TEHDAS2 (RIVM). https://www.icthealth.org/news/eu-launches-cancerwatch-for-better-and-faster-cancer-data ; https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://www.rivm.nl/en/international-projects/tehdas2
- Research data infrastructure: Health-RI (national health data infrastructure); Oncode Institute. https://iknl.nl/en/news/iknl-ehds-en

### (d) Digital, non-FHIR, cancer-relevant
- Information standards: Informatiestandaard Mammacarcinoom (IKNL with NABON, ART-DECOR, zib 2017), Gegevensset Oncologie Algemeen plus tumour-specific datasets (Zorginstituut: >80% of colorectal dataset generic); uptake still low (Nictiz 2024). https://nictiz.nl/app/uploads/2024/08/ICThealth_nr4_2024_10-11.pdf ; https://wpn.nen.nl/app/uploads/sites/16/2024/09/Zorginstituut-Nederland-Sterk_datafundament_voor_kwaliteit_van_zorg-def.pdf
- zibs: TNMTumorClassificatie v4.1 (2025) and related oncology zibs on zibs.nl. https://www.zibs.nl/wiki/TNMTumorClassificatie-v4.1(2024NL)
- Regional oncology networks: IHE-NL guideline MDO (multidisciplinary consultation) 2021; OncoNext data re-use initiative. https://ihe-nl.org/wp-content/uploads/2022/07/IHE-Guideline-MDO-and-Addendum-2021-English-Final.pdf ; https://oncologie.nu/nieuws/onconext-de-volgende-stap-naar-betere-beschikbaarheid-en-hergebruik-van-medische-gegevens
- Pathology: PALGA protocol module (PPM) for synoptic reporting, national PALGA protocols approved by NVVP; PALGA codes aligned to SNOMED. https://richtlijnendatabase.nl/richtlijn/schildkliercarcinoom_2024/pathologie_bij_rl_schildkliercarcinoom/pathologie_-_protocollaire_verslaglegging_palga.html ; https://wiki.hl7.org/Pathology_Report-abstracts_Request_Use_Case_(Linda_Mook)
- Lab coding: Nederlandse Labcodeset (LOINC 2.83). https://labterminologie.nl/
- Palliative/advance care planning: IKNL PZP IG (STU3/R4). https://api.iknl.nl/docs/pzp/r4/1.0.0-rc2/index.html
- Patient portals, Oncoguide, chemotherapy ePrescription, openEHR: n/f.

### Key organisations and people
- IKNL (NKR; NkrIG contributors jeroen-trompetter, basharmsen, Harmke Koning), PALGA, Nictiz (zibs, NTS, SNOMED NRC), Health-RI, Nederlands Kanker Collectief, RIVM (WHO-FIC, TEHDAS2), CBS, Bevolkingsonderzoek Nederland. https://github.com/IKNL/NkrIG ; https://iknl.nl/en/news/iknl-ehds-en

---

## Belgium

### (a) Cancer registries
- Population-based: Belgian Cancer Registry (Stichting Kankerregister / Fondation Registre du Cancer), national since 2004, mandatory registration by oncological care programmes and pathology laboratories (law of 2006); data on screening also collected; ENCR member (National Cancer Registry listed). https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2019.00120/full ; https://publications.iarc.fr/_publications/media/download/3789/c59f506329fb5e54d3a355edbb825388ed440e50.pdf
- Clinical registration: via multidisciplinary oncology consultation (MOC/COM) reimbursed under the 2003 royal decree on oncological care programmes; form Bijlage 55 (RIZIV Verordening 28-07-2003, amended 15-12-2025). https://www.riziv.fgov.be/SiteCollectionDocuments/formulier_verordening20030728_bijlage_55.docx
- Screening: BCR collects screening data; Flemish Centrum voor Kankeropsporing screening register: n/f; Sciensano is EUCanScreen partner. https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf
- Submission format: WBCR web application or batch extraction; healthdata.be BCR_Cancer collection (v1.1, CSV via HD4DP) with ICD-O-3 topography/morphology, CODAP, SNOMED axes and UICC TNM; TNM edition: n/f. https://dcd.healthdata.be/en/collection/BCR_Cancer/
- Data access: BCR "data request" for in-depth research; linkage via trusted third parties (eHealth TTP, CBSS); national registry number enables linkage with health insurance (IMA) and hospital discharge data (ISC deliberation 18/178, 2025). https://www.in.ehealth.fgov.be/ehealthplatform/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/82f246426c189e659fa2372a0f5936dcad93ea8d/18-178-n184-herval-bij-borst--en-gynaecologische-kankerpatienten-stichting-kankerregister-gewijzigd-op-6-mei-2025.pdf

### (b) Public datasets
- Open statistics: BCR publishes incidence, prevalence, mortality, survival (20 years of statistics, >78,000 new diagnoses); Sciensano Belgian National Burden of Disease cancer dashboard. https://kankerregister.org/en/ ; https://burden.sciensano.be/shiny/cancer/
- Research access body: Health Data Agency (HDA, law of 14 March 2023, launched 17 Jan 2024) building a national metadata catalogue; healthdata.be (Sciensano) hosts data collections. https://www.hoganlovells.com/en/publications/creation-of-a-health-data-agency-in-belgium-a-key-agency-for-the-future-european-health-data-space ; https://dcd.healthdata.be/en/collection/BCR_Cancer/
- OMOP: BCR breast and lung dataset (incidence 2014–2023) mapped to OMOP, ETL in progress (EMA catalogue). https://catalogues.ema.europa.eu/node/4943/data-flows-and-management
- Tumour bank: Belgian Virtual Tumourbank catalogue (BVTc) coordinated by BCR, 11 university hospitals. https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2019.00120/full
- ECIS contribution, synthetic datasets: n/f.

### (c) Cancer infrastructure
- National plan: National Cancer Plan 2008 (Onkelinx); current cancer plan 2025: n/f. https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2019.00120/full
- OECI: Leuven Cancer Institute recognised as Comprehensive Cancer Centre (Jan 2025); Institut Jules Bordet listed as OECI CCC (secondary source). https://www.uzleuven.be/en/nieuws/oeci ; https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- EU projects: EUnetCCC partners Sciensano, UZ Antwerpen, KU Leuven, Cliniques universitaires Saint-Luc, UGent; EUCAIM (Sciensano project list); TEHDAS2 (Sciensano); EUCanScreen (Sciensano). https://sciensano.be/en/projects/european-network-comprehensive-cancer-centre ; https://www.sciensano.be/en/taxonomy/term/305/projects-all ; https://sciensano.be/en/print/projects/second-joint-action-towards-european-health-data-space
- Genomics: Sciensano owns NGS data of BALLETT/GeNeo precision oncology trials (BSMO). https://pmc.ncbi.nlm.nih.gov/articles/PMC12420906
- Biobanks: BBMRI.be national network incl. BVT. https://www.gigabiotheque.uliege.be/cms/c_6227843/en/gigabiotheque-networks
- OMOP: 14 Belgian EHDEN data partners incl. UZ Brussel, UZA, UZ Leuven. https://ehden.eu/datapartners/

### (d) Digital, non-FHIR, cancer-relevant
- National exchange: KMEHR (legacy XML standard), eHealth platform hubs (Vitalink, RSW, Abrumet); KMEHR oncology content: n/f. https://ehealth.fgov.be/standards/kmehr/en/page/hl7-fhir-governance
- Registry forms: Bijlage 55 paper/web form; healthdata.be HD4DP2 collection tooling with code lists (ICD-10-CM, ICD-O-3). https://fair-v1.healthdata.be/book/export/html/10094
- Coding: ICD-10-BE (hospital MZG/RHM, since 2015), coding tool icd10be.health.belgium.be; SNOMED CT Belgian edition via Ontoserver. https://www.health.belgium.be/sites/default/files/uploads/fields/fpshealth_theme_file/passage_a_licd-10-be_version_2023_et_au_apr-drg_version_v40.0.pdf
- PROMs/PREMs project at BCR (ISC deliberation 25/124). https://www.ehealth.fgov.be/ehealthplatform/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/fe87d440cf3b4806455ff4b5f321469af07462a3/25-124-n256-project-proms-prems-bcr.pdf
- Tumour-board software, structured pathology, openEHR, ePrescription oncology: n/f.

### Key organisations and people
- Belgian Cancer Registry (Brussels), Sciensano / healthdata.be, Health Data Agency, FPS Public Health Terminology Centre, RIZIV/INAMI, eHealth platform (Bart Decuypere), HL7 Belgium (Jose Costa Teixeira), Tiro.health (Axel Vanraes). https://kankerregister.org/en/ ; https://hl7.eu/affiliate_be.html

---

## Luxembourg

### (a) Cancer registries
- Population-based: Registre National du Cancer (RNC), hosted at Luxembourg Institute of Health (LIH, EPICAN group), covering residents and non-residents diagnosed or treated in Luxembourg; ENCR membership: n/f. https://researchportal.lih.lu/en/projects/registre-national-du-cancer-national-cancer-regestry/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12668946/
- Clinical registries, screening registries: organised breast (Programme Mammographie) and colorectal programmes run by the Direction de la santé, age lowered to 45 from 2024; LIH/EPICAN evaluates the mammography programme by linking RNC data. https://chronicle.lu/category/medical/59357-luxembourg-takes-action-to-improve-cancer-screening-and-prevention ; https://lih.lu/?p=42090
- Legal basis: n/f (règlement grand-ducal on RNC not retrieved).
- Submission format and dictionary: n/f.
- Data access: RNC data linkage scoping review (2025) names legal permission, data availability, data flow, linkage key and method as prerequisites; partners IBBL and IGSS. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12668946/

### (b) Public datasets
- RNC reports (incidence and mortality 2014–2021, Nov 2025); OECD country cancer profile 2025. https://www.lih.lu/en/research-scope/research-department/department-of-precision-health/cancer-epidemiology-and-prevention-epican/
- Research data access: Luxembourg National Data Service (LNDS) (TEHDAS2 page); RNC is EHDEN data partner with planned OMOP conversion (2021 announcement). https://www.lnds.lu/?p=4771 ; https://www.researchluxembourg.org/en/luxembourg-to-speed-up-the-standardisation-of-clinical-data/ ; https://zenodo.org/records/6490069/files/EHDEN%20Year%203%20partner%20report_final.pdf
- ECIS contribution, synthetic datasets, catalogue: n/f.

### (c) Cancer infrastructure
- National plan: Plan National Cancer 2 (PNC2, 2020–2026) with digitalisation priority; Institut National du Cancer (INC) created under PNC2 to coordinate cancer activities. https://chronicle.lu/category/medical/31407-luxembourg-approves-second-national-cancer-plan-based-on-digitalisation-innovation ; https://luxtoday.lu/fr/sant-et-environnement/oncologie-au-luxembourg-cancer-chez-les-jeunes-et-nouvelles-mesures-de-soutien-aux-patients
- CCCs/OECI: n/f.
- Genomics: LuxGen Genome Center (LIH); 1+MG: n/f.
- Biobanks: Integrated Biobank of Luxembourg (IBBL, LIH). https://www.lih.lu/en/news/page/6/
- EU projects: CancerWatch (LIH/RNC, Sept 2025–Aug 2028); Clinnova cross-border (LU, FR, DE, CH); Dataspace4Health oncology use case; EUCanScreen Luxembourg entry: n/f. https://www.lih.lu/wp-content/uploads/2025/09/CancerWatchPR_FR.pdf ; https://www.lih.lu/en/news/page/6/

### (d) Digital, non-FHIR, cancer-relevant
- National EHR: Dossier de Soins Partagé (DSP, Agence eSanté); oncology content: n/f.
- Terminology, structured pathology, tumour-board software, openEHR: n/f.
- Digital strategy: PNC2 digitalisation axis incl. diagnosis-reporting tools (2025 actions). https://luxtoday.lu/fr/sant-et-environnement/oncologie-au-luxembourg-cancer-chez-les-jeunes-et-nouvelles-mesures-de-soutien-aux-patients

### Key organisations and people
- LIH (RNC, EPICAN, IBBL, LuxGen), Direction de la santé / Ministère de la Santé (Martine Deprez, minister), Institut National du Cancer, LNDS, Agence eSanté, Laboratoire national de santé (LNS). https://www.lih.lu/en/research-scope/research-department/department-of-precision-health/cancer-epidemiology-and-prevention-epican/ ; https://www.lnds.lu/?p=4771

---

## Cross-cutting EU projects (verified facts)
- EUnetCCC: Joint Action 1 Oct 2024–30 Sep 2028, 166 partners in 35 countries, follow-up of CraNE (2022–2024). https://sciensano.be/en/projects/european-network-comprehensive-cancer-centre
- JANE-2: coordinated by Fondazione IRCCS Istituto Nazionale Tumori Milan, 121 partners from 29 countries. https://health.ec.europa.eu/non-communicable-diseases/cancer/europes-beating-cancer-plan-eu4health-financed-projects/projects/jane-2_en
- canSERV: Horizon Europe, coordinated by BBMRI-ERIC, ended 31 Aug 2025. https://cordis.europa.eu/project/id/101058620
- EUCanScreen: coordinated by University of Latvia (consortium list Oct 2025). https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf
- TEHDAS2: May 2024–end 2026, Sitra coordinated, 68 partners/30 countries. https://grnet.gr/en/?p=21645
- EUCAIM: 12 countries, 83 datasets (106,968 subjects), EDIC in preparation. https://digital-strategy.ec.europa.eu/en/policies/cancer-imaging
- EHDEN: >187 data partners in 29 countries; partner list by country. https://ehden.eu/datapartners/
- CancerWatch: Sept 2025–Aug 2028, coordinated by Norwegian Institute of Public Health. https://www.icthealth.org/news/eu-launches-cancerwatch-for-better-and-faster-cancer-data
