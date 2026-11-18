### Norway (NO)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** no-basis, package `hl7.fhir.no.basis`, FHIR R4, v2.2.2 (bugfix 2025-03-26), publisher HL7 Norway, canonical http://hl7.no/fhir/; 19 approved base profiles (Feb 2025), no must-support; recommended standard in Helsedirektoratet's Referansekatalogen; survey rates it "widely used".
   https://simplifier.net/hl7norwayno-basis ; https://packages.fhir.org/hl7.fhir.no.basis ; https://www.helsedirektoratet.no/standarder/norske-basisprofiler-for-hl7-fhir ; https://hl7europe-test.azurewebsites.net/wp-content/uploads/2025/02/05_eusni2025_norway.pdf
2. **Oncology FHIR specifications:** not found. No Kreftregisteret FHIR IG located.
   https://packages.fhir.org/jurisdictions/NO
3. **Cancer registry reporting:** Kreftregisteret, part of Folkehelseinstituttet (FHI) since 1 January 2024. Clinical reporting via the KREMT web service or EHR systems built on the registry's message specifications; paper abolished spring 2017. Pathology: copies of over 350,000 pathology reports per year as e-helse "Svar" messages v1.3/v1.4 (AppRec 1.0/1.1), selected by NORPAT codes; spec revised 04.12.2025.
   https://www.fhi.no/en/cancer/reporting/kremt-cancer-registrys-electronic-reporting-service/ ; https://www.fhi.no/contentassets/bb8d17623751483099eb6321111b868b/spesifikasjon---elektronisk-innsending-av-patologiremisser-1.pdf ; https://fhi.no/om/fhi/omrader/kreftregisteret
4. **Terminologies:** SNOMED CT member since 1 January 2017 (30th member); NRC Helsedirektoratet; about 10 extension releases per year. ICD-10 Norwegian edition updated annually ("Nytt i 2026", FinnKode); ICD-11 upgrade strategy drafted; NCSP/NCMP/NCRP. NORPAT for pathology. ICD-O-3, TNM edition, LOINC (NPU in use, to be published on tx-nordics), ATC: not found. National FHIR terminology server: in development.
   https://www.snomed.org/news/norway-joins-snomed-international-as-our-30th-member ; https://www.helsedirektoratet.no/digitalisering-og-e-helse/helsefaglige-kodeverk/snomed-ct/snomed-ct-i-norge ; https://www.helsedirektoratet.no/veiledere/kodeveiledning-regler-og-veiledning-for-klinisk-koding-i-spesialisthelsetjenesten
5. **Organisations and people:** Helsedirektoratet (standards body, absorbed Direktoratet for e-helse 2024), HL7 Norway (best-practice site), FHI/Kreftregisteret. Øyvind Aassve (HL7 Norway, Sykehuspartner, affiliate presenter, profile portal contact); Line Andreassen Sæle (styreleder HL7 Norge, 2025).
   https://hl7norway.github.io/best-practice/ ; https://www.helsedirektoratet.no/om-oss/rad-og-utvalg/standardiseringsutvalet/_/attachment/inline/03002456-798d-4951-b803-d003f50171b5:75bfd5a71b2a2e8d9edc1ad5ca2524a4ef3d51c3/M%C3%B8te%202-25%20Referat.pdf

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Kreftregisteret (Cancer Registry of Norway), founded 1952, part of Folkehelseinstituttet since 1 Jan 2024; basic registry covers 98.6% of cancer patients 2019–2023. https://fhi.no/om/fhi/omrader/kreftregisteret ; https://www.fhi.no/en/cancer/clinical-registries/prostate-cancer-registry/Degree-of-coverage-and-data-quality
- ENCR/IACR: listed; ANCR member. https://catalogues.ema.europa.eu/node/1039/data-flows-and-management ; https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: Kreftregisteret operates 12 quality registries (8 with national status, 2022). https://www.fhi.no/kreft/statistikk/Opplysninger-i-databasen/ ; https://www.ntnu.no/ojs/index.php/norepid/article/view/4975
- Screening: three programmes (Mammografiprogrammet, Livmorhalsprogrammet, Tarmscreeningprogrammet), all run by Kreftregisteret. https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/diagnose-og-behandling/kreft/screeningprogram-for-kreft
- Legal basis: Kreftregisterforskriften; mandatory electronic reporting since 2017. https://www.fhi.no/kreft/innrapportering/innrapportering-kremt/
- Submission format: KREMT web portal or EHR-integrated messages per registry message specs; pathology as e-helse "Svar" v1.3/1.4 messages selected by NORPAT codes; radiotherapy data twice a year. https://www.fhi.no/contentassets/bb8d17623751483099eb6321111b868b/spesifikasjon---elektronisk-innsending-av-patologiremisser-1.pdf ; https://www.fhi.no/om/strategi-2026-2030/fhis-helsedatastrategi/
- Coding: ICD-O-3 (NORDCAN), NORPAT; TNM registration voluntary (UICC 5/6/7 in 2004–2016 study); current edition n/f. https://medicaljournalssweden.se/actaoncologica/article/download/24253/28421/74284
- Researcher access: Helsedataservice via helsedata.no single application form (since 2019); Kreftregisteret Data Delivery Unit; Janus serum bank. https://www.fhi.no/en/cancer/data-and-statistics/Datautlevering/ ; https://www.fhi.no/en/hd/access-to-data/applying-for-access-to-data/

