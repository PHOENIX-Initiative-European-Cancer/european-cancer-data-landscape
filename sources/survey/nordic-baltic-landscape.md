# Non-FHIR digital cancer landscape: Nordic and Baltic countries

Companion to `nordic-baltic.md` (FHIR survey). Compiled 2026-11-18, verification pass 2026-11-19 (see nordic-baltic-verification-log.md) from web search and direct page downloads. One bullet = one fact with its source URL. "n/f" = not found in a primary source. Cross-cutting partner lists (TEHDAS2, EUCAIM, EHDEN, EUCanScreen, ECHoS, JANE-2) were read from the project partner pages and are cited per country.

Cross-cutting sources used repeatedly:
- TEHDAS2 partner page: https://tehdas.eu/partners/
- EUCAIM (Cancer Image Europe) partner page: https://cancerimage.eu/partners/
- EHDEN data partner catalogue: https://www.ehden.eu/datapartners/
- DARWIN EU onboarded data partners (EMA): https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- EUCanScreen participants: https://www.fhi.no/en/projects/eucanscreen/eucanscreen-list-of-participants/
- ECHoS consortium: https://ki.se/en/cancerresearchki/a-new-european-consortium-funded-with-6-million-euros-will-create-a-network-of
- JANE-2 partner listing: https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/
- EUnetCCC: https://sciensano.be/en/projects/european-network-comprehensive-cancer-centre
- NORDCAN 2.0: https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- ECIS contributing registries: https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Nordic registry comparison (Engholm/Pukkala et al.): https://medicaljournalssweden.se/actaoncologica/article/view/24912
- Nordic OECI study 2026: https://pubmed.ncbi.nlm.nih.gov/41941979/
- BBMRI-ERIC annual report 2025: https://www.bbmri-eric.eu/annual_report_2025_singlepages/

---

## Denmark

### (a) Cancer registries
- Population-based: Cancerregisteret (Danish Cancer Registry), founded 1942/43, controller Sundhedsdatastyrelsen (Danish Health Data Authority), mandatory reporting since 1987; electronic since 2004. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://www.encr.eu/node/169
- Coverage: Nordic overview reports close to 100% completeness of incident solid malignancies in all Nordic registries; Danish register declaration estimates coverage above 95% (mandatory reporting since 1987) (verified 2026-11-19) https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf https://medicaljournalssweden.se/actaoncologica/article/view/24912
- ENCR/IACR: listed on encr.eu; member of Association of Nordic Cancer Registries (ANCR). https://www.encr.eu/node/169 ; https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: DMCG (Danske Multidisciplinære Cancer Grupper, est. 2005) run cancer-specific quality databases hosted by RKKP (Regionernes Kliniske Kvalitetsudviklingsprogram); 25 diagnosis-specific registries; annual reports published on sundhed.dk (e.g. DCCG colorectal, DBCR childhood cancer, DGCD gynaecological). https://cdn2.gopublic.dk/indenrigssundhedsmin/Media/638415267703842146/Danske%20Multidisciplin%C3%A6re%20Cancer%20Grupper.pdf ; https://informahealthcare.com/doi/full/10.1080/0284186X.2020.1820573 ; https://www.sundhed.dk/content/cms/81/4681_dccg-aarsrapport-2022_offentliggjort-version.pdf
- Screening registries: RKKP quality databases DKMS (mammography, est. 2007), DKLS (cervical screening) and DTS (bowel screening, covers 96% of invited target group); annual reports on sundhed.dk (verified 2026-11-19) https://sundhed.dk/content/cms/78/4678_dkms-aarsrapport-2024-offentliggjort-version-20240527.pdf ; https://sundhed.dk/content/cms/82/4682_dkls-aarsrapport-2023_offentliggjort-version-270624.pdf ; https://www.sundhed.dk/content/cms/45/61245_dts-aarsrapport-2022-offentliggjort-version-20240308.pdf
- Submission format: hospital data via Landspatientregisteret LPR3 (mandatory cTNM, optional pTNM; LPR3 reporting guide 2025 v5.1); pathology via Patobank using MEDRPT EDI messages, daily FTP. https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf ; https://www.retsinformation.dk/eli/lta/2018/1049/pdf
- Variable dictionary / coding: ICD-10 diagnosis plus ICD-O-3 morphology since 2004 (1978–2003 converted); TNM mandatory since 2004, coded by clinicians under UICC 5/6/7 in 2004–2016 period; register declaration codes extent per the current ('gældende') TNM edition, LPR3 v5.1 requires qualified cTNM and defers the edition to clinical guidelines; edition number not fixed in registry documents (verified 2026-11-19) https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638650952569270242/Registerdeklaration%20Cancerregisteret.pdf ; https://medicaljournalssweden.se/actaoncologica/article/download/24253/28421/74284
- Legal basis: Sundhedsloven and the reporting order (Bekendtgørelse om lægers anmeldelse til Cancerregisteret, 2018). https://www.retsinformation.dk/eli/lta/2018/1049/pdf
- Researcher access: Sundhedsdatastyrelsen Forskerservice (Research Services), data delivered on the Secure Research Platform (no internet); foreign researchers need a Danish data-responsible partner; Statistics Denmark hosts linked microdata. https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/research-services ; https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/research-services/the-secure-research-platform ; https://www.dst.dk/en/TilSalg/Forskningsservice/Data/Andre_Styrelser

### (b) Public datasets
- Open statistics: eSundhed.dk cancer topic; annual report "Nye kræfttilfælde i Danmark 2024" (published 25 June 2025) with municipality tables. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/Media/638938615398782138/Nye%20kr%C3%A6fttilf%C3%A6lde%202024,%20fordelt%20p%C3%A5%20kommuner%20(udgivet%2025.%20juni%202025).pdf ; https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/media/16526/Kraefttilfaelde%202023.pdf
- NORDCAN 2.0 participant (incidence, mortality, survival, prevalence since 1943). https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- ECIS contributor: Danish Cancer Registry among ENCR registries contributing to ECIS. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Research data access body (EHDS): Sundhedsdatastyrelsen; TEHDAS2 partners: Danish Health Data Agency, Aarhus University Hospital, Central Denmark Region. https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/european-health-data-space ; https://tehdas.eu/partners/
- Quality database annual reports (RKKP/DMCG) are public on sundhed.dk. https://www.sundhed.dk/content/cms/87/16287_dbcr-aarsrapport-2022.pdf
- Synthetic datasets: n/f
- National health data catalogue: n/f (EMA catalogue lists "Danish Health Data Registries"). https://catalogues.ema.europa.eu/node/1145/data-flows-and-management

