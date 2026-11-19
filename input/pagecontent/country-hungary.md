### Hungary (HU)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** none found. Simplifier jurisdiction page has no survey content (14 projects, 136 resources). EESZT (Elektronikus Egészségügyi Szolgáltatási Tér, operated by OKFŐ) uses local standards, with HL7 V3 and FHIR in specific projects (TEHDAS 2022 factsheet).
   https://api.simplifier.net/jurisdictions/HU ; https://tehdas.eu/app/uploads/2023/03/hungary-country-visit-factsheets-10-2022.pdf ; https://e-egeszsegugy.gov.hu/documents/26398/557047/EESZT_GDPR_erintett_tajekoztatasa_egeszsegugyi_intezmenyben.pdf/22667ce0-2df3-d32b-a49b-3b45c73e744f
2. **Oncology FHIR specifications:** none found. mCODE reuse: not found.
3. **Cancer registry reporting standard:** Nemzeti Rákregiszter (and Nemzeti Gyermek Onkológiai Regiszter for under-18s). Decree 49/2018 EMMI (in force version from 2025-04-05): providers report at least quarterly by the 15th of the month after the quarter; data generated automatically from provider IT systems where feasible; NEAK also reports quarterly; the transfer format is fixed by agreement between the registry and the national chief medical officer, not in the decree. Web portal nrr.hu provides "Jelentés feltöltés" (report upload). Operator organisation: not verified.
   https://net.jogtar.hu/jogszabaly?docid=A1800049.EMM ; https://njt.jog.gov.hu/jogszabaly/2018-49-20-5H ; https://nrr.hu/
4. **Terminologies:** SNOMED CT: member since Sept 2024 (announced 5 Sept 2024), contact ESZFK (www.eszfk.hu, snomed@eszfk.hu), Member Forum Zoltán Falussy and Krisztián Iszak; national edition/translation: not found. ICD-10: BNO-10 (version not found). Registry coding: the National Cancer Registry codes diagnoses and morphology on ICD-10 (BNO-10 chapter II and the ICD-10 morphology annex), not ICD-O, per Wéber et al. 2023 (Cancer Epidemiology 82:102306) (verified 2026-11-19) https://pubmed.ncbi.nlm.nih.gov/36521336/ ; the 2019 government data-element list requires pTNM "per the separately defined TNM version" (verified 2026-11-19) https://2015-2019.kormany.hu/download/b/ea/81000/ML.pdf ; TNM 8th edition (7th for prostate) used in a 2022 registry-based study (verified 2026-11-19) https://www.por-journal.com/articles/10.3389/pore.2022.1610668/full . LOINC, ATC variant, national terminology server: not found.
   https://www.snomed.org/members/hungary ; https://www.snomed.org/news/snomed-international-welcomes-hungary-to-a-growing-and-global-community-of-practice
5. **Organisations and people:** OKFŐ (EESZT operator), ESZFK (SNOMED contact), NEAK. HL7 Hungary affiliate: still not found after re-check of HL7 Europe affiliate index and HL7 International reports (an older source lists Hungary only as "pre-affiliate"). Named maintainers: not found.
   https://www.ringholm.com/column/HL7_membership_model.htm

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Nemzeti Rákregiszter (Hungarian National Cancer Registry), legally established 1999, operating since 2000, run by Országos Onkológiai Intézet (OOI); coverage 100% (mandatory reporting). https://eld.bl.uk/catalog/100174728264_0x000001 ; https://mta.hu/data/dokumentumok/egyeb_dokumentumok/2023/Daganatos_betegsegek_osszeallitas.pdf
- ENCR/IACR: follows ENCR/IACR rules; formal membership n/f. https://dea.lib.unideb.hu/bitstreams/bfa051b0-0a28-4302-9cc7-ecfc417b4986/download
- Paediatric: Nemzeti Gyermekonkológiai Regiszter (since 1971, Magyar Gyermekonkológiai Hálózat, 8 centres, online data entry); listed as Hungary's ECIS contributor. https://real.mtak.hu/199534/1/650-article-p933.pdf ; https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Legal basis and submission: decree 49/2018 EMMI, quarterly reporting generated automatically from provider systems; NEAK quarterly data; format set by agreement; web upload at nrr.hu. https://net.jogtar.hu/jogszabaly?docid=A1800049.EMM ; https://nrr.hu/
- Variable dictionary: electronic data elements fixed in 2019 government document: BNO-10 chapter II diagnosis code, morphology code per BNO-10 morphology annex, pTNM "per separately defined TNM version", grade, OENO procedure code (verified 2026-11-19) https://2015-2019.kormany.hu/download/b/ea/81000/ML.pdf . CORRECTED: registry coding is based on ICD-10, not ICD-O (Wéber et al. 2023, morphologically verified 57.8 percent) (verified 2026-11-19) https://pubmed.ncbi.nlm.nih.gov/36521336/ ; TNM 8th edition (7th for prostate) in 2022 registry-based study (verified 2026-11-19) https://www.por-journal.com/articles/10.3389/pore.2022.1610668/full https://eld.bl.uk/catalog/100174728264_0x000001
- Researcher access: ETT ethics approval for research use of central data (2016 guidance); formal registry request route n/f. https://ett.aeek.hu/wp-content/uploads/2016/09/adatvedelem.pdf

