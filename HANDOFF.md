# CIS133 Textbook: HANDOFF

**Last updated:** 2026-07-08
**Repo:** https://github.com/jor2050111/cis133
**Live site:** https://jor2050111.github.io/cis133/
**Task list:** cis133-fall26 (`export CLAUDE_CODE_TASK_LIST_ID=cis133-fall26`)

## What Was Done (2026-07-08 Chapter 5 session)

* Wrote and shipped `book/chapters/chapter-05.md` (The Box Model and
  Typography): 4 content sections (every element is a box, spacing
  syntax individual and shorthand, choosing fonts, text properties
  and readable typography), 5 Try It Yourself exercises, 4 Quick
  Checks, Skills Lab 5A, 367 sentences at 14.3 words average, zero
  at 35+. 480 lines. Same orchestrated pipeline as Chapter 4.
* Consolidated Module 5's four draft MLOs into exactly 3:
  MLO-5.1 (Apply) padding/border/margin with individual and shorthand
  syntax -> 5.1-5.2, MLO-5.2 (Apply) font stacks, sizes, text
  properties for readability -> 5.3-5.4, MLO-5.3 (Analyze) diagnose
  spacing and readability with the DevTools box-model diagram and the
  four-point checklist -> threads all sections, lab-assessed. Rubric
  byte-identical to chapter-01.md.
* Built `assets/code/chapter-05/`: `starter-site/` (the Lab 4A model
  solution: 3 pages + `club-styles.css` + 7 images), `club-palette.txt`
  (byte-identical copy from chapter-04), `box-practice.html` +
  `box-practice.css` (engineered numbers: .event-notice 354px total,
  .volunteer-call 336px from the same 300px width, all 300 under
  border-box, plus the deliberately cramped `.drive-notes` region
  whose contrast passes while size 11px, line-height 1.05, and
  missing max-width violate the checklist), `skills-lab-5a-answers.txt`,
  README.
* Lab 4A model solution key calls (in club-styles.css): body light
  sand/ink, header club teal/white, nav white, footer deep teal/white,
  `h2, figcaption` deep teal (h1 wears the header's white because deep
  teal on club teal fails contrast at 1.60:1 and combinators wait for
  Ch 6), `.reminder` sunset orange on 2 paragraphs across 2 pages,
  `#meeting-times` sand on the contact schedule ul, figure white
  plates as the stretch. KNOWN WART, deliberate: footer links render
  default blue on deep teal (1.26:1). It is the model's own 3.B
  critique answer and Chapter 6's selector hook. Do not fix before
  Chapter 6.
* All validation executed (2026-07-08): Nu zero messages on all 4
  HTML files, jigsaw 0 errors on both stylesheets, Oswald css2 URL
  live (single-link student form recorded), all 5 Further Reading
  URLs 200.
* Added 20 terms to `book/glossary.md` (19 from the draft plus
  font-style from review).
* Ran the three review agents. Applied required fixes: three TIY
  answer leaks removed (prose now works .event-notice only and TIY
  5.2 predicts .volunteer-call, the shorthand-clock example switched
  to fresh `.callout` numbers so TIY 5.3's expansion stays a
  prediction, the body-margin reveal softened so TIY 5.1 discovers
  the element and layer), Quick Check 5.1 Q2 given a fresh transfer
  scenario, Looking Ahead's nav-bar promise reattributed to Chapter 4
  (its true in-text home), font-style bolded and glossaried, and the
  UPSTREAM stale promise in chapter-02.md fixed ("leave size for CSS
  to fix in Chapter 4" now says Chapter 5, where font-size actually
  lands). Applied judgment calls: Google Fonts preconnect aside
  trimmed to a bare mention. Skipped with rationale: TIY 5.4/5.5
  step counts (the checklist practice IS the exercise), 4-subsection
  density pattern (within the 2-4 band), part-structure.md's Part II
  Bloom's-focus line reading "Analyze entering in Chapter 6" while
  Ch 4 ships Evaluate and Ch 5 ships Analyze (same docs-note
  precedent as Part I), Google Fonts unbolded (matches the CSS Zen
  Garden external-resource precedent).
* Uncommented the Chapter 5 nav line. `zensical build --clean`: no
  issues.

**Chapter 5 design notes:**

