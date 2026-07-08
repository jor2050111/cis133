# CIS133 Textbook: HANDOFF

**Last updated:** 2026-07-08
**Repo:** https://github.com/jor2050111/cis133
**Live site:** https://jor2050111.github.io/cis133/
**Task list:** cis133-fall26 (`export CLAUDE_CODE_TASK_LIST_ID=cis133-fall26`)

## What Was Done (2026-07-08 Chapter 1 session)

* Wrote and shipped `book/chapters/chapter-01.md` (The Internet and
  the World Wide Web): 4 content sections, 5 Try It Yourself
  exercises, 4 Quick Checks, Skills Lab 1A, ~6,000 words at Flesch-
  friendly 13.2 words/sentence average, zero sentences at 35+ words.
* Consolidated Module 1's five draft MLOs into exactly 3:
  MLO-1.1 (Understand) Internet/web/browsers/servers -> 1.1,
  MLO-1.2 (Understand) IP/DNS/domains/URL parts -> 1.2,
  MLO-1.3 (Analyze) compare sources and practices for reliability,
  authorship, security, and ethical use -> 1.3-1.4. The Analyze tag
  matches CLO III's own level.
* LOCKED THE RUBRIC. Chapter 1 holds the course's first in-book
  rubric copy, now canonical for all 12 chapters. The one sanctioned
  adaptation reads "HTML and CSS syntax and the course tools" in the
  Code Accuracy Mastery cell. Copy it verbatim from chapter-01.md
  (or the template) into every later chapter.
* Built `assets/code/chapter-01/`: skills-lab-1a-worksheet.txt,
  url-inventory.txt, source-profiles.txt (five fictional source
  profiles), README.md data dictionary.
* Added 16 terms to `book/glossary.md` (cache through top-level
  domain, plus client-server model and query string).
* Uncommented the Part I nav block with only Chapter 1 live in
  `zensical.toml`, and the cover's Getting Started link.
* Added an accessibility bullet to the Chapter 1 entry in
  `docs/part-structure.md` (outline I.C.4 covers it under Internet
  fundamentals, and the chapter previews screen readers).
* Ran three review agents (scope, consistency, pedagogy) and applied
  every required fix: MLO-1.3 broadened to claim the security strand,
  SEO given a Quick Check touchpoint, TIY 1.2 made cache-outcome
  robust, query-string field aligned across chapter/Quick Check/
  worksheet, TIY 1.3's 404 target switched to
  www.w3.org/this-page-does-not-exist (verified 404 with visible
  error page via curl 2026-07-08; the college site's WAF blocks
  curl).
* `zensical build --clean`: no issues.

**Chapter 1 design notes:**

* Chapter 1 is a conceptual chapter (no HTML authoring yet), so it
  carries 5 `text` diagram blocks instead of the 8-15 code-example
  band. Exempt by design, do not "fix" this.
* Pre-term verification (5 min in a real browser): TIY 1.3 error
  pages, TIY 1.5 padlock/certificate panel on phoenixcollege.edu,
  TIY 1.4 two-engine comparison.
* Promises planted for later chapters (pay these debts explicitly):
  Ch 2 = VS Code, first HTML document, W3C validator. Ch 3 = semantic
  HTML with search engines as an audience, alt text. Ch 9 =
  accessibility standards and testing. Ch 11 = forms and responsible
  data collection. Ch 12 = FTP family / secure transfer, publishing.
* This session ran without CLAUDE_CODE_TASK_LIST_ID set, so its task
  breakdown lived in a per-session list. Export
  `CLAUDE_CODE_TASK_LIST_ID=cis133-fall26` before future sessions.

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

## Deploy Status: Live

Mr. Vega refreshed the gh token with the `workflow` scope on
2026-07-08 and pushed the deploy workflow. The Actions run succeeded
and the site is live. Future textbook setups will not hit the scope
rejection.

## Source Material for Chapters

Draft material lives at
`/Users/vega/Documents/code/textbooks/cis133-OLD-DRAFT-docs-only/`
(copied there by Mr. Vega on 2026-07-08 from the old Desktop temp
folder, which is now redundant):

* 10 draft chapters (`chapter-01.md` ... `chapter-10.md`), extracted
  from *HTML & CSS Simply Explained* by Brad Olsen
  (open.maricopa.edu/cis133da), plus `intro.md`, `appendix.md`, and an
  `assets/` folder of figures
* `draft-a-cis133-course-map-v2.md`: the QM course map with drafted
  MLOs, CC1-CC6, checkpoints, and final project. Its modules carry 3-5
  MLOs each. The textbook rule is exactly 3 per chapter, so MLOs get
  consolidated chapter by chapter during writing.
* `cis133-course-learning-outcomes.md`: official CLOs and outline
  (already folded into docs/CIS133_CLOs.md)
* `module-*-task.html`: Canvas module assignment pages. They need
  refinement and feed Skills Lab design after chapters ship.

**License:** the source book is CC BY-NC 4.0 by Brad Olsen, so
adapting its materials is permitted with attribution for this
noncommercial OER textbook. The attribution block lives on the cover
page (`book/index.md`, Sources & Permissions). Keep it on the cover in
every redesign. Chapters still get written fresh at CIS360 quality,
beginner level, in Mr. Vega's voice, with the drafts as scope and
topic reference. The draft folder itself stays out of this public
repo.

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

1. Write Chapter 2 (Basic HTML Elements). Same cycle as Chapter 1:
   consolidate draft MLOs to exactly 3, outline, draft with the
   instructional-content-writing skill, starter files with README,
   glossary, QA sweeps, review agents, nav line, build, push. Copy
   the locked rubric verbatim from chapter-01.md. Pay Chapter 1's
   promises: VS Code setup, first HTML document, W3C validator.
2. Repeat per chapter through Chapter 12 (chapters 9 and 12 are new
   coverage with no draft, built from docs/part-structure.md).
3. Before the term starts: run the 5-minute browser verification of
   Chapter 1's Try It exercises (see design notes above).
4. After chapters ship: refine the `module-*-task.html` Canvas pages,
   assemble the course data pack zip for Canvas, and set assessment
   weights in docs/part-structure.md.

## How to Continue

Open a session in `~/Documents/code/textbooks/cis133/`, read CLAUDE.md
and this file, then start with Next Steps. The authoritative course
reference is `docs/CIS133_CLOs.md`. The authoritative structure is
`docs/part-structure.md`.