### (c) Cancer infrastructure
- National plan: Kræftplan IV (2016); Kræftplan V published by the government on 23 May 2025 with 36 initiatives, implementation agreement with Danske Regioner and KL dated 27 November 2025 (verified 2026-11-19) https://medcom.dk/wp-content/uploads/2026/08/Bilag-2-Udmoentningsaftale-om-Kraeftplan-V-2026-og-frem.pdf ; https://www.ism.dk/Media/638926676927162662/KPV-udmoentningsaftale-2025.pdf ; https://www.sst.dk/-/media/Udgivelser/2016/Styrket-indsats-på-kræftområdet-–-et-fagligt-oplæg-til-Kræftplan-IV/styrket-indsats-paa-kraeftomraadet-2016-fagligt-oplaegt-til-kraeftplan-IV-2016.ashx
- Danish Comprehensive Cancer Center (DCCC), national network of regions and DMCG. https://www.regioner.dk/media/3849/danish-comprehensive-cancer-center-modelpapir.pdf
- OECI: Aarhus University Hospital joined OECI June 2023; final report and notification certificate as "Aarhus University Hospital Comprehensive Cancer Centre" (2026). Aarhus OECI site visit March 2026 with board decision expected May 2026 https://www.fagperson.auh.dk/siteassets/04-forskning-og-udvikling/aarhus-comprehensive-cancer-centre/c-udvikling-og-akkreditering/260327_audit_closing_meeting.pdf . OECI accredited-centres list (2026-11-19) shows three Danish entries: Aarhus University Hospital CCC, Copenhagen CCC Rigshospitalet and Herlev-Gentofte, and Vejle Cancer Centre Lillebaelt Hospital; Odense is not listed (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://www.fagperson.auh.dk/siteassets/04-forskning-og-udvikling/aarhus-comprehensive-cancer-centre/nyt-fra-ccc/nyheder/2026/vigtig-international-anerkendelse/aarhus-final-report-and-notification-certificate.signed.pdf
- Genomics: Nationalt Genom Center (National Genome Center) runs national WGS programme incl. oncology patient groups (QIAGEN interpretation adopted 2023; data must stay in Denmark); national personalised medicine strategy 2021–2022. https://www.selectscience.net/article/danish-national-genome-center-selects-qiagen-for-variant-interpretation-in-oncology-genome-sequencing ; https://admin.ism.dk/Media/637616833229549022/Danish%20Strategy%20for%20personalised%20medicine%202021%202022.pdf
- 1+MG / Genome of Europe: Denmark listed as 1+MG observer (not signatory) in 2018-era sources; Danish National Genome Center is the Genome of Europe partner (1,414 samples to be sequenced) (verified 2026-11-19) https://genomeofeurope.eu/partners/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7115898 . Nationalt Genom Center merged into Sundhedsdatastyrelsen 1 July 2025 https://www.altinget.dk/sundhed/artikel/styrelse-og-nationalt-genom-center-laegges-sammen-centerdirektoer-fortsaetter
- Biobank: Danish National Biobank (SSI); Denmark is BBMRI-ERIC observer, not full member (2025 report). https://www.bbmri-eric.eu/annual_report_2025_singlepages/
- Imaging infrastructure: EUCAIM Danish partner n/f (partner page lists none). https://cancerimage.eu/partners/
- EU projects: TEHDAS2 (Danish Health Data Agency, AUH, Central Denmark Region); EUCanScreen (Region Syddanmark); ECHoS Danish partner still n/f; EUnetCCC Danish participants: Region Hovedstaden, Aarhus Universitet, Region Syddanmark, Region Sjælland, Aarhus Universitetshospital (grant data sheet) (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf ; JANE-2 n/f. https://tehdas.eu/partners/ ; https://www.fhi.no/en/projects/eucanscreen/eucanscreen-list-of-participants/
- OMOP/EHDEN: EHDEN data partners Center for Surgical Science (Region Hovedstaden) and University of Southern Denmark; DARWIN EU onboarded "Danish Health Data Registries". https://www.ehden.eu/datapartners/ ; https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: Sundhedsdatastyrelsen leads EHDS implementation (regulation in force 25 March 2025; four supporting projects); Sundhedsdatastyrelsen, MedCom, sundhed.dk and Nationalt Genom Center will be merged into Digital Sundhed Danmark on 1 January 2027 (preparatory management from 1 January 2026) (verified 2026-11-19) https://english.sundhedsdatastyrelsen.dk/about-us/digital-health-denmark . https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/european-health-data-space

### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: sundhed.dk (national portal, hosts quality database reports; patient access to records). https://www.sundhed.dk/
- EHR: Sundhedsplatformen (Epic) in Region Hovedstaden and Sjælland; other regions use Systematic Columna; chemotherapy module details n/f. n/f
- Exchange formats: MedCom EDIFACT/XML messages; pathology to Patobank via MEDRPT EDI; LPR3 reporting via SEI/XML. https://cdn1.gopublic.dk/sundhedsdatastyrelsen/media/15228/SEI_LPR_Manual.pdf
- Structured pathology: Patobank, SNOMED-coded (Danish SNOMED pathology codes, converted to ICD-O-3 by conversion tables). https://cdn1.gopublic.dk/sundhedsdatastyrelsen/media/15733/FI%20Registrering%20Patologi.pdf
- Tumour-board/MDT software: n/f
- National cancer datasets not in FHIR: DMCG/RKKP database variable sets; LPR3 cancer-specific reporting rules. https://cdn.sundhedsdatastyrelsen.dk/sundhedsdatastyrelsen/Media/638955095432142451/LPR-indberetningsvejledning_2025_v.5.1.pdf
- Chemotherapy / ePrescription: FMK (Fælles Medicinkort) national medication record; hospital chemo systems n/f. n/f
- openEHR oncology: n/f
- Digital health strategy naming cancer: DMCG.dk calls for a national cancer data platform. https://cdn2.gopublic.dk/indenrigssundhedsmin/Media/638415267703842146/Danske%20Multidisciplin%C3%A6re%20Cancer%20Grupper.pdf

### Key organisations and people
- Sundhedsdatastyrelsen (Cancerregisteret, Forskerservice, EHDS); RKKP; DMCG.dk; DCCC; Nationalt Genom Center; Kræftens Bekæmpelse (Danish Cancer Society, Registry Core Function); MedCom; Aarhus University Hospital CCC. People: Maya Christel Milter (Director, Danish Cancer Registry, ENCR page) (verified 2026-11-19) https://www.encr.eu/node/169 .

---

## Sweden

### (a) Cancer registries
- Population-based: Cancerregistret at Socialstyrelsen, founded 1958; mandatory reporting; six Regional Cancer Centres (RCC) check, code and compile notifications annually. https://socialstyrelsen.se/statistik-och-data/register/cancerregistret/framstallning-och-kvalitet/ ; https://cancercentrum.se/syd/regional-cancer-centres/knowledge-based-healthcare/cancer-registry/
- Coverage: near 100% completeness (Nordic overview); Sweden lacks legal basis to use death certificates to supplement the registry. https://medicaljournalssweden.se/actaoncologica/article/view/24912
- ENCR/IACR: Swedish Cancer Registry listed by ENCR; ANCR member. https://catalogues.ema.europa.eu/node/1097/data-flows-and-management ; https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: about 30 national cancer quality registers on the INCA platform (RCC i samverkan), plus Individuell patientöversikt (IPÖ). https://cancercentrum.se/syd/regional-cancer-centres/knowledge-based-healthcare/national-swedish-cancer-registry/ ; https://akademiska.se/en/departments/specialist-healthcare/uppsala-comprehensive-cancer-centre/our-services/quality-data-at-uppsala-comprehensive-cancer-centre-uccc
- Screening registries: NKCx (Nationellt Kvalitetsregister för Cervixcancerprevention, Karolinska Institutet, 100% national coverage, annual reports at nkcx.se); mammography and colorectal screening data via INCA/RCC. https://www.socialstyrelsen.se/contentassets/3a659c41107e40099b5d404ded89b50e/2020-6-6800-metodbilaga.pdf
- Submission format: A-report (clinician) and B-report (lab) via INCA forms, Socialstyrelsen form, or electronic lab diagnostic statements; RCC convert to ICD-O/3. https://www.socialstyrelsen.se/contentassets/6b4e25c21ce446f2a9d850ef43daa294/2026-5-10247.pdf
- Coding: ICD-O/3.2 (applied since 2019) with Socialstyrelsen modifications; TNM mandatory since 2004, UICC TNM versions 8 and 9 currently in use per 'Kodning i cancerregistret 2026' (verified 2026-11-19) https://www.socialstyrelsen.se/contentassets/6b4e25c21ce446f2a9d850ef43daa294/2026-5-10247.pdf ; ICD-10-SE. https://www.socialstyrelsen.se/contentassets/ad9a86523e93449097d5136a8989f561/2024-1-8918.pdf ; https://lagen.nu/sosfs/2006:15
- Legal basis: SOSFS 2006:15 (cancer notification regulation); Patientregistret rules from 2027 mandate ICD-10-SE. https://lagen.nu/sosfs/2006:15 ; https://socialstyrelsen.se/statistik-och-data/register/patientregistret/nya-foreskrifter-om-uppgiftsskyldighet-till-patientregistret/
- Researcher access: Socialstyrelsen register service for Cancerregistret; quality registers via RCC per-register application forms and steering-group approval; ethics approval from Etikprövningsmyndigheten; SKR quick guide. https://cancercentrum.se/syd/regional-cancer-centres/research-and-innovation/registry-research/ ; https://skr.se/kvalitetsregister/omnationellakvalitetsregister/qualityregistries/registrydatainresearch/quickguideforresearchers.54757.html

### (b) Public datasets
- Socialstyrelsen Statistikdatabas (cancer incidence) and "Cancerregistrets framställning och kvalitet". https://socialstyrelsen.se/statistik-och-data/register/cancerregistret/framstallning-och-kvalitet/
- NORDCAN 2.0 participant. https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- ECIS contributor (Swedish Cancer Registry). https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- RCC publishes quality register annual reports and SVF (standardised care pathway) indicators. https://cancercentrum.se/globalassets/vara-uppdrag/kunskapsstyrning/varje-dag-raknas/vardforlopp/redovisningar/2025/berakningsunderlag-for-andel-patienter-som-genomgatt-svf-version-9.0.pdf
- Research data access body: Socialstyrelsen and Statistics Sweden (SCB) for linked microdata; TEHDAS2 partners: E-hälsomyndigheten, Region Skåne, Karolinska Institutet, Region Stockholm, Vetenskapsrådet, Socialstyrelsen, Uppsala University. https://tehdas.eu/partners/
- Synthetic datasets: n/f. National health data catalogue: registerforskning.se (Vetenskapsrådet) n/f in this search.

### (c) Cancer infrastructure
- National cancer strategy: new national cancer strategy presented by government January 2026 (10–15 year horizon), following "Bättre tillsammans" consultation. https://www.regeringen.se/pressmeddelanden/2026/01/ny-nationell-cancerstrategi-ska-radda-liv-och-hoja-livskvaliteten/
- RCC i samverkan (six Regional Cancer Centres) as national coordination structure. https://cancercentrum.se/globalassets/om-rcc/samverkan/minnesanteckningar/2025/minnesanteckningar-rcc-i-samverkan-2025-01-21.pdf
- OECI: Karolinska CCC (first in Sweden, 2020; re-accredited May 2025); Skåne University Hospital Cancer Centre accredited CCC; Uppsala CCC accreditation 2024; Sahlgrenska CCC (hosted first Nordic-Baltic CCC network meeting, Feb 2023); Umeå/Northern Sweden in process. OECI accredited-centres list (2026-11-19) shows five Swedish entries: Karolinska Institute and University Hospital, Linköping CCC, Sahlgrenska University Hospital, Skåne University Hospital CCC, Uppsala University Hospital (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://www.karolinska.se/om-oss/centrala-nyheter/2025/05/karolinska-comprehensive-cancer-center-forst-i-sverige-med-fornyad-ackreditering/ ; https://vard.skane.se/en/skane-university-hospital/about-us/news/skane-university-hospital-cancer-centre-accredited-as-comprehensive-cancer-centre ; https://www.uu.se/en/staff/disciplinary-domain/medicine-and-pharmacy/news/archive/2024-10-15-accreditation-of-uppsala-comprehensive-cancer-centre ; https://www.sahlgrenska.se/om-sjukhuset/organisation/centrumbildningar/sccc/moten-och-konferenser/first-nordic-baltic-comprehensive-cancer-centers-network-meeting/ ; https://www.umu.se/en/news/northern-swedens-cancer-care-closer-to-international-quality-accreditation_12183076/
- Genomics: Genomic Medicine Sweden (GMS, since 2017, seven Genomic Medicine Centres); WGS/WTS standard for all children with cancer since May 2024; GMS–Hartwig partnership for adult WGS. https://publications.scilifelab.se/publication/bc1322ec034a40f2b805278a57b8c967 ; https://www.eppermed.eu/?p=7217 ; https://www.genomeweb.com/node/653996
- Genome of Europe: Sweden/SciLifeLab contributes (Vinnova co-funding, ≥1,000 long-read genomes). https://www.scilifelab.se/news/sweden-and-scilifelab-contribute-to-the-genome-of-europe/
- Biobank: Biobank Sverige = Swedish BBMRI-ERIC node (National Node Director Tobias Sjöblom); runs Svenska Biobanksregistret. https://biobanksverige.se/en/about-biobank-sweden/ ; https://dev2.bbmri-eric.eu/national-nodes/sweden/
- Imaging: EUCAIM partners Karolinska Institute, Linköping University, NBIS, Region Västerbotten, Umeå University, Vinnova; AIDA Data Hub. https://cancerimage.eu/partners/
- EU projects: ECHoS (Karolinska CCC, Zero Vision Cancer, SALAR, Stockholm School of Economics); EUCanScreen (Socialstyrelsen); TEHDAS2 (see above); EUnetCCC Swedish participants: Socialstyrelsen, SKR, Karolinska Institutet, Region Stockholm, Västra Götalandsregionen, Region Östergötland, Region Skåne, Region Uppsala (grant data sheet) (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf ; JANE-2 Swedish partner n/f. https://ki.se/en/cancerresearchki/a-new-european-consortium-funded-with-6-million-euros-will-create-a-network-of
- OMOP/EHDEN: EHDEN data partners MEB Karolinska Institutet, CREAtinine Measurements Project, SWIBREG, Gothenburg University; DARWIN EU Swedish partner: still n/f (EMA partner PDF blocks automated fetch; needs browser). https://www.ehden.eu/datapartners/
- National health data space: E-hälsomyndigheten leads; Sweden mandates FHIR for national services; VALO Nordic EHDS project. https://packages.fhir.org/jurisdictions/SE ; https://www.sitra.fi/en/projects/value-from-nordic-health-data-valo

### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: 1177 (Journalen); cancer-specific content n/f.
- INCA platform: openEHR data store (CDR) receiving forms via AQL from regional systems; IPÖ. https://svfp.se/media/biki5rbx/slutrapport_openehrv12.pdf
- openEHR oncology: Swedish pathology synoptic archetype work (building on Dutch PALGA); Karolinska "Symphony" prostate MDT dashboards on openEHR templates. https://discourse.openehr.org/t/refreshing-archetypes-related-to-pathology-reporting/2393 ; https://docs.google.com/presentation/d/1i6K_Ry6Q4CwlpeZFEjHQGguefTbRETm1/htmlpresent
- Structured pathology: Svensk förening för patologi (KVAST) publishes cancer reporting protocols (listed by SNOMED alongside CAP/ICCR). https://conf.spaces.snomed.org/wiki/spaces/CC/pages/131826462
- EHR: regional systems (Cosmic, Millennium in Skåne SDV); Skåne SDV antitumoral treatment coexistence guidance. https://vardgivare.skane.se/siteassets/support/sdv/samexistens/forlaga---antitumoral-behandling-under-samexistensperioden.pdf
- Chemotherapy: Omda Oncology (ex-Cytodose) used in Nordic hospitals (vendor claim: 40+ hospitals). https://intuitionlabs.ai/software/pdfs/omda-oncology.pdf
- Nationella informationsmängder (NIM) / national information model used for breast cancer modelling outside openEHR. https://discourse.openehr.org/t/refreshing-archetypes-related-to-pathology-reporting/2393
- MDT software: n/f national.
- Standardiserade vårdförlopp (SVF) indicator datasets. https://cancercentrum.se/globalassets/vara-uppdrag/kunskapsstyrning/varje-dag-raknas/vardforlopp/redovisningar/2025/berakningsunderlag-for-andel-patienter-som-genomgatt-svf-version-9.0.pdf

### Key organisations and people
- Socialstyrelsen (Cancerregistret, ICD-10-SE, SNOMED NRC), RCC i samverkan / INCA, E-hälsomyndigheten, Inera, Biobank Sverige, GMS, Karolinska CCC. People: Joakim Dillner (NKCx), Tobias Sjöblom (Biobank Sverige), Daniel Karlsson (E-hälsomyndigheten terminology), Mattias Colliander (HL7 Sweden).

---

## Norway

### (a) Cancer registries
- Population-based: Kreftregisteret (Cancer Registry of Norway), founded 1952, part of Folkehelseinstituttet since 1 Jan 2024; basic registry covers 98.6% of cancer patients 2019–2023. https://fhi.no/om/fhi/omrader/kreftregisteret ; https://www.fhi.no/en/cancer/clinical-registries/prostate-cancer-registry/Degree-of-coverage-and-data-quality
- ENCR/IACR: listed; ANCR member. https://catalogues.ema.europa.eu/node/1039/data-flows-and-management ; https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: Kreftregisteret operates 12 quality registries (8 with national status, 2022). https://www.fhi.no/kreft/statistikk/Opplysninger-i-databasen/ ; https://www.ntnu.no/ojs/index.php/norepid/article/view/4975
- Screening: three programmes (Mammografiprogrammet, Livmorhalsprogrammet, Tarmscreeningprogrammet), all run by Kreftregisteret. https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/diagnose-og-behandling/kreft/screeningprogram-for-kreft
- Legal basis: Kreftregisterforskriften; mandatory electronic reporting since 2017. https://www.fhi.no/kreft/innrapportering/innrapportering-kremt/
- Submission format: KREMT web portal or EHR-integrated messages per registry message specs; pathology as e-helse "Svar" v1.3/1.4 messages selected by NORPAT codes; radiotherapy data twice a year. https://www.fhi.no/contentassets/bb8d17623751483099eb6321111b868b/spesifikasjon---elektronisk-innsending-av-patologiremisser-1.pdf ; https://www.fhi.no/om/strategi-2026-2030/fhis-helsedatastrategi/
- Coding: ICD-O-3 registration codes converted to ICD-10 for reporting (Cancer in Norway 2025); NORPAT; TNM registration voluntary (UICC 5/6/7 in 2004–2016 study); current edition is UICC 8th, stated by Helsedirektoratet's handlingsprogram to match Kreftregisteret routines; registry stage derived from cTNM/pTNM (verified 2026-11-19) https://www.fhi.no/Content/cancer-in-norway-2025.pdf ; https://www.helsedirektoratet.no/retningslinjer/kreft-i-tykktarm-og-endetarm-handlingsprogram/patologi/uicc-tnm-klassifisering-og-stadieinndeling https://medicaljournalssweden.se/actaoncologica/article/download/24253/28421/74284
- Researcher access: Helsedataservice via helsedata.no single application form (since 2019); Kreftregisteret Data Delivery Unit; Janus serum bank. https://www.fhi.no/en/cancer/data-and-statistics/Datautlevering/ ; https://www.fhi.no/en/hd/access-to-data/applying-for-access-to-data/

### (b) Public datasets
- Statistikkbank (Kreftregisteret) and "Cancer in Norway" annual report. https://www.fhi.no/kreft/statistikk/data-og-statistikk/ ; https://develop.fhi.no/globalassets/cancer-in-norway/2023/cancer-in-norway-2023.pdf
- data.norge.no catalogue entry for Kreftregisteret. https://data.norge.no/datasets/caf3d50c-1d5c-3909-860b-0f491b24177b
- NORDCAN 2.0 participant; ECIS contributor. https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- Research access body: Helsedataservice (helsedata.no); TEHDAS2 partners Helsedirektoratet and FHI. https://tehdas.eu/partners/
- Synthetic datasets: n/f.

### (c) Cancer infrastructure
- National strategy: "Joint efforts against cancer 2025–2035" (Nasjonal kreftstrategi); goal that all patients have access to a CCC or cancer centre. https://www.regjeringen.no/en/documents/joint-efforts-against-cancer-20252035/id3087629/?ch=8
- OECI: Oslo University Hospital CCC accredited 2017, re-accredited 2023 (only accredited centre in Norway); Haukeland (Helse Bergen) in accreditation process 2024–2025; Ahus pursuing. OECI accredited-centres list (2026-11-19) shows two Norwegian entries: Haukeland University Hospital Bergen and Oslo University Hospital, so Haukeland is now accredited (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). EUnetCCC EU-Designated CCCs (first 30, 23 Feb 2026): St. Olav University Hospital and University Hospital of Northern Norway (UNN); EUnetCCC participants OUS, UNN, FHI, St Olavs, Helse Bergen (verified 2026-11-19) https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ ; https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf https://med.uio.no/klinmed/english/about/organization/divisions/cancer-medicine/comprehensive-cancer-centre ; https://www.helse-bergen.no/en/comprehensive-cancer-center-accreditation/ ; https://www.ahus.no/en/profession-and-research/research-and-innovation/Ahus-Cancer-Centre/oeci-accreditation/
- Precision medicine: InPreD national infrastructure (six university hospitals, two WGS hubs); IMPRESS-Norway trial; CONNECT consortium (Oslo Cancer Cluster); Helsedirektoratet coordinates national precision medicine strategy. https://pubmed.ncbi.nlm.nih.gov/35513529/ ; https://oslocancercluster.no/?p=16655
- 1+MG / Genome of Europe: Norway participates (about 6,700 genomes target; Helsedirektoratet page). https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/diagnose-og-behandling/persontilpasset-medisin/1-mg ; https://elixir.no/funding-and-projects/genome-of-europe
- Biobank: BBMRI.no (Director Kristian Hveem); Janus serum bank at Kreftregisteret. https://www.bbmri-eric.eu/national-nodes/norway/
- Imaging: EUCAIM partner Oslo Universitetssykehus HF. https://cancerimage.eu/partners/
- EU projects: ECHoS (Norwegian Cancer Society, Oslo Cancer Cluster, Research Council; national Cancer Mission Hub established); EUCanScreen (Helsedirektoratet, Kreftregisteret); JANE-2 (Oslo University Hospital); EOSC4Cancer (ELIXIR Norway). https://oslocancercluster.no/news/echos-gathers-europe-against-cancer ; https://elixir.no/funding-and-projects/eosc4cancer
- OMOP/EHDEN: EHDEN data partners Norwegian Cancer Registry and University of Oslo. https://www.ehden.eu/datapartners/
- National health data space: helsedata.no / Helsedataservice; FHI health data strategy 2024–2027. https://www.fhi.no/om/strategi-2026-2030/fhis-helsedatastrategi/

### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: helsenorge.no (national portal; cancer-specific content n/f).
- EHR: DIPS (most hospitals), Helseplattformen (Epic, Midt-Norge, contested). https://www.helseplattformen.no/om-oss/helseplattformen-one-common-regional-health-record/
- Exchange formats: e-helse "Svar" (XML) messages with AppRec; KREMT message specifications; HER-id addressing. https://www.fhi.no/contentassets/bb8d17623751483099eb6321111b868b/spesifikasjon---elektronisk-innsending-av-patologiremisser-1.pdf
- Structured pathology: NORPAT codes mandatory in all pathology departments; registry aims for structured templates in LIS. https://conf.spaces.snomed.org/wiki/spaces/PLT/pages/131829871 ; https://www.fhi.no/en/cancer/reporting/reporting-pathology-information/
- openEHR: Norwegian MDT work for prostate and kidney cancer using openEHR and SNOMED CT (2022 Nordic openEHR meeting). https://discourse.openehr.org/uploads/short-url/1zvfSCUCq01AbnjQXEb2CaIY1jk.pdf
- Chemotherapy: Omda Oncology/Cytodose developed at Norway's leading cancer centre, launched 2001. https://intuitionlabs.ai/software/pdfs/omda-oncology.pdf
- Medication: Pasientens legemiddelliste, SFM Datashare (FHIR) for prescriptions. https://utviklerportal.nhn.no/informasjonstjenester/sentral-forskrivningsmodul/sfm-full-integration/integrating-with-the-datashare-api
- ICD-11 transition strategy (draft 2026). https://www.helsedirektoratet.no/rapporter/oppgraderingsstrategi-for-icd-11-informasjonsforvaltning-kodeverk-og-terminologi/sammendrag

### Key organisations and people
- FHI/Kreftregisteret, Helsedirektoratet, Helsedataservice, OUS CCC, Oslo Cancer Cluster, InPreD/IMPRESS, BBMRI.no. People: Kristian Hveem (BBMRI.no); IMPRESS-Norway leads per Nat Med 2022 paper (Helland/Tasken et al.) https://pubmed.ncbi.nlm.nih.gov/35513529/

---

## Finland

### (a) Cancer registries
- Population-based: Finnish Cancer Registry (Suomen Syöpärekisteri), founded 1952/53, a THL statutory register maintained by the Cancer Society of Finland; statutory notification by all providers and labs. https://cancerregistry.fi/cancer-information-notification/
- Coverage: near-complete (Nordic overview); ENCR listed; ANCR member. https://medicaljournalssweden.se/actaoncologica/article/view/24912 ; https://catalogues.ema.europa.eu/network/2221158
- Screening registry: Mass Screening Registry (Joukkotarkastusrekisteri) within FCR; three statutory programmes (cervical, breast, colorectal since 2022). https://www.finngen.fi/sites/default/files/inline-files/FinnGen%20data%20protection%20statement%20April%202026.pdf ; https://www.news-medical.net/news/20240117/Study-shows-promise-of-gene-based-screening-to-fight-colorectal-cancer.aspx
- Clinical quality registries: national cancer quality register project (Cancer Society, THL, FICAN) funded; permanent status pending. https://www.sttinfo.fi/tiedote/72255408/puutteita-syovanhoidossa-ei-voida-korjata-ilman-rahoitusta?lang=fi
- Submission format: electronic transfers from hospitals/labs plus manual forms (older sources); current spec still n/f (cancerregistry.fi pages require a browser). https://medicaljournalssweden.se/actaoncologica/article/download/26654/31366/79205
- Coding: ICD-O-3 topography/morphology/behaviour, stage, ICD-10 for statistics; TNM edition still n/f; stage (levinneisyys) information available for 42% of 2024 cases nationally, target 70% (Syöpä 2024 report) (verified 2026-11-19) https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ https://finngen.gitbook.io/finngen-handbook/finngen-data-specifics/red-library-data-individual-level-data/what-phenotype-files-are-available-in-sandbox-1/other-registers/finnish-cancer-registry-detailed-cancer-data
- Legal basis: Act on THL / Act on Secondary Use of Health and Social Data (552/2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC10396416
- Researcher access: Findata (data permit authority) under the Secondary Use Act; FinnGen access via Findata and FINBB Fingenious. https://www.finngen.fi/en/node/1995

### (b) Public datasets
- cancerregistry.fi statistics (incidence, survival, screening) and annual report. https://cancerregistry.fi/
- NORDCAN 2.0 participant; ECIS contributor. https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- FinnGen public summary releases; FinRegistry. https://www.finngen.fi/en/public-data-releases
- Research access body: Findata; TEHDAS2 partners Sitra (coordinator), CSC, Findata, THL, HUS, VTT. https://tehdas.eu/partners/
- Synthetic datasets: n/f.

### (c) Cancer infrastructure
- National cancer strategy "Yhdessä syöpää vastaan" 2026–2035 (published autumn 2025); roadmap due 2026. https://valtioneuvosto.fi/-/1271139/yhteinen-suunta-ihmislahtoiseen-ja-vaikuttavaan-syovan-ehkaisyyn-ja-hoitoon-kansallinen-syopastrategia-on-julkaistu
- FICAN (national cancer centre, 2019; five regional centres; represents Finland in OECI). https://stm.fi/en/personalized-medicine/national-cancer-center
- OECI: HUS CCC accredited twice (first Nordic CCC); Tays Cancer Centre renewed; all five regional centres OECI members. OECI accredited-centres list (2026-11-19) shows four Finnish entries: Helsinki University Hospital CCC, TAYS Tampere, Turku University Hospital Cancer Centre, Kuopio University Hospital Cancer Center (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://www.hus.fi/en/newsroom/hus-comprehensive-cancer-centre-designated-top-level-european-cancer-hospital-second-time ; https://www.tuni.fi/en/news/tays-cancer-centre-meets-rigorous-european-quality-standards
- Genomics: FinnGen (public-private, >500k participants; cancer registry linkage); Genome Center: the genome act (genomilaki) was removed from the government's legislative programme and the Genomikeskus has not been established (verified 2026-11-19) https://stm.fi/-/genomilain-antaminen-siirtyy-eteenpain-genomikeskuksen-valmistelu-jatkuu https://www.finngen.fi/en/node/2635
- Biobank: FINBB (Finnish Biobank Cooperative) = BBMRI.fi; Fingenious portal. https://www.finngen.fi/en/node/1995
- Imaging: EUCAIM partners Euro-BioImaging ERIC, Wellbeing Services County of North Savo. https://cancerimage.eu/partners/
- EU projects: ECHoS (Cancer Society of Finland, HUS); EUCanScreen (THL, Cancer Society); TEHDAS2 coordinator Sitra; EUnetCCC participant HUS-yhtymä (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf https://ki.se/en/cancerresearchki/a-new-european-consortium-funded-with-6-million-euros-will-create-a-network-of
- OMOP/EHDEN: FinOMOP consortium (THL) onboarded in DARWIN EU; EHDEN partners Pirkanmaa Hospital District, BCB Medical, Hospital District of Southwest Finland, Prostate Cancer Registry of South West Finland, THL, FinRegistry, HUS. https://www.ehden.eu/datapartners/ ; https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: Findata as HDAB; Kanta. https://www.sitra.fi/en/projects/value-from-nordic-health-data-valo

### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: OmaKanta (national); oncology-specific content n/f.
- Kanta: CDA R2 documents for patient records; FHIR only for new content. https://www.kanta.fi/en/fhir-technology-and-kanta
- Koodistopalvelu (national code server, SOAP/XML retired Jan 2026). https://www.kanta.fi/documents/d/guest/koodistopalvelun-rajapinnat-ja-liittymisohje-1_8
- Structured pathology: THL "patologian tietosisältöjen yhtenäistäminen" work. https://www.slideshare.net/THLfi/patologian-tietosisltjen-yhtenistminen-suomessa
- EHR: Apotti (Epic, HUS area), Esko, others; chemo systems n/f.
- MDT software, openEHR oncology: n/f.
- THL-coordinated guide on follow-up of access to cancer care (16 cancer types). https://www.sttinfo.fi/files/69820264/70275300/98389/fi

### Key organisations and people
- THL, Kela/Kanta, Findata, Finnish Cancer Registry / Cancer Society of Finland, FICAN, HUS CCC, FINBB, FinnGen, Sitra. People: Janne Pitkäniemi (Director, Finnish Cancer Registry, Syöpä 2024 report (verified 2026-11-19) https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ ) https://www.sttinfo.fi/files/69820264/70275300/98389/fi ; Mikael Rinnetmäki (HL7 Finland).

---

## Iceland

### (a) Cancer registries
- Population-based: Icelandic Cancer Registry (Krabbameinsskrá), founded 1954, operated by the Icelandic Cancer Society research centre on behalf of the Directorate of Health (Act 41/2007); covers >99% of cancers; registration since 1955. https://www.krabb.is/rannsoknasetur/en/activities/about-icr/ ; https://www.laeknabladid.is/media/2024-06/f02.pdf
- ENCR/IACR: ANCR member; ENCR registry page still n/f (ENCR list is script-rendered; needs browser). https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: cancer quality registration started 1998 with prostate cancer and was expanded in 2010 (Læknablaðið) (verified 2026-11-19) https://www.laeknabladid.is/media/2020-09/u09.pdf
- Screening: Samhæfingarstöð krabbameinsskimana (Cancer Screening Coordination Centre, Heilsugæsla höfuðborgarsvæðisins) runs breast, cervical and (from Feb 2025) colorectal screening; results via Heilsuvera. https://island.is/s/hh/samhaefingarstod-krabbameinsskimana ; https://island.is/s/hh/frett/langthradur-afangi-ad-hefja-skimun-fyrir-ristilkrabbameini-28-02-2025
- Submission format: most reports arrive electronically from pathology laboratories; coverage over 99% of diagnoses (Læknablaðið 2024) (verified 2026-11-19) https://www.laeknabladid.is/media/2024-06/f02.pdf ; private clinicians report only prostate cancers. https://medicaljournalssweden.se/actaoncologica/article/view/24912
- Coding: ICD-O rules per registry (edition number not stated), IARC/ENCR rules, ICD-10 for publication (verified 2026-11-19) https://www.laeknabladid.is/media/2024-06/f02.pdf ; TNM still n/f. https://medicaljournalssweden.se/actaoncologica/article/view/24912
- Researcher access: application form plus ethics-approved research plan to the Cancer Registry; family database requires National Bioethics Committee permission; >600 studies. https://www.krabb.is/rannsoknasetur/en/activities/about-icr/

### (b) Public datasets
- NORDCAN 2.0 participant (Iceland included). https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- Cancer Society publishes five-year average statistics. https://www.krabb.is/rannsoknasetur/en/activities/about-icr/
- ECIS contributor: n/f.
- Research access body (EHDS): Directorate of Health (TEHDAS2 partner). https://tehdas.eu/partners/
- Synthetic datasets, national catalogue: n/f.

### (c) Cancer infrastructure
- National plan: government cancer action plan approved by parliament June 2025 (16 measures); Cancer Council established. https://island.is/en/news/new-cancer-council
- Landspítali Cancer Center established 2025; standardised care pathways; accreditation preparation. https://island.is/en/o/landspitali/landspitali-cancer-center ; https://island.is/en/o/landspitali/landspitali-cancer-center/standardized-cancer-care-pathways
- OECI: Landspítali Cancer Center (2025) states it operates per OECI standards and prepares accreditation; no Icelandic centre on the OECI accredited-centres list (2026-11-19) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt); membership still n/f https://island.is/en/o/landspitali/landspitali-cancer-center
- Genomics: deCODE genetics (>2/3 of adults participating by 2019); Iceland is not a 1+MG signatory and has no Genome of Europe partner (absent from partner list) (verified 2026-11-19) https://genomeofeurope.eu/partners/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7115898 https://www.decode.com/?p=2007
- Biobank: Iceland is neither BBMRI-ERIC member nor observer (2025 annual report); Landspítali runs licensed biobanks (LLR, LLSV) (verified 2026-11-19) https://www.bbmri-eric.eu/annual_report_2025_singlepages/ ; https://island.is/en/o/landspitali/biobanks-of-landspitali
- Imaging: EUCAIM n/f.
- EU projects: EUCanScreen (Heilsugæsla höfuðborgarsvæðisins); TEHDAS2 (Directorate of Health); EUnetCCC participant Landspítali University Hospital (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf ; ECHoS still n/f. https://island.is/en/o/hh/eu-can-screen ; https://tehdas.eu/partners/
- OMOP/EHDEN: n/f.
- National health data space: Stafræn heilsa (from Jan 2026) as development and service centre; draft Digital Health Act (consultation Aug 2026). https://island.is/s/stafraen-heilsa/frett/droeg-ad-frumvarpi-um-stafraena-heilsu-til-umsagnar

### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: Heilsuvera (screening invitations and results; cancer plan calls for interactive symptom-monitoring portal). https://island.is/s/hh/frett/bod-og-nidurstodur-vegna-krabbameinsskimana-a-heilsuveru-14-03-2025 ; https://island.is/en/o/sak/news/rafraen-samskiptagatt-styrkir-thjonustu-vid-sjuklinga-i-veikindum
- EHR: Saga (Origo/Helix) nationwide; Hekla health network; prescription gateway. https://island.is/s/stafraen-heilsa/innvidir-og-kerfi
- Classification distribution: SKAFL.is (ICD-10, NCSP). https://island.is/flokkunarkerfi-i-heilbrigdisthjonustu/skafl.is
- Structured pathology: SNOMED used in pathology registration. https://island.is/en/classification-system-in-health-services
- MDT software, chemotherapy system, openEHR: n/f.

### Key organisations and people
- Embætti landlæknis, Stafræn heilsa (Sigurður Þórarinsson), Krabbameinsfélagið (Sigríður Gunnarsdóttir, head of Rannsóknasetur – Krabbameinsskrá per 2025 annual report; Laufey Tryggvadóttir, epidemiologist) (verified 2026-11-19) https://www.krabb.is/media/arsskyrsla-krabbameinsfelagsins-2025.pdf , Landspítali Cancer Center, Heilsugæsla höfuðborgarsvæðisins, deCODE (Kári Stefánsson). https://island.is/s/stafraen-heilsa/frett/sigurdur-thorarinsson-skipadur-forstoedumadur-stafraennar-heilsu

---

## Estonia

### (a) Cancer registries
- Population-based: Estonian Cancer Registry (vähiregister), controller Tervise Arengu Instituut (TAI); compulsory reporting by physicians and labs; ICD-O-3 since 2008; linkage with Population and Causes of Death registries. https://en.tai.ee/en/r-and-d/registers/estonian-cancer-registry ; https://www.riigiteataja.ee/akt/123052023056.pdf
- ENCR: Estonian registry follows ENCR recommendations; coverage percent n/f, but the 2026 mid-term evaluation reports that about 20% of cancer cases reach the registry with incomplete data (verified 2026-11-19) https://www.sm.ee/sites/default/files/documents/2026-04/Eesti%20V%C3%A4hit%C3%B5rje%20tegevuskava%202021%E2%80%932030%20vahehindamine_L%C3%95PPRAPORT_0.pdf https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Screening registry: Estonian Cancer Screening Registry (TAI, since 2015; breast, cervical, colorectal) fed automatically from ENHIS via X-Road. https://en.tai.ee/en/r-and-d/registers/estonian-cancer-screening-registry
- Clinical quality registries: n/f; cancer data dashboard (VJL) project at Tartu. https://sisu.ut.ee/estcan/cancer-data-dashboard/
- Submission format: paper, electronic or X-Road; 30-day deadline in 2025 draft regulation; TAI notification guide. https://en.tai.ee/images/Teatise_vormistamise_juhend.pdf
- Coding: RHK-O-3 (ICD-O-3) topography and morphology; notification guide requires stage with TNM values per the 8th edition (pTNM, else cTNM); ICD-10 for publication (verified 2026-11-19) https://tai.ee/sites/default/files/2021-03/Teatise_vormistamise_juhend.pdf https://medicaljournalssweden.se/actaoncologica/article/download/24331/28536/74545
- Legal basis: Public Health Act; Vähiregistri põhimäärus. https://www.riigiteataja.ee/akt/123052023056.pdf
- Researcher access: TAI register data requests; national secondary-use governance model still being defined (Ministry of Social Affairs); secondary use needs no consent except biobank. https://tehdas.eu/app/uploads/2023/03/estonia-country-visit-factsheets-10-2022.pdf

### (b) Public datasets
- TAI Health Statistics and Health Research Database (cancer incidence PK tables, screening VSR tables). https://statistika.tai.ee/pxweb/en/Andmebaas/Andmebaas__02Haigestumus__04PahaloomulisedKasvajad/PK10.px/ ; https://statistika.tai.ee/Resources/PX/Databases/Andmebaas/02Haigestumus/07Soeluuringud/VSRinfo_en.htm
- ECIS contributor. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- NORDCAN: not a participant.
- Research access body: TEHIK/Ministry of Social Affairs (TEHDAS2 partner). https://tehdas.eu/partners/
- Synthetic datasets: n/f.

### (c) Cancer infrastructure
- Cancer Control Action Plan 2021–2030 (15 themes incl. cancer data); mid-term evaluation April 2026 found 45% of actions not started. https://www.sm.ee/sites/default/files/documents/2026-04/Eesti%20V%C3%A4hit%C3%B5rje%20tegevuskava%202021%E2%80%932030%20vahehindamine_L%C3%95PPRAPORT_0.pdf
- Estonian Cancer Centre / ESTCAN network at University of Tartu; aims at EU CCC recognition. https://sciencebusiness.net/network-updates/university-tartu-will-be-home-estonian-cancer-centre ; https://sisu.ut.ee/estcan/
- OECI: East Tallinn Central Hospital holds full OECI membership; Tartu University Hospital appears on the OECI accredited-centres list (2026-11-19), the only Estonian entry (accreditation level not shown in the saved list) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). Earlier statement that no Estonian centre is accredited is withdrawn. https://www.itk.ee/en/news/east-tallinn-central-hospital-gains-full-oeci-membership ; https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: Estonian Biobank (>200,000 participants, Human Genes Research Act 2000; auto-updated from Cancer Registry); PacBio WGS of 10,000. https://ut.ee/en/content/estonian-researchers-strive-personalise-healthcare ; https://www.digitalhealth.net/2024/04/estonian-biobank-selects-pacbio-for-whole-genome-sequencing
- Biobank: University of Tartu Institute of Genomics = BBMRI-ERIC national node. https://genomics.ut.ee/en/cooperation-networks
- Imaging: EUCAIM partner Better Medicine OÜ. https://cancerimage.eu/partners/
- EU projects: EUnetCCC (ESTCAN, North Estonia Medical Centre, Tartu University Hospital, TAI); UNCAN-Connect coordinated by University of Tartu (2025–2030); EUCanScreen (TAI, University of Tartu); TEHDAS2 (Ministry of Social Affairs). https://sisu.ut.ee/estcan/eunet-ccc/ ; https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/ ; https://www.unicancer.fr/en/unicancer-group/international-partners/
- OMOP/EHDEN: EHDEN data partner University of Tartu. https://www.ehden.eu/datapartners/
- National health data space: TEHIK; EHDS integration into existing ENHIS. https://tehdas.eu/app/uploads/2023/03/estonia-country-visit-factsheets-10-2022.pdf

### (d) Digital, non-FHIR, cancer-relevant
- ENHIS/TIS national EHR with CDA and HL7 v3 documents still in use alongside FHIR. https://packages.fhir.org/jurisdictions/EE
- Patient portal: terviseportaal.ee (Patsiendiportaal); oncology-specific content n/f.
- Cancer data dashboard (VJL) and lung cancer treatment pathway pilot (Tartu). https://www.sm.ee/sites/default/files/documents/2026-04/Eesti%20V%C3%A4hit%C3%B5rje%20tegevuskava%202021%E2%80%932030%20vahehindamine_L%C3%95PPRAPORT_0.pdf
- Structured pathology: standardised pathology report templates based on ICCR and CAP, updated to TNM 9, being rolled out (2026 mid-term evaluation) (verified 2026-11-19) https://www.sm.ee/sites/default/files/documents/2026-04/Eesti%20V%C3%A4hit%C3%B5rje%20tegevuskava%202021%E2%80%932030%20vahehindamine_L%C3%95PPRAPORT_0.pdf ; MDT software, chemotherapy system, openEHR: n/f.
- Terminology server endpoint https://term.tehik.ee/fhir (verified 2026-11-19).
- CDA-to-FHIR migration research (infectious disease system) as template. https://ws.lib.ttu.ee/digibase/en/Publ/Register/Item/337803

### Key organisations and people
- TEHIK, TAI (Cancer Registry, Screening Registry), Ministry of Social Affairs, University of Tartu (ESTCAN, Institute of Genomics, UNCAN-Connect), Tartu University Hospital, North Estonia Medical Centre. People: Igor Bossenko (TalTech, FHIR migration research); registry leads n/f.

---

## Latvia

### (a) Cancer registries
- Population-based: cancer data within "Ar noteiktām slimībām slimojošu pacientu reģistrs" (Register of patients with particular diseases) at SPKC since 2009; new digital population-based cancer register under development. https://statistika.spkc.gov.lv/Resources/PX/Databases/Health/Metadati/ONKO_Registra_metadati_en.html ; https://www.intechopen.com/online-first/1204840
- ENCR: Latvian registry presented at ENCR conference; data quality issues 2006–2009; ENCR membership page still n/f (list script-rendered; needs browser). https://www.encr.eu/sites/default/files/2018-ENCR-Conference/Kojalo_LV%20cancer%20registry%20quality.%20Some%20examples.pdf
- Screening: state-funded cervical, breast, colorectal, prostate screening (Cabinet Reg. 555/2018); SPKC oversees since 2023 and calls for a screening registry; colorectal screening metadata on SPKC stats. https://www.vmnvd.gov.lv/en/node/3011 ; https://www.spkc.gov.lv/lv/jaunums/baltic-congress-laboratory-medicine-centre-disease-prevention-and-control-latvia-presented-progress-implementation-organized-cancer-screening-latvia
- Clinical quality registries: n/f.
- Submission format: cancer patient card mandatory in e-veselība since 1 Jan 2024; NVD monthly non-personalised transfers to SPKC; manual collection reported 2024. https://vmnvd.gov.lv/lv/media/28572/download ; https://www.lsm.lv/raksts/zinas/latvija/20.08.2024-veza-registrs-vel-nepabeigts-un-nepilnigs.a565719/
- Coding: SSK-10 (ICD-10) C00–C97; cancer patient card uses SSK-O-3.2 topography/morphology and TNM 8th edition, with ICCC and TNM 8 added to the data-entry algorithm by 1 January 2024 (verified 2026-11-19) https://www.spkc.gov.lv/lv/media/19929/download ; https://spkc.gov.lv/lv/media/19977/download
- Legal basis: Cabinet Regulation No. 134 (e-veselība); register regulation. https://likumi.lv/ta/id/264943
- Researcher access: no clear legal procedure for inter-institutional data exchange for research (older study); SPKC data requests. https://pmc.ncbi.nlm.nih.gov/articles/PMC6979557

### (b) Public datasets
- SPKC statistics database ONKO tables (incidence, stage, 5-year survival). https://statistika.spkc.gov.lv/pxweb/en/Health/Health__Saslimstiba_Slimibu_Izplatiba__Onkologija/ONKO030.px
- ECIS contributor: Latvian registry listed in ECIS. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Research access body: SPKC and Latvian Biomedical Research and Study Centre (TEHDAS2 partners). https://tehdas.eu/partners/
- Synthetic datasets, national catalogue: n/f.

### (c) Cancer infrastructure
- Oncology care improvement plan 2025–2027 (government order 22 Oct 2025); fourth comprehensive plan. https://www.likumi.lv/ta/id/363895 ; https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-lv-2024-1675-en.pdf
- OECI: Riga East University Hospital Latvian Cancer Centre accredited, certificate valid to 26 Aug 2031 (first in Latvia); confirmed as the only Latvian entry on the OECI accredited-centres list (2026-11-19) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://www.researchlatvia.gov.lv/en/latvian-cancer-centre-joins-ranks-recognised-european-centres
- Genomics: Latvian Genome Database (LGDB, BMC, ~31,500 participants). https://pubmed.ncbi.nlm.nih.gov/29576601/
- Biobank: BMC = BBMRI-ERIC national node (Jānis Kloviņš); Biobank Law in parliament 2025. https://www.bbmri-eric.eu/national-nodes/latvia/ ; https://www.researchlatvia.gov.lv/en/looking-back-2025-key-highlights-latvian-biobank-network-bbmri-latvia
- Imaging: EUCAIM partner University of Latvia. https://cancerimage.eu/partners/
- EU projects: EUCanScreen coordinated by University of Latvia; ECHoS (Riga East hospital, Latvian Council of Science); JANE-2 (RSU); TEHDAS2 (SPKC, BMC); EUnetCCC participants University of Latvia, RSU and two hospital entities (names truncated in grant sheet) (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf . Latvia is not among the first 30 EU-Designated CCCs (Feb 2026; eight countries, Latvia not included) https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ . Pauls Stradiņš hospital cancer centre passed an OECI audit in 2026 https://lvportals.lv/dienaskartiba/392169-stradina-slimnicas-veza-centrs-veiksmigi-aizvadijis-oeci-auditu-un-turpina-virzibu-uz-starptautisku-akreditaciju-2026 https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/
- OMOP/EHDEN: n/f.
- National health data space: LDVC architecture and guidelines 2025; strategy names FHIR, SNOMED CT, LOINC, UCUM. https://www.varam.gov.lv/lv/media/46103/download

### (d) Digital, non-FHIR, cancer-relevant
- e-veselība (NVD): CDA-based documents (discharge summary NVD.EVK.CDA.3.09); cancer patient card; patient portal eveseliba.gov.lv. https://www.vmnvd.gov.lv/en/e-veseliba
- Structured pathology, MDT software, chemotherapy, openEHR: n/f.
- Survey cites "oncology registry" as FHIR use case (no spec). https://packages.fhir.org/jurisdictions/LV

### Key organisations and people
- Ministry of Health, SPKC, NVD, LDVC, Riga East University Hospital (Latvian Cancer Centre), University of Latvia (EUCanScreen), BMC (Jānis Kloviņš). Registry leads: n/f.

---

## Lithuania

### (a) Cancer registries
- Population-based: Lithuanian Cancer Registry at Nacionalinis vėžio institutas (NVI); ENCR-listed; modernised registry with open data portal (Dec 2025); fully electronic registration per NVI 2025 report. https://encr.eu/node/262 ; https://ground.news/article/since-1978-67-million-cancer-cases-in-lithuania-new-tool-for-disease-control-introduced ; https://nvi.lt/wp-content/uploads/2026/04/2-priedas.-NVI_Ataskaita_2025_26-02-26.pdf
- Source document: form Nr. 090/a (first-diagnosis notice). https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
- Screening: ESPBI subsystem for prevention programmes (breast, cervical, colorectal, prostate) built 2023–2025 (Kaunas Clinics project). https://kaunoklinikos.lt/media/file/Prevencini%C5%B3%20program%C5%B3%20vykdymo,%20kokyb%C4%97s%20u%C5%BEtikrinimo%20ir%20kokyb%C4%97s%20kontrol%C4%97s%20ESPBI%20IS%20posistem%C4%97s%20k%C5%ABrimas.pdf
- Clinical quality registries: n/f.
- Coding: ICD-O-3 topography/morphology; TLK-10-AM diagnoses; TNM edition still n/f (no Lithuanian registry coding manual located). https://www.nvi.lt/uploads/pdf/Vezio%20registras/Vezys_lietuvoje_2012.pdf
- Legal basis: mandatory statistical form 090/a (Ministry of Health order). https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
- Researcher access: procedure n/f; State Data Agency's Lithuanian Digital Health Platform onboarded in DARWIN EU. https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf

### (b) Public datasets
- NVI "Vėžys Lietuvoje" annual reports; new open data portal. https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202017.pdf
- ECIS contributor; CancerWatch project participation (Ministry of Health, NVI). https://sam.lrv.lt/en/during-the-visit-to-japan-the-focus-was-on-patient-safety/to-improve-cancer-data-quality-and-strengthen-cancer-control-europe-is-beginning-to-implement-the-cancerwatch-program-Y3mw
- IHE Cancer Dashboard Lithuania (2025). https://ihe.se/app/uploads/2025/01/IHE-Cancer-Dashboard-Lithuania_.pdf
- Research access body: Valstybės duomenų agentūra (TEHDAS2 partner, DARWIN EU). https://tehdas.eu/partners/
- Synthetic datasets: n/f.

### (c) Cancer infrastructure
- National Cancer Prevention and Control Programme 2014–2025; successor in development. https://ihe.se/app/uploads/2025/01/IHE-Cancer-Dashboard-Lithuania_.pdf ; https://www.iccp-portal.org/sites/default/files/plans/LTU_2020.pdf
- OECI: NVI accredited Clinical Cancer Centre since 2013; NVI and VU Santaros Klinikos seeking joint CCC accreditation. OECI accredited-centres list (2026-11-19) carries a 'National Cancer Institute' entry without country, consistent with NVI Vilnius (no other Lithuanian entry) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). EUnetCCC EU-Designated CCCs (first 30, 23 Feb 2026): Klaipėda University Hospital, Vilnius University Hospital Santaros Clinics with National Cancer Centre, and LSMU Kaunas Clinics (verified 2026-11-19) https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ https://www.vu.lt/en/news-events/news/vu-santaros-klinikos-and-the-national-cancer-institute-will-cooperate-in-the-treatment-of-oncological-diseases-and-the-development-of-oncology-science-the-aim-is-to-become-a-centre-for-comprehensive-cancer-care
- Genomics: 1+MG participation via Santaros Klinikos biobank; €7.6M for GDI 2023–2026. https://oecd.ai/en/dashboards/policy-initiatives/1-million-genomes-vilnius-university-hospital-vul-santaros-klinikos
- Biobank: BBMRI-ERIC full member 2024; national node via NVI; Santaros, LSMU/Kaunas biobanks. https://www.bbmri-eric.eu/national-nodes/lithuania/ ; https://nvi.lt/biobank-projects
- Imaging: EUCAIM n/f.
- EU projects: ECHoS (LSMU Kaunas Clinics, PI); JANE-2 (Vilnius University Hospital Santaros Klinikos); EUCanScreen (Ministry of Health, Vilnius and Kaunas hospitals); TEHDAS2 (State Data Agency). https://lsmu.lt/en/research-and-innovations/projects/international-projects/establishing-of-cancer-mission-hubs-networks-and-synergies/
- OMOP/EHDEN: DARWIN EU partner Lithuanian Digital Health Platform (State Data Agency). https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: State Data Agency platform; openEHR pilot for health information systems. https://discourse.openehr.org/uploads/short-url/3r2W1AWAHYxZ2AnvTJyCdLuq2Zw.docx

### (d) Digital, non-FHIR, cancer-relevant
- ESPBI IS (Registrų centras): DSTU1 Atom feeds (SKL01–03), patient portal esveikata.lt and mobile app; prevention-programme subsystem. https://www.esveikata.lt/en/en/ehealth ; https://esveikata.lt/bylos/failai/Mobilioji%20program%C4%97l%C4%97/Esveikatos%20naudojo%20vadovas-v1.1.pdf
- openEHR: national openEHR pilot/tender for health information systems. https://discourse.openehr.org/uploads/short-url/3r2W1AWAHYxZ2AnvTJyCdLuq2Zw.docx
- TLK-10-AM classification; TLK-11 mapping planned. https://e-seimas.lrs.lt/rs/legalact/TAD/e1ba28a055e911f0a19dcea0bcc863ad/
- Structured pathology: LT Lab IG pathology profiles (ICD-O-3, pTNM) are FHIR; non-FHIR pathology standard n/f.
- MDT software, chemotherapy system: n/f.

### Key organisations and people
- NVI (cancer registry, biobank node), Ministry of Health, Registrų centras (ESPBI), Valstybės duomenų agentūra, VU Santaros Klinikos, LSMU Kaunas Clinics, Lithuanian Medical Library (SNOMED NRC, HL7 IGs). People: Giedrė Smailytė (Director, Lithuanian Cancer Registry, ENCR page) (verified 2026-11-19) https://encr.eu/node/262 ; Laima Ambrozaitytė (Genome of Europe contact, Santaros) https://genomeofeurope.eu/partners/ .
