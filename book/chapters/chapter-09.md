# Chapter 9: Web Accessibility

A clubmate could not wait for the next meeting. They built a Drive Day flyer between classes, linked it to the club's pages, and posted it in the group chat: bright teal and sand, an eager pitch, every date and detail in place. Then Devon replied. Devon, whose email about the recycling guide opened Chapter 3, tried to read the flyer with a screen reader and gave up halfway down. The flyer is loud, cheerful, and closed to one of the club's own members.

Chapter 8 ended on a question, and this chapter is the answer. The club's site now serves every screen size a visitor can bring. Does it serve every visitor? Here is the surprising part: you have been building the answer since Chapter 1. Honest alt text, landmarks Devon jumps by, focus outlines no rule may remove, navigation labels that predict their pages, a palette whose pairings pass a contrast bar. Every one of those habits comes from a single written standard this book has never named. This chapter names it.

You will meet WCAG, its four POUR principles, and the conformance level this course tests against. You will audit structure the way a screen reader reads it. You will decode the contrast math the palette file has promised since Chapter 4, and learn what `rem` buys a visitor who resizes their type. Then you will add the last tool in the course's checking stack, an accessibility evaluator, and learn which checks belong to no tool at all. Skills Lab 9A repairs the flyer, audits the whole club site, and closes Part III.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 3-8 (semantic HTML and alt text, CSS, the box model's px and rem, focus states, UX principles, and responsive habits)
* **Deliverables:** Skills Lab 9A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-9.1 (Apply):** Implement accessible structure and navigation: ordered headings, landmarks, descriptive link text, and visible focus styles
* **MLO-9.2 (Apply):** Apply WCAG's perceivability rules to color, type, and images: AA contrast, color-independent meaning, rem-sized text, and purpose-matched alt text
* **MLO-9.3 (Evaluate):** Evaluate pages against WCAG Level AA with an accessibility evaluator and human checks, prioritizing repairs

### This chapter aligns with the following Course Learning Outcomes

* **CLO VIII (Apply):** Implement basic web accessibility practices to improve site usability

---

## 9.1 Every User: WCAG, POUR, and Conformance Levels

The flyer will wait for the lab. First the framework, because the flyer's real lesson is bigger than one page: a page can validate with zero messages, adapt to every screen, and still lock a visitor out. Chapters 2 through 8 built standards for correctness, presentation, layout, and screens. Accessibility is the standard for people, and it starts by counting who is at the door.

### Who Accessibility Serves

Accessibility entered this course in Chapter 7 as a UX principle: the site works for every visitor, including people who rely on screen readers, keyboards, or other assistive tools. Put faces on the words. Devon reads with a screen reader and hears your markup instead of seeing your pixels. A student with a tremor, or an arm in a cast, runs whole sessions from the keyboard, so everything a mouse can reach must answer the Tab key. A visitor with low vision doubles the zoom, or raises the browser's default type size and leaves it raised. Another visitor cannot tell red from green, so a message carried by color alone never arrives.

Now widen the lens, because barriers do not only meet disabilities. They meet situations. Phone glare in an Arizona parking lot makes low-contrast text invisible to everyone. A parent holding a toddler browses one-handed. A dead mouse battery turns the most confident mouse user into a keyboard user mid-form. Permanent, temporary, situational: the same barriers stop all three, and the same repairs serve all three at once. That arithmetic is why accessibility work is never niche work.

| The limit | A visitor it meets | The repair that serves them |
| --- | --- | --- |
| Permanent | Devon, reading by screen reader | Semantic structure and honest alt text |
| Temporary | A student typing one-handed in a cast | Full keyboard operability with visible focus |
| Situational | Anyone reading a phone in direct sun | Contrast that clears the standard's bar |

There is also the plain fairness of it, the concern Chapter 1 raised when it introduced screen readers. The web is where classes enroll, jobs post, and appointments book, and a barrier on those pages is a locked door on a public building. Public institutions, including colleges and government agencies, also carry legal obligations to publish accessible sites, which is one reason this skill appears in job postings.

### WCAG and the POUR Principles

The standard has a name. The **Web Content Accessibility Guidelines (WCAG)** are the W3C's written rules for accessible web content, maintained by the same standards body behind your two validators. When this chapter calls something a barrier or a repair, WCAG is the authority it stands on.

WCAG organizes everything it asks under four principles, remembered as **POUR**:

