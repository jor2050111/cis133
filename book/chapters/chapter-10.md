# Chapter 10: HTML Tables

The officers' expansion brief has waited three chapters to be paid. Its second request was an events page: visitors keep asking when the next drop-off is, so publish the fall schedule. A helpful clubmate took a first pass this week and pasted the six events into a draft page as six paragraphs. Now try to answer one visitor's question: when is the Fix-It Workshop? You read all six paragraphs to find out. The officers' notes have structure the paragraphs threw away. Every event answers the same five questions: its name, date, time, location, and one detail worth knowing.

The draft also marks a turn in the course. Part III designed for every user: you planned the site, adapted it to every screen, and audited it against WCAG. Part IV builds the pages the site plan promised, starting here. The tool this chapter adds is the HTML table, the element that gives every fact two addresses: its row and its column. A visitor hunting the workshop date reads down one column and across one row, and the answer waits at the intersection. No full read required.

You will learn to tell table data from everything else, and to refuse tables that only want to arrange boxes. You will build the grid from its elements, then make it announce itself honestly to every tool, because Devon is still a member and Chapter 9's work never pauses. You will style the grid until a schedule reads at a glance, and teach a wide table to behave on a phone. Skills Lab 10A publishes the fall schedule at last and adds the events page to every page's navigation. Final Checkpoint 2, the first draft pages of your own site, rides right behind it.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 3-9 (semantic structure, CSS selectors and the box model, pseudo-classes, responsive habits, and the accessibility standard)
* **Deliverables:** Skills Lab 10A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-10.1 (Analyze):** Differentiate data that belongs in a table from content that belongs in lists or layout, justifying the choice
* **MLO-10.2 (Apply):** Construct accessible data tables with rows, header and data cells, captions, and header scope
* **MLO-10.3 (Create):** Produce the club's events page: a styled, readable schedule table integrated into the site

---

## 10.1 The Right Tool for the Data

Before the markup, the judgment call. HTML gives you an element built for data grids, and the first skill is knowing which content deserves it. The campus tutoring center returns as this chapter's test bench, because its content poses the question three ways.

The center's site holds a welcome paragraph, a five-step enrollment procedure, and a drop-in schedule: four subjects, each with a day, hours, and a room. Ask what any single value in that schedule means. "Thursday" means nothing on its own. It means what its row and its column say together: Chemistry tutoring runs on Thursday. That double address is the test. Content is **tabular data** when every value takes its meaning from two directions at once, its row and its column. A paragraph has no axes: it means what its sentences say. A list has one axis: each item stands alone, and at most its position matters. A table has two.

Run the center's three content blocks through the test:

| Content | Axes of meaning | The right tool |
| --- | --- | --- |
| The welcome paragraph | None: it reads as sentences | A paragraph |
| The enrollment steps | One: each step's position in the sequence | An ordered list |
| The drop-in schedule | Two: the subject's row and the fact's column | A table |

The pattern generalizes. Schedules, results tallies, and side-by-side comparisons earn tables, because their readers arrive with a two-part question: which row, which fact. Procedures stay ordered lists, however grid-like they look. Prose stays prose.

One prohibition ships with the element, and its history explains it. Before CSS could lay out a page, developers built whole designs as giant invisible tables: the banner in one cell, the nav in another, every region nailed into a grid of fake data. That era is over. Flexbox arranges a line better (Chapter 6), media queries adapt it (Chapter 8), and neither one lies about the content. The lie is the disqualifier. A screen reader that meets a table announces a table and offers to read it by rows and columns. Aim that behavior at page furniture and the tool narrates layout as if it were data, row by meaningless row. The division of labor from Chapter 3 has not moved. Tables present data. CSS lays out pages.

### Try It Yourself 10.1: The Two-Axes Test 🛠️

**Predict:** Three more blocks want onto the center's site. The candidates: a roster of its tutors (name, subjects, and email for each), a tip list for preparing for a session, and a paragraph announcing new evening hours. Predict which one passes the two-axes test, and write one sentence naming its two axes.

