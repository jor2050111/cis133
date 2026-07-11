# Chapter 8: Responsive Design and Media Queries

Skills Lab 7A ended with a site plan the club's officers could read and approve: six pages, a navigation plan, and wireframes for every page at two widths. The desktop frames were easy to trust, because you have been building their layouts since Chapter 6. The phone frames were promises. Nav labels stacked into a column, regions narrowed, and type stepped down, all below some chosen width. Chapter 7 admitted the debt in its final paragraph: your toolbox could not fully keep those promises yet.

The debt is older than the wireframes. When Chapter 6's announcement board learned to wrap, the book called that trick "half of responsive design." Rows that break, images that never overflow, and a column that stops growing all bend to whatever window they are given. Not one of them can change a value because the screen changed. The padding you tuned for a laptop stays laptop-sized on a phone. So does every font size, every gap, and every link target. Bending is not adapting.

This chapter delivers the other half. You will teach every page to report its true width with one line in the head. You will test phone layouts in browser DevTools device mode without owning a drawer of phones. You will write media queries, style rules that switch on at the widths you choose. And you will organize a stylesheet as base styles plus overrides, so one file serves every screen your visitors bring. Skills Lab 8A puts all of it to work on the club's site, which returns as this chapter's starter exactly as Chapter 7's audit left it.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 5-7 (the box model, Flexbox, the club site's stylesheet, and the phone-width wireframes from Lab 7A)
* **Deliverables:** Skills Lab 8A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-8.1 (Apply):** Implement the viewport meta tag on every page of a site, testing the result in browser DevTools device mode
* **MLO-8.2 (Apply):** Construct media queries that adjust layout, spacing, and type at content-driven breakpoints
* **MLO-8.3 (Analyze):** Diagnose where a layout fails across screen widths and which layer of a base-plus-overrides stylesheet owns the fix

### This chapter aligns with the following Course Learning Outcomes

* **CLO X (Apply):** Adapt web content for various screen sizes using CSS media queries

---

## 8.1 One Site, Every Screen

The club's site reads beautifully in a laptop window. That is the width it grew up at, across three labs of colors, spacing, and layout. Around half of the web's traffic arrives on a phone, though, and a phone offers a fraction of that width. No club officer will accept "works on my laptop" as done.

**Responsive design** is the practice of building one page that adapts its layout to every screen size. One URL, one HTML file, one stylesheet, every screen. This section takes inventory of how far the site already gets on that promise, and names exactly what is missing.

### The Inventory: What Already Bends

You have been building responsiveness without the name since Part II. Three mechanisms in `club-styles.css` already answer a narrow window, and each one pays a debt this book has carried.

First, rows that break. `flex-wrap` lets the header's flex line and the gallery's row drop items onto new lines when the width runs out. Chapter 6 built both and called the trick half of responsive design.

Second, images that never overflow. One rule has been riding in your stylesheet since the Chapter 6 pack, and that pack's README promised Chapter 8 would explain it. This is that explanation:

```css
/* Every image caps at the width of whatever box holds it, and
   height: auto keeps its shape as the width shrinks. Shipped
   ahead of schedule in the Chapter 6 pack. This is its chapter. */
img {
    max-width: 100%;
    height: auto;
}
```

Developers call the pattern fluid images. An image with a fixed width bursts out of any box narrower than itself, which is exactly what an 800-pixel photo would do to a phone-width column. Capped at 100 percent of its container, the image shrinks with the box that holds it and never punches through.

Third, a ceiling instead of a fixed size. The readable column Chapter 5 built uses `max-width`, and Chapter 5 promised the column would learn to adapt to any screen. Half of that promise was built in from the start. A ceiling caps how wide the column may grow and says nothing about how narrow it may shrink, so a narrow window already gets a narrower column for free.

### What No Rule Can Do Yet

Now look at what all three mechanisms have in common. They bend to the window continuously, the same way at every width, because nothing in CSS so far can ask how wide the screen is. No rule you own can say "on a small screen, use this value instead." Padding you tuned at laptop width in Chapter 5 is the same padding on a phone, where it spends width the visitor cannot spare. The banner heading sized for a wide window stays that size on a narrow one. The wireframe promise "the nav stacks below a chosen width" needs a tool that knows what the width is. That tool is this chapter's media query, and it is the difference between a layout that bends and a layout that adapts on purpose.