* **Perceivable.** Content must be able to reach every visitor's senses in some form. Alt text is the course's oldest example: when pixels cannot arrive, words do.
* **Operable.** Every control must work for every input. The focus outlines Chapter 6 protected keep the keyboard a first-class citizen.
* **Understandable.** Content and controls must make sense: plain language, labels that predict what follows, pages that behave consistently. Chapter 7's navigation label law is this principle wearing course clothes.
* **Robust.** Markup must be valid and semantic enough for any tool to parse, including tools that do not exist yet. Chapters 2 and 3 built nothing else.

Read the list again and notice whose examples those are. Yours. This course has taught accessibility since its first chapter and withheld only the standard's name. Nothing here asks you to start. It asks you to finish: see the habits as one framework, measure pages against it, and repair what falls short.

### Conformance Levels: A, AA, AAA

Standards need a pass bar, and WCAG defines three. A **conformance level** is the grade of WCAG a page claims to meet: Level A, Level AA, or Level AAA. Level A is the floor, the rules whose absence locks visitors out entirely. Level AA includes everything in A and raises the bar, adding demands like contrast minimums and resizable text. Level AAA tightens every dial further, and even organizations devoted to accessibility rarely promise it for every page.

This course works to Level AA. It is the working target across the industry. When this book says a page passes or fails, AA is the bar it means.

!!! note
    In the wild you will see "WCAG 2" with a minor version number after it. The numbers mark revisions of one standard, and everything this chapter teaches holds across them.

One AA expectation is close enough to test right now. Pages must survive zoom, many visitors' first tool. Raising the zoom makes every CSS pixel larger, so the page lays itself out as if the window were narrower. Responsive work and accessibility work meet exactly there: Chapter 8 prepared you for narrow widths, and it was quietly preparing you for zoom too.

### Try It Yourself 9.1: The Zoom Test 🛠️

**Predict:** At 200 percent zoom, the stylesheet will see about half your window's width. Check your window width with the DevTools readout, halve it, and predict whether the club stylesheet's own small-screen query will fire. Then predict what you will see either way: readable text, or sideways scrolling?

**Run:** Open `assets/code/chapter-09/starter-site/recycling-guide.html`. Press Ctrl and plus (Cmd and plus on Mac) until the browser reports 200 percent, then walk the page top to bottom: text, line lengths, nav links, any sideways scroll. Reset with Ctrl and 0 (Cmd and 0) when you finish.

**Explain:** In 1-2 sentences, report whether the query fired as predicted and how you could tell, and name the POUR principle a page that survives zoom serves.

### Quick Check 9.1 ✅

1. A clubmate declares the site accessible "because every page validates and the device-mode test passes." Name the standard neither check consulted, and give one barrier both checks would miss.
2. Sort three habits you already own under their POUR principles: alt text on the gallery figures, the nav links' `:focus` style, and validating every page before submission.
3. State the difference between Level A and Level AA in one sentence each, then name the level this course tests against.

---

## 9.2 Structure That Every Tool Can Read

Devon does not read your pages the way you watch them render. A screen reader lists a page's headings, its landmarks, and its links as separate menus, and its user jumps instead of scrolling. Every one of those menus is built from your markup and from nothing else. This section walks the three menus, then the keyboard that drives them.

### Heading Order Is the Outline

Since Chapter 2, this book has enforced a rule it never fully explained: heading levels never skip on the way down. Here is the explanation. Screen reader users skim by heading list. Devon pulls up the list, hears the page's shape in seconds, and jumps straight to the section that answers the visit. The levels are that outline's indentation, so a page that steps from `h2` to `h4` promises a level that does not exist. It reads like a book with pages torn out.

The tutoring center's schedule page shows the defect and the repair:

```html
<!-- BROKEN: the outline skips from h2 to h4. A heading list
     shows a hole where the h3 level should be. -->
<h1>Campus Tutoring Center</h1>
<h2>Math Help</h2>
<h4>Drop-in Hours</h4>
```

```html
<!-- REPAIRED: every step down is exactly one level. The
     heading list reads as an honest outline. -->
<h1>Campus Tutoring Center</h1>
<h2>Math Help</h2>
<h3>Drop-in Hours</h3>
```

If the `h4` was chosen for its smaller default size, Chapter 4 already handed you the honest tool. Keep the level the outline needs and set the size in the stylesheet.

