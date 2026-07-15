# Chapter 7: UX and Web Design

Skills Lab 6A sent the club's site out the door with its Part II milestone complete. Three pages share one stylesheet, the header lays its logo and title on a flex line, and the navigation bar answers the mouse and the keyboard alike. Notice the fact hiding inside that success: you never drew a plan. You never needed one. Three pages fit in one head, and every decision could wait until your cursor was already in the file.

That approach stops working the moment a site wants to grow, and the club's site wants to grow. This chapter's Skills Lab opens with a brief from the club's officers asking for more, and asking to see a plan before anyone writes markup. The request is standard practice, not caution. Professionals plan on paper first because the costs are lopsided. A sketch changes in minutes. Built pages change in hours, and the hours multiply across every page the change touches.

Chapter 7 opens Part III, Design for Every User, and it works differently than the chapters before it: more drawing than typing. You will turn goals and audiences into pages. You will separate user experience from user interface and measure both with five principles. You will draw sitemaps and wireframes, and discover that every box in them is something you already own. By the end you will assemble all of it into a site plan, the same document you can use to launch an independent project.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 1-6 (the full toolkit: semantic structure, CSS, the box model, and Flexbox)
* **Deliverables:** Skills Lab 7A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **7.1 (Analyze):** Differentiate user experience (UX) from user interface (UI) decisions, using the five UX principles: usability, accessibility, consistency, feedback, and responsiveness (Sections 7.1-7.2)
* **7.2 (Apply):** Construct a sitemap and wireframes that plan a multi-page site's structure and layout before any code is written (Section 7.3)
* **7.3 (Evaluate):** Critique an existing site's navigation and page consistency against UX principles to produce a site plan (Section 7.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO III (Analyze):** Compare and contrast various research information resources available on the Internet/WWW
* **CLO XII (Create):** Produce a multi-page website incorporating learned techniques

---

## 7.1 Plan Before You Code

Every chapter so far started at the keyboard, and for good reason: you had elements, rules, and tools to learn, and the club's site stayed small enough to design as you typed. Professional sites do not start there. They start with questions on paper, because of one lopsided piece of arithmetic. Changing a sketch costs minutes. Changing built pages costs hours, and the cost multiplies by the number of pages the change touches. Add one page to a three-page site and every page's navigation bar needs an edit. Discover after building that the pages themselves are the wrong pages, and the bill covers everything.

Planning does not require new software. It requires answers to three questions, in order: what the site must accomplish, who it serves, and what those people will do there. This section asks the questions. The rest of the chapter turns the answers into diagrams a developer can build from.

### What the Site Must Accomplish

Every site exists to accomplish something, and the something should be checkable. "So people know about us" is a wish: no one can tell when it comes true. "A first-time visitor can say what the group does after one screen" is a goal: you can sit someone in front of the page and check. Write two or three goals per site, each phrased as an outcome someone could test. A few rewrites show the shape:

| The wish | The checkable goal |
| --- | --- |
| "People should know about us" | A first-time visitor can say what the group does after one screen |
| "The site should look professional" | Every page passes both validators and keeps one consistent look |
| "Fewer repeat questions" | Our three most-asked questions are each answered within two clicks |

Goals also settle arguments later. When two page ideas compete for the top of the home page, the written goals decide which one earns it.

### Who the Site Serves

The second question names the visitors. A site's **target audience** is the people it is built to serve, described by what they already know, what they come to do, and what would make them leave. Most sites serve more than one audience, and the differences drive design. A visitor who already knows your organization wants current details fast. A visitor who has never heard of you needs the what-is-this answer before anything else. Professional teams sometimes press further and write personas, short fictional profiles of one typical visitor, complete with a name and a schedule. This course works at the audience level.

Knowing an audience is research, and you already own the habits. Chapter 1 taught you to interrogate sources: who wrote this, when, and why. Point the same discipline outward. Who will read this site, arriving from where, needing what? Talk to the people the site is for, read the questions they already ask, and treat every assumption about them as a claim that needs evidence.

### From Actions to Pages

The third question converts audiences into structure. For each audience, list the actions they should be able to take: read a guide, check a date, sign up, send a message. Actions that recur earn pages of their own, and the pages you name here become the sitemap you draw in Section 7.3. This is the step beginners skip. Skipping it produces sites organized around what the owner wants to say instead of what the visitor came to do.