* Promises paid: Ch 2's "spacing belongs to CSS, never br" (named
  callback in 5.1's paint rule), Ch 2's "heading size belongs to
  CSS" final installment (5.3 font-size), Ch 4's Looking Ahead
  (text pressing against edges opens the chapter).
* Promises planted (pay these explicitly): Ch 6 = Flexbox arranges
  the boxes, the nav becomes a navigation bar (promise now correctly
  attributed to Chapter 4's text), selectors sharp enough to fix the
  footer-link wart. Ch 8 = the readable column adapts to any screen.
  Ch 9 = rem and user settings, the contrast math. Ch 12 = publish.
* Universal selector, rem-vs-em, inheritance (one sentence in 5.3),
  and Google Fonts internals are deliberate one-mention previews.
  Do not deepen in place.
* Pre-term verification (5 min in a real browser): the DevTools
  box-model diagram's current tab home (Computed or Layout) in
  Chrome/Edge/Firefox, body default margin still 8px, TIY 5.4's
  Verdana-wide claim eyeballed once, Google Fonts embed panel still
  offering the link form.

## What Was Done (2026-07-08 Chapter 4 session)

* Wrote and shipped `book/chapters/chapter-04.md` (CSS Foundations):
  4 content sections (what CSS is and rule anatomy, inline/internal/
  external and the cascade, element/class/id selectors, color systems
  and CSS validation), 5 Try It Yourself exercises, 4 Quick Checks,
  Skills Lab 4A, 446 sentences at 14.3 words average, zero at 35+.
  538 lines. This chapter was built by an orchestrated agent pipeline
  (outline -> asset agent -> draft agent -> three review agents), same
  quality gates as Chapters 1-3.
* Consolidated Module 4's four draft MLOs into exactly 3:
  MLO-4.1 (Apply) connect CSS three ways -> 4.1-4.2,
  MLO-4.2 (Apply) rules with selectors and color systems -> 4.1/4.3/4.4,
  MLO-4.3 (Evaluate) critique with HTML and CSS validators -> 4.4.
  The Evaluate tag matches CLO IV's own verb (Chapter 1 precedent).
  Rubric copied verbatim from chapter-01.md (byte-diff verified).
* Built `assets/code/chapter-04/`: `starter-site/` (Lab 3A model
  solutions rebuilt from the Chapter 3 answer key, 3 pages + 7 images),
  `club-palette.txt` (exact hexes extracted from the chapter-03
  generator, 9 recommended pairings verified in Python at WCAG AA
  4.5:1 or better), `selector-practice.html`, `cascade-practice.html`
  + `practice-styles.css`, `skills-lab-4a-answers.txt`, README.
* Planted defect: `drive-gallery.html` in starter-site carries one
  leftover inline style (`style="color: #1a5e5e;"` on the second
  figcaption). Lab Part 3 hunts and migrates it. Disclosed in the
  README per the gallery-content.txt precedent.
* All validator claims executed (2026-07-08): Nu checker zero messages
  on all 8 HTML files, jigsaw clean-pass message captured verbatim,
  missing-semicolon error captured (the in-chapter worked example:
  the report blames line 9 for line 8's defect), colr typo error
  captured but NOT quoted in prose. The typo lives in TIY 4.5 as a
  genuine discovery, per the Chapter 2 title/em precedent. The
  duplicate-id validator claim in 4.3 was verified live.
* Palette: club teal #268080, deep teal #1a5e5e, sunset orange
  #f4a259, light sand #fac78d, sand #deb887, saguaro green #5e9959,
  ink #333333, white #ffffff, plus 2 labeled decoy browns.
* Added 25 terms to `book/glossary.md`.
* Ran the three review agents (scope, consistency, pedagogy). Applied
  the required fixes: validator section restructured so prose keeps
  only the semicolon worked example (TIY discovery preserved), id
  lowercased in two headings, Key Terms reordered to first-use order,
  stale pack README rows corrected. Applied judgment calls: WCAG
  ratio numbers trimmed to a preview (Chapter 9 owns the math), the
  bare teal keyword rule dropped from the color block, the hex-reading
  TIY moved ahead of the validator subsection (TIYs renumbered
  4.4/4.5), the two-browns judgment routed into Part 3's stretch, an
  Evaluate-level critique prompt added to answer 3.B, one filler
  "just" removed, glossary declaration/value examples aligned to the
  chapter's anatomy rule. Skipped with rationale: TIY 4.2's three
  refresh cycles (inherent to the cascade demo), the 14-line landmark
  block (coherent unit mirroring the lab task), 6 Key Concepts bullets
  (template sanctions 4-6), splitting 4.4 into two sections (the fix
  pass shortened it instead), MLO-4.3's verb chain (matches shipped
  MLO-2.3/3.3 house pattern).
* ANSWER KEY (instructor, for the Lab 5A starter build): the Lab 4A
  model solution links `club-styles.css` from all three heads and uses
  the chapter's own example rules: body light sand + ink, header club
  teal + white, nav white, footer deep teal + white, h1/h2 selector
  list deep teal, a role-named class on content in at least two pages,
  one id on a unique element, the gallery figcaption's inline
  declaration migrated into a stylesheet rule, every pairing from the
  palette's passing list. The chapter-05 asset agent makes the
  remaining concrete choices from the actual page content and records
  them in its facts sheet.
* Uncommented the Part II nav block with only Chapter 4 live in
  `zensical.toml`. `zensical build --clean`: no issues.

**Chapter 4 design notes:**

* Promises paid from earlier chapters: Ch 2's "heading size belongs
  to CSS" (TIY 4.1 catches font-size in DevTools, the anatomy example
  colors h1), Ch 3's "landmarks are the exact hooks your stylesheets
  grab first" (4.3 styles header/nav/footer), div and span get their
  styling jobs (4.3).
