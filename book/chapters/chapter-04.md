# Chapter 4: CSS Foundations

Skills Lab 3A left the club with a site that does everything right. Three pages validate with zero messages, every image carries honest alt text, and Devon's screen reader jumps region to region through the landmarks you built. Then the club president opened the site at a meeting and asked the question you could feel coming: "Our logo is teal. Our illustrations paint a whole desert palette. Why is the site gray?"

The president has a point, and the answer is not that something went wrong. HTML says what content IS, and it stays silent about looks on purpose. Every color the site shows today came from the browser's own defaults: black text, white background, blue links. Changing that is the job of a second language, one you have known by name since Chapter 1. CSS describes how content LOOKS, and this chapter puts it in your hands: rules that select exactly the elements you mean and declare how they should appear.

The design team already did the hard part. The illustration set that drew the logo, the charts, and the drive scenes defines the club's palette, and it ships in your data pack as a file of exact color values. You will connect stylesheets to pages three ways and learn which one professionals default to. You will write selectors that target whole regions, chosen groups, and single elements. You will dress all three pages from one file. And you will add a second validator to your toolkit, because CLO IV's critique habit covers styles as much as markup. One rule carries over from Chapter 3: nothing you style this week may cost the meaning your landmarks built. Devon's jump menu works today, and it still works when the site is teal.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapters 2-3 (the HTML skeleton, attributes, landmarks, and the W3C validator habit)
* **Deliverables:** Skills Lab 4A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-4.1 (Apply):** Connect CSS to HTML pages through inline styles, internal stylesheets, and external stylesheets, choosing the method that fits the job
* **MLO-4.2 (Apply):** Write CSS rules that style page content using element, class, and id selectors with the web's color systems
* **MLO-4.3 (Evaluate):** Critique styled pages with the W3C HTML and CSS validators, interpreting their reports to repair markup and styling defects

---

## 4.1 What CSS Is: One Language for Looks

Chapters 2 and 3 built one half of a professional division of labor. HTML holds the content and says what each piece IS: a heading, a list of steps, a navigation region. CSS holds the presentation and says how each piece LOOKS: its color, its size, its place on the page. Developers call this split **separation of concerns**, and it is the single most useful idea in this chapter. Keep content and looks in separate files and you can restyle an entire site by editing one of them, without touching the other.

That is not a hypothetical payoff. It is the answer to the president's question. The site is gray because nobody has written its looks yet. The fix will not open a single HTML file.

The split also settles who each language serves. Chapter 3 named the three readers of an HTML file, and only one of them, the browser rendering for sighted visitors, ever sees a pixel. CSS speaks to that reader alone. Devon's screen reader and the search crawlers keep reading your markup's meaning, untouched by anything a stylesheet says. That is why styling done right costs the other readers nothing.

### The Anatomy of a Rule

CSS is a language of rules. Here is a complete one:

```css
h1 {
    color: #1a5e5e;
}
```

Read it outside in. The whole thing is a **CSS rule**, one styling instruction. The `h1` at the front is the **selector**, which names the elements the rule styles: every `h1` on the page, in this case. Everything between the braces is the **declaration block**, the list of styling instructions to apply. This block holds one **declaration**, and a declaration is always a pair: a **property** (`color`, the aspect being styled) and a **value** (`#1a5e5e`, the setting it gets). A colon separates the pair, and a semicolon ends the declaration.

That value is a color written in a system Section 4.4 unpacks. For now, know that it is the deep teal from the club logo's shading. Load this rule and every `h1` on the page turns deep teal at once. Chapter 2 told you to stop picking heading levels for their looks and promised that CSS would own them. This rule is that promise starting to pay: the headings changed and not one tag did.

A declaration block can hold as many declarations as the job needs, each ending in its own semicolon. You will collect properties for the rest of the course, and the pattern never changes. Keep the five anatomy names straight, because every tool you meet uses them:

* **Selector:** which elements the rule styles
* **Declaration block:** everything between the braces
* **Declaration:** one complete styling instruction inside the block
* **Property:** the aspect being styled, before the colon
* **Value:** the setting that aspect gets, after the colon

Error reports, DevTools panels, and documentation all speak this vocabulary. So does every teammate who ever reads your stylesheet.

### Comments in CSS

Stylesheets grow, and future readers (including you in three weeks) need notes. A **CSS comment** opens with `/*` and closes with `*/`, and browsers skip everything between. The convention from your HTML comments carries over: comment the WHY, because the code already shows the what.

