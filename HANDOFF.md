# CIS133 Textbook: HANDOFF

**Last updated:** 2026-07-08
**Repo:** https://github.com/jor2050111/cis133
**Live site:** https://jor2050111.github.io/cis133/ (will 404 until the
workflow push below lands)
**Task list:** cis133-fall26 (`export CLAUDE_CODE_TASK_LIST_ID=cis133-fall26`)

## What Was Done (2026-07-08 scaffold session)

* Instantiated the repo from
  `/Users/vega/Documents/code/textbooks/template/` following
  NEW-TEXTBOOK-SETUP.md. All placeholder tokens replaced, grep
  acceptance test clean.
* Ran `../shared/tools/sync-shared.sh` and seeded
  `docs/blooms-taxonomy-reference.md` from `../shared/`.
* Wrote `docs/CIS133_CLOs.md` (official description, 12 elevated CLOs,
  condensed CC1-CC6 course-map outcomes, CLO-to-chapter mapping, full
  district outline).
* Wrote `docs/part-structure.md` (authoritative 12-chapter plan in 4
  Parts, coverage matrices, dependencies, schedule).
* Completed `book/index.md` and seeded `book/glossary.md` with 12
  Chapter 1 terms.
* Local build verified: `zensical build --clean` reports no issues.
* Created the GitHub repo, pushed `main`, enabled Pages with
  build_type=workflow.

## BLOCKED: One Action Needed From Mr. Vega

The gh OAuth token lacks the `workflow` scope, so the push of
`.github/workflows/docs.yml` was rejected. The workflow sits in a
local commit waiting to go. To unblock, run in any terminal:

```bash
gh auth refresh -h github.com -s workflow
cd ~/Documents/code/textbooks/cis133 && git push
```

After that push, the Actions run builds and deploys the site. Confirm
the live URL loads. (This same refresh fixes future textbook setups.)

## Source Material for Chapters

Draft material lives at
`/Users/vega/Desktop/temp-to-delete-later/textbook/cis133/`:

* 10 draft chapters (`chapter-01.md` ... `chapter-10.md`), extracted
  from the Maricopa OER Pressbooks book previously used
  (open.maricopa.edu/cis133da), plus `intro.md`, `appendix.md`, and an
  `assets/` folder of figures
* `draft-a-cis133-course-map-v2.md`: the QM course map with drafted
  MLOs, CC1-CC6, checkpoints, and final project
* `cis133-course-learning-outcomes.md`: official CLOs and outline
  (already folded into docs/CIS133_CLOs.md)
* `module-*-task.html`: Canvas module assignment pages, useful when
  designing Skills Labs

**Do not delete that folder until all 12 chapters are written.** The
folder name says temp-to-delete-later, so consider copying it to Drive
(co-professor) for safekeeping.

**Treatment:** the drafts are scope and topic reference only. Chapters
get written fresh at CIS360 quality, beginner level, in Mr. Vega's
voice. Do not paste Pressbooks prose. If any passage is reused, first
confirm the source book's CC license terms and attribution
requirements. The drafts do not ship in this public repo.

## Key Design Decisions

* 12 chapters in 4 Parts (see `docs/part-structure.md`). The 10 proven
  module topics keep their order. Two chapters were added where the
  district outline had no dedicated module: Chapter 9 (Web
  Accessibility, outline section V) and Chapter 12 (Scripting Concepts
  and Publishing, outline sections VII and III.B/VIII.G).
* Nav in `zensical.toml` holds all 12 chapters as comments. Uncomment
  each entry as its chapter ships so the build never references a
  missing file.
* Bloom's rule (QM measurability): full RBT range allowed, every MLO
  uses a measurable action verb, never "understand," "know," or
  "learn" as the verb.
* Flesch Reading Ease 60-70, top of band. No prerequisites, teach from
  zero.
* Data pack ships starter files (HTML, CSS, images, text), never
  hand-typed content. Load pattern recorded in CLAUDE.md.

## Pending Decisions

* Assessment weights in `docs/part-structure.md` (marked [weight]%):
  confirm against the Canvas build before syllabus publication.
* Chapter subtitles in `docs/part-structure.md` are working titles.
  Adjust freely before each chapter is written.

## Next Steps

1. Mr. Vega: run the `gh auth refresh` + `git push` above.
2. Confirm the Actions run succeeds and the live site loads.
3. Write Chapter 1 (use `templates/chapter-template.md`, the draft
   chapter 1 as scope reference, and the instructional-content-writing
   skill).
4. Build the `assets/code/chapter-01/` starter files alongside the
   chapter, with a README data dictionary.
5. Uncomment the Chapter 1 nav line in `zensical.toml` when it ships.

## How to Continue

Open a session in `~/Documents/code/textbooks/cis133/`, read CLAUDE.md
and this file, then start with Next Steps. The authoritative course
reference is `docs/CIS133_CLOs.md`. The authoritative structure is
`docs/part-structure.md`.