!!! note
    The heading outline serves a second audience you met in Chapter 1: search engines weigh headings when they index a page. One honest outline serves Devon, the crawler, and the sighted skimmer alike.

### Landmarks Are the Doors

Chapter 3 built the landmark skeleton and admitted its payoff was real but invisible. Name the payoff precisely now, one landmark at a time:

* A screen reader announces `<header>` as the page's banner, so Devon knows the identity block without listening through it.
* It announces `<nav>` as navigation and reports how many links the menu holds before reading one.
* A single keystroke jumps to `<main>`, skipping the banner and menu that repeat on every page. That jump was the whole ask in Devon's Chapter 3 email.
* `<footer>` is announced as content info, where every tool expects contact lines and fine print to live.

The club's pages have carried all four since Lab 3A. That is why the exercises below are confirmation walks, not repair jobs.

### Links That Name Their Destination

The third menu is the link list. A screen reader can pull every link on a page into one list, read away from its sentences. Pulled out of its sentence, "Click here" names nothing:

```html
<!-- BROKEN: heard in a links list, away from their sentences,
     all three say nothing about their destinations. -->
<a href="schedule.html">Click here</a>
<a href="subjects.html">here</a>
<a href="tips.html">this page</a>

<!-- REPAIRED: each link names its destination, in or out of
     its sentence. -->
<a href="schedule.html">See this week's tutoring schedule</a>
<a href="subjects.html">Browse the subjects we cover</a>
<a href="tips.html">Read our exam-week study tips</a>
```

This is not a new law. Chapter 3 demanded descriptive link text, and Chapter 7's label law asked every navigation label to predict its page. WCAG asks the same of every link on the page, and now you know the menu it protects.

### The Keyboard Walk

The last structural demand is **keyboard navigation**: operating a page entirely from the keyboard, with Tab stepping forward through its interactive elements and Shift plus Tab stepping back. Three things must be true. Every interactive element is reachable. The order makes sense to a visitor working through the page. And the current stop is always visible.

That last demand is Chapter 6's law grown up: never remove a focus outline without a replacement at least as visible. WCAG states its rules as numbered success criteria, and this one is criterion 2.4.7, Focus Visible. That citation is a naming sample, not the start of a catalog, and it is the only criterion number this course asks you to recognize.

The walk is also the cheapest test you own. It needs no install, no upload, and no second tab: put the mouse away, and the page tells on itself in under a minute.

```css
/* BROKEN: the outline is deleted and nothing replaces it. A
   keyboard visitor now moves through the page blind. */
.study-links a {
    outline: none;
}
```

```css
/* REPAIRED: if the default outline fights the design, replace
   the signal instead of deleting it. */
.study-links a:focus {
    outline: 3px solid #268080;
}
```

The replacement does not have to be an outline. Chapter 6 answered `:focus` with a background flip, and any change at least as visible as the default keeps the law.

### Try It Yourself 9.2: The Heading Outline Read 🛠️

**Predict:** You have edited the club's recycling guide since Chapter 2. From memory, write its heading outline: how many headings, at which levels, in what order?

**Run:** Open `assets/code/chapter-09/starter-site/recycling-guide.html`, open DevTools, and search the Elements panel for `<h` with Ctrl+F (Cmd+F on Mac), Chapter 3's trick. Read the headings in order with their levels.

**Explain:** In 1-2 sentences, compare the real outline to your prediction, and state what Devon hears from this list that a sighted visitor gets from type sizes.

### Try It Yourself 9.3: The Tab Walk 🛠️

**Predict:** Stay on the recycling guide. Write the order in which you expect focus to travel through the nav's three links. Then state what visible signal should mark every stop, and name the rule in `club-styles.css` you expect to provide part of it.

**Run:** Click once at the top of the page, put the mouse away, and press Tab through the whole page, into the footer and out. Watch the order and the signal at every stop.

**Explain:** In 1-2 sentences, state what determined the order you observed, and name the POUR principle a complete, visible walk satisfies.

### Quick Check 9.2 ✅

1. A page's headings run `h1`, `h2`, `h2`, `h5`. Describe what a screen reader's heading list shows at the fourth heading, and write the repair.
2. A sentence reads "Click here to check this week's hours" with the link on "Click here." Rewrite the link text so it survives the link-list read, and name one beneficiary besides screen reader users.
3. A new theme ships `a { outline: none; }` site-wide because outlines "clutter the look." Name the POUR principle at stake and the repair that keeps the clean design.

---