Line up your Chapter 7 phone frames against the toolbox and the gap shows plainly:

| Phone-frame promise | The tool that keeps it |
| --- | --- |
| Full rows break into stacks | `flex-wrap`, owned since Chapter 6 |
| Images never overflow their region | fluid images, owned and now explained |
| The text column never outgrows the screen | `max-width` ceilings, owned since Chapter 5 |
| Regions rearrange below a chosen width | media queries, this chapter |
| Type and spacing step down on phones | media queries, this chapter |

### Design the Narrow Screen First

Chapter 7 had you draw the phone frame for every page, and that order was deliberate. **Mobile-first** design starts every decision at the narrow screen: plan the phone layout first, then let wider screens be the enhancement. The narrow frame forces the hard calls, because width is scarce and every region must earn its place. Widen from there and the page grows generous. Work the other direction, shrinking a finished desktop design, and you spend the afternoon deciding what to take away.

Mobile-first is an order of operations, not a law. Section 8.4 shows both directions inside a stylesheet, because the club's own stylesheet grew up at laptop width, and the honest path from there runs the other way.

Your final project rides on this chapter too. The phone wireframes in your Checkpoint 1 site plan were promises, and now their build tool exists. When Checkpoint 2 asks for draft pages, those pages should arrive responsive.

One more connection before the tools arrive. Chapter 7's principle list named responsiveness as one of five measures of UX, and a phone-ready layout serves more of the list than its own row. A page a visitor can read without pinching is usability on a small screen. Targets a thumb can hit are accessibility. Responsive design is UX work you happen to do in CSS.

### Try It Yourself 8.1: Two Sites, One Narrow Window 🛠️

**Predict:** You are about to squeeze two pages: the Wikipedia article you audited in Chapter 7, and the club's own starter page. Predict what each page will do as the window narrows. Does either one change its layout plan outright, with regions moving or disappearing? Does either keep a single plan and bend it? Commit to one specific expectation per page.

**Run:** Open `https://en.wikipedia.org/wiki/Recycling` in one browser window and the pack's `assets/code/chapter-08/starter-site/recycling-guide.html` in another. Drag each window's edge slowly from full laptop width to as narrow as it will go, twice each. Watch regions, not words: what moves, what shrinks, what rearranges, what disappears.

**Explain:** In 1-2 sentences, report what each page did, and tie the club page's changes to this section's inventory: name the mechanism behind each change you saw.

### Quick Check 8.1 ✅

1. A clubmate declares the site phone-ready because "the images shrink and the rows wrap." Using this section's inventory, name what those mechanisms do, and the one thing neither of them can do.
2. Chapter 7's phone wireframes stacked the nav labels and narrowed every region "below a chosen width." Explain why no tool from Chapters 1-6 can honor the words "below a chosen width."
3. Responsive design pays the responsiveness principle by definition. Name one more of Chapter 7's five UX principles that a phone-ready layout serves, with one small-screen example.

---

## 8.2 The Viewport Meta Tag

Before a page can adapt to a phone, the phone has to tell the truth about its width. By default, it will not.

### The Phone's Make-Believe Canvas

Hand most phone browsers a page with a bare head and they pretend. They lay the page out on a make-believe canvas about 980 pixels wide, then shrink the finished picture until it fits the glass. The visitor gets a postcard of a laptop page: the whole layout visible, every word too small to read, pinch and zoom as the price of entry.

The lie is history, not malice. When browsers first reached phones, nearly every page on the web was built for desktops and had never been asked about a small screen. Rendered at a phone's true width, those pages collapsed into mangled single columns. Rendered wide and shrunk, they at least looked like themselves. Phone browsers chose the shrink, and legacy pages still depend on it. Your pages pay the same price until they announce they can do better.

The canvas in this story has a name you will use for the rest of the course. The **viewport** is the area a browser gives a page to lay out in. On your laptop it is the window's page area, which is why dragging a window's edge has resized every layout this book has shown you. On a phone, for a page that stays silent, it is the wide make-believe canvas.

### One Line in the Head

The announcement is one line, the **viewport meta tag**, and you should learn it as a unit:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

