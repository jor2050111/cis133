# Chapter 5: The Box Model and Typography

Skills Lab 4A sent the club's site to the meeting wearing its own colors, and the president studied every page. The verdict came in two parts. The colors are right. "But it still looks like a form, not a site." Look once and you see the complaint. Heading text presses against the edges of the teal header. The reminder hugs its orange panel. Lines of body text run the full width of the window. Every region ends exactly where its words do, and nothing gets room to breathe.

Chapter 4's Looking Ahead promised this chapter would fix that, and the fix starts with a change of eyesight. The browser treats every element you have ever written as a rectangular box with four measurable layers, and CSS sets each layer by name. Space is not something the browser dispenses on a whim. It is a property you declare. The same goes for the site's type, because the club's pages still speak in the browser's default font at the browser's default sizes. Those are two more defaults you now know how to override.

This chapter works in that order. You will read a box from the inside out and X-ray any element with the browser DevTools box-model diagram. You will space the club's regions with padding and margin, written one side at a time or in shorthand. You will build font stacks that survive any visitor's machine and set sizes that respect the reader. You will finish with a four-point checklist that turns "readable" from an opinion into a diagnosis. Same three pages, same `club-styles.css`. One chapter of space and type.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapter 4 (CSS rules and selectors, external stylesheets, the club palette, and the CSS validator habit)
* **Deliverables:** Skills Lab 5A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-5.1 (Apply):** Control the space inside and around elements with padding, border, and margin, using individual and shorthand syntax
* **MLO-5.2 (Apply):** Style text with font stacks, sizes, and text properties chosen for readability
* **MLO-5.3 (Analyze):** Diagnose spacing and readability problems with the DevTools box-model diagram and the chapter's typography guidelines

---

## 5.1 Every Element Is a Box

Chapter 2 sorted elements into two kinds: block-level elements that stack like bricks, and inline elements that flow along inside a line. The brick language was never a metaphor. To the browser, every element is a rectangular box, and the **box model** is its map of that box: four layers it measures and you control.

### The Four Layers, Inside Out

Start at the center. The content is the text or image the box exists to hold. Around it sits **padding**, open space between the content and the border that still belongs to the element's own body. Around the padding runs the **border**, a drawn line with a width, a style, and a color of its own. Outside the border lies the **margin**, transparent space the element claims to keep its neighbors at a distance.

One fact makes the layers easy to tell apart on screen. An element's background color paints its content and its padding, stops at the border, and never touches the margin. Padding is space inside the paint. Margin is space outside it.

The numbers are yours to set. Your data pack ships a practice pair for this chapter, `assets/code/chapter-05/box-practice.html` and `box-practice.css`, which styles three club announcements as boxes you can measure. Here is the first box's rule, exactly as shipped:

```css
.event-notice {
    width: 300px;
    padding: 24px;
    border: 3px solid #268080;  /* club teal frames the event */
    margin-bottom: 16px;
    background-color: #ffffff;
}
```

Every layer answers to a property. The padding declaration opens 24 pixels between the announcement's text and its teal frame, on all four sides. The margin declaration pushes the next element 16 pixels away, below only. Section 5.2 unpacks the border value and the rest of the syntax. First, a discovery about space you never wrote.

### The Space You Never Wrote

Your pages have carried spacing since Chapter 2, long before you wrote a line of CSS. Blank lines in your files collapse, yet paragraphs still render with clear gaps between them. Page content starts a small distance in from the window's edge, though you never asked for that either. Chapter 4 named the author of both effects: the browser default styles. The browser's own stylesheet ships margins of its own, and margins you never wrote are still margins. Which element carries the one at the window's edge? Try It Yourself 5.1 sends you after it with the right instrument.

The point is not trivia. Your rules override the browser's spacing the same way your colors overrode its gray. When a gap on your page looks wrong, some rule put it there, and you can find out which one.

### The Box-Model Diagram: Your X-Ray

Finding out is a DevTools job. Right-click any element and choose Inspect, the move you learned in Try It Yourself 4.1. Beside the markup, scroll the styling information down and you will meet a colored diagram of nested rectangles: content at the center, then padding, border, and margin, each side labeled with its current number. If you do not see it, look for a tab named Computed or Layout.

The diagram never guesses. It reports the box the browser drew, layer by layer, whatever your CSS asked for. When a region looks cramped, you could stare at the stylesheet and re-guess. The diagram ends the argument in one glance, which is why Skills Lab 5A grades you on reading it.

