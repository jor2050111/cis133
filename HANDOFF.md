# CIS133 Textbook: HANDOFF

**Last updated:** 2026-07-13
**Repo:** https://github.com/jor2050111/cis133
**Live site:** https://jor2050111.github.io/cis133/
**Task list:** cis133-fall26 (`export CLAUDE_CODE_TASK_LIST_ID=cis133-fall26`)

## What Was Done (2026-07-13 Phase 1 publication remediation)

This phase corrected P0 items 1, 2, 3, and 5 from the 2026-07-12 V2
evaluation. P0 items 4 and 6 remain for the next phase.

1. **Source safety:** Reconciled all 145 complete URL occurrences in
   `book/` and `assets/code/` to a 100 percent source manifest. The
   manifest contains 86 unique exact URLs, no broken URL, no unresolved
   URL, and no unsupported source-linked claim. Fixed the Phoenix
   College, Maricopa, National Park Service, City of Phoenix, TLS, and
   accessibility references. Removed URLs from fictional source
   profiles instead of attaching unrelated live pages to fictional
   publishers.
2. **Schedule neutrality:** Removed chapter assignments to weeks,
   course-shell timing, and numbered project checkpoints. The same 12
   chapters now support 9-, 12-, 14-, and 16-week mappings. Optional
   independent-project milestones stay in the instructor layer.
3. **Keyboard access:** Disabled rendered code-line permalinks. The
   rebuilt site contains zero `__codelineno` anchors, down from 950.
   Keyboard and mobile browser checks found no remaining blocker or
   page-level horizontal overflow.
4. **Traceability:** Added explicit teaching-section bindings to all 36
   MLOs. Updated the chapter template and authoring law so future MLOs
   retain the binding.

The full V2 reevaluation scored **88.8 out of 100**, the Strong draft
band. G1 through G5 and G8 pass. G6 remains open because the book still
lacks an open license. G7 remains open because the two deferred
banned-word hits remain at `book/glossary.md:187` and
`book/chapters/chapter-03.md:45`. The scorecard and source manifest live
in `../evaluations/` with the `cis133-2026-07-13-phase-1` prefix.

Verification passed: clean Zensical build, 16 rendered pages, 1,952
internal links and anchors, 45 intended-valid HTML files, 16 CSS files,
two JavaScript files, 75 PNG files, all 12 chapter contracts, all 217
declared glossary terms, and the 221-entry course archive. Pillow 12.3.0
reproduced all nine generated images byte for byte. The Pillow version
is still not pinned and remains a maintenance item.

## What Was Done (2026-07-11 rubric criteria renamed)

