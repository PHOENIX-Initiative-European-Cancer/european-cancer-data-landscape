### Portugal (PT)

Region: Southern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National core IG:** Portuguese Core IG ("Portuguese FHIR R4B Core Profiles"), version 1.0.0, FHIR R4B, published by SPMS on Simplifier in 2024 (history entries 19-07-2024 to 29-11-2024); covers AllergyIntolerance, Bundle, MessageHeader, OperationOutcome, Parameters, Composition, List, Patient, Practitioner, PractitionerRole, Location, Organization, Schedule, Slot. Package id: not found. Source: https://simplifier.net/guide/portuguese-core-ig-prod?version=1.0.0 . Separate HL7 Portugal `hl7.fhir.pt.core` 0.0.1 CI build, R4, canonical http://hl7.pt/fhir/core, generated 2024-09-23, not authorised (https://hl7-pt.github.io/core/).
2. **Oncology FHIR IG:** not found. SPMS awarded a RON platform contract on 2025-05-02 under PRR (https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/a3e1ea2f-e50d-3f30-815e-c6a058d260d7); no FHIR specification public. mCODE: not found.
3. **Registry reporting:** RON (Registo Oncológico Nacional), Law 53/2017, single national electronic platform; all new diagnoses registered within 9 months, annual updates on stage, treatment and vital status; coordinator Maria José Bento (IPO Porto); ICD-O-3 used by RORENO. Submission format: not found (ron.min-saude.pt unreachable). Source: https://diariodarepublica.pt/dr/detalhe/lei/53-2017-107692693
4. **Terminologies:** SNOMED CT member since Jan 2014, SPMS Centro de Terminologias Clínicas (CTC) as NRC (https://www.snomed.org/member/portugal); national edition: not found. ICD-10-CM/PCS (English original) for hospital coding since 2017-01-01 (https://interop-pt.atlassian.net/wiki/spaces/CTCPT/pages/58884368). ICD-O-3. LOINC national variant: not found. Drug code CHNM (INFARMED, Portaria 155/2007, https://www.infarmed.pt/documents/15786/1068150/034-B_Port_155_2007_VF.pdf). TNM edition: not found. Terminology server: not available; SPMS PRR consultancy tender for a terminology server, 2026 (https://diariodarepublica.pt/dr/detalhe/anuncio-procedimento/1947-2026-1027897292).
5. **Organisations and people:** SPMS (CTC, https://www.ctc.min-saude.pt), HL7 Portugal (chair João Almeida, technical lead Ricardo Correia, https://hl7.eu/affiliate_pt.html), IPO Porto (RON coordination, Maria José Bento).

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- RON (Registo Oncológico Nacional): single national electronic platform created by Lei 53/2017, in force 1 Jan 2018; mandatory registration of all new diagnoses (public, social, private) within 9 months; annual updates on stage, treatment, vital status; diagnoses coded with ICD version in force. https://diariodarepublica.pt/dr/detalhe/lei/53-2017-107692693
- Former regional registries ROR-Sul, ROR-Centro, RORENO, RORA (Azores) and the paediatric registry integrated into RON. https://comum.rcaap.pt/bitstream/10400.26/29608/1/Ron%2002.07.2019.pdf
- Coverage: all tumours in the resident population (national, 100%). https://recipp.ipp.pt/bitstreams/2d6bfbcf-bde1-4e0f-bd69-ee3a79381f07/download
- Coordinator: Maria José Bento (IPO Porto, Epidemiology Service). https://observador.pt/2025/12/29/portugal-registou-mais-de-60-mil-novos-casos-de-cancro-em-2022/
- Coding: ICD-O-3 (RORENO; IPO Porto registry listed in EMA catalogue). https://catalogues.ema.europa.eu/print/pdf/node/966
- Submission format and variable dictionary: n/f (ron.min-saude.pt unreachable); SPMS procured a new RON solution under PRR, awarded 2 May 2025. https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/a3e1ea2f-e50d-3f30-815e-c6a058d260d7
- Timeliness: 2022 incidence published Dec 2025; backlog reported (some hospitals years behind). https://24noticias.sapo.pt/tecnologia/artigos/auroramed-a-ia-portuguesa-que-quer-por-o-registo-oncologico-em-dia
- ENCR/IACR: RON designated as Portugal's representative in a European joint action on registry harmonisation (2024). https://www.noticiasaominuto.com/pais/2092628/registados-2685-casos-de-cancro-pediatrico-em-10-anos
- Screening registries: DGS population screening monitoring (SIIMA n/f); 2024 report: breast coverage 61%, colorectal 32.5%. https://www.dnoticias.pt/2026/2/4/480090-cobertura-do-rastreio-dos-cancros-colon-e-recto-e-colo-do-utero-ainda-longe-da-meta/
- Researcher access route: n/f.

#### (b) Public datasets
- RON incidence report (2022 data: 60,954 cases, 579.6/100,000) and survival report (2019 cohort, 66% five-year survival, May 2026). https://www.rtp.pt/noticias/pais/sobrevivencia-ao-cancro-em-portugal-atinge-66-mas-desigualdades-persistem_n1742152
- DGS planned an electronic tool to publish screening activity data (2024). https://theportugalnews.com/news/2024-02-04/standardising-cancer-screening-costs/85696
- Research data access body: HealthData@PT (SPMS, EU4Health, from 1 Nov 2023, 48 months) preparing the national HDAB and dataset catalogue (D6.1, Oct 2025). https://www.spms.min-saude.pt/wp-content/uploads/2025/10/D6.1-National-dataset-catalogue-requirements-and-specifications.pdf
- ECIS contribution: Portuguese registries via ENCR; list n/f. Open data portal (Transparência SNS) oncology datasets: n/f. Synthetic data: n/f.

#### (c) Cancer infrastructure
- Estratégia Nacional de Luta contra o Cancro, horizonte 2030, approved by Despacho 13227/2023, prepared by DGS/PNDO; four pillars. https://vlex.pt/vid/despacho-n-13227-2023-973680823
- OECI: Porto.CCC (IPO Porto + i3S) re-accredited Comprehensive Cancer Centre to 2027; IPO Lisboa OECI-accredited clinical cancer centre with national Tumour Biobank. https://www.i3s.up.pt/pccc.php ; https://core.ac.uk/download/427722367.pdf
- CCI4EU consultancy at IPO Porto (OECI-led). https://oncodaily.com/voices/373816
- Biobanks: Portugal joined BBMRI-ERIC; GIMM national node, coordinating Biobanco.pt network (GIMM, Champalimaud, Católica, INSA, CHAIN|NMS). https://gimm.pt/?p=12407
- Genomics: 1+MG signatory; INSA (Astrid Vicente) co-authored 1+MG maturity model pilot. https://zenodo.org/records/8135894/files/ESHG%2023_Poster%20MLM_Final.pdf
- EUCAIM partners: Champalimaud Foundation, CHU Santo António, Liga Portuguesa Contra o Cancro (Centro). https://cancerimage.eu/partners/
- EHDEN/OMOP: 11 Portuguese data partners incl. Hospital do Espírito Santo Évora, CHU Coimbra, Hospital da Luz, Hospital de Santarém. https://www.ehden.eu/datapartners/
- EUnetCCC: Portugal has a pilot centre (Nov 2025). https://observador.pt/2025/11/13/rede-europeia-de-centros-de-cancro-vai-garantir-acesso-aos-mesmos-tratamentos-em-todos-os-paises-da-ue-incluindo-portugal/
- Other EU projects (EOSC4Cancer, UNCAN.eu, canSERV, JANE, CraNE, ECHoS, EUCanScreen, TEHDAS2): n/f.

#### (d) Digital, non-FHIR
- E-prescription: PEM (Prescrição Eletrónica Médica); hospital PEMH and BDNP-H database; INFARMED/ACSS/SPMS technical norms for hospital outpatient prescribing (2021). https://www.infarmed.pt/documents/15786/4183417/Normas+t%C3%A9cnicas%2C+especifica%C3%A7%C3%B5es+e+requisitos+t%C3%A9cnicos+dos+sistemas+inform%C3%A1ticos+de+prescri%C3%A7%C3%A3o+e+dispensa+de+medicamentos+a+utentes+em+regime+de+ambulat%C3%B3rio+hospitalar+pelos+servi%C3%A7os+farmac%C3%AAuticos+hospitalares+do+Servi%C3%A7o+Nacional+de+Sa%C3%BAde+%28SNS%29/281ebc9d-00e3-cc31-dcd4-fa61f71ecfd5
- Patient portal SNS 24 (prescriptions, exams). https://www.deco.proteste.pt/saude/medicamentos/noticias/receita-medica-eletronica-funciona-precisa-saber
- Coding: ICD-10-CM/PCS since 2017-01-01; CHNM drug code (INFARMED); SNOMED CT (SPMS CTC, member 2014). https://interop-pt.atlassian.net/wiki/spaces/CTCPT/pages/58884368
- Structured pathology: Portuguese study converting ICCR colorectal dataset to FHIR SDC (research, 2025). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12463337/
- Tumour-board software, openEHR oncology archetypes, RSE oncology content: n/f.

#### Key organisations and people
- SPMS (HealthData@PT, RON procurement, CTC); DGS / PNDO; INSA; INFARMED; ACSS.
- RON coordinator Maria José Bento (IPO Porto); IPO Lisboa; Porto.CCC / i3S; GIMM (BBMRI.pt). https://gimm.pt/?p=12407
- HL7 Portugal chair João Almeida. https://hl7.eu/affiliate_pt.html

---
