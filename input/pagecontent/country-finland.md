### Finland (FI)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "Finnish Base Profiles", package `hl7.fhir.fi.base` (also `.r4`/`.r4b`), v2.0.0 STU 2, FHIR R4, active 2025-10-05, official HL7 Finland standard (OID 1.2.246.777.11.2025.4), publisher HL7 Finland, canonical https://hl7.fi/fhir/finnish-base-profiles; no must-support; no R5 plan.
   https://hl7.fi/fhir/finnish-base-profiles/ ; https://get-ig.org/hl7.fhir.fi.base/2.0.0
2. **Oncology FHIR specifications:** not found. Kanta FHIR profiles (PHR, medication list) on Simplifier; no oncology profile set.
   https://www.kanta.fi/en/fhir-technology-and-kanta
3. **Cancer registry reporting:** Finnish Cancer Registry is THL's register maintained by the Cancer Society of Finland; statutory notification of every case or strong suspicion by hospitals, physicians and pathology, cytology and haematology laboratories. Current transmission format: not found (older literature: electronic transfers from large hospitals and labs plus manual forms). Variables include ICD-O-3 topography, morphology, behaviour, stage.
   https://cancerregistry.fi/cancer-information-notification/ ; https://finngen.gitbook.io/finngen-handbook/finngen-data-specifics/red-library-data-individual-level-data/what-phenotype-files-are-available-in-sandbox-1/other-registers/finnish-cancer-registry-detailed-cancer-data
4. **Terminologies:** SNOMED CT member 2018 (THL, 36th member); Finnish edition published each December (SNOMED International Finland page, updated June 2024, gives no year; edition module id 11000229106 per Finnish Base Profiles expansion parameters; exact latest release date still not found); subset translation only. https://hl7.fi/fhir/finnish-base-profiles/2.0.0/Parameters-exp-params.json.html ICD-10: THL Tautiluokitus ICD-10 on the national code server (version not found); ICD-11 planned from 2028. National code server (Koodistopalvelu, content THL, operations Kela; SOAP/XML retired 13.1.2026 with v9.2), not available in FHIR. LOINC, ATC: not found. ICD-O-3 variables (topography, morphology, behaviour) confirmed in the registry data description; TNM edition still not found, and the registry reported stage information available for only 42% of 2024 cases (verified 2026-11-19) https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ . National FHIR terminology server: not yet available, in planning.
   https://www.snomed.org/members/finland ; https://conf.spaces.snomed.org/wiki/spaces/MCC/pages/131343642/Finland ; https://hl7.fi/fhir/finnish-base-profiles/terminology.html ; https://www.kanta.fi/documents/d/guest/koodistopalvelun-rajapinnat-ja-liittymisohje-1_8 ; https://packages.fhir.org/jurisdictions/FI