The campus tutoring center you have been advising in review questions since Chapter 2 makes a clean worked example. Its goals: students find help hours fast, and new students book a first appointment. Two audiences fall out of those goals, and their actions name the pages:

| Audience | Comes to | Page that answers |
| --- | --- | --- |
| Regulars | check current hours, book a slot | Hours and Booking |
| First-timers | learn what help exists, in which subjects | Subjects |
| Both | pick up exam-week study advice | Study Tips |
| Both | find the room, ask a question | Contact |

Notice what the table is not. It is not a list of what the center's staff find interesting. Every row starts with a visitor, and every page must earn its place by answering one. Hold onto this table: Section 7.3 turns it into a diagram.

### Try It Yourself 7.1: Reverse-Engineer a Home Page 🛠️

**Predict:** Phoenix College's home page was planned by someone, and the plan shows. Before visiting, write two predictions: the audience the page serves first, and the single action the college most wants that visitor to take.

**Run:** Visit `https://www.phoenixcollege.edu` in your browser. Study the first screen before you scroll, then scroll once and note the two or three actions the page pushes hardest. Big buttons and banners are the tell.

**Explain:** In 1-2 sentences, state the page's primary goal as this section would write it: a checkable outcome, not a wish. Then say whether the pushed actions matched the audience you predicted.

### Quick Check 7.1 ✅

1. A classmate opens VS Code to start a five-page site with no plan, reasoning that sketches waste time when you already know the tools. Use this section's cost arithmetic to answer them in two sentences.
2. The campus food pantry wants a site "so people know we exist." Rewrite that wish as one checkable site goal, then name one visitor action the site should invite.
3. An intramural soccer league's site serves current players and students thinking about joining. Name one thing each audience comes to do, and the page each action earns.

---

## 7.2 UX, UI, and the Five Principles

Planning needs a vocabulary for quality, because "make it good" plans nothing. Two terms sort every design conversation you will ever sit in. **User experience (UX)** is the quality of a visitor's whole visit: whether they find what they came for, how much guesswork it takes, and whether they would come back. **User interface (UI)** is the set of controls and visuals a visitor operates: the buttons, links, menus, and forms, and how each one looks. The two are easy to confuse and worth separating. A button with rounded corners in a pleasing teal is UI. Whether a visitor can find that button, and whether it visibly answers the press, is UX. A beautiful interface can still deliver a miserable visit, which is how a site can win a design award and lose its visitors.

Hold the relationship straight and the rest follows: UI serves UX. Every interface choice either serves the visitor's experience or gets in its way.

On large teams, UX is a job title: researchers who interview visitors and designers who shape each page's path. On a team of one, which is what this course's labs make you, the developer wears the hat. The five principles below are how you wear it well.

### The Five Principles

This course measures UX with five principles. None of them is new to you. Each one names something you have been building since Part I.

* **Usability.** Visitors can complete their tasks without instructions or guesswork. A usable page answers "what do I do next" before the visitor has to ask it.
* **Accessibility.** The site works for every visitor, including people who rely on screen readers, keyboards, or other assistive tools. You have built for this since Chapter 3: honest alt text and landmarks Devon's screen reader jumps by. Chapter 6 added focus outlines no rule removes. Chapter 9 walks the full standards framework behind the habit.
* **Consistency.** The same things look and behave the same way on every page, so nothing has to be relearned. You engineered this in Chapter 4 without the name. One external stylesheet dressing every page IS consistency, enforced by a file. The navigation bar you shipped on all three pages in Lab 6A is the same principle in markup.
* **Feedback.** The site answers every visitor action with a visible response. Your `:hover` and `:focus` states are this principle at work. The link that lights under the pointer, and lights again for the Tab key, tells the visitor the page heard them.
* **Responsiveness.** The layout adapts to the visitor's screen instead of demanding one screen size. `flex-wrap` bought half of this in Chapter 6, when full rows learned to break instead of squeeze. Chapter 8 buys the other half.

