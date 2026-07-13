# CIS133 Textbook: 12-Chapter Structure (Authoritative)

**Course:** CIS133: Internet/Web Development Level I
**Structure:** 12 chapters organized into 4 thematic Parts
**Pacing:** Schedule-neutral. Instructors may use the book in 9-, 12-,
14-, or 16-week courses without changing chapter content.
**Prerequisite:** None. Chapters teach from zero.
**Last revised:** 2026-07-13

This document is the single authoritative plan for chapter order,
scope, and outcome coverage.

---

## Design Rationale

This plan synthesizes four sources:

1. **Official CLOs and district course outline** (docs/CIS133_CLOs.md):
   every outcome and outline section maps to a chapter
2. **The previous Canvas build:** a 10-module course map (course map
   v2) with drafted MLOs, milestones, and an independent project
3. **OER draft chapters:** 10 draft chapters extracted from the
   Maricopa Pressbooks book used previously (open.maricopa.edu/cis133da),
   kept as raw material only
4. **The textbook family structure:** 12 chapters in 4 Parts, the
   pattern proven by the sibling textbooks

**Key design decisions:**

* Kept the 10 proven module topics in their taught order. They become
  chapters 1 through 8 plus 10 and 11.
* Added Chapter 9 (Web Accessibility). Outline section V and CLO VIII
  name WCAG, POUR, and conformance levels, but no previous module gave
  accessibility dedicated coverage. It was scattered across modules.
* Added Chapter 12 (Scripting Concepts and Publishing). It covers
  outline section VII (scripting concepts, CLO XI) and the hosting,
  file transfer, and publishing content (outline III.B and VIII.G,
  CLO VI) that the 10-module build compressed into independent project
  instructions.
* Renamed module topics into action-oriented chapter titles (CSS
  Foundations, Layout with Flexbox, Responsive Design and Media
  Queries).
* An optional independent project threads through Parts III and IV with
  two schedule-neutral milestones: a site plan in Chapter 7 and draft
  pages in Chapter 10.

**Bloom's rule for every MLO (course-configured, mirrors CLAUDE.md):**
the full RBT range is available. Early chapters lean on Remember
through Apply verbs. Analyze through Create verbs appear in Skills
Labs, later chapters, and final-project work. Every MLO uses a
measurable action verb. Never write "understand," "know," or "learn"
as the verb.

---

## Part I: Web Foundations (Chapters 1-3)

**Theme:** how the web works, and how to structure real content with HTML
**Learning arc:** Describe the web -> Build valid pages -> Structure content semantically
**Outcome alignment:** CLO I, II, III, IV (introduced), V (begun), VIII (alt text begins)
**Bloom's focus:** Remember through Apply

### Chapter 1: The Internet and the World Wide Web

**Subtitle:** EXPLAIN how the Internet, the web, and browsers work together
**Outcome(s):** CLO I, II, III
**Outline section(s):** I (Internet fundamentals), II (Information retrieval)

**Content:**

* The Internet vs the World Wide Web, and a short history of both
* IP addresses, DNS, domain names, and the parts of a URL
* Browsers and how a page request travels
* Search engines, SEO basics, and evaluating online information
* Ethics, privacy, security (SSL, digital certificates), and copyright
* Accessibility as a social issue: screen readers preview (outline I.C.4)

**Prior-course parallel:** Module 1 (The Internet, Domains, and Web
Browsers) and draft chapter 1
**Prerequisite bridge:** new content. The course has no prerequisite.

### Chapter 2: Basic HTML Elements

**Subtitle:** BUILD your first valid HTML pages in VS Code
**Outcome(s):** CLO IV, V
**Outline section(s):** III (workflow), IV.A-B (structural and content elements)

**Content:**

* The development workflow: VS Code, file saving, browser preview
* Anatomy of an HTML document: doctype, html, head, body
* Headings, paragraphs, lists, and links
* Elements vs attributes
* Validating markup with the W3C validator

