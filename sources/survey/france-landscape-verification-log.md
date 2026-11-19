# Verification log for france-landscape.md (2026-11-19)

Method: French/English web searches, curl with browser user-agent into `scratchpad/survey/fr-nonfhir-dl/`, HTML-to-text with a script kept in `scratchpad/survey/scripts/` (run with `python3 -I`), `pdftotext -layout` for PDFs, web.archive.org for blocked sites (no archived copies existed for oeci.eu/Accreditation or cancer.fr/Media/files).

## VERIFIED (n/f replaced by fact + URL)

1. **ENCR membership of French registries**: 25 French entries with directors obtained from the ENCR contact list filtered on France (`field_country_target_id=12`, pages 0–2). https://encr.eu/encr-members-contact-list?field_country_target_id=12 (and `&page=1`, `&page=2`).
2. **OECI-accredited French centres**: full list with designation levels from the OECI accreditation site (browser cross-check by team lead 2026-11-19 confirmed the same 18 certified French centres, capture at scratchpad/verify/oeci-centres-2026-11-19.txt; the home page does not show designation types, the certified-centres page does): 15 "Comprehensive Cancer Centre with Research Excellence", 1 CCC (IUCT Oncopole), 1 Comprehensive Cancer Network (ATOP Toulouse), 1 Cancer Centre (Antoine Lacassagne), 7 "In Accreditation". https://accreditation.oeci.eu/certified-centres/ ; dated confirmations: Jean Perrin 22 Apr 2026 https://www.cjp.fr/a-la-une/actualites/actualite/le-centre-jean-perrin-accredite-comprehensive-cancer-center-par-loeci ; Baclesse https://www.baclesse.fr/en/baclesse-accredited-by-the-organization-of-european-cancer-institutes-oeci/ ; OECI Warsaw 2026 programme https://www.oeci.eu/Attachments/Warsaw_26/OECI_Warsaw_2026_Final_15_MAY.pdf
3. **CLIP² list 2024–2029**: 16 CLIP² (8 adult+paediatric) from the INCa deck presented at the phases-précoces meeting (Feb 2025), plus 2025 wave (IPC) giving 19 adult structures. https://www.phases-precoces.fr/wp-content/uploads/2025/02/3-2024_PPC_Diaporama_Actualisation.pdf ; https://alliance-cancer.org/clip2-2/ ; https://institutpaolicalmettes.fr/wp-content/uploads/2025/03/CP-IPC-labellise-CLIP2-par-l-INCa.pdf
4. **Francim base commune common variables and coding**: mandatory and complementary variables, CIM-O-3 + UICC TNM, ENCR/Francim rules, annual integration at HCL. https://www.chu-dijon.fr/registre-bourguignon-des-cancers-digestifs ; history/size (1999, 1.7 M cases 1975–2017) https://www.edimark.fr/revues/correspondances-en-onco-hematologie/n-4-septembre-2020/le-reseau-francais-des-registres-descancers-francim-un-acteur-majeur-de-lepidemiologie-des-cancers-en-france ; 32 registries evaluated by CER at 31 Dec 2023, 27 in the partnership https://registre-tumeurs-29.fr/Accueil/les-registres-des-cancers-en-france/
5. **EUCAIM French partners** confirmed on the official partner page (AP-HP, CNRS, CERF, Inria, LIMICS, Medexprim; Owkin left Dec 2023). https://cancerimage.eu/partners/
6. **canSERV French participants**: IARC/CIRC Lyon, ECRIN, EMBRC-ERIC. https://cordis.europa.eu/project/id/101058620
7. **UNCAN-Connect French partner**: Alia Santé (no French cancer centre or INCa). https://www.srdc.com.tr/rndprojects/uncan-connect/
9. **Décret 2025-1366 full text** (browser check by team lead 2026-11-19): https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053177576 ; confirmed articles R. 1415-2-1 to R. 1415-2-6, nine sources, 11 data categories, NIR/IPP/episode identifiers, retention 24 months / 20 years / 8 months logs, scientific and ethics committee, INCa-run information system for local registries with annual transmission to the base commune, no data format or interoperability standard named. Report updated; the decree now replaces the CNIL mirror as primary source for decree facts.
8. **HDAB (ORAD) designation under EHDS**: none yet; PDS expected, legislative vehicle 2026, EHDS applies 26 Mar 2027. https://gnius.esante.gouv.fr/sites/default/files/2025-11/English%20version_The%20French%20National%20Strategy%20for%20Artificial%20Intelligence%20and%20Health%20Data.pdf ; https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cenum/l17cenum2526033_compte-rendu.pdf ; https://www.donneespersonnelles.fr/espace-europeen-donnees-sante ; https://esante.gouv.fr/doctrine/usage-secondaire-donnees-sante

## CORRECTED (old vs new)

