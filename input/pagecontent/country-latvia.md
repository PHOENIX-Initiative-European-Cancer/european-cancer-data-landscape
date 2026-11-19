### Latvia (LV)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** none. Ministry of Health decides standards; SPKC maintains ICD-10; Latvijas Digitālās veselības centrs (LDVC) established 2025 as digital health authority; NVD operates e-veselība (Cabinet Regulation No. 134). FHIR R4B primary; systems use generic FHIR without IGs; discharge summary spec is CDA (NVD.EVK.CDA.3.09 v1.1).
   https://packages.fhir.org/jurisdictions/LV ; https://lvportals.lv/dienaskartiba/385601-latvijas-digitalas-veselibas-centrs-pirmaja-darbibas-gada-paveikts-butisks-darbs-digitalas-veselibas-attistiba-2026 ; https://www.varam.gov.lv/lv/media/46103/download
2. **Oncology FHIR specifications:** not found. Survey cites "oncology registry" as a FHIR use case without a published spec. Since 1 January 2024 institutions must submit the cancer patient card in e-veselība.
   https://packages.fhir.org/jurisdictions/LV ; https://vmnvd.gov.lv/lv/media/28572/download
3. **Cancer registry reporting:** oncology part of "Ar noteiktām slimībām slimojošu pacientu reģistrs", run by SPKC; data from NVD/e-veselība (cancer patient card) and monthly transfers; ICD-10 C00–C97; reporting to ENCR/IARC; manual collection reported in 2024. Technical format: not found.
   https://statistika.spkc.gov.lv/Resources/PX/Databases/Health/Metadati/ONKO_Registra_metadati_en.html ; https://www.lsm.lv/raksts/zinas/latvija/20.08.2024-veza-registrs-vel-nepabeigts-un-nepilnigs.a565719/
4. **Terminologies:** SNOMED CT member since January 2026; NRC SPKC; roadmap to 2030; SNOMED GPS used for cross-border and lab exchange. SSK-10 (ICD-10, SPKC; still the coding basis in Cabinet Regulation No. 6 of 13 January 2026; version numbering not found; SSK-11 under consideration) https://likumi.lv/ta/id/365793 . LOINC and UCUM planned. ICD-O: SSK-O-3.2 topography and morphology, and TNM 8th edition, are fields of the cancer patient card (SPKC lecture Dec 2023; ICCC and TNM 8 added to the data-entry algorithm by 1 January 2024) (verified 2026-11-19) https://www.spkc.gov.lv/lv/media/19929/download ; https://spkc.gov.lv/lv/media/19977/download . ATC: not found. National FHIR terminology server: in production per survey; operator and URL not found.
   https://www.snomed.org/members/latvia ; https://lvportals.lv/dienaskartiba/395031-snomed-ct-palidzes-veidot-vienotu-klinisko-zinasanu-telpu-latvija-2026 ; https://likumi.lv/ta/id/264943
5. **Organisations and people:** Ministry of Health, SPKC, NVD, LDVC. Named FHIR or oncology spec maintainers: not found.

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: cancer data within "Ar noteiktām slimībām slimojošu pacientu reģistrs" (Register of patients with particular diseases) at SPKC since 2009; new digital population-based cancer register under development. https://statistika.spkc.gov.lv/Resources/PX/Databases/Health/Metadati/ONKO_Registra_metadati_en.html ; https://www.intechopen.com/online-first/1204840
- ENCR conference: Latvian registry presented at the 2018 ENCR conference; data quality issues 2006–2009. https://www.encr.eu/sites/default/files/2018-ENCR-Conference/Kojalo_LV%20cancer%20registry%20quality.%20Some%20examples.pdf
- ENCR member registries: Latvian Cancer Register (director Dr. Elina Liepina). Corrected: the registry is on the ENCR member list, with SPKC (Centre for Disease Prevention and Control) as institute; the earlier n/f is resolved. Source: https://www.encr.eu/encr-members-contact-list (read 2026-11-19) (verified 2026-11-19)
- Screening: state-funded cervical, breast, colorectal, prostate screening (Cabinet Reg. 555/2018); SPKC oversees since 2023 and calls for a screening registry; colorectal screening metadata on SPKC stats. https://www.vmnvd.gov.lv/en/node/3011 ; https://www.spkc.gov.lv/lv/jaunums/baltic-congress-laboratory-medicine-centre-disease-prevention-and-control-latvia-presented-progress-implementation-organized-cancer-screening-latvia
- Clinical quality registries: n/f.
- Submission format: cancer patient card mandatory in e-veselība since 1 Jan 2024; NVD monthly non-personalised transfers to SPKC; manual collection reported 2024. https://vmnvd.gov.lv/lv/media/28572/download ; https://www.lsm.lv/raksts/zinas/latvija/20.08.2024-veza-registrs-vel-nepabeigts-un-nepilnigs.a565719/
- Coding: SSK-10 (ICD-10) C00–C97; cancer patient card uses SSK-O-3.2 topography/morphology and TNM 8th edition, with ICCC and TNM 8 added to the data-entry algorithm by 1 January 2024 (verified 2026-11-19) https://www.spkc.gov.lv/lv/media/19929/download ; https://spkc.gov.lv/lv/media/19977/download
- Legal basis: Cabinet Regulation No. 134 (e-veselība); register regulation. https://likumi.lv/ta/id/264943
- Researcher access: no clear legal procedure for inter-institutional data exchange for research (older study); SPKC data requests. https://pmc.ncbi.nlm.nih.gov/articles/PMC6979557