Say the five as questions and they become an audit. Can visitors finish their tasks? Can every visitor? Does anything change between pages without a reason? Does the page answer every action? Does the layout survive a narrow window? Section 7.4 folds these questions into the site plan, and the lab hands you a worksheet built from them.

### Sorting Decisions into Layers

Here is Objective 7.1's skill in one move. When a design decision lands on your desk, ask two questions: which layer is it, and which principle is at stake? A few decisions, sorted:

| Decision | Layer | Principle at stake |
| --- | --- | --- |
| The navigation bar keeps one label order on every page | UX | consistency |
| A link inverts its colors under the pointer and the Tab key | UI | feedback |
| The gallery row wraps on a narrow window instead of squeezing | UX | responsiveness |
| Meeting times sit one click away from every page | UX | usability |
| Every page's headings render in the same Oswald stack | UI | consistency |

Read the middle column and the pattern shows: UI rows pick the paint, and UX rows shape the visit. Both matter. The principle column is what connects them, because a UI choice earns its place by serving a principle. The inverted link colors are paint, chosen so the feedback is visible.

The principles also argue with each other, and sorting helps there too. Suppose a clubmate proposes a navigation bar that hides itself until the pointer reaches the top of the window. The screen gains room, which is a usability point on small displays. But the bar stops being findable, keyboard visitors may never summon it, and no other page on the site behaves that way. One UI idea picked fights with usability, accessibility, and consistency at once. Design is deciding which principle wins, on purpose, and writing the decision down.

### Try It Yourself 7.2: A Field Audit in Five Principles 🛠️

**Predict:** You counted a Wikipedia article's landmarks in Chapter 3, and now you can judge them. A long article shows a contents sidebar listing its sections. Predict which of the five principles that sidebar serves most directly. Then predict what pressing Tab will show: will you always know which link holds the focus?

**Run:** Open `https://en.wikipedia.org/wiki/Recycling`. Use the contents sidebar to jump to one section deep in the article. Put the mouse away and press Tab a dozen times, watching for a visible signal at every stop. Then open any other article and compare the two pages, region by region.

**Explain:** In 1-2 sentences, name the principle the sidebar serves and the principle your Tab test measured, and report one strength or gap you observed for each.

### Quick Check 7.2 ✅

1. Two decisions arrive for review: (a) the site's search box sits in the same corner of every page, and (b) the search button shows a magnifying glass icon in the site's brand color. Sort each into UX or UI and name the principle at stake.
2. A site's links change color under the pointer and give nothing to the Tab key. Which principle is only half-served, and which visitors pay for the missing half?
3. A clubmate calls accessibility "the Chapter 9 topic." Correct the timeline: name two techniques from earlier chapters that already serve that principle.

---

## 7.3 Sitemaps and Wireframes

With goals, audiences, and principles in hand, you can draw the plan itself. Two diagrams carry it, and both fit on paper. The first decides what pages exist. The second decides what each page holds. Neither one uses color, and that restraint is deliberate.

### The Sitemap: Structure on One Page

A **sitemap** is a diagram of a site's structure: every page, branching from the home page, with connections showing how the pages relate. Section 7.1 already turned the tutoring center's audiences into pages. The sitemap arranges those pages into a tree and records how they connect:

```text
Home (index.html)
 +-- Subjects (subjects.html)
 +-- Hours and Booking (hours.html)
 |    +-- FAQ (faq.html)
 +-- Study Tips (study-tips.html)
 +-- Contact (contact.html)
```

Read the tree from the top. Every sitemap starts at Home, and Chapter 3 already banked the file name for it: `index.html`, the page a web server serves by default. The four pages one step below Home sit at the top level, and each of those earns a label in the navigation bar. The FAQ sits one step deeper. Its questions belong to the hours-and-booking conversation, so that page links to it and the navigation bar does not. That placement is a real decision, and the diagram records it.

Two working rules keep sitemaps honest. First, a page that is not in the tree does not exist, so name every page now, with its file name. Second, keep a site this size shallow: every page within two clicks of Home. Depth hides content, and hidden content fails the usability principle before any code runs.

One misreading is worth heading off. The tree records structure, not every link. Pages still cross-link freely, so the study-tips page can link to booking wherever it helps. The tree answers a narrower pair of questions: where does each page live, and which pages earn a place in the bar?

