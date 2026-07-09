# CIS133 Textbook: HANDOFF

**Last updated:** 2026-07-08
**Repo:** https://github.com/jor2050111/cis133
**Live site:** https://jor2050111.github.io/cis133/
**Task list:** cis133-fall26 (`export CLAUDE_CODE_TASK_LIST_ID=cis133-fall26`)

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

1. Write Chapter 10 (HTML Tables), opening Part IV. Same cycle as
   Chapters 4-9. Consolidate Module 9's three draft MLOs (identify
   table components, style tables with CSS, create an accessible
   styled table page) to house format. Pay Chapter 9's plant: the
   events page from the Lab 7A site plan finally gets its content
   (the chapter-07 project-brief.txt lists the 6 events with
   dates/times/locations: that content becomes the table), and
   accessible tables (th, scope, caption) continue Chapter 9's
   work. Starter site: the Lab 9A model solution (club site with
   rem conversions; rebuild from the chapter-09 answers + facts
   sheet key). Chapter 10 also hosts Final Checkpoint 2 (draft
   pages) per docs/part-structure.md.
2. Then Chapter 11 (HTML Forms: the join page, the label-input
   contract) and Chapter 12 (Scripting Concepts and Publishing,
   the other new-coverage chapter).
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
