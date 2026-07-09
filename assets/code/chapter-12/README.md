# Chapter 12 Data Pack: Skills Lab 12A Files

Starter files for Skills Lab 12A: The Site Ships. Students build
the club site's home page, attach the course's one shipped script,
run the pre-flight check on all six pages, and publish the site to
a web server. Students never retype provided content: the home
page's words come from the officers' content file, and the lab's
script ships finished.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `starter-site/recycling-guide.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/drive-gallery.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/events.html` | Valid HTML, the events page Skills Lab 10A delivered | Parts 1-3 |
| `starter-site/join.html` | Valid HTML, the join page Skills Lab 11A delivered | Parts 1-3 |
| `starter-site/contact.html` | Valid HTML, links the Oswald font and the site stylesheet | Parts 1-3 |
| `starter-site/club-styles.css` | Valid CSS, the site stylesheet as Skills Lab 11A finished it | Parts 1-3 |
| `starter-site/images/` | 7 PNG images, unchanged from the Chapter 11 pack | Parts 1-3 |
| `home-content.txt` | The officers' home page content, block by block | Part 1 |
| `footer-year.js` | The lab's one script: writes the current year into the footer | Part 2 |
| `script-playground.html` | Three small script demos on one page | Chapter Try It Yourself exercises |
| `playground-script.js` | The playground's script file | Chapter Try It Yourself exercises |
| `path-test.html` | Two images, two styles of src | Chapter Try It Yourself exercises |
| `volunteer-crew.png` | The path test's photo, copied beside it on purpose | Chapter Try It Yourself exercises |
| `pre-flight-checklist.txt` | The page-by-page publishing checklist | Part 3 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Parts 1-3 |
| `skills-lab-12a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The starter site

`starter-site/` holds the club's site exactly as Skills Lab 11A
finished it: the Lab 11A model solution. Five pages now, because
the join page joined the site in Chapter 11. The stylesheet carries
the Lab 11A form block. All five pages and the stylesheet validate
with zero messages.

## The playground is a teaching prop

`script-playground.html` and `playground-script.js` exist so you
can watch a script work before the lab asks you to attach one. Run
the page first. Read the script only when an exercise says to.

One disclosure, because this file promises no answers: the members
corner's pass-phrase gate is deliberately insecure. That is the
lesson, not a defect, and the chapter asks you to discover why
before it explains. Never protect anything real this way.

## The path test is broken on purpose

`path-test.html` shows two photos, and one of its two src values
cannot work on any machine but its author's. Which one, and why,
is the exercise. Read both src values in VS Code and predict
before you open the page. The copy of `volunteer-crew.png` sitting
beside the file is intentional: the test needs an image the page
can reach with a relative path.

## home-content.txt

The officers' content for the home page: the headline, the
what-the-club-is paragraph, three what-we-do blocks, three links
with their target pages, and the standing meeting line. The blocks
map one-to-one onto what Skills Lab 12A builds, so you copy wording
instead of inventing it.

## footer-year.js

The lab's one script, finished and four lines short. It writes the
current year into the footer so nobody edits the site every
January. Its comment states the contract: the page supplies a span
with `id="footer-year"`, and the script element sits just before
the closing body tag.

## pre-flight-checklist.txt

The publishing instrument: eight checks per page, from both
validators through the live-URL verify. Copy the file once per
page, the same habit the Chapter 9 checklist taught.

## club-palette.txt

The palette travels with every CSS chapter, copied byte-identical
from the Chapter 11 pack. It maps the club's design set to exact
hex values and lists every text-on-background pairing that passes
the WCAG AA minimum for body text. The home page needs no color
the site does not already wear.

## Image files

All images are PNG and share one flat-illustration style: the
fictional club's matching design set. The seven files in
`starter-site/images/` are unchanged from the Chapter 11 pack, and
their alt text is already written into the site's pages.

## Source and license

Written for CIS133 by the course author. The PC Computer Club, its
officers, and its events are fictional, and the club's email
address uses the reserved example.org domain. The pass phrase and
the supply closet code in the playground are fictional teaching
props. All images are original illustrations rendered by the
course's seeded generator script
(`assets/code/_generators/generate_chapter03_images.py`), so they
carry no third-party license. The starter site is the Chapter 11
Skills Lab model solution, so Lab 12A does not punish a weak Lab
11A twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