5. **Organisations and people:** HL7 Finland (technical committee), THL, Kela/Kanta, Cancer Society of Finland. Mikael Rinnetmäki (contact on fi.base IG, mikael@sensotrend.com); Janne Pitkäniemi (Director, Finnish Cancer Registry, Syöpä 2024 report) (verified 2026-11-19) https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ .
   https://hl7.fi/fhir/finnish-base-profiles/ImplementationGuide-hl7.fhir.fi.base.json

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Finnish Cancer Registry (Suomen Syöpärekisteri), founded 1952/53, a THL statutory register maintained by the Cancer Society of Finland; statutory notification by all providers and labs. https://cancerregistry.fi/cancer-information-notification/
- Coverage: near-complete (Nordic overview); ANCR member. https://medicaljournalssweden.se/actaoncologica/article/view/24912 ; https://catalogues.ema.europa.eu/network/2221158
- ENCR member registries: Finnish Cancer Registry (director Dr. Janne Pitkäniemi). Source: https://www.encr.eu/encr-members-contact-list (read 2026-11-19) (verified 2026-11-19)
- Screening registry: Mass Screening Registry (Joukkotarkastusrekisteri) within FCR; three statutory programmes (cervical, breast, colorectal since 2022). https://www.finngen.fi/sites/default/files/inline-files/FinnGen%20data%20protection%20statement%20April%202026.pdf ; https://www.news-medical.net/news/20240117/Study-shows-promise-of-gene-based-screening-to-fight-colorectal-cancer.aspx
- Clinical quality registries: national cancer quality register project (Cancer Society, THL, FICAN) funded; permanent status pending. https://www.sttinfo.fi/tiedote/72255408/puutteita-syovanhoidossa-ei-voida-korjata-ilman-rahoitusta?lang=fi
- Submission format: electronic transfers from hospitals/labs plus manual forms (older sources); current spec still n/f (cancerregistry.fi pages require a browser). https://medicaljournalssweden.se/actaoncologica/article/download/26654/31366/79205
- Coding: ICD-O-3 topography/morphology/behaviour, stage, ICD-10 for statistics; TNM edition still n/f; stage (levinneisyys) information available for 42% of 2024 cases nationally, target 70% (Syöpä 2024 report) (verified 2026-11-19) https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ https://finngen.gitbook.io/finngen-handbook/finngen-data-specifics/red-library-data-individual-level-data/what-phenotype-files-are-available-in-sandbox-1/other-registers/finnish-cancer-registry-detailed-cancer-data
- Legal basis: Act on THL / Act on Secondary Use of Health and Social Data (552/2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC10396416
- Researcher access: Findata (data permit authority) under the Secondary Use Act; FinnGen access via Findata and FINBB Fingenious. https://www.finngen.fi/en/node/1995

#### (b) Public datasets
- cancerregistry.fi statistics (incidence, survival, screening) and annual report. https://cancerregistry.fi/
- NORDCAN 2.0 participant; ECIS contributor. https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- FinnGen public summary releases; FinRegistry. https://www.finngen.fi/en/public-data-releases
- Research access body: Findata; TEHDAS2 partners Sitra (coordinator), CSC, Findata, THL, HUS, VTT. https://tehdas.eu/partners/
- Synthetic datasets: n/f.

#### (c) Cancer infrastructure
- National cancer strategy "Yhdessä syöpää vastaan" 2026–2035 (published autumn 2025); roadmap due 2026. https://valtioneuvosto.fi/-/1271139/yhteinen-suunta-ihmislahtoiseen-ja-vaikuttavaan-syovan-ehkaisyyn-ja-hoitoon-kansallinen-syopastrategia-on-julkaistu
- FICAN (national cancer centre, 2019; five regional centres; represents Finland in OECI). https://stm.fi/en/personalized-medicine/national-cancer-center
- OECI: HUS CCC accredited twice (first Nordic CCC); Tays Cancer Centre renewed; all five regional centres OECI members. OECI accredited-centres list (2026-11-19) shows four Finnish entries: Helsinki University Hospital CCC, TAYS Tampere, Turku University Hospital Cancer Centre, Kuopio University Hospital Cancer Center (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://www.hus.fi/en/newsroom/hus-comprehensive-cancer-centre-designated-top-level-european-cancer-hospital-second-time ; https://www.tuni.fi/en/news/tays-cancer-centre-meets-rigorous-european-quality-standards
- Genomics: FinnGen (public-private, >500k participants; cancer registry linkage); Genome Center: the genome act (genomilaki) was removed from the government's legislative programme and the Genomikeskus has not been established (verified 2026-11-19) https://stm.fi/-/genomilain-antaminen-siirtyy-eteenpain-genomikeskuksen-valmistelu-jatkuu https://www.finngen.fi/en/node/2635
- Biobank: FINBB (Finnish Biobank Cooperative) = BBMRI.fi; Fingenious portal. https://www.finngen.fi/en/node/1995
- Imaging: EUCAIM partners Euro-BioImaging ERIC, Wellbeing Services County of North Savo. https://cancerimage.eu/partners/
- EU projects: ECHoS (Cancer Society of Finland, HUS); EUCanScreen (THL, Cancer Society); TEHDAS2 coordinator Sitra; EUnetCCC participant HUS-yhtymä (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf https://ki.se/en/cancerresearchki/a-new-european-consortium-funded-with-6-million-euros-will-create-a-network-of
- OMOP/EHDEN: FinOMOP consortium (THL) onboarded in DARWIN EU; EHDEN partners Pirkanmaa Hospital District, BCB Medical, Hospital District of Southwest Finland, Prostate Cancer Registry of South West Finland, THL, FinRegistry, HUS. https://www.ehden.eu/datapartners/ ; https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: Findata as HDAB; Kanta. https://www.sitra.fi/en/projects/value-from-nordic-health-data-valo

#### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: OmaKanta (national); oncology-specific content n/f.
- Kanta: CDA R2 documents for patient records; FHIR only for new content. https://www.kanta.fi/en/fhir-technology-and-kanta
- Koodistopalvelu (national code server, SOAP/XML retired Jan 2026). https://www.kanta.fi/documents/d/guest/koodistopalvelun-rajapinnat-ja-liittymisohje-1_8
- Structured pathology: THL "patologian tietosisältöjen yhtenäistäminen" work. https://www.slideshare.net/THLfi/patologian-tietosisltjen-yhtenistminen-suomessa
- EHR: Apotti (Epic, HUS area), Esko, others; chemo systems n/f.
- MDT software, openEHR oncology: n/f.
- THL-coordinated guide on follow-up of access to cancer care (16 cancer types). https://www.sttinfo.fi/files/69820264/70275300/98389/fi

#### Key organisations and people
- THL, Kela/Kanta, Findata, Finnish Cancer Registry / Cancer Society of Finland, FICAN, HUS CCC, FINBB, FinnGen, Sitra. People: Janne Pitkäniemi (Director, Finnish Cancer Registry, Syöpä 2024 report (verified 2026-11-19) https://www.verkkouutiset.fi/a/syopatiedoissa-isot-alueelliset-erot-yksi-seutu-erottuu/ ) https://www.sttinfo.fi/files/69820264/70275300/98389/fi ; Mikael Rinnetmäki (HL7 Finland).

---