1. **Unicancer OMOP**: old "n/f" → new: no production OMOP conversion exists; the 2024 ConSoRe paper names bridging the ConSoRe common data model to OMOP-CDM as a planned next step, and the Centre Léon Bérard 2024 paper states the goal to align OSIRIS with OMOP and FHIR. https://pdfs.semanticscholar.org/9d0a/3840b7bdf51ba2869686e1b438c2099e1294.pdf ; https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0000415
2. **OECI**: old partial list (6 names, status uncertain) → new full list of 25 French entries with designation levels (see VERIFIED 2). Gustave Roussy, Curie, Léon Bérard, Paoli-Calmettes, Bergonié, ICO etc. are "CCC with Research Excellence"; Lacassagne is "Cancer Centre"; CGFL is "In Accreditation" (earlier search result said "Cancer Centre").
3. **CLIP²**: old "list not retrievable, 2024–2029 labels e.g. Lacassagne, IPC" → new: 16 CLIP² labelled July 2024 (named), 19 adult structures after the 2025 wave, 8 paediatric.
4. **Screening IS ("Siden")**: old plain n/f → new: regulatory architecture from the arrêté of 16 Jan 2024 (one regional business software + one regional database per CRCDC; national INCa IS for cervical screening), vendor example OSI Santé Zeus; the name "Siden" itself remains unfound. https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049025564 ; https://www.osi-sante.fr/Depistage/
5. **"Oncodata"**: old n/f → new: no French platform of that name; nearest is Unicancer/Roche Onco Data Hub (ODH). https://www.unicancer.fr/en/programs/onco-data-hub/
6. **SeqOIA report**: old n/f → new (partial): dematerialised pathway via SPICE e-prescription tool (spice.aphp.fr), result returned as a "compte-rendu d'examen de biologie médicale" to downstream RCPs. Machine-readable format still unfound. https://laboratoire-seqoia.fr/nos-activites/ ; https://fimarad.org/wp-content/uploads/2021/10/Pre%CC%81sentation-SeqOIA-Michel-Vidaud.pdf

## STILL NOT FOUND

1. **Francim base commune file format / ICD-O-3 edition / multiple-primary rule version**: tried francim-reseau.org (subpages 404), Wikipedia FRANCIM, Edimark 2020 article, registry sites (Dijon, Finistère, Bas-Rhin methodology page 404), cancer.fr readme 2018, searches on "dictionnaire des variables" Francim. Only the common-variable list (Dijon) exists publicly.
2. **IACR membership of French registries**: IACR member directory requires login (cinportal.iarc.fr); iacr.com.fr shows only publications; searches returned nothing.
3. **Francim president / bureau**: not on francim-reseau.org, Wikipedia, Edimark, registry sites; searches with candidate names returned nothing.
4. **"Siden"**: no hit in any French source (searches with CRCDC, Assurance maladie, vendor names).
5. **"Oncodata"** as a named French platform: no hit beyond Onco Data Hub.
6. **SeqOIA/AURAGEN machine-readable report format**: SeqOIA site, Vidaud deck, PFMG2025 documents describe process only.
7. **French cancer centres as EUCAIM data holders**: cancerimage.eu partner page lists no cancer centre; data-holder roster not public.
8. **ECHoS French consortium partner**: not confirmed (INCa runs "Hub Cancer France" but the ECHoS partner list was not retrieved).

## NEEDS BROWSER (blocked or JS-rendered for automated fetch)

- esante.gouv.fr was in maintenance on 2026-11-19 ("Page de maintenance ANS"), so none of the ANS pages below could be verified in the browser either; retry later.
- https://esante.gouv.fr/interoperabilite/ci-sis/espace-publication (CI-SIS publication space, cancer volets status table) — curl returns 776-byte challenge page.
- https://esante.gouv.fr/volet-frcp-fiche-de-reunion-de-concertation-pluridisciplinaire and https://esante.gouv.fr/volet-cancer-pps-programme-personnalise-de-soins-en-cancerologie — same block.
- https://esante.gouv.fr/sites/default/files/media/document/20260519%20-%20support%20HDH.pdf (PDS presentation May 2026 on ORAD/EHDS) — not fetched.
- https://gnius.esante.gouv.fr/sites/default/files/2025-11/English%20version_The%20French%20National%20Strategy%20for%20Artificial%20Intelligence%20and%20Health%20Data.pdf — returns HTML instead of PDF via curl.
- https://www.cancer.fr/Media/files/liste-des-centres (CLIP² list), https://www.e-cancer.fr/Professionnels-de-sante/Les-therapies-ciblees/Essais-cliniques-et-therapies-ciblees/Les-CLIP2 , https://www.e-cancer.fr/Institut-national-du-cancer/Appels-a-projets/Appels-a-projets-en-cours/CLIP2-2025-2029 , https://www.cancer.fr/content/download/141527/file/PANOKFR2026_Panorama%20des%20cancers%202026.pdf?version=3 , https://www.cancer.fr/content/download/124863/file/Cahier%20des%20charges%20fonctionnel_PDE-MES-PPS-CANCER_2026.04_ERRATUM_VF.pdf?version=3 — cancer.fr returns 315-byte challenge page to curl (the HDH and Senate PDFs were fetched fine).
- RESOLVED 2026-11-19: decree full text verified in the browser at https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053177576 (the id 052859580 tried by curl was wrong; aphp returned nothing).
- https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049025564 (arrêté 16 Jan 2024 on screening programmes, annex on information systems).
- https://www.oeci.eu/MemberList.aspx (fetched, 1.4 MB, not parsed; the accreditation site sufficed) and oeci.eu/Accreditation/* (404 / not archived).
- https://cinportal.iarc.fr (IACR registry portal, login).
- https://www.sciencedirect.com/science/article/pii/S2949820125005442 (CDISC-SDTM to OMOP conversion of a French oncology RWD database; affiliation unknown) — text not extractable.
- https://www.esante-occitanie.fr/app/uploads/2025/12/Presentation-DCC-ATs.pdf (404) and https://www.francim-reseau.org/le-reseau , /la-base-commune (404).
