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

Do not zip `assets/code` by hand. This folder is author-facing and
must not ship to students, and ten chapter READMEs cite paths inside
it. The build tool drops the folder, rewrites those citations, and
reflows `IMAGE-MANIFEST.md` into a student-facing `PROVENANCE.md` at
the pack root:

```bash
python3 /Users/vega/Documents/code/textbooks/shared/tools/build_student_packs.py
```

It verifies that every data file stays byte-identical and refuses to
write a zip if a check fails. The zip lands in the GitHub Pages repo
at `jor2050111.github.io/data-packs/`, which is the one place the
student pack lives. Pushing that repo publishes it.