```css
/* Deep teal instead of club teal: the darker shade keeps
   headings readable on the site's light backgrounds. */
h1 {
    color: #1a5e5e;
}
```

Two more habits ride along. Comment the file itself at the top, the way your HTML files have carried an identifying comment since Chapter 2. And update comments when the code under them changes, because a comment that lies is worse than no comment at all.

### One File, Any Look

How far can separation of concerns go? The classic demonstration is [CSS Zen Garden](https://csszengarden.com), a site that has collected designer submissions for over two decades. Every design on it uses the identical HTML file. Only the stylesheet changes, and the results range from clean corporate pages to full illustrated landscapes. Same content, same markup, any look. That is the power the club's site is about to borrow at a smaller scale: one stylesheet, three pages, one visual identity.

Here is the twist hiding inside the president's complaint: your "unstyled" pages were never unstyled. Every browser ships a stylesheet of its own and applies it to any page that brings no CSS. Those are the **browser default styles**, and they are where every look you have seen so far came from. Large bold headings, indented bullets, blue underlined links: all of it is the browser's taste, not the absence of taste. When you write your own rules, you are overriding defaults that were there all along.

### Try It Yourself 4.1: Catch the Browser's Stylist 🛠️

**Predict:** You are about to inspect the main heading of the Wikipedia article you visited in Chapter 3. Its look comes from CSS rules you can switch off one at a time. If you uncheck one of its declarations, will the heading lose all styling, or fall back to something else?

**Run:** Open [en.wikipedia.org/wiki/Recycling](https://en.wikipedia.org/wiki/Recycling), right-click the article's main heading, and choose Inspect. Beside the markup, browser DevTools shows a Styles panel listing every rule that reaches the heading, written exactly like this section's examples. Look for a `font-size` declaration while you are there: the heading size Chapter 2 told you to leave to CSS, being left to CSS. Hover over a declaration and a checkbox appears. Uncheck a font or color declaration, watch the heading change, then check it back on. Now scroll the panel down: the bottom rules are labeled "user agent stylesheet."

**Explain:** In 1-2 sentences, explain what took over when you unchecked a declaration, and what the user agent stylesheet entries tell you about who styled your Chapter 3 pages.

### Quick Check 4.1 ✅

1. In the rule `footer { background-color: #1a5e5e; }`, name the selector, the property, and the value.
2. Your Chapter 3 pages contained zero CSS, yet their headings rendered large and bold. Where did that styling come from, and what happens to it once your own stylesheet says otherwise?
3. The president approves a full redesign for the fall drive. Using separation of concerns, explain why the redesign can ship without editing a single HTML file.

---

## 4.2 Three Ways In: Inline, Internal, External

A rule does nothing until it reaches a page. HTML offers three connection points, and they differ in one thing that matters: how far each rule reaches. You will use all three this chapter, and by the end of it you will know why professionals default to the third.

### The style Attribute: Inline Styles

The narrowest connection is an **inline style**, CSS written into one element's `style` attribute:

```html
<h1 style="color: #268080;">Club Announcements</h1>
```

The attribute's value is a declaration list with no selector and no braces, because the selection is already made: this one element, and nothing else. That reach is the problem. Style thirty headings this way and you type thirty attributes, and the fall redesign means editing all thirty again. Worse, an inline style puts presentation back inside the content file that separation of concerns moved it out of.

Note one fact for later, because Skills Lab 4A turns it into a hunt: an inline style is legal HTML, and a page full of them validates with zero messages. Valid and well built are different standards. You learned that lesson about markup in Chapter 3, and it holds for styling too.

### The style Element: Internal Stylesheets

The middle option is an **internal stylesheet**: real rules, selectors and all, written inside a **style element** in the page's head.

```html
<head>
    <meta charset="UTF-8">
    <title>Club Announcements</title>
    <style>
        h1 {
            color: #268080;  /* club teal, the brand color */
        }
    </style>
</head>
```

Now one rule styles every `h1` on the page, and the styling lives in one findable place. The reach is still one page, though. A three-page site needs the same rules pasted into three heads, and every edit happens three times.

Internal stylesheets earn their keep on one-page experiments and practice files, which is exactly how this chapter's exercises use them. For a site, they are a halfway house you will learn to walk past.

### The link Element: External Stylesheets

The professional connection is an **external stylesheet**: a separate file of nothing but CSS, saved with a `.css` extension and connected to each page by a **link element** in the head.

```html
<link rel="stylesheet" href="club-styles.css">
```

`<link>` is an empty element, like `<meta>` and `<img>`. Its `rel` attribute names the relationship: the linked file is this page's stylesheet. Its `href` holds the file's address, under the same relative URL rules every `href` and `src` has followed since Chapter 2. The stylesheet itself holds rules and comments and nothing else. No `<style>` tags, no HTML at all:

```css
/* club-styles.css styles every page that links it. */
body {
    background-color: #fac78d;  /* light sand */
    color: #333333;             /* ink */
}
```

Notice where both the style element and the link element live: in the page's head, never in the body. The placement follows Chapter 2's definition. The head holds information about the document, and "here is how this document should look" is exactly that kind of information. It is practical too. The browser reads a file top to bottom, so a stylesheet connected in the head arrives before any content gets drawn. Move the connection to the bottom of the body and visitors watch the plain default version flash past before your colors land.

Here is the reach that changes everything. Link this one file from all three club pages and one edit restyles the whole site. Add a fourth page next month and it inherits the site's look with a single link element. That one file follows the site everywhere: Chapter 8 adapts it to every screen size, and Chapter 12 publishes it along with the pages. When this book says "stylesheet" without qualification from here on, it means this.

One clarification keeps beginners out of trouble. The stylesheet does not broadcast itself to the site. Each page opts in with its own link element, so a three-page site carries three identical `<link>` lines, one per head. Forget one and that page alone shows up to the meeting in browser defaults.

| Method | Lives in | Reaches | Reach for it when |
| ------ | ------- | ------- | ----------------- |
| Inline style | A `style` attribute on one tag | One element | Quick tests, and even then think twice |
| Internal stylesheet | A `<style>` element in the head | One page | One-page practice files and experiments |
| External stylesheet | A separate `.css` file | Every page that links it | Building a site, which makes it the default |

Why learn three methods when one wins? Because you will meet all three in the wild, and because they explain each other. This chapter's practice exercises use internal stylesheets to keep each experiment in one file. Old code and page-builder tools lean on inline styles more than they should, and Skills Lab 4A has you retire one. Professional sites keep everything they can external. Knowing all three also prepares you for the moment they disagree, which is next.

### When Rules Collide: The Cascade

Three connection methods mean rules can disagree. Suppose the external file says the heading is deep teal, an internal rule says ink, and an inline style says club teal. The heading can only be one color, so CSS needs tie-breakers. That system is the **cascade**, the C in CSS, and two of its rules carry you a long way:

* An inline style wins over stylesheet rules, because nothing sits closer to the element.
* Between stylesheet rules with an equal claim, the later one wins: later in the file, or from the later of two stylesheets in the head.

One more tie-breaker, a more specific selector beating a general one, makes a cameo in the next section. The full system, and selectors smart enough to need it, arrive in Chapter 6.

The cascade also explains Section 4.1's overriding act. The browser treats its own default stylesheet as the weakest claim of all, so any rule you write beats it. Your pages were never fighting the defaults. The defaults were only ever holding the floor until you spoke.

### Try It Yourself 4.2: One Heading, Many Rules 🛠️

Your data pack ships a matched pair for this experiment: `assets/code/chapter-04/cascade-practice.html` and `practice-styles.css`, which sit side by side so the page's relative `href` finds the stylesheet. Open the page in your browser and both files in VS Code. The heading arrives deep teal, courtesy of the external file's `h1` rule.

**Predict:** You will add an internal rule making the heading ink (`#333333`) and then an inline style making it club teal (`#268080`). With all three in place, which color shows? And after you delete the inline style, which of the two survivors takes over?

**Run:** Add a `<style>` element to the page's head, below the link element, containing `h1 { color: #333333; }`. Save and refresh. Then add `style="color: #268080;"` to the `h1`'s opening tag. Save and refresh. Finally, delete the inline style attribute and refresh once more.

**Explain:** In 1-2 sentences, rank the three connection methods by what you watched win, and explain why the internal rule beat the external one after the inline style left.

### Quick Check 4.2 ✅

1. The club adds a fourth page next month. With the site on one external stylesheet, list every edit the new page needs to wear the site's full look.
2. One stylesheet contains `h2 { color: #268080; }` near the top and `h2 { color: #1a5e5e; }` near the bottom. Which color renders, and which cascade tie-breaker decided?
3. An inline style is legal HTML and passes the validator. Give two reasons it is still the wrong home for a site's styling.

---

## 4.3 Choosing Your Target: Element, Class, and id Selectors

Chapter 3 closed with a promise: the landmarks you built would become the exact hooks your stylesheets grab first. This section pays it. Every selector you write answers one question, which elements does this rule reach, and CSS gives you three levels of aim: every element of a kind, a chosen group, or exactly one.

### Element Selectors: Styling the Landmarks

An **element selector** is what you have been writing all along: an element's name, bare, which styles every instance of that element. Point one at a landmark and a whole region changes at once.

```css
/* The landmark hooks Chapter 3 built, now earning their keep. */
header {
    background-color: #268080;  /* club teal */
    color: #ffffff;             /* white text on the brand teal */
}

nav {
    background-color: #ffffff;  /* a white bar under the header */
}

footer {
    background-color: #1a5e5e;  /* deep teal closes the page */
    color: #ffffff;
}
```

Because `club-styles.css` is linked from all three pages, these three rules style three headers, three navs, and two footers in one stroke, and the contact page's missing footer stays deliberately absent. Notice what made this cheap: the semantic structure was already there. A page of anonymous `<div>` elements has nothing this clean to grab. In Chapter 6, that `nav` hook does more: its list of links becomes a real navigation bar.

When several elements need the same declarations, a **selector list** groups them with commas instead of repeating the block:

```css
h1, h2 {
    color: #1a5e5e;  /* one heading color across the site */
}
```

### Class Selectors: Some of These, By Role

Element selectors are all-or-nothing. Style `p` and every paragraph obeys. But the club's pages have two kinds of paragraphs: ordinary prose and time-sensitive deadlines that should stand out. Same element, different roles. That calls for a **class selector**, which targets only the elements you have opted in.

The opt-in happens in the HTML, through the **class attribute**:

```html
<p class="deadline">Volunteer sign-up for the fall drive closes
Friday, October 2, at 5:00 p.m.</p>
```

The rule lives in the stylesheet, with a dot marking the name as a class:

```css
.deadline {
    background-color: #f4a259;  /* sunset orange flags the date */
}
```

A class is reusable by design. Any number of elements, on any page of the site, can carry `class="deadline"`, and every one of them gets the treatment. The reuse crosses element types too: a paragraph and a figcaption can share one class, because the selector asks about the attribute, not the element's name. A class is also a pair by design. The attribute with no matching rule changes nothing, and the rule with no opted-in elements reaches nothing.

### id Selectors: Exactly This One

Some elements are one of a kind. For those, HTML offers the **id attribute**, which names a single element, and CSS offers the **id selector**, written with a hash, to match it. An id value may appear on only one element per page. That is a promise you make in the markup, and tools take you at your word.

```html
<section id="meeting-times">
```

```css
#meeting-times {
    background-color: #deb887;  /* sand sets the schedule apart */
}
```

The one-per-page promise is enforceable, too. Hand the W3C validator a page where two elements share an id and the report flags the duplicate. That is one more defect a browser renders straight through without a word.

The decision rule for all three is worth memorizing:

* An element selector styles every one of these.
* A class styles some of these, chosen by role.
* An id styles exactly this one.

When in doubt between class and id, choose the class. Reuse costs nothing, and "unique" has a way of becoming "two of them" by next semester.

This is also where Chapter 3's meaningless containers get their jobs. A `<div>` with a class styles a region no landmark fits, and a `<span>` with a class styles a few words mid-sentence. The habit stands: semantic element first, generic container only when nothing with meaning fits.

### Name the Role, Never the Look

One law governs every class and id name you write in this course: describe the content's role, never its appearance. The class above is `.deadline`, not `.orange-text`. Both would work today. Only one survives a redesign. When the club rebrands and deadlines turn teal, `.deadline` stays true in every file that uses it, while `.orange-text` becomes a lie you either live with or hunt through the whole site to fix. The stylesheet is the single place looks are allowed to live, and appearance-based names smuggle looks back into the markup. Name by role and the HTML never needs to know what color it is.

A few pairs to calibrate your ear, role-based name first:

* `.deadline`, not `.orange-text`
* `.callout`, not `.yellow-box`
* `#signup-banner`, not `#big-teal-block`

A caution before you style the club's site: presentation never replaces structure. Once classes exist, the temptation is to wrap everything in `<div class="...">` and skip the semantic elements. Resist it. Devon's screen reader announces `<header>` as a landmark and announces a `.header-box` div as nothing at all. The landmarks cost you nothing to keep and everything to lose. Style the meaning Chapter 3 built. Never trade it for styling hooks you already have.

### Try It Yourself 4.3: Who Gets Caught 🛠️

The pack page `assets/code/chapter-04/selector-practice.html` is a club announcements page with five paragraphs, two of which carry `class="deadline"`. It links no stylesheet on purpose: you will add an internal one, which is what internal stylesheets are for.

**Predict:** You will add two rules: `p { background-color: #ffffff; }` and `.deadline { background-color: #f4a259; }`. Which paragraphs end up white and which end up orange? Be careful with the two deadline paragraphs, because both rules reach them.

**Run:** Open the file in VS Code and in your browser. Add a `<style>` element to the head holding both rules. Save, refresh, and count the white and orange paragraphs.

**Explain:** In 1-2 sentences, explain why orange won on the deadline paragraphs even though the `p` rule also matched them. Which claim is more specific: any paragraph, or paragraphs you opted in by name?

### Quick Check 4.3 ✅

1. Three styling requests arrive. Every page's footer needs the same background. Five paragraphs across three pages need deadline styling. The one announcements banner, which exists only on the home page, needs a highlight. Assign each request a selector kind and defend the calls.
2. A teammate names a class `.orange-box`. The club rebrands to green next term. Explain what breaks, what does not, and what the class should have been named.
3. You add `class="deadline"` to a paragraph, save, and refresh, and nothing changes. The attribute is spelled correctly. What is missing?

---

## 4.4 Color Systems and Validating Your CSS

Every example so far has leaned on two properties. This section makes them official, gives you three ways to write their values, and hands the club its palette. Then it closes the loop your Chapter 2 habit opened: a validator for your styles, and a lesson in what browsers do with CSS they cannot read.

### Two Properties for Color

The `color` property sets an element's text color. The `background-color` property paints the area behind it. The pack's practice stylesheet uses both to set a site-wide base, because `body` is an element selector like any other, and every visible element sits inside it:

```css
body {
    background-color: #fac78d;  /* light sand */
    color: #333333;             /* ink, from the palette's passing list */
}
```

Neither property is reserved for `body`. Any element can carry a background, which is how this same stylesheet lifts its paragraphs onto white panels with `p { background-color: #ffffff; }`, and how the lab's landmarks get their regions of teal.

Treat the two properties as a pair when you design. Text you can barely read against its background is a defect, whatever the markup says. That is why the club's palette file lists the text-on-background pairings that pass the web's accessibility bar for body text. Ink on light sand, the pairing in the rule above, is on the list. Chapter 9 teaches how that bar is measured. For now, trust the list, and treat any pairing missing from it as one that has not earned a place.

### Three Ways to Write a Color

CSS accepts color values in several systems, and this course teaches three.

A **color name** is a predefined keyword: `teal`, `white`, `tomato`. CSS defines more than 140 of them, and they are perfect for quick tests, since nobody misremembers `white`.

Their limit is precision, and here the club learns it the hard way. CSS's named `teal` is the exact color `#008080`. The club's teal is `#268080`. Close, and close is not the brand.

A **hex color** is the industry workhorse: a `#` followed by six characters, read as three pairs, one each for red, green, and blue light. Each pair runs from `00` (none of that light) to `ff` (all of it). So `#268080` is a little red plus matching mid-level green and blue, which mix to the logo's teal, and `#ffffff` is every channel at full, which is white. Hex is what design tools export, what palette files record, and what you will copy and paste for the rest of your career.

Practice the read on the palette's sunset orange, `#f4a259`. The `f4` puts red near full, `a2` holds green to a middle level, and `59` keeps blue low. Heavy red, moderate green, little blue: a warm orange. Nobody computes exact colors in their head. Ranking light against dark from the digits, though, is a skill worth having, and Try It Yourself 4.4 locks it in.

**RGB** is the color model both of those spell: every screen color is a mix of red, green, and blue. CSS can state the mix directly through the `rgb()` function, with each channel from 0 to 255. One brand teal, two exact spellings:

```css
h2 {
    color: #268080;             /* the club's exact brand teal */
}

h2 {
    color: rgb(38, 128, 128);   /* the same brand teal in rgb() */
}
```

One name to bank for the wild: CSS also offers `hsl()`, which describes colors by hue, saturation, and lightness. You will meet it in DevTools on commercial sites long before you need to write it.

The club's palette ships in your pack as `assets/code/chapter-04/club-palette.txt`: eight site colors with exact hex values, a usage note apiece, and the passing contrast pairings. Every value was extracted from the illustration set's own generator, so the site and its art will always agree.

| Color | Hex | Where the set uses it |
| ----- | --- | --------------------- |
| club teal | `#268080` | The logo disk and every banner |
| deep teal | `#1a5e5e` | The logo's shading |
| sunset orange | `#f4a259` | The sky in every outdoor scene |
| light sand | `#fac78d` | The palest tone, from the sunlit sky |
| sand | `#deb887` | The desert ground under every scene |
| saguaro green | `#5e9959` | The cactus and bin green |
| ink | `#333333` | Text and outlines |
| white | `#ffffff` | Label plates and the logo's arrows |

The file also lists two prop browns from the set, labeled as lookalikes that sit close to sand and earned no job on the site. Choosing sand over them is a design decision, not a coin flip, and Skills Lab 4A's Part 3 stretch hands that judgment to you. Copy values from the file every time. The `teal` versus `#268080` lesson is exactly what retyping from memory costs.

### Try It Yourself 4.4: Read the Hex Before the Screen 🛠️

**Predict:** Rank these three palette values from lightest to darkest using only their pairs: `#fac78d`, `#268080`, `#1a5e5e`. Remember that pairs closer to `ff` mean more light.

**Run:** Open `practice-styles.css` in VS Code, which draws a small color swatch beside every color value in a CSS file. Paste each of the three values, one at a time, into the h1 rule's `color` declaration and watch the swatch. Undo your edits when you finish, and confirm the file matches the pack original.

**Explain:** In 1-2 sentences, explain which digits let you rank the three without a screen, and check your ranking against `club-palette.txt`'s names for these values.

### The CSS Validator

Chapter 2 built a habit: check your markup against the standard at validator.w3.org before you trust it. That validator reads HTML and never opens your stylesheet. Styles get their own checker, the **CSS validator**, run by the same W3C at [jigsaw.w3.org/css-validator](https://jigsaw.w3.org/css-validator/). It offers the same three doors as its HTML twin: by URL, by file upload, or by direct input, where you paste the stylesheet itself.

While your site lives on your laptop, direct input is your door: open the `.css` file in VS Code, select all, copy, paste, validate. The URL door starts mattering in Chapter 12, once the site has an address.

Why does this deserve a habit? Because of what browsers do with CSS they cannot parse: nothing. No error page, no warning, no message. A browser that meets a declaration it does not recognize skips it silently and renders on, the same forgiving shrug you watched it give broken markup in Chapter 2. Silence is kind to visitors and brutal to developers, because your only symptom is a page that looks subtly wrong.

Paste the pack's `practice-styles.css` into the direct input tab exactly as shipped, and the validator reports the message you want to see every time:

```text
Congratulations! No Error Found.

This document validates as CSS level 3 + SVG !
```

Now watch it catch what a browser swallows. This defect takes sharp eyes: every property name below is perfect, and the only flaw is a deleted semicolon at the end of line 8. The stylesheet's body rule now reads:

```css
body {
    background-color: #fac78d  /* light sand */
    color: #333333;             /* ink */
}
```

Validate that, and the report points somewhere unexpected:

```text
Sorry! We found the following errors (1)

URI : file://localhost/TextArea

Line : 9 body
       (Value Error : background-color (nullcolors.html#propdef-background-color))
       Missing a semicolon before the property name “color”
```

Read the report like a developer. It names a line (9), names the rule it sits in (`body`), and describes the problem in plain words: "Missing a semicolon before the property name." Every character of that is information the browser had and kept to itself.

But look closer. The mistake is on line 8, and the report says line 9. That is not a validator bug. It is how parsing works. Without the semicolon, the parser keeps reading line 8's value until line 9's `color` turns the declaration into nonsense, and that is where it finally objects. Bank the rule of thumb now, because it will save you twenty minutes someday. When a CSS error report points at a line that looks innocent, look one declaration up.

Make the clean report your shipping bar for styles, the same bar Chapter 2 set for markup. Skills Lab 4A requires it: three pages through the HTML validator, one stylesheet through this one, zero messages everywhere.

### Try It Yourself 4.5: Break a Declaration on Purpose 🛠️

Time to earn a validator report of your own. If your `cascade-practice.html` still carries the TIY 4.2 style block, remove it first so the external file is back in charge.

**Predict:** You will change line 13 of `practice-styles.css` from `color` to `colr`. Three predictions. What will the browser show when you refresh the page? What color does the heading fall back to with its own rule dead? And what will the validator's report say about a property that does not exist?

**Run:** Make the typo, save, and refresh `cascade-practice.html`. Note the heading's color and the complete absence of any complaint. Then paste the stylesheet into the CSS validator's direct input tab and read the report closely: the line it names, the rule it names, and the help it offers beyond a rejection. Fix the typo, revalidate, and leave the file clean.

**Explain:** In 1-2 sentences, explain where the heading's new color came from, and what the browser's silence would cost you in a 200-line stylesheet.

### Quick Check 4.4 ✅

1. A teammate claims `color: teal` and `color: #268080` are the same color, since both look teal. Check the claim with this section's facts.
2. A page looks right in the browser, yet the CSS validator reports one error in its stylesheet. Explain how both can be true at once.
3. The validator flags line 9 of your stylesheet, but line 9 looks correct. Name the likely defect and where you should look for it.

---

## 4.5 Summary and Retrieval 💡

### Key Concepts

* Separation of concerns splits the work: HTML says what content is, CSS says how it looks, and one stylesheet edit can restyle a whole site without touching content. The "plain" look of unstyled pages is the browser default styles, which your rules override.
* A CSS rule is a selector plus a declaration block, and each declaration pairs a property with a value, ending in a semicolon. CSS comments (`/* */`) document the why, and browsers skip them.
* CSS reaches a page three ways. An inline style styles one element. An internal stylesheet in a `<style>` element styles one page. An external `.css` file connected by `<link rel="stylesheet">` styles every page that links it, which makes it the professional default. When rules collide, the cascade breaks ties: inline wins, and among equals the later rule wins.
* Selectors set the aim. An element selector styles every one of these. A class selector (`.deadline`, opted in through the `class` attribute) styles some of these by role. An id selector (`#meeting-times`, through the unique `id` attribute) styles exactly this one. A selector list (`h1, h2`) shares one block. Names describe the content's role, never its appearance.
* Colors arrive as names (quick but imprecise), hex values (`#268080`, the industry workhorse, read as red-green-blue pairs), or `rgb()` mixes. The club's palette file carries the exact values and the text-on-background pairings that pass contrast, and pairings missing from its list have not earned that trust.
* Browsers silently skip declarations they cannot parse, so a broken stylesheet's only symptom is a page that looks subtly wrong. The CSS validator names what the browser swallowed, and a report that blames an innocent line usually means a missing semicolon one declaration up.

### Key Terms

See course glossary for full definitions

* separation of concerns, CSS rule, selector, declaration block, declaration, property, value, CSS comment, browser default styles (Section 4.1)
* inline style, internal stylesheet, style element, external stylesheet, link element, cascade (Section 4.2)
* element selector, selector list, class selector, class attribute, id attribute, id selector (Section 4.3)
* color name, hex color, RGB, CSS validator (Section 4.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Write a complete CSS rule from memory, then label its selector, declaration block, declaration, property, and value.
2. Name the three ways to connect CSS to a page and the reach of each. State which one professionals default to and why.
3. State the decision rule for choosing among element, class, and id selectors, and give one club-site example of each.
4. List the three ways this chapter wrote color values, and describe the moment a color name stops being good enough.
5. Describe what a browser does with a declaration it cannot parse, what the CSS validator does with the same declaration, and where to look when the validator's line number seems wrong.

---

## 4.6 Skills Lab 4A: Dress the Club's Site in Its Own Colors

**Goal:** Connect one external stylesheet to all three of the club's pages and dress the site in the club's own palette with element, class, and id selectors, validating markup and styles to zero messages.

**Dataset:** Provided files in `assets/code/chapter-04/` from the course data pack. `starter-site/` holds the club's finished three-page site: `recycling-guide.html`, `drive-gallery.html`, `contact.html`, and its `images` folder. `club-palette.txt` maps the design set's colors to exact hex values and lists the text-on-background pairings that pass contrast. `skills-lab-4a-answers.txt` is your written answers file. The folder's README documents every file. Work at the extracted `cis133` root, style the site without changing its structure, and copy every hex value from the palette file instead of retyping it.

The lab walks the chapter's own path. Part 1 connects one stylesheet to the whole site. Part 2 aims selectors at regions, groups, and one unique element. Part 3 hunts down styling in the wrong home and validates everything to zero.

### Part 1: Foundation (Aligns with MLO-4.1)

1. Copy the whole `starter-site` folder to your `cis133` root and rename the copy `skills-lab-4a-lastname`. Copy `skills-lab-4a-answers.txt` into it.
2. Create `club-styles.css` at the folder's top level, beside the three pages. Start the file with a CSS comment carrying the lab number, your name, and the date.
3. Connect the stylesheet to all three pages: one `<link rel="stylesheet" href="club-styles.css">` in each page's head.
4. Write the site's base: a `body` rule setting a background color and text color from the palette, as a pairing on the palette file's passing list. Save, then refresh all three pages and watch one file style the whole site.
5. Record your link element and why it belongs in the head in answer 1.A, and describe the three-page refresh in answer 1.B.

### Part 2: Application (Aligns with MLO-4.2)

1. Style the landmarks with element selectors: give the header, nav, and footer background colors from the palette, and set heading colors that read against their backgrounds. Every text-on-background pairing you create must appear on the palette file's passing list.
2. Create one class with a role-based name and apply it where the content warrants on at least two pages. The club's content offers candidates: a deadline, a key reminder, a callout.
3. Create one id for a genuinely unique element on one page, and style it.
4. Log every selector you wrote in answer 2.A, and justify the class call and the id call in answer 2.B.

### Part 3: Extension (Aligns with MLO-4.1, MLO-4.3)

1. One of the three pages carries exactly one leftover inline style. Hunt it down, move its declaration into a fitting rule in `club-styles.css`, and delete the attribute from the markup. Record the hunt in answer 3.A, including why the stylesheet is the better home.
2. Validate all three pages with the W3C HTML validator and `club-styles.css` with the CSS validator, repairing until every report shows zero messages. Log your results in answer 3.B, then add the critique no validator can make: name one thing about your styling that passes both validators but that you would still improve, and say why.
3. Stretch: make one more palette decision, such as a distinct link color or an accent background for one section. The palette file's two lookalike browns are fair game to weigh and reject. Defend your choice in a CSS comment above the rule, citing the palette file's passing list.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Cite the moment one edit to `club-styles.css` changed all three pages at once: what did you edit, and what changed where? Then estimate what the same site-wide change would have cost on a site styled with inline styles on every element. Ground your answer in your own Part 1 and Part 2 work.
2. The HTML validator passed all three of your pages before you wrote a single CSS rule, yet the CSS validator still found work for you during this lab or its Try It Yourself exercises. What does each validator check, and why does a professional run both before shipping?

**Submission:** Zip your `skills-lab-4a-lastname` folder containing your three HTML pages, your `images` folder, `club-styles.css`, and `skills-lab-4a-answers.txt`, and submit it as `skills-lab-4a-lastname.zip`. All three pages and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 4A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Code Accuracy and
Efficiency, Output Quality, Documentation and Code Comments, and
Analysis, Interpretation, and Response to QUESTION(s).

---

## 4.7 Review Questions 🔄️

1. **Remember:** Define the five anatomy terms of a CSS rule (selector, declaration block, declaration, property, value) and point at each part in one example rule you write.

2. **Understand:** A classmate styles every page of a five-page site with internal stylesheets. The pages look identical, so they see no problem. Explain what separation of concerns says about that choice, and what next month's redesign will cost them that an external stylesheet would not.

3. **Apply:** The tutoring center's site from Chapters 2 and 3 is adopting a stylesheet, and three requests came in. Every `h2` on every page gets the center's green. The "bring your student ID" reminder is highlighted on the three pages where it appears. The sign-up banner on the home page, and only there, gets a background. For each request, choose an element, class, or id selector, write the selector as it would appear in the stylesheet (inventing role-based names where needed), and give one reason apiece.

4. **Evaluate:** You inherit a stylesheet whose classes are named `.orange-box`, `.big-blue-title`, and `.left-text`, and it passes the CSS validator with zero errors. Judge whether the clean report makes this stylesheet well built. Critique the names against this chapter's naming law, predict what next year's rebrand does to them, and propose better names for any two.

---

## Further Reading 📖

* [MDN: What is CSS?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/What_is_CSS) - A beginner-level introduction to rules, selectors, and how CSS reaches a page, at exactly this chapter's depth.
* [web.dev: Learn CSS](https://web.dev/learn/css) - Google's free CSS course. The selectors and color modules extend this chapter with industry examples.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - The validator itself. Bookmark the direct input tab you used in this chapter.
* [CSS Zen Garden](https://csszengarden.com) - The classic proof that one HTML file can wear any design. Browse a few submissions and confirm the markup never changes.
* [MDN: named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) - The full list of CSS color keywords with swatches, including the `teal` this chapter measured against the club's own.

---

## Looking Ahead ⏩

The club's site wears its own colors now, and you probably noticed what is still missing: the text presses right against the edges of every colored region, and the pages want breathing room. Chapter 5 hands you the box model, CSS's system for space. The spacing Chapter 2 told you never to fake with `<br>` finally gets its real tools, margins and padding, in the same stylesheet you built this week. You can color boxes now. Next you control their space.