It is a `<meta>` element, the same head machinery that has carried your character encoding since Chapter 2. Its `content` value makes two statements. `width=device-width` sets the layout viewport to the device's real width: no make-believe canvas, no shrinking. `initial-scale=1` starts the zoom at 100 percent, so the page arrives at its true size and the visitor zooms only when they choose to.

The tag belongs in the head of every page, next to the charset line. From this chapter on, it is part of the course's document skeleton, as fixed as the doctype:

```html
<!-- The course's head skeleton from this chapter on: encoding,
     viewport, title, stylesheet. -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Recycling Guide | PC Computer Club</title>
    <link rel="stylesheet" href="club-styles.css">
</head>
```

Be clear about what the tag buys, because it is honesty, not magic. It stops the shrink and hands your stylesheet the device's true width. If the layout cannot fit that width (a fixed-width box, an uncapped image), the page overflows and the visitor scrolls sideways. The tag creates the conditions responsive design works in. The stylesheet still does the adapting, which is the rest of this chapter.

One more fact explains why this must become a habit. The HTML validator does not require the tag. A page with a bare head validates with zero messages and still renders as a postcard on every phone. You met this gap in Chapter 4: valid and well built are different standards. No tool will remind you, so the skeleton is the reminder.

### Device Mode: A Drawer of Phones in DevTools

You could test all this by owning one of every phone. DevTools ships the practical answer. **Device mode** is DevTools' phone emulation view: find the device toolbar in DevTools, switch it on, and pick a phone profile from its list. The page area re-renders as that phone would render it, at that phone's width, and device mode reports the rendered width so you can log exact numbers.

Device mode is also where you can watch the lie happen, and the next exercise stages exactly that. A narrow desktop window can never show you it, because a desktop window always gives the page its real width, tag or no tag. That is why your window-dragging tests from earlier chapters kept working on tagless pages, and why they stop being enough the moment phones are the audience.

Device mode is an emulation, and emulation is not the last word. Chapter 12's pre-flight check renders the finished site in multiple browsers and screen sizes before anything publishes, and a real phone belongs in that check. For this chapter's work, device mode is the right tool: fast, exact about widths, and sitting inside the DevTools you already use.

### Try It Yourself 8.2: One Line, Two Pages 🛠️

**Predict:** Your pack ships one page in two head states: `no-viewport.html` and `viewport.html`, in `assets/code/chapter-08/`. Their bodies are identical, and their heads differ by exactly one line. Predict what device mode will show for each at the same phone profile: will the two match, and if not, what will differ? Predict the rendered width each one reports.

**Run:** Open each file in its own browser tab. Switch on device mode, pick the same phone profile for both, and compare the two tabs: the text size, the line lengths, and the rendered width in the readout.

**Explain:** In 1-2 sentences, name the visitor the tag serves, and explain how one line in the head produced every difference you saw.

### Quick Check 8.2 ✅

1. A page validates with zero messages and still renders as tiny, shrunken text on every phone. Reconcile the two facts, and name the line that fixes the rendering without changing the validator's report.
2. State what most phone browsers do with a page whose head carries no viewport tag, then translate the tag's two settings into plain words.
3. A clubmate tests phone layouts by dragging their laptop's browser window narrow and calls device mode unnecessary. Name one thing the narrow window shows honestly, and one thing only device mode can show.

---

## 8.3 Media Queries and Breakpoints

The tag makes phones honest about their width. Now the stylesheet needs a way to act on the number.

Your pack ships this chapter's practice bench: `query-playground.html` and `query-playground.css` in `assets/code/chapter-08/`, side by side so the page's relative `href` finds the stylesheet. The page is the club's bulletin: a deep teal banner, a wrapping row of four update cards, and a centered reading column. Its head already carries the viewport tag, because the skeleton rule starts now. Unlike Chapter 6's bench, this one arrives with its queries already written at the bottom of the stylesheet. Your work in this section is to read each one, predict what it does, and check yourself against the screen.

### The Anatomy of a Media Query

A **media query** is a condition wrapped around ordinary CSS rules. The rules inside apply only while the screen satisfies the condition. Here is one the tutoring center might write for its sign-up banner:

