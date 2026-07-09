# Chapter 8 Data Pack: Skills Lab 8A Files

Starter files for Skills Lab 8A: The Club Site Meets Every Screen.
Students take the club's finished three-page site and retrofit it
for phones: the viewport meta tag on every page, a small-screen
media query at a breakpoint the site's own content demands, and one
more query of their own choosing. Every page then proves itself at
three widths in browser DevTools device mode. Students never retype
provided content, and every color still comes from the palette file.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `starter-site/recycling-guide.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/drive-gallery.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/contact.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/club-styles.css` | Valid CSS, the site stylesheet as Skills Lab 6A finished it | Parts 1-3 |
| `starter-site/images/` | 7 PNG images, see the image table below | Parts 1-3 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Parts 2-3 |
| `query-playground.html` | Standalone chapter practice page | Chapter Try It Yourself exercises |
| `query-playground.css` | Practice stylesheet beside its page | Chapter Try It Yourself exercises |
| `no-viewport.html` | Standalone demo page, head carries no viewport tag | Chapter Try It Yourself exercises |
| `viewport.html` | The same demo page with the viewport tag | Chapter Try It Yourself exercises |
| `skills-lab-8a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The starter site

`starter-site/` holds the club's site exactly as Skills Lab 6A
finished it: three pages, one external stylesheet, and the full
Flexbox layout. It is a byte-identical copy of the site Chapter 7's
lab audited, which Lab 7A studied and never edited. All three pages
and the stylesheet validate with zero messages.

Two disclosures. First, no page in the starter carries a viewport
meta tag. That absence is deliberate and it is Part 1's work: the
site has never been told how to meet a phone, and this lab is where
it learns. Second, one rule in the stylesheet has been running ahead
of its chapter since the Chapter 6 pack: images cap at the width of
whatever box holds them (`max-width: 100%` with `height: auto`).
The Chapter 6 README promised that Chapter 8 would explain
that rule properly. This chapter pays the debt: fluid images are
one of the mechanisms responsive design is built from.

## Image files

All seven images are PNG and share one flat-illustration style:
the fictional club's matching design set. Their alt text is
already written into the pages. The table exists so the `width`
and `height` attributes can be checked against the files' true
pixels.

| File | Pixels | Contents |
| ---- | ------ | -------- |
| `club-logo.png` | 240 x 240 | Club logo: a monitor circled by recycling arrows on a teal disk. Transparent background |
| `recycling-drive.png` | 800 x 450 | Outdoor collection table scene with labeled bins and students |
| `devices-collected-chart.png` | 640 x 400 | Bar chart of items collected at the spring drive, five categories |
| `desert-divider.png` | 800 x 24 | Thin decorative strip of alternating diamonds |
| `sorting-station.png` | 640 x 360 | Volunteer sorting donations into three labeled bins |
| `donation-boxes.png` | 640 x 360 | Three cardboard boxes filled with coiled cables |
| `volunteer-crew.png` | 640 x 360 | Four volunteers behind the drive's welcome table |

## File details

**club-palette.txt** travels with every CSS chapter, copied
byte-identical from the Chapter 6 pack (Chapter 7's wireframe work
was deliberately grayscale, so the palette sat that chapter out).
It maps the design set's colors to exact hex values with a usage
note per color and records every text-on-background pairing that
passes the WCAG AA minimum of 4.5 to 1 for body text. The
playground's color switch draws both of its backgrounds from that
passing list, so no new contrast math enters this chapter.

**query-playground.html and query-playground.css** travel as a
pair. The page links the stylesheet with a bare relative href, so
both files must stay in the same folder. The page is the club's
bulletin: a deep teal banner, a wrapping row of four cards numbered
ONE through FOUR, and a centered reading column. Unlike Chapter 6's
playground, this one ships with its media queries already written
at the bottom of the stylesheet. The chapter's exercises read each
query, predict what fires and at what width, then drag the window
to check. Three mechanisms are engineered in: the page background
switches at one width (with the card padding tightening in the same
block), the banner title carries a max-width and min-width pair
that leaves a middle range where only the base rule stands, and the
260px cards wrap at widths the chapter derives from the row's own
arithmetic. The page carries the viewport meta tag, the course's
document skeleton from this chapter on.

**no-viewport.html and viewport.html** are one page in two head
states. Their bodies are byte-identical, and their heads differ by
exactly one line: the viewport meta tag. Open both in DevTools
device mode and every difference on screen traces to that line.
Neither page links a stylesheet, on purpose: the browser's default
styles make the size difference loudest. Neither page carries an
image, also on purpose: an oversized image would force horizontal
scrolling in both states and muddy the one-variable comparison.
Both pages validate with zero messages. The validator does not
require a viewport tag, which is its own small lesson: valid markup
and phone-ready markup are different standards.

**skills-lab-8a-answers.txt** holds numbered answer spaces: the
Part 1 viewport tag, device-mode observations, rendered widths, and
three-width diagnosis list, the Part 2 breakpoint defense and query
block, and the Part 3 query defense, validator log, three-width
verification, and Part III milestone check, followed by the
Questions & Analysis section. It travels inside the submission
folder unrenamed.

## Source and license

Written for CIS133 by the course author. The PC Computer Club and
its events are fictional, and the club's email address uses the
reserved example.org domain. All seven images are original
illustrations rendered by the course's seeded generator script
(`assets/code/_generators/generate_chapter03_images.py`), so they
carry no third-party license. The starter site is the Chapter 6
Skills Lab model solution, unchanged through Chapter 7's audit, so
Lab 8A does not punish a weak Lab 6A twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
