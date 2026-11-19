### Iceland (IS)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** none ("not yet available"). Standards body Stafræn heilsa (Digital Health, under Ministry of Health, operational 2 January 2026). FHIR R4 and R5 in limited use; specifications in development for prescriptions/pharmacy and allergy intolerance, based on European IGs.
   https://packages.fhir.org/jurisdictions/IS ; https://island.is/s/stafraen-heilsa
2. **Oncology FHIR specifications:** not found.
3. **Cancer registry reporting:** Icelandic Cancer Registry (Krabbameinsskrá), founded 1954, operated by the Icelandic Cancer Society's research centre as one of the Directorate of Health's (Embætti landlæknis) health registries under Act 41/2007; mandatory reporting; coding follows IARC/ENCR rules. Transmission format: not found.
   https://www.krabb.is/rannsoknasetur/en/activities/about-icr/ ; https://www.laeknabladid.is/media/2024-06/f02.pdf
4. **Terminologies:** SNOMED CT member since September 2011; Directorate of Health holds national licence; used in pathology, microbiology, virology, immunology. ICD-10 Icelandic translation (1996), current editions 2014, published on SKAFL.is; NCSP listed. ICD-O coding rules confirmed by the registry (Læknablaðið 2024; edition number not stated) (verified 2026-11-19) https://www.laeknabladid.is/media/2024-06/f02.pdf ; TNM, LOINC, ATC: not found. National FHIR terminology server: in development.
   https://www.snomed.org/members/iceland ; https://island.is/en/classification-system-in-health-services/icd-10 ; https://island.is/flokkunarkerfi-i-heilbrigdisthjonustu/skafl.is
5. **Organisations and people:** Stafræn heilsa (director Sigurður Þórarinsson), Embætti landlæknis, Krabbameinsfélagið: Sigríður Gunnarsdóttir heads Rannsóknasetur – Krabbameinsskrá per the 2025 annual report, Laufey Tryggvadóttir is registry epidemiologist (verified 2026-11-19) https://www.krabb.is/media/arsskyrsla-krabbameinsfelagsins-2025.pdf . HL7 affiliate or FHIR maintainer: still not found (no Icelandic HL7 affiliate located; Stafræn heilsa is the standards body).
   https://island.is/s/stafraen-heilsa/frett/sigurdur-thorarinsson-skipadur-forstoedumadur-stafraennar-heilsu ; https://medicaljournalssweden.se/actaoncologica/article/view/24912

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Icelandic Cancer Registry (Krabbameinsskrá), founded 1954, operated by the Icelandic Cancer Society research centre on behalf of the Directorate of Health (Act 41/2007); covers >99% of cancers; registration since 1955. https://www.krabb.is/rannsoknasetur/en/activities/about-icr/ ; https://www.laeknabladid.is/media/2024-06/f02.pdf
- ENCR/IACR: ANCR member; ENCR registry page still n/f (ENCR list is script-rendered; needs browser). https://catalogues.ema.europa.eu/network/2221158
- Clinical quality registries: cancer quality registration started 1998 with prostate cancer and was expanded in 2010 (Læknablaðið) (verified 2026-11-19) https://www.laeknabladid.is/media/2020-09/u09.pdf
- Screening: Samhæfingarstöð krabbameinsskimana (Cancer Screening Coordination Centre, Heilsugæsla höfuðborgarsvæðisins) runs breast, cervical and (from Feb 2025) colorectal screening; results via Heilsuvera. https://island.is/s/hh/samhaefingarstod-krabbameinsskimana ; https://island.is/s/hh/frett/langthradur-afangi-ad-hefja-skimun-fyrir-ristilkrabbameini-28-02-2025
- Submission format: most reports arrive electronically from pathology laboratories; coverage over 99% of diagnoses (Læknablaðið 2024) (verified 2026-11-19) https://www.laeknabladid.is/media/2024-06/f02.pdf ; private clinicians report only prostate cancers. https://medicaljournalssweden.se/actaoncologica/article/view/24912
- Coding: ICD-O rules per registry (edition number not stated), IARC/ENCR rules, ICD-10 for publication (verified 2026-11-19) https://www.laeknabladid.is/media/2024-06/f02.pdf ; TNM still n/f. https://medicaljournalssweden.se/actaoncologica/article/view/24912
- Researcher access: application form plus ethics-approved research plan to the Cancer Registry; family database requires National Bioethics Committee permission; >600 studies. https://www.krabb.is/rannsoknasetur/en/activities/about-icr/

