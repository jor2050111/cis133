# CIS133 Pedagogy Upgrade Plan (Copperwind Website Spine)

**Date:** 2026-07-28 (revision 2, after the Codex adversarial review)

**Branch:** `pedagogy-upgrade` (never push to `main`: a push deploys)

**Pre-upgrade snapshot:** `../cis133-archive/` and commit `00c482d`

**Governing documents:**

* `../../PEDAGOGY-UPGRADE-PLAYBOOK-V1.md` (the workflow, V1.1)
* `../../evaluations/tech-learning-book-findings-2026-07-28.md` (the research)
* `../../cis215/docs/pedagogy-upgrade-plan-2026-07-28.md` (the pilot
  spec: source of the Copperwind canonical facts)

**Prime directive:** This book stands at 91.6/100 (Publication-ready)
with every layout number browser-verified, every validator claim
executed, and a complete source manifest. The upgrade changes the
scenario and adds the five upgrades. It does NOT rewrite teaching
content, restructure sections, touch MLOs, CLO blocks, Quick Check
counts, rubric blocks, or the selector discipline. Every number stated
in prose that an edit could move (wrap thresholds, contrast ratios,
file sizes, validator message counts) is re-verified after the edit,
with the same instrument the original session used.

## 1. The scenario change: from the PC Computer Club to Copperwind

CIS215 (the pilot) put students INSIDE Copperwind as its data analyst.
CIS133 approaches the same fictional universe from the other side:
**students are hired to build Copperwind's community program website.**
The club scenario retires. The site students build, page by page,
chapter by chapter, is the same site in structure: only the
organization behind it changes.

### 1.1 The spine organization (canonical facts, family-wide)

**Copperwind IT Services** is a fictional managed IT services provider
(MSP) in Phoenix, Arizona. About 30 employees. Two support teams,
**Deskside** and **Network Ops**, with 8 technicians total. Roughly 40
client companies across the Valley. These facts are canonical across
the textbook family and come from the CIS215 spec. Reuse them exactly.
Never invent conflicting facts.

**Canonical cast (the 8 technicians, from CIS215):** Priya Sharma,
Malik Johnson, Mei Lin, Diego Ramos, Amara Okafor, Sofia Reyes,
Ethan Cole, Naomi Redhouse.

**New CIS133-side canon (recorded here, now family canon):**
Copperwind runs a public community program: free e-waste recycling
drives, device refurbishment and donation, and drop-in tech help
clinics and workshops. **Priya Sharma is the program's outreach
coordinator** and the client voice in every content brief. Cast
members appear in content files where a Copperwind person is needed:
Malik Johnson runs the sorting station at drives, Naomi Redhouse
coordinates volunteers, Diego Ramos leads the repair clinic.

**Scope of the cast rule (review finding 4):** the eight names bind
ONLY Copperwind employees speaking or acting inside the spine.
Explicitly preserved: Devon (the book's accessibility anchor,
chapters 3-12), Maria Contreras and Dr. Lena Ortiz and every name in
the ch1 source-profiles scenario, the fictional-student folder
convention (skills-lab-3a-ortiz), and any name inside a neutral cover
story (the tutoring center, the soccer league).

**The student's role:** Copperwind has hired you to build the
program's website. You are the web developer. The role is stated in
Chapter 2's lab intro (where building starts) and echoed lightly
afterward. Chapter 1 needs no role framing (it is conceptual).

**Two-audience model (canonical, replaces current/prospective
members):** (a) Valley neighbors holding unused electronics at home:
they need to know what the program accepts, how to prepare a device,
and when to drop off. (b) Prospective volunteers: they need to see
the work and a clear way to join. Every audience statement in the
brief, chapter prose, and answer keys derives from these two.

### 1.2 The site identity

