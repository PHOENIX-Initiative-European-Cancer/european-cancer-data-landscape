#!/usr/bin/env python3
"""Generate the per-country pages, the country index, the landscape tables and the
page list in sushi-config.yaml from the research reports in sources/survey/.

Idempotent: run it after every change to sources/survey/."""
import csv, io, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "sources" / "survey"
PAGES = ROOT / "input" / "pagecontent"
DATA = ROOT / "data"

# name as used in report headings -> (ISO 3166-1 alpha-2, slug, region)
COUNTRIES = {
    "Germany": ("DE", "germany", "DACH and Benelux"),
    "Austria": ("AT", "austria", "DACH and Benelux"),
    "Switzerland": ("CH", "switzerland", "DACH and Benelux"),
    "Netherlands": ("NL", "netherlands", "DACH and Benelux"),
    "Belgium": ("BE", "belgium", "DACH and Benelux"),
    "Luxembourg": ("LU", "luxembourg", "DACH and Benelux"),
    "France": ("FR", "france", "Southern Europe"),
    "Italy": ("IT", "italy", "Southern Europe"),
    "Spain": ("ES", "spain", "Southern Europe"),
    "Portugal": ("PT", "portugal", "Southern Europe"),
    "Greece": ("GR", "greece", "Southern Europe"),
    "United Kingdom": ("GB", "united-kingdom", "Islands"),
    "Ireland": ("IE", "ireland", "Islands"),
    "Cyprus": ("CY", "cyprus", "Islands"),
    "Malta": ("MT", "malta", "Islands"),
    "Denmark": ("DK", "denmark", "Nordic and Baltic"),
    "Sweden": ("SE", "sweden", "Nordic and Baltic"),
    "Norway": ("NO", "norway", "Nordic and Baltic"),
    "Finland": ("FI", "finland", "Nordic and Baltic"),
    "Iceland": ("IS", "iceland", "Nordic and Baltic"),
    "Estonia": ("EE", "estonia", "Nordic and Baltic"),
    "Latvia": ("LV", "latvia", "Nordic and Baltic"),
    "Lithuania": ("LT", "lithuania", "Nordic and Baltic"),
    "Poland": ("PL", "poland", "Central and Eastern Europe"),
    "Czechia": ("CZ", "czechia", "Central and Eastern Europe"),
    "Slovakia": ("SK", "slovakia", "Central and Eastern Europe"),
    "Hungary": ("HU", "hungary", "Central and Eastern Europe"),
    "Slovenia": ("SI", "slovenia", "Central and Eastern Europe"),
    "Croatia": ("HR", "croatia", "Central and Eastern Europe"),
    "Romania": ("RO", "romania", "Central and Eastern Europe"),
    "Bulgaria": ("BG", "bulgaria", "Central and Eastern Europe"),
}
ALIASES = {"UK": "United Kingdom", "Czech Republic": "Czechia", "The Netherlands": "Netherlands"}

# which report files feed which page section (section title, file glob)
SECTIONS = [
    ("FHIR guides, registry format and terminologies", "*.md", "fhir"),
    ("Registries, public datasets, infrastructure and non-FHIR digital assets", "*-landscape.md", "landscape"),
]
EXCLUDE = {"overview.md", "overview-non-fhir.md", "eu-funding.md"}


def split_sections(text):
    """Return {country: body} for every '## Country' section of a report."""
    out = {}
    cur, buf = None, []
    for line in text.splitlines():
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            if cur:
                out[cur] = "\n".join(buf).strip()
            name = ALIASES.get(m.group(1).strip(), m.group(1).strip())
            cur, buf = (name if name in COUNTRIES else None), []
            continue
        if cur:
            buf.append(line)
    if cur:
        out[cur] = "\n".join(buf).strip()
    return out


def demote(body):
    """Report '###' headings become '####' inside a page section."""
    return re.sub(r"^(#{3,5}) ", lambda m: "#" + m.group(1) + " ", body, flags=re.M)


