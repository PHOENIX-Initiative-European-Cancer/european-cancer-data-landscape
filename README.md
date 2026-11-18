# European Cancer Data Landscape

Country-by-country survey of the digital cancer data landscape in Europe, compiled by the
[PHOENIX Initiative](https://github.com/PHOENIX-Initiative-European-Cancer) to inform the
[HL7 Europe Common Cancer Data Model (ECCDM)](https://build.fhir.org/ig/hl7-eu/cancer-common/).

Per country: national base/core FHIR guide, oncology FHIR specifications, cancer registry input
format, terminologies and versions, public datasets, cancer research infrastructure and the digital
assets that are not FHIR. 31 countries (EU-27, Iceland, Norway, Switzerland, United Kingdom).

**Status: draft survey, 2026-11-18.** Compiled from public sources with automated research runs; every
statement on the country pages carries its source URL; "n/f" = not found; "not verified" = taken
from a search snippet because the primary site blocks automated access. Not a specification, no
profiles, no patient data. Corrections welcome as issues or pull requests.

## Layout

| path | what |
|---|---|
| `sources/survey/*.md` | the raw research reports (one per region, plus `<country>-<topic>.md` deep dives) |
| `scripts/build_pages.py` | generates the country pages, the country index, the landscape tables and the page list from the reports |
| `input/pagecontent/` | IG pages (generated country pages plus hand-written overview pages) |
| `data/*.csv` | machine-readable landscape tables |
| `sushi-config.yaml`, `ig.ini` | FHIR IG configuration (IG Publisher, `fhir.base.template`) |

## Build

```
python3 scripts/build_pages.py
./_genonce.sh          # downloads the IG Publisher into input-cache/ on first run
```

The GitHub Actions workflow builds the guide on every push to `main` and deploys it to GitHub Pages.

## Licence

CC0 1.0.