**Run:** No files this time. Sketch your pick on paper as a grid: one row per entry, one column per fact, labels on both edges. Then cover any single cell's row and column labels with two fingers and try to say what the value means.

**Explain:** In 1-2 sentences, name one question the grid answers in a single glance that prose answers only after a full read. State which of the two axes does the finding.

### Quick Check 10.1 ✅

1. The center keeps a printer-loan log: each loan's date, the borrowing student, the device, and the return date. It also posts a three-step guide for booking a session. Run each through the two-axes test and name the right element for both.
2. A teammate proposes rebuilding a page header as a one-row table (logo in one cell, title in the next, nav links in the third) because "it lines up perfectly." Grade the proposal, and name the visitor it costs the most.
3. Anything can be forced into a grid. Name what the center's staff-bio paragraphs lack that tabular data has, and what a reader would lose if you gridded them anyway.

---

## 10.2 Table Structure: Rows, Cells, and Headers

Judgment made, the schedule earns its markup. Three elements build the grid, and their names do what Chapter 3 trained you to expect: they say what the content is.

```html
<!-- The drop-in schedule's first two subjects: one tr per
     subject, one td per fact. -->
<table>
    <tr>
        <td>Algebra</td>
        <td>Monday</td>
        <td>10:00 to 1:00</td>
    </tr>
    <tr>
        <td>Biology</td>
        <td>Tuesday</td>
        <td>1:00 to 4:00</td>
    </tr>
</table>
```

The **table element** (`<table>`) wraps the grid. Each **table row** (`<tr>`) holds one horizontal run of cells, one subject per row here. Each **data cell** (`<td>`) holds one value. Now notice what the markup never mentions: columns. No column element exists. Columns emerge from position, every row's first cell stacking into the first column, every second cell into the second. Position is a promise, so every row must carry the same number of cells.

Break the promise and the browser stays calm. It draws the short row with a gap where the missing cell would sit, and shifts nothing. The HTML checker is less calm. Fed a two-column test table whose second row held a single cell, it answers with a warning:

```text
Warning: A table row was 1 columns wide, which is less than the
column count established by the first row (2).
```

A warning is not an error, but your bar has been zero messages since Chapter 2, and a ragged row keeps a page from it. Count cells whenever a row misbehaves.

The schedule's top row should not be data cells at all, because Subject, Day, and Hours are not facts about any subject. They are the names of the columns. The **header cell** element (`<th>`) marks a cell that names things:

```html
<!-- The header row: th for names, td for values. It sits
     first, like any other row. -->
<tr>
    <th>Subject</th>
    <th>Day</th>
    <th>Hours</th>
</tr>
```

Browsers hand header cells a default look of their own, and Chapter 3 already taught you how much default looks matter: not much. Whatever the browser draws is a side effect one CSS rule can change, and TIY 10.2 has you catch the look in the act. The meaning is the point. A `<th>` tells every tool that this cell names its column, and Section 10.3 spends that meaning.

One more layer of honesty separates the namers from the named. The **thead element** (`<thead>`) groups the header row, and the **tbody element** (`<tbody>`) groups the data rows:

```html
<!-- The same schedule, its rows grouped by job. -->
<table>
    <thead>
        <tr>
            <th>Subject</th>
            <th>Day</th>
            <th>Hours</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Algebra</td>
            <td>Monday</td>
            <td>10:00 to 1:00</td>
        </tr>
        <tr>
            <td>Biology</td>
            <td>Tuesday</td>
            <td>1:00 to 4:00</td>
        </tr>
    </tbody>
</table>
```

Nothing visible changes, which should ring a Chapter 3 bell: landmarks changed no pixels either. The split states which rows are structure and which are data, and Section 10.4 pays it, the moment a style rule needs to know exactly where the data starts. The browser holds its own opinion about this split, and TIY 10.3 catches it acting on that opinion.

Two powers get named once and set aside. Cells can span several columns or rows with the `colspan` and `rowspan` attributes, and this course's tables never need them. A third grouping element, `<tfoot>`, wraps summary rows, and the course never needs it either.

