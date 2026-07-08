# Chapter 4 Data Pack: Skills Lab 4A Files

Starter files for Skills Lab 4A: Dress the Club's Site in Its Own
Colors. Students connect one external stylesheet to the club's
finished three-page site, style it with the club's own palette
using element, class, and id selectors, and validate both markup
and styles to zero messages. They never retype provided content,
and they copy every hex value from the palette file.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `starter-site/recycling-guide.html` | Valid HTML, the finished Lab 3A guide page | Parts 1-3 |
| `starter-site/drive-gallery.html` | Valid HTML, carries one leftover inline style | Parts 1-3 |
| `starter-site/contact.html` | Valid HTML, the finished Lab 3A contact page | Parts 1-3 |
| `starter-site/images/` | 7 PNG images, see the image table below | Parts 1-3 |
| `club-palette.txt` | Plain text palette with exact hex values and contrast notes | Try It Yourself 4.4, Parts 1-3 |
| `selector-practice.html` | Standalone chapter practice page | Try It Yourself 4.3 |
| `cascade-practice.html` | Chapter practice page linked to its stylesheet | Try It Yourself 4.2 and 4.5 |
| `practice-styles.css` | Small valid stylesheet beside its page | Try It Yourself 4.2, 4.4, and 4.5 |
| `skills-lab-4a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The starter site

`starter-site/` holds the club's finished Chapter 3 site: three
pages with full landmarks, working navigation, placed images, and
written alt text. All three pages validate with zero messages.
Students copy the whole folder into their lab folder and style it
without changing its structure.

One disclosure, in the spirit of Chapter 3's content file shipping
no alt text: `drive-gallery.html` carries exactly one leftover
inline `style` attribute on purpose. Part 3 of the lab sends
students hunting for it. The page still validates, because an
inline style is legal HTML. It is the wrong home for site styling,
which is the lesson.

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

**club-palette.txt** maps the design set's colors to exact hex
values with a usage note per color. The values were extracted from
the set's generator script, and every recommended text-on-background
pairing was checked against the WCAG AA minimum of 4.5 to 1 for
body text. It also lists two prop browns that look like the sand
color, so choosing the right one takes judgment.

**selector-practice.html** is a standalone announcements page for
the chapter's selector exercise. Two of its paragraphs carry
`class="deadline"`. It links no stylesheet, because the exercise
adds rules internally.

**cascade-practice.html and practice-styles.css** travel as a
pair. The page links the stylesheet with a bare relative href, so
both files must stay in the same folder. The stylesheet holds
three correct rules using palette colors. Chapter exercises pile
conflicting rules onto its heading, read its color swatches in
VS Code, and later break a declaration on purpose to see what the
CSS validator reports.

**skills-lab-4a-answers.txt** holds numbered answer spaces: the
Part 1 link placement and one-file observation, the Part 2
selector log and class-vs-id justification, the Part 3 inline
style hunt and validator log, and the Questions & Analysis
section. It travels inside the submission folder unrenamed.

## Source and license

Written for CIS133 by the course author. The PC Computer Club and
its events are fictional, and the club's email address uses the
reserved example.org domain. All seven images are original
illustrations rendered by the course's seeded generator script
(`assets/code/_generators/generate_chapter03_images.py`), so they
carry no third-party license. The starter pages are the Chapter 3
Skills Lab model solutions, so Lab 4A does not punish a weak
Lab 3A twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
