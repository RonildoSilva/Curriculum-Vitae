#!/usr/bin/env bash
# Gera o PDF a partir de um .md usando cv.css. Uso: ./build.sh curriculo-backend-developer.md
set -euo pipefail
cd "$(dirname "$0")"
md="$1"; html="$(mktemp --suffix=.html)"
pandoc "$md" -s --css cv.css --embed-resources -V pagetitle="Ronildo Silva · Currículo" -V maxwidth=none -o "$html"
google-chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$PWD/${md%.md}.pdf" "file://$html" 2>/dev/null
rm -f "$html"