* **Site name:** `Copperwind Community` (the program's public site).
* **Page h1s stay page-specific (review finding 1).** The h1 answers
  "where am I now?", exactly as Chapter 7 teaches. Only h1s and
  titles that carry the club name change:

| Page | Old | New |
| --- | --- | --- |
| every `<title>` suffix | `| PC Computer Club` | `| Copperwind Community` |
| recycling-guide.html h1 | Recycle Your Old Electronics | unchanged |
| drive-gallery.html h1 | (page-specific) | unchanged |
| events.html h1 | (page-specific) | unchanged |
| join.html h1 | (club wording) | Join the Program (or the shipped page's wording with club swapped; ch11 agent verifies) |
| contact.html h1 | Contact the PC Computer Club | Contact the Copperwind Team |
| ch12 home page h1 | The PC Computer Club | Copperwind Community (20 = 20 chars) |

* **Nav labels (character-count parity noted):**
    * `Home` (4, was 4)
    * `Recycling Guide` (15, was 15)
    * `Spring Drive Gallery` (20, was 20)
    * `Fall Events` (11, was 11)
    * `Join the Program` (16, was "Join the Club" 13: the one label
      that grows. Re-verify nav wrap behavior in a browser per the
      probe matrix and update stated numbers if they move)
    * `Contact the Team` (16, was "Contact the Club" 16)
* **Email:** `copperwind-community@example.org` (was
  computer-club@example.org). The reserved example.org domain stays:
  it is taught content.
* **Page content mapping (structure unchanged):** Recycling Guide is
  Copperwind's community e-waste guide. Gallery shows the spring
  recycle drive Copperwind hosts. Fall Events lists the canonical
  roster (Section 1.5). Join the Program is the volunteer and
  workshop signup page (ch11 form). Contact the Team carries the
  drop-off hours schedule. Home (ch12) is the program's front door.
* **The chart data is untouched:** the spring drive collected
  Cables 64, Phones 38, Laptops 21, Small electronics 17, Tablets 14,
  total 154. These numbers thread ch3 (chart and alt text), ch10 (the
  practice table), and the wide-practice per-date splits. They are
  now Copperwind's drive numbers. Do not change them.

### 1.3 Renames and canonical vocabulary (review finding 3)

File and token renames:

| Old | New |
| --- | --- |
| `club-styles.css` | `copperwind-styles.css` |
| `club-palette.txt` | `copperwind-palette.txt` |
| `chapter-07/club-site/` | `chapter-07/copperwind-site/` |
| `club-logo.png` | `copperwind-logo.png` |
| `membership-chart.png` | `workshop-signups-chart.png` |
| color name "club teal" | "copperwind teal" (hex unchanged) |
| passphrase `cactus-club-2026` | `copperwind-2026` |
| `computer-club@example.org` | `copperwind-community@example.org` |
| id `#meeting-times` | `#drop-off-hours` |
| h2 "Meeting Times" | "Drop-Off Hours" |
| checkbox value `general-meetings` | `drop-in-clinics` |
| gate string "Welcome, officer." | "Welcome, team member." (re-verify the ch12 behavioral quote) |
| caption "PC Computer Club fall 2026 schedule" | "Copperwind Community fall 2026 schedule" |

Role and vocabulary mappings (contextual, applied by the Phase 3
mapping table in assets and by chapter agents in prose):

| Old concept | New canon |
| --- | --- |
| the officers | the outreach team |
| an officer | a team member (or a named cast member) |
| From the club officers (brief signature) | From the Copperwind outreach team |
| members / new members | volunteers (helpers) or neighbors/participants (attendees), by context |
| club meetings / meeting hours | drop-in clinics, workshop hours, or posted drop-off hours, by context |
| "New members welcome, no device required." | "New volunteers welcome, no experience required." |
| Skills Lab titles naming the club | same title with the Copperwind site (e.g. "The Copperwind Site Gets Its Layout") |

**The palette hex values do not change.** Copperwind teal #268080,
deep teal #1a5e5e, sunset orange #f4a259, light sand #fac78d, sand
#deb887, saguaro green #5e9959, ink #333333, white #ffffff, plus the
two labeled decoy browns. Every verified contrast ratio (4.69, 4.85,
3.04, 6.81, 8.19, 2.19, 1.26 wart, 10.12/4.12/1.88 cards) therefore
survives. Class names `.drive-gallery`, `.reminder`, `.page-divider`,
`.table-scroll` survive (they describe content role, unchanged).

**Zero-residue gate (word-boundary, case-insensitive), after the
sweep:** `computer club`, `computer-club`, `club-styles`,
`club-palette`, `club-logo`, `club-site`, `cactus-club`, `\bclub\b`,
`\bofficer(s)?\b`, `\bclubmate\b` must return zero in `book/` and
`assets/` outside an approved exception list (history quotes in
HANDOFF are exempt; `\bmember\b` and `\bmeeting\b` are checked with
word boundaries and a reviewed exception list because neutral cover
stories may legitimately use them, and "Remember" must not match).

**Varied cover stories stay varied (U1 constraint).** The spine claims
the Skills Lab thread. Practice files and TIYs keep their own worlds:
the tutoring center, the soccer league, Wikipedia and MDN field
trips. Playground files that currently wear the club's skin
(flex-playground announcement cards, query-playground bulletin bench)
take a neutral community-center skin or a light Copperwind skin, at
the chapter agent's choice, but the book must NOT become wall-to-wall
Copperwind.

### 1.4 Fictional disclaimer (verbatim, every chapter README)

> Copperwind IT Services is a fictional company created for this
> textbook. All names, clients, and records are synthetic. Any
> resemblance to a real company or person is coincidental.

The name-collision search was run for the family during the CIS215
pilot (2026-07-28). Do not re-litigate the name.

### 1.5 Canonical fall 2026 event roster (review finding 5)

One canonical roster feeds the ch7 brief, the ch10 events file and
table, the ch12 home content, chapter prose, and answer keys. Field
parity (Event, Date, Time, Location, Details) is asserted across all
of them in Phase 3. Dates MUST be verified against the real 2026
calendar before shipping (all weekday claims checked with `cal`).

| Event | Date | Time | Location | Details |
| --- | --- | --- | --- | --- |
| Fall Kickoff Drive | Saturday, September 12 | 9:00 a.m. to noon | Copperwind HQ parking lot | Bring any item on the accepted list. |
| Repair Clinic | Saturday, September 26 | 10:00 a.m. to 1:00 p.m. | Copperwind HQ training room | Watch a repair, or bring a device that needs one. |
| Device Drop-Off Day | Saturday, October 10 | 9:00 a.m. to noon | Mesa Community Center | Drive up, drop off, done in minutes. |
| Digital Safety Workshop | Thursday, October 22 | 6:00 to 7:30 p.m. | Online | Passwords, backups, and safe browsing. |
| Volunteer Orientation | Saturday, November 7 | 10:00 to 11:30 a.m. | Copperwind HQ training room | New volunteers welcome, no experience required. |
| Fall Wrap Drive | Saturday, November 21 | 9:00 a.m. to noon | Copperwind HQ parking lot | Last drop-off day before the holidays. |

The winter-drive mention in the ch8 viewport demo and any other dated
reference re-derives from this roster's calendar (same verification).

## 2. What every chapter receives

| Upgrade | Chapters | Form |
| --- | --- | --- |
| U1 Spine | 1-12 | The Skills Lab thread becomes Copperwind's site (scenario swap). Labs already satisfy "one spine block per chapter." NO new Try It Yourself blocks are added, so TIY counts and numbering do not change |
| U2 Fading | 5-8 completion, 9-12 problem-first | ONE existing TIY per chapter converts (Section 4 table). Chapters 1-4 stay full-worked (no change) |
| U3 Cumulative retrieval | 2-12 | 1-2 Retrieval Practice items REPLACED with "From Chapter N:" items. Totals stay at 5 (review finding 2: the family caps Retrieval Practice at 3-5, so cumulative items replace the weakest same-chapter items instead of appending). At least 3 same-chapter prompts remain |
| U4 Fix It block | 1-12 | One `### Fix It N.1: [Title] 🔧` per chapter |
| U5 Subgoal labels | 1-12 | Step comments added to the 2 most complex worked examples |
| Backward callback | 2-12 | This book already pays promises by name. Verify at least one genuine callback exists per chapter. Add one ONLY if missing |

**Checker contract (hard constraints):**

* Try It Yourself count per chapter is UNCHANGED (5 per chapter, 6 in
  ch9 and ch10). Numbering is untouched.
* Quick Checks stay exactly 4 per chapter. Retrieval Practice stays
  at 5 items per chapter.
* `**Predict:**`, `**Run:**`, and `**Explain:**` counts stay equal
  within each chapter. Fading conversions keep all three labels.
* Fix It blocks use ONLY `**Symptom:**`, `**Diagnose:**`,
  `**Repair:**`, `**Verify:**`. Never Predict/Run/Explain inside a
  Fix It.
* Anatomy N.1-N.7 unchanged. Fix It is an H3 inside a main content
  section. Exactly one per chapter, always numbered N.1.
* Broken, gapped, or non-runnable code lives in `text` fences only.
* MLOs, CLO blocks, lab part structure, Questions & Analysis, rubric
  link blocks: untouched.
* A versioned structure checker (`tools/check_course_structure.py`,
  CIS133 edition, review finding 15) encodes all of the above and is
  built and baselined in Phase 3, BEFORE any chapter wave.

## 3. Fix It blocks: the web-course discipline gate

"Real captured error" translates per the playbook: a validator
message (Nu or Jigsaw), a browser console line, or a rendered symptom
described exactly as a browser shows it. NEVER invent message text.
Capture protocol: run the broken file through the same instrument the
chapter teaches, paste the final message line(s) into a text fence,
and record the run in the wave's verification notes.

The book needs at least one silent bug (wrong render, no error).
This plan ships several (ch4, ch5, ch6, ch8): CSS fails silently by
design, and teaching that IS the point.

A Fix It must not recycle a message, path, or answer already used by
a TIY, Quick Check, worked example, or planted lab defect in its
chapter (review finding 8). The ch2, ch3, ch5, ch10, and ch11 bugs
below were re-chosen under that rule and finding 9's
validity-of-premise rule.

| Ch | Fix It N.1 (place, bug, instrument) |
| --- | --- |
| 1 | §1.2, after TIY 1.3. A shared link written `htps://www.phoenixcollege.edu` (protocol typo). Symptom: what the browser actually does with the unknown scheme, captured from a real address-bar attempt. Repair: correct the scheme. Verify: the page loads over https |
| 2 | §2.4, after TIY 2.5. A missing closing quote on an href value (`<a href="contact.html>Contact</a>`) in a short Copperwind announcement snippet. Real Nu messages captured fresh (attribute-parsing errors cascade instructively). Repair and revalidate to zero |
| 3 | §3.3, after TIY 3.4. A `<figcaption>` placed AFTER `</figure>` (orphaned caption). Real Nu error captured fresh. Repair: move it inside the figure. Verify: Nu zero plus the caption renders with its image. Does not reuse TIY 3.3's broken path or its missing-alt probe |
| 4 | §4.3, after TIY 4.3. SILENT bug: rule written `.galery` while the HTML says `class="gallery"`. Jigsaw passes, the page ignores the rule. Diagnose with DevTools (selector matches zero elements). Teaches: valid CSS is not correct CSS |
| 5 | §5.2, after TIY 5.3. SILENT bug: two-value shorthand order swapped (author wants 24px top/bottom and 16px sides but writes `padding: 16px 24px`). Renders legally but wrong, using only the taught two-value mapping. Repair with the correct order, verify in the DevTools box diagram |
| 6 | §6.1, after TIY 6.1. SILENT bug: `display: flex` placed on the items instead of the container. Nothing errors, nothing lines up. The Diagnose step names the container rule |
| 7 | §7.4, after TIY 7.5. A site plan whose nav lists "Click Here" and "More" as labels, plus a page that appears in the nav but not the sitemap. Symptom: the label audit fails (the screen-reader link list, read as a list, is ambiguous: capture the actual link-list text). Repair the plan |
| 8 | §8.3, after TIY 8.4. SILENT bug: the `min-width` and `max-width` conditions swapped so the phone override applies on desktop. No validator complaint. Diagnose with DevTools device mode at two widths (capture the real rendered difference) |
| 9 | §9.3, after TIY 9.4. A "fix" that swaps flyer body text to #c99b66 on white, which still fails AA. Symptom: the real WebAIM contrast checker ratio (compute and paste the actual number). Repair with a palette pairing that passes, verify with the checker |
| 10 | §10.2, after TIY 10.3. `<thead>` placed after `<tbody>`. Real Nu error captured fresh. Repair: head before body. Verify: Nu zero and zebra rows unchanged. Does not reuse the misplaced-caption or ragged-row probes already quoted in the chapter |
| 11 | §11.1, after TIY 11.1. Two controls sharing one id, with a label pointing at the duplicated id. Real Nu "Duplicate ID" error captured fresh, PLUS the behavioral symptom (the label activates only the first match). Repair with unique ids. Verify: Nu zero and the click test passes. Does not reuse Quick Check 11.1's for/id mismatch |
| 12 | §12.1, after TIY 12.1. `<script src="js/footer-year.js">` while the file lives at `footer-year.js`. Symptom: the real browser console 404 line plus the missing footer year. Repair the path, verify in the console |

Keep each broken file in the wave's scratch notes (never in the data
pack).

## 4. Fading conversions (U2)

One existing TIY per chapter converts. Chapters 1-4: none. The
conversion keeps the heading, number, title, and all three labels.
**Fade the support, never the reasoning (review finding 7):** each
conversion must preserve the original exercise's misconception,
observation, or design-judgment goal, and remove only scaffold.

| Ch | Target TIY | Conversion |
| --- | --- | --- |
| 5 | TIY 5.3: Prove the Clock | Completion: the shorthand expansion appears with 2 value gaps (`____`) in a text fence. The Predict still commits to the full expansion before filling gaps (the clock reasoning is the retained goal) |
| 6 | TIY 6.2: The Alignment Drill | Completion: the drill's rule set appears with gaps for the two alignment property NAMES (values shown). Predict still commits to what each property controls on which axis. TIY 6.5's design-defense stays untouched |
| 7 | TIY 7.4: Wireframe a Page You Did Not Build | Completion: the wireframe frame is given with two regions blank in the text fence. Predict still commits to what belongs in each blank region and why. TIY 7.3's live-MDN discovery stays untouched |
| 8 | TIY 8.4: Three Widths, One Title | Completion: the two query blocks appear with their breakpoint values gapped. The stated sizes at three widths are given (browser-verified), and the student engineers the breakpoints that produce them. The neither-query-gap lesson is retained as the Explain |
| 9 | TIY 9.5: The rem Experiment | Problem-first, on a NEW derived file `rem-practice.css` (three px rules, review finding 6). Task plus expected computed sizes at default and 20px roots (real numbers from a browser run). The shipped rem-demo.css controlled comparison stays in the section as the worked observation |
| 10 | TIY 10.4: The Caption Arrives | Problem-first: the task (give the practice table a caption and head/body structure so every tool can read it) plus the expected outcomes (real Nu clean result, caption rendering position from a real check). TIY 10.5's zebra discovery stays untouched |
| 11 | TIY 11.2: Breaking the Group | Problem-first: build the three-option exclusive radio group from the requirement, then break it by splitting the names and observe (the discovery is retained inside Run). Expected click behavior stated from a real browser check |
| 12 | TIY 12.4: The Move Test | Problem-first: the task (rewrite the absolute src so the image survives the move to a host) plus the expected render on any machine. Student writes the path. Respects the book's no-writing-scripts law |

Conversion rules: gapped code never sits in a fence a checker or
harness might execute (use `text`). Expected outputs and behaviors
come from real runs or real browser checks, never from memory. The
implementer writes the reference solution, verifies it, and keeps it
in the wave notes, not the chapter.

## 5. Cumulative retrieval map (U3)

REPLACE the weakest 1-2 same-chapter Retrieval Practice items (agent
picks, with rationale: usually the item most redundant with a Quick
Check) so each chapter still has exactly 5 items, at least 3 of them
same-chapter. New items are labeled exactly `From Chapter N:` and are
answerable from memory. Space the reach-back (roughly N-2 and N-4).

| Ch | Items |
| --- | --- |
| 2 | From Ch1: what the browser and server each do in the round trip |
| 3 | From Ch1: the parts of a URL. From Ch2: what the validator checks and what it cannot check |
| 4 | From Ch2: the required document skeleton. From Ch3: name the four landmark elements |
| 5 | From Ch3: block vs inline in one sentence each. From Ch1: what HTTPS protects |
| 6 | From Ch4: class selector vs id selector. From Ch2: why a nav menu is marked up as a list |
| 7 | From Ch5: the four-point readability checklist. From Ch3: which landmark holds a page's unique content |
| 8 | From Ch6: what flex-wrap does. From Ch4: why external stylesheets beat inline styles for a multi-page site |
| 9 | From Ch5: px vs rem. From Ch7: which of the five principles accessibility belongs to |
| 10 | From Ch8: what the viewport meta tag tells the phone. From Ch3: the alt-text decision for a decorative image |
| 11 | From Ch9: why a label must be programmatically tied to its control. From Ch7: which planned page the join form realizes |
| 12 | From Ch2: the relative-links promise (why they survive the move). From Ch10: why a data table needs th and scope |

## 6. Subgoal labels (U5)

Two most complex worked examples per chapter gain numbered decision
comments: `<!-- Step 1: ... -->` in HTML, `/* Step 1: ... */` in CSS,
`// Step 1: ...` in JS. Comments only. Steps name decisions, not
syntax. 3-5 steps, never single lines. **Non-code chapters (review
finding 16):** where a chapter's most complex worked examples are
text-fence diagrams, the approved callout syntax is a
`[Step k: decision]` line INSIDE the text fence, at the top of the
region it names. Defaults (agent may substitute a demonstrably more
complex example with rationale):

| Ch | Targets |
| --- | --- |
| 1 | The round-trip diagram and the URL anatomy diagram (text fences, `[Step k:]` syntax) |
| 2 | The document-skeleton walkthrough, the validator-repair worked example |
| 3 | The landmark page skeleton, the figure/figcaption example |
| 4 | The cascade three-ways example, the class/id selector example |
| 5 | The shorthand-clock example, the font-stack single-link example |
| 6 | The navigation-bar capstone rule set, the gallery flex block |
| 7 | The box-to-landmark mapping diagram (`[Step k:]` syntax), the site-plan assembly example |
| 8 | The base-plus-overrides worked block, the content-driven breakpoint derivation |
| 9 | The focus-repair example, the contrast-repair example |
| 10 | The accessible finished table, the zebra/hover style block |
| 11 | The labeled form worked example, the form-geometry CSS blocks (label each of the two split blocks) |
| 12 | The attach-a-script HTML listing, the playground gate JS listing (`// Step k:` comments) |

## 7. Data pack changes (Phase 3, before any chapter edit)

### 7.1 The mechanical sweep (scenario rename)

Per the mechanical-sweeps law: census first, scripted sweep with
per-file asserts, dry run, two passes, repo checkers green before and
after, one read-only review of the final diff. The sweep covers:
`book/`, `assets/code/`, filenames in Section 1.3, HTML titles, h1s
per the Section 1.2 table, nav labels, content text files, README
files, and answer files. After the sweep, the Section 1.3
zero-residue gate runs with its word-boundary rules and exception
list.

### 7.2 Content files (voice rewrite, Copperwind outreach team)

`recycling-guide-content.txt`, `gallery-content.txt` (still ships no
alt text on purpose), `events-content.txt` (the Section 1.5 roster,
five labeled fields per event), `project-brief.txt` (Priya Sharma's
expansion brief: home, events, join; the Section 1.1 two-audience
model; never says table or form), `join-page-notes.txt` (required
name+email ask, 5-option select, 4 interest checkboxes, questions
textarea, the data promise sentence, "and nothing else"),
`home-content.txt` (headline, what-the-program-is, three what-we-do
blurbs, three calls to action, the standing drop-in clinic line),
`source-profiles.txt` (ch1: five fictional source profiles, neutral,
light touch only if club-tied). Keep labeled-block structure and
approximate lengths so downstream layout checks hold. Field parity
with the roster is asserted by script.

### 7.3 Images: the Codex GPT-5.6-Sol upgrade

The nine flat Pillow masters retire (they remain in the archive). The
replacement set keeps EXACT dimensions and placement:

| Image | Size | Source |
| --- | --- | --- |
| `copperwind-logo.png` | 240x240, alpha-transparent (palette PNG with full alpha) | Codex native image generation |
| `cactus-garden.png` | 400x400 | Codex |
| `recycling-drive.png` | 800x450 | Codex |
| `sorting-station.png` | 640x360 | Codex |
| `donation-boxes.png` | 640x360 | Codex |
| `volunteer-crew.png` | 640x360 | Codex |
| `desert-divider.png` | 800x24 | Codex |
| `devices-collected-chart.png` | 640x400 | Seeded generator (data-exact: 64/38/21/17/14), restyled for quality |
| `workshop-signups-chart.png` | 640x400 | Seeded generator (data-exact: 18 to 39), restyled |

Rules:

* **Flat-color illustration style ONLY (review finding 10):** one
  coherent modern flat-illustration system across the seven Codex
  images, leaning on the palette (teals, copper, sand). Chapter 3's
  PNG-because-flat-illustrations lesson must remain true. No
  photographic or photorealistic direction.
* NO text baked into any image except the logo wordmark, and the
  wordmark only if it renders cleanly (AI text artifacts fail QA).
  The old volunteer-crew baked the club name into pixels: the new one
  must not bake any words.
* Charts stay programmatic because their numbers are taught content.
  The chart generator is seeded, asserted, byte-identical on rerun
  (Codex may write it, Claude verifies).
* **Executable acceptance gates (review finding 11):** a new
  `tools/check_images.py` asserts, for the shipped masters: exact
  dimensions per the table, a real source alpha layer (RGBA, or palette mode with
  transparency) and transparent corners for the logo, file-size ordering (the flat logo is the smallest file; the
  scenes exceed it: the TIY 3.5 teaching point), chart pixel checks
  (the generator's own data asserts), and palette-role presence
  (dominant tones sampled from the palette family). It runs in Phase
  3 and again in Phase 5.
* Provenance: AI masters cannot be seed-reproduced. New file
  `assets/code/_generators/IMAGE-MANIFEST.md` records for each
  master: SHA-256, dimensions, byte size, generator (Codex CLI,
  model gpt-5.6-sol, date), and the prompt used. The propagation
  script (master -> starter-site copies) is scripted with asserts.
  Chapter 4's "palette extracted from the generator" sentence is
  reworded by the ch4 agent to the new truthful provenance (the
  canonical palette lives in copperwind-palette.txt and the chart
  generator consumes it).
* **No discovery leaks (review finding 12):** exact byte sizes live
  in the manifest and instructor notes ONLY. TIY 3.5 keeps its
  discovery framing: the ch3 agent re-verifies that the ranking the
  chapter relies on (flat logo smallest, scenes larger) still holds
  and adjusts only what the chapter already reveals. Alt text for
  GRADED lab images goes in the instructor answer key only; chapter
  worked examples continue to use the two chapter-only images
  (cactus-garden, workshop-signups-chart).

### 7.4 Starter-site chain rebuild

The chain law holds: chapter N's starter site is the Lab (N-1) model
solution. The sweep transforms each starter in place (names, titles,
nav labels, logo file, images, CSS filename) and then the FULL
verification battery re-runs on every pack HTML/CSS file: Nu zero
messages, Jigsaw zero errors, and the probe matrix of Section 9. The
ch4 starter keeps its planted inline-style defect. The ch9 flyer
keeps exactly 8 planted barriers. broken-contact.html keeps exactly 4
planted defects producing exactly 8 Nu messages (re-run and
re-capture after the text swap). **Engine pinning (review finding
14):** the ch9 flyer's "exactly 2 messages" claim is pinned to
validator.w3.org (checked through the browser). validator.nu is
supplementary evidence everywhere and its known one-message flyer
result is documented, never substituted.

## 8. Codex delegation plan (how the plugin is used)

Codex runs `gpt-5.6-sol` (the config default: no `--model` flag is
ever passed; verified against a live session rollout on 2026-07-28).

1. **Adversarial spec review (this document):** DONE 2026-07-28,
   xhigh, verdict REJECT with 16 findings, all dispositioned in
   Addendum A and folded into this revision.
2. **Image generation:** background Codex tasks per Section 7.3.
3. **Chart generator:** Codex writes, Claude verifies seed and
   asserts.
4. **Per-wave verification:** after each wave commit, a read-only
   Codex review of the wave diff. Findings dispositioned before the
   next wave starts.
5. **Final review:** read-only Codex review of the full branch diff
   before Mr. Vega sees it.
6. **Rescue rule:** after two failed fix attempts on any defect, the
   investigation goes to Codex rescue instead of a third guess.

## 9. Implementer QA protocol (per chapter, before reporting done)

1. `python3 tools/check_sentence_length.py book/chapters/chapter-NN.md`
   reports zero.
2. `python3 tools/check_course_structure.py book/chapters/chapter-NN.md`
   reports zero errors (the Section 2 contract, encoded).
3. `grep -cE '—'` zero. Prose semicolon check zero (code and URLs
   exempt).
4. Banned vocabulary and filler sweep on the diff (list in
   `docs/style-guide-core.md`).
5. Every validator message, console line, computed ratio, byte size,
   and rendered behavior stated in the edits is captured from a real
   run this session. Instruments: Nu (validator.w3.org through the
   browser for pinned claims; validator.nu supplementary), Jigsaw,
   the orchestrator's browser pane, `node --check` for JS.
6. Layout claims whose input text changed are flagged for the
   orchestrator's browser probe matrix (below). Agents never guess
   new numbers.
7. Readability: chapter Flesch within 60-70 or above, and not below
   the archive value for the same chapter (identical tool).
8. Report: lines added, blocks added, verification evidence, real
   outputs used, reference solutions, flagged layout claims.

**Browser probe matrix (review finding 13), run by the orchestrator
after each wave on every page whose text or styles changed:** both
sides of every recorded boundary that the book states: 583/584,
863/864, 1143/1144 (card row wraps), 599/600 (playground flip),
639/640/641 (gallery seating, starter query block, h1 step), 375
(phone base, nav wrap rows), the remeasured nav-width threshold (was
~415px with four links; remeasure with "Join the Program"), plus the
header logo+h1 line-one check at 640. Results recorded in the wave
notes with px numbers.

Whole-book gates (Phase 5) additionally run: Nu on ALL pack HTML,
Jigsaw on ALL stylesheets, `node --check` on both JS files,
`tools/check_images.py`, glossary integrity, full-book banned-vocab
and em-dash and semicolon sweeps, the structure checker on all 12
chapters, TIY/QC/Retrieval count table vs archive, `zensical build
--clean` no issues, chart generator byte-identical rerun, image
manifest verification, data pack rebuild, and the archive-vs-branch
readability comparison with the identical tool (every chapter equal
or improved).

## 10. Phase 6 records (explicit deliverables, review finding 15)

1. CLAUDE.md: Pedagogy Upgrade Law section (spine, fading, Fix It,
   cumulative-retrieval-by-replacement, subgoal labels, checker
   contract) and the retrieval-law amendment (the final 1-2 items
   reach back with "From Chapter N:" labels).
2. `templates/chapter-template.md`: Fix It block format, fading
   patterns, spine note, quality-checklist entries.
3. HANDOFF.md entry with full verification evidence.
4. Data pack zip rebuilt (`build/cis133-data-pack.zip`), NOT uploaded
   to Canvas (Mr. Vega uploads manually).
5. command-brain capture of the durable decisions (site identity,
   roster, image provenance policy, retrieval-by-replacement).
6. Re-score under the family rubric (V2.1 or later) queued as the
   publication gate, expecting movement on C5/C7/C9 (the playbook's
   scoring rule).

## 11. What this upgrade deliberately does not do

* No new Try It Yourself blocks (the labs are the spine)
* No changes to MLOs, CLOs, Quick Checks, rubric, lab part structure
* No new selectors, elements, or concepts (the selector discipline
  and one-mention treatments stand)
* No changes to the chart's taught data (64/38/21/17/14, total 154;
  18 to 39)
* No palette hex changes
* No Canvas uploads (Mr. Vega uploads the data pack zip manually)
* No push to `main` (Mr. Vega reviews side-by-side first)

## Addendum A: Codex adversarial review disposition (2026-07-28)

Review: gpt-5.6-sol at xhigh, read-only, verdict REJECT (2 BLOCKER,
13 MAJOR, 1 MINOR). Every finding accepted. Dispositions:

| # | Finding (short) | Disposition in this revision |
| --- | --- | --- |
| 1 | Universal h1 erases page identity | ACCEPTED: page-specific h1s preserved, explicit h1/title map in §1.2 |
| 2 | Retrieval append breaks the 3-5 cap | ACCEPTED: replace-not-append, totals stay 5, ≥3 same-chapter (§2, §5); CLAUDE.md amendment in §10 |
| 3 | Rename table omissions (email, roles, lab titles) | ACCEPTED: §1.3 extended with email, role vocabulary, lab titles, word-boundary residue gate with exception list |
| 4 | Cast rule vs Devon and source profiles | ACCEPTED: cast rule scoped to Copperwind employees in the spine; Devon and scenario names preserved (§1.1) |
| 5 | No canonical event/audience dataset | ACCEPTED: §1.5 canonical roster with date verification, §1.1 two-audience model, parity asserts (§7.2) |
| 6 | ch9 fading mismatch with rem-demo | ACCEPTED: new derived rem-practice.css with three px rules; demo comparison preserved (§4) |
| 7 | Conversions replaced reasoning tasks | ACCEPTED: retargeted ch6 to TIY 6.2, ch7 to 7.4, ch8 to 8.4, ch10 to 10.4; fade-support-keep-reasoning rule added (§4) |
| 8 | Fix It duplicates (ch3, ch10, ch11) | ACCEPTED: re-chosen: orphaned figcaption, thead-after-tbody, duplicate id (§3) |
| 9 | Invalid premises (ch2 li, ch5 3-value) | ACCEPTED: re-chosen: unquoted href attribute, two-value order swap (§3) |
| 10 | Photographic art vs PNG lesson | ACCEPTED: flat-color illustration only (§7.3) |
| 11 | No executable image gates | ACCEPTED: tools/check_images.py with transparency, dimension, ordering, chart, palette asserts (§7.3); ch4 provenance sentence reworded |
| 12 | TIY 3.5 and lab-alt leak risk | ACCEPTED: byte sizes to manifest/instructor notes only; graded-lab alt text to answer key only (§7.3) |
| 13 | Fixed viewport trio insufficient | ACCEPTED: named browser probe matrix on both sides of every recorded boundary (§9) |
| 14 | validator.nu cannot verify the flyer claim | ACCEPTED: flyer claim pinned to validator.w3.org; nu supplementary (§7.4, §9) |
| 15 | No structure checker; Phase 6 records implicit | ACCEPTED: checker built and baselined in Phase 3 (§2); Phase 6 deliverables enumerated (§10) |
| 16 | ch1/ch12 subgoal mechanism undefined | ACCEPTED: `[Step k:]` text-fence syntax defined; ch12 retargeted to real HTML and JS listings (§6) |

## Addendum B: wave and final review dispositions (2026-07-28)

Codex (gpt-5.6-sol, xhigh) reviewed every wave read-only and the
whole branch at the end. Findings and dispositions, all same-day:

* Wave 1 (chapters 1-4): 6 findings. Volunteer-crew alt corrected to
  the six-person image chain-wide, the online drop-off line became
  the HQ parking lot, ch4 subgoal comments rewritten to decisions,
  palette usage notes rederived from the final art, ch3's jump-menu
  claim removed per WCAG H101, the Fix It capture's unreproducible
  location line dropped.
* Wave 2 (chapters 5-8): 8 findings. QC 6.1 q3 and QC 7.4 q1
  replaced (no Fix It parallels), TIY 7.4 refaded so the live-page
  observation returns, ch6 subgoal chain made coherent, box-practice
  aligned to the canonical Oct 10 Mesa event, ch7 README join
  description matched to the brief, bulletin cards TWO and FOUR
  replaced with canonical activities, "announcements" became
  "labels".
* Wave 3 (chapters 9-12): 6 findings. ch9's false no-background
  claim corrected (5.03 and 8.36 counter-ratios verified), ch12's
  Fix It pastes the complete captured console line, TIY 12.4's
  named-solution hint removed, the CLAUDE.md retrieval example
  expanded to five prompts, the faded-TIY checklist split by fading
  level, one template filler word removed.
* Final branch review: 4 findings. Program canon unified
  (refurbish-and-donate plus recycle, cadence "a few times a
  year"), two cumulative retrieval items re-sourced to the chapters
  that teach them, the logo's palette-with-alpha mode stated
  honestly in manifest/spec/checker with a source-alpha assertion,
  and the join-form publish-policy decision recorded in HANDOFF as
  Mr. Vega's pre-term ruling (the in-fiction sign-up claim was
  corrected to the program inbox).
