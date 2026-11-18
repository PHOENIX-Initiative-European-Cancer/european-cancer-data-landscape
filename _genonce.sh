#!/usr/bin/env bash
# Build the IG locally. Needs Java 17+, SUSHI, Jekyll and the IG Publisher jar.
set -euo pipefail
cd "$(dirname "$0")"
PUB="${PUBLISHER_JAR:-input-cache/publisher.jar}"
if [ ! -f "$PUB" ]; then
  mkdir -p input-cache
  curl -L https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar -o input-cache/publisher.jar
  PUB=input-cache/publisher.jar
fi
python3 scripts/build_pages.py
java -jar "$PUB" -ig . "$@"