**Prior-course parallel:** Module 2 and draft chapter 2
**Prerequisite bridge:** builds only on Chapter 1

### Chapter 3: Semantic HTML and Images

**Subtitle:** STRUCTURE content with semantic elements and accessible images
**Outcome(s):** CLO V, VIII (begins)
**Outline section(s):** IV.C (text-level semantics), V.G and V.I (images, alt text)

**Content:**

* Semantic vs non-semantic elements, and why meaning matters
* Page landmarks: header, nav, main, section, article, footer
* Embedding images and writing useful alt text
* Choosing image file formats for the web
* Organizing site files and folders

**Prior-course parallel:** Module 3 and draft chapter 3
**Prerequisite bridge:** builds on Chapters 1-2

**Part I milestone:** students hand-build a valid page with semantic
structure, working links, and accessible images.

---

## Part II: Styling with CSS (Chapters 4-6)

**Theme:** separate presentation from structure and take control of layout
**Learning arc:** Connect styles -> Control the box -> Arrange the page
**Outcome alignment:** CLO IV, V, IX
**Bloom's focus:** Apply, with Analyze entering in Chapter 6

### Chapter 4: CSS Foundations

**Subtitle:** STYLE pages with selectors, colors, and external stylesheets
**Outcome(s):** CLO IV, V, IX
**Outline section(s):** VI.A-C (inline, internal, external), VI.E-F (properties, element/class/id selectors), VI.H (color)

**Content:**

* What CSS does: separating content from presentation
* Inline, internal, and external stylesheets, and when each fits
* Rule syntax: selectors, properties, values
* Element, class, and id selectors
* Color systems and validating CSS

**Prior-course parallel:** Module 4 and draft chapter 4
**Prerequisite bridge:** builds on Chapters 2-3

### Chapter 5: The Box Model and Typography

**Subtitle:** CONTROL spacing and text with the box model
**Outcome(s):** CLO V, IX
**Outline section(s):** VI.D (box model), VI.E (properties), VI.H (font options)

**Content:**

* The box model: content, padding, border, margin
* Individual and shorthand spacing syntax
* Font families, sizes, and web-safe choices
* Text alignment, decoration, and transform
* Readable typography as a design decision

**Prior-course parallel:** Module 5 and draft chapter 5
**Prerequisite bridge:** builds on Chapter 4

### Chapter 6: Layout with Flexbox

**Subtitle:** ARRANGE page sections with Flexbox and smarter selectors
**Outcome(s):** CLO V, IX
**Outline section(s):** VI.F.4-5 (descendant selectors, pseudo-classes), VIII.E (navigation)

**Content:**

* Flex containers and flex items, main and cross axes
* justify-content, align-items, flex-wrap, and gap
* Building a navigation bar with semantic HTML and Flexbox
* CSS combinators for targeting related elements
* Pseudo-classes for interactivity: hover and focus

**Prior-course parallel:** Module 6 and draft chapter 6
**Prerequisite bridge:** builds on Chapters 4-5

**Part II milestone:** students style a multi-section page with an
external stylesheet, controlled spacing and type, and a Flexbox
navigation bar.

---

## Part III: Design for Every User (Chapters 7-9)

**Theme:** plan sites deliberately and design for every device and every user
**Learning arc:** Plan the site -> Adapt to screens -> Include every user
**Outcome alignment:** CLO II (applied), III (applied), VIII, IX, X
**Bloom's focus:** Apply through Evaluate

### Chapter 7: UX and Web Design

**Subtitle:** PLAN sites with sitemaps, wireframes, and UX principles
**Outcome(s):** CLO III (applied), XII (planning begins)
**Outline section(s):** VIII.B (website planning and design)

**Content:**

* Why planning beats coding first
* UX vs UI, and the core UX principles
* Sitemaps, wireframes, and prototypes
* Navigation design and layout consistency
* Independent project milestone: site plan

