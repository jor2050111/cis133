# Data Pack Generators

## Current scripts (pedagogy upgrade, 2026-07-28)

* `generate_chart_images.py`: renders the two chart PNGs into
  `../chapter-03/` (Pillow 12.3.0, deterministic, byte-identical on
  rerun, data asserted in code).
* `propagate_pack_images.py`: copies the nine chapter-03 masters to
  every downstream folder and asserts byte identity.
* `IMAGE-MANIFEST.md`: provenance and SHA-256 checksums for all nine
  images, including the seven AI-generated illustrations (Codex CLI,
  model gpt-5.6-sol). AI masters are canonical files, not
  seed-reproducible; the manifest is the record.
* Retired: `generate_chapter03_images.py` (the club-era Pillow
  illustration generator) lives in `../../../cis133-archive/` and in
  git history.


Scripts in this folder rebuild every derived file in the course data
pack. Follow the pattern the existing textbooks use:

## Conventions

* **Seeded and reproducible.** Synthetic datasets use a fixed base seed
  (pick the course number) so reruns are byte-identical. Add asserts
  that verify the engineered properties each chapter depends on.
* **Document provenance.** Real datasets record their source, license,
  and retrieval date here and in the chapter folder's README.
* **One-time captures are not rebuilt.** Files captured from live APIs
  are committed as-is and documented, not regenerated.
* **Each chapter folder gets a README** describing every file, its
  schema, and which sections or labs load it.

## Rebuilding the student data pack zip

From the parent of the repo root (the zip's internal root is
`cis133`, the folder name the published chapters tell
students to work in):

```bash
cd /Users/vega/Documents/code/textbooks && \
zip -r cis133/build/cis133-data-pack.zip \
    cis133/assets/code \
    -x '*.DS_Store' -x '*__pycache__*'
```

The zip lands in `build/` (gitignored) and uploads to Canvas.