### Padding or Margin?

Every box-model beginner hits the same decision again and again: the design needs space, so which layer gets it? The paint rule settles most cases.

* Space that should wear the region's color lives inside the paint. That is padding. The reminder text touching its orange panel's edge is a padding problem.
* Space that should separate an element from its neighbors lies outside the paint. That is margin. Two figures crowding each other is a margin problem.

Chapter 2 caught you wanting space between paragraphs, banned `<br>` as the tool, and promised the real one would arrive with CSS. Here it is, paid in full. The space between elements is margin: one declaration in a stylesheet, and not one change to the markup.

### Try It Yourself 5.1: Find the Frame 🛠️

Open `assets/code/chapter-05/box-practice.html` in your browser and `box-practice.css` in VS Code. The stylesheet gives `body` two colors and nothing else. No rule in the file mentions a margin on it.

**Predict:** The white announcement boxes still stop short of the window's left edge. Which element owns that gap, and which of its four layers holds it?

**Run:** Right-click the first announcement box and choose Inspect, then find the box-model diagram. Read its numbers against the `.event-notice` rule: 24 of padding, 3 of border, 16 of margin below. Now select the `body` element in the markup panel and read its diagram. The margin layer carries a number no file of yours wrote, and the styles listing traces it to the same "user agent stylesheet" you met in Chapter 4.

**Explain:** In 1-2 sentences, name the stylesheet that spaced your page and explain how the diagram proved it.

### Quick Check 5.1 ✅

1. List the four box-model layers from the inside out, and name the one an element's background color never reaches.
2. A caption's words touch its figure's sand border, and the figure itself presses against the paragraph above it. Name the layer that fixes each problem, using the paint rule.
3. Your Chapter 3 pages showed gaps between paragraphs even though blank lines collapse and you had written zero CSS. Where did those gaps come from, and what happens to them once your own stylesheet says otherwise?

---

## 5.2 Spacing Syntax: Individual and Shorthand

You can read a box's layers. This section teaches you to set them: first one side at a time, then in the shorthand professionals reach for. It ends at the scale of the whole page, where widths, centered columns, and one famous accounting surprise live.

### One Side at a Time

Padding and margin each come in four single-side properties, named for the side they set: `margin-top`, `margin-right`, `margin-bottom`, and `margin-left`, with padding following the same pattern.

```css
/* Room above and below every figure, one side at a time. */
figure {
    margin-top: 24px;
    margin-bottom: 24px;
}
```

Single-side properties shine when you mean one side. The practice file's `margin-bottom: 16px` spaces each announcement from the next without adding stray space above the first one. When all four sides need values, four separate declarations start to feel like typing the same word four times. CSS agrees.

### The Shorthand Clock

A **shorthand property** sets several longhand properties in one declaration. For padding and margin, the shorthand is the bare property name with up to four values. Four values travel clockwise from the top, the way a clock's hand sweeps: top, right, bottom, left.

```css
/* Clockwise from the top: 24 top, 32 right, 16 bottom, 32 left. */
main {
    padding: 24px 32px 16px 32px;
}
```

Two shorter forms cover most declarations you will write. When top matches bottom and left matches right, two values do the work: vertical first, then horizontal. When all four sides match, one value sets them all, which is what the first box's `padding: 24px` did.

```css
/* Two values: 8 top and bottom, 20 left and right. */
.callout {
    padding: 8px 20px;
}
```

The practice file's third box, `.donation-tip`, uses the two-value form for both padding and margin. Learn the clock once and shorthand stops being cryptic. Try It Yourself 5.3 has you prove it against the diagram, on numbers of its own.

### Borders: Width, Style, Color

A border is a drawn line, so it takes three decisions: how thick, what kind of line, and what color. Each decision has a longhand property, and the **border shorthand** takes all three in one declaration, in that order.

```css
/* Longhand: three decisions, three declarations. */
figure {
    border-width: 3px;
    border-style: solid;
    border-color: #deb887;
}

/* Shorthand: the same border in one line: width, style, color. */
figure {
    border: 3px solid #deb887;  /* sand frames each figure plate */
}
```

`solid` is the style you will use most. `dashed` and `dotted` exist, and this course leaves them to your experiments. Borders also come one side at a time, which turns them into accents:

```css
/* An accent along one edge only. */
#meeting-times {
    border-left: 6px solid #268080;  /* club teal marks the schedule */
}
```

### The Readable Column and the Width Surprise

Block-level elements claim the full width of their container, which is why the club's text runs edge to edge on a wide monitor. Long lines exhaust readers, because every line ends with an eye trip back across the screen. The `width` property sets an exact width, and it is usually the wrong tool for text: a box fixed at 640 pixels overflows a phone screen nowhere near that wide. **max-width** makes the promise you mean. Never wider than this, and free to shrink.

Pair it with a margin trick. The value `auto` asks the browser to compute a margin for you, and `margin: 0 auto` (zero top and bottom, auto left and right) splits the leftover horizontal space evenly. The box centers itself.

```css
/* The readable column: never wider than 640px, and centered
   whenever the window is wider than that. */
main {
    max-width: 640px;
    margin: 0 auto;
}
```

That pair is the classic readable-column pattern, and Chapter 8 teaches the column to adapt itself to any screen. Now for the surprise.

The practice file's first box declares `width: 300px`, yet its diagram reports 354 pixels across. That is not a bug. By default, `width` sets the content layer only, and padding and border are added on top of it. The box carries 24 of padding and 3 of border per side: 300 + 48 + 6 = 354. The declared width is an opening bid, not the finished box, and margin sits outside the total entirely.

Developers spent years doing that arithmetic backward from broken layouts, and CSS eventually shipped a fix. The **box-sizing** property decides what `width` measures. Its `border-box` value makes width cover content, padding, and border together, so the number you declare is the box you see:

```css
/* Width now means the whole visible box, padding and border
   included. Professional stylesheets open with this rule. */
* {
    box-sizing: border-box;
}
```

The `*` at the front is the **universal selector**, which matches every element on the page, and delivering this one rule is most of what you will ever see it do. With the rule in place, all three practice boxes render an even 300 pixels wide, and padding carves space inside that total instead of growing it. Skills Lab 5A makes this rule the first line of the club's stylesheet, and every stylesheet you write from now on should start the same way.

### Try It Yourself 5.2: The Width Surprise 🛠️

**Predict:** `.volunteer-call` declares the same `width: 300px` as `.event-notice`, but carries 12 of padding and 6 of border per side. Compute its total rendered width. Will the two boxes render the same?

**Run:** Inspect both boxes and read their box-model diagrams against your math. Then add the `* { box-sizing: border-box; }` rule to the top of `box-practice.css`, save, refresh, and measure both boxes again. Leave the rule in place, since the lab makes the same move on the club's site.

**Explain:** In 1-2 sentences, explain what `width` measured before the rule and what it measures after, using the diagram's numbers as evidence.

### Try It Yourself 5.3: Prove the Clock 🛠️

**Predict:** The third box's rule says `padding: 12px 24px` and `margin: 16px 32px`. Write the four-line longhand expansion of each declaration, all eight values.

**Run:** Inspect the third announcement box and read the diagram's padding and margin layers, side by side against your predictions.

**Explain:** In 1-2 sentences, state the rule that maps two shorthand values onto four sides, and name which sides each value reached.

### Quick Check 5.2 ✅

1. A teammate writes `padding: 16px` expecting padding on the top only. What did the declaration set, and how should the top-only version be written?
2. In `margin: 0 auto`, say what each of the two values does, and name the property that must also be set on the element before the centering works.
3. A box declares `width: 400px`, `padding: 20px`, and `border: 5px solid`. Give its rendered width under the browser's default sizing, and under `box-sizing: border-box`.

---

## 5.3 Choosing Fonts

Space was half the president's complaint. The other half is type. Every page you have shipped so far speaks in the browser's default font, one more default style you have now learned to see. The property that changes it is `font-family`, and its value has a shape worth understanding before you write one.

### Font Stacks: First Choice, Backup, Safety Net

Here is the catch that shapes everything: a font renders only if the visitor's device can supply it, and you do not control the visitor's device. A font you take for granted may not exist on a five-year-old tablet or a locked-down lab machine. So `font-family` takes a list, called a **font stack**: fonts in order of preference, first choice first. The browser walks the list left to right and uses the first font it can supply.

The last entry is the safety net. A **generic font family** is a category instead of a font. `serif` means letters with small finishing strokes, the printed-book look. `sans-serif` means letters without them, the cleaner screen look. `monospace` gives every character the same width, the code look. The browser always owns a font in each category, so a stack that ends in one can never come up empty.