#### (b) Public datasets
- NORDCAN 2.0 participant (Iceland included). https://www.iarc.who.int/news-events/iarc-and-partners-launch-nordcan-2-0-comparable-cancer-statistics-for-the-nordic-countries
- Cancer Society publishes five-year average statistics. https://www.krabb.is/rannsoknasetur/en/activities/about-icr/
- ECIS contributor: n/f.
- Research access body (EHDS): Directorate of Health (TEHDAS2 partner). https://tehdas.eu/partners/
- Synthetic datasets, national catalogue: n/f.

#### (c) Cancer infrastructure
- National plan: government cancer action plan approved by parliament June 2025 (16 measures); Cancer Council established. https://island.is/en/news/new-cancer-council
- Landspítali Cancer Center established 2025; standardised care pathways; accreditation preparation. https://island.is/en/o/landspitali/landspitali-cancer-center ; https://island.is/en/o/landspitali/landspitali-cancer-center/standardized-cancer-care-pathways
- OECI: Landspítali Cancer Center (2025) states it operates per OECI standards and prepares accreditation; no Icelandic centre on the OECI accredited-centres list (2026-11-19) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt); membership still n/f https://island.is/en/o/landspitali/landspitali-cancer-center
- Genomics: deCODE genetics (>2/3 of adults participating by 2019); Iceland is not a 1+MG signatory and has no Genome of Europe partner (absent from partner list) (verified 2026-11-19) https://genomeofeurope.eu/partners/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7115898 https://www.decode.com/?p=2007
- Biobank: Iceland is neither BBMRI-ERIC member nor observer (2025 annual report); Landspítali runs licensed biobanks (LLR, LLSV) (verified 2026-11-19) https://www.bbmri-eric.eu/annual_report_2025_singlepages/ ; https://island.is/en/o/landspitali/biobanks-of-landspitali
- Imaging: EUCAIM n/f.
- EU projects: EUCanScreen (Heilsugæsla höfuðborgarsvæðisins); TEHDAS2 (Directorate of Health); EUnetCCC participant Landspítali University Hospital (verified 2026-11-19) https://sciensano.be/sites/default/files/eunetccc_participants_list_-_edit.pdf ; ECHoS still n/f. https://island.is/en/o/hh/eu-can-screen ; https://tehdas.eu/partners/
- OMOP/EHDEN: n/f.
- National health data space: Stafræn heilsa (from Jan 2026) as development and service centre; draft Digital Health Act (consultation Aug 2026). https://island.is/s/stafraen-heilsa/frett/droeg-ad-frumvarpi-um-stafraena-heilsu-til-umsagnar

#### (d) Digital, non-FHIR, cancer-relevant
- Patient portal: Heilsuvera (screening invitations and results; cancer plan calls for interactive symptom-monitoring portal). https://island.is/s/hh/frett/bod-og-nidurstodur-vegna-krabbameinsskimana-a-heilsuveru-14-03-2025 ; https://island.is/en/o/sak/news/rafraen-samskiptagatt-styrkir-thjonustu-vid-sjuklinga-i-veikindum
- EHR: Saga (Origo/Helix) nationwide; Hekla health network; prescription gateway. https://island.is/s/stafraen-heilsa/innvidir-og-kerfi
- Classification distribution: SKAFL.is (ICD-10, NCSP). https://island.is/flokkunarkerfi-i-heilbrigdisthjonustu/skafl.is
- Structured pathology: SNOMED used in pathology registration. https://island.is/en/classification-system-in-health-services
- MDT software, chemotherapy system, openEHR: n/f.

#### Key organisations and people
- Embætti landlæknis, Stafræn heilsa (Sigurður Þórarinsson), Krabbameinsfélagið (Sigríður Gunnarsdóttir, head of Rannsóknasetur – Krabbameinsskrá per 2025 annual report; Laufey Tryggvadóttir, epidemiologist) (verified 2026-11-19) https://www.krabb.is/media/arsskyrsla-krabbameinsfelagsins-2025.pdf , Landspítali Cancer Center, Heilsugæsla höfuðborgarsvæðisins, deCODE (Kári Stefánsson). https://island.is/s/stafraen-heilsa/frett/sigurdur-thorarinsson-skipadur-forstoedumadur-stafraennar-heilsu

---