```css
/* Waits until the condition in parentheses is true, then
   recolors the sign-up banner. On screens the condition does
   not describe, this block might as well not exist. */
@media (max-width: 720px) {
    .signup-banner {
        background-color: #5e9959;  /* saguaro green */
    }
}
```

Read it outside in, the way Chapter 4 read its first rule. `@media` is the opener, and it breaks a pattern: every rule you have written until now began with a selector. This one begins with an at sign, and CSS calls it an **at-rule**, an instruction to the stylesheet itself instead of a style for one selector. `@media` is the first at-rule this course has needed. Others exist (`@import` loads another stylesheet, `@font-face` loads a font), and you will meet them in the wild long before you need to write one.

After the opener comes the **media feature** in parentheses: `(max-width: 720px)`, the condition being tested. It looks like a declaration and is not one. It is a question about the viewport. Between the braces sits a block of ordinary rules, selectors and declarations exactly as Chapter 4 taught them. Keep the three anatomy names straight:

* The at-rule: `@media`, announcing a condition instead of a selector
* The media feature: the question in parentheses, here "is the viewport at most 720 pixels wide?"
* The block: ordinary rules that apply only while the answer is yes

Nothing inside the braces is new. What is new is the switch around them.

### Try It Yourself 8.3: Call the Flip 🛠️

**Predict:** Open `query-playground.css` and read the small-screen block at the bottom of the file. From the query alone, predict the exact width at which the page background changes as you drag inward. Predict whether the boundary width itself shows the old color or the new one. And name the second thing the same block changes.

**Run:** Open `query-playground.html` with DevTools open, so the browser reports the window's width in the corner of the page area while you resize. Drag the window edge inward slowly until the background flips, then creep back and forth across the boundary until you have pinned the number.

**Explain:** In 1-2 sentences, state the flip width you observed and which color the boundary width wore, then point at the words in the query that predicted both.

### At Least, At Most

Two media features carry this course, and they are mirror images. `max-width` asks "is the viewport at most this wide?" It is the small-screen feature: its block fires on narrow windows and sleeps on wide ones. `min-width` asks "is the viewport at least this wide?" It is the wide-screen feature, and it fires in the other direction. Before you trust any query, say it aloud as a sentence. The words settle most confusion before it starts, including what happens at the boundary itself:

| Query | Say it aloud | At a window exactly 600px wide |
| --- | --- | --- |
| `@media (max-width: 600px)` | "at most 600 pixels wide" | Applies, because 600 is at most 600 |
| `@media (min-width: 600px)` | "at least 600 pixels wide" | Applies, because 600 is at least 600 |

Each feature includes the width it names. That is why TIY 8.3's flip landed exactly on the boundary instead of one pixel inside it. Bank one consequence now: a `max-width: 600px` query and a `min-width: 600px` query would both fire at a 600-pixel window. When two queries must split every width cleanly between them, their numbers differ by one, and Section 8.4 shows the pair.

The playground's banner title carries a matched pair, one of each:

```css
/* The banner title's two adjustments. The base rule above the
   queries sets 28px. One query steps the title down on narrow
   windows, the other steps it up on wide ones. */
@media (max-width: 500px) {
    .banner-title {
        font-size: 22px;
    }
}

@media (min-width: 900px) {
    .banner-title {
        font-size: 36px;
    }
}
```

Look carefully at the pair's numbers. A pair like this can leave a stretch of widths where neither condition is true and neither block applies. A width the queries leave alone is not an error. It is the base rule doing its job, and the next exercise makes you find that stretch and prove it.

### Try It Yourself 8.4: Three Widths, One Title 🛠️

**Predict:** Using the pair above and the base rule, predict the banner title's computed `font-size` at three window widths: 400, 700, and 1000 pixels. One of the three is caught by neither query. Name which, and say what size it gets instead.

**Run:** Set each width in turn, dragging the window against the width readout or typing the width into device mode. At each stop, right-click the title, choose Inspect, and read its computed `font-size` in DevTools.

**Explain:** In 1-2 sentences, name the width that fell in the gap between the queries, and state which rule supplied its size.

### Where Breakpoints Come From

A **breakpoint** is the width at which a media query changes the layout. Every query you write needs one, so where does the number come from?

