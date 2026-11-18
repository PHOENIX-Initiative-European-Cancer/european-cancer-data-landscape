### Slovenia (SI)

Region: Central and Eastern Europe. Sources: see the URLs on each statement; raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).

### FHIR guides, registry format and terminologies

1. **National base/core FHIR IG:** a national core IG exists, used for a limited set of cases, shared with national stakeholders via Simplifier but not fully public; FHIR R4 (some R4B). Package id, version, canonical: not found. NIJZ is the key national body; FHIR advised, not mandated (Healthcare Databases Act). Slovenia has approved specifications in the FHIR Community Process.
   https://api.simplifier.net/jurisdictions/SI
2. **Oncology FHIR specifications:** none found. mCODE reuse: not found.
3. **Cancer registry reporting standard:** Register raka Republike Slovenije at Onkološki inštitut Ljubljana (since 1950; legal basis Ur. l. RS 47/15, 31/18). Traditional form "Prijavnica rakave bolezni"; since 2019 "active registration" in which hospital information systems prepare and send lists of registrable patients; passive paper reporting being phased out. No FHIR interface found.
   https://www.onko-i.si/rrs/register-raka-republike-slovenije
4. **Terminologies:** SNOMED CT: member since Jan 2010 (Ministry of Health; GA rep Iztok Štotl, Member Forum Alen Vrečko of NIJZ); 2024 advisory-council minutes discuss SNOMED rollout, Slovene translation and terminology servers; national edition: not found. ICD-10: MKB-10-AM version 11 since 1 Jan 2023 (NIJZ; v6 before). ICD-O-3, TNM edition, LOINC, ATC variant: not found. Terminology server: national FHIR terminology server in development.
   https://www.snomed.org/members/republic-of-slovenia ; https://gov.si/assets/ministrstva/MZ/DOKUMENTI/4-ZBIRKE/RSK/RSK-za-informatiko-v-zdravstvu/2024/Zapisnik-8.-seje-RSK-za-informatiko-v-zdravstvu-3.-12.-2024.pdf ; https://podatki.nijz.si/docs/Opomba_MKB-10-AM_v6_v11.pdf ; https://api.simplifier.net/jurisdictions/SI
5. **Organisations and people:** NIJZ, HL7 Slovenia (site hl7.si unreachable at survey time), Onkološki inštitut Ljubljana. Brane Leskošek (University of Ljubljana Faculty of Medicine / HL7 Slovenia); Alen Vrečko (NIJZ, SNOMED).
   https://api.simplifier.net/jurisdictions/SI ; https://www.snomed.org/members/republic-of-slovenia

### Registries, public datasets, infrastructure and non-FHIR digital assets

#### (a) Cancer registries
- Population-based: Register raka Republike Slovenije, Onkološki inštitut Ljubljana (since 1950); member of IACR since 1968 and ENCR from its start; coverage 100% (ECIS). https://www.onko-i.si/rrs/register-raka-republike-slovenije ; https://ecis.jrc.ec.europa.eu/pdf/Prevalence_List_of_cancer_registries.pdf
- Legal basis: Ur. l. RS 47/15, 31/18 (ZZPPZ). https://www.onko-i.si/rrs/register-raka-republike-slovenije
- Submission: paper "Prijavnica rakave bolezni" being phased out; since 2019 active registration from hospital information systems (lists of registrable patients); format n/f. https://www.onko-i.si/rrs/register-raka-republike-slovenije
- Clinical registries: national clinical registries and OI hospital cancer registry hosted at OI Ljubljana. https://www.onko-i.si/rrs
- Screening registries: ZORA (cervical), DORA (breast), Svit (colorectal) programmes under DPOR; registries at OI/NIJZ. https://www.gov.si/novice/2021-12-23-sprejet-je-drzavni-program-obvladovanja-raka-do-leta-2026/
- Variable dictionary (ICD-O/TNM editions): n/f. Diagnoses in NIJZ databases coded MKB-10-AM v11 since 2023. https://podatki.nijz.si/docs/Opomba_MKB-10-AM_v6_v11.pdf
- Researcher access: request form to Register raka (register@onko-i.si), paid for larger extracts; NIJZ researcher application form. https://www.onko-i.si/rrs/register-raka-republike-slovenije ; https://nijz.si/sites/www.nijz.si/files/uploaded/ob_vloga_raziskovalci_nijz_v_1-1.pdf