### Try It Yourself 10.2: The Naked Table 🛠️

**Predict:** Open `assets/code/chapter-10/table-practice.html` in VS Code and read it without opening a browser. The table holds the spring drive's category counts, the same data behind Chapter 3's chart on the guide page. Predict the render: does the browser draw grid lines? Borders anywhere at all? What type does the header row wear?

**Run:** Open the page in the browser and grade your three predictions against the screen.

**Explain:** In 1-2 sentences, name what the browser supplied on its own and what it left entirely to CSS. Then pick the presentation of this tally a visitor gets more from today: Chapter 3's chart or this table.

### Try It Yourself 10.3: The Browser's Silent Repair 🛠️

**Predict:** `table-practice.html` contains no `<tbody>` tag: confirm it with Ctrl+F (Cmd+F on Mac) in VS Code. Will the DevTools Elements panel match the file? Write yes or no, plus one sentence of reasoning.

**Run:** With the page open, open DevTools and expand the `<table>` in the Elements panel. Compare the tree against the file in VS Code, and count the rows inside anything the file did not write.

**Explain:** In 1-2 sentences, name what the browser built without asking, and state why writing that structure yourself keeps your file honest with the page the browser serves. Section 10.4 pays this discovery.

### Quick Check 10.2 ✅

1. In one sentence each, state the claim a `<td>` makes about its content and the claim a `<th>` makes.
2. A three-column table has one row holding only two cells. Describe what the browser draws for that row, and state what the HTML checker reports: an error, a warning, or silence.
3. The schedule renders identically with and without `<thead>` and `<tbody>`. Give one reason to write them anyway, this chapter's version of a familiar Chapter 3 argument.

---

## 10.3 Tables Every Tool Can Read

Chapter 9 ended with a promise: the events page would continue its work, with headers, scope, and captions carrying the accessibility habits into the grid. This section keeps that promise. Devon reads tables too, and a well-built one makes for good listening. A screen reader entering a table announces its size, then reads any cell together with the headers that govern it, on request: "Chemistry, Thursday, 2:00 to 5:00." No guesswork, no counting cells aloud. Every word of that announcement is assembled from markup, and this section writes the markup.

Start with the title. The **caption element** (`<caption>`) gives a table its own name, written as the table's first child, before `<thead>` and every row:

```html
<!-- The table's own title rides inside it, always first. -->
<table>
    <caption>Fall drop-in tutoring schedule</caption>
    <thead>
        <tr>
            <th>Subject</th>
            <th>Day</th>
            <th>Hours</th>
        </tr>
    </thead>
    <!-- data rows unchanged -->
</table>
```

Why not a heading above the table? On screen the two can look alike, and to tools they are strangers. The caption belongs to the table: a screen reader announces it on entering the grid, lists it in its menu of the page's tables, and wherever the table travels, the title travels inside it. A nearby heading promises none of that. You have met this pattern before: `<figcaption>` does the same job for figures. Tables bring their own.

First child is law, not style advice. Place the caption anywhere else and the HTML checker objects. Here is its verbatim answer for a caption slipped in after the header row:

```text
Error: Element "caption" not allowed as child of element "table"
in this context. (Suppressing further errors from this subtree.)
```

Headers name, and the **scope attribute** says what they govern. The decision runs by position:

| The header | Its scope | It governs |
| --- | --- | --- |
| A column header in the top row | `scope="col"` | Every cell below it |
| A row header leading its row | `scope="row"` | Every cell beside it |

Column headers the schedule has. Row headers it has been hiding. Each subject name is not a fact about its row, it is the row's name, so those cells deserve a promotion from `<td>` to `<th scope="row">`:

```html
<!-- The finished schedule: column headers govern down, and
     each subject cell is a row header governing across. -->
<table>
    <caption>Fall drop-in tutoring schedule</caption>
    <thead>
        <tr>
            <th scope="col">Subject</th>
            <th scope="col">Day</th>
            <th scope="col">Hours</th>
            <th scope="col">Room</th>
        </tr>
    </thead>
    <tbody>
        <!-- The other subjects' rows follow the same pattern. -->
        <tr>
            <th scope="row">Chemistry</th>
            <td>Thursday</td>
            <td>2:00 to 5:00</td>
            <td>L207</td>
        </tr>
    </tbody>
</table>
```

