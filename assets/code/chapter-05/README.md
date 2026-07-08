# Chapter 5 Data Pack: Skills Lab 5A Files

Starter files for Skills Lab 5A: Give the Club's Site Breathing
Room. Students take the club's finished, fully colored three-page
site, space it with the box model, and set its typography for
comfortable reading, diagnosing their own spacing with the DevTools
box-model diagram. They never retype provided content, and every
color still comes from the palette file.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `starter-site/recycling-guide.html` | Valid HTML, links the site stylesheet | Parts 1-3 |
| `starter-site/drive-gallery.html` | Valid HTML, links the site stylesheet | Parts 1-3 |
| `starter-site/contact.html` | Valid HTML, links the site stylesheet | Parts 1-3 |
| `starter-site/club-styles.css` | Valid CSS, the site stylesheet from Lab 4A | Parts 1-3 |
| `starter-site/images/` | 7 PNG images, see the image table below | Parts 1-3 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Parts 2-3 and the chapter's readability checklist |
| `box-practice.html` | Standalone chapter practice page | Try It Yourself 5.1 through 5.5 |
| `box-practice.css` | Practice stylesheet beside its page | Try It Yourself 5.1 through 5.5 |
| `skills-lab-5a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The starter site

`starter-site/` holds the club's site exactly as Skills Lab 4A
left it: three pages connected to one external stylesheet,
`club-styles.css`, wearing the club's palette through element,
class, and id selectors. All three pages and the stylesheet
validate with zero messages. Students copy the whole folder into
their lab folder and give it space and type without changing its
structure.

The stylesheet's design, for orientation: ink text on a light sand
base, a club teal header with white text, a white nav bar, a deep
teal footer, deep teal h2 headings and figure captions, a reminder
class on sunset orange used on two pages, one id on the contact
page's meeting schedule with a sand panel, and white plates behind
the figures. Every text-on-background pairing appears on the
palette file's passing list.

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
byte-identical from the Chapter 4 pack so this folder stays
self-contained. It maps the design set's colors to exact hex
values with a usage note per color, lists two lookalike prop
browns, and records every text-on-background pairing that passes
the WCAG AA minimum of 4.5 to 1 for body text. The chapter's
readability checklist starts with that passing list.

**box-practice.html and box-practice.css** travel as a pair. The
page links the stylesheet with a bare relative href, so both files
must stay in the same folder. The page stacks three announcement
boxes whose width, padding, and border values were chosen so the
box-model math works out in whole pixels, and the chapter quotes
those exact numbers. One disclosure, in the spirit of Chapter 4's
planted inline style: the page's drive-notes region is cramped on
purpose. Its tiny font, tight line height, missing padding, and
unlimited line length are the diagnosis material for a chapter
exercise. Both files still validate with zero messages, because
bad design is legal CSS. That is the lesson.

**skills-lab-5a-answers.txt** holds numbered answer spaces: the
Part 1 before-and-after of one spaced region and one shorthand
expansion, the Part 2 readable-column justification and type log,
the Part 3 DevTools diagnosis and validator log, and the Questions
& Analysis section. It travels inside the submission folder
unrenamed.

## Source and license

Written for CIS133 by the course author. The PC Computer Club and
its events are fictional, and the club's email address uses the
reserved example.org domain. All seven images are original
illustrations rendered by the course's seeded generator script
(`assets/code/_generators/generate_chapter03_images.py`), so they
carry no third-party license. The starter pages and stylesheet are
the Chapter 4 Skills Lab model solution, so Lab 5A does not punish
a weak Lab 4A twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