## 9.3 Perceivable Content: Color, Type, and Images

Structure serves the tools that read for people. Perceivability serves the senses directly, and this section pays two of the book's oldest debts: the math behind the palette's passing list, and the reason `rem` exists.

### The Contrast Math, At Last

The palette file has carried the same promise since Chapter 4: trust the passing list, and Chapter 9 will teach the math. A **contrast ratio** measures how strongly text stands out from its background. It compares how much light the two colors give off, with a small constant added so the scale behaves at the dark end. The scale runs from 1 to 1, text on its own exact color, to 21 to 1, pure black on pure white. Run white on white through the math and it computes exactly 1.00. Black on white computes exactly 21.00. Every real pairing lands between those anchors.

WCAG Level AA sets the thresholds. Body text needs 4.5 to 1 or better. Large text passes at 3 to 1, because bigger, heavier strokes stay readable at lower contrast. WCAG counts text as large at 24 pixels and up, or about 18.7 pixels and up when bold. The whole scale at a glance:

| Measurement | Ratio | What it means |
| --- | --- | --- |
| Text on its own exact color | 1.00 | The scale's floor: invisible |
| Pure black on pure white | 21.00 | The scale's ceiling |
| AA minimum for body text | 4.5 to 1 | The bar this course grades against |
| AA minimum for large text (24px+, or bold 18.7px+) | 3 to 1 | Bigger or heavier strokes earn a lower bar |

Now the passing list's numbers read as measurements instead of decoration. The footer fix from Chapter 6, light sand on deep teal, sits on the list at 4.85 to 1: past the AA bar with room to spare. The wart it repaired has a number too. Default link blue on deep teal measures 1.26 to 1, barely above text on its own color. Invisible ink. Devon never met that wart, but every visitor squinting through glare met it head-on.

You never compute a ratio by hand. The WebAIM contrast checker (`webaim.org/resources/contrastchecker`) takes a text color and a background color and returns the ratio, graded against every threshold. What you may not do is eyeball it. Eyes adapt, screens differ, and near-misses fool nearly everyone, as the first exercise below will demonstrate on you.

!!! tip
    Bookmark the checker beside the two validators. The three travel together from here on: every color pairing you ship gets a number before it gets an opinion.

### Color Never Carries the Signal Alone

Contrast has a sibling rule. Color may decorate a signal, but it can never be the signal alone. A visitor who cannot tell red from green loses it, a screen reader announces no color at all, and glare erases it for everyone. The tutoring center's schedule shows the failure and the fix:

```html
<!-- BROKEN: color is the only signal. A visitor who cannot
     see the red hears an ordinary list item. -->
<p>Sessions shown in red are full.</p>
<li class="session-full">Algebra, Tuesday 3:00</li>

<!-- REPAIRED: a text label carries the signal, and the color
     is free to keep decorating it. -->
<li class="session-full">Algebra, Tuesday 3:00 (full)</li>
```

Notice that the repair removes nothing. The red stays for everyone it serves. The label is for everyone else.

The same rule guards a habit from Chapter 5. Links inside body text are told apart by color, so stripping their underline leaves color as the only signal, which is exactly the failure this section names. The underline stays on in-sentence links, and now you know the standard behind the style advice.

### Type a Visitor Can Resize

Chapter 5 introduced `px` and `rem` as two different promises and saved the payoff for now. A pixel value is a fixed promise: `16px` renders the same for every visitor, whatever their settings say. A `rem` is a proportional promise: `1rem` means the root element's text size. That size comes from the visitor's own browser default (16 pixels until the visitor raises it) as long as no stylesheet resets the root. Here is why the two promises matter: many low-vision visitors raise that default once and leave it raised, and the two units answer that request differently. The rem experiment at the end of this section stages the difference so you can watch it.

Zoom does not make the setting redundant. Zoom is a per-page chore repeated on every site, while the default size is set once and follows the visitor everywhere. Converting is one division, the `px` value over 16:

```css
/* The tutoring center's type, converted. Divide each px value
   by the 16px default: 16 / 16 = 1rem, 24 / 16 = 1.5rem. */
body {
    font-size: 1rem;      /* was 16px */
}

.center-heading {
    font-size: 1.5rem;    /* was 24px */
}
```

One neighbor scales for free. The unitless `line-height` from Chapter 5 multiplies whatever size the element ends up at, so converted text keeps its breathing room. Skills Lab 9A runs this exact conversion on the club's own stylesheet, base rules and query block alike.

