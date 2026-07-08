# Chapter 2: Basic HTML Elements

At the end of Chapter 1's lab, you sent the campus computer club a memo naming the sources it could trust for its electronics recycling page. The club president read it and replied with one line: "Great. Now build the page." That reply changes your seat. In Chapter 1 you watched pages arrive from servers and judged them. Starting now, you write the files the servers will send.

Every page on the web, from a campus club page to a streaming giant's home screen, starts the same way: as a plain text file full of HTML. HTML is the structure layer of the web. It tells the browser what each piece of content is: a heading, a paragraph, a list, a link. Get the structure right and every browser, every screen reader, and every search engine can read your page correctly. That skill is the start of CLO V, creating web pages, and this chapter also begins CLO IV, checking your markup with a validator instead of guessing.

This chapter walks you through your first build. You will set up VS Code and learn the edit-save-refresh cycle every developer lives in. You will write a complete HTML document from its first line to its last. You will structure text with headings, paragraphs, and lists, and connect pages with links. Then you will run your markup through the W3C validator, the referee Chapter 1 promised you. No prior coding experience is expected. Every step is shown.

## Module Overview 🧭

* **Estimated time:** 4-6 hours
* **Prerequisites:** Chapter 1 (the round trip of a page request and the parts of a URL)
* **Deliverables:** Skills Lab 2A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-2.1 (Apply):** Build a complete HTML document in VS Code that uses the required structure: doctype, html, head, and body
* **MLO-2.2 (Apply):** Structure page content with headings, paragraphs, lists, and links, choosing each element by the meaning of its content
* **MLO-2.3 (Analyze):** Diagnose markup errors in an HTML document by interpreting W3C validator reports

---

## 2.1 Your Workspace: VS Code, Files, and the Browser

Chapter 1 ended with the browser rendering files a server sent. Those files do not appear out of nowhere. A developer typed each one on an ordinary computer, saved it, and checked it in a browser, over and over, until it was right. This section sets up that loop on your machine.

### Web Pages Are Plain Text

An HTML file is a **plain text** file: nothing but characters, with no hidden formatting. That ruling matters more than it sounds. A word processor like Word or Google Docs buries invisible formatting data inside every file it saves, and that hidden data breaks a web page. So developers write HTML in a **text editor**, a program that saves exactly the characters you type and nothing else.

This course uses **VS Code** (Visual Studio Code), a free code editor from Microsoft that runs on Windows, macOS, and Linux. A code editor is a text editor with help built in for programmers. VS Code colors your markup so mistakes stand out, suggests tag names while you type, and can preview files. It is one of the most widely used editors in the industry, so the muscle memory you build here transfers to any team.