### The Wireframe: Layout Without Paint

A **wireframe** is a grayscale sketch of one page's layout: labeled boxes for each region, and nothing else. No colors, no fonts, no finished text. The restraint is the point. A wireframe review should argue about structure, meaning what sits where and what a visitor sees first. Gray boxes keep the argument there. Show a full-color mockup instead, and the meeting spends its hour debating the shade of teal.

Here is the tutoring center's home page at desktop width:

```text
+---------------------------------------------------------------+
| header                                                        |
|  +--------+  +---------------------------------------------+  |
|  |  logo  |  | site title                                  |  |
|  +--------+  +---------------------------------------------+  |
+---------------------------------------------------------------+
| nav                                                           |
|  [ Subjects ] [ Hours and Booking ] [ Study Tips ] [ Contact ]|
+---------------------------------------------------------------+
| main                                                          |
|  +---------------------------------------------------------+  |
|  | h1: page heading                                        |  |
|  +---------------------------------------------------------+  |
|  +----------------+  +----------------+  +----------------+   |
|  | Math card      |  | Writing card   |  | Science card   |   |
|  +----------------+  +----------------+  +----------------+   |
|  +---------------------------------------------------------+  |
|  | sign-up banner (this page only)                         |  |
|  +---------------------------------------------------------+  |
+---------------------------------------------------------------+
| footer                                                        |
|  drop-in hours line and campus map link                       |
+---------------------------------------------------------------+
```

The boxes carry content notes, not content. "Math card" stands for whatever that card will say, and the wireframe only promises the card a place. Draw frames on paper, on a whiteboard, or in plain keyboard characters like these. The tool does not matter. The decisions do, and a working recipe keeps them coming fast:

1. Draw the outer boxes first, top to bottom: header, nav, main, footer.
2. Split `main` into content regions, one box per job the page does.
3. Pull side by side whatever belongs on one line, and mark each such row as a flex line.
4. Label every box: landmarks by element name, content boxes by a short note.
5. Stop. Detail belongs to the page, and paint belongs to the stylesheet.

!!! tip
    Ugly wireframes work. A frame that took five minutes invites correction ("move that row up"), while a polished one invites politeness. Speed is a feature: sketch three layouts and argue about them, instead of perfecting one.

### Every Box Is Something You Already Own

Chapter 6 closed with a promise: you can build any layout you can sketch, once you learn to sketch deliberately. Here is the payment. Read the wireframe's labels again. Every outer box is a landmark you have written since Chapter 3, and every row of side-by-side boxes is a flex line you built in Chapter 6:

```text
wireframe box            what you already own
-------------            ----------------------------------------
header                   <header> holding the logo and site title
nav                      <nav> holding the list of links
h1: page heading         <h1> at the top of <main>
row of three cards       a flex container and its three cards
sign-up banner           a <section> with an id, styled once
footer                   <footer> holding the closing links
```

The markup skeleton falls straight out of the sketch:

```html
<!-- The wireframe's outer boxes, top to bottom. Every label is
     an element you have written since Chapter 3. -->
<header>the logo and the site title</header>
<nav>the navigation bar's links</nav>
<main>
    <h1>the page heading</h1>
    <section class="subject-cards">the three cards</section>
</main>
<footer>the hours line and the campus map link</footer>
```

And the sketch demands exactly one layout rule:

```css
/* The only layout the sketch asks for: the card row. Boxes
   that stack are normal flow and need no rule at all. */
.subject-cards {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
}
```

That is the whole translation. A wireframe is not a drawing of some future skill. It is a drawing of your current one.

The translation runs the other direction too. A wireframe is a document a stakeholder can read. The people a site belongs to may never read a stylesheet, but anyone can point at a box and say "swap these two." That is why plans travel as sketches, and why this chapter's deliverable is a document instead of a folder of code.

### The Same Page at Phone Width

Plan every page at two widths, because phones are not an edge case. They are how a large share of your visitors will meet the site. The same home page, sketched narrow:

