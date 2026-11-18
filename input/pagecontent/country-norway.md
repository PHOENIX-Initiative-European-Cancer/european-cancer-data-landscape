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