CROSS = []  # (report file, section title, body) for non-country sections


def split_other(text):
    """Return [(title, body)] for '## ' sections that are not countries."""
    out, cur, buf = [], None, []
    for line in text.splitlines():
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            if cur:
                out.append((cur, "\n".join(buf).strip()))
            name = ALIASES.get(m.group(1).strip(), m.group(1).strip())
            cur, buf = (None if name in COUNTRIES else name), []
            continue
        if cur:
            buf.append(line)
    if cur:
        out.append((cur, "\n".join(buf).strip()))
    return [(t, b) for t, b in out if b and not t.lower().startswith("method")]


def collect():
    per_country = {c: {"fhir": [], "landscape": [], "deep": []} for c in COUNTRIES}
    for f in sorted(SRC.glob("*.md")):
        if f.name in EXCLUDE:
            continue
        kind = "landscape" if f.name.endswith("-landscape.md") else "fhir"
        # dedicated deep-dive files: <country>-<topic>.md, e.g. france-fhir.md, greece.md
        m = re.match(r"^([a-z-]+?)(?:-(fhir|terminology|landscape))?\.md$", f.name)
        slug_to_name = {v[1]: k for k, v in COUNTRIES.items()}
        if m and m.group(1) in slug_to_name:
            name = slug_to_name[m.group(1)]
            per_country[name]["deep"].append((f.name, m.group(2) or "overview", f.read_text(encoding="utf-8")))
            continue
        text = f.read_text(encoding="utf-8")
        for country, body in split_sections(text).items():
            per_country[country][kind].append((f.name, body))
        for title, body in split_other(text):
            CROSS.append((f.name, title, body))
    return per_country


def write_cross_cutting():
    lines = ["### Cross-cutting notes", "", "Sections of the regional reports that are not about a single country: "
             "EU project participation, shared infrastructures and comparative notes. Verbatim from the reports.", ""]
    for fname, title, body in CROSS:
        lines += [f"### {title} (from {fname})", "", demote(body), ""]
    (PAGES / "cross-cutting.md").write_text("\n".join(lines), encoding="utf-8")