#### (b) Public datasets
- SPKC statistics database ONKO tables (incidence, stage, 5-year survival). https://statistika.spkc.gov.lv/pxweb/en/Health/Health__Saslimstiba_Slimibu_Izplatiba__Onkologija/ONKO030.px
- ECIS contributor: Latvian registry listed in ECIS. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Research access body: SPKC and Latvian Biomedical Research and Study Centre (TEHDAS2 partners). https://tehdas.eu/partners/
- Synthetic datasets, national catalogue: n/f.

#### (c) Cancer infrastructure
- Oncology care improvement plan 2025–2027 (government order 22 Oct 2025); fourth comprehensive plan. https://www.likumi.lv/ta/id/363895 ; https://cancer-inequalities.jrc.ec.europa.eu/sites/default/files/docs/ccp2025/ec-oecd-lv-2024-1675-en.pdf
- OECI: Riga East University Hospital Latvian Cancer Centre accredited, certificate valid to 26 Aug 2031 (first in Latvia); confirmed as the only Latvian entry on the OECI accredited-centres list (2026-11-19) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). https://www.researchlatvia.gov.lv/en/latvian-cancer-centre-joins-ranks-recognised-european-centres
- Genomics: Latvian Genome Database (LGDB, BMC, ~31,500 participants). https://pubmed.ncbi.nlm.nih.gov/29576601/
- Biobank: BMC = BBMRI-ERIC national node (Jānis Kloviņš); Biobank Law in parliament 2025. https://www.bbmri-eric.eu/national-nodes/latvia/ ; https://www.researchlatvia.gov.lv/en/looking-back-2025-key-highlights-latvian-biobank-network-bbmri-latvia
- Imaging: EUCAIM partner University of Latvia. https://cancerimage.eu/partners/
- EU projects: EUCanScreen coordinated by University of Latvia; ECHoS (Riga East hospital, Latvian Council of Science); JANE-2 (RSU); TEHDAS2 (SPKC, BMC); EUnetCCC participants University of Latvia, RSU and two hospital entities (names truncated in grant sheet) (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf . Latvia is not among the first 30 EU-Designated CCCs (Feb 2026; eight countries, Latvia not included) https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ . Pauls Stradiņš hospital cancer centre passed an OECI audit in 2026 https://lvportals.lv/dienaskartiba/392169-stradina-slimnicas-veza-centrs-veiksmigi-aizvadijis-oeci-auditu-un-turpina-virzibu-uz-starptautisku-akreditaciju-2026 https://www.unicancer.fr/wp-content/uploads/2025/10/eucanscreen-project-consortium-octobre-2025-1.pdf ; https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/
- OMOP/EHDEN: n/f.
- National health data space: LDVC architecture and guidelines 2025; strategy names FHIR, SNOMED CT, LOINC, UCUM. https://www.varam.gov.lv/lv/media/46103/download

#### (d) Digital, non-FHIR, cancer-relevant
- e-veselība (NVD): CDA-based documents (discharge summary NVD.EVK.CDA.3.09); cancer patient card; patient portal eveseliba.gov.lv. https://www.vmnvd.gov.lv/en/e-veseliba
- Structured pathology, MDT software, chemotherapy, openEHR: n/f.
- Survey cites "oncology registry" as FHIR use case (no spec). https://packages.fhir.org/jurisdictions/LV

#### Key organisations and people
- Ministry of Health, SPKC, NVD, LDVC, Riga East University Hospital (Latvian Cancer Centre), University of Latvia (EUCanScreen), BMC (Jānis Kloviņš). Registry leads: n/f.

---