With scope in place, the opening announcement assembles itself. Devon lands on a cell and asks for its headers, and the reader walks the markup: the row header says Chemistry, the column header says Hours, the cell says 2:00 to 5:00. None of this needed a new standard, and none of it adds a number to memorize. Caption, headers, and scope are POUR's perceivable and robust principles carried into the grid, at the same Level AA bar every page has answered since Chapter 9.

### Try It Yourself 10.4: The Caption Arrives 🛠️

**Predict:** The practice table still has no caption, and its data still restates Chapter 3's chart. You will add this exact line as the table's first child: `<caption>Spring Drive Results: 154 items collected</caption>`. Predict where the text will render relative to the grid, and in what type: body-plain, bold, centered, something else?

**Run:** Add the line directly after the opening `<table>` tag in `table-practice.html`, save, and reload.

**Explain:** In 1-2 sentences, name who receives this title that a paragraph above the table would deny, and state what the first-child law guarantees about the title and its grid.

### Quick Check 10.3 ✅

1. A teammate titles a schedule with an `<h3>` directly above the table and calls it "the same thing as a caption." Name two things the caption delivers that the heading cannot.
2. The library's study-room grid leads each row with a room name and heads each column with a weekday. Name which cells become `<th>`, and assign each its scope value.
3. A finished schedule marks every cell `<td>`, headers included. Describe what a screen reader can still do with that grid, and what it can no longer do, compared to the table this section built.

---

## 10.4 Styling Tables for Readability

TIY 10.2 delivered the verdict: the browser draws no grid at all. Every border on the naked practice table computes to zero, the whole tally shrink-wraps to 199 pixels, and the bold header row is the browser's entire contribution. Chapter 5 turned readable type into a four-point checklist. Tables extend the same duty, because a grid nobody can scan is data nobody gets.

Borders come first, and they come with a surprise. Put a border on `th` and `td` and the browser keeps its default gap between neighboring cells, 2 pixels of border-spacing, so every interior line draws doubled. The **border-collapse** property retires the gap: its `collapse` value merges neighboring borders into single shared lines. On a two-column probe table, identical markup measured 147 pixels wide with separate borders and 140 collapsed. Seven pixels of doubled lines, gone.

```css
/* One clean line per boundary. The table opens the collapse,
   and the cells own the borders and the breathing room. */
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #333333;
    padding: 8px 12px;
    text-align: left;
}
```

Read the division of labor before moving on. The collapse rides on the table, because the table owns the gaps. The borders ride on `th, td`, because a border on the table alone outlines the grid and draws nothing between the cells. The padding is Chapter 5's box model at its oldest job, keeping every value off its own walls. `text-align: left` settles the header question: `th` centers by default, and a header reads best sitting flush over the column it names. And `width: 100%` lets the table claim its container instead of shrink-wrapping its content, which is how 199 pixels happened.

Wide tables ask the eye to hold a line across many columns, and **zebra striping** is the standing aid: a soft background tint on every other data row. The selector that builds it is new, and it is deliberately the last new selector of the course. Chapter 6's `:hover` and `:focus` matched elements by state, what is happening to them right now. A **structural pseudo-class** matches by position instead: where an element sits among its siblings. **`:nth-child()`** is the one this course teaches, and its `even` and `odd` keywords select alternating siblings.

```css
/* Tint every even data row. Scoping to tbody starts the count
   at the first data row, because the header row lives in thead,
   outside the count. */
tbody tr:nth-child(even) {
    background-color: #f2f2f2;
}
```

The tutoring schedule wrote its `<thead>` and `<tbody>` in Section 10.3, so its count is clean. The selector reads: rows inside the tbody, at even positions among the tbody's own children. The header row lives in the thead, outside the count entirely, and the tint lands on data rows two and four, Biology and Writing. Hold onto that reasoning. TIY 10.5 hands you a table that never wrote the split and asks the same question.