**Prior-course parallel:** Module 7 and draft chapter 7
**Prerequisite bridge:** builds on Chapters 1-6

### Chapter 8: Responsive Design and Media Queries

**Subtitle:** ADAPT layouts to any screen with media queries
**Outcome(s):** CLO X
**Outline section(s):** VI.I (styling for screen resizing), VIII.F (responsive styling)

**Content:**

* Why responsive design exists, and mobile-first thinking
* The viewport meta tag
* Media query syntax and breakpoints
* Base styles plus overrides as a pattern
* Testing layouts in DevTools device mode

**Prior-course parallel:** Module 8 and draft chapter 8
**Prerequisite bridge:** builds on Chapters 5-6

### Chapter 9: Web Accessibility

**Subtitle:** APPLY WCAG and POUR so every user can use your site
**Outcome(s):** CLO VIII, II (applied)
**Outline section(s):** V (entire accessibility section)

**Content:**

* WCAG and the POUR principles
* Conformance levels: A, AA, AAA
* Accessible structure: headings, landmarks, and link design
* Color contrast and accessible color selection
* Alt text decisions and accessible forms preview
* Running an accessibility evaluator on a real page

**Prior-course parallel:** gap. No previous module gave accessibility
dedicated coverage. This chapter consolidates and deepens it.
**Prerequisite bridge:** builds on Chapters 3-4 (semantic HTML, CSS)

**Part III milestone:** students plan a small site, make a page
responsive, and evaluate pages against WCAG basics with an
accessibility checker.

---

## Part IV: Building Complete Sites (Chapters 10-12)

**Theme:** complete the toolkit, then ship a real multi-page site
**Learning arc:** Present data -> Collect input -> Publish the site
**Outcome alignment:** CLO V, VI, VII, XI, XII
**Bloom's focus:** Apply through Create

### Chapter 10: HTML Tables

**Subtitle:** PRESENT data with accessible, styled tables
**Outcome(s):** CLO V, VIII (applied), IX (applied)
**Outline section(s):** IV.E (tables)

**Content:**

* Table structure: rows, data cells, and headers
* When a table is the right tool (and when it is not)
* Styling tables for readability
* Accessible tables: header scope and captions
* Independent project milestone: draft pages

**Prior-course parallel:** Module 9 and draft chapter 9
**Prerequisite bridge:** builds on Chapters 4-5

### Chapter 11: HTML Forms

**Subtitle:** COLLECT user input with accessible forms
**Outcome(s):** CLO VII, VIII (applied)
**Outline section(s):** IV.D (forms, input types, attributes)

**Content:**

* Form structure and the label-input partnership
* Input types: text, email, checkboxes, and friends
* Attributes that help users: placeholder, required, autocomplete
* Where form data goes: server-side processing in concept
* Styling and accessibility for forms

**Prior-course parallel:** Module 10 and draft chapter 10
**Prerequisite bridge:** builds on Chapters 4 and 9

### Chapter 12: Scripting Concepts and Publishing

**Subtitle:** PUBLISH your multi-page site and preview what scripting adds
**Outcome(s):** CLO VI, XI, XII, IV (applied)
**Outline section(s):** VII (scripting concepts), III.B (hosting and file transfer), VIII (multi-page site, publish to a server)

**Content:**

* Client-side vs server-side scripting in concept
* What JavaScript adds to a page (a preview, not a tutorial)
* Server-side ideas: security, databases, and languages
* Hosting options and secure file transfer
* Pre-flight checks: validation, links, accessibility
* Publishing an independent project site

**Prior-course parallel:** gap. The previous build compressed this
into independent project instructions.
**Prerequisite bridge:** builds on the entire book

**Part IV milestone:** students publish a complete, accessible,
responsive multi-page website (the independent project).

---

## Schedule-Neutral Course Mapping

