# Skills Lab Rubric: Single-Source Reference

The rubric table no longer lives in this file, in chapters, or in any
copy an author edits by hand. The canonical master for the whole
textbook family is `../../shared/skills-lab-rubric.md`. The sync
script (`../../shared/tools/sync-shared.sh`) copies it into each book
at `book/skills-lab-rubric.md`, which publishes as the "Skills Lab
Rubric" page in the site nav.

To change the rubric: edit the master in `shared/`, re-run the sync,
rebuild each book, and commit in each repo. Never hand-edit the synced
copy.

## How chapters reference the rubric

Chapter 1 (first use) displays the full table by transcluding it at
build time. Under the `### Rubric: Skills Lab 1A` heading:

```text
Every Skills Lab in this book is graded with the same 16-point rubric.
Bookmark the [Skills Lab Rubric](../skills-lab-rubric.md) page for
quick reference in later chapters.

--8<-- "skills-lab-rubric.md:rubric"
```

Chapters 2-12 reference the page instead of repeating the table:

```text
This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): 16 points, four criteria
at 4 points each (Code Accuracy and Efficiency, Output Quality,
Documentation and Code Comments, and Analysis, Interpretation, and
Response to QUESTION(s)).
```

The transclusion works because `pymdownx.snippets` is enabled in
`zensical.toml` with `base_path = ["book"]`. The include pulls only
the table between the snippet section markers in the rubric file, so
the rubric page's preamble never leaks into chapters.

## Why one universal rubric

Students who take more than one course in this family learn the four
criteria once: Code Accuracy and Efficiency, Output Quality,
Documentation and Code Comments, and Analysis, Interpretation, and
Response to QUESTION(s). The 16 points split evenly between technical
execution (8) and transferable skills (8).
