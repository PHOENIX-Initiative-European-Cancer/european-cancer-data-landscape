### Purpose

This guide is a country-by-country survey of the digital cancer data landscape in Europe. It was compiled by the PHOENIX Initiative (the HL7 Europe cancer accelerator) to inform the editors of the [HL7 Europe Common Cancer Data Model (ECCDM)](https://build.fhir.org/ig/hl7-eu/cancer-common/): which national FHIR guides and oncology FHIR specifications exist, how cancer registries receive data today, which terminologies in which versions are in use, and what else is digital but not FHIR: registries, public datasets, research infrastructure, document standards and national platforms.

It is a survey, not a specification. It defines no profiles. It contains no patient data.

### How to read it

* [FHIR landscape](landscape-fhir.html): one row per country with the national base guide, oncology FHIR work and the registry input format.
* [Terminology landscape](landscape-terminology.html): SNOMED CT membership and edition, ICD-10 variant, ICD-O edition, TNM edition, LOINC variant and the national terminology server.
* [Registries, datasets and infrastructure](landscape-non-fhir.html): the non-FHIR side: population-based and clinical registries, open data, genomics and imaging infrastructure, EU project participation, document standards.
* [Implications for ECCDM](implications.html): what the landscape means for the common model's bindings and design.
* [Countries](countries.html): the detailed page per country. Every statement there carries its source URL.
* [Method and caveats](methodology.html): how the survey was made and how far to trust it.

### Status

Draft, compiled 2026-11-18 from public sources. Facts were collected by automated research runs and checked only where a primary source could be fetched; items marked "not verified" or "n/f" (not found) are exactly that. Corrections are welcome as issues or pull requests in the [GitHub repository](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape).

### Scope

31 countries: the 27 EU member states plus Iceland, Norway, Switzerland and the United Kingdom. Liechtenstein and the micro-states are out of scope.

### Artefacts

The guide defines one FHIR artefact, the [Surveyed jurisdictions](ValueSet-surveyed-jurisdictions.html) value set, so that the survey can be referenced from other guides. Everything else is narrative.

### Dependencies and intellectual property

{% include dependency-table.xhtml %}
{% include globals-table.xhtml %}
{% include cross-version-analysis.xhtml %}
{% include ip-statements.xhtml %}