```text
+---------------------------+
| header                    |
|  logo, site title         |
+---------------------------+
| nav                       |
|  [ Subjects ]             |
|  [ Hours and Booking ]    |
|  [ Study Tips ]           |
|  [ Contact ]              |
+---------------------------+
| main                      |
|  +---------------------+  |
|  | h1: page heading    |  |
|  +---------------------+  |
|  +---------------------+  |
|  | Math card           |  |
|  +---------------------+  |
|  +---------------------+  |
|  | Writing card        |  |
|  +---------------------+  |
|  +---------------------+  |
|  | Science card        |  |
|  +---------------------+  |
|  +---------------------+  |
|  | sign-up banner      |  |
|  +---------------------+  |
+---------------------------+
| footer                    |
|  hours and map link       |
+---------------------------+
```

Compare the two frames. The card row becomes a stack, the navigation labels break onto new lines, and every region narrows. Read those changes with Chapter 6 eyes and one is already yours: rows that break are `flex-wrap`. The rest of the phone frame's promises (regions that rearrange only below a chosen width, type that adjusts) need a tool you do not own yet. Chapter 8's media queries keep exactly this sketch's promises. Draw the phone frame anyway. The plan should not shrink to fit the tools you have.

One artifact exists past the wireframe, and you should recognize its name. A **prototype** is a clickable mockup: wireframes wired together so a test visitor can tap through them before any code exists, usually in a design tool such as Figma. Teams building large sites prototype before they build. This course's sites plan fine on paper and in text frames, so prototypes stay a term you can recognize, not a deliverable you owe.

### Try It Yourself 7.3: A Sitemap from a Navigation Bar 🛠️

**Predict:** Open `https://developer.mozilla.org` and read the top navigation bar's labels without clicking anything. From the labels alone, sketch the sitemap tree you expect: one branch per label, with one or two guessed pages under each.

**Run:** Open the Learn label and one more of your choice, and compare what sits behind each against the branch you guessed for it.

**Explain:** In 1-2 sentences, judge the labels as predictions: which one earned its branch, and which one led somewhere your tree did not expect?

### Try It Yourself 7.4: Wireframe a Page You Did Not Build 🛠️

**Predict:** Return to the article page from TIY 7.2, this time for its layout. Before drawing, predict two counts: how many outer regions the page stacks from top to bottom, and how many boxes sit side by side at laptop width.

**Run:** Draw the article page as a wireframe: boxes and labels only, on paper or in keyboard characters. Label every box you can with the landmark element it would be, and mark each side-by-side row as a flex line.

**Explain:** In 1-2 sentences, name the boxes that mapped cleanly onto landmarks you own, and the one box that resisted a label.

### Quick Check 7.3 ✅

1. State what a sitemap decides and what a wireframe decides, and name one decision neither diagram is allowed to make.
2. A teammate's wireframe arrives in full color with chosen fonts, and the review meeting spends its hour debating the palette. What did the grayscale rule exist to prevent, and where do the color decisions belong instead?
3. A wireframe for a soccer league's site shows the footer holding four sponsor logos on one shared row. Name what the footer becomes in CSS terms the moment you build that row, and write the declaration that starts it.

---

## 7.4 Navigation Design and the Site Plan

The sitemap decided what pages exist. Navigation design decides how visitors move among them, and it is where UX principles meet markup you have owned since Chapter 3. It is also where this chapter's deliverable comes together: the plan document a stakeholder can approve.

### Labels a Visitor Can Predict

A **navigation label** is the visible text of a navigation bar link, and it lives under the law Chapter 3 gave all link text: descriptive, meaningful out of context, never "Click Here". A good label lets a visitor predict the page behind it before clicking. "Hours and Booking" passes, because the visitor knows what arrives next. "Info" fails, because info about what? Test every label the same way: could a first-time visitor say what the page holds from the label alone?

| Label | Verdict | Why |
| --- | --- | --- |
| Recycling Guide | pass | Names the content: a guide, about recycling |
| Resources | borderline | Promises a page exists without saying what it holds |
| Learn More | fail | More about what? The label only works mid-sentence |

The club's own bar passes this test today. Recycling Guide, Spring Drive Gallery, and Contact the Club each name their destination, which is one reason the site's three pages have needed no instructions.