The wrong answer is a chart. Lists of popular device widths circulate online, with 768 pixels as a perennial favorite, and they describe last year's devices. Devices change sizes every year. Your content does not change with them, and your content is what the breakpoint protects.

The right answer is a test you already know how to run: resize until the layout embarrasses itself, and read the width where it happens. The playground's card row shows how concrete that number is. Each update card is 260 pixels wide, the gaps between cards are 20, and the row's own padding and borders take 44 pixels of the window in total. Two cards plus one gap need 540 pixels of row content, and 540 plus 44 is 584. Drag the playground across that line and watch: at 584 the row seats two cards, and at 583 it drops to one. The same arithmetic seats three cards from 864 and four from 1144.

That drop at 584 is the content talking. If the one-card row looked cramped and you wanted a query to restyle it, 584 would be your breakpoint, derived from your own boxes instead of copied from a chart. Skills Lab 8A asks you to derive a breakpoint from the club site's content exactly this way: find where the layout stops fitting, and let the width you read become the number you write.

!!! tip
    Name breakpoints after content events in your comments: "where the card row drops to one" travels better than "tablet width." Devices retire every year. Your content stays yours.

### Quick Check 8.3 ✅

1. Read `@media (min-width: 860px)` aloud as a sentence, and state whether its rules apply at a window exactly 860 pixels wide.
2. In `@media (max-width: 480px) { .club-note { padding: 8px; } }`, point out the at-rule, the media feature, and the ordinary rule, naming each part.
3. A teammate picks 1024 pixels as a breakpoint because a chart of device widths recommends it. State where this chapter says breakpoints come from, and describe the test that finds one for any page.

---

## 8.4 The Pattern: Base Styles Plus Overrides

You can now write a query. This section teaches you where queries live in a stylesheet, and it is the difference between a file that scales and a file that fights you.

### Base Rules and Their Overrides

The architecture has two layers. The rules outside every query are the stylesheet's **base styles**, and they serve every screen, whatever its width. The rules inside a query are **overrides**, and they carry only the differences for the widths the query names. An override never repeats what the base already says. The playground's card padding is the model:

```css
/* The base rule, trimmed to the declaration that changes: a
   card's padding at every width the queries leave alone. */
.update-card {
    padding: 20px;
}

/* The small-screen override: only the difference. At 600 pixels
   and below the padding tightens, and every other declaration
   in the base rule still applies. */
@media (max-width: 600px) {
    .update-card {
        padding: 10px;
    }
}
```

On a narrow window the card keeps its white background, its teal border, and its width from the base rule. Only the padding changes, because only the padding is written in the block. Repeat the whole rule inside the query and you plant a trap: next month someone edits the base border and the query's forgotten copy quietly disagrees.

Why does the override win at 600 pixels and below? Not because queries outrank base rules. They do not. A rule inside a query has exactly the specificity its selector earns, so `.update-card` inside the block ties `.update-card` outside it. Chapter 4's tie-breaker settles ties between equals: the later rule wins. That is why every query block lives below the base rules it adjusts. Put the block above the base and the base has the last word at every width, and your overrides never show. This is a law of source order, not a preference.

Step back and notice what the pattern preserves. Chapter 4 promised that the one external stylesheet would follow the site everywhere, adapting it to every screen size. This is how the promise is kept without a second file. The site still has one stylesheet and every page keeps its single link element. The file grew layers, not copies.

!!! tip
    Gather every query block at the bottom of the stylesheet, below all the base rules, the way the playground's stylesheet does. One place to look, and the source-order law holds for the whole file. Comment each block with its job, because Chapter 4's comment law has not changed.

### Two Directions, One Pattern

The pattern reads in two directions, and the difference is which screen the base serves. Mobile-first order is Section 8.1's design habit applied to CSS: the base rules describe the narrow layout, and `min-width` queries grant wider screens their extra room.

```css
/* Mobile-first: the base is the phone layout, and the query
   hands wider windows their extra side padding. */
.tour-schedule {
    padding: 12px;
}

@media (min-width: 700px) {
    .tour-schedule {
        padding: 12px 40px;
    }
}
```

Desktop-first order runs the retrofit direction: the base rules describe the wide layout, and `max-width` queries tighten it for small screens.