One more reading aid costs one rule: light the row under the pointer. The selector reuses Chapter 6's `:hover`, and its placement matters more than its color:

```css
/* The reading aid under the pointer. This rule sits after the
   stripe rule on purpose: the two selectors tie on specificity,
   so the later rule wins and the highlight shows on striped
   rows too (Chapter 4's tie-breaker at work). */
tbody tr:hover {
    background-color: #e0e0e0;
}
```

!!! tip
    A stripe is a background behind body text, so the pairing must clear the same contrast bar as any text on the site. The grays above are teaching stand-ins. The club palette's passing list carries stripe-ready pairings, and the lab shops from it.

### Try It Yourself 10.5: Stripe the Results 🛠️

**Predict:** `table-practice.html` still has no `<thead>` or `<tbody>`, as TIY 10.3 confirmed. You will append the stripe rule exactly as this section wrote it, `tbody tr:nth-child(even) { background-color: #f2f2f2; }`, to `practice-styles.css`. Predict which rows will paint. Does the header row count as row one? Write your list of painted rows before touching anything.

**Run:** Append the rule, save, and reload. Record which rows painted. Then edit the HTML: wrap the header row in `<thead>` and the five data rows in `<tbody>`, save, and reload again.

**Explain:** In 1-2 sentences, use TIY 10.3's discovery to explain the first paint pattern, and state what writing the split yourself changed about which row counts as row one.

### When the Table Meets the Phone

Every page you have shipped since Chapter 8 obeys one law: the page itself never scrolls sideways. Tables strain that law harder than anything else you own, because a table refuses to shrink past its content. A cell will not wrap below its longest word, a column must seat its widest cell, and the sum of those minimums is a floor. A schedule with enough columns carries a floor wider than a phone, and then something has to give. TIY 10.6 puts a seven-column table on a 375-pixel screen so you can watch what gives.

The honest repair at this course's level is a scroll container: one wrapper, one rule.

```html
<!-- The wrapper takes the sideways scroll so the page never
     has to. -->
<div class="table-scroll">
    <table>
        <!-- the schedule, unchanged -->
    </table>
</div>
```

```css
/* The wrapper's one job: a policy for content wider than
   itself. */
.table-scroll {
    overflow-x: auto;
}
```

`overflow-x: auto` hands the wrapper a policy for content wider than itself. What that policy does to the table, and to the page's own footing against the law, is TIY 10.6's discovery to make. The `<div>` is the right container for exactly Chapter 3's reason: no semantic element means "scrolling viewport," so the meaningless box takes the styling job. One line of foresight before the exercise: tables are not the only content that can hit a phone-width wall. Any bar of items can meet it, and `flex-wrap` from Chapter 6 already answers that one.

### Try It Yourself 10.6: The Phone Test 🛠️

**Predict:** Open `assets/code/chapter-10/wide-practice.html` in VS Code: the spring drop-off log, seven columns, structurally complete. In device mode at 375 pixels, will the columns squeeze until the table fits, or will something scroll sideways? If something scrolls, predict which element it will be. Then predict what changes once the wrapper arrives.

**Run:** Open the page in device mode at 375 pixels and try to read the whole log. Record what moves. Then wrap the table in the `.table-scroll` div, add the wrapper rule to `practice-styles.css`, and run the same test again.

**Explain:** In 1-2 sentences, state which element takes the sideways scroll after the repair, and how the page's standing against Chapter 8's law changed between the two runs.

!!! note
    Judge any table repair the Chapter 8 way: device mode, a phone profile, and a slow walk down the whole page. A table that pans inside a page that stands still is the pass. A page that moves with it is not.

### Final Checkpoint 2: Draft Pages