The bar itself follows two more conventions. It keeps the same labels, in the same order, in the same place on every page, which is the consistency principle doing quiet work. And every page should answer "where am I now": the page's `h1` and its `title` carry that answer today, and many sites also mark the current page's label in the bar. On the tutoring center's plan, the hours page would answer with an `h1` of Hours and Booking, the Chapter 2 pairing doing navigation work. Deep sites add breadcrumbs, a trail of links tracing the path from the home page to the current one. Your sites run two levels deep, so a clear bar and honest headings cover the question.

!!! note
    Navigation conventions are boring on purpose. Visitors arrive carrying habits learned from every other site they use, and meeting those habits is free usability. Spend creativity on content, not on reinventing where the bar goes.

### Where Eyes Go First

Layout has one more audience fact worth planning around. Readers of left-to-right languages scan pages in rough patterns: an F shape down text-heavy pages (a full sweep across the top, then shorter sweeps below) and a Z across sparser ones. The patterns are averages, not laws. The habit they support is safe everywhere: put what matters most where eyes land first, at the top and along the left, and never bury a page's purpose below decoration.

### Consistency Across Pages, on Purpose

Look at what the club's site already does right. Every page shares the same header, the same navigation bar, the same footer, and the one stylesheet behind them all. A visitor who learns one page has learned all three. None of that happened by luck. It happened because one file owns the look and every page loads it. A site plan writes such rules down as promises: the shared regions, the one stylesheet, whatever must never vary from page to page. Breaking a written rule later is still allowed. It becomes a design decision that needs a reason, instead of an accident nobody catches.

### Test the Plan on a Person

Plans get one more quality gate, and it costs ten minutes. Before anything gets built, show the sitemap and wireframes to someone who did not make them. Hand them a task ("find out when you could get math help") and watch where their finger lands. Count the guesses. Every hesitation marks a label or a placement to fix while fixing still costs minutes. The industry runs this practice formally as usability testing, with scripts, recordings, and participant counts. One patient friend buys you the course-sized version.

### The Site Plan

Assemble everything this chapter built and you hold the deliverable. A **site plan** is the planning document a site is built from, and yours carries six sections. Each one answers a question no one should answer at the keyboard:

| Plan section | The question it answers |
| --- | --- |
| Site goals | What must this site accomplish, checkably? |
| Target audience | Who is it for, and what do they come to do? |
| Sitemap | What pages exist, and how do they connect? |
| Wireframes | What does each page hold, at each width? |
| Navigation plan | Do the labels predict their pages? |
| Consistency rules | What must never vary from page to page? |

In one document, the plan does two jobs. It is the builder's blueprint, specific enough to start coding from. And it is the stakeholder's approval device: the people the site belongs to can read it, push back, and sign off before code costs anyone anything.

### Independent Project Milestone 1: Site Plan

If your course includes an independent multi-page project, use this chapter's process to plan it. Your topic, audience, sitemap, wireframes, navigation plan, and consistency rules belong in one site plan. Your instructor can assign that milestone wherever it fits the course calendar without changing this chapter.

Choose the topic with the remaining chapters in mind. It needs enough content for several pages, an audience you can name, and at least one person you can hand the plan to for the ten-minute test. A club you belong to, a hobby you can teach, or a cause you can document all carry that weight.

### Try It Yourself 7.5: The Label Audit 🛠️

**Predict:** WebAIM (`https://webaim.org`) teaches web accessibility, and its navigation bar holds five one-word labels. Read the five labels without clicking, and write one line per label predicting the page behind it.

**Run:** Click through all five labels, one at a time. Grade each label pass or fail: pass means the page matches what a first-time visitor would predict from the label alone.

**Explain:** In 1-2 sentences, name the label that earned its pass most clearly and the one you would rewrite, with the label text you would ship instead.

### Quick Check 7.4 ✅

1. A food truck's navigation bar reads Home, Info, Stuff, Click Here. The truck posts its menu, its weekly locations, and a catering request page. Grade the last three labels against this section's law and rewrite each one.
2. A visitor lands on an inner page straight from a search result. Name two signals the page can give so the visitor knows where they are, using only techniques this book has taught.
3. The site plan's last section writes down consistency rules everyone already intends to follow. Using this section's language, what does writing them down buy?

---

## 7.5 Summary and Retrieval 💡

### Key Concepts