The family renamed two Skills Lab rubric criteria so one rubric can
serve non-coding courses (CIS105, future BPC170/270): "Code Accuracy
and Efficiency" is now "Technical Accuracy and Efficiency", and
"Documentation and Code Comments" is now "Documentation Quality". In
this repo: `book/skills-lab-rubric.md` re-synced from the family
master, the link block in chapters 2-12 updated (byte-identical across
the family's 33 blocks), the pattern in
`templates/skills-lab-rubric-template.md` updated, and the CLAUDE.md
rubric law updated. The pending Canvas rubric task must use the NEW
labels.

## What Was Done (2026-07-10 CLO surfacing + restamp: 91.6 CONFIRMED)

Executed this book's slice of the family CLO alignment plan
(`../evaluations/family-clo-alignment-plan-2026-07-10.md`) in commit
`82d64d5`: the twelve elevated CLOs now display verbatim on
`book/index.md`, every chapter opens with a CLO alignment block after
its MLO list (primary alignments, Ch 7: III/XII, Ch 10: V/VIII), and
`templates/chapter-template.md` plus `CLAUDE.md` carry the pattern as
law. A restamp evaluation then re-verified the score at the new head:
all prose-touched mechanical checks rerun clean (CLO verbatim check 12
of 12, structure greps, style law, sentence ceiling, Flesch in band,
clean build), untouched-input checks carried forward from the parent,
and C4 stays 4 because the approved B1 bindings are not implemented
yet. **Index confirmed 91.6, Publication-ready, at `82d64d5`.**
Addendum: `../evaluations/cis133-2026-07-10-clo-restamp-addendum.md`.
Note: `82d64d5` is not yet pushed, so the live site predates the CLO
blocks until the next push.

## What Was Done (2026-07-10 improvement plan Phase A: 87.2 -> 91.6, PUBLICATION-READY)

Executed Phase A of `../evaluations/cis133-2026-07-10-improvement-plan.md`
in full (A1 accuracy sweep, A2 Predict-leak closure, A3 README polish),
then re-scored with the baseline method appendix. Four commits
(`3158fe5`, `ea658f0`, `9a07f1d`, `9e02961`), one per rubric criterion
plus the re-audit tightenings, all pushed, all four Pages deploys green,
live site verified serving the revised text. Post-revision scorecard:
`../evaluations/cis133-2026-07-10-post-revision-scored-rubric.md`.

* **C1 3->4.** All nine enumerated accuracy defects fixed. The landmark
  fix used the pre-authorized B4 minimal option: section/article are now
  "organizing elements inside main," not landmarks, the jump-menu claim
  attaches to the big four only (section 3.2, summary 3.5, Lab 3A,
  both glossary entries), and nothing students build changed. Also:
  print as media type, border order as convention, honest validation
  rationale (standardized recovery hides defects), refresh-button
  revalidation, "light sand" at the 3.04:1 claim, derivable 608px
  budget (Lab 6A now prints the starter's real main rule), background
  under the border, NAT hedge, strong/em voicing hedged to
  machine-readability, W3C "one of the bodies," GIF lossless qualified,
  699/700 fractional hedge, WCAG bold-18.7px large-text clause, 1rem
  as root size, margin collapse banked at the figure example.
* **C5 3->4.** All twenty enumerated Predict leaks closed by the plan's
  move/genericize/repoint pattern. The acceptance re-audit ran: four
  parallel adversarial reviewers re-read all 62 Predicts, none of the
  twenty re-flagged on its cited prose, and four repairs they caught as
  still loose (TIY 1.3, 3.1, 4.1, 11.3, including two chapter-intro
  foreshadows) were tightened in `9e02961`. C5 stops at 4, not 5,
  because the re-audit surfaced a second ring OUTSIDE the enumerated
  twenty (see found-not-fixed below); per session ground rules those
  went to this list, never the diff.
* **C15 4->5.** ch3 README "eight"->nine images (generator comment too;
  generator re-run in a fresh venv on Pillow 12.3.0: asserts pass, git
  status clean, zero drift). ch2 README states the exact contract: 4
  planted errors, exactly 8 validator messages. ch10-12 READMEs state
  the by-reference rule: starter images byte-identical to the prior
  pack (one checksum per file name, verified), dimensions documented in
  the ch3 image table.
* **Full method re-run at `9e02961`:** 45/45 intended-valid HTML zero
  messages, broken-contact exactly 8, flyer exactly 2 ON THE PINNED
  W3.ORG ENGINE (see watchlist below), Jigsaw 16/16 at 0 errors, node
  --check 2/2, sentence checker zero flags 12/12, Flesch 64.9-73.0 all
  in or above band (mean 69.5), style sweep all zeros, chain md5s and
  diffs hold, 36/36 path references resolve, 59 Further Reading URLs
  live (same 9 bot-block 403s, same 4 MDN redirects), build clean,
  deploys green.

**FOUND, NOT FIXED (queue for a C5-closure micro-session; all existed
verbatim at baseline and sit outside the plan's enumerated twenty):**

* TIY 2.4 (chapter-02.md Explain): opens "The browser accepted both.",
  printing the outcome inside the exercise (the TIY 3.5 species). The
  strongest item; it alone blocks C5 = 5.
* TIY 12.3 (chapter-12.md): the receive/re-check/store trip is narrated
  in prose just before the sketch exercise asks students to draw it.
* Explain steps that name the outcome they ask students to explain:
  TIY 4.3 ("why orange won"), TIY 6.4 ("why the contact page's email
  link kept its default blue").
* Run steps that narrate outcomes: TIY 5.1 (body margin + user agent
  attribution; prose at ch5:51 also pre-states the layer), TIY 5.4
  ("watch the lines tighten... falls back to the browser's own
  default").
* TIY 1.1 (chapter-01.md:56): "show you the code it received" directly
  before the what-will-you-see Predict.
* Self-answering titles (stricter lens; decide once whether titles
  count): 10.3 "The Browser's Silent Repair," 11.4 "The Browser Says
  No," 11.5 "The Vanishing Hint," 12.2 "The Lock Drawn on the Door,"
  12.5 "The Five-Minute Pre-Flight." Also TIY 5.5's lead-in "cramped
  on purpose."
* Glossary `W3C` entry still reads "The organization that maintains the
  web's standards" (the ch2 fix's one-word cousin).

**Watchlist addition (sharpens the baseline's pre-term item):** the
ch9 "exactly 2 messages" flyer claim is engine-deployment-sensitive.
validator.w3.org (the engine the chapter points students at) returns
2; validator.nu's current deployment omits the heading-skip message
and returns 1. Verified both ways this session (w3.org via browser
page-context fetch after curl drew Cloudflare all day). Re-check at
pre-term on validator.w3.org itself.

**Decisions made (Mr. Vega, 2026-07-10, end of this session; NONE
IMPLEMENTED YET, next session executes):** B1 approved: inline
"(Section N.X)" MLO bindings in CIS133 now, CIS360's identical item
queued (CIS215 already carries bindings). B2 approved: the validation
harness lives in `../shared/tools/` as the family web-discipline gate,
with its log committed to `docs/execution-logs/` (W3C Nu + Jigsaw +
node --check; sync into cis133 like the Python tools). B3 approved:
embed committed pack illustrations as in-chapter figures with
descriptive alt text, starting at the ch3 image walk-through (chart,
logo, divider). Expected: C4, C14, C10 to 5. Pair the implementation
session with the C5 found-not-fixed micro-closure above.

## What Was Done (2026-07-09 universal rubric: single-source rollout)

The Skills Lab rubric is now single-sourced family-wide. The canonical
master is `../shared/skills-lab-rubric.md`, synced to
`book/skills-lab-rubric.md` (published in the site nav). Chapter 1
transcludes the table at build time with
`--8<-- "skills-lab-rubric.md:rubric"` (pymdownx.snippets enabled in
`zensical.toml`), and chapters 2-12 carry a short link block instead of
the table. This book's labels were already canonical. The cells changed
slightly: criterion 1 is now course-neutral (no HTML/CSS tool list),
the Documentation Mastery cell encodes the WHY-over-WHAT and colleague
standards, and the scoring line states the 8 technical + 8 transferable
split. CLAUDE.md law, `templates/skills-lab-rubric-template.md`, and
the chapter template now describe the single-source pattern.

## What Was Done (2026-07-08 Chapter 12 session, COMPLETES THE BOOK)

ALL 12 CHAPTERS ARE SHIPPED. Part IV and the textbook are complete.

* Wrote and shipped `book/chapters/chapter-12.md` (Scripting
  Concepts and Publishing), the book's second new-coverage chapter
  (no draft module existed): 4 content sections (what scripting
  adds: the client's half, the server's half, hosting and the
  move, the pre-flight and the publish), 5 Try It Yourself
  exercises, 4 Quick Checks, Skills Lab 12A, 409 sentences at 15.1
  words average, zero at 35+. 491 lines, 11 code examples (2 html,
  4 js listings byte-faithful to the pack files, 5 text
  diagrams). Same pipeline as Chapters 4-11.
* Designed 3 MLOs fresh: MLO-12.1 (Understand) ILLUSTRATE what
  scripting adds, client-side and server-side in concept (CLO XI's
  own verb and level, the MLO-1.3/4.3 matching-CLO-verb precedent)
  -> 12.1-12.2, MLO-12.2 (Apply) perform the pre-flight and
  publish with secure transfer -> 12.3-12.4, MLO-12.3 (Create)
  produce the complete six-page club site (CLO XII's own verb) ->
  lab. Rubric byte-identical to chapter-01.md.
* Built `assets/code/chapter-12/`: `starter-site/` (the Lab 11A
  model verbatim: 5 pages including the join form, cmp and diff -r
  verified), `club-palette.txt` (chain ch04->...->ch12),
  `home-content.txt` (officers' front-door text, labeled blocks:
  headline, what-the-club-is, three what-we-do blurbs, three calls
  to action, the standing meeting line), `footer-year.js` (one
  line + WHY comment, span id="footer-year" contract),
  `script-playground.html` + `playground-script.js` (button demo,
  the deliberately insecure pass-phrase gate cactus-club-2026 with
  the supply-closet payoff line, the visit-date line),
  `path-test.html` + a copied image (relative src renders,
  absolute file:///Users/club-officer/... breaks on every machine:
  the upload lesson), `pre-flight-checklist.txt` (8 checks per
  page), `skills-lab-12a-answers.txt` (with LIVE URL line),
  README (both broken-on-purpose disclosures).
* Lab 12A model solution (scratchpad chapter-12-model-solution/)
  IS THE COURSE'S FINISHED SITE: index.html built from
  home-content (title Home | PC Computer Club, h1 The PC Computer
  Club, three CTAs to guide/events/join), Home FIRST in all six
  navs (Home, Recycling Guide, Spring Drive Gallery, Fall Events,
  Join the Club, Contact the Club), footer-year.js attached with
  the copyright span, club-styles.css UNCHANGED (the no-new-CSS
  law held to the last page). The final project references this
  model. No further chapter consumes it.
* All validation executed (2026-07-08/09): Nu zero messages on all
  13 HTML files (validator.w3.org engine 26.7.8, driven through
  the preview browser's page-context fetch after curl drew
  Cloudflare). BY-URL INPUT MODE PROVEN: the validator fetched the
  live textbook site and checked it (9 messages, all site-generator
  chrome, none course-authored: the chapter claims only the input
  mode, never zero-on-live). Jigsaw 0 errors both stylesheets.
  Behavioral checks executed over http AND file:// (identical):
  button before/after strings, gate wrong/right messages with the
  phrase readable at line 19 of the served js, footer year and
  visit date matched system values at run time (recorded as
  match-not-literal), path-test relative renders while absolute
  breaks showing its alt text, model index clean at 375/641/1280
  with the six-link nav wrapping 3/2/1 rows, all six navs in
  site-plan order, zero console errors. Both .js files pass node
  --check. All 5 Further Reading URLs 200 with zero redirects
  (five MDN pages: Publishing your website, What is JavaScript,
  What is a web server, Upload files, How much does it cost).
* Added 12 terms to `book/glossary.md` (JavaScript, script
  element, client-side scripting, server-side scripting, database,
  static site, dynamic page, web host, FTP, SFTP, index.html,
  pre-flight check). Referenced, never re-added: client, server,
  client-server model, HTTP, HTTPS, protocol, query string.
* Ran the three review agents. Applied required fixes: section
  12.2 gained TIY 12.3 "The Trip You Cannot Watch" (a paper-trace
  Predict-Run-Explain: sketch the join list's future before the
  section draws it; the no-server rule kept, and every section
  now carries a TIY per the house standard; the move test and
  pre-flight TIYs renumbered 12.4/12.5), and the glossary's SFTP
  entry's sentence fragment repaired. Applied judgment calls: the
  Chapter 2 relative-links promise given proper quotation marks
  (it is verbatim, confirmed at chapter-02.md line 302), Quick
  Check 12.4 #2 reframed as a soccer-league direct-input-vs-live
  validator split (it had been recall of just-taught content),
  the script-attach fragment's indentation cleaned, Module
  Overview prerequisites line gained Chapter 8's device-mode
  habit, and the PRE-EXISTING glossary sort slip fixed (sitemap
  now precedes site plan, letter-by-letter law). Skipped with
  rationale: Looking Ahead longer than the outline's 2-3
  sentences (it is the book's single closing paragraph), the
  code-example tally counting text diagrams (house convention
  since Chapter 9), MLO-12.1's Understand tag (institutionally
  correct: CLO XI's own level).
* Uncommented the Chapter 12 nav line: ALL 12 CHAPTERS LIVE,
  PART IV COMPLETE. `zensical build --clean`: no issues.

**Chapter 12 design notes:**

* Promises paid (the book's full debt list, each verified against
  its source text): Ch 1's FTP plant (line 170, quoted) and HTTPS
  law (line 284, quoted) and client-server model, Ch 2's
  relative-links-survive-the-move (line 302, quoted verbatim) and
  file://-becomes-https, Ch 3's index.html plant (line 318) and
  self-contained folder, Ch 4's stylesheet-publishes promise and
  the validator URL door, Ch 5's borrowed-font-travels clause, Ch
  7's six-page site plan (closed by name in lab Part 3), Ch 8's
  multi-browser pre-flight plant (line 138, quoted), Ch 9's audit
  re-run (check 4 runs the seven-check instrument), Ch 10/11
  Looking Aheads (home page, server story, pre-flight), Ch 11's
  join-page no-server sentence (quoted verbatim opening 12.2).
* Promises planted: NONE. The book ends. The final project (weeks
  13-15) and "writing scripts is a later course's work" are the
  only forward pointers. The close lands the theme: the course
  ends where the web begins.
* One-mention treatments: FileZilla, Python/PHP/server-side
  JavaScript (one naming sentence), databases (one honest
  sentence), static-vs-dynamic (one breath), the copyright
  entity. Do not deepen.
* Hosting is deliberately generic: the course shell names the
  host and credentials, and the lab carries a hosting contingency
  (pre-flight and zip submit on time even if the host is not
  provisioned). BEFORE THE TERM: provision the course host and
  write the hosting details + credentials flow into the Canvas
  shell, then run one end-to-end publish following lab Part 3.
* Pre-term verification (5 min in a real browser): the playground
  button and gate by hand, path-test opened from Finder, the
  address-input tab on validator.w3.org (the chapter's check 8
  ceremony), VoiceOver on the finished index.html, the Nu probe
  parity items carried from Chapters 10-11.

## What Was Done (2026-07-08 Chapter 11 session)

* Wrote and shipped `book/chapters/chapter-11.md` (HTML Forms):
  4 content sections (the form and the label contract, the input
  family, where the data goes, the accessible styled form), 5 Try
  It Yourself exercises, 4 Quick Checks, Skills Lab 11A, 392
  sentences at 14.5 words average, zero at 35+. 493 lines, 13
  code examples. Same pipeline as Chapters 4-10.
* Consolidated Module 10's three draft MLOs to house format:
  MLO-11.1 (Apply) construct labeled form controls -> 11.1-11.2,
  MLO-11.2 (Apply) DEMONSTRATE how submitted data travels
  (elevated from the draft's Understand-level "explain": lab Part
  3 literally demonstrates it) -> 11.3, MLO-11.3 (Create) design
  the join page collecting only what it needs -> 11.4 plus lab.
  Rubric byte-identical to chapter-01.md.
* Built `assets/code/chapter-11/`: `starter-site/` (the Lab 10A
  model solution verbatim: 4 pages with the events table and
  nav-wrap, cmp-verified), `club-palette.txt` (chain
  ch04->...->ch11), `join-page-notes.txt` (officers' voice:
  required name+email, 5-option select, 4 interest checkboxes,
  questions textarea, the "and nothing else" line, the data
  promise sentence), `session-request.html` + `request-styles.css`
  (the tutoring center's complete labeled form: the TIY
  read-predict-verify object, no :focus rule so the lab adds
  focus styling), `skills-lab-11a-answers.txt`, README.
* Lab 11A model solution (scratchpad chapter-11-model-solution/,
  becomes Chapter 12's starter): join.html (8 for/id-paired
  labels, required+autocomplete on name/email, fieldset/legend
  around the interest checkboxes sharing name="interest", the
  empty-value "Choose one" first option on the optional select,
  the data promise in .reminder, an honest no-server sentence
  planting Chapter 12), Join the Club link on ALL FIVE navs
  (Guide, Gallery, Events, Join, Contact), club-styles.css form
  block (label display block stacking, fieldset label inline,
  controls width 100% + padding + restated type, fieldset input
  width auto, teal 2px :focus ring on every control, button
  club-teal/white with hover/focus twins, one-checkbox-per-p
  stacking with element selectors only).
* SELECTOR DISCIPLINE HELD: Chapter 10's last-new-selector claim
  is binding law. Chapter 11 introduces NO new selector kinds
  (no attribute selectors anywhere), grep-verified by two review
  agents.
* All validation executed (2026-07-08): Nu zero messages on all
  10 HTML files (validator.nu: w3.org Cloudflare-challenged all
  session, parity re-run on the pre-term list). Action-less forms
  and the autocomplete tokens draw nothing. Jigsaw 0 errors on
  all 3 stylesheets. Contrast pairings all on the palette's
  printed list (focus ring 3.04 vs light sand passes the 3:1
  non-text edge). All 5 Further Reading URLs 200 with zero
  redirects.
* BEHAVIORAL verification executed (headless browser over http,
  plus the orchestrator's file:// proof with headless Chrome):
  label clicks focus inputs and select radios, shared-name radios
  exclusive and split names let both check, GET submit lands on
  the same page with exactly
  ?student-name=Jordan+Ortiz&student-email=jordan%40example.org&subject=algebra&session-type=drop-in&notes=
  (space -> +, @ -> %40, empty named control travels, untouched
  select sends its first option), a nameless control stays home,
  unchecked radio groups send nothing, empty required blocked
  with the current-Chrome bubble (quoted hedged), @-less email
  blocked, placeholder vanishes at the first character, repeated
  interest= pairs travel for multi-checked boxes, model join
  page clean at 375/641/1280. FILE:// PROVEN: the same submit
  works identically from file:// (auto-submit probe, query
  string received on the file URL), so TIY 11.3's address-bar
  read works where students actually work. POST probe: python
  http.server answers 501, so POST stays concept-only.
* Added 14 terms to `book/glossary.md` (checkbox, fieldset
  element, form element, GET, input element, label element,
  legend element, name attribute, name-value pair, placeholder,
  POST, radio button, select element, textarea element).
  query string, client-server model, and pseudo-class referenced,
  never re-added.
* Ran the three review agents. Applied required fixes: the
  28-line form-geometry CSS block split in two at the
  labels/controls boundary (the 25-line ceiling), and MLO-11.1's
  "text areas" unified to "textareas" (glossary spelling).
  Applied judgment calls: the temporal "just" in TIY 11.1's
  Explain reworded ("a moment ago"), Quick Check 11.1 #3 given a
  fresh newsletter-signup transfer scenario (it had reused the
  worked example's exact control, leaving the set with two recall
  anchors). Skipped with rationale: glossary entries for label
  and placeholder state the click and vanish behaviors that TIYs
  11.1/11.5 discover (a glossary's job is the complete
  definition, both sit after their TIYs in linear order:
  structural tradeoff, precedent stands), three 15-16 line CSS
  blocks (under the ceiling, Chapter 10 precedent).
* Uncommented the Chapter 11 nav line. `zensical build --clean`:
  no issues.

**Chapter 11 design notes:**

* Promises paid BY NAME: Ch 9's 9.4 label-partnership plant
  (quoted verbatim in 11.1), Ch 1's query string + Lab 1A
  dissection (11.3, the student's own form now writes one), Ch
  1 line 293's collection promise (quoted in 11.3, drives lab
  Part 3's refusal defense and Q&A Q2), Ch 1 line 284's HTTPS
  rule (one POST/GET callback sentence), Ch 10's Looking Ahead
  and Ch 7's brief (the join page, the officers' name-and-email
  ask quoted in the intro).
* Promises planted (pay in Ch 12, explicitly): the server story
  (the form's missing mail carrier: what receives the pairs,
  hosting, secure transfer), the home page, the publish, the
  pre-flight check. The join page's own no-server sentence
  plants it in the club's voice.
* One-mention treatments: password/number/date/file input types,
  input type="submit" as the older spelling, POST (conceptual
  only, NO exercise: the 501 probe is why). Do not deepen.
* Pre-term verification (5 min in a real browser): stock-Chrome
  validation bubble wording and default focus-ring color (the
  chapter names no ring color on purpose), the button hover
  feel on join.html, VoiceOver on join.html (label announced
  with input, legend with each checkbox), one ceremonial file://
  submit of session-request.html, w3.org validator parity for
  the 10 files.

## What Was Done (2026-07-08 Chapter 10 session, opens Part IV)

* Wrote and shipped `book/chapters/chapter-10.md` (HTML Tables):
  4 content sections (the right tool for the data, table structure,
  tables every tool can read, styling tables for readability plus
  the phone wrapper and Final Checkpoint 2), 6 Try It Yourself
  exercises, 4 Quick Checks, Skills Lab 10A, 337 sentences at 14.6
  words average, zero at 35+. 476 lines, 10 teaching code examples
  plus 2 quoted Nu messages. Same pipeline as Chapters 4-9,
  including the orchestrator browser-verification pass (independent
  second execution of the asset agent's numbers: all matched).
* Consolidated Module 9's three draft MLOs to house format:
  MLO-10.1 (Analyze) differentiate tabular data via the two-axes
  test -> 10.1, MLO-10.2 (Apply) construct accessible tables with
  headers, scope, captions -> 10.2-10.3, MLO-10.3 (Create) produce
  the styled events page -> 10.4 plus lab. MLO-10.3 is THE BOOK'S
  FIRST CREATE-LEVEL MLO (Part IV's reserved tier). Rubric
  byte-identical to chapter-01.md.
* Built `assets/code/chapter-10/`: `starter-site/` (the Lab 9A
  model solution: pages byte-identical to chapter-09's, stylesheet
  carries ONLY the rem conversions: body 1rem, h1 2.5rem, h2
  1.5rem, query h1 2rem), `club-palette.txt` (cmp chain
  ch04->...->ch10), `events-content.txt` (the six fall events,
  word-for-word from the Chapter 7 brief, labeled fields = the
  table's five columns), `table-practice.html` +
  `practice-styles.css` (the spring drive tally, NO
  thead/tbody/caption on purpose: TIYs add them),
  `wide-practice.html` (7-column drop-off log, complete
  structure, engineered to overflow a phone),
  `skills-lab-10a-answers.txt`, README. PRACTICE DATA = THE
  CHAPTER 3 CHART'S DATA exactly (Cables 64, Phones 38, Laptops
  21, Small electronics 17, Tablets 14, sum 154, chart order):
  one truth, two presentations, asserted by parsing the shipped
  files. Wide-practice per-date splits sum to those counts.
* Lab 10A model solution (scratchpad chapter-10-model-solution/,
  becomes Chapter 11's starter): events.html (caption, thead with
  5 th scope="col": Event/Date/Time/Location/Details, six tbody
  rows, .table-scroll wrapper div), nav Recycling Guide / Spring
  Drive Gallery / Fall Events / Contact the Club on all four
  pages, club-styles.css table block (collapse, width 100%, white
  base, ink 1px cell borders, 8px 12px padding, text-align left,
  caption deep teal bold, thead white-on-club-teal 4.69, zebra
  ink-on-sand 6.81, hover ink-on-light-sand 8.19 placed after the
  stripe rule, .table-scroll overflow-x auto) plus ONE base
  change: `nav ul` gained flex-wrap wrap (browser-proven: four
  links need ~415px, three fit 375 exactly). The lab surfaces the
  nav overflow as a Part 3 phone-test discovery repaired with
  Chapter 6's flex-wrap.
* All validation executed (2026-07-08): Nu zero messages on all 9
  files (starter pages, practice pages, 4 model pages; six on
  validator.w3.org engine 26.7.8, the rest on validator.nu after a
  Cloudflare rate limit: same engine). Nu probes captured verbatim:
  misplaced caption = ERROR ("Element caption not allowed as child
  of element table in this context..."), ragged row = WARNING
  ("...was 1 columns wide, which is less than the column count
  established by the first row (2)."). Jigsaw 0 errors on all
  three stylesheets. Contrast ratios all on the palette's printed
  passing list. Date and sum asserts all pass. All 5 Further
  Reading URLs 200 (two MDN pages cited at their new Reference
  final URLs).
* Browser-verified twice (asset agent headless + orchestrator
  preview server, matching numbers): naked table 0px borders and
  auto-inserted tbody wrapping all 6 rows, zebra with auto tbody
  paints data rows 1/3/5 (header counts as position one) and
  shifts to 2/4 with explicit thead/tbody (TIY 10.5's chained
  discovery), wide table overflows 375px by 199px and the wrapper
  contains it (550px content in 327px window), model events page
  clean at 375/640/641/1280 with the h1 2rem/2.5rem step and nav
  wrap, collapse probe 147px vs 140px.
* Added 13 terms to `book/glossary.md` (border-collapse, caption
  element, data cell, header cell, :nth-child(), scope attribute,
  structural pseudo-class, table element, table row, tabular data,
  tbody element, thead element, zebra striping) and extended the
  existing pseudo-class entry from state-only to state-or-position.
* Ran the three review agents. Applied required fixes: THREE TIY
  answer leaks closed (TIY 10.1's worked table had pre-classified
  the exercise's target, so the TIY now runs on three fresh
  candidates: tutor roster, tip list, hours paragraph. TIY 10.2's
  th-bold-centered default was pre-stated, now discovered. TIY
  10.6's wrapper outcome was narrated in prose, now held to a
  policy statement with the outcome as the discovery, and the
  judging admonition moved after the exercise), the false Chapter
  5 attribution corrected ("readability contract" -> the actual
  four-point checklist), and the glossary's border-collapse entry
  re-sorted before border shorthand. Applied judgment calls: the
  29-line finished-schedule example trimmed to 22 (one tbody row),
  Quick Check 10.1 #1 given a fresh printer-loan-log scenario,
  :nth-child() spelling standardized (chapter Key Terms + glossary
  key now both carry the parens). Skipped with rationale: 10.4's
  five H3 subsections (house precedent counts TIY/QC H3s, every
  shipped chapter exceeds the literal 2-4 band), QC 10.3/10.4
  first questions as recall anchors (one allowed per set), the
  Create-level grading emphasis note (rubric's Analysis criterion
  already carries it).
* Uncommented the Part IV nav block with only Chapter 10 live.
  `zensical build --clean`: no issues.

**Chapter 10 design notes:**

* Promises paid: Ch 9's Looking Ahead (headers, scope, captions
  continue the accessibility work: 10.3 opens by redeeming it),
  Ch 7's brief (the events page finally publishes the six events),
  Ch 8's no-sideways-scroll law (the wrapper repair), Ch 3's chart
  (the practice table restates its exact data), Final Checkpoint 2
  hosted at the end of 10.4 (Ch 7's Checkpoint 1 register).
* Promises planted (pay these explicitly): Ch 11 = the join page,
  forms, the label-input contract Chapter 9 promised. Ch 12 = the
  home page arrives, the whole site publishes behind a full
  pre-flight check.
* colspan/rowspan and tfoot are deliberate one-mention items.
  :nth-child() is deliberately the course's LAST new selector
  (only even/odd taught, pattern arguments left to Further
  Reading). Do not deepen any of these.
* Pre-term verification (5 min in a real browser): VoiceOver (or
  any screen reader) on the model events page (caption announced,
  cell read with its column header), the hover-beats-stripe feel
  check on the events table, re-POST the two Nu probe files to
  validator.w3.org once its rate limit cools (validator.nu
  recorded the verbatim messages; parity expected), and TIY 10.3's
  DevTools auto-tbody view in current Chrome/Edge/Firefox.

## What Was Done (2026-07-08 Chapter 9 session, closes Part III)

* Wrote and shipped `book/chapters/chapter-09.md` (Web
  Accessibility): 4 content sections (WCAG/POUR/conformance levels,
  structure every tool can read, perceivable content: color/type/
  images, the audit: evaluators and human checks), 6 Try It Yourself
  exercises, 4 Quick Checks, Skills Lab 9A, 387 sentences at 14.8
  words average, zero at 35+. 490 lines, 9 code examples. PART III
  IS COMPLETE and its milestone (plan, adapt, include) closes in Lab
  9A Part 3. New coverage: no draft module existed. Same pipeline as
  Chapters 4-8 including the orchestrator browser-verification step.
* Designed 3 MLOs fresh (no course-map module): MLO-9.1 (Apply)
  implement accessible structure and navigation -> 9.2, MLO-9.2
  (Apply) apply WCAG perceivability rules to color/type/images ->
  9.3, MLO-9.3 (Evaluate) evaluate pages against Level AA with an
  evaluator and human checks -> 9.4 plus lab. Section 9.1 is the
  framework section (thematic mapping, house pattern). Rubric
  byte-identical to chapter-01.md.
* Built `assets/code/chapter-09/`: `starter-site/` (the Lab 8A
  model solution: viewport tags on all 3 pages, one max-width 640px
  query block with gallery figures 100%, main padding 24px 8px, nav
  a padding 12px 16px, h1 40->32px step-down as the Part 3
  refinement choice), `drive-day-flyer.html` + `flyer-styles.css`
  (the audit target with EXACTLY 8 planted barriers: h1->h3 skip,
  two Click-here links counted once, missing alt on an informative
  image, verbose alt on the decorative divider, #c99b66-on-#fdeecd
  body text at 2.19:1, color-alone "shown in red" signal,
  outline: none with no replacement, hard 11px body),
  `flyer-images/` (2 byte-copies, self-contained), `club-palette.txt`
  (cmp chain intact), `contrast-cards.txt` (TIY pairs: 10.12 pass,
  4.12 near-miss fail, 1.88 clear fail, ratios not printed in the
  file), `rem-demo.html` + `.css` (three specimens 16px/1rem/1.5rem),
  `accessibility-checklist.txt` (7 human checks),
  `skills-lab-9a-answers.txt`, README (flyer-broken-on-purpose and
  Lab-8A-lineage disclosures). INSTRUCTOR DEFECT KEY lives in the
  session facts sheet (scratchpad chapter-09-facts.md), not the
  README.
* All validation executed (2026-07-08): Nu zero on the 3 starter
  pages and rem-demo, the flyer fails with exactly 2 messages
  (missing alt + heading skip: the validator layer catches 2 of the
  8, and lab Q1's tool-stack assignment honors it), jigsaw 0 errors
  on all three stylesheets, contrast ratios computed in Python
  (2.19 flyer, cards 10.12/4.12/1.88, re-verified 4.85 light sand
  on deep teal and 1.26 old wart, 21.00/1.00 scale anchors), all 8
  candidate URLs 200 (WAVE, WAVE extension, WebAIM contrast
  checker, WCAG22 quickref, W3C WCAG overview, MDN Accessibility,
  A11Y Project checklist, WebAIM POUR).
* Orchestrator browser-verified (preview server): the starter's
  query block on both sides of 640 (figures 623px/1-per-line vs
  296px/2-per-line, both padding changes, h1 step), all 8 flyer
  defects rendering live, rem-demo root-size response (16/16/24 at
  default root, 16/20/30 at a 20px root).
* Added 10 terms to `book/glossary.md` (WCAG, POUR, perceivable,
  operable, understandable, robust, conformance level, contrast
  ratio, accessibility evaluator, keyboard navigation). Collision
  discipline held: accessibility, alt text, the three image kinds,
  rem, and screen reader were NOT re-added.
* Ran the three review agents. Applied required fixes: TIY 9.6
  "First WAVE" added to section 9.4 (wave.webaim.org on the W3C
  home page, prediction open-ended, no unverified report claims),
  restoring the every-section-has-a-TIY standard, and the
  prerequisites line widened to Chapters 3-8 (it had omitted
  Chapter 5, whose px/rem distinction the chapter depends on).
  Applied judgment calls: the second legal-standards clause cut
  (one-mention discipline), Quick Check 9.2 #1's heading pattern
  freshened to h1/h2/h2/h5 (it had reused the worked example
  verbatim), Review Q4's skip changed to h3->h5 (third reuse of the
  same pattern), a bridging sentence added after the focus-repair
  example noting Chapter 6's background flip also satisfies the law
  (TIY 9.3 anchoring risk), and the 8-barrier count clarified in
  the lab and README ("counting a barrier once even where it
  strikes twice": the two Click-here links are one barrier).
  Skipped with rationale: the alt four-jobs table restating three
  known kinds (the lab needs the table as a working reference), QC
  9.1 #3 at recall level (a QC set may carry one recall anchor),
  QC 9.4 #2's two-finding triage rehearsal (deliberate scaffolding
  for the lab's 8-finding version), bare "DevTools" without the
  "browser DevTools" first-mention (matches shipped Chapters 2/3/7,
  a book-wide pass would be the fix, not a Ch 9 edit).
* Uncommented the Chapter 9 nav line: PART III FULLY LIVE.
  `zensical build --clean`: no issues.

**Chapter 9 design notes:**

* Promises paid: Ch 4's "math behind the palette's passing list"
  (the 1-to-21 scale, AA thresholds, 4.85 decoded, the 1.26 wart
  named invisible ink), Ch 5's "rem and user settings" (9.3 + the
  lab's px-to-rem conversion), Ch 6's ":focus opened the keyboard
  door" (the law is WCAG 2.4.7, cited once as a naming sample),
  Ch 7's accessibility-principle plant (the framework arrives),
  Ch 8's "every screen size served, now every user" (intro), Ch
  3's alt-decision deepening (four jobs, complex images new) and
  Devon's return, Ch 1's social framing (one paragraph, one legal
  sentence).
* Promises planted (pay these explicitly): Ch 10 = the events page
  from the Lab 7A site plan gets its content, accessible tables
  (headers, scope, captions) continue this work. Ch 11 = the forms
  accessibility contract (label-input partnership), the join page.
  Ch 12 = the pre-flight check runs this chapter's audit before
  publishing. Final project = checkpoint pages arrive auditable.
* ARIA, VoiceOver/NVDA, legal obligations (one sentence), AAA
  (described not pursued), and WCAG criterion numbers (2.4.7 only)
  are deliberate one-mention treatments. Do not deepen.
* Pre-term verification (5 min in a real browser): the WAVE online
  tool's summary panel on w3.org (TIY 9.6 asserts nothing about
  its findings), the WAVE extension install flow, the browser
  settings path for default font size in Chrome/Edge/Firefox (TIY
  9.5), a 200 percent zoom walk on the starter site (TIY 9.1), and
  the WebAIM contrast checker UI (TIY 9.4).

## What Was Done (2026-07-08 Chapter 8 session)

* Wrote and shipped `book/chapters/chapter-08.md` (Responsive Design
  and Media Queries): 4 content sections (one site every screen, the
  viewport meta tag, media queries and breakpoints, base styles plus
  overrides), 5 Try It Yourself exercises, 4 Quick Checks, Skills
  Lab 8A, 392 sentences at 15.1 words average, zero at 35+. 480
  lines, 9 code examples. Same orchestrated pipeline as Chapters
  4-7, plus a NEW PIPELINE STEP: the orchestrator browser-verified
  every layout claim with a local preview server before drafting
  (results appended to the session facts sheet).
* Consolidated Module 8's three draft MLOs into house format:
  MLO-8.1 (Apply) implement the viewport meta tag, tested in
  DevTools device mode -> 8.1-8.2, MLO-8.2 (Apply) construct media
  queries at content-driven breakpoints -> 8.3, MLO-8.3 (Analyze)
  diagnose where layouts fail and which base-plus-overrides layer
  owns the fix -> 8.4 plus lab. Rubric byte-identical to
  chapter-01.md.
* Built `assets/code/chapter-08/`: `starter-site/` (byte-identical
  copy of chapter-07/club-site, cmp-verified, still no viewport
  tag: adding it is Lab Part 1), `club-palette.txt` (cmp-verified
  chain ch04->ch05->ch06->ch08), `query-playground.html` + `.css`
  (the club bulletin bench, queries pre-written for
  read-predict-verify), `no-viewport.html` + `viewport.html` (TIY
  8.2 pair, bodies byte-identical, heads differ by one line),
  `skills-lab-8a-answers.txt`, README.
* Engineered and BROWSER-VERIFIED numbers (preview server,
  2026-07-08): body background flips light sand to sunset orange at
  exactly 600px (inclusive), .banner-title 22/28/36px at
  400/700/1000 with the 501-899 neither-query gap, .update-card
  padding 10px at and below 600 and 20px above, card row wrap
  thresholds exact at 584/864/1144, and the starter gallery (with a
  viewport tag injected) seats 2 figures at 640px and 1 at 639px:
  the lab's expected content-driven breakpoint derivation is
  browser-exact. BONUS: the preview environment emulated the
  no-viewport ~980px layout viewport live, executing the "phone's
  lie" claim.
* All validation executed (2026-07-08): Nu zero messages on all 6
  pack HTML files (and Nu confirmed it does NOT require a viewport
  tag: the chapter frames that as "valid and phone-ready are
  different standards"), jigsaw 0 errors both stylesheets, at-rule
  grep of Chapters 1-7 came back zero so @media is truthfully the
  course's first at-rule, all 5 Further Reading URLs 200 (two MDN
  URLs cited at their final redirect targets).
* Added 11 terms to `book/glossary.md` (base styles, breakpoint,
  device mode, media query, mobile-first, override, responsive
  design, viewport, viewport meta tag, plus at-rule and media
  feature from review).
* Ran the three review agents. Applied required fixes: the img
  max-width provenance corrected from "Chapter 5 pack, promised
  twice" to the truth (Chapter 6 pack, one README promise) in both
  the chapter and the pack README, TIY 8.3's answer leak closed
  (the anatomy example now teaches on an invented tutoring center
  rule at 720px instead of printing the playground's real 600px
  block with its outcome narrated), TIY 8.4's gap leak closed (the
  501-899 resolution sentence replaced with the general
  a-pair-can-leave-a-gap concept, students now derive it). Applied
  judgment calls: MLO-8.1's verb Prepare swapped to the approved
  Implement, MLO-8.3 reworded to one verb with two objects
  (MLO-5.3 pattern), at-rule and media feature bolded and
  glossaried (Quick Check 8.3 quizzes them by name), prerequisites
  line unified to "Chapters 5-7", Quick Check 8.3 #3's breakpoint
  chart number swapped 768 -> 1024 (768 was the section's own
  worked anti-pattern). Skipped with rationale: the banner-title
  example reuse across TIY 8.4 and 8.4's cascade trace (deliberate
  scaffolding, same numbers two skills), 9 code examples near the
  band floor (in band), TIY 8.1's inventory-implication (reviewer
  ruled it stops short of a leak).
* Uncommented the Chapter 8 nav line. `zensical build --clean`: no
  issues.

**Chapter 8 design notes:**

* Promises paid: Ch 6's "flex-wrap is half of responsive design"
  (quoted and paid through 8.3-8.4), Ch 7's phone-width wireframe
  becomes buildable (intro and lab), Ch 5's "the column learns to
  adapt to any screen" (8.1's max-width-as-ceiling inventory), Ch
  4's one-stylesheet promise (8.4's file-grew-layers framing), the
  Chapter 6 pack README's img max-width promise (8.1, fluid
  images).
* Promises planted (pay these explicitly): Ch 9 = every screen size
  is served, now every user: WCAG, POUR, the contrast math, what
  rem does for visitors who resize type. Ch 12 = the pre-flight
  check renders the site in multiple browsers and screen sizes
  before publishing. Final project = Checkpoint 2 draft pages
  arrive responsive.
* Orientation and print media features, device-width charts (named
  to be argued against), and the ~980px default (hedged "most
  phone browsers... about 980 pixels") are deliberate one-mention
  or hedged treatments. Do not deepen.
* Pre-term verification (5 min in a real browser): DevTools device
  toolbar location and device list naming in current
  Chrome/Edge/Firefox (the chapter deliberately avoids precise UI
  names), Wikipedia's narrow-window visual adaptation (TIY 8.1),
  no-viewport.html vs viewport.html on a physical phone or device
  mode (TIY 8.2), the playground flip at 600 on a real machine
  (TIY 8.3, browser-verified locally this session).

## What Was Done (2026-07-08 Chapter 7 session, opens Part III)

* Wrote and shipped `book/chapters/chapter-07.md` (UX and Web Design):
  4 content sections (plan before you code, UX/UI and the five
  principles, sitemaps and wireframes, navigation design and the site
  plan), 5 Try It Yourself exercises, 4 Quick Checks, Skills Lab 7A,
  404 sentences at 14.1 words average, zero at 35+. ~482 lines. Same
  orchestrated pipeline as Chapters 4-6. Planning chapter: exempt by
  design from the 8-15 code-example band (Chapter 1 precedent), it
  carries 4 text diagram blocks (tutoring center sitemap, two
  wireframes, box-to-landmark mapping) plus one HTML skeleton and one
  CSS flex rule. Chapter 7 hosts the final project kickoff (Final
  Checkpoint 1: the site plan).
* Consolidated Module 7's four draft MLOs into exactly 3:
  MLO-7.1 (Analyze) differentiate UX from UI via the five principles
  -> 7.1-7.2, MLO-7.2 (Apply) construct sitemap and wireframes ->
  7.3 (Construct-as-Apply per the MLO-6.3 precedent), MLO-7.3
  (Evaluate) critique navigation and consistency to produce a site
  plan -> 7.4 plus lab Parts 1 and 3. Rubric byte-identical to
  chapter-01.md (diff-verified by two review agents).
* Built `assets/code/chapter-07/` (planning artifacts, no starter
  code): `club-site/` (the Lab 6A model solution rebuilt from the
  chapter-06 pack plus the HANDOFF rule list: header flex row,
  .drive-gallery wrap row with 296px figures, footer-link wart FIXED
  FOR KEEPS with footer a light sand, hover/focus twins, full nav
  bar, centered .page-divider), `project-brief.txt` (officers'
  expansion brief: home page, events page, join page, 3 goals, 2
  audiences, 6 date-verified events, never says table or form),
  `ux-audit-worksheet.txt` (five principles, blank findings),
  `site-plan-template.txt` (serves Lab 7A AND Final Checkpoint 1),
  `wireframe-examples.txt` (generic ASCII frames, desktop 65-char
  and phone 29-char), `skills-lab-7a-answers.txt`, README with two
  disclosures (wart fixed, no palette file because wireframes are
  deliberately grayscale).
* Lab 7A design: Part 1 digests the brief and audits the shared
  club-site copy against the five principles (the missing home page
  is the discoverable headline gap, never announced in prose),
  Part 2 constructs the six-page sitemap (Home, Guide, Gallery,
  Events, Join, Contact) and wireframes two pages at two widths,
  Part 3 assembles the stakeholder-ready site plan with a
  self-critique and one-user test plan.
* All validation executed (2026-07-08): Nu zero messages on all 3
  club-site pages, jigsaw 0 errors on club-styles.css, every pairing
  from the palette passing list (4.69:1 and 4.85:1, no new math),
  Wikipedia Recycling still renders 1 main and 12 nav, MDN top-nav
  labels recorded for TIY 7.3, WebAIM nav labels recorded for TIY
  7.5, phoenixcollege.edu WAF-blocked (TIY 7.1 asserts nothing about
  its contents), all 5 Further Reading URLs 200 (A List Apart cited
  at its final long-form URL).
* Added 13 terms to `book/glossary.md` (accessibility, consistency,
  feedback, navigation label, prototype, responsiveness, site plan,
  sitemap, target audience, usability, UX, UI, wireframe).
* Ran the three review agents. Applied required fixes: the site-plan
  table's last row had swallowed the following paragraph (silent
  content loss confirmed in rendered HTML, fixed and render-verified),
  and the focus-outline attribution split correctly across Chapter 3
  (alt text, landmarks) and Chapter 6 (focus outlines). Applied
  judgment calls: two "just" fillers cut, Quick Check 7.3 #3 rewritten
  as a fresh soccer-league footer scenario (it nearly re-asked the
  section's own worked card-row example), lab Part 1 co-tagged with
  MLO-7.3 (its audit is critique work, Chapter 3 label precedent).
  Skipped with rationale: 7.3's length imbalance (the diagram-heavy
  core is the chapter's point), 7.4's six subsections (Chapter 6
  precedent), the backtick-vs-linked Wikipedia URL style (book-wide
  split, cleanup candidate), lab Part 3's assemble verb read as
  Create (Create is reserved for Part IV, assembly sits under
  MLO-7.2's Construct), and the thematic MLO-to-section offset
  (shipped house pattern since Chapter 1).
* Uncommented the Part III nav block with only Chapter 7 live.
  `zensical build --clean`: no issues.

**Chapter 7 design notes:**

* Promises paid: Ch 6's "you can build any layout you can sketch,
  learn to sketch deliberately" (7.3's box-to-landmark payoff), Ch
  6's hover/focus named as the feedback principle in action (7.2),
  Ch 3's descriptive link text rule returning as nav-label law
  (7.4), Ch 4's one-stylesheet consistency engineering (7.2), Ch 1's
  source-evaluation habit connected to audience research (7.1).
* Promises planted (pay these explicitly): Ch 8 = the phone-width
  wireframe cannot be fully built yet, flex-wrap is half and media
  queries finish it. Ch 9 = the accessibility principle's full
  framework (WCAG, POUR, the contrast math). Ch 10 = the events
  page's schedule content wants a table. Ch 11 = the join page's
  signup wants a form. Ch 12 = the home page becomes index.html and
  the plan's site ships. Final Checkpoint 2 (draft pages) lands near
  Chapter 10.
* Personas, prototypes/Figma, breadcrumbs, F/Z scanning patterns,
  and usability testing are deliberate one-mention previews. Do not
  deepen in place.
* IMPORTANT for Chapter 8: `assets/code/chapter-07/club-site/` is
  the Lab 6A model solution and Chapter 8's starter site. Copy it
  into the chapter-08 pack rather than rebuilding.
* Pre-term verification (5 min in a real browser): phoenixcollege.edu
  home page's calls to action (TIY 7.1, WAF blocks curl), the
  Wikipedia article's contents sidebar and Tab focus visibility
  (TIY 7.2/7.4), MDN's top nav labels (TIY 7.3), WebAIM's nav labels
  (TIY 7.5).

## What Was Done (2026-07-08 Chapter 6 session, closes Part II)

* Wrote and shipped `book/chapters/chapter-06.md` (Layout with
  Flexbox): 4 content sections (the Flexbox model, controlling the
  line, combinators and pseudo-classes, the navigation bar capstone),
  5 Try It Yourself exercises, 4 Quick Checks, Skills Lab 6A, 367
  sentences at 14.0 words average, zero at 35+. ~498 lines. Same
  orchestrated pipeline as Chapters 4-5. PART II IS COMPLETE and the
  full Part II nav block is live.
* Consolidated Module 6's five draft MLOs into exactly 3 (the old
  module-06 task file was a byte-duplicate of module-05, so Lab 6A
  was designed fresh): MLO-6.1 (Apply) flex containers and line
  control -> 6.1-6.2, MLO-6.2 (Analyze) differentiate by tree
  relationship and interaction state -> 6.3, MLO-6.3 (Apply)
  construct the accessible navigation bar -> 6.4. The pedagogy agent
  downgraded MLO-6.3 from the outline's Create to Apply: the
  taxonomy reference's own canonical Apply example IS "construct a
  responsive menu bar using flexbox and the nav element." Rubric
  byte-identical to chapter-01.md.
* Built `assets/code/chapter-06/`: `starter-site/` (the Lab 5A model
  solution, wart intact), `club-palette.txt`, `flex-playground.html`
  + `.css` (four 220px announcement cards, gap 16, wrap threshold
  near 980px, card TWO longest for cross-axis demos),
  `skills-lab-6a-answers.txt`, README with the wart disclosure.
* Lab 5A model solution key calls (in the starter's club-styles.css):
  box-sizing border-box first, body margin 0 + Verdana/Arial/
  sans-serif + 16px + line-height 1.5, header/nav/footer padding,
  main max-width 640px centered with 24px 16px padding,
  #meeting-times 4-value padding + club teal border-left, figure sand
  borders, Oswald h1/h2 via the single-link form, img max-width 100%
  (shipped ahead of Ch 8, README disclosed), .page-divider class.
  Full rule list in the session facts sheet.
* Lab 6A model solution (built and BROWSER-VERIFIED this session,
  lives in the session scratchpad): header display flex + wrap +
  align-items center + gap 16 (logo and h1 verified sharing line one,
  h1 dead-centered, intro paragraphs each full-width), .drive-gallery
  flex wrap gap 16 with 296px figures (verified two per line in the
  640px column, third wrapping), footer a light sand, nav/footer
  hover+focus states, full nav ul/nav a bar, .page-divider display
  block + margin auto.
* All validation executed (2026-07-08): Nu zero messages on all 4
  pack HTML files, jigsaw 0 errors on both stylesheets, light sand
  on deep teal computed 4.85:1 PASS (the footer fix), wart 1.26:1
  FAIL recorded, all 5 Further Reading URLs 200. Layout claims
  browser-executed via a local preview server (bounding-box measured).
* Added 17 terms to `book/glossary.md`.
* Ran the three review agents. Applied required fixes: MLO-6.3
  Create->Apply with verb Construct, MLO-6.2 rewritten to one verb
  (Differentiate), TIY 6.4's census leak closed (prose reach
  explanation genericized, the two-links reveal removed from the
  Predict), the palette file gained the LIGHT SAND on DEEP TEAL line
  in all three chapter copies (byte-identical, cmp-verified), and
  UPSTREAM: chapter-05.md's Lab 5A critique prompt broadened from
  "spacing or typography" to "styling" so the footer-link wart is a
  legitimate 3.B answer (Chapter 6's origin story depends on it).
  Applied judgment calls: three Quick Check items rewritten as fresh
  transfer scenarios (QC 6.1 #2, QC 6.4 #1 and #3), Q&A Q1 given a
  comparative frame to reach Analyze, flex-shrink name-drop removed,
  "browser DevTools" on first mention, Read-the-Bar-Back display:
  block attribution made precise. Skipped with rationale: TIY
  6.4/6.5 running on the real site (deliberate capstone graduation,
  plan-compliant), the 5-subsection count in 6.2 and 6.4 (content
  coherence beats the 2-4 band, scope agent called both folds
  optional), TIY 6.5's space-between reuse (new item count and a
  design judgment make it genuine transfer), invented demo classes
  (.officer-roster etc.) not shipping in files (they are the
  anti-leak mechanism).
* Uncommented the Chapter 6 nav line: Part II fully live.
  `zensical build --clean`: no issues.

**Chapter 6 design notes:**

* Promises paid: Ch 4's nav-bar promise (6.4 + lab Part 3), Ch 4's
  specificity cameo (6.3, one paragraph, no scoring), Ch 5's
  "Flexbox arranges the boxes" and the footer-link wart (fixed live
  in 6.3, for keeps in lab Part 2), Ch 5's text-decoration caveat
  (nav links drop underlines with the affordance case argued).
* Promises planted (pay these explicitly): Ch 7 = sketch layouts
  deliberately, wireframes, the site plan (Final Checkpoint 1).
  Ch 8 = flex-wrap is half of responsive design, media queries
  finish it. Ch 9 = :focus opened the keyboard door, WCAG walks
  through it. Ch 12 = the multi-page site with real navigation ships.
* Child combinator, specificity, flex-direction column layouts, and
  responsive design are deliberate one-mention/limited previews. Do
  not deepen in place. flex-grow/shrink/basis are deliberately
  untaught.
* Pre-term verification (5 min in a real browser): drag the
  playground window past the ~980px wrap threshold, Tab-key focus
  stepping in current Chrome/Edge/Firefox, the header row and
  gallery at a phone-width window (laptop widths were
  browser-verified this session), default link blue eyeballed once.

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

THE TEXTBOOK IS COMPLETE: all 12 chapters shipped, all 12 asset
packs built, the full nav live, every build clean. What remains is
course operations, not authoring:

1. Before the term starts: run each chapter's 5-minute pre-term
   browser verification list (every "What Was Done" section above
   carries one; Chapters 1-3 and 9-12 have the meatiest).
2. Provision the course web host, write the hosting details and
   credentials flow into the Canvas shell (Lab 12A and the final
   project depend on it), and run one end-to-end publish following
   Lab 12A Part 3.
3. Assemble the course data pack zip for Canvas from assets/code/
   (all 12 chapter folders plus the _generators note) and post it
   per the CLAUDE.md loading convention.
4. Refine the `module-*-task.html` Canvas pages against the
   shipped Skills Labs, and set assessment weights in
   docs/part-structure.md before syllabus publication.
5. DONE 2026-07-09: the Lab 12A model solution (the course's
   finished six-page site) is preserved on Drive at
   `co-professor/01-teaching/05-cis133-web-development/textbook-instructor-materials/lab-12a-model-site/`
   with a README. It stays out of this public repo on purpose
   (answer-key discipline). The Chapter 10/11 model solutions
   need no copy: each ships as the next chapter's starter-site.

## How to Continue

Open a session in `~/Documents/code/textbooks/cis133/`, read CLAUDE.md
and this file, then start with Next Steps. The authoritative course
reference is `docs/CIS133_CLOs.md`. The authoritative structure is
`docs/part-structure.md`.
