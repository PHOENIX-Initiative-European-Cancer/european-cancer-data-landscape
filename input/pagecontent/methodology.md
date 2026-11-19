### Method

The survey was produced on 2026-11-18 in three passes, each run as parallel research tasks per region (DACH and Benelux; Southern Europe; Nordic and Baltic; Central and Eastern Europe; Islands) with dedicated deep dives for Greece and France:

1. **FHIR and terminology pass.** For each country: national base or core FHIR guide (package id, version, FHIR release, publisher, dependency on HL7 Europe Base), oncology FHIR specifications (and whether they reuse mCODE), the cancer registry's input format, the terminologies in use with versions, and the responsible organisations and people. Sources: packages.fhir.org and Simplifier package feeds, the guides' own package-list.json, GitHub repositories (read-only inspection of sushi-config and FSH files), national agency pages, SNOMED International member pages, registry methodology reports.
2. **Non-FHIR landscape pass.** For each country: population-based, clinical and screening cancer registries with coverage and submission format; public datasets and data access bodies; cancer infrastructure (institutes, comprehensive cancer centres, genomics and imaging programmes, biobanks, EU project participation, OMOP adoption); and digital assets that are not FHIR (document standards, tumour-board systems, pathology reporting, EHR portals, strategies).
3. **Verification pass (2026-11-19).** Every statement marked "n/f", "not verified" or taken from a search snippet was re-checked by the agent that wrote it, with national-language searches, primary documents, archived copies and direct registry or terminology-server queries; pages that block automated access were read in a real browser by the editor, except where a human check (CAPTCHA) or a certificate warning would have had to be bypassed. Corrected statements carry "(verified 2026-11-19)"; the per-item outcomes are on the [Verification pass](verification.html) page.
4. **Consolidation.** The regional reports were merged into the landscape tables and the implications page. The per-country pages are generated verbatim from the reports by `scripts/build_pages.py`; the reports themselves are kept in `sources/survey/`.

### Caveats

* Every statement in the country pages carries the URL it was taken from. Where the primary site refused automated access (for example digital.nhs.uk, hse.ie, hl7belgium.org, dhir.gov.mt), the statement is marked "not verified" and comes from search snippets or secondary sources.
* "n/f" means the item was not found in a public source within the research pass, not that it does not exist.
* Versions are those visible on the package registries and agency pages on the survey date. Ballot and CI builds change weekly.
* Names of people are limited to public roles (chairs, named contacts, maintainers) as published by the organisations themselves.
* The survey was compiled with the help of automated research agents. Treat it as a starting point for the editors' own verification, not as an authoritative reference.

### Reproducing and updating

The repository holds the raw reports (`sources/survey/*.md`), the generated pages (`input/pagecontent/`), the CSV extracts (`data/`) and the generator script. To update a country, edit its section in the regional report or add a dedicated `<country>-<topic>.md` file, run `python3 scripts/build_pages.py`, and rebuild the guide with the IG Publisher (`./_genonce.sh`).