The four Parts define the skill sequence, not a calendar. An instructor
can assign one or more chapters per instructional unit and place the two
independent project milestones where they fit the section. The same
chapter files support 9-, 12-, 14-, and 16-week courses. Course dates,
exams, submission windows, hosting details, and final-project pacing
belong in instructor materials.

**Assessment structure:**

* Skills Labs (chapter deliverables): [weight]%
* Module quizzes: [weight]%
* Independent project (with two milestones): [weight]%
* Weights live in the Canvas build. Confirm before syllabus
  publication.

---

## Outcome Coverage Matrix

| Outcome | Primary chapters | Supporting chapters | Coverage assessment |
| ------- | ---------------- | ------------------- | ------------------- |
| I. Analyze Internet/WWW impact | Ch 1 | Ch 12 | Strong: dedicated opening chapter |
| II. Evaluate ethical/privacy concerns | Ch 1 | Ch 9, Ch 12 | Strong: introduced early, applied later |
| III. Compare research resources | Ch 1 | Ch 7 | Adequate: watch depth in Ch 1, it carries three outcomes |
| IV. Critique with validators | Ch 2, Ch 4 | Every lab, Ch 12 | Strong: habit built into every Skills Lab |
| V. Create pages with HTML and CSS | Ch 2-6 | Ch 7-12 | Strong: the spine of the book |
| VI. Apply file transfer protocols | Ch 12 | None | Adequate: single chapter, keep the lab hands-on |
| VII. Construct HTML forms | Ch 11 | Ch 12 | Strong: dedicated chapter |
| VIII. Implement accessibility | Ch 9 | Ch 3, Ch 10, Ch 11 | Strong: dedicated chapter plus threads |
| IX. Compose CSS styles | Ch 4-6 | Ch 8, Ch 10 | Strong: three-chapter arc |
| X. Adapt with media queries | Ch 8 | Ch 12 | Strong: dedicated chapter |
| XI. Illustrate scripting concepts | Ch 12 | None | Adequate: conceptual coverage only, matches outcome verb |
| XII. Produce a multi-page website | Ch 12 | Ch 7 | Strong: independent project threads from Ch 7 |

---

## District Outline Coverage Map

| District outline section | Chapter(s) |
| ------------------------ | ---------- |
| I. Internet fundamentals | Ch 1 |
| II. Information retrieval | Ch 1 |
| III. Workflow for creating web pages | Ch 2 (editors, validation), Ch 12 (hosting, upload) |
| IV.A-C. HTML structural/content/semantic | Ch 2, Ch 3 |
| IV.D. Forms | Ch 11 |
| IV.E. Tables | Ch 10 |
| V. Accessibility practices | Ch 9 (primary), Ch 3 (images and alt text) |
| VI. Cascading Style Sheets | Ch 4, Ch 5, Ch 6, Ch 8 (media queries) |
| VII. Web scripting concepts | Ch 12 |
| VIII. Developing a multi-page website | Ch 7 (planning), Ch 6 (navigation), Ch 8 (responsive), Ch 12 (publish) |

---

## Cross-Chapter Dependencies

**Strict prerequisites:**

* Chapter 3 requires Chapter 2 (HTML document anatomy)
* Chapters 4-6 run in sequence (selectors, then box model, then layout)
* Chapter 8 requires Chapters 5-6 (box model and Flexbox come first)
* Chapter 9 requires Chapters 3-4 (semantic HTML and CSS basics)
* Chapters 10-11 require Chapter 4 (styling)
* Chapter 12 synthesizes the book (it publishes the independent project)

**Knowledge assumed across all chapters:**

* None from prior courses. The course has no prerequisite.
* Basic file management (creating folders, saving files) is taught
  explicitly in Chapter 2, then assumed.

---

## Prerequisite-to-CIS133 Bridge Map

Not applicable. CIS133 has no prerequisite course. Every chapter
builds only on earlier chapters of this book.
