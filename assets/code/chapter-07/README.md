# Chapter 7 Data Pack: Skills Lab 7A Files

Planning artifacts for Skills Lab 7A: The Copperwind Site Grows Up. This
chapter's lab produces a site plan, not code. Students digest
Copperwind's expansion brief and audit the finished Copperwind site against
the five UX principles. They construct a six-page sitemap,
wireframe new pages at two widths, and assemble everything into a
stakeholder document. The same site plan template returns for Final
Checkpoint 1, the final project's first deliverable.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `copperwind-site/recycling-guide.html` | Valid HTML, links the Oswald font and the site stylesheet | Part 1 (audit target) |
| `copperwind-site/drive-gallery.html` | Valid HTML, links the Oswald font and the site stylesheet | Part 1 (audit target) |
| `copperwind-site/contact.html` | Valid HTML, links the Oswald font and the site stylesheet | Part 1 (audit target) |
| `copperwind-site/copperwind-styles.css` | Valid CSS, the site stylesheet as Skills Lab 6A finished it | Part 1 (audit target) |
| `copperwind-site/images/` | 7 PNG images, see the image table below | Part 1 (audit target) |
| `project-brief.txt` | Plain text expansion brief from the outreach coordinator | Parts 1-3 |
| `ux-audit-worksheet.txt` | Plain text audit worksheet for the five UX principles | Part 1, chapter exercises |
| `site-plan-template.txt` | Plain text site plan skeleton, also the Final Checkpoint 1 template | Part 3, Final Checkpoint 1 |
| `wireframe-examples.txt` | Plain text ASCII wireframe skeletons at two widths | Part 2, chapter exercises |
| `skills-lab-7a-answers.txt` | Plain text answer file (travels in the submission folder) | Parts 1-3, Questions & Analysis |

## The Copperwind site

`copperwind-site/` holds the Copperwind site exactly as Skills Lab 6A leaves
it: three pages, one external stylesheet, and the full Flexbox
layout. The header lays its logo and title on a flex line, and the
gallery wraps its figure plates two per line. The navigation bar
stands finished with hover and focus states, and the divider strip
finally sits centered. All three pages and the stylesheet validate
with zero messages.

One disclosure, and this time it is good news: the footer-link
defect the site carried from Chapter 4 through Chapter 6 is fixed
for keeps. The footer's links now wear light sand on the deep teal
footer, a pairing that passes contrast at 4.85 to 1, with hover and
focus states that invert it. The wart's account is closed.

This folder is the lab's audit target. Everyone audits this copy,
not their own Lab 6A build, so every student critiques the same
site. It also becomes the starter site for Chapter 8's lab, so
leave it unedited.

## Image files

All seven images are PNG and share one flat-illustration style:
the fictional Copperwind design set. Their alt text is
already written into the pages. The table exists so the `width`
and `height` attributes can be checked against the files' true
pixels.

| File | Pixels | Contents |
| ---- | ------ | -------- |
| `copperwind-logo.png` | 240 x 240 | Copperwind logo: a saguaro, mountains, and a copper wind ribbon in a teal ring. Transparent background |
| `recycling-drive.png` | 800 x 450 | Outdoor collection drive: a canopy table, a volunteer, neighbors carrying devices, icon-marked bins |
| `devices-collected-chart.png` | 640 x 400 | Bar chart of items collected at the spring drive, five categories |
| `desert-divider.png` | 800 x 24 | Thin desert horizon strip: mountain silhouettes and tiny saguaros |
| `sorting-station.png` | 640 x 360 | A volunteer sorting phones, laptops, and cables into bins, seen from above |
| `donation-boxes.png` | 640 x 360 | Open cardboard boxes filled with donated electronics |
| `volunteer-crew.png` | 640 x 360 | Six volunteers, one using a wheelchair, standing near the collection bins |

## File details

**project-brief.txt** is the outreach coordinator's expansion brief, the
lab's founding document. It states the program's goals, describes two
audiences, and keeps the three existing pages. It asks for three
new ones: a home page, an events page with the fall schedule as
raw content, and a join page that collects names and
emails from anyone who wants program updates. The brief describes content needs in the team's own
voice and never prescribes markup. Deciding how to build what it
asks for is the work of Chapters 8 through 12.

**ux-audit-worksheet.txt** turns the chapter's five UX principles
(usability, accessibility, consistency, feedback, responsiveness)
into an audit instrument: a definition, a what-to-check prompt, and
blank strength and gap lines per principle. It ships blank on
purpose. The findings are the student's discovery, not the pack's.

**site-plan-template.txt** is the site plan skeleton: goals,
audience, sitemap, wireframes, navigation plan, and consistency
rules, with one instruction line per section. Lab 7A fills it for Copperwind. Final Checkpoint 1 fills it again for the student's own
final project site.

**wireframe-examples.txt** holds two ASCII wireframe skeletons of
a generic page, one at desktop width and one at phone width, drawn
with plain keyboard characters so they survive any viewer. Students
copy and adapt them, or sketch on paper and photograph the result.
Both submission forms are accepted.

**skills-lab-7a-answers.txt** holds numbered answer spaces: the
Part 1 brief restatement and audit summary, the Part 2 sitemap tree
and wireframe inventory, the Part 3 navigation defense and
self-critique, and the Questions & Analysis section. It travels
inside the submission folder unrenamed.

**No palette file ships this chapter**, and that is a design
statement. Wireframes are deliberately grayscale: structure first,
color never. The site's color decisions already live in
`copperwind-site/copperwind-styles.css`, and the palette file resumes its
travels with Chapter 8's pack, when the stylesheet work returns.

## Source and license

Written for CIS133 by the course author. Copperwind IT Services is a fictional company created for this textbook. All names, clients, and records are synthetic. Any resemblance to a real company or person is coincidental. The program's email address uses the reserved example.org domain. All seven images are
original course artwork (chart generator plus AI-generated
illustrations, see `assets/code/_generators/IMAGE-MANIFEST.md`), so
they carry no third-party license. The Copperwind site is the Chapter 6
Skills Lab model solution, so Lab 7A does not punish a weak Lab 6A
twice.

Copyright 2026 Jorge Vega, Phoenix College. Provided to enrolled
students for coursework.
