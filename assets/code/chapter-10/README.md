# Chapter 10 Data Pack: Skills Lab 10A Files

Starter files for Skills Lab 10A: The Events Page. Students build
the club site's events page as an accessible, styled table, add it
to every page's navigation, and deliver the site plan's first
promised addition. Students never retype provided content, and
every color the table wears comes from the palette file's passing
list.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `starter-site/recycling-guide.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/drive-gallery.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/contact.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/club-styles.css` | Valid CSS, the site stylesheet as Skills Lab 9A finished it | Parts 1-3 |
| `starter-site/images/` | 7 PNG images, unchanged from the Chapter 9 pack | Parts 1-3 |
| `events-content.txt` | The six fall events with labeled fields, ready to copy into cells | Part 1 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Part 2 |
| `table-practice.html` | The spring drive results (the guide page's chart data), marked up as a bare table | Chapter Try It Yourself exercises |
| `wide-practice.html` | The spring drop-off log, seven columns wide | Chapter Try It Yourself exercises |
| `practice-styles.css` | Shared stylesheet for both practice pages, base type only | Chapter Try It Yourself exercises |
| `skills-lab-10a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The starter site

`starter-site/` holds the club's site exactly as Skills Lab 9A
finished it: the Lab 9A model solution. The three pages are
unchanged from the Chapter 9 pack, because the audit found nothing
to repair on them. The stylesheet is the one file that moved: its
text sizes now speak rem instead of px (body 1rem, headings 2.5rem
and 1.5rem, the query's banner step-down 2rem), so a visitor's own
font-size setting scales the whole site. All three pages and the
stylesheet validate with zero messages.

## The practice tables ship incomplete on purpose

`table-practice.html` holds the spring drive results with a header
row and nothing more. It carries no caption, no tbody tags, and no
table styling. The chapter's Try It Yourself exercises supply each
missing piece in turn: one adds the caption, one inspects the
markup in DevTools, and one adds a stripe rule to the stylesheet.
Every exercise begins with a prediction, and what the browser does
with each missing piece is the discovery. Do not read ahead by
completing the file early.

`wide-practice.html` is the opposite case: structurally complete
(caption, thead, tbody, scope on every header cell) but seven
columns wide, and it ships without a scroll wrapper. The chapter's
phone-width exercise adds one. Both pages share
`practice-styles.css`, which sets readable base type and leaves
every table decision to you.

Both practice tables restate the same spring-drive tally the
recycling guide's bar chart (`devices-collected-chart.png`)
delivers as a finding in Chapter 3: 154 items collected, cables
leading with 64. The results table repeats the chart's five
categories, and the drop-off log splits the same totals across the
four collection days. One drive, one truth, two presentations.

## events-content.txt

The six fall events repeat the officers' planning notes from the
Chapter 7 site expansion brief (`project-brief.txt`), word for
word, restated with labeled fields. The fields map to the table's
columns, so you copy values instead of retyping prose. The lab's
schedule table publishes this content at last.

## club-palette.txt

The palette travels with every CSS chapter, copied byte-identical
from the Chapter 9 pack. It maps the club's design set to exact hex
values and lists every text-on-background pairing that passes the
WCAG AA minimum for body text. The lab's header row and stripe
colors both come from that passing list, ratios included.

## Image files

All images are PNG and share one flat-illustration style: the
fictional club's matching design set. The seven files in
`starter-site/images/` are byte-identical to the Chapter 9 pack's
copies (one checksum per file name across the whole course
pack, verified), and their alt text is already written into
the site's pages. Each file's pixel dimensions and role are
documented once, in the Chapter 3 pack README's image table,
and that table applies to these copies unchanged.

## Source and license

Written for CIS133 by the course author. The PC Computer Club, its
officers, and its events are fictional, and the club's email
address uses the reserved example.org domain. All images are
original illustrations rendered by the course's seeded generator
script (`assets/code/_generators/generate_chapter03_images.py`), so
they carry no third-party license. The starter site is the Chapter
9 Skills Lab model solution, so Lab 10A does not punish a weak Lab
9A twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