```css
/* Desktop-first: the base is the wide layout, and the query
   tightens it for small screens. Same two layouts, same
   boundary, read from the other direction. */
.tour-schedule {
    padding: 12px 40px;
}

@media (max-width: 699px) {
    .tour-schedule {
        padding: 12px;
    }
}
```

The two numbers differ by one on purpose. "At most 699" and "at least 700" split every whole-pixel width between them, with no overlap. A zoomed browser can report a fractional width that slips between the two, a corner case to know about, not to design around.

Which direction should you write? Starting a stylesheet from nothing, professionals usually go mobile-first. The reason is Chapter 7's: the narrow layout is the harder discipline, so it should be the foundation, not the afterthought. The club's stylesheet is not starting from nothing. It grew up at laptop width across three labs, it works there, and rewriting it narrow-first would cost hours and teach little. So the lab retrofits: the desktop-grown sheet stays the base, and `max-width` overrides tighten the small screens. Retrofit is honest, common industry work. Many of the stylesheets you will meet in the wild were desktop sites once.

### Reading a Responsive Stylesheet

The last skill is reading, because from now on a stylesheet's rules no longer all apply at once. The skill is the trace: pick one element, one property, and one width, then ask which rules are awake at that width and let the cascade pick among them. Here is the banner title, complete, followed by its trace:

```css
/* The banner title, complete: one base rule, two overrides.
   Every window width lands in exactly one of three outcomes. */
.banner-title {
    font-size: 28px;
}

@media (max-width: 500px) {
    .banner-title { font-size: 22px; }
}

@media (min-width: 900px) {
    .banner-title { font-size: 36px; }
}
```

| Window width | Query awake at that width | Computed `font-size` |
| --- | --- | --- |
| 400px | `max-width: 500px` | 22px, the small-screen override |
| 700px | none | 28px, the base |
| 1000px | `min-width: 900px` | 36px, the wide-screen override |

Run every trace the same way. Start from the base value, then let each query whose condition is true, and whose block mentions the property, overwrite it in source order. You confirmed this exact table in TIY 8.4 with DevTools. The exercise below hands you a fresh trace with one deliberate surprise in it.

One boundary of this chapter, marked on the way out: width is not the only question a query can ask. Media features exist for orientation (is the screen taller than it is wide?), among others, and a query can also name a media type: `@media print` styles the page headed to a printer. This course's work needs width alone.

### Try It Yourself 8.5: Trace the Card Padding 🛠️

**Predict:** Run the trace on `.update-card`'s `padding` at three widths: 480, 800, and 1100 pixels. Write all three computed values before touching the browser, using the playground queries you have already read. Think hard about the third width: does any rule grant wide screens extra padding?

**Run:** Set each width in turn, select one update card with Inspect, and read its computed `padding` in DevTools. Three widths, three readings, checked against your three predictions.

**Explain:** In 1-2 sentences, explain why two of the three widths produced the same value, using the words base and override.

### Quick Check 8.4 ✅

1. A query block copies all five declarations from the base rule it adjusts and changes only one. Name the pattern rule this breaks, and describe what happens when the base rule changes next month.
2. A stylesheet's small-screen query block sits at the top of the file, above the base rules, and none of its overrides ever show. Diagnose the defect using Chapter 4's tie-breaker, and state the fix.
3. Contrast mobile-first order with desktop-first order in one sentence each, then name which order Skills Lab 8A uses on the club's stylesheet and why.

---

## 8.5 Summary and Retrieval 💡

### Key Concepts

