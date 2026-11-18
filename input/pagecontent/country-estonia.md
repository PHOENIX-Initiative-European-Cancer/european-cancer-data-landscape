### Estonia (EE)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "Estonian Base Implementation Guide" (EEBase), package `ee.fhir.base` 2.0.0 (6 Nov 2025, trial-use; must-support removed), FHIR R5 (5.0.0), publisher HL7 Estonia, canonical https://fhir.ee/base, contact fhir@tehik.ee. Three-level profiling (international, Estonian base, system-specific); TIS resources also on fhir.tehik.ee.
   https://build.fhir.org/ig/HL7EE/ig-ee-base ; https://packages.fhir.org/ee.fhir.base
2. **Oncology FHIR specifications:** "VJL – Vähiandmete juhtimislaud" (cancer data dashboard), package `ee.fhir.vjl` 0.1.0, draft (2026-10-09), FHIR R5, publisher TEHIK, canonical https://fhir.ee/vjl; depends on ee.fhir.base 2.0.0, ee.fhir.mpi 1.5.0, ee.fhir.spd; no mCODE dependency; profile EEVJLCancerDiagnosis; project (Tartu University Hospital and partners) aims to automate submission to the cancer registry. Registry data standard implemented: not stated.
   https://build.fhir.org/ig/TEHIK-EE/ig-ee-vjl/ ; https://sisu.ut.ee/estcan/cancer-data-dashboard/
3. **Cancer registry reporting:** Estonian Cancer Registry (vähiregister), controller Tervise Arengu Instituut (TAI). Statutory cancer notification (vähiteatis) submitted on paper, electronically or via the X-Road data exchange layer; 2025 draft regulation sets 30-day deadline. ICD-O-3 for topography and morphology since 2008; ICD-10 for publication.
   https://www.riigiteataja.ee/akt/123052023056.pdf ; https://en.tai.ee/images/Teatise_vormistamise_juhend.pdf ; https://en.tai.ee/en/r-and-d/registers/estonian-cancer-registry
4. **Terminologies:** SNOMED CT member January 2010; NRC TEHIK; Estonian edition URI http://snomed.info/sct/11000181102. RHK-10 (Estonian ICD-10; version not found). LOINC Estonian linguistic variant (Estonian Society for Clinical Chemistry; UMLS lists v2.77, 2024-02-27). TNM, ATC: not found. National FHIR terminology server: Ontoserver hosted by TEHIK, in production, over 400 value sets plus SNOMED CT EE+INT, publishes under https://fhir.ee/; endpoint URL not found; described in ee.fhir.ts IG (draft 1.0.0).
   https://build.fhir.org/ig/TEHIK-EE/TerminologyServices ; https://www.snomed.org/members/estonia ; https://loinc.org/?p=7910
5. **Organisations and people:** TEHIK (fhir@tehik.ee, snomed@tehik.ee), HL7 Estonia (info@hl7.ee), TAI. Named IG maintainers: not found. Igor Bossenko (TalTech) publishes on Estonian CDA-to-FHIR migration; TEHIK role not confirmed.
   https://fhir.ee/base/contact.html

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Estonian Cancer Registry (vähiregister), controller Tervise Arengu Instituut (TAI); compulsory reporting by physicians and labs; ICD-O-3 since 2008; linkage with Population and Causes of Death registries. https://en.tai.ee/en/r-and-d/registers/estonian-cancer-registry ; https://www.riigiteataja.ee/akt/123052023056.pdf
- ENCR: Estonian registry listed in ECIS/ENCR; coverage percent n/f. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- Screening registry: Estonian Cancer Screening Registry (TAI, since 2015; breast, cervical, colorectal) fed automatically from ENHIS via X-Road. https://en.tai.ee/en/r-and-d/registers/estonian-cancer-screening-registry
- Clinical quality registries: n/f; cancer data dashboard (VJL) project at Tartu. https://sisu.ut.ee/estcan/cancer-data-dashboard/
- Submission format: paper, electronic or X-Road; 30-day deadline in 2025 draft regulation; TAI notification guide. https://en.tai.ee/images/Teatise_vormistamise_juhend.pdf
- Coding: ICD-O-3, ICD-10 for publication; TNM edition n/f (study used 7th). https://medicaljournalssweden.se/actaoncologica/article/download/24331/28536/74545
- Legal basis: Public Health Act; Vähiregistri põhimäärus. https://www.riigiteataja.ee/akt/123052023056.pdf
- Researcher access: TAI register data requests; national secondary-use governance model still being defined (Ministry of Social Affairs); secondary use needs no consent except biobank. https://tehdas.eu/app/uploads/2023/03/estonia-country-visit-factsheets-10-2022.pdf

