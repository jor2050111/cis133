# Chapter 9 Data Pack: Skills Lab 9A Files

Starter files for Skills Lab 9A: The Club Site Passes the Audit.
Students audit a clubmate's Drive Day flyer against WCAG Level AA,
repair it, then verify the whole club site with an accessibility
evaluator and the chapter's human checklist, closing the Part III
milestone. Students never retype provided content, and every repair
color comes from the palette file's passing list.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `drive-day-flyer.html` | The audit target, broken on purpose (see the disclosure below) | Parts 1-3 |
| `flyer-styles.css` | Valid CSS whose choices carry barriers of their own | Parts 1-3 |
| `flyer-images/` | 2 PNG images, byte-identical copies from the club site | Parts 1-2 |
| `starter-site/recycling-guide.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 2-3, chapter Try It Yourself exercises |
| `starter-site/drive-gallery.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 2-3, chapter Try It Yourself exercises |
| `starter-site/contact.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 2-3 |
| `starter-site/club-styles.css` | Valid CSS, the site stylesheet as Skills Lab 8A finished it | Parts 2-3 |
| `starter-site/images/` | 7 PNG images, unchanged from the Chapter 8 pack | Parts 2-3 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Part 2 |
| `contrast-cards.txt` | Three fresh text-on-background pairings for prediction practice | Chapter Try It Yourself exercises |
| `rem-demo.html` | Standalone demo page for the px and rem experiment | Chapter Try It Yourself exercises |
| `rem-demo.css` | Demo stylesheet beside its page | Chapter Try It Yourself exercises |
| `accessibility-checklist.txt` | The human audit instrument: seven checks with blank findings lines | Parts 1-3 |
| `skills-lab-9a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The flyer ships broken on purpose

`drive-day-flyer.html` and `flyer-styles.css` announce the club's
Drive Day, written in a hurry by an enthusiastic clubmate. The pair
carries **8 planted accessibility barriers**, counting a barrier
once even where it strikes twice, and finding and repairing all 8
is the lab's work. Until it is repaired, the flyer
fails HTML validation with exactly 2 messages. The other 6 barriers
sail through every validator, which is the chapter's lesson: valid
and accessible are different standards. The stylesheet itself
validates with zero messages even though some of its choices are
barriers, because its sins are decisions, not syntax. Audit first.
Do not fix anything until your checklist says why.

The flyer's images live in `flyer-images/`, byte-identical copies
of two images from the club site's `images` folder. The copies keep
the flyer self-contained, so it renders correctly wherever the
folder travels.

## The starter site

`starter-site/` holds the club's site exactly as Skills Lab 8A
finished it: the Lab 8A model solution. Every page's head now
carries the viewport meta tag, and the bottom of `club-styles.css`
holds the small-screen query block at the site's own 640-pixel
breakpoint. The block gives the gallery figures the full row,
tightens `main`'s side padding, grows the nav links into
finger-sized targets, and steps the banner heading down. For its
Part 3 choice the model solution took the refinement path (the
heading step-down, inside the same block) instead of a wide-screen
query. All three pages and the stylesheet validate with zero
messages.

## Image files

All images are PNG and share one flat-illustration style: the
fictional club's matching design set. The seven files in
`starter-site/images/` are unchanged from the Chapter 8 pack, and
their alt text is already written into the site's pages. The two
files in `flyer-images/` are copies of images from that set. What
the flyer's markup does with them is part of the audit.

| File | Pixels | Contents |
| ---- | ------ | -------- |
| `flyer-images/recycling-drive.png` | 800 x 450 | Outdoor collection table scene with labeled bins and students |
| `flyer-images/desert-divider.png` | 800 x 24 | Thin decorative strip of alternating diamonds |

## File details

**club-palette.txt** travels with every CSS chapter, copied
byte-identical from the Chapter 8 pack. It maps the design set's
colors to exact hex values and records every text-on-background
pairing that passes the WCAG AA minimum of 4.5 to 1 for body text.
The palette's promise finally gets its math this chapter, and its
passing list supplies every color the lab's repairs need.

**contrast-cards.txt** holds three labeled text-on-background
pairings for the chapter's contrast prediction exercise. None of
the six hex values comes from the palette or the flyer. The file
prints no ratios on purpose: you predict first, and the WebAIM
checker settles it.

**rem-demo.html and rem-demo.css** travel as a pair. The page shows
three bordered paragraphs, one sized in px and two sized in rem,
each naming its own rule. In-page instructions walk through raising
the browser's default font size and watching what follows. The page
validates with zero messages and carries the viewport tag, the
course's document skeleton since Chapter 8.

**accessibility-checklist.txt** is the chapter's human audit
instrument: seven checks no automated tool can run for you, each
with a what-to-check line and blank findings lines. It ships blank
on purpose. The findings are your discovery, not the pack's. Copy
it once per page you audit.

**skills-lab-9a-answers.txt** holds numbered answer spaces: the
Part 1 structure findings and fixes, the Part 2 contrast, color,
alt, and type-conversion log, and the Part 3 evaluator results,
human-check results, milestone close, and triage call, followed by
the Questions & Analysis section. It travels inside the submission
folder unrenamed.

## Source and license

Written for CIS133 by the course author. The PC Computer Club, its
events, and the clubmate who rushed the flyer are fictional, and
the club's email address uses the reserved example.org domain. All
images are original illustrations rendered by the course's seeded
generator script
(`assets/code/_generators/generate_chapter03_images.py`), so they
carry no third-party license. The starter site is the Chapter 8
Skills Lab model solution, so Lab 9A does not punish a weak Lab 8A
twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