Checkpoint 1 asked for a plan. Final Checkpoint 2 asks for pages: the first draft pages of your own final site, built to the standard this chapter's lab models. Draft means structurally honest, not finished. Each page carries the full head skeleton, real content in real landmarks, working navigation between the drafts, and a clean pass through the Chapter 9 habits: both validators plus the checklist. Your home page can wait, because Chapter 12 builds it when the whole site publishes and re-runs every check first. The course shell carries the dates and the required page count. The events page you are about to build is the working pattern. You are not practicing pages this week. You are building your site.

### Quick Check 10.4 ✅

1. A teammate put a 1px border on `th` and `td` and complains that every interior line draws doubled. Name the property and value that repair it, and state which element the rule belongs on.
2. The study-room grid wrote `<thead>` and `<tbody>`. Write the one rule that tints its even data rows, and explain what keeps the header row out of the count.
3. At phone width, a nine-column table overflows. One teammate wants to shrink `font-size` until the table fits. Defend the scroll wrapper instead, using this section plus one Chapter 9 rule.

---

## 10.5 Summary and Retrieval 💡

### Key Concepts

* Content earns a table by the two-axes test: every value means what its row and its column say together. Steps stay ordered lists, prose stays paragraphs, and layout belongs to CSS. A layout table makes a screen reader narrate page furniture as data.
* The grid is `<table>`, `<tr>` rows, `<td>` data cells, and `<th>` header cells, with columns emerging from cell position. Every row carries the same cell count, and the checker warns when one falls short. `<thead>` and `<tbody>` group the namers apart from the named.
* Tools read the markup, not the pixels. The caption is the table's own title, first child by validator-enforced law. `scope="col"` and `scope="row"` tell a screen reader which headers govern which cells, so Devon hears "Chemistry, Thursday, 2:00 to 5:00" instead of a bare value.
* Naked tables draw no grid. `border-collapse: collapse` on the table merges doubled lines, cells take the borders and padding, and `text-align: left` seats headers over their columns.
* Zebra striping uses the course's last new selector: `tbody tr:nth-child(even)`, a structural pseudo-class matching position instead of state. The thead/tbody split keeps the header row out of the count, and the hover rule sits after the stripe rule so the later rule wins their tie.
* A wide table can out-floor a phone. The repair is a wrapper div with `overflow-x: auto`: the wrapper scrolls, the page keeps the no-sideways-scroll law. Final Checkpoint 2 is open: draft pages of your own site, built to this chapter's pattern.

### Key Terms

See course glossary for full definitions