* Responsive design serves every screen from one page, one stylesheet, one URL. The club's stylesheet already bends: rows wrap (`flex-wrap`), images stay fluid (`max-width: 100%` with `height: auto`, the pack rule finally explained), and the readable column's `max-width` is a ceiling narrow windows duck under. None of those can change a value at a chosen width. That is the media query's job.
* Most phone browsers lay a silent page onto a make-believe canvas about 980 pixels wide and shrink the picture to fit. The viewport meta tag (`width=device-width, initial-scale=1`) opts out, and it belongs in every head from now on. The validator never requires it: valid and phone-ready are different standards.
* Device mode is DevTools' phone emulation view. It renders a page as a chosen phone would, reports the rendered width, and shows what the missing tag costs, which a narrow desktop window can never show.
* A media query is the course's first at-rule: `@media`, a media feature in parentheses, and a block of ordinary rules that apply only while the condition holds. `max-width` means at most, `min-width` means at least, and each includes the width it names. Widths no query catches fall back to the base rules.
* Breakpoints come from content, not device charts. Resize until the layout embarrasses itself, read the width, and write that number, the way the playground's card row hands you 584 from its own arithmetic.
* Base styles serve every screen, and overrides carry only the differences. A query's rules tie their base rules on specificity, so source order decides: every query block lives below the rules it adjusts. Mobile-first and desktop-first read the same pattern in opposite directions, and retrofitting a desktop-grown sheet with `max-width` overrides is honest industry work.

### Key Terms

See course glossary for full definitions

* responsive design, mobile-first (Section 8.1)
* viewport, viewport meta tag, device mode (Section 8.2)
* media query, at-rule, media feature, breakpoint (Section 8.3)
* base styles, override (Section 8.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the viewport meta tag, and state what most phone browsers do to a page that lacks it.
2. Say `@media (max-width: 800px)` and `@media (min-width: 800px)` aloud in words, and state what each does at a window exactly 800 pixels wide.
3. State where this course says breakpoints come from, and describe the resize test that finds one.
4. Explain why a query block must sit below the base rules it adjusts, naming the cascade tie-breaker that makes it so.
5. Name the two halves of responsive design as this book taught them, with the chapter that delivered each half.

---

## 8.6 Skills Lab 8A: The Club Site Meets Every Screen

**Goal:** Retrofit the club's site for every screen: the viewport meta tag on every page, a content-driven small-screen query block, and one more query of your own, proven at three widths in device mode.

**Dataset:** Provided files in `assets/code/chapter-08/` from the course data pack. `starter-site/` holds the club's three pages, the `images` folder, and `club-styles.css`, exactly as Skills Lab 6A finished them and Chapter 7's audit left them. The pages validate with zero messages, and no head carries a viewport tag. `club-palette.txt` travels with every CSS chapter, copied unchanged from the Chapter 6 pack. `query-playground.html` and `query-playground.css` are the chapter's practice pair. `no-viewport.html` and `viewport.html` are TIY 8.2's matched pair, one page in two head states. `skills-lab-8a-answers.txt` is your written answers file. The folder's README documents every file. Work at the extracted `cis133` root and copy every hex value from the palette file.

The lab walks the chapter's own path. Part 1 gives every page the tag and gathers the diagnosis. Part 2 turns the diagnosis into the site's first query block. Part 3 adds a query of your own and proves the site at three widths.

### Part 1: Foundation (Aligns with MLO-8.1)

1. Copy the whole `starter-site` folder to your `cis133` root and rename the copy `skills-lab-8a-lastname`. Copy `skills-lab-8a-answers.txt` into it.
2. Add the viewport meta tag to all three pages' heads, next to the charset line, exactly as Section 8.2 wrote it. Open one page in device mode at a phone profile, before and after the edit if you want the drama, and record the tag, what changed, and your phone profile in answer 1.A.
3. With the tag in place, log the rendered width device mode reports for each of the three pages at your phone profile in answer 1.B.
4. Now diagnose. Walk each page at three widths (a phone width, a mid width, and a laptop width) and list every place the layout embarrasses itself: what crowds, what wastes space, what gets hard to tap. Record the diagnosis list in answer 1.C, naming the page, the width, and the failure. This list is your evidence for Part 2.

### Part 2: Application (Aligns with MLO-8.2, MLO-8.3)

1. Derive the breakpoint. One page in your diagnosis hands you a number. Drag the gallery page inward and find the exact width where its figures stop sharing a line, pinning it down the way TIY 8.3 pinned the flip. Defend the number with content evidence in answer 2.A: what stops fitting there, and what observation or arithmetic produced it. The gallery row's own widths can confirm the number, the way Section 8.3's card arithmetic confirmed 584.
2. Write the small-screen block. At the bottom of `club-styles.css`, below every base rule, open a `max-width` query at your breakpoint with a comment naming its job. Give it three overrides. The gallery's figures span the full row width. `main`'s side padding tightens, because the laptop cushion spends width a phone cannot spare. And the nav links' padding grows into targets a thumb can hit, which serves Chapter 7's accessibility principle.
3. Prove it fired. Check each page below your breakpoint in device mode and confirm all three overrides show. Then copy the whole block, comment included, into answer 2.A.

### Part 3: Extension (Aligns with MLO-8.3)

1. Write one more query of your own choosing and defend it in answer 3.A. Two directions are worth the work. A wide-screen enhancement: a `min-width` query that seats three gallery figures when the window offers the room, with your arithmetic shown. Or a further small-screen refinement: a heading that steps down, or a header that stacks its logo above its title. Whichever you choose, the block carries only differences and sits below the rules it adjusts.
2. Run the three-width verification pass: every page at your phone, mid, and laptop widths from Part 1, in device mode. At each stop confirm the layout you shipped: nothing overflows, nothing crowds, every target is comfortable.
3. Validate everything: all three pages through the W3C HTML validator and `club-styles.css` through the CSS validator, repairing until every report shows zero messages. Log the results in answer 3.B. Then run the Part III milestone check for the responsive leg: name where a grader sees the site adapt, as a page, a width to set, and a visible change.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Before this lab, `club-styles.css` never asked the window its width, and the site still bent on narrow screens. Name two mechanisms already in the stylesheet that adapt without a query, and explain what your Part 2 block does that neither of them could. Cite one observation from your own Part 1 diagnosis as evidence.
2. A clubmate skipped the diagnosis and set their breakpoint at 768 pixels because a chart of device widths named it. Defend your Part 2 breakpoint against theirs: what makes a breakpoint right for this site in particular, and what happens to each approach when next year's phones arrive at new sizes?

**Submission:** Zip your `skills-lab-8a-lastname` folder containing your three HTML pages, your `images` folder, `club-styles.css`, and `skills-lab-8a-answers.txt`, and submit it as `skills-lab-8a-lastname.zip`. All three pages and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 8A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s).