### Four Jobs, Four Alt Decisions

Chapter 3 taught alt text by the image's job and named three jobs. Audit work meets a fourth, and the full set makes a decision table worth keeping:

| The image's job | The tell | The alt text |
| --- | --- | --- |
| Informative | The image carries content the page needs | Describe what matters, in about a sentence |
| Decorative | The image is visual polish | `alt=""`, empty on purpose, so tools skip it |
| Functional | The image is the content of a link | Name the destination, never the picture |
| Complex | A chart or diagram carries data | Deliver the finding, with a visible caption beside it |

One recall from Chapter 3 keeps the table honest: the job belongs to the page, not the file. The same illustration can be informative on one page and pure decoration on another, so no alt decision survives a copy and paste unexamined.

Functional images earn the new paragraph, because an image inside a link changes the question. The visitor deciding whether to press it does not need the picture described. They need to know where it goes:

```html
<!-- The logo IS the link, so the alt answers the only question
     that matters: where does this go? -->
<a href="index.html">
    <img src="images/center-logo.png" alt="Tutoring center home"
    width="240" height="240">
</a>
```

Complex images you have already met: Chapter 3's membership chart shipped alt text that delivered the finding while the `figcaption` commented beside it. One honesty rule covers all four jobs. Alt text describes the image's purpose on this page, and software can detect a missing `alt` attribute in an instant but can never grade a dishonest one. Hold that thought. It is the whole plot of Section 9.4.

### Try It Yourself 9.4: Three Contrast Calls 🛠️

**Predict:** Open `assets/code/chapter-09/contrast-cards.txt`: three text-on-background pairings, none from the club's palette. For each card, predict pass or fail against the 4.5 to 1 body-text bar, by eye alone, and write all three predictions on the card's lines before checking anything.

**Run:** Run each card's two hex values through the WebAIM contrast checker and record the ratio it reports next to your prediction.

**Explain:** In 1-2 sentences, report which predictions held, and state what the closest call says about eyeballing contrast versus measuring it.

### Try It Yourself 9.5: The rem Experiment 🛠️

**Predict:** Open `assets/code/chapter-09/rem-demo.html`. Its three bordered paragraphs name their own sizing rules: `16px`, `1rem`, and `1.5rem`. Predict which paragraphs will grow when you raise the browser's default font size, and whether any two match before you change anything.

**Run:** Follow the page's own numbered instructions: raise the default font size in your browser's settings, return to the page, and compare the three paragraphs. Set the default back to Medium (16) when you finish.

**Explain:** In 1-2 sentences, explain the split you observed using this section's two promises, and name a visitor the growing paragraphs serve.

### Quick Check 9.3 ✅

1. A teammate insists their gray-on-white body text "looks fine to me." Name the instrument that settles the question, and the minimum the pairing must meet at Level AA.
2. The food pantry's needs list marks its most urgent items in orange only. Name the rule this breaks, the POUR principle behind it, and a repair that keeps the orange.
3. Convert a 32px heading to `rem`, show the division, and name whose setting the converted value respects.

---

## 9.4 The Audit: Evaluators and Human Checks

You can now repair structure, color, type, and images. What remains is the auditor's skill: finding every barrier on a page you did not write, and knowing which tool, or which human, catches which kind.

### The Tool Stack, Layer by Layer

The course has been assembling a checking stack since its second chapter. Here is the full automated half:

| Layer | Owned since | What it catches |
| --- | --- | --- |
| HTML validator | Chapter 2 | Syntax, plus two structural accessibility errors: a missing `alt` attribute and a skipped heading level |
| CSS validator | Chapter 4 | Stylesheet syntax, and nothing about whether the styled result is readable |
| Contrast checker | This chapter | One text-on-background pairing at a time, graded against the thresholds |
| Accessibility evaluator | This chapter | A whole rendered page, scanned for every barrier software can detect |

The new layer needs its introduction. An **accessibility evaluator** is a tool that scans a rendered page and flags the accessibility problems software can detect. The course's evaluator is WAVE, built by WebAIM, the organization behind the contrast checker. WAVE draws its findings as icons on the page itself, and its catch list covers this chapter's mechanical side:

* Missing alt text, and empty links or buttons
* Low-contrast text pairings
* Skipped heading levels and missing landmarks