def write_country_pages(per_country):
    for country, parts in per_country.items():
        iso, slug, region = COUNTRIES[country]
        lines = [f"### {country} ({iso})", "", f"Region: {region}. Sources: see the URLs on each statement; "
                 f"raw research reports in [sources/survey](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/tree/main/sources/survey).", ""]
        if parts["fhir"]:
            lines += ["### FHIR guides, registry format and terminologies", ""]
            for fname, body in parts["fhir"]:
                lines += [demote(body), ""]
        if parts["landscape"]:
            lines += ["### Registries, public datasets, infrastructure and non-FHIR digital assets", ""]
            for fname, body in parts["landscape"]:
                lines += [demote(body), ""]
        for fname, topic, text in parts["deep"]:
            title = {"fhir": "Deep dive: FHIR", "terminology": "Deep dive: terminologies",
                     "landscape": "Deep dive: registries, datasets, infrastructure", "overview": "Deep dive"}[topic]
            # drop the report's H1, demote the rest by one level so H2 -> H3
            body = re.sub(r"^# .*\n", "", text, count=1)
            body = re.sub(r"^(#{2,5}) ", lambda m: "#" + m.group(1) + " ", body, flags=re.M)
            lines += [f"### {title}", "", body.strip(), ""]
        if not (parts["fhir"] or parts["landscape"] or parts["deep"]):
            lines += ["No country report yet.", ""]
        (PAGES / f"country-{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_country_index(per_country):
    rows = ["### Countries", "", "One page per country. Flags in the table: F = FHIR/terminology report present, "
            "N = registries/datasets/infrastructure report present, D = dedicated deep dive.", "",
            "| Country | ISO | Region | Reports |", "|---|---|---|---|"]
    for country, parts in sorted(per_country.items(), key=lambda kv: kv[0]):
        iso, slug, region = COUNTRIES[country]
        flags = "".join(k for k, v in (("F", parts["fhir"]), ("N", parts["landscape"]), ("D", parts["deep"])) if v)
        rows.append(f"| [{country}](country-{slug}.html) | {iso} | {region} | {flags or '–'} |")
    (PAGES / "countries.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def extract_table(text, heading_prefix):
    """Return the markdown table lines under the '## <heading_prefix>...' heading."""
    lines, grab, started = [], False, False
    for line in text.splitlines():
        if line.startswith("## "):
            grab = line.startswith("## " + heading_prefix)
            continue
        if grab and line.startswith("|"):
            lines.append(line); started = True
        elif grab and started and not line.startswith("|"):
            break
    return lines


def table_to_csv(lines, path):
    rows = [[c.strip() for c in l.strip("|").split("|")] for l in lines if not re.match(r"^\|\s*-", l)]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)


def write_landscape_tables():
    ov = (SRC / "overview.md").read_text(encoding="utf-8")
    a = extract_table(ov, "A.")
    b = extract_table(ov, "B.")
    DATA.mkdir(exist_ok=True)
    table_to_csv(a, DATA / "fhir-landscape.csv")
    table_to_csv(b, DATA / "terminology-landscape.csv")

    def linkify(lines):
        out = []
        for l in lines:
            m = re.match(r"^\| ([^|]+?) \|", l)
            name = ALIASES.get(m.group(1).strip(), m.group(1).strip()) if m else None
            if name in COUNTRIES:
                l = l.replace(f"| {m.group(1)} |", f"| [{name}](country-{COUNTRIES[name][1]}.html) |", 1)
            out.append(l)
        return out

    (PAGES / "landscape-fhir.md").write_text(
        "### FHIR landscape\n\nNational base or core FHIR guides, oncology FHIR specifications and the "
        "format in which the national cancer registry receives data today. \"none\" = nothing published; "
        "\"n/f\" = not found in a public source. Package versions as published on packages.fhir.org / "
        "Simplifier on 2026-11-18. Machine-readable copy: "
        "[data/fhir-landscape.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/fhir-landscape.csv).\n\n"
        + "\n".join(linkify(a)) + "\n\nDetails and source URLs are on the [country pages](countries.html).\n",
        encoding="utf-8")
    (PAGES / "landscape-terminology.md").write_text(
        "### Terminology landscape\n\nWhich terminologies, and which national variants and versions, are in use "
        "for oncology data. \"n/f\" = not found in a public source. Machine-readable copy: "
        "[data/terminology-landscape.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/terminology-landscape.csv).\n\n"
        + "\n".join(linkify(b)) + "\n\nDetails and source URLs are on the [country pages](countries.html).\n",
        encoding="utf-8")


def write_non_fhir_tables():
    """Tables C/D and patterns E from overview-non-fhir.md, if the consolidation exists."""
    src = SRC / "overview-non-fhir.md"
    intro = ("### Registries, public datasets, infrastructure and non-FHIR digital assets\n\n"
             "Consolidated from the regional non-FHIR reports (registries, public datasets, cancer "
             "infrastructure, non-FHIR digital assets). \"n/f\" = not found in a public source. "
             "Details with source URLs are on the [country pages](countries.html) and in the "
             "[cross-cutting notes](cross-cutting.html).\n\n")
    if not src.exists():
        (PAGES / "landscape-non-fhir.md").write_text(intro + "The consolidated tables are being compiled.\n", encoding="utf-8")
        return
    text = src.read_text(encoding="utf-8")
    c, d = extract_table(text, "C."), extract_table(text, "D.")
    table_to_csv(c, DATA / "registries-landscape.csv")
    table_to_csv(d, DATA / "infrastructure-landscape.csv")
    patterns = []
    grab = False
    for line in text.splitlines():
        if line.startswith("## "):
            grab = line.startswith("## E."); continue
        if grab:
            patterns.append(line)
    def linkify(lines):
        out = []
        for l in lines:
            m = re.match(r"^\| ([^|]+?) \|", l)
            name = ALIASES.get(m.group(1).strip(), m.group(1).strip()) if m else None
            if name in COUNTRIES:
                l = l.replace(f"| {m.group(1)} |", f"| [{name}](country-{COUNTRIES[name][1]}.html) |", 1)
            out.append(l)
        return out
    body = (intro + "### Cancer registries and data access\n\nMachine-readable copy: "
            "[data/registries-landscape.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/registries-landscape.csv).\n\n"
            + "\n".join(linkify(c)) + "\n\n### Infrastructure, EU projects and non-FHIR digital assets\n\nMachine-readable copy: "
            "[data/infrastructure-landscape.csv](https://github.com/PHOENIX-Initiative-European-Cancer/european-cancer-data-landscape/blob/main/data/infrastructure-landscape.csv).\n\n"
            + "\n".join(linkify(d)) + "\n\n### Patterns\n\n" + "\n".join(patterns).strip() + "\n")
    (PAGES / "landscape-non-fhir.md").write_text(body, encoding="utf-8")


def write_funding():
    """Funding page from eu-funding.md plus the national funding sections of the deep dives."""
    src = SRC / "eu-funding.md"
    lines = ["### Research funding and upcoming calls", "",
             "EU-level calls and running projects relevant to cancer data, interoperability and the EHDS, "
             "compiled 2026-11-18. Deadlines and budgets are as published on the survey date; check the "
             "Funding & Tenders portal before acting. National funding lines are on the country pages of "
             "Germany, France, Italy and the Netherlands under \"Research funding and calls\".", ""]
    if src.exists():
        body = re.sub(r"^# .*\n", "", src.read_text(encoding="utf-8"), count=1)
        body = re.sub(r"^(#{2,5}) ", lambda m: "#" + m.group(1) + " ", body, flags=re.M)
        lines += [body.strip(), ""]
    else:
        lines += ["The EU funding survey is being compiled.", ""]
    for f in sorted(SRC.glob("*-landscape.md")):
        slug_to_name = {v[1]: k for k, v in COUNTRIES.items()}
        slug = f.name[:-len("-landscape.md")]
        if slug not in slug_to_name:
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^## Research funding and calls\s*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
        if m:
            name = slug_to_name[slug]
            lines += [f"### National funding: {name}", "", demote(m.group(1).strip()), "",
                      f"See the [{name} page](country-{COUNTRIES[name][1]}.html) for context.", ""]
    (PAGES / "funding.md").write_text("\n".join(lines), encoding="utf-8")


def write_sushi_pages():
    cfg = ROOT / "sushi-config.yaml"
    text = cfg.read_text(encoding="utf-8")
    block = ["  # BEGIN country pages (generated by scripts/build_pages.py)"]
    for country in sorted(COUNTRIES):
        iso, slug, _ = COUNTRIES[country]
        block += [f"  country-{slug}.md:", f"    title: {country}"]
    block.append("  # END country pages")
    new = "\n".join(block)
    if "__COUNTRY_PAGES__" in text:
        text = text.replace("__COUNTRY_PAGES__", new)
    else:
        text = re.sub(r"  # BEGIN country pages.*?  # END country pages", new, text, flags=re.S)
    cfg.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    PAGES.mkdir(parents=True, exist_ok=True)
    pc = collect()
    write_country_pages(pc)
    write_country_index(pc)
    write_cross_cutting()
    write_landscape_tables()
    write_non_fhir_tables()
    write_funding()
    write_sushi_pages()
    n = sum(1 for p in pc.values() if p["fhir"] or p["landscape"] or p["deep"])
    print(f"wrote {n}/{len(COUNTRIES)} country pages, index, landscape tables, sushi page list")