#### (b) Public datasets
- Statistikkbank (Kreftregisteret) and "Cancer in Norway" annual report. https://www.fhi.no/kreft/statistikk/data-og-statistikk/ ; https://develop.fhi.no/globalassets/cancer-in-norway/2023/cancer-in-norway-2023.pdf
- data.norge.no catalogue entry for Kreftregisteret. https://data.norge.no/datasets/caf3d50c-1d5c-3909-860b-0f491b24177b
- NORDCAN 2.0 participant; ECIS contributor. https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- Research access body: Helsedataservice (helsedata.no); TEHDAS2 partners Helsedirektoratet and FHI. https://tehdas.eu/partners/
- Synthetic datasets: n/f.

#### (c) Cancer infrastructure
- National strategy: "Joint efforts against cancer 2025–2035" (Nasjonal kreftstrategi); goal that all patients have access to a CCC or cancer centre. https://www.regjeringen.no/en/documents/joint-efforts-against-cancer-20252035/id3087629/?ch=8
- OECI: Oslo University Hospital CCC accredited 2017, re-accredited 2023 (only accredited centre in Norway); Haukeland (Helse Bergen) in accreditation process 2024–2025; Ahus pursuing. https://med.uio.no/klinmed/english/about/organization/divisions/cancer-medicine/comprehensive-cancer-centre ; https://www.helse-bergen.no/en/comprehensive-cancer-center-accreditation/ ; https://www.ahus.no/en/profession-and-research/research-and-innovation/Ahus-Cancer-Centre/oeci-accreditation/
- Precision medicine: InPreD national infrastructure (six university hospitals, two WGS hubs); IMPRESS-Norway trial; CONNECT consortium (Oslo Cancer Cluster); Helsedirektoratet coordinates national precision medicine strategy. https://pubmed.ncbi.nlm.nih.gov/35513529/ ; https://oslocancercluster.no/?p=16655
- 1+MG / Genome of Europe: Norway participates (about 6,700 genomes target; Helsedirektoratet page). https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/diagnose-og-behandling/persontilpasset-medisin/1-mg ; https://elixir.no/funding-and-projects/genome-of-europe
- Biobank: BBMRI.no (Director Kristian Hveem); Janus serum bank at Kreftregisteret. https://www.bbmri-eric.eu/national-nodes/norway/
- Imaging: EUCAIM partner Oslo Universitetssykehus HF. https://cancerimage.eu/partners/
- EU projects: ECHoS (Norwegian Cancer Society, Oslo Cancer Cluster, Research Council; national Cancer Mission Hub established); EUCanScreen (Helsedirektoratet, Kreftregisteret); JANE-2 (Oslo University Hospital); EOSC4Cancer (ELIXIR Norway). https://oslocancercluster.no/news/echos-gathers-europe-against-cancer ; https://elixir.no/funding-and-projects/eosc4cancer
- OMOP/EHDEN: EHDEN data partners Norwegian Cancer Registry and University of Oslo. https://www.ehden.eu/datapartners/
- National health data space: helsedata.no / Helsedataservice; FHI health data strategy 2024–2027. https://www.fhi.no/om/strategi-2026-2030/fhis-helsedatastrategi/

#### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: helsenorge.no (national portal; cancer-specific content n/f).
- EHR: DIPS (most hospitals), Helseplattformen (Epic, Midt-Norge, contested). https://www.helseplattformen.no/om-oss/helseplattformen-one-common-regional-health-record/
- Exchange formats: e-helse "Svar" (XML) messages with AppRec; KREMT message specifications; HER-id addressing. https://www.fhi.no/contentassets/bb8d17623751483099eb6321111b868b/spesifikasjon---elektronisk-innsending-av-patologiremisser-1.pdf
- Structured pathology: NORPAT codes mandatory in all pathology departments; registry aims for structured templates in LIS. https://conf.spaces.snomed.org/wiki/spaces/PLT/pages/131829871 ; https://www.fhi.no/en/cancer/reporting/reporting-pathology-information/
- openEHR: Norwegian MDT work for prostate and kidney cancer using openEHR and SNOMED CT (2022 Nordic openEHR meeting). https://discourse.openehr.org/uploads/short-url/1zvfSCUCq01AbnjQXEb2CaIY1jk.pdf
- Chemotherapy: Omda Oncology/Cytodose developed at Norway's leading cancer centre, launched 2001. https://intuitionlabs.ai/software/pdfs/omda-oncology.pdf
- Medication: Pasientens legemiddelliste, SFM Datashare (FHIR) for prescriptions. https://utviklerportal.nhn.no/informasjonstjenester/sentral-forskrivningsmodul/sfm-full-integration/integrating-with-the-datashare-api
- ICD-11 transition strategy (draft 2026). https://www.helsedirektoratet.no/rapporter/oppgraderingsstrategi-for-icd-11-informasjonsforvaltning-kodeverk-og-terminologi/sammendrag

#### Key organisations and people
- FHI/Kreftregisteret, Helsedirektoratet, Helsedataservice, OUS CCC, Oslo Cancer Cluster, InPreD/IMPRESS, BBMRI.no. People: Kristian Hveem (BBMRI.no); IMPRESS-Norway leads per Nat Med 2022 paper (Helland/Tasken et al.) https://pubmed.ncbi.nlm.nih.gov/35513529/

---