Run it two ways. For a public page, paste the address at `wave.webaim.org`. For local files like yours, install the WAVE browser extension (`wave.webaim.org/extension`), which runs the same checks on any page your browser has open.

Notice what the table's first row admits. The HTML validator has been catching two kinds of accessibility defect all along: it reports a missing `alt` attribute and a skipped heading level as errors. Remember that overlap. The lab will ask you to map findings to layers, and the first layer catches more than syntax.

### Try It Yourself 9.6: First WAVE 🛠️

**Predict:** WAVE is one paste away, so aim it at a page you respect. Pick the W3C's home page (`www.w3.org`), the organization that publishes WCAG itself. Predict the result: spotless, or flagged? Write down your call and one reason.

**Run:** Paste the address at `wave.webaim.org` and read the summary, then click one icon on the page to see what it marks.

**Explain:** In 1-2 sentences, state whether the run matched your prediction, and what any flag on a standards body's own page says about the gap between automated findings and human judgment.

### The Checks That Belong to You

Now the limit, and it is a hard one. No software can judge whether alt text tells the truth or whether link text predicts its page. None can decide whether the focus order makes sense to a person, or whether a page still works at 200 percent zoom. Tools catch the absence of alt text. Humans judge its quality.

The human half of the audit is a checklist you already own move by move. Its seven checks: the heading outline read, the landmark check, the link text read, the Tab walk, the zoom test, the alt honesty read, and contrast spot checks. Your pack ships them as `accessibility-checklist.txt`, with blank findings lines, copied once per page you audit. The lab runs it end to end.

A few field names, offered once. VoiceOver is the screen reader built into every Mac and iPhone, and NVDA is a free standard on Windows: an afternoon spent hearing your own pages through one is humbling and worth it. ARIA is an attribute toolkit for describing complex widgets that HTML's own elements cannot, and this course never needs it, because the semantic elements you build with carry their meaning for free.

One contract waits for later. Forms carry accessibility rules of their own, built on the partnership between every input and the label that announces it, and Chapter 11 teaches that contract when it builds the club's join form.

### Triage: Not All Findings Weigh the Same

One habit ties every layer together: audit first, repair second. Log every finding before you fix the first one, because repairs change the page under your feet, and a half-audited page hides the defects you have not reached yet.

An audit produces a findings list, and a findings list is not a repair order until you rank it. Blockers lock visitors out entirely: an informative image with no alt text, a page the keyboard cannot finish, body text that fails contrast. Polish problems degrade the visit without ending it: a wordy decorative alt, a label that could read better. Repair blockers first, and be ready to defend the order out loud, because a stakeholder will ask. The lab's Part 3 ends on exactly that judgment.

The flyer from this chapter's opening is still waiting. You now hold the full stack, the checklist, and the triage rule, and the lab hands you the page Devon could not read.

### Quick Check 9.4 ✅

1. Name two barriers WAVE can flag and two it cannot see, and state what covers the second pair.
2. Two findings arrive from the pantry site's audit: the hero photo has no `alt` attribute, and a decorative leaf border carries a three-sentence alt. Rank them with this section's rule and defend the ranking in one sentence.
3. A teammate skips the human checklist because "WAVE came back clean." Using this section's division of labor, state what a clean WAVE run proves and what it cannot.

---

## 9.5 Summary and Retrieval 💡

### Key Concepts

* Accessibility serves every visitor at once. Permanent, temporary, and situational limits meet the same barriers, so one repair clears them for all. WCAG is the W3C standard behind habits this course has taught since Chapter 1, organized under POUR: perceivable, operable, understandable, robust. Level AA is the working target.
* Structure is what a screen reader skims. Heading levels never skip because they build the outline Devon jumps by, landmarks label the page's doors, and link text must name its destination even when pulled out of its sentence.
* Keyboard navigation must reach every interactive element, in source order, with focus visible at every stop. Chapter 6's outline law turned out to be a WCAG success criterion all along.
* A contrast ratio runs from 1.00 (text on its own color) to 21.00 (black on white). Level AA demands 4.5 to 1 for body text and 3 to 1 for large text at 24 pixels and up. The WebAIM checker computes it, eyes never do, and color may decorate a signal but never carry it alone.
* `px` freezes type against the visitor's chosen default size, and `rem` multiplies it: divide the px value by 16. Alt text follows the image's job: informative, decorative, functional, or complex.
* The audit stack runs the HTML validator, the CSS validator, the contrast checker, and the evaluator (WAVE), then hands the rest to seven human checks. Tools catch absence, humans judge honesty, and repairs land blockers before polish.

