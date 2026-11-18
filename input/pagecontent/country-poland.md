### Poland (PL)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** "Polska specyfikacja bazowa HL7 FHIR (HL7 FHIR PL Base)", publisher HL7 Poland (Polskie Stowarzyszenie HL7). Two tracks in the repo: hl7.fhir.pl.base.r5 v0.2.0 (FHIR 5.0.0, releaseLabel ci-build, depends on hl7.fhir.eu.base-r5 2.0.1 and xtehr.eu.ehds.models 1.0.0) and hl7.fhir.pl.base.r4 v0.1.1 (FHIR 4.0.1, draft, depends on hl7.fhir.eu.base current). Canonical http://hl7.org.pl/fhir/ig/pl-base. Package registry shows 0.1.2 (R5) built 9 Oct 2025. No official release; Simplifier State of FHIR 2026 calls the national core guide "under development". Companions: hl7.fhir.pl.terminology 0.1.0 (R5), PL Laboratory IG (ci 0.1.2).
   https://build.fhir.org/ig/HL7-Poland/pl-fhir-base/ ; https://raw.githubusercontent.com/HL7-Poland/pl-fhir-base/master/sushi-config.yaml ; https://raw.githubusercontent.com/HL7-Poland/pl-fhir-base/main/sushi-config.yaml ; https://get-ig.org/hl7.fhir.pl.base.r5 ; https://api.simplifier.net/jurisdictions/PL
2. **Oncology FHIR specifications:** none found. eDiLO (electronic oncology diagnostics/treatment card) enters into force 11 Aug 2026 and becomes electronic-only on 1 Jan 2027, technical support by Centrum e-Zdrowia; a CeZ document bases e-DiLO documentation on IHE XDS.b; no FHIR profile or mCODE reuse found. CeZ publishes FHIR profiles for other domains (SMPL, e.g. PLPatient).
   https://www.nfz.gov.pl/aktualnosci/aktualnosci-centrali/komunikat-dla-swiadczeniodawcow,8995.html ; https://www.nfz.gov.pl/aktualnosci/aktualnosci-centrali/komunikat-dot-realizacji-diagnostyki-i-leczenia-nowotworow-po-1-stycznia-2027-r-w-oparciu-o-karte-dilo,9041.html ; https://ezdrowie.gov.pl/pobierz/15343 ; https://isus.ezdrowie.gov.pl/smpl/StructureDefinition-PLPatient.html
3. **Cancer registry reporting standard:** Krajowy Rejestr Nowotworów (KRN), run by NIO-PIB (Narodowy Instytut Onkologii im. M. Skłodowskiej-Curie – PIB). Since 1 Oct 2024 reporting is electronic only through e-KRN+ (web application with account login; integrated hospitals have data extracted from clinical records). Form basis: MZ/N-1a card (KZNZ); reportable ICD-10 C00–C97, D00–D09 (and some D37–D48).
   https://onkol.kielce.pl/sites/default/files/Biuletyny/instrukcja_ekrn.pdf ; https://onkologia.org.pl/sites/default/files/iu_ekrn_lekarz_i_asystent_v1.0.pdf ; https://medycynarodzinna.wum.edu.pl/sites/medycynarodzinna.wum.edu.pl/files/2026-03/6_rok_dokumentacja_onkologiczna_w_poz.pdf.pdf
4. **Terminologies:** SNOMED CT: not a member (Poland absent from SNOMED International member list). ICD-10: Polish 2008 edition maintained by CeZ, ICD-11 translation published as pre-final, no formal adoption decision. ICD-O-3: Polish edition published by KRN. LOINC: Polish translation (~20,000 concepts) deposited Aug 2023, included in LOINC 2.81 (Aug 2025), Polish LOINC centre at Medical University of Łódź. TNM 8 used in KRN material. ATC / national drug code: not found. Terminology server: none, "in the planning stage".
   https://www.snomed.org/members ; https://www.gov.pl/web/zdrowie/pytania-i-odpowiedzi-icd-11 ; https://onkologia.org.pl/sites/default/files/publications/2023-11/icd_o_3_pl.pdf ; https://loinc-ssidl.umed.pl/2025/09/09/ ; https://api.simplifier.net/jurisdictions/PL