* Promises planted (pay these explicitly): Ch 5 = the box model,
  spacing belongs to CSS and never br, "you can color boxes, next you
  control their space." Ch 6 = the nav list becomes a navigation bar,
  cascade/specificity deepens with smarter selectors. Ch 8 = one
  stylesheet adapts to every screen. Ch 9 = the math behind the
  palette's passing list. Ch 12 = the stylesheet publishes with the
  site.
* hsl() and specificity are deliberate one-mention previews. Do not
  deepen them in place.
* Pre-term verification (5 min in a real browser): TIY 4.1's Wikipedia
  Styles panel and "user agent stylesheet" labels on current browsers,
  the jigsaw direct-input tab layout, and VS Code still drawing color
  swatches in .css files (TIY 4.4).

## What Was Done (2026-07-08 Chapter 3 session)

* Wrote and shipped `book/chapters/chapter-03.md` (Semantic HTML
  and Images): 4 content sections (semantic vs non-semantic with
  the full strong/em story, page landmarks, images and alt text,
  formats and site organization), 5 Try It Yourself exercises,
  4 Quick Checks, Skills Lab 3A, 349 sentences at 14.7 words
  average, zero at 35+ words.
* Consolidated Module 3's four draft MLOs into exactly 3:
  MLO-3.1 (Apply) semantic elements by meaning -> 3.1-3.2,
  MLO-3.2 (Apply) images with purpose-matched alt text -> 3.3,
  MLO-3.3 (Analyze) differentiate formats, pick format and folder
  home -> 3.4. Rubric copied verbatim from chapter-01.md
  (consistency agent diff-verified: only the heading differs).
* FIRST CHAPTER WITH IMAGE ASSETS. Nine PNGs in
  `assets/code/chapter-03/`, all rendered by the seeded generator
  `assets/code/_generators/generate_chapter03_images.py`
  (BASE_SEED=133, Pillow 12.3.0, byte-identical rerun proven by a
  double-render assert, plus asserts on dimensions, logo
  transparency, chart data, and the file-size teaching point).
  One flat-illustration style throughout: the fictional club's
  design set. `cactus-garden.png` and `membership-chart.png` are
  chapter-practice images. The other seven are lab images.
* IF IMAGES ARE EVER REPLACED (for example with AI-photo
  upgrades): re-verify TIY 3.5's executed size numbers (~13 KB
  chart, ~11 KB drive scene, ~3 KB logo), the membership example
  alt (grows 18 to 39), and the lab chart's cited numbers (64
  cables, 154 total). The generator asserts pin all of these.
* Data pack text/HTML: `recycling-guide-start.html` and
  `contact-start.html` (Lab 2A model solutions, so Lab 3A does not
  punish a weak Lab 2A twice), `gallery-content.txt` (ships no alt
  text on purpose), `skills-lab-3a-answers.txt` (landmark map, alt
  log, format decisions), README with the image data dictionary.