* Plans precede code because the costs are lopsided: a sketch changes in minutes, and built pages change in hours that multiply across pages. Three questions start every plan: what the site must accomplish (checkable goals), who it serves (target audiences), and what those visitors will do (actions that become pages).
* UX is the quality of the whole visit. UI is the controls and their look, and UI serves UX. Five principles measure the experience: usability, accessibility, consistency, feedback, and responsiveness. Each one names work you have shipped since Part I, from alt text to `:focus` twins to `flex-wrap`.
* A sitemap decides what pages exist and how they connect: a tree branching from Home (`index.html`), every page named, nothing deeper than two clicks. A wireframe decides one page's layout as labeled grayscale boxes, drawn at desktop and phone width. Neither diagram picks colors or fonts. Those wait for the stylesheet.
* Every wireframe box is a landmark you own, and every side-by-side row is a flex line. The phone frame's remaining promises wait for Chapter 8's media queries.
* Navigation labels obey the link-text law: a visitor should predict the page behind a label before clicking. The bar keeps one order and one place on every page, and the plan's consistency rules turn those habits into written promises.
* The site plan assembles six sections into one stakeholder-ready document: goals, target audience, sitemap, wireframes, navigation plan, and consistency rules. Independent Project Milestone 1 uses the same template to plan your own site.

### Key Terms

See course glossary for full definitions