5. **Organisations and people:** Centrum e-Zdrowia (cez.gov.pl); HL7 Poland, chair Roman Radomski; NIO-PIB (KRN). GitHub contributor to pl-fhir-base: "sbojanowski" (full name not found).
   https://api.simplifier.net/jurisdictions/PL ; http://hl7.org.pl/ ; https://api.github.com/repos/HL7-Poland/pl-fhir-base/contributors

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Krajowy Rejestr Nowotworów (KRN), run by NIO-PIB (Narodowy Instytut Onkologii im. M. Skłodowskiej-Curie – PIB, Warsaw), central database integrating 16 voivodeship cancer registration offices (Wojewódzkie Biura Rejestracji Nowotworów). https://sympozjum.ceestahc.org/wp-content/uploads/symp2020/didkowska.pdf
- Coverage: 100% national (ECIS prevalence list). https://ecis.jrc.ec.europa.eu/pdf/Prevalence_List_of_cancer_registries.pdf
- ENCR/IACR: KRN works to ENCR/IACR rules (2024 registration conference agenda); formal membership record n/f. https://onkologia.szczecin.pl/wp-content/uploads/2024/08/Agenda-Konferencji-Rejestracja-nowtworow-24.09.2024.pdf
- Legal basis: regulation on KRN, consolidated text Dz.U. 2024 poz. 160 (original Dz.U. 2012 poz. 1497). https://eli.gov.pl/eli/DU/2024/160/ogl/pol/pdf
- Submission: electronic only since 1 Oct 2024 via e-KRN+ (web application; integrated hospital systems extract data from clinical records); form basis MZ/N-1a card (KZNZ). https://onkol.kielce.pl/sites/default/files/Biuletyny/instrukcja_ekrn.pdf
- Variable dictionary: ICD-10 C00–C97, D00–D09 (some D37–D48); ICD-O-3 morphology (histology/behaviour/grade); TNM 8 stage tables. https://medycynarodzinna.wum.edu.pl/sites/medycynarodzinna.wum.edu.pl/files/2026-03/6_rok_dokumentacja_onkologiczna_w_poz.pdf.pdf
- Organ/clinical registries: e-KRN+ was built as a platform for KRN plus oncology organ registries ("onkologiczne rejestry narządowe"); NIO organ registries discussed in 2026 patient-organisation briefings. https://onkologia.org.pl/sites/default/files/iu_ekrn_lekarz_i_asystent_v1.0.pdf ; https://alivia.org.pl/wp-content/uploads/sites/10/2026/06/Rejestry-narzadowe-NIO.pdf
- Screening registry: NFZ SIMP (System Informatyczny Monitorowania Profilaktyki), since 2007, breast/cervical/colorectal/HPV results; provider interface SOAP/XML v3. https://www.nfz.gov.pl/dla-swiadczeniodawcy/sprawozdawczosc-elektroniczna/interfejsy-integracyjne/simp/
- Researcher access route: formal procedure n/f; contact krn@nio.gov.pl; online reports on onkologia.org.pl. https://sympozjum.ceestahc.org/wp-content/uploads/symp2020/didkowska.pdf

#### (b) Public datasets
- Open statistics portal: KRN interactive reports and annual bulletin "Nowotwory złośliwe w Polsce" (latest: 2023 data, published Jan 2026). https://onkologia.org.pl/sites/default/files/publications/2026-01/0.nowotwory-krn-2025-book-20260123.pdf
- Survival/incidence open data: via KRN portal; dane.gov.pl datasets n/f.
- ECIS: Poland national registry contributes (100% coverage). https://ecis.jrc.ec.europa.eu/pdf/Prevalence_List_of_cancer_registries.pdf
- Screening data: NFZ publishes monthly programme implementation data. https://api.sejm.gov.pl/sejm/term10/interpellations/attachment/ATTDJ2HVE/i09872-o1.pdf
- Synthetic datasets: n/f. National health data catalogue: n/f (CeZ is TEHDAS2 partner). https://tehdas.eu/tehdas2/partners/
- Research data access body (EHDS HDAB): n/f.