* tabular data (Section 10.1)
* table element, table row, data cell, header cell, thead element, tbody element (Section 10.2)
* caption element, scope attribute (Section 10.3)
* border-collapse, zebra striping, structural pseudo-class, :nth-child() (Section 10.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the grid's anatomy: the element that wraps it, the element for a row, the two kinds of cells, and the two grouping elements.
2. State the two-axes test, then apply it from memory to a bus schedule and to a recipe's steps.
3. Write the zebra stripe rule from memory and explain why it is scoped to `tbody`.
4. A seven-column table meets a phone. Recite the repair: the wrapper, its one rule, and the law it protects.
5. Name the two pieces of table markup that exist for tools, not for pixels, and what a screen reader does with each.

---

## 10.6 Skills Lab 10A: The Events Page

**Goal:** Produce the club's events page: the officers' fall schedule as an accessible, styled table, linked from every page's navigation, closing the site plan's first promised addition.

**Dataset:** Provided files in `assets/code/chapter-10/` from the course data pack. `starter-site/` holds the club's three pages, the `images` folder, and `club-styles.css` exactly as Skills Lab 9A finished them: the pages are unchanged, and the stylesheet's type now speaks rem. `events-content.txt` carries the six fall events with labeled fields, word for word from the Chapter 7 brief's planning notes, so you copy values instead of retyping prose. `club-palette.txt` travels with every CSS chapter, and its passing list supplies every color this lab's table wears. `table-practice.html`, `wide-practice.html`, and `practice-styles.css` are the chapter's Try It Yourself files and stay out of the submission. `skills-lab-10a-answers.txt` is your written answers file. Part 3 reuses `accessibility-checklist.txt` from the Chapter 9 pack. The folder's README documents every file. Work at the extracted `cis133` root.

The lab walks the chapter's own path. Part 1 builds the page and its table and wires the navigation. Part 2 styles the grid from the palette's passing list. Part 3 survives the phone, passes the Chapter 9 habit, and hands off to Final Checkpoint 2.

### Part 1: Foundation (Aligns with MLO-10.2)

1. Create a folder named `skills-lab-10a-lastname` at your `cis133` root. Copy in the whole `starter-site` folder, keeping its name, and `skills-lab-10a-answers.txt`.
2. Create `events.html` inside `starter-site` the Chapter 2 way: open an existing page, save as, and keep everything the pages share. Retitle the head, keep the header, nav, and footer, and clear `main` down to one short intro paragraph you write.
3. Build the schedule table inside `main`: a caption you write, a `<thead>` row of five `<th scope="col">` headers, and six `<tbody>` rows copied from `events-content.txt`. The file's own field labels name your columns: Event, Date, Time, Location, Details. Record the build in answer 1.A.
4. Add the events link to the navigation bar on all four pages, between the gallery link and the contact link, the site plan's order. Choose the link text yourself, and let Chapter 7's label law choose with you.
5. Validate all four pages to zero messages, and record the nav update and the counts in answer 1.B.

### Part 2: Application (Aligns with MLO-10.3, MLO-10.2)

1. In `club-styles.css`, add a commented table block below the base rules and above the query block, so the query block keeps the bottom of the file. Set the collapse, the cell borders and padding, the table's width, and your alignment call. Record the block's decisions in answer 2.A.
2. Dress the grid from the palette's passing list: one pairing for the header row, one for the zebra stripe. Both calls are yours to make and defend. Quote each pairing's ratio from the list in answer 2.B, along with any pairing you considered and rejected.
3. Stretch, here or in Part 3: the row hover from Section 10.4, placed after the stripe rule. Validate the stylesheet to zero messages.

### Part 3: Extension (Aligns with MLO-10.3, MLO-10.1)

1. Run the phone test on the finished events page in device mode at a phone width. Walk the whole page and log everything that breaks the no-sideways-scroll law, top to bottom, before you fix anything: Chapter 9's audit-first habit. Then repair each finding with the tool that owns it, and know that not every repair is new this chapter. Record the findings, the fixes, and which element scrolls now in answer 3.A.
2. Run the Chapter 9 habit on the new page: copy `accessibility-checklist.txt` from the Chapter 9 pack, run all seven checks on `events.html`, and repair anything they surface. Then validate all four pages and the stylesheet to zero messages. Log the findings and counts in answer 3.B.
3. Close answer 3.B with two hand-downs. First, the right-tool defense: why the schedule earned a table while the recycling guide's preparation steps stayed a list. Second, the Final Checkpoint 2 hand-off: name the draft pages of your own site that will follow this page's pattern.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Your finished table carries a caption, header cells with scope, and a stripe from the passing list. Assign each of those features one visitor it serves, name what each replaces or prevents, and cite your own page as evidence.
2. The officers' notes already published this schedule as readable prose in the Chapter 7 brief. Using the two axes of meaning, argue what the table version answers that the prose version cannot. Then name one content block on the club's site that must never become a table, and defend the refusal.

**Submission:** Zip your `skills-lab-10a-lastname` folder containing the updated `starter-site` folder (four pages, `club-styles.css`, and `images`), your completed checklist copy, and `skills-lab-10a-answers.txt`, and submit it as `skills-lab-10a-lastname.zip`. Every page and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 10A

| Criteria | Mastery (4) | Proficiency (3) | Developing (2) | Emerging (1) | Not Evident (0) |
| --- | --- | --- | --- | --- | --- |
| **Code Accuracy and Efficiency** | Code is Accurate, Efficient, and ERROR-FREE. Demonstrates optimal use of HTML and CSS syntax and the course tools | Code is mostly accurate and efficient. MINOR ERRORS are present but do not significantly affect the output or performance | Code runs but contains SOME ERRORS or INEFFICIENCIES. The output is sometimes incorrect or incomplete | Code is FREQUENTLY INCORRECT or inefficient, with multiple errors that prevent the program from running | No Submission or Not Evident |
| **Output Quality** | EXCEPTIONAL outputs with outstanding clarity and detail. They effectively enhance understanding of the work | GOOD quality outputs that accurately represent the results. Well-labeled and clear | Outputs are ADEQUATE but lack sophistication or have minor errors in labeling or presentation | Outputs are POORLY CONSTRUCTED, unclear, or irrelevant. Labeling is missing or incorrect | No Submission or Not Evident |
| **Documentation and Code Comments** | COMPREHENSIVE and concise documentation and comments. They greatly enhance the readability and understanding of the code | CLEAR documentation and comments that aid in understanding the code's purpose and logic | SOME documentation and comments are present, but they lack clarity or are incomplete | MINIMAL or no documentation and comments. Code is difficult to follow | No Submission or Not Evident |
| **Analysis, Interpretation, and Response to QUESTION(s)** | COMPREHENSIVE and INSIGHTFUL analysis. Interpretations are precise and fully supported by compelling evidence. Answers to questions are thorough, demonstrating deep understanding and insight | SOLID analysis. Interpretations are logical, well-reasoned, and supported by evidence. Answers to questions demonstrate a good understanding of the material | BASIC analysis is conducted. Interpretations are present but lack depth or detail. Answers to questions are basic and show limited understanding | Analysis is MINIMAL or incorrect. Interpretations and conclusions are missing or irrelevant. Fails to adequately answer the questions asked in the assignment | No Submission or Not Evident |

**Scoring:** 16 points total (4 points per criterion)

---

## 10.7 Review Questions 🔄️

1. **Remember:** Name the four elements that build a table's grid and the two grouping elements that organize its rows. Then name the element and the attribute this chapter added for the tools that read tables.

2. **Understand:** The intramural soccer league's standings table writes `<thead>` and `<tbody>`, and its stripe rule reads `tbody tr:nth-child(even)`. Explain what the grouping split contributes to the stripe: which rows the selector counts, and what would change about the count in a file that never wrote the split.

3. **Apply:** The food pantry published its hours in the table below. Rewrite it so every tool can read it: a title that travels with the table, honest header cells with scope in both directions, and the grouping split.

    ```html
    <table>
        <tr>
            <td>Day</td>
            <td>Open</td>
            <td>Close</td>
        </tr>
        <tr>
            <td>Wednesday</td>
            <td>10:00 a.m.</td>
            <td>2:00 p.m.</td>
        </tr>
        <tr>
            <td>Saturday</td>
            <td>9:00 a.m.</td>
            <td>noon</td>
        </tr>
    </table>
    ```

4. **Analyze:** The soccer league's new site presents its photo gallery as a table (one photo per cell, "because it makes a perfect grid") and its league standings as paragraphs of prose. Critique both calls with the two-axes test, name the right tool for each job, and state which visitor pays the highest price for each mistake.

---

## Further Reading 📖

* [MDN: The table element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table) - This chapter's anatomy on one reference page, with every table element linked from it.
* [MDN: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics) - The gentlest full walk through rows, cells, headers, and captions: a second telling of Sections 10.2 and 10.3.
* [W3C WAI: Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/) - The accessibility source this chapter's scope and caption teaching follows, with screen reader context throughout.
* [MDN: Styling tables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Tables) - Section 10.4 extended, with zebra striping and caption styling among its examples.
* [MDN: :nth-child()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child) - The course's last new selector in full, including the pattern arguments this course leaves untaught.

---

## Looking Ahead ⏩

The site plan promised three additions, and the first is now live in the nav. The home page waits for Chapter 12, when the whole site publishes behind a full pre-flight check. Next comes the join page: the officers want to collect the name and email of every interested student, and collecting input is the job of HTML forms. Chapter 11 builds that page on the partnership Chapter 9 promised, the contract between every input and the label that announces it.