#### (b) Public datasets
- Open cancer statistics portal: n/f (registry annual data via OOI publications; GHDx catalogues incidence reports). https://ghdx.healthdata.org/node/114505
- ECIS: adult registry not in ECIS historical list; paediatric registry listed. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- NEAK and KSH databases linked to registry by OOI National Tumour Biology Laboratory (Jan 2026). https://infostart.hu/belfold/2026/01/06/attores-kuszoben-a-hazai-rakgyogyitas-ot-ev-kutatasi-eredmenyeit-osszegeztek
- Screening data, synthetic data: n/f. HDAB: no designation found (Hungarian-language search, Nov 2026); OKFŐ co-authors TEHDAS2 HDAB guidelines. TEHDAS2 partners: OKFŐ, ESZFK. https://tehdas.eu/tehdas2/partners/

#### (c) Cancer infrastructure
- Institute: OOI Budapest, OECI Comprehensive Cancer Centre (first in CEE), on the OECI certified-centres list as of 2026-11-19 (verified 2026-11-19) https://accreditation.oeci.eu/ ; minister initiated accreditation of the whole oncology network. https://news.ki.se/strengthened-collaboration-with-hungary-in-the-field-of-cancer ; https://www.ceskenoviny.cz/zpravy/2366057
- Plan: Nemzeti Rákellenes Program (government programme 2006, revised 2018); OECD 2023 profile cites target of 10 percent cut in cancer mortality by 2030 (verified 2026-11-19) https://infostart.hu/belfold/2018/07/30/nemzeti-egeszsegprogram ; https://www.oecd.org/social-issues-migration-health/rakugyi-orszagprofil-magyarorszag-2023_39a8899f-hu
- OECI: Korányi Institute listed as member not in accreditation. https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: Hungary joined 1+MG/GDI April 2024 (with Cyprus, Malta, Romania). https://agerpres.ro/educatie-stiinta/2024/05/27/mcid-romania-a-aderat-la-proiectul-european-pentru-infrastructura-de-date-genomice--1301941
- Biobank: BBMRI.hu (Hungarian Biobank Node, est. 2021, Semmelweis-led; Oncobank subnetwork; director Mária Judit Molnár). https://www.bbmri-eric.eu/national-nodes/ ; https://semmelweis.hu/english/2022/03/semmelweis-biobank-network-our-goal-is-to-become-a-regional-leader-of-the-field/
- Imaging/EUCAIM: none listed. EU projects: CraNE (OOI), EUCanScreen (Korányi NKIP, NNGYK), TEHDAS2 (OKFŐ, ESZFK), ECHoS hub planned. https://crane4health.eu/partners/ ; https://eucanscreen.eu/partners/
- OMOP: EHDEN partners Semmelweis University, NEAK, University of Pécs, Bács-Kiskun and Szabolcs-Szatmár-Bereg county hospitals; Hungarian narrative review on OMOP. https://www.ehden.eu/datapartners/
- National tumour biology laboratory (NKFIH national laboratories). https://nkfih.gov.hu/for-the-applicants/national-laboratories/laboratories/national-tumor-biology

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: EESZT (since Nov 2017, operator OKFŐ): eProfil, eRecept, eBeutaló, central event catalogue, EHR document archive; HL7 V3 and FHIR in specific projects, otherwise local standards. https://tehdas.eu/app/uploads/2023/03/hungary-country-visit-factsheets-10-2022.pdf
- Oncology IT: 2019 project (23 bn HUF) to backfill EESZT and introduce a national oncology IT system across 19 county and 4 regional centres. https://infostart.hu/belfold/2019/03/20/uj-modszerrel-javitananak-az-egeszsegugyi-munkaerohianyon
- Registry exchange: electronic quarterly reports (format by agreement); nrr.hu upload. https://nrr.hu/
- Tumour-board software: Semmelweis University onkoteam rules require recording team decisions in the MedSolution clinical IT system (verified 2026-11-19) https://semmelweis.hu/jogigfoig/files/2022/05/Onkoteam_szabalyzat_hataly_2022_V_21.pdf ; Oncompass molecular decision-support software recommended by 26 Hungarian onkoteams (2020) https://index.hu/bcs/2020/07/20/rakkutatas-magyar-szoftver-oncompass/ . Structured pathology, chemotherapy system, openEHR: n/f.

#### Key organisations and people
- OOI (registry, OECI, CraNE); OKFŐ (EESZT); ESZFK (SNOMED, TEHDAS2); NEAK; Semmelweis University (BBMRI.hu, EHDEN); registry data-quality authors per 2023 evaluation. https://eld.bl.uk/catalog/100174728264_0x000001

---