#### (b) Public datasets
- TAI Health Statistics and Health Research Database (cancer incidence PK tables, screening VSR tables). https://statistika.tai.ee/pxweb/en/Andmebaas/Andmebaas__02Haigestumus__04PahaloomulisedKasvajad/PK10.px/ ; https://statistika.tai.ee/Resources/PX/Databases/Andmebaas/02Haigestumus/07Soeluuringud/VSRinfo_en.htm
- ECIS contributor. https://ecis.jrc.ec.europa.eu/list-registries-contributing-ecis-historical-data
- NORDCAN: not a participant.
- Research access body: TEHIK/Ministry of Social Affairs (TEHDAS2 partner). https://tehdas.eu/partners/
- Synthetic datasets: n/f.

#### (c) Cancer infrastructure
- Cancer Control Action Plan 2021–2030 (15 themes incl. cancer data); mid-term evaluation April 2026 found 45% of actions not started. https://www.sm.ee/sites/default/files/documents/2026-04/Eesti%20V%C3%A4hit%C3%B5rje%20tegevuskava%202021%E2%80%932030%20vahehindamine_L%C3%95PPRAPORT_0.pdf
- Estonian Cancer Centre / ESTCAN network at University of Tartu; aims at EU CCC recognition. https://sciencebusiness.net/network-updates/university-tartu-will-be-home-estonian-cancer-centre ; https://sisu.ut.ee/estcan/
- OECI: n/f.
- Genomics: Estonian Biobank (>200,000 participants, Human Genes Research Act 2000; auto-updated from Cancer Registry); PacBio WGS of 10,000. https://ut.ee/en/content/estonian-researchers-strive-personalise-healthcare ; https://www.digitalhealth.net/2024/04/estonian-biobank-selects-pacbio-for-whole-genome-sequencing
- Biobank: University of Tartu Institute of Genomics = BBMRI-ERIC national node. https://genomics.ut.ee/en/cooperation-networks
- Imaging: EUCAIM partner Better Medicine OÜ. https://cancerimage.eu/partners/
- EU projects: EUnetCCC (ESTCAN, North Estonia Medical Centre, Tartu University Hospital, TAI); UNCAN-Connect coordinated by University of Tartu (2025–2030); EUCanScreen (TAI, University of Tartu); TEHDAS2 (Ministry of Social Affairs). https://sisu.ut.ee/estcan/eunet-ccc/ ; https://science.rsu.lv/en/projects/joint-action-on-networks-of-expertise-on-cancer/ ; https://www.unicancer.fr/en/unicancer-group/international-partners/
- OMOP/EHDEN: EHDEN data partner University of Tartu. https://www.ehden.eu/datapartners/
- National health data space: TEHIK; EHDS integration into existing ENHIS. https://tehdas.eu/app/uploads/2023/03/estonia-country-visit-factsheets-10-2022.pdf

#### (d) Digital, non-FHIR, cancer-relevant
- ENHIS/TIS national EHR with CDA and HL7 v3 documents still in use alongside FHIR. https://packages.fhir.org/jurisdictions/EE
- Patient portal: terviseportaal.ee (Patsiendiportaal); oncology-specific content n/f.
- Cancer data dashboard (VJL) and lung cancer treatment pathway pilot (Tartu). https://www.sm.ee/sites/default/files/documents/2026-04/Eesti%20V%C3%A4hit%C3%B5rje%20tegevuskava%202021%E2%80%932030%20vahehindamine_L%C3%95PPRAPORT_0.pdf
- Structured pathology, MDT software, chemotherapy system, openEHR: n/f.
- CDA-to-FHIR migration research (infectious disease system) as template. https://ws.lib.ttu.ee/digibase/en/Publ/Register/Item/337803

#### Key organisations and people
- TEHIK, TAI (Cancer Registry, Screening Registry), Ministry of Social Affairs, University of Tartu (ESTCAN, Institute of Genomics, UNCAN-Connect), Tartu University Hospital, North Estonia Medical Centre. People: Igor Bossenko (TalTech, FHIR migration research); registry leads n/f.

---
