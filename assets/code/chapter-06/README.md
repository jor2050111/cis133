# Chapter 6 Data Pack: Skills Lab 6A Files

Starter files for Skills Lab 6A: The Club Site Gets Its Layout.
Students take the club's spaced, typeset three-page site and give
it its layout: a flex header row, a wrapping gallery row, the
long-promised footer-link fix, and hover and focus states. Part 3
builds the navigation bar the site has owed its visitors since
Chapter 4. Students never retype provided content, and every color
still comes from the palette file.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `starter-site/recycling-guide.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/drive-gallery.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/contact.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/club-styles.css` | Valid CSS, the site stylesheet as Skills Lab 5A finished it | Parts 1-3 |
| `starter-site/images/` | 7 PNG images, see the image table below | Parts 1-3 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Parts 2-3 |
| `flex-playground.html` | Standalone chapter practice page | Chapter Try It Yourself exercises |
| `flex-playground.css` | Practice stylesheet beside its page | Chapter Try It Yourself exercises |
| `skills-lab-6a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The starter site

`starter-site/` holds the club's site exactly as Skills Lab 5A
left it: three pages connected to one external stylesheet,
`club-styles.css`, now spaced with the box model and typeset for
comfortable reading. The stylesheet opens with the border-box
baseline, pads every landmark, and centers a 640-pixel readable
column. It sets the site's type (a Verdana body stack, 16px body
text, line-height 1.5) and borrows Oswald from Google Fonts for
the headings through one link element in each page's head. All
three pages and the stylesheet validate with zero messages.

One disclosure, and it is the point of this chapter: the footer's
links still render the browser's default link blue on the deep
teal footer, a pairing that fails contrast badly. This defect is
known and deliberate. The site has carried it since Lab 4A, where
the model's own critique line named it as the thing no validator
can see. Chapter 4's selectors could not repaint one region's
links without repainting them all. Lab 6A Part 2 finally
fixes it with this chapter's descendant combinator.

One rule in the stylesheet runs ahead of its chapter: images cap
at the width of whatever box holds them (`max-width: 100%` with
`height: auto`). The cap keeps the 800-pixel drive photo inside
the 640-pixel column. Chapter 8 teaches that pattern properly. It
ships here because the readable column breaks visibly without it.

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
byte-identical from the Chapter 5 pack (which copied it from
Chapter 4) so this folder stays self-contained. It maps the design
set's colors to exact hex values with a usage note per color and
lists two lookalike prop browns. It also records every
text-on-background pairing that passes the WCAG AA minimum of
4.5 to 1 for body text. The footer fix and every hover and focus
style in this chapter draw from that passing list.

**flex-playground.html and flex-playground.css** travel as a
pair. The page links the stylesheet with a bare relative href, so
both files must stay in the same folder. The page is the club's
announcement board: one container div holding four labeled cards,
numbered ONE through FOUR so alignment experiments read at a
glance. The container rule ships with no layout declarations on
purpose. The chapter's exercises add `display: flex` and its
friends there one at a time. The 220-pixel card width is
deliberate: four cards plus three 16-pixel gaps need 928 pixels
of container width, so the row wraps at common laptop window
sizes once wrapping is allowed. Two cards carry longer text than
the others, which makes cross-axis experiments visible. Both
files validate with zero messages.

**skills-lab-6a-answers.txt** holds numbered answer spaces: the
Part 1 axis reasoning for the header row and the gallery row's
wrap observations, plus the Part 2 footer-fix selector reasoning
and keyboard Tab log. Part 3 spaces cover the layout defense, the
validator log, and the Part II milestone check, followed by the
Questions & Analysis section. It travels inside the submission
folder unrenamed.

## Source and license

Written for CIS133 by the course author. The PC Computer Club and
its events are fictional, and the club's email address uses the
reserved example.org domain. All seven images are original
illustrations rendered by the course's seeded generator script
(`assets/code/_generators/generate_chapter03_images.py`), so they
carry no third-party license. The starter pages and stylesheet are
the Chapter 5 Skills Lab model solution, so Lab 6A does not punish
a weak Lab 5A twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
