### Lithuania (LT)

Region: Nordic and Baltic. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base IG:** "Lithuanian Base Implementation Guide" (LTBase), package `lt.hl7.fhir.base` 0.3.0 (DSTU 1 draft, "not ready for production"), FHIR R5 (5.0.0), canonical https://hl7.lt/fhir/base, published via HL7 Lithuania registry (hl7.lt, GitHub HL7LT) by the Lithuanian Medical Library. Legacy national ESPBI system (Registrų centras) uses DSTU1 Atom feeds (SKL01–03) and an eLab FHIR IG with ESPBI identifiers.
   https://hl7.lt/fhir/base/0.3.0/en/index.html ; https://hl7.lt/ ; https://specialistas-pub.esveikata.lt/dp/elab/iframe/fhir-ig/StructureDefinition-lt-patient-definitions.html
2. **Oncology FHIR specifications:** ADP early-diagnosis programme IGs: `lt.hl7.fhir.lung` (LDCT screening, Lung-RADS v2022), `lt.hl7.fhir.colorectal`, `lt.hl7.fhir.cervical`, `lt.hl7.fhir.breast`, `lt.hl7.fhir.prostate`; all 0.0.1 CI-build drafts (2026-09), FHIR R5, publisher Lithuanian Medical Library; depend on lt.hl7.fhir.base, lt.hl7.fhir.lab (pathology report, ICD-O-3 morphology, prostate pTNM, AJCC grade), lt.hl7.fhir.eu and hl7.fhir.eu.base-r5 0.1.0. No mCODE dependency. They implement national screening datasets, not the cancer registry standard.
   https://build.fhir.org/ig/HL7LT/ig-lt-lung/en/index.html ; https://build.fhir.org/ig/HL7LT/ig-lt-colorectal/en/terminology.html ; https://build.fhir.org/ig/HL7LT/ig-lt-lab/en/terminology.html
3. **Cancer registry reporting:** Lithuanian Cancer Registry (Vėžio registras) run by Nacionalinis vėžio institutas (NVI); primary source is form Nr. 090/a (notice of first-diagnosed oncological disease); NVI's 2025 report states registration is now fully electronic after system integrations; ICD-O-3 for topography/morphology.
   https://nvi.lt/wp-content/uploads/2026/04/2-priedas.-NVI_Ataskaita_2025_26-02-26.pdf ; https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
4. **Terminologies:** SNOMED CT charter member 2007; NRC Lithuanian Library of Medicine (Ministry of Health); 40,000 concepts translated 2015. TLK-10-AM (ICD-10-AM) introduced by Health Minister order V-164 of 23 February 2011, used as interim since 2019 and still referenced in 2026 health-fund documents; specific ICD-10-AM edition still not found; TLK-11 mapping planned https://e-seimas.lrs.lt/rs/legalact/TAD/TAIS.211963/ . LOINC and ICD-O-3 used in lab IG; ATC: not found; TNM edition: not found. Terminology server: https://tx.hl7.lt/fhir/ (HL7 Lithuania); national terminology server adaptation for TLK-11 planned.
   https://snomed.org/snomed-in-action/lithuanian-nrc-library-of-medicine ; https://e-seimas.lrs.lt/rs/legalact/TAD/e1ba28a055e911f0a19dcea0bcc863ad/ ; https://build.fhir.org/ig/HL7LT/ig-lt-lab/en/terminology.html
5. **Organisations and people:** Lithuanian Medical Library (IG publisher, SNOMED NRC), HL7 Lithuania (hl7.lt), Registrų centras (ESPBI), NVI. Cancer registry director: Giedrė Smailytė (ENCR registry page) (verified 2026-11-19) https://encr.eu/node/262 . Named IG maintainers: still not found.

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Lithuanian Cancer Registry at Nacionalinis vėžio institutas (NVI); modernised registry with open data portal (Dec 2025); fully electronic registration per NVI 2025 report. https://encr.eu/node/262 ; https://ground.news/article/since-1978-67-million-cancer-cases-in-lithuania-new-tool-for-disease-control-introduced ; https://nvi.lt/wp-content/uploads/2026/04/2-priedas.-NVI_Ataskaita_2025_26-02-26.pdf
- ENCR member registries: Lithuanian Cancer Registry (director Dr. Giedre Smailyte). Institute still listed under its former name, Institute of Oncology, Vilnius University (now NVI). Source: https://www.encr.eu/encr-members-contact-list (read 2026-11-19) (verified 2026-11-19)
- Source document: form Nr. 090/a (first-diagnosis notice). https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
- Screening: ESPBI subsystem for prevention programmes (breast, cervical, colorectal, prostate) built 2023–2025 (Kaunas Clinics project). https://kaunoklinikos.lt/media/file/Prevencini%C5%B3%20program%C5%B3%20vykdymo,%20kokyb%C4%97s%20u%C5%BEtikrinimo%20ir%20kokyb%C4%97s%20kontrol%C4%97s%20ESPBI%20IS%20posistem%C4%97s%20k%C5%ABrimas.pdf
- Clinical quality registries: n/f.
- Coding: ICD-O-3 topography/morphology; TLK-10-AM diagnoses; TNM edition still n/f (no Lithuanian registry coding manual located). https://www.nvi.lt/uploads/pdf/Vezio%20registras/Vezys_lietuvoje_2012.pdf
- Legal basis: mandatory statistical form 090/a (Ministry of Health order). https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202016.pdf
- Researcher access: procedure n/f; State Data Agency's Lithuanian Digital Health Platform onboarded in DARWIN EU. https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf

#### (b) Public datasets
- NVI "Vėžys Lietuvoje" annual reports; new open data portal. https://www.nvi.lt/uploads/pdf/Vezio%20registras/V%C4%97%C5%BEys%20Lietuvoje%202017.pdf
- ECIS contributor; CancerWatch project participation (Ministry of Health, NVI). https://sam.lrv.lt/en/during-the-visit-to-japan-the-focus-was-on-patient-safety/to-improve-cancer-data-quality-and-strengthen-cancer-control-europe-is-beginning-to-implement-the-cancerwatch-program-Y3mw
- IHE Cancer Dashboard Lithuania (2025). https://ihe.se/app/uploads/2025/01/IHE-Cancer-Dashboard-Lithuania_.pdf
- Research access body: Valstybės duomenų agentūra (TEHDAS2 partner, DARWIN EU). https://tehdas.eu/partners/
- Synthetic datasets: n/f.

#### (c) Cancer infrastructure
- National Cancer Prevention and Control Programme 2014–2025; successor in development. https://ihe.se/app/uploads/2025/01/IHE-Cancer-Dashboard-Lithuania_.pdf ; https://www.iccp-portal.org/sites/default/files/plans/LTU_2020.pdf
- OECI: NVI accredited Clinical Cancer Centre since 2013; NVI and VU Santaros Klinikos seeking joint CCC accreditation. OECI accredited-centres list (2026-11-19) carries a 'National Cancer Institute' entry without country, consistent with NVI Vilnius (no other Lithuanian entry) (verified 2026-11-19) https://accreditation.oeci.eu/ (list as shown 2026-11-19, saved at scratchpad/verify/oeci-centres-2026-11-19.txt). EUnetCCC EU-Designated CCCs (first 30, 23 Feb 2026): Klaipėda University Hospital, Vilnius University Hospital Santaros Clinics with National Cancer Centre, and LSMU Kaunas Clinics (verified 2026-11-19) https://www.kpmi.lu.lv/jaunumi/zinas/zina/t/107989/ https://www.vu.lt/en/news-events/news/vu-santaros-klinikos-and-the-national-cancer-institute-will-cooperate-in-the-treatment-of-oncological-diseases-and-the-development-of-oncology-science-the-aim-is-to-become-a-centre-for-comprehensive-cancer-care
- Genomics: 1+MG participation via Santaros Klinikos biobank; €7.6M for GDI 2023–2026. https://oecd.ai/en/dashboards/policy-initiatives/1-million-genomes-vilnius-university-hospital-vul-santaros-klinikos
- Biobank: BBMRI-ERIC full member 2024; national node via NVI; Santaros, LSMU/Kaunas biobanks. https://www.bbmri-eric.eu/national-nodes/lithuania/ ; https://nvi.lt/biobank-projects
- Imaging: EUCAIM n/f.
- EU projects: ECHoS (LSMU Kaunas Clinics, PI); JANE-2 (Vilnius University Hospital Santaros Klinikos); EUCanScreen (Ministry of Health, Vilnius and Kaunas hospitals); TEHDAS2 (State Data Agency). https://lsmu.lt/en/research-and-innovations/projects/international-projects/establishing-of-cancer-mission-hubs-networks-and-synergies/
- OMOP/EHDEN: DARWIN EU partner Lithuanian Digital Health Platform (State Data Agency). https://www.ema.europa.eu/system/files/documents/other/data-partners-onboarded-darwin-eu-phase-i-ii-iii-iv_en.pdf
- National health data space: State Data Agency platform; openEHR pilot for health information systems. https://discourse.openehr.org/uploads/short-url/3r2W1AWAHYxZ2AnvTJyCdLuq2Zw.docx

#### (d) Digital, non-FHIR, cancer-relevant
- ESPBI IS (Registrų centras): DSTU1 Atom feeds (SKL01–03), patient portal esveikata.lt and mobile app; prevention-programme subsystem. https://www.esveikata.lt/en/en/ehealth ; https://esveikata.lt/bylos/failai/Mobilioji%20program%C4%97l%C4%97/Esveikatos%20naudojo%20vadovas-v1.1.pdf
- openEHR: national openEHR pilot/tender for health information systems. https://discourse.openehr.org/uploads/short-url/3r2W1AWAHYxZ2AnvTJyCdLuq2Zw.docx
- TLK-10-AM classification; TLK-11 mapping planned. https://e-seimas.lrs.lt/rs/legalact/TAD/e1ba28a055e911f0a19dcea0bcc863ad/
- Structured pathology: LT Lab IG pathology profiles (ICD-O-3, pTNM) are FHIR; non-FHIR pathology standard n/f.
- MDT software, chemotherapy system: n/f.

#### Key organisations and people
- NVI (cancer registry, biobank node), Ministry of Health, Registrų centras (ESPBI), Valstybės duomenų agentūra, VU Santaros Klinikos, LSMU Kaunas Clinics, Lithuanian Medical Library (SNOMED NRC, HL7 IGs). People: Giedrė Smailytė (Director, Lithuanian Cancer Registry, ENCR page) (verified 2026-11-19) https://encr.eu/node/262 ; Laima Ambrozaitytė (Genome of Europe contact, Santaros) https://genomeofeurope.eu/partners/ .