```css
/* First choice, a close backup, then the safety net. Quote any
   font name that contains spaces. */
body {
    font-family: Georgia, "Times New Roman", serif;
}
```

Two conventions ride along: most specific first and generic last, and quotes around any font name with spaces in it. Stack lookalikes together, so the second choice honors the design of the first. A **web-safe font** is one so widely installed you can treat it as everywhere. Arial, Verdana, Georgia, and Times New Roman lead that list, which is why they anchor so many stacks. One `body` rule is enough to set the whole site's type, because font settings flow down into every element inside the body, a behavior called inheritance that later chapters put to work.

### Sizing Type: px and rem

**font-size** sets how large text renders, and its two everyday units make different promises. A pixel value is fixed: `font-size: 16px` renders at sixteen pixels for every visitor, whatever their settings say. A **rem** is relative: `1rem` equals the visitor's own base text size, the one their browser settings choose, so `1.5rem` means one and a half times whatever the reader picked.

```css
p {
    font-size: 16px;    /* fixed: the same for every visitor */
}

h2 {
    font-size: 1.5rem;  /* relative: 1.5 times the visitor's base */
}
```

Rem sizes respect a visitor who raised their base size to read comfortably, which is why they matter to accessibility, and Chapter 9 measures that respect properly. For now, know what each unit promises and use either in your work. (A related unit named `em` exists, resizes against a different base, and can wait.)

Sizing in hand, Chapter 2's oldest styling promise closes. You were told to pick a heading's level by its rank and leave its size to CSS. This is the final installment: when an `h2` renders bigger than the design wants, the fix is a `font-size` declaration, never a demotion to `h3`. Structure states what the heading is. CSS states how big it looks.

### Weight and Style, Without Stealing Meaning

Two more properties finish the set. **font-weight** sets how heavy the strokes render, with `bold` as its everyday value, and **font-style** slants the letters with its `italic` value. Both are looks, and Chapter 3 already assigned the meanings. Content the reader must not miss is `<strong>`, whatever it looks like. Stressed words are `<em>`. A caption you want italic purely for style is a one-declaration job: `figcaption { font-style: italic; }` changes the look and claims no meaning.

The division of labor protects the readers who never see pixels. Devon's screen reader reads the markup's meaning and never opens the stylesheet. Style with CSS freely. Mark meaning in HTML, always.

### Borrowed Type: Google Fonts