### Key Terms

See course glossary for full definitions

* WCAG, POUR, perceivable, operable, understandable, robust, conformance level (Section 9.1)
* keyboard navigation (Section 9.2)
* contrast ratio (Section 9.3)
* accessibility evaluator (Section 9.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite POUR's four principles, each with one technique from an earlier chapter that serves it.
2. State the contrast scale's two anchors and the two Level AA thresholds, with the text sizes they apply to.
3. Explain what `1rem` measures, what raising the browser's default size does to rem text and to px text, and who the difference serves.
4. List as many of the seven human checks as you can, and name one thing they judge that no tool can.
5. Name the four automated layers of the checking stack in the order the course taught them, with one defect each can catch.

---

## 9.6 Skills Lab 9A: The Club Site Passes the Audit

**Goal:** Audit and repair a clubmate's Drive Day flyer against WCAG Level AA, then verify the whole club site with an accessibility evaluator and the human checklist, closing the Part III milestone.

**Dataset:** Provided files in `assets/code/chapter-09/` from the course data pack. `drive-day-flyer.html` and `flyer-styles.css` are the audit target, written in a hurry by an enthusiastic clubmate, and they ship broken on purpose: 8 planted accessibility barriers, disclosed in the folder's README. The flyer fails HTML validation with exactly 2 messages, and its stylesheet validates clean, because its sins are decisions, not syntax. `flyer-images/` holds the flyer's two images, byte-identical copies from the club's set, so the flyer renders wherever the folder travels. `starter-site/` holds the club's three pages, `images` folder, and `club-styles.css` exactly as Skills Lab 8A finished them: every head carries the viewport tag, and the stylesheet ends in the small-screen query block. `club-palette.txt` travels with every CSS chapter, and its passing list supplies every repair color this lab needs. `contrast-cards.txt`, `rem-demo.html`, and `rem-demo.css` are the chapter's Try It Yourself files. `accessibility-checklist.txt` is the human audit instrument: seven checks with blank findings lines, copied once per page you audit. `skills-lab-9a-answers.txt` is your written answers file. The README documents every file. Work at the extracted `cis133` root.

The lab walks the chapter's own path. Part 1 audits the flyer and repairs its structure. Part 2 repairs what perceivability demands: color, type, and images. Part 3 brings in the evaluator and the checklist, proves the whole site, and closes Part III.

### Part 1: Foundation (Aligns with MLO-9.1)

1. Create a folder named `skills-lab-9a-lastname` at your `cis133` root. Copy in `drive-day-flyer.html`, `flyer-styles.css`, the whole `flyer-images` folder, the whole `starter-site` folder, `skills-lab-9a-answers.txt`, and `accessibility-checklist.txt`. Keep the `starter-site` name unchanged, because the flyer's links resolve into it.
2. Audit before you fix anything. Make a checklist copy for the flyer and run its structure checks: the heading outline read, the landmark check, the link text read, and the Tab walk. The flyer holds 8 barriers in all, counting a barrier once even where it strikes twice, and this pass surfaces the structural share. Log each finding in answer 1.A with the POUR principle it violates, and write "clean" where a check finds nothing.
3. Repair the structure: correct any heading level that skips, rewrite any link whose text fails the out-of-sentence read, and restore the focus visibility the stylesheet took away. Then re-run the same four checks and confirm they read clean. Record each fix in answer 1.B: the element or rule you changed, what it says now, and who the new version serves that the old one failed.

### Part 2: Application (Aligns with MLO-9.2)

1. Run the contrast spot checks: measure the flyer's text-on-background pairings with the WebAIM checker until you find the pairing that fails, and log the ratio it reports. Repair it with a pairing from the palette's passing list, and record the before and after ratios in answer 2.A.
2. Find the message the flyer carries in color alone, and give it a text label that survives without the color. Log the finding and the fix in answer 2.A.
3. Run the alt honesty read and make both calls the four-jobs table demands: write the missing alt text yourself, and empty the alt that decoration never needed. Log both decisions in answer 2.A with the image job that justifies each.
4. Convert the type. In `flyer-styles.css`, replace the hard px body size with a rem value that restores readable body text (the club site's own body size is a fine model). In `club-styles.css`, convert the body and heading sizes to rem with the divide-by-16 math, in the base rules and in the query block. Record the px values found, the rem values shipped, the base your math used, and who the conversion serves in answer 2.B.

### Part 3: Extension (Aligns with MLO-9.3)

1. Run WAVE on the repaired flyer and on one club site page: the browser extension for local files, or `wave.webaim.org` if you have a hosted copy. Log the tool, the pages, and every flag in answer 3.A. Then name at least one problem you repaired that no tool flagged, and the human check that caught it.
2. Run the full seven-check checklist on each of the club site's three pages, one checklist copy per page. Repair anything a check surfaces, and log the human-check results in answer 3.B.
3. Validate everything: the flyer and all three club pages through the HTML validator, both stylesheets through the CSS validator, repairing until every report shows zero messages. Log the final counts in answer 3.B.
4. Close the Part III milestone in answer 3.B. Name where a grader sees each leg: the site plan from Lab 7A, the responsive behavior from Lab 8A, and this lab's WCAG evaluation. Then hand down your triage call: of your 8 repairs, the one you would ship first if you could ship only one, defended in two or three sentences.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Every page in this course has validated with zero messages since Chapter 2, yet the flyer held 8 barriers, and the HTML validator caught exactly 2 of them. Lay out the five-layer stack (HTML validator, CSS validator, contrast checker, accessibility evaluator, human checks) and assign each of your 8 findings to the first layer that could have caught it. State what the finished assignment proves about relying on any single tool.
2. Pick two of your repairs. For each, name the POUR principle it serves, one visitor beyond Devon who benefits and how, and whether a tool or a human check caught the original defect.

**Submission:** Zip your `skills-lab-9a-lastname` folder containing the repaired `drive-day-flyer.html` and `flyer-styles.css`, the `flyer-images` folder, the updated `starter-site` folder, your completed checklist copies, and `skills-lab-9a-answers.txt`, and submit it as `skills-lab-9a-lastname.zip`. Every page and stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 9A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Code Accuracy and
Efficiency, Output Quality, Documentation and Code Comments, and
Analysis, Interpretation, and Response to QUESTION(s).

---

## 9.7 Review Questions 🔄️

1. **Remember:** Name POUR's four principles with one course technique that serves each, then name WCAG's three conformance levels and the one this course targets.

2. **Understand:** A classmate calls the never-skip-headings rule "a style preference, since the page looks the same either way." Explain what a screen reader builds from heading levels, and what a skipped level does to the visitor using it.

3. **Apply:** The food pantry's volunteer page contains the fragment below. Find every barrier in it, write the repaired version, and name the POUR principle behind each fix.

    ```html
    <h1>Volunteer With the Pantry</h1>
    <h4>Saturday Shifts</h4>
    <p>Shifts fill fast. <a href="signup.html">Click here</a>
    before Friday.</p>
    <img src="images/sorting-tables.png" width="600" height="400">
    ```

4. **Evaluate:** An audit of the intramural soccer league's site returns four findings:

    * The schedule page's body text fails the contrast check
    * The league logo links home, with alt text describing its stripes and colors
    * A decorative banner image carries a two-sentence alt
    * One page's headings jump from `h3` to `h5`

    Rank the two repairs you would ship first. Defend the ranking with this chapter's triage rule and the visitors each repair unblocks.

---

## Further Reading 📖

* [W3C WAI: WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/) - The standard's own front door: what WCAG is, who maintains it, and how its principles and levels fit together.
* [WebAIM: Constructing a POUR Website](https://webaim.org/articles/pour/) - The people-first essay behind this chapter's framework, walking each POUR principle with examples.
* [WebAIM: Contrast Checker](https://webaim.org/resources/contrastchecker/) - The course's contrast tool. Worth a permanent bookmark beside the two validators.
* [WAVE Web Accessibility Evaluation Tools](https://wave.webaim.org/) - The course's evaluator, with the browser extension for local files linked from the same page.
* [The A11Y Project: Checklist](https://www.a11yproject.com/checklist/) - A practitioner checklist that extends this chapter's human checks across a whole site.

---

## Looking Ahead ⏩

Part III set out to design for every user, and its milestone is now yours to claim. You planned a site in Lab 7A. You adapted it to every screen in Lab 8A. You evaluated it against WCAG in this lab. Plan, adapt, include. Part IV builds the pages your site plan promised, starting with Chapter 10's events page. There HTML tables arrive with accessibility built in from the first row: headers, scope, and captions continue exactly this chapter's work.