#### (c) Cancer infrastructure
- National institute/plan: NIO-PIB; Narodowa Strategia Onkologiczna 2020–2030 (budget 5.1 bn PLN). https://www.gov.pl/web/zdrowie/narodowa-strategia-onkologiczna
- Network: Krajowa Sieć Onkologiczna (KSO) in force 1 Apr 2025; Krajowy Ośrodek Monitorujący at NIO-PIB plus voivodeship monitoring centres; 2026 amendment (Dz.U. 2026 poz. 208) on quality indicators. https://www.infor.pl/akt-prawny/DZU.2026.208.0001007,ustawa-o-zmianie-ustawy-o-krajowej-sieci-onkologicznej-oraz-niektorych-innych-ustaw.html
- OECI: no accredited centre found; Wielkopolskie Centrum Onkologii (Poznań) listed as OECI member not in accreditation. https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: Poland is not a 1+MG signatory (observer); national genomics roadmap 2024; G4PL (Genomics for Poland) project 2026–2029, ~PLN 248 m; contributes to Genome of Europe. https://port.lukasiewicz.gov.pl/wp-content/uploads/2024/06/Roadmap-draft-Polish-Genomics-2024-MMedits-v.8-final-corrected.pdf ; https://www.genomeweb.com/sequencing/polish-population-genomics-project-wins-pln-248m-sequence-7k-individuals
- Biobank: BBMRI.pl, national node at Łukasiewicz–PORT (Wrocław), 12 biobanks in Directory, node director Radosław Zagożdżon. https://www.bbmri-eric.eu/national-nodes/
- Imaging/EUCAIM: Gdańsk University of Technology, Łukasiewicz–PORT, Medical University of Gdańsk. https://cancerimage.eu/partners/
- EU projects: CraNE (NIZP-PZH), EUCanScreen (NIO as competent authority, IGiChP affiliated), TEHDAS2 (MoH, CeZ), ECHoS (first National Cancer Mission Hub in Europe launched in Poland). https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/ ; https://sciencebusiness.net/news/r-d-funding/horizons-cancer-mission-debuts-first-national-coordination-hub
- OMOP: EHDEN data partners list has no Polish entry; DARWIN EU partner Children's Memorial Health Institute (Warsaw). https://www.ehden.eu/datapartners/ ; https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: n/f.

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR/portal: P1 platform (CeZ) with IKP (Internetowe Konto Pacjenta); e-recepta, e-skierowanie; EDM documents in PIK HL7 CDA (Polska Implementacja Krajowa, v1.3.x); IKP displays PIK CDA with embedded PDF. https://ezdrowie.gov.pl/pobierz/15343 ; https://ezdrowie.gov.pl/downloadFile/5348
- Oncology documents: eDiLO (electronic oncology card) live 11 Aug 2026, electronic-only 1 Jan 2027; e-DiLO documentation based on IHE XDS.b per CeZ document; NFZ DiLO web-service interface v4.0 (SOAP/XML). https://www.nfz.gov.pl/aktualnosci/aktualnosci-centrali/komunikat-dla-swiadczeniodawcow,8995.html ; https://nfz.gov.pl/download/gfx/nfz/pl/defaultstronaopisowa/1218/2/1/system_dilo_-_format_uslug_sieciowych_v4.0.pdf
- Registry exchange: e-KRN+ hospital integration (format n/f); SIMP SOAP/XML for screening. https://www.nfz.gov.pl/dla-swiadczeniodawcy/sprawozdawczosc-elektroniczna/interfejsy-integracyjne/simp/
- Structured pathology: PTP adopted CAP synoptic report format (breast, colorectal, lung first); MoH accreditation standards for pathology units (obwieszczenie 24 Sep 2021, Dz.Urz.MZ 2021.75). https://journals.viamedica.pl/oncology_in_clinical_practice/article/download/38273/26904 ; https://www.pap.pl/aktualnosci/news%2C751169%2Cministerstwo-zdrowia-powstaly-wytyczne-dla-zakladow-patomorfologii.html
- Tumour-board/MDT software: n/f. Chemotherapy e-prescribing system: n/f (e-recepta general). openEHR oncology: n/f.
- Strategy items naming cancer: NSO 2020–2030 and KSO act (quality indicators, e-DiLO). https://www.gov.pl/web/zdrowie/narodowa-strategia-onkologiczna

#### Key organisations and people
- NIO-PIB / KRN: Joanna Didkowska (KRN head, per 2020 presentation). https://sympozjum.ceestahc.org/wp-content/uploads/symp2020/didkowska.pdf
- Centrum e-Zdrowia (P1, IKP, eDiLO); NFZ (SIMP, DiLO); Ministry of Health (NSO, KSO); Łukasiewicz–PORT (BBMRI.pl, genomics roadmap); HL7 Poland (Roman Radomski).

---