#### (b) Public datasets
- SLORA (slora.si) interactive cancer data portal; annual "Rak v Sloveniji". https://www.onko-i.si/rrs
- NIJZ data portal podatki.nijz.si (px/xlsx/csv exports). https://podatki.nijz.si/docs/NAVODILA.pdf
- SI-SUD project: metadata catalogue, data access platform, secure processing environment for EHDS secondary use (planned). https://nijz.si/wp-content/uploads/2025/05/Predstavitev_SI_SUD_projekt_GA_Ljubljana_final.pdf
- ECIS: Slovenian registry contributes (100%). Synthetic data: n/f. TEHDAS2 partner: NIJZ. https://tehdas.eu/tehdas2/partners/

#### (c) Cancer infrastructure
- Plan: Državni program obvladovanja raka 2022–2026 (adopted Dec 2021, managed by OI Ljubljana from 2022); draft DPOR 2027–2036. https://www.gov.si/novice/2021-12-23-sprejet-je-drzavni-program-obvladovanja-raka-do-leta-2026/ ; https://www.gov.si/assets/ministrstva/MZ/DOKUMENTI/DJZ-Preventiva-in-skrb-za-zdravje/rak/Predlog-Strateski-dokument-Drzavnega-programa-obvladovanja-raka-2027-2036.pdf
- OECI: OI Ljubljana listed as OECI member; accreditation status inconsistent across sources. https://en.wikipedia.org/wiki/Organisation_of_European_Cancer_Institutes
- Genomics: 1+MG original signatory (2018); GDI node operational (UL MF, UKC Ljubljana, UM); 1+MGenom-SI national genomics infrastructure funded Aug 2026 (~3.6 m EUR). https://www.gov.si/en/news/2026-08-14-eu-funding-for-the-establishment-of-national-research-infrastructure-on-genomics/
- Biobank: BBMRI.si (UM, UL, UP, NIB, UKC Maribor, Klinika Golnik; 6 biobanks; director Urban Bren). https://www.bbmri-eric.eu/national-nodes/
- Imaging/EUCAIM: none listed. EU projects: CraNE (coordinator NIJZ, OI affiliated), EUCanScreen (OI Ljubljana, NIJZ), JANE-2 (NIJZ, Tit Albreht), EUnetCCC (NIJZ), TEHDAS2 (NIJZ), ECHoS hub. https://crane4health.eu/partners/ ; https://nijz.si/en/projects/jane-2/ ; https://nijz.si/en/projects/eunetccc-ja/
- OMOP: no EHDEN partner listed. https://www.ehden.eu/datapartners/

#### (d) Digital, non-FHIR, cancer-relevant
- National EHR: eZdravje (NIJZ): CRPP central patient data register (openEHR + FHIR, Better platform), zVEM portal, eNaročanje, eRecept; CRPP access authorisation rules (Oct 2025). https://ezdrav.si/wp-content/uploads/2025/10/Pooblastila_za_dostop_do_CRPP_opis_in_navodila_V02.pdf ; https://www.better.care/news/institute-of-oncology-ljubljana-will-implement-a-postmodern-ehr-based-on-better-platform/
- openEHR: OI Ljubljana implementing openEHR-based EHR (Better) synchronised with national CRPP; openEHR patient summary template in national solution. https://discourse.openehr.org/t/rare-disease-model-in-openehr/287
- Registry exchange: active registration lists from hospital systems (format n/f).
- Structured pathology, tumour-board software, chemotherapy system: n/f.
- Strategy items: Healthcare Digitalisation Act (upcoming), National Interoperability Framework. https://api.simplifier.net/jurisdictions/SI

#### Key organisations and people
- OI Ljubljana (Register raka: register@onko-i.si; DPOR management); NIJZ (eZdravje, CraNE, JANE-2: Tit Albreht; SNOMED: Alen Vrečko); Better d.o.o. (openEHR platform); UL MF (genomics; Brane Leskošek HL7 SI).

---