* target audience (Section 7.1)
* user experience (UX), user interface (UI), usability, accessibility, consistency, feedback, responsiveness (Section 7.2)
* sitemap, wireframe, prototype (Section 7.3)
* navigation label, site plan (Section 7.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the five UX principles, and pair each with one technique from Chapters 3-6 that already serves it.
2. List the six sections of a site plan in order, and state in one line what question each section answers.
3. Explain what a sitemap decides that a wireframe cannot, and what a wireframe decides that a sitemap cannot.
4. Recite the label law for navigation bars, and name the test every label must pass before it ships.
5. Describe what changes between a desktop wireframe and its phone twin, and name the one change you can already build with Chapter 6 tools.

---

## 7.6 Skills Lab 7A: The Club Site Grows Up

**Goal:** Produce a stakeholder-ready site plan that grows the club's three-page site into the six-page site its officers asked for.

**Dataset:** Provided files in `assets/code/chapter-07/` from the course data pack. This lab ships planning artifacts instead of starter code. `project-brief.txt` is the expansion brief from the club's officers and the lab's founding document. `club-site/` holds the club's finished site exactly as Skills Lab 6A leaves it (three pages, `club-styles.css`, and the `images` folder), and it is the shared audit target, documented in the folder's README. `ux-audit-worksheet.txt` turns the five principles into an audit instrument. `site-plan-template.txt` is the plan document's skeleton, and the same template supports Independent Project Milestone 1. `wireframe-examples.txt` holds copy-and-adapt text frames at both widths. `skills-lab-7a-answers.txt` is your written answers file. Work at the extracted `cis133` root, and leave `club-site/` unedited: it returns as Chapter 8's starter site.

The lab walks the chapter's own path. Part 1 digests the brief and audits the site you just finished building. Part 2 draws the structure and the layouts. Part 3 assembles the stakeholder document and closes with the judgment call no template can make for you.

### Part 1: Foundation (Aligns with Objectives 7.1 and 7.3)

1. Create a folder named `skills-lab-7a-lastname` at your `cis133` root, and copy `skills-lab-7a-answers.txt` and `ux-audit-worksheet.txt` into it. Read `project-brief.txt` twice: once straight through, once with a pen. Restate the club's goals and its two audiences in your own words in answer 1.A. The officers' sentences are off limits. Prove you understood them.
2. Audit the provided club site against the five principles. Open the three `club-site/` pages in your browser and the stylesheet in VS Code, then work through the worksheet principle by principle. Follow each what-to-check prompt, and log at least one strength and one gap wherever they exist. Point at pages and regions, not feelings. Everyone audits this shared copy instead of their own Lab 6A build, so every student critiques the same site.
3. Complete the worksheet's headline finding: the one gap you would fix first, and why it costs the site's visitors the most. Then summarize the audit in answer 1.B: your strongest strength and costliest gap, each tied to its principle, and who feels each one most.

### Part 2: Application (Aligns with Objective 7.2)

1. Construct the six-page sitemap: the three pages the brief keeps plus the three it adds. Draw it as a text tree with a file name beside each page title. Decide which pages sit in the navigation bar, then record the tree, your nav decisions, and a defense of anything you left out of the bar in answer 2.A.
2. Wireframe the new home page at desktop width and at phone width. Copy and adapt the frames in `wireframe-examples.txt`, or sketch on paper and photograph the result. Label every outer box with the landmark element it will become. No colors, no fonts.
3. Wireframe one more page of your choice from the tree, at both widths. Then record your frame inventory in answer 2.B: where the wireframes live, the page and width each frame shows, and the landmark labels each one carries.

### Part 3: Extension (Aligns with Objectives 7.2 and 7.3)

1. Write the navigation plan: the bar's labels in order, each defended in one line as a descriptive label (what it leads to, and why a visitor would predict that before clicking). Record the labels and defenses in answer 3.A.
2. Write the consistency rules every page will follow: the shared regions, the one stylesheet, and anything else that must never vary. Remember the officers' closing constraint. The colors and the logo stay, and the new pages must match.
3. Assemble the full site plan from `site-plan-template.txt`, addressed to the club's officers, with every section complete. Then close with the self-critique in answer 3.B: the two biggest UX risks in your own plan, and the one-user test you would run for each risk before building anything.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. The site you audited in Part 1 validates with zero messages, and every color pairing on it comes off the palette's passing list. Your worksheet still filled with findings. What does that gap prove about the difference between valid code and good UX? Citing two of your own findings, state where along the five principles a validator's help runs out.
2. Choose one of the five principles and trace it from plan to build. Point to the section of your site plan that serves it. Name the HTML or CSS technique you already own that will implement it, with the chapter that taught it. Then name one part of the plan that must wait for a tool a later chapter teaches.

**Submission:** Zip your `skills-lab-7a-lastname` folder containing your completed audit worksheet, your site plan document, your wireframes (text frames or photographed sketches), and `skills-lab-7a-answers.txt`, and submit it as `skills-lab-7a-lastname.zip`. Every answer sits under its numbered prompt, and your site plan must complete all six template sections.

### Rubric: Skills Lab 7A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s). Your instructor sets
the point weights in your course. The criteria and levels are the
same everywhere.

---

## 7.7 Review Questions 🔄️

1. **Remember:** List the five UX principles and state, in one line each, what each principle promises a visitor.

2. **Understand:** Explain the difference between user experience and user interface using a single button as the example, then explain how a UI decision can serve a UX principle.

3. **Apply:** The campus food pantry needs a four-page site: what the pantry does, a current-needs list, drop-off details, and contact. Construct its sitemap as a text tree with a file name beside each page, then list the navigation bar's labels in the order you would ship them.

4. **Evaluate:** A local restaurant's site shows four traits. The menu exists only as a photographed PDF. The navigation labels differ from page to page. Links respond to the pointer but not to the Tab key, and the layout demands a 1200-pixel window. Match each trait to the principle it breaks, then rank the two you would fix first for a visitor on a phone, defending your ranking.

---

## Further Reading 📖

* [NN/g: The Definition of User Experience (UX)](https://www.nngroup.com/articles/definition-user-experience/) - The industry's standard short definition of UX, and how it differs from usability and UI.
* [NN/g: 10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) - A concise usability checklist. This chapter's five principles are the course-sized relative of these ten.
* [MDN: Design for developers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Design_for_developers) - MDN's design primer written for people who code first, at exactly this chapter's depth.
* [A List Apart: Sketching: the Visual Thinking Power Tool](https://alistapart.com/article/sketching-the-visual-thinking-power-tool/) - The case for fast, rough sketching as a thinking tool, not an art project.
* [W3C WAI: Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/) - The standards body's introduction to the principle that gets its own chapter in this book.

---

## Looking Ahead ⏩

Your phone-width wireframes made promises this chapter's toolbox cannot fully keep. `flex-wrap` lets full rows break, and that is half of responsive design. Chapter 8 delivers the other half, media queries: style rules that switch on at chosen screen widths, so one stylesheet serves every frame you drew. The club's site returns as that chapter's starter files, and your narrow sketches stop being promises.