---

## 8.7 Review Questions 🔄️

1. **Remember:** Write the viewport meta tag from memory, name where in a document it belongs, and state what each of its two settings tells the browser.

2. **Understand:** A stylesheet contains `@media (max-width: 700px)`. Say in plain words when its rules apply, state whether they apply at a window exactly 700 pixels wide, and explain why the block belongs below the base rules it adjusts.

3. **Apply:** The tutoring center's banner heading renders at 34 pixels on every screen, crowding phones and whispering on wide monitors. Write two queries on its `.banner-heading` rule. One steps it down to 26 pixels when the window is at most 480 pixels wide. The other steps it up to 40 pixels at 1000 pixels and wider. Then state the heading's computed size at a 720-pixel window and justify it with the trace.

4. **Evaluate:** A tutoring center volunteer proposes solving phones with a second site: copy every page into a phone folder, keep a separate phone stylesheet, and post a second address for phone visitors. Judge the proposal against this chapter's pattern and Chapter 7's consistency principle. Count the cost of the next content edit under each approach, and name what one stylesheet with query overrides preserves that a copied site cannot.

---

## Further Reading 📖

* [MDN: Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using) - The reference walk through `@media` syntax and media features, at exactly this chapter's depth.
* [MDN: Viewport meta tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport) - What each part of the tag's `content` value means, and why the tag exists at all.
* [web.dev: Learn Responsive Design](https://web.dev/learn/design/) - Google's free responsive design course, extending this chapter from queries into fluid layouts and responsive type.
* [MDN: Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) - The overview that places media queries beside the other responsive tools, including the fluid images this chapter explained.
* [CSS-Tricks: A Complete Guide to CSS Media Queries](https://css-tricks.com/a-complete-guide-to-css-media-queries/) - The industry reference card for query syntax and features beyond width.

---

## Looking Ahead ⏩

The club's site now answers every screen size a visitor can bring. Chapter 9 asks the harder question: does it answer every visitor? The accessibility habits you have carried since Chapter 3 (honest alt text, landmarks, focus styles no rule removes) come from a written standard called WCAG, with four principles of its own. You will meet the contrast math behind the palette's passing list, and you will learn what the `rem` unit does for visitors who resize their type. Device mode tested widths. Chapter 9 tests everything else.