* All validator claims executed (Nu checker via curl, 2026-07-08):
  both starters and all three model-solution pages validate with
  zero messages, and the missing-alt error message was captured
  live. Model solutions live in the session scratchpad only, per
  the Chapter 2 precedent.
* ANSWER KEY (instructor, not in the student README): guide
  landmark map is header (logo, h1, 2 intro paragraphs), nav
  (3-link list), main with 4 sections, divider img, footer.
  `<strong>` on "in order", `<em>` on "not". Contact page earns no
  footer (deliberate teaching decision in Part 3 step 3). Model
  informative alts describe the illustrated scenes, divider gets
  alt="", chart alt delivers cables 64 of 154 total.
* TIY 3.2 verified live 2026-07-08: en.wikipedia.org/wiki/Recycling
  renders exactly 1 main and 12 nav elements. All five Further
  Reading URLs return 200.
* Added 30 terms to `book/glossary.md` (new G, J, and L sections).
* Ran the three review agents. Applied all 3 required fixes:
  banned filler "just" removed (twice), Skills Lab Part 2/3 MLO
  labels corrected to what each part exercises, and the worked
  examples de-coupled from graded lab images (the figure example
  now uses the new chapter-only `membership-chart.png`, the
  informative example uses `cactus-garden.png`, the folder example
  uses the divider's taught alt=""). Applied judgment calls: time
  estimate to 5-6 hours, Ctrl+F-in-Elements bridge added to TIY
  3.2, example folder renamed to skills-lab-3a-ortiz (fictional
  student convention), folder tree lists all four lab images,
  "text-level elements" glossed in 3.1 and unified with the lab
  wording. Skipped with rationale: dedicated retrieval touchpoints
  for header-vs-head and img-inline (Quick Checks capped at 3
  questions, both reinforced indirectly), moving off the 8-example
  band floor (scope agent recommended no forced additions), and
  part-structure.md's Part I "Bloom's focus" line still reading
  "Remember through Apply" while all three shipped chapters tag
  their third MLO Analyze (docs note, not a chapter defect).
* Uncommented the Chapter 3 nav line in zensical.toml.
  `zensical build --clean`: no issues.

**Chapter 3 design notes:**

* Promises paid from Chapter 2: semantic landmarks, the full
  strong/em story, images with alt text, "the club's pages get
  their pictures." Also paid Chapter 1's semantic-HTML-for-search
  and alt-text previews, and Chapter 2's block-vs-inline return.
* Promises planted (pay these explicitly): Ch 4 = CSS styles the
  landmarks ("the exact hooks your stylesheets grab first"),
  heading size belongs to CSS. Ch 6 = the nav list becomes a
  styled navigation bar. Ch 9 = accessibility deep dive, alt
  decisions deepen. Ch 12 = publish, index.html becomes the home
  page name, the self-contained folder survives the move.
* aside and WebP are deliberate one-mention previews. Do not
  deepen them in place.
* Pre-term verification (5 min in a real browser): TIY 3.2's
  Wikipedia landmark counts (a skin change could alter them),
  TIY 3.3 broken-src rendering with and without alt on current
  browsers, and the lab pages opening cleanly from a zipped and
  re-extracted folder.

## What Was Done (2026-07-08 Chapter 2 session)

* Wrote and shipped `book/chapters/chapter-02.md` (Basic HTML
  Elements): 4 content sections (workspace and the edit-save-refresh
  cycle, document anatomy, headings/paragraphs/lists, links and the
  W3C validator), 5 Try It Yourself exercises, 4 Quick Checks, Skills
  Lab 2A, 353 sentences at 13.7 words average, zero at 35+ words.
* Consolidated Module 2's three draft MLOs into exactly 3:
  MLO-2.1 (Apply) build a complete document -> 2.1-2.2,
  MLO-2.2 (Apply) structure content by meaning -> 2.3-2.4,
  MLO-2.3 (Analyze) diagnose markup errors from validator
  reports -> 2.4. Full Evaluate-level validator critique (CLO IV)
  deepens when CSS validation arrives in Chapter 4.
* Rubric copied verbatim from chapter-01.md (consistency agent
  diff-verified every cell and the Scoring line).
* Built `assets/code/chapter-02/`: recycling-guide-content.txt
  (labeled page text, students type only the markup),
  broken-contact.html (planted defects for the repair task),
  skills-lab-2a-answers.txt (fix log plus Q&A), README.md.
  Continuity: the lab builds the recycling page whose sources
  Skills Lab 1A vetted.
* All validator numbers executed, never estimated (Nu checker via
  curl, 2026-07-08). broken-contact.html: 4 defects produce exactly
  8 messages, the unclosed strong cascading into 5. The chapter's
  worked example (unclosed em, 3 messages) and TIY 2.5 (deleted
  /title, 2 messages) quote captured output. Model solutions for
  both lab pages validate with zero messages.
* ANSWER KEY (instructor, not in the student README):
  broken-contact.html defects are (1) head missing title,
  (2) h2 closed by /h3, (3) p as a direct child of ul,
  (4) unclosed strong under Collection Events.
* Link check: every external URL returns 200 except azdeq.gov,
  whose WAF blocks curl, so the lab's second source swapped to
  phoenix.gov (verified 200). Same precedent as Chapter 1's
  WAF-blocked TIY target.
* Added 24 terms to `book/glossary.md`.
* Ran the three review agents (scope, consistency, pedagogy).
  Applied all 5 required fixes: comment row added to the skeleton
  walkthrough table, DevTools panel named for Chrome/Edge/Firefox/
  Safari, block-vs-inline given a Quick Check touchpoint, bolded
  terms matched to glossary spellings (valid markup, singular
  block-level/inline element). Applied 4 judgment calls: merged the
  Attributes H3 so section 2.2 holds 4 subsections, sharpened TIY
  2.3's predict, switched the worked validator example from title
  to em so TIY 2.5 stays a discovery, and tightened the hyperlink
  parenthetical. Skipped with rationale: thematic MLO-to-section
  mapping (Chapter 1 precedent), DevTools TIY as tooling
  orientation, and the lab Q&A "justify" verb, which
  docs/part-structure.md sanctions for Skills Labs.
* Uncommented the Chapter 2 nav line in zensical.toml.
  `zensical build --clean`: no issues.
* CLAUDE_CODE_TASK_LIST_ID pin worked: this session's tasks lived
  on cis133-fall26 from the start.

**Chapter 2 design notes:**

* Promises paid from Chapter 1: VS Code setup, first HTML document,
  W3C validator, DevTools first look.
* Promises planted (pay these explicitly): Ch 3 = semantic
  landmarks, the full strong/em story, images with alt text ("the
  club's pages get their pictures"). Ch 4 = heading size belongs to
  CSS. Ch 5 = spacing belongs to CSS, never br. Ch 12 = publish,
  file:// becomes https://, relative links survive the move.
* strong/em and block-vs-inline are deliberate previews with full
  treatment in Chapter 3. Do not deepen them in place.
* Pre-term verification (5 min in a real browser): TIY 2.3 DevTools
  panel names on current browsers, TIY 2.5 blank-page result after
  deleting /title, and the two lab links (epa.gov electronics page,
  phoenix.gov) resolving normally.

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

1. Write Chapter 6 (Layout with Flexbox). Same cycle as Chapters 1-5:
   consolidate draft MLOs to exactly 3 (the old module-06 task file
   was a duplicate of module-05, so Lab 6A is designed fresh),
   outline, asset build with executed facts, draft, glossary, QA
   sweeps, review agents, nav line, build, push. Copy the locked
   rubric verbatim from chapter-01.md. Pay the nav-bar promise
   (planted in Chapter 4's text, re-planted by Chapter 5's Looking
   Ahead) and fix the footer-link wart with Chapter 6 selectors.
   Lab 6A starters = the Lab 5A model solution (build from
   chapter-05/starter-site plus the Chapter 5 answer key above).
   Lab 6A completes the Part II milestone: multi-section page,
   external stylesheet, controlled spacing and type, Flexbox
   navigation bar.
2. Repeat per chapter through Chapter 12 (chapters 9 and 12 are new
   coverage with no draft, built from docs/part-structure.md).
3. Before the term starts: run the 5-minute browser verifications
   for Chapters 1, 2, and 3 (see each chapter's design notes
   above).
4. After chapters ship: refine the `module-*-task.html` Canvas pages,
   assemble the course data pack zip for Canvas, and set assessment
   weights in docs/part-structure.md.

## How to Continue

Open a session in `~/Documents/code/textbooks/cis133/`, read CLAUDE.md
and this file, then start with Next Steps. The authoritative course
reference is `docs/CIS133_CLOs.md`. The authoritative structure is
`docs/part-structure.md`.
