#!/usr/bin/env bash
set -uo pipefail

# Add TeX Live to PATH
export PATH="/opt/texlive/bin:$PATH"

mkdir -p build

# Compile IEEE (biblatex + biber)
echo "[build] Compiling IEEE"
latexmk -f -file-line-error -outdir=build -xelatex main_ieee.tex || true

# Compile ACM (BibTeX)
echo "[build] Compiling ACM"
latexmk -f -file-line-error -outdir=build -bibtex -xelatex main_acm.tex || true

# Compile APA7 (biblatex + biber)
echo "[build] Compiling APA7"
latexmk -f -file-line-error -outdir=build -xelatex main_apa7.tex || true

echo "[build] PDFs available in build/"