Download the installer from [code.visualstudio.com](https://code.visualstudio.com/), run it, and accept the defaults. When VS Code opens, you are looking at the same class of tool professionals use all day.

### Files, Folders, and Names

Websites are made of files, so tidy file habits are part of the craft. Two habits start now.

First, keep every course file inside one project folder. You already have it: the course data pack you downloaded from Canvas extracts to a folder named `cis133`. Save all of your work inside that folder, so your files and the provided files travel together. In VS Code, choose File, then Open Folder, and open `cis133` once. The Explorer panel then shows everything in the folder, and you can create and edit files without leaving the editor.

Second, name files the way the web expects. The safe pattern is all lowercase, no spaces, with hyphens between words: `about-us.html`, `recycling-guide.html`. A space in a file name turns into `%20` when it becomes part of a URL, and some servers treat `About.html` and `about.html` as two different files. The **file extension**, the ending after the dot, tells your computer and your browser what kind of file it is. `.html` marks a web page, and `.txt` marks plain notes.

### The Edit-Save-Refresh Cycle

Here is the loop you will run thousands of times in this course:

1. Edit the file in VS Code.
2. Save it (Ctrl+S on Windows, Cmd+S on Mac).
3. View it in the browser. The first time, open the file by double-clicking it, or drag it onto a browser window. After that, refresh the tab to load your newest save.

Look at the address bar after you open a local file. Instead of `https://`, the address starts with `file://`. Connect that to Chapter 1: no request crossed the Internet, and no server was involved. The browser, your usual client, read the file straight off your disk. In Chapter 12 you will move these same files to a web server, and the address will earn its `https://`. Until then, `file://` is your private workshop.

One warning about step 2: an unsaved edit does not exist yet as far as the browser is concerned. If you refresh and nothing changes, check VS Code's file tab first. A dot on the tab means unsaved changes.

### Try It Yourself 2.1: Text Without Markup 🛠️

**Predict:** Create a file with two short sentences separated by a blank line, and no markup at all. When a browser opens it as a web page, will you see two paragraphs, one paragraph, or an error?

**Run:** In VS Code, create a new file in your `cis133` folder named `two-lines.html`. Type one short sentence, press Enter twice, and type a second sentence. Save the file and open it in your browser.

**Explain:** In 1-2 sentences, describe what happened to your blank line and what that tells you about how browsers treat spacing in a file. Keep this file. Section 2.3 explains the behavior, and the fix.

### Quick Check 2.1 ✅

1. A classmate writes a page in Google Docs and renames the file `page.html`. It looks wrong in every browser. Using this section's terms, explain the mistake.
2. Which of these file names will cause trouble in a URL, and why: `Club Page.html`, `club-page.html`?
3. You open your page and the address bar reads `file:///Users/maria/cis133/two-lines.html`. Using Chapter 1's client and server roles, explain who delivered this page.

---

## 2.2 Anatomy of an HTML Document

Your `two-lines.html` experiment proved that a browser ignores your typing habits. It needs structure spelled out in its own notation. That notation is the markup in HyperText Markup Language, and its unit is the element.

### Elements, Tags, and Attributes

An **element** is one piece of page structure: a paragraph, a heading, a list. Most elements are written as a pair of tags with content between them. A **tag** is the markup itself: the element's name inside angle brackets. The opening tag starts the element, and the closing tag, which adds a forward slash, ends it.

```html
<p>Meetings pause during finals week.</p>
```

Read it in three parts:

* `<p>` is the opening tag. It says "a paragraph starts here."
* `Meetings pause during finals week.` is the content, the part visitors see.
* `</p>` is the closing tag. The slash says "the paragraph ends here."

A few elements carry no content at all. An **empty element** has a single tag and no closing tag, because there is nothing to wrap. You will meet two in this section: `<meta>` and the line break `<br>`.

Sometimes an element needs a setting attached. An **attribute** is a name and value pair written inside an opening tag that configures the element. The pattern is always `name="value"`.

```html
<html lang="en">
```

The `lang` attribute declares the page's language. Screen readers use it to pick the right pronunciation rules, and search engines use it to match pages to searchers. One attribute, two audiences served. Attributes do most of the web's configuration work, and Section 2.4 introduces the one you will type most often.

### The Required Skeleton

Every HTML document you will ever write starts from the same skeleton. Here it is, followed by the complete first page it becomes:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Study Log</title>
</head>
<body>
    <!-- CIS133 Chapter 2 practice page -->
    <h1>My Study Log</h1>
    <p>This page tracks what I learn in CIS133, one week at a time.</p>
</body>
</html>
```

Walk it line by line:

| Line | Job |
| ---- | --- |
| `<!DOCTYPE html>` | The **doctype declaration** tells the browser "this file uses modern HTML." It is a declaration, not an element, and it is always the first line. |
| `<html lang="en">` | The root element. Every other element lives inside it. |
| `<head>` | The **head** holds information about the page: things the browser needs that never paint on screen. |
| `<meta charset="UTF-8">` | Declares the character encoding. UTF-8 covers nearly every written language, so accented names and symbols display correctly. |
| `<title>` | The **title element** names the page. Its text appears in the browser tab, in bookmarks, and as the headline of a search result. Chapter 1's SEO section is why it matters. |
| `<body>` | The **body** holds everything that appears in the browser window. All of your visible content lives here. |
| `<!-- ... -->` | A note to humans that the browser skips. The Comments subsection below explains it fully. |

Notice what is missing: nothing in the head is visible on the page, and nothing visible lives outside the body. When something you typed refuses to appear, checking which side of that line it landed on is the first diagnosis to run.

### Nesting and Indentation

Elements live inside other elements: the paragraph sits inside the body, and the body sits inside the html element. That containment is called **nesting**, and it has one law: an element that opens inside another must close inside it too. First opened, last closed.

```html
<!-- Right: </strong> closes before the paragraph does -->
<p>Bring <strong>working chargers</strong> to the drive.</p>

<!-- Wrong: the tags cross, and the validator will object -->
<p>Bring <strong>working chargers</p></strong>
```

The `<strong>` element marks text as important, and browsers show it bold. Its partner `<em>` marks a stressed word, and browsers show it italic. Both get their full story in Chapter 3. Here `<strong>` demonstrates the law of nesting.

Indentation makes nesting visible to humans. Each level of containment steps in four spaces, which is why the skeleton's head and body contents sit indented. The browser does not care. The next person to read your file does, and in this course that person is your grader.

### Comments: Notes to Humans

The skeleton's body opened with a line the browser never displays. An **HTML comment** is a note wrapped in `<!--` and `-->` that browsers skip entirely.

```html
<!-- Skills Lab 2A - Maria Ortiz - 2026-08-25 -->
```

Comments are your documentation channel: name the file's purpose, author, and date at the top, and explain any decision a reader could not guess. The Skills Lab rubric grades documentation in every lab, and comments are how an HTML file carries it. One caution: visitors can read comments with View Page Source, the trick you learned in Chapter 1, so never put anything private in one.

### Try It Yourself 2.2: Your First Document 🛠️

**Predict:** In the skeleton above, the title element says `My Study Log` and the h1 says the same. If you change only the title's text and refresh, where will the change appear, and where will nothing change?

**Run:** Type the twelve-line page above into a new file named `study-log.html` in your `cis133` folder. Type it by hand this once, so every line passes through your fingers. Save it, open it in your browser, then change the title's text to something new, save, and refresh.

**Explain:** In 1-2 sentences, explain the result using the head and body's division of labor.

### Try It Yourself 2.3: Meet DevTools 🛠️

**Predict:** In Chapter 1 you used View Page Source to see the exact text a server sent. Browser DevTools shows the browser's live working copy instead. Predict one difference you might see between your file and that working copy.

**Run:** With `study-log.html` open in your browser, right-click your h1 heading and choose Inspect. A panel opens showing your document as a folding tree (Chrome and Edge call it Elements, and Firefox calls it Inspector. On Safari, enable the Develop menu first, as in Chapter 1). Click the small triangles to fold and unfold elements, and slide your mouse across the tree while watching the page above.

**Explain:** In 1-2 sentences, describe how DevTools presents your document differently from the flat file, and what the highlighting told you about which markup produced which pixels.

### Quick Check 2.2 ✅

1. In `<html lang="en">`, name which part is the element and which part is the attribute, and state one audience the attribute serves.
2. A new page shows its own file name in the browser tab, and a paragraph typed into the head refuses to appear on screen. Explain both symptoms with one sentence each.
3. Why does `<meta charset="UTF-8">` have no closing tag?

---

## 2.3 Headings, Paragraphs, and Lists

The skeleton stands, and its body is nearly empty. Time to structure some content. The elements in this section carry most of the text on the web, and each one answers the same question: what IS this content? Choosing by meaning, not by looks, is the discipline this section builds.

### Headings

HTML provides six heading levels, `<h1>` down to `<h6>`. They are the outline of your page. The `<h1>` is the page's one main title, `<h2>` marks each major section, and `<h3>` marks subsections inside an `<h2>`.

```html
<h1>Recycle Your Old Electronics</h1>
<h2>Why It Matters</h2>
<h2>What the Club Accepts</h2>
```

Two rules keep an outline honest. Use exactly one `<h1>` per page. And never skip levels on the way down: an `<h3>` belongs inside an `<h2>` section, not directly under the `<h1>`. This textbook follows the same rules, which is why every chapter has one title and numbered sections beneath it.

Here is the trap: each heading level has a default size, and beginners pick the level that looks right. Wrong instrument. Chapter 1 introduced screen readers, and heading levels are how their users move through a page: many jump from heading to heading and listen to the outline before reading anything. A page whose headings were chosen for size reads to them like a shuffled outline. Choose the level that states the content's rank, and leave size for CSS to fix in Chapter 5.

### Paragraphs and Whitespace

The `<p>` element wraps one paragraph of running text. Now for the mystery from Try It Yourself 2.1. Browsers apply **whitespace collapsing**: any run of spaces, tabs, and line breaks in your file renders as a single space. Your blank line vanished because the browser collapsed it.

```html
<p>This    text has
odd     spacing in the file.</p>
<!-- The browser renders: This text has odd spacing in the file. -->
```

This is liberating, not annoying. You may break and indent your markup however readability demands, because only markup creates structure on screen. Two paragraphs exist when two `<p>` elements exist.

For the rare spot where a line break IS the content, use the empty element `<br>`: the line turns in a street address or a poem. Do not use `<br>` to push paragraphs apart. Spacing between elements is presentation, and CSS owns it (Chapter 5).

```html
<p>PC Computer Club<br>
1202 W Thomas Rd<br>
Phoenix, AZ 85013</p>
```

### Lists

Whenever content is a series, mark it as a list. HTML gives you two kinds, and the choice carries meaning. An **ordered list** (`<ol>`) numbers its items because their sequence matters. An **unordered list** (`<ul>`) bullets its items because it is a collection in no particular order. Both hold the same children: one `<li>`, or list item, per entry.

Ask one question to choose: if I shuffled these items, would the content break? Steps break when shuffled, so they are ordered. A supply list survives shuffling, so it is unordered.

```html
<h2>Prepare Your Device</h2>
<ol>
    <li>Back up your files.</li>
    <li>Sign out, then factory reset.</li>
    <li>Remove any SIM or memory card.</li>
</ol>
```

A list can nest inside another list, and the placement follows the law of nesting: the inner list lives inside an `<li>` of the outer list, right after that item's text.

```html
<ul>
    <li>Phones and tablets</li>
    <li>Computers and accessories
        <ul>
            <li>Laptops</li>
            <li>Keyboards and mice</li>
        </ul>
    </li>
    <li>Cables and chargers</li>
</ul>
```

The browser indents the inner list and switches its bullet style, no extra work required.

One more pair rounds out this section's toolkit. A heading, a paragraph, or a list is a **block-level element**: it begins on a new line and claims the page's full width, stacking like a brick. An element that flows along inside a line of text, like `<strong>` or this section's `<br>`, is an **inline element**. The distinction returns in Chapter 3's semantics and again when CSS starts controlling layout.

### Try It Yourself 2.4: The Meaning Test 🛠️

**Predict:** Take the three device-prep steps above and mark them as a `<ul>` instead of an `<ol>`. Will the browser show an error, renumber them, or render them happily as bullets?

**Run:** Add both versions to `study-log.html`, the steps as an `<ol>` and the same steps as a `<ul>`. Save and refresh.

**Explain:** The browser accepted both. In 1-2 sentences, explain which version is wrong anyway, and who gets misled when steps carry no numbers.

### Quick Check 2.3 ✅

1. A teammate marks a page's section titles with `<h4>` everywhere because the size looked right. Name the two audiences from this chapter that choice harms, and what each one loses.
2. Classify each of these as block-level or inline, and name the on-screen behavior that gives it away: `<h2>`, `<strong>`, `<p>`, `<br>`.
3. In the nested list example above, why does the inner `</ul>` come before `</li>` instead of after it?

---

## 2.4 Links, Attributes in Action, and the Validator

A page with no links is a dead end, and Chapter 1 defined the web as linked pages. This section wires your pages into that web, then holds your markup to the standard the web agreed on.

### The Anchor Element

A **hyperlink** (or link, for short) is text or another element a visitor activates to jump somewhere else. The anchor element `<a>` creates one, and its `href` attribute holds the destination address. The content between the tags becomes the clickable text.

```html
<p>Read the
<a href="https://www.epa.gov/recycle/electronics-donation-and-recycling">EPA
guide to electronics donation and recycling</a> before tossing anything.</p>
```

There is the attribute pattern from Section 2.2 doing the web's most important job. Without an `href`, an anchor goes nowhere. With it, your page joins the web.

### Absolute and Relative Addresses

The `href` accepts two forms of address, and choosing between them is a judgment you will make on every link.

An **absolute URL** is the complete address, the full form you dissected in Chapter 1: protocol, domain, and path. Use it to reach a page on someone else's site.

A **relative URL** gives directions from the current file instead: no protocol, no domain. Use it to reach your own site's files. A bare file name points to a file in the same folder, and a folder name with a slash steps down into a subfolder.

| You are linking to | Form to use | Example `href` |
| ------------------ | ----------- | -------------- |
| A page on another site | Absolute | `https://www.phoenix.gov` |
| Your page, same folder | Relative | `contact.html` |
| Your file, in a subfolder | Relative | `guides/setup.html` |

Why not write absolute addresses everywhere? Because your site moves. Right now your pages live at `file://` paths in your `cis133` folder. In Chapter 12 they move to a server. Relative links describe files in relation to each other, so they survive the move untouched. Absolute links to your own machine would break the moment the site leaves it.

One more `href` trick from Chapter 1's protocol family: begin the value with `mailto:` and a click opens the visitor's mail app with the address filled in. A **mailto link** is how a plain page offers one-click email.

```html
<a href="mailto:computer-club@example.org">Email the club</a>
```

### Link Text Is Content

The words inside the anchor matter as much as the address. Screen readers can list a page's links out of context, so every link must make sense alone. A list that reads "click here, click here, here" is a locked door. Meaningful link text also feeds search engines, which treat it as a description of the destination, a ranking signal you met in Chapter 1.

```html
<!-- Weak: says nothing on its own -->
<a href="recycling-guide.html">Click here</a> for the guide.

<!-- Strong: the link text names its destination -->
Read the <a href="recycling-guide.html">electronics recycling guide</a>.
```

### Valid Markup and the W3C Validator

Chapter 1 promised you a tool that checks your work, and here it is. **Valid markup** follows the rules of the HTML standard: required elements present, tags closed, nesting legal. Browsers do not enforce those rules. When markup breaks, a browser silently guesses at what you meant, and different browsers guess differently. Your page can look fine on your machine and fall apart on a visitor's, and you control your code, never their browser.

The referee is the **W3C validator** at [validator.w3.org](https://validator.w3.org/), a free checker run by the **W3C** (World Wide Web Consortium), the body that maintains the web's standards. Give it your page three ways: by address, by file upload, or by pasting your markup into Direct Input. For `file://` pages, upload or paste.

The validator answers with a report. Each message names the problem and points to a line and column in your file. Reading those reports is a skill, and two habits make it:

* Fix errors from the top of the report down, and revalidate after each fix.
* Expect cascades. One defect can generate several messages, because everything after the defect confuses the parser. Fix the first defect and the phantom messages below it disappear.

Here are the real messages the validator produces for a page whose eighth line reads `<p>Bring <em>working chargers to the drive.</p>`, with the closing `</em>` tag missing:

```text
Error: End tag "p" seen, but there were open elements.
From line 8, column 48; to line 8, column 51

Error: Unclosed element "em".
From line 8, column 14; to line 8, column 17

Error: End tag for "body" seen, but there were unclosed elements.
From line 9, column 1; to line 9, column 7
```

One missing tag, three messages, and only the middle one names the defect. The last message blames line 9, a line with nothing wrong on it. That is why you fix top to bottom.

The validator checks grammar, not judgment. Your recipe steps marked as an unordered list sail through validation, wrong meaning and all. Try It Yourself 2.4 was a test no machine runs. Validation is the floor, and your element choices are the craft above it.

!!! tip
    Make validation a habit, not an event: validate every page before you call it done, the way you proofread an email before sending. Every Skills Lab in this course expects validated pages from here on.

### Try It Yourself 2.5: Break It on Purpose 🛠️

**Predict:** Delete the closing `</title>` tag from `study-log.html` and refresh the browser. What will you see: your page, an error message, or something stranger?

**Run:** Delete `</title>`, save, and refresh. Note what the browser shows and check the tab's text. Then paste the whole file into the validator's Direct Input tab and read the report. Finally, restore the tag, save, and validate again.

**Explain:** In 1-2 sentences, contrast how the browser handled the defect with how the validator handled it. Which one told you what was wrong?

### Quick Check 2.4 ✅

1. Your site's `index.html` needs two links: one to your own `contact.html` in the same folder, and one to the college's home page. Write the `href` value for each and name the address form you chose.
2. Rewrite this link so its text works for a screen reader user hearing it out of context: `<a href="drop-off.html">here</a>`.
3. A validator report shows six errors, but your classmate swears they only changed one line. Using this section's two report-reading habits, what do you advise before they start rewriting six spots?

---

## 2.5 Summary and Retrieval 💡

### Key Concepts

* Web pages are plain text files. You write them in a code editor (VS Code in this course), and you work in a loop: edit, save, refresh the browser. Files use lowercase, hyphenated names, and everything lives in one project folder.
* Every HTML document uses the same skeleton: the doctype declaration, then an `html` root holding a `head` (information about the page, including its title) and a `body` (everything visible). HTML comments document the file without appearing on the page.
* An element is a piece of page structure, usually an opening tag, content, and a closing tag. Attributes configure elements from inside the opening tag. Nested elements must close in reverse order of opening, and indentation makes that structure readable.
* Choose text elements by meaning. One `<h1>` and unskipped heading levels form the outline, and `<p>` wraps paragraphs (whitespace in the file collapses). `<ol>` numbers steps that must stay in order, and `<ul>` bullets collections that do not.
* The anchor element and its `href` attribute create links: absolute URLs reach other sites, relative URLs connect your own files and survive publishing, and link text must describe its destination. The W3C validator checks your markup against the standard. Fix reports top to bottom and expect one defect to cascade into several messages.

### Key Terms

See course glossary for full definitions

* plain text, text editor, VS Code, file extension (Section 2.1)
* element, tag, empty element, attribute, doctype declaration, head, title element, body, nesting, HTML comment (Section 2.2)
* whitespace collapsing, ordered list, unordered list, block-level element, inline element (Section 2.3)
* hyperlink, absolute URL, relative URL, mailto link, valid markup, W3C, W3C validator (Section 2.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Write the required document skeleton from memory: doctype, html, head with its two standard children, and body.
2. Explain the difference between an element and an attribute, with one example of each.
3. State the one question that decides between an ordered and an unordered list, and give one example on each side.
4. A link needs to reach another page in your own site. State which address form you use and why it will keep working after the site is published in Chapter 12.
5. Describe what the browser does with invalid markup, what the validator does with it, and why the difference makes validation a habit.

---

## 2.6 Skills Lab 2A: Build the Club's Recycling Guide

**Goal:** Build and validate the recycling guide page your Chapter 1 research approved, then repair the club's broken contact page and connect the two.

**Dataset:** Provided files in `assets/code/chapter-02/` from the course data pack: `recycling-guide-content.txt` (every piece of the page's text, labeled), `broken-contact.html` (the club's contact page, with planted markup errors), and `skills-lab-2a-answers.txt` (your written answers file). Work at the extracted `cis133` root. Copy text from the content file instead of retyping it: you type only the markup.

### Part 1: Foundation (Aligns with MLO-2.1)

1. Create a folder named `skills-lab-2a-lastname` at your `cis133` root, and copy `skills-lab-2a-answers.txt` into it.
2. In VS Code, create `recycling-guide.html` inside that folder. Write the full skeleton: doctype, `html` with a `lang` attribute, a head holding `<meta charset="UTF-8">` and the [BROWSER TAB TITLE] from the content file, and an empty body.
3. At the top of the body, add an HTML comment with the lab number, your name, and the date.
4. Add the [MAIN HEADING] and the two intro paragraphs from the content file. Save, open the page in your browser, and confirm all three appear.
5. Prove your edit-save-refresh cycle: change your title element's text, save, refresh, and watch the tab. Record your file's path in answer 1.A and what changed in answer 1.B.

### Part 2: Application (Aligns with MLO-2.2)

1. Mark up the rest of the content file in order. Each [SECTION HEADING] becomes a heading at the level your outline calls for, and each labeled paragraph becomes a `<p>`.
2. The content file labels one series where order matters and one where it does not. Choose the right list element for each, and nest the three indented accessory items as a list inside their parent item.
3. Add the two Learn More links using the provided link text and addresses, and finish the footer paragraph with its email link. Every link's text must make sense out of context.
4. Save, refresh, and read your page top to bottom against the content file. Then record your heading outline in answer 2.A.

### Part 3: Extension (Aligns with MLO-2.2, MLO-2.3)

1. Validate `recycling-guide.html` at [validator.w3.org](https://validator.w3.org/) using file upload or Direct Input. Fix anything it reports and revalidate until the report is clean.
2. Copy `broken-contact.html` from the data pack into your lab folder and rename the copy `contact.html`. Open it in your browser first and notice how normal it looks. Then validate it and read the full report.
3. Repair `contact.html` one defect at a time, working top to bottom and revalidating after each fix. Log every repair in the answers file's fix log: the exact message(s), the line numbers, the actual problem, and your fix. Stop when the report is clean.
4. Connect the pages with relative links. In the guide's footer, add the [PART 3 LINK TEXT] link to `contact.html`. On the contact page, add a link back to `recycling-guide.html` with link text you write yourself. Validate both pages one final time.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Your fix log has more validator messages than repairs. Citing one specific message from your log, explain how a single missing character produced messages on lines you never touched, and what that teaches you about the order in which to fix validator errors.
2. Your guide page uses one numbered list and one bulleted list, and its links use three kinds of address: absolute, relative, and mailto. Pick the numbered list and one link kind. For each, justify the choice by what the content means, and describe a change to the content that would flip your choice.

**Submission:** Zip your `skills-lab-2a-lastname` folder containing `recycling-guide.html`, `contact.html`, and `skills-lab-2a-answers.txt`, and submit it as `skills-lab-2a-lastname.zip`. Both pages must validate with zero errors, and every answer in the answers file must sit under its numbered prompt.

### Rubric: Skills Lab 2A

| Criteria | Mastery (4) | Proficiency (3) | Developing (2) | Emerging (1) | Not Evident (0) |
| --- | --- | --- | --- | --- | --- |
| **Code Accuracy and Efficiency** | Code is Accurate, Efficient, and ERROR-FREE. Demonstrates optimal use of HTML and CSS syntax and the course tools | Code is mostly accurate and efficient. MINOR ERRORS are present but do not significantly affect the output or performance | Code runs but contains SOME ERRORS or INEFFICIENCIES. The output is sometimes incorrect or incomplete | Code is FREQUENTLY INCORRECT or inefficient, with multiple errors that prevent the program from running | No Submission or Not Evident |
| **Output Quality** | EXCEPTIONAL outputs with outstanding clarity and detail. They effectively enhance understanding of the work | GOOD quality outputs that accurately represent the results. Well-labeled and clear | Outputs are ADEQUATE but lack sophistication or have minor errors in labeling or presentation | Outputs are POORLY CONSTRUCTED, unclear, or irrelevant. Labeling is missing or incorrect | No Submission or Not Evident |
| **Documentation and Code Comments** | COMPREHENSIVE and concise documentation and comments. They greatly enhance the readability and understanding of the code | CLEAR documentation and comments that aid in understanding the code's purpose and logic | SOME documentation and comments are present, but they lack clarity or are incomplete | MINIMAL or no documentation and comments. Code is difficult to follow | No Submission or Not Evident |
| **Analysis, Interpretation, and Response to QUESTION(s)** | COMPREHENSIVE and INSIGHTFUL analysis. Interpretations are precise and fully supported by compelling evidence. Answers to questions are thorough, demonstrating deep understanding and insight | SOLID analysis. Interpretations are logical, well-reasoned, and supported by evidence. Answers to questions demonstrate a good understanding of the material | BASIC analysis is conducted. Interpretations are present but lack depth or detail. Answers to questions are basic and show limited understanding | Analysis is MINIMAL or incorrect. Interpretations and conclusions are missing or irrelevant. Fails to adequately answer the questions asked in the assignment | No Submission or Not Evident |

**Scoring:** 16 points total (4 points per criterion)

---

## 2.7 Review Questions 🔄️

1. **Remember:** List the four structural parts every HTML document starts with, in order, and state one job of each.

2. **Understand:** A teammate says "I use whichever heading looks the right size, and I add blank lines in my file when I want space on the page." Explain what each habit misunderstands about how browsers read HTML.

3. **Apply:** The campus tutoring center's page needs four pieces of markup: its drop-in hours (a set of day and time entries), the three steps to book an appointment, and two links. One link reaches the campus map on the college's main website, and the other reaches the center's own `faq.html` in the same folder. Name the element or address form you would use for each of the four, with one reason apiece.

4. **Analyze:** A classmate's validator report shows `Error: Unclosed element "strong"` followed by `Error: End tag "p" seen, but there were open elements` and two more errors on later lines they never edited. Diagnose the likely single defect, explain why the extra messages appeared, and describe the order in which you would repair and revalidate.

---

## Further Reading 📖

* [MDN: Basic HTML syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax) - A beginner-level tour of elements, attributes, and the document skeleton, with live examples to edit.
* [MDN: HTML elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) - The complete catalog of every HTML element. Bookmark it now, because you will use it for the rest of the course.
* [The W3C Markup Validation Service](https://validator.w3.org/) - The validator itself. The About page explains what the checker looks for.
* [VS Code documentation](https://code.visualstudio.com/docs) - Setup guides and editing basics for the course editor, straight from its maker.
* [web.dev: Learn HTML](https://web.dev/learn/html) - Google's free HTML course. The early modules reinforce this chapter at a comfortable depth.

---

## Looking Ahead ⏩

You can now build a valid page: structured text, working links, and a clean validator report. Chapter 3 raises the standard from valid to meaningful. You will mark up pages with semantic elements that name each region's purpose, give `<strong>` and `<em>` their full story, and add images with alt text that serves every visitor, sighted or not. The club's pages you built this week are about to get their pictures.