Stacks built on installed fonts limit you to a short shared list. Google Fonts ([fonts.google.com](https://fonts.google.com)) is a free library of fonts your pages can borrow: the browser downloads the font when the page loads, so the visitor does not need it installed. Browse the library, pick a font, and the site hands you markup to paste. This course uses the single-link form. Here it is for Oswald, a condensed sans that suits headings, placed in the head beside the stylesheet link:

```html
<head>
    <meta charset="UTF-8">
    <title>Contact | PC Computer Club</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400..700&display=swap">
    <link rel="stylesheet" href="club-styles.css">
</head>
```

Google's embed panel currently hands out a three-link version of the same connection. Both forms work, and the single link keeps the lesson in one line. The link delivers the font, and your stack decides to use it. Keep the stack honest: back a borrowed font with installed fonts of the same character, so the design degrades gracefully if the download ever fails.

```css
/* Oswald is a condensed sans, so its backups stay sans. */
h1, h2 {
    font-family: "Oswald", Arial, sans-serif;
}
```

When Chapter 12 publishes the site, the link element travels in the head like any other markup, and the borrowed font travels with it.

### Try It Yourself 5.4: Break a Stack on Purpose 🛠️

Run this one on `box-practice.css`.

**Predict:** You will give the practice page the stack `Verdana, Arial, sans-serif`, then sabotage it in two stages. First you will misspell Verdana. Which font catches the text? Then you will delete every entry except the misspelled name. Does the browser keep Arial, report an error, or do something else?

**Run:** Add `font-family: Verdana, Arial, sans-serif;` to the `body` rule and refresh. Change `Verdana` to `Verdanna` and refresh: Verdana runs wide, so watch the lines tighten as the fallback catches them. Now make the whole value `Verdanna` alone and refresh once more. The text falls back to the browser's own default, the font your Chapter 2 pages wore. Undo your edits when you finish.

**Explain:** In 1-2 sentences, explain what the generic family was buying you, and who chose the final font once your stack ran out of real names.

### Quick Check 5.3 ✅

1. Every professional font stack ends in a generic family. What does that last entry guarantee, and what happens on a machine that owns none of the named fonts?
2. A teammate's `h2` headings render bigger than the design calls for, so they change the markup to `h3`. Critique the move with Chapter 2's rule, and write the one-line fix that respects it.
3. State what `1rem` measures, and explain which visitors a rem-sized page respects that a pixel-sized page ignores.

---

## 5.4 Text Properties and Readable Typography

Fonts chosen, one property family remains: the text properties that control alignment, casing, decoration, and the room between lines. Then everything this chapter taught becomes one checklist.

### Aligning and Transforming Text

**text-align** sets how lines sit inside their box: `left`, `center`, or `right`. Body text in English reads best where the browser starts it, on the left, with a ragged right edge. Centering earns its keep on short display lines, like a page title or a caption. One value is a trap: `justify` squares both edges the way print does, but browsers justify by stretching the spaces between words, and they do not hyphenate. The stretched gaps stack into distracting rivers of white space. Leave justification to print.

**text-transform** recases text for display: `uppercase`, `lowercase`, or `capitalize`. The win is the usual one. The look lives in the stylesheet while the markup keeps normal casing, so a redesign never means retyping content. Uppercase suits short labels, like a compact heading. Whole sentences in caps read like shouting and slow the eye. Label, yes. Paragraph, never.

```css
h1 {
    text-align: center;         /* a short display line, centered */
}

h2 {
    text-transform: uppercase;  /* short labels wear caps well */
}
```

### Underlines Carry Meaning

**text-decoration** controls the lines drawn under and through text. Its famous value is `none`, because the web underlines every link by default and generations of developers have itched to remove that:

```css
/* Tempting, and costly: the underline is the link's uniform. */
a {
    text-decoration: none;
}
```

Resist, at least for links inside body text. The underline there is not decoration. It is the signal that says "this is a link," and it works for every visitor, including colorblind visitors a color change alone would strand. Strip it and your links dress like ordinary words. Navigation bars may drop underlines by convention, because their position announces what they are, and Chapter 6 styles the club's nav properly. (The club's footer links still wear the browser's default blue on deep teal, a pairing Chapter 6's sharper selectors will finally fix.)

### line-height: Room Between Lines

Padding spaced the box. **line-height** spaces the text itself, setting the vertical room each line occupies. Write it unitless and the number multiplies the element's own font size, whatever that size turns out to be:

```css
/* Unitless 1.5: each line gets 1.5 times its own text size. */
body {
    line-height: 1.5;
}
```

Browser defaults run tighter than that, which suits a short label and fatigues over a paragraph. For body text, 1.5 is the readable default this course uses. Headings, short and large, usually want less.

### The Readability Checklist

You now hold every tool this chapter promised, so here is the discipline for using them. Readable typography is a design decision you can check point by point, not a feeling. Four points, one property apiece:

| Checklist point | What passes | The CSS that controls it |
| --- | --- | --- |
| Contrast | Every text-on-background pairing appears on the palette's passing list | `color`, `background-color` |
| Size | Body text no smaller than the browser's own default | `font-size` |
| Line height | Body text around 1.5 | `line-height` |
| Line length | Lines end before the eye loses its way back, capped by a column | `max-width` |

The palette's passing list has guarded contrast since Chapter 4, and Chapter 9 teaches the math behind it. The other three points are new powers, which means three new ways to hurt a reader without one invalid declaration. The checklist runs in both directions: design with it, then diagnose with it. Skills Lab 5A asks for both.

### Try It Yourself 5.5: Diagnose the Drive Notes 🛠️

The practice page saves its worst region for last, and it is cramped on purpose.

**Predict:** The Drive Day Notes section at the bottom of `box-practice.html` renders ink text on a white panel: 12.63 to 1, the strongest pairing on the palette's list. Its stylesheet validates with zero messages. Can the region still be hard to read? Before looking, predict which of the four checklist points it violates.

**Run:** Open the page and read the section, then run the checklist against the `.drive-notes` rule in `box-practice.css`. Score all four points: contrast, size, line height, line length. Then fix exactly one violated point with one declaration, refresh, and judge how far the single fix carried the region.

**Explain:** In 1-2 sentences, explain how a region can pass the validator and the contrast list and still fail its readers, and name the box-model defect the rule hides beyond the four points.

### Quick Check 5.4 ✅

1. A teammate wants clean edges on both sides of every paragraph and proposes `text-align: justify`. Predict the result on the web, and name what it costs the reader.
2. The club wants its short section headings in caps. Compare typing the headings in caps in the HTML against `text-transform: uppercase` in the stylesheet: which survives a redesign, and why?
3. A page passes every contrast pairing, yet readers on wide monitors complain they keep losing their place between lines. Which two checklist points do you examine first, and which property fixes each?

---

## 5.5 Summary and Retrieval 💡

### Key Concepts

* Every element is a box with four layers: content, padding, border, margin. Background color paints content and padding and stops at the border, so space inside the paint is padding and space between neighbors is margin. The browser default styles include margins you never wrote, and your rules override them.
* The DevTools box-model diagram reports every layer of any element's box, which turns "this looks wrong" into numbers you can read. It is the diagnosis tool this chapter and its lab lean on.
* Padding and margin come one side at a time or in shorthand: four values clockwise from the top, two values as vertical then horizontal, one value for all sides. The border shorthand takes width, style, and color, and single-side borders make accents.
* By default `width` sets the content layer only, so padding and border grow the rendered box: a declared 300 can render 354. `box-sizing: border-box`, delivered by the universal selector, makes width mean the visible box. `max-width` plus `margin: 0 auto` builds the centered readable column.
* A font stack lists fonts in order of preference and ends in a generic family the browser can always supply. Sizes come fixed in px or relative in rem, and bold and italic looks stay in CSS while meaning stays with `<strong>` and `<em>`. Google Fonts lends fonts through one link element, backed by an honest stack.
* Readability is a four-point diagnosis: contrast, size, line height, line length. A region can validate cleanly, pass contrast, and still fail its readers.

### Key Terms

See course glossary for full definitions

* box model, padding, border, margin (Section 5.1)
* shorthand property, border shorthand, max-width, box-sizing, universal selector (Section 5.2)
* font stack, generic font family, web-safe font, font-size, rem, font-weight, font-style (Section 5.3)
* text-align, text-transform, text-decoration, line-height (Section 5.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. List the box model's four layers from the inside out, and state which layers an element's background color paints.
2. Expand `padding: 12px 24px` into its four longhand declarations, then state the order in which four-value shorthand travels.
3. Explain how a box declaring `width: 300px` can render 354 pixels wide, and write the rule that prevents the surprise site-wide.
4. Write a body font stack from memory that ends in a generic family, and state the job of each position in it.
5. Recite the four-point readability checklist and pair each point with the CSS property that controls it.

---

## 5.6 Skills Lab 5A: Give the Club's Site Breathing Room

**Goal:** Space the club's site with the box model and set its typography so every page reads comfortably, diagnosing your own spacing with the DevTools box-model diagram.

**Dataset:** Provided files in `assets/code/chapter-05/` from the course data pack. `starter-site/` holds the club's three pages (`recycling-guide.html`, `drive-gallery.html`, `contact.html`), the stylesheet Skills Lab 4A built (`club-styles.css`), and the `images` folder, all validating with zero messages. `club-palette.txt` travels with every CSS chapter, copied unchanged from the Chapter 4 pack. `skills-lab-5a-answers.txt` is your written answers file, and the folder's README documents every file. Work at the extracted `cis133` root and copy every hex value from the palette file.

The lab walks the chapter's own path. Part 1 spaces the regions, Part 2 builds the readable column and sets the site's type, and Part 3 borrows a heading font and closes with a DevTools diagnosis.

### Part 1: Foundation (Aligns with MLO-5.1)

1. Copy the whole `starter-site` folder to your `cis133` root and rename the copy `skills-lab-5a-lastname`. Copy `skills-lab-5a-answers.txt` into it.
2. Set the site's sizing baseline: add `* { box-sizing: border-box; }` at the top of `club-styles.css`, below the file comment, with a comment saying what it makes `width` mean.
3. Space the regions. Give the header, nav, and footer padding so their text stops pressing against their colored edges. Pad the `.reminder` and `#meeting-times` panels the same way. Give the figures margins where they crowd their neighbors.
4. Write at least one of those rules with a two-value or four-value shorthand, and say in a comment which sides it reaches.
5. Record one region's before and after in answer 1.A, with the rule that made the difference, and your shorthand's four-line expansion in answer 1.B.

### Part 2: Application (Aligns with MLO-5.1, MLO-5.2)

1. Build the readable column: give `main` a `max-width` and center it with auto margins. Justify your chosen width in answer 2.A.
2. Add at least one border where the design warrants it, such as a frame for the figure plates or an accent along one panel's edge. Palette colors only.
3. Set the site's type: a body font stack ending in a generic family, font sizes for body text and headings, and a body `line-height`. Every text-on-background pairing you touch must stay on the palette file's passing list.
4. Log your stack, its generic family, and your sizes and line-height in answer 2.B, with one reason apiece.

### Part 3: Extension (Aligns with MLO-5.2, MLO-5.3)

1. Borrow one Google Font for the site's headings using the single-link form from Section 5.3, back it with an honest fallback stack, and defend the pick in a CSS comment above the rule.
2. Run a diagnosis. Find one element on any page whose spacing still looks wrong, transcribe its box-model diagram numbers into answer 3.A, name the layer at fault, and fix it with the fewest declarations that solve it.
3. Validate everything: all three pages through the W3C HTML validator and `club-styles.css` through the CSS validator, repairing until every report shows zero messages. Log the results in answer 3.B and finish with the critique no validator can make: one thing about your styling you would still improve, and why.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Judge your finished site against the chapter's four-point readability checklist: contrast, size, line height, and line length. Cite one checklist item your work satisfies, name the exact rule in `club-styles.css` that satisfies it, and explain how the page reads differently because of it.
2. Tell the story of your Part 3 diagnosis: what the box-model diagram showed for your chosen element, and why the browser was doing exactly what your CSS told it to do. Close with what the diagram gave you that guess-and-refresh could not.

**Submission:** Zip your `skills-lab-5a-lastname` folder containing your three HTML pages, your `images` folder, `club-styles.css`, and `skills-lab-5a-answers.txt`, and submit it as `skills-lab-5a-lastname.zip`. All three pages and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 5A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Code Accuracy and
Efficiency, Output Quality, Documentation and Code Comments, and
Analysis, Interpretation, and Response to QUESTION(s).

---

## 5.7 Review Questions 🔄️

1. **Remember:** Name the four box model layers from the inside out. State which layers an element's background color paints, and which layer holds the space between neighboring elements.

2. **Understand:** Explain why `font-family` takes a list instead of a single font. Using `Georgia, "Times New Roman", serif` as the example, state what each position contributes and what happens on a machine with neither named font installed.

3. **Apply:** The tutoring center's site from earlier chapters wants breathing room too, and three requests came in. The pages need a centered reading column no wider than 640 pixels. Body text needs comfortable room between lines. The "bring your student ID" reminder needs space between its text and the edges of its highlight panel. Write the rule or declaration that answers each request, inventing role-based names where needed, and give one reason apiece.

4. **Analyze:** A clubmate complains: "I gave the announcement box `margin: 24px`, and the text still touches the box's edge." The box-model diagram shows content 300 wide, padding 0 on every side, border 3, margin 24. Diagnose the defect: name the layer they aimed at, the layer their complaint is about, and the fix. Then explain what the diagram settled that another round of guess-and-refresh could not.

---

## Further Reading 📖

* [MDN: The box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model) - The reference walk through content, padding, border, and margin, at exactly this chapter's depth.
* [web.dev: Box model](https://web.dev/learn/css/box-model) - Google's Learn CSS module on the box model, including the width accounting this chapter measured.
* [MDN: Fundamentals of text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals) - Font stacks, sizes, weights, and styles, with worked examples.
* [MDN: line-height](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height) - The property reference, including why unitless values are the safe choice.
* [Google Fonts](https://fonts.google.com) - The font library itself. Browse, pick, and copy the link markup you used in this chapter.

---

## Looking Ahead ⏩

The club's site can breathe now, and its type is chosen instead of inherited. One structure is still wearing a disguise: the nav is a bulleted list in colors, and Chapter 4 promised it would become a real navigation bar. Chapter 6 pays that oldest debt with Flexbox, CSS's system for arranging boxes side by side, plus selectors sharp enough to style the links inside one region without touching another's. You can space and dress boxes now. Next you arrange them.
