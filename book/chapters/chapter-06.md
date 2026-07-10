# Chapter 6: Layout with Flexbox

Skills Lab 5A sent the club's site back to the president wearing space and chosen type, and the pages finally read like pages. Stand back from the screen, though, and one old habit shows. Every element still stacks in a single column, one box per line, exactly as blocks have stacked since Chapter 2. The logo sits above the title. The gallery's figures wait in a patient tower. And the nav is still a bulleted list wearing site colors, even though Chapter 4 promised it would become a real navigation bar.

There is also a defect on the record, in the lab's own paperwork. Lab 5A's critique line, the one thing no validator can see, named the footer's links. They render the browser's default link blue on deep teal, a pairing that fails the accessibility bar by a wide margin. The site has carried that wart since Lab 4A. Chapter 5 could not fix it honestly, because the selectors you owned would repaint every link on the site to reach three of them.

This chapter pays both debts. You will turn a stacked container into an arranged line with one declaration. You will control that line: where items sit, how they space themselves, and what happens when they run out of room. You will write selectors that reach the links inside one region and leave every other link alone. Then you will assemble the navigation bar from parts you already own. Skills Lab 6A completes the Part II milestone: a multi-section site with an external stylesheet, controlled spacing and type, and a Flexbox navigation bar.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapters 4-5 (selectors and stylesheets, the box model, and the club site's styled pages)
* **Deliverables:** Skills Lab 6A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-6.1 (Apply):** Arrange page content with flex containers, controlling alignment, spacing, and wrapping along the main and cross axes
* **MLO-6.2 (Analyze):** Differentiate elements by tree relationship and interaction state to scope styles with descendant combinators and accessible pseudo-classes
* **MLO-6.3 (Apply):** Construct an accessible navigation bar from the semantic nav list using Flexbox, combinators, and pseudo-classes

---

## 6.1 The Flexbox Model

Every layout you have shipped so far used the browser's one built-in arrangement. Block-level elements stack, one per line, top to bottom, exactly as Chapter 2 described. You have colored those boxes, spaced them, and set their type. You have never once placed two of them side by side. That is the missing tool, and CSS ships a whole system for it.

### One Declaration, Two New Roles

**Flexbox** is CSS's system for arranging elements along a line. You switch it on with a single declaration, and the declaration goes on the parent:

```css
/* The parent becomes the container. Its direct children, and
   only those, become the items it arranges. */
.officer-roster {
    display: flex;
}
```

That one line hands out two new roles. The element carrying `display: flex` becomes a **flex container**, the element in charge of the line. Its direct children become **flex items**, the boxes the container arranges. The word direct matters. Children of children keep their normal behavior, so a paragraph inside a card inside the container is not an item. The card is.

Chapter 3's tree vocabulary earns its keep here. Before you flex a container, read its markup and name its children, because those children, and nothing deeper, are what will move.

### Two Axes, One Direction

A flex container lays its items along its **main axis**. Perpendicular to it runs the **cross axis**. The **flex-direction** property chooses where the main axis points:

```css
/* row is the default: you get it without writing it. column
   turns the main axis vertical. */
.officer-roster {
    display: flex;
    flex-direction: column;
}
```

With `row`, the main axis runs horizontally and the cross axis runs vertically. With `column`, the two trade places. Every control in the next section speaks this axis language instead of saying left, right, top, or bottom. That is why the vocabulary comes first: learn it for rows and you already own it for columns.

### The Practice Bench: The Announcement Board

Your data pack ships this chapter's bench: `assets/code/chapter-06/flex-playground.html` and `flex-playground.css`, which sit side by side so the page's relative `href` finds the stylesheet. The page is the club's announcement board, a `div` carrying the class `announcement-board` and holding four `section` cards headed ONE through FOUR. The board's title sits outside the div on purpose, so the container has exactly four children. Each card is 220 pixels wide under the border-box baseline, and the cards carry no margins. TWO holds the longest text and FOUR the shortest, which will matter soon.

The board's rule ships with a background, a border, padding, and no layout declarations at all. Every experiment in this chapter starts by adding one there.

### Try It Yourself 6.1: Flip the Switch 🛠️

**Predict:** You will add `display: flex;` to the `.announcement-board` rule. The four cards currently stack. Predict what the page shows after the switch: where the cards sit, what happens to their widths, and what happens to their heights (compare TWO's long text against FOUR's short one). Then predict what adding `flex-direction: column;` beneath it will show.

**Run:** Open the page in your browser and the stylesheet in VS Code, with your window at full laptop width. Add `display: flex;` to the board's rule, save, and refresh. Study the four heights before you move on. Then add `flex-direction: column;`, save, and refresh again. When you finish, delete the `flex-direction` line and keep `display: flex;`: the rest of the chapter builds on it.

**Explain:** In 1-2 sentences, describe what the row did to the cards' heights, and explain why the column version looked so familiar.

### Quick Check 6.1 ✅

1. A page's `main` holds three `section` elements, and the first section holds two paragraphs. `display: flex` lands on `main`. Which elements become flex items, and why do the paragraphs stay put?
2. The officers page lists its members in a column (`flex-direction: column`). A clubmate wants the whole stack pushed toward the container's bottom edge. Which property does that job here, `justify-content` or `align-items`, and why?
3. A clubmate adds `display: flex` to each announcement card instead of the board, and nothing lines up. Diagnose the mistake with the container and item vocabulary.

---

## 6.2 Controlling the Line

The container owns the line, so the line's controls all go on the container. This section hands you four of them. They decide where items sit along the main axis, where they sit along the cross axis, how much space separates them, and what happens when the line runs out of room. Not one of these declarations touches an item.

### justify-content: Placing Items on the Main Axis

**justify-content** distributes the items, and any leftover space, along the main axis. Its everyday values:

| Value | What the line shows |
| --- | --- |
| `flex-start` | Items at the line's start, leftover space after them (the default) |
| `center` | Items clustered mid-line, leftover space split between the ends |
| `flex-end` | Items at the line's end, leftover space before them |
| `space-between` | First and last items at the edges, leftover space shared between neighbors |
| `space-around`, `space-evenly` | Leftover space dealt around every item, with slightly different edge math |

One example carries the idea. Picture a status strip for the drive: the date at one end, a sign-up link at the other.

```css
/* The date holds one end, the sign-up link holds the other,
   and the leftover space sits between them. */
.drive-status-bar {
    display: flex;
    justify-content: space-between;
}
```

This course leans on `flex-start`, `center`, `flex-end`, and `space-between`. The last two values in the table exist, and you will meet them in browser DevTools on other people's sites long before you need to write them.

### align-items: Placing Items on the Cross Axis

**align-items** places items along the cross axis, and its default explains something you have already watched. The default is `stretch`: every item stretches across the cross axis to match the line, so a row's boxes all stand as tall as the tallest content. That is what TIY 6.1 did to the four cards' heights. The other everyday values are `center`, `flex-start`, and `flex-end`, and none of them stretches. Each item keeps its natural height and takes its assigned position: centered on the line, or hugging one edge of it.

Between the two properties, remember the split. `justify-content` answers "where along the line," and `align-items` answers "where across it."

### Try It Yourself 6.2: The Alignment Drill 🛠️

**Predict:** The board's rule carries `display: flex;` from TIY 6.1 and nothing else. Three edits are coming, and your job is to call each result before running it. First, `justify-content: center;`: where do the four cards sit, and where does the leftover space go? Second, the value changes to `flex-end`. Third, `align-items: center;` joins the rule: what happens to the four heights, remembering TWO's long text?

**Run:** Make the three edits one at a time, saving and refreshing after each, and check every prediction against the screen before the next edit. When you finish, delete both alignment declarations, leaving `display: flex;` alone for the next exercise.

**Explain:** In 1-2 sentences, name the axis each property worked along, and state which edit ended the height matching and why.

### gap: The Container Owns the Space

Chapter 5 spaced neighbors with margins, one element at a time, each box claiming its own moat. Flexbox adds a tool with different ownership. **gap** is declared once, on the container, and opens the same space between every pair of neighboring items:

```css
/* One declaration on the container, and every pair of roster
   cards gets the same 24 pixels between them. */
.officer-roster {
    display: flex;
    gap: 24px;
}
```

The pitch is consistency. No item carries a spacing rule, so no item can drift out of step, and changing one number respaces the whole line. Gap and margins do not behave identically, though, and the difference is easier to see than to memorize. The next exercise puts them side by side.

### Try It Yourself 6.3: Gap Versus Margin 🛠️

**Predict:** Two competing plans for spacing the announcement cards. Plan A adds `gap: 16px;` to the board's rule. Plan B instead adds `margin: 16px;` to the `.announcement-card` rule. Will the two boards look the same? Predict what each plan puts between neighboring cards, and what each puts between the outer cards and the board's own padded edges.

**Run:** Try Plan A: add the gap, save, refresh, and look hard at the middles and then at the edges. Delete it and try Plan B: the margin on the card rule. Compare the two, then finish in Plan A's state: gap on the board, no margins on the cards.

**Explain:** In 1-2 sentences, explain the difference using ownership language: which element owned the space in each plan, and where did the margin plan put space that the gap plan did not?

### flex-wrap: When the Line Runs Out of Room

A little arithmetic sets up the problem. Four cards at 220 pixels need 880. With `gap: 16px`, three gaps add 48 more, so the line wants 928 pixels of board content width. The board's content width is your window minus 52: the browser's default 8-pixel body margin on each side, the board's 2-pixel borders, and its 16 pixels of padding per side. A window narrower than about 980 pixels cannot seat the line.

What happens then? By default, nothing wraps. A flex container squeezes its items instead, shrinking each one below its declared width. Drag your own window's edge slowly inward and watch the four cards compress.

**flex-wrap** offers the other answer. Its `wrap` value lets a full line break, moving the items that no longer fit onto a new line at their declared size:

```css
/* Lines break instead of items shrinking. The fourth card drops
   whole onto a new line once the window gets too narrow. */
.announcement-board {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
```

Make the board match this rule, narrow the window past that same threshold, and the fourth card jumps down whole instead of squeezing. The gap holds between the lines as well as between neighbors. Notice what you built: content that rearranges itself to fit the space it is given. That is half of responsive design already. Chapter 8 adds media queries, and one site will serve every screen.

### Dead Center, Both Axes

One pairing is so common it deserves its own memory slot. Center on the main axis, center on the cross axis, and the content sits in the middle of its container:

```css
/* The classic: one item, dead center, whatever size the panel is. */
.welcome-panel {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

Centering a box inside a box was famously awkward for years. Now it is three declarations on the container.

### Quick Check 6.2 ✅

1. A toolbar's three buttons need to sit at the right end of their bar. Name the property and value that does it, and the axis you worked along.
2. A card row needs 20 pixels between neighboring cards and no extra space at the row's ends. Which spacing tool fits, and what would the other one have added?
3. A row of photos overflows its container on a phone-width window. Name the declaration that lets the row break onto new lines, and describe what the row does without it.

---

## 6.3 Smarter Selectors: Combinators and Pseudo-Classes

Now for the wart. The footer's links have worn default blue on deep teal since Lab 4A, and two critique lines have named it. The fix looks trivial: one `color` declaration. The declaration was never the problem. The aim was:

```css
/* Repaints EVERY link on the site: the footer's, the nav's, and
   the guide's source links in main. Far too broad for the job. */
a {
    color: #fac78d;
}
```

Light sand text would heal the footer and wreck everything else. The guide's source links sit on the light sand page background, so they would vanish into it, and the nav's white bar would fare little better. Every selector you own picks targets by identity: what the element is, what class it carries, what id it holds. None of them can say where the element sits. You could stamp a class on every footer link, today and forever. Or the stylesheet could read the tree.

### The Descendant Combinator

A **combinator** is a symbol written between two selectors that targets elements by their relationship in the page's tree. The workhorse is the **descendant combinator**, and it is the humblest character on the keyboard: a space.

```css
/* Anchors inside a footer, at any depth, and nothing else. Light
   sand on deep teal is on the palette's passing list. */
footer a {
    color: #fac78d;
}
```

Read combinator selectors right to left: `footer a` means every `a` that sits anywhere inside a `footer`. A link with no footer ancestor is invisible to the rule, whatever page it sits on. The selector finally says where instead of what, which is the power the wart was waiting for. Notice one thing it never touches: the underline stays, because these links live inside a paragraph, exactly where Chapter 5 said the uniform stays on.

This is Chapter 3's parent and child vocabulary paying off. Analyze the tree before you write the selector: name the ancestor that bounds the region, then the element you want inside it.

### One Stricter Sibling: The Child Combinator

The space matches descendants at any depth. Its stricter sibling, the **child combinator** (`>`), matches direct children only, one generation and no deeper. One contrast shows the difference:

```css
/* Descendant: matches all three nav links, which sit inside
   list items inside the list. */
nav a { color: #268080; }

/* Child: matches nothing on the club's pages, because every
   anchor sits three levels below the nav, not one. */
nav > a { color: #268080; }
```

You will meet `>` in stylesheets in the wild. This course's work only ever needs the space.

### The More Specific Selector Wins

Chapter 4's cascade left one tie-breaker as a cameo: a more specific selector beats a general one. Here is the payoff. Suppose a stylesheet contains both the bare `a` rule and the `footer a` rule. When both match the same footer link, `footer a` wins, wherever the two rules sit in the file. It says more about where the element lives, and CSS trusts the rule with the better aim. The measuring system behind that call is named specificity, and deeper courses assign it numbers. For this course, the working rule covers you: a region-scoped selector such as `footer a` outranks a bare element selector such as `a`, and "later wins" breaks ties only between equals.

### Pseudo-Classes: Styling States

The fix has a second half, because links are not static content. They respond. A **pseudo-class**, written with a leading colon, selects an element by its current state instead of its identity. Two states carry this chapter.

**:hover** matches while the visitor's pointer rests on the element. **:focus** matches while the element holds the keyboard's focus. Press Tab in the course browsers and focus steps from link to link, and the focused link is the one Enter activates. Two states, two audiences, one law: they are equal citizens. Devon's screen reader moves through pages by keyboard. So does every visitor whose hands cannot steer a mouse, and every power user racing through a form. A link that lights up for the mouse and stays silent for the keyboard tells those visitors the site was not built for them.

Two habits enforce the law:

* Every `:hover` style gets a `:focus` twin. Chapter 4's selector list makes the twin nearly free: one comma, one shared block.
* Browsers draw an outline around the focused element by default. Never remove it (`outline: none`) without replacing it with something at least as visible, because an invisible focus strands a keyboard visitor mid-page.

```css
/* One block, two states: mouse and keyboard get the same signal.
   Light sand on deep teal comes off the passing list. */
.join-link:hover,
.join-link:focus {
    background-color: #1a5e5e;
    color: #fac78d;
}
```

### Try It Yourself 6.4: The Footer Census, by Mouse and by Key 🛠️

This one runs on the real site: the pack's `assets/code/chapter-06/starter-site/` folder.

**Predict:** You are about to add this section's `footer a` rule to `club-styles.css`. Take a census first. Across all three pages, list every link the rule will catch and every link it will leave alone, page by page. The contact page deserves a second look before you commit.

**Run:** Add `footer a { color: #fac78d; }` to the stylesheet, refresh all three pages, and check your census against what changed. Then give the same links a state block: write a `footer a:hover, footer a:focus` rule using another pairing from the palette's passing list for deep teal (white is sitting right there). Put the mouse away and press Tab until focus reaches a footer link, and watch your style announce the stop. Undo every edit when you finish, because Skills Lab 6A makes this fix for keeps in your own copy.

**Explain:** In 1-2 sentences, explain why the contact page's email link kept its default blue, and name who the `:focus` style serves that the `:hover` style cannot.

### Quick Check 6.3 ✅

1. On the recycling guide, a teammate adds `main a { font-weight: bold; }`. Which links change, and which links on the page stay untouched?
2. A stylesheet ships `.menu a:hover { background-color: #268080; color: #ffffff; }` and no other state rule. Name the visitors who never see the highlight, and write the selector list that closes the gap.
3. A teammate adds `a:focus { outline: none; }` because the outline "clutters the design." State the law this breaks, and what any outline removal must ship alongside.

---

## 6.4 The Navigation Bar

Time to pay the oldest debt. The nav has worn the same disguise since Chapter 3: a semantic `nav` landmark holding a bulleted list of three links, indented, blue, and underlined on its white bar. The bar you are about to build contains nothing new. Every line comes from a chapter you have already finished, which makes this build a review wearing work clothes.

### Step 1: The List Becomes a Line

The bullets and the 40-pixel indent are browser default styles, the same authorship Chapter 4 exposed. **list-style** controls a list's markers, and its `none` value removes them. The indent is the list's default padding, and Chapter 5 taught you to zero what you did not ask for. Then this chapter's opener lays the items on a line:

```css
/* The bar: strip the browser's list dressing (the bullets and
   the 40-pixel indent), then lay the items on one line. */
nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: 8px;
}
```

Look at the selector before the declarations. `nav ul` is Section 6.3 at work: only lists inside the nav lose their dressing. The contact page's meeting-times list keeps its bullets, which a bare `ul` rule would have stripped along with everything else.

### Step 2: The Links Become Blocks

```css
/* Padded blocks make bigger targets, in the brand teal that
   passes on the bar's white. */
nav a {
    display: block;
    padding: 8px 12px;
    color: #268080;
    text-decoration: none;
}
```

Three decisions live in that rule.

* `display: block`. An anchor is an inline element (Chapter 2), and an inline box wears vertical padding badly, painting it without making room for it. Declaring `display: block` hands each link a real box that owns its padding, so the whole rectangle is the target.
* `padding: 8px 12px`. Chapter 5's two-value shorthand, buying finger-sized targets on a phone and forgiving aim everywhere.
* `text-decoration: none`. Chapter 5 let navigation bars drop underlines by convention, and attached a condition: something else must carry the signal. The bar's position and shape now say "these are links," and the next rule says it louder. The condition is paid.

### Step 3: The States

```css
/* Hover and focus, equal citizens: the same signal for the
   mouse and the keyboard. White on club teal is on the
   palette's passing list. */
nav a:hover,
nav a:focus {
    background-color: #268080;
    color: #ffffff;
}
```

Each block inverts on contact: teal text on white becomes white on teal. And note what the rule never touched. The browser's focus outline still draws, because the rule adds a signal and removes none.

### The Header Joins In

The header still stacks its logo above its title. One rule fixes all three pages:

```css
/* Logo and title share the line, centered against each other on
   the cross axis. wrap keeps each intro paragraph on its own
   full-width line instead of squeezing it into a column. */
header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 16px;
}
```

The logo and the `h1` fit the first line together, so they sit side by side, centered against the logo's height. Each intro paragraph wants more width than the line has left, so `wrap` hands it a fresh line at full width. The site finally looks like a site.

One old comment can retire too. The `.page-divider` rule has said since Lab 5A that centering the strip needs tools Chapter 6 teaches. Here they are:

```css
/* An image is inline until told otherwise, and auto margins
   center a block. The Chapter 5 comment can finally retire. */
.page-divider {
    display: block;
    margin: 32px auto;
}
```

### Read the Bar Back

The finished bar is a review of the course so far. Name where each ingredient came from:

* The `nav` landmark and its list of links: Chapter 3, built before you owned any CSS.
* The `nav ul` and `nav a` selectors: this chapter's descendant combinator, scoping every rule to the bar.
* `list-style: none` plus the zeroed margin and padding: Chapter 4's browser default styles, removed with Chapter 5's box-model tools.
* `display: flex` and `gap`: Sections 6.1 and 6.2.
* `display: block` and the padded targets: Chapter 2's inline-versus-block concept, given its CSS override here, spaced with Chapter 5's shorthand.
* The colors: Chapter 4's palette and its passing list.
* `:hover` and `:focus`: Section 6.3, with the outline law intact.

### Try It Yourself 6.5: One Change at a Time 🛠️

**Predict:** Copy this section's three nav rules into the pack starter site's `club-styles.css` and refresh any page: the bar appears, links resting at the line's start. Now call three variations before running them. On `nav ul`, what does `justify-content: center` show? What does `space-between` show, with only three links and a wide white bar? What does `flex-end` show?

**Run:** Add each value in turn, saving and refreshing between edits, and judge each bar against what a visitor expects from a navigation bar. Pick the one you would ship. Then undo all your edits, because the lab builds the bar for keeps in your own copy.

**Explain:** In 1-2 sentences, defend your shipping choice with the axis vocabulary, and name the value that scattered the links furthest apart.

### Quick Check 6.4 ✅

1. The tutoring center strips its menu's bullets with `ul { list-style: none; }` and finds its study-tips list went bald too. Name the one-word change that scopes the rule to the menu, and the chapter vocabulary that explains why it works.
2. The tutoring center's header stacks its logo above its title. Write the declarations that put them on one line, centered against each other, with breathing room between.
3. A clubmate deletes `text-decoration: none` from the nav rule because "Chapter 5 said underlines carry meaning." Make the counter-case for this context: name what still tells a visitor the bar's items are links.

---

## 6.5 Summary and Retrieval 💡

### Key Concepts

* `display: flex` on a parent creates a flex container and turns its direct children, and only those, into flex items. Items flow along the main axis, the cross axis runs perpendicular, and `flex-direction` points the main axis in a row (the default) or a column.
* The container owns the line's controls. `justify-content` places items along the main axis, and `align-items` places them along the cross axis, where its `stretch` default is why a row's boxes match heights. `gap` opens container-owned space between neighboring items.
* By default a full line shrinks its items instead of breaking. `flex-wrap: wrap` lets items drop whole onto new lines, which is half of responsive design before Chapter 8 even starts.
* Combinators target elements by relationship instead of identity. The descendant combinator (a space) reaches any depth, so `footer a` repaints the footer's links and nothing else, while the child combinator (`>`) takes direct children only. When two rules match one element, the more specific selector wins.
* Pseudo-classes style states: `:hover` for the pointer and `:focus` for the keyboard, written as twins in one selector list. Never remove a focus outline without a replacement at least as visible.
* The navigation bar assembles entirely from taught parts: the semantic nav list, `list-style: none` with zeroed spacing, flex plus gap, and padded block links with hover-focus twins from the palette's passing list. The dropped underline is paid for by the bar's position and its states.

### Key Terms

See course glossary for full definitions

* Flexbox, flex container, flex item, main axis, cross axis, flex-direction (Section 6.1)
* justify-content, align-items, gap, flex-wrap (Section 6.2)
* combinator, descendant combinator, child combinator, pseudo-class, :hover, :focus (Section 6.3)
* list-style (Section 6.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. State what `display: flex` does to the element that carries it and to that element's direct children, and name the two axes it creates.
2. Name the container property that controls each of these: placement along the main axis, placement along the cross axis, space between items, and line breaking.
3. Explain the difference in reach between `a` and `footer a`, and state which rule wins when both match the same link.
4. Recite the two accessibility laws this chapter attached to link states.
5. List the ingredients of the navigation bar in build order, naming the chapter that taught each one.

---

## 6.6 Skills Lab 6A: The Club Site Gets Its Layout

**Goal:** Give the club's site its layout: a flex header row, a wrapping gallery row, region-scoped link styling with accessible hover and focus states, and the navigation bar owed since Chapter 4.

**Dataset:** Provided files in `assets/code/chapter-06/` from the course data pack. `starter-site/` holds the club's three pages, the `images` folder, and `club-styles.css` exactly as Skills Lab 5A finished them: spaced, typeset, and validating with zero messages. The footer-link defect is still in place, documented in the folder's README. `club-palette.txt` travels with every CSS chapter, copied unchanged from the Chapter 5 pack. `flex-playground.html` and `flex-playground.css` are the chapter's practice pair. `skills-lab-6a-answers.txt` is your written answers file. Work at the extracted `cis133` root and copy every hex value from the palette file.

The lab walks the chapter's own path. Part 1 arranges the header and the gallery into flex lines. Part 2 fixes the inherited footer defect and gives every link region accessible states. Part 3 builds the bar and closes the Part II milestone.

### Part 1: Foundation (Aligns with MLO-6.1)

1. Copy the whole `starter-site` folder to your `cis133` root and rename the copy `skills-lab-6a-lastname`. Copy `skills-lab-6a-answers.txt` into it.
2. Build the header row: one `header` rule that puts the logo and the page title on a flex line, centered against each other on the cross axis, with a gap between them. Let the rule wrap, so each intro paragraph keeps its own full-width line. One rule serves all three pages. Record the rule and its axis reasoning in answer 1.A.
3. Build the gallery row on the drive gallery page. Give that page's `main` a role-based hook (your Chapter 4 class-versus-id decision rule applies), then make it a wrapping, gapped flex row. Give the gallery's figures a width that seats two per line inside the readable column. The starter's `main` rule reads `max-width: 640px` with `padding: 24px 16px`, so under border-box the column offers 640 minus 16 on each side: 608 pixels of content width. Two figure widths plus one gap must fit inside that. Zero the gallery figures' old margins with a descendant selector so the gap owns the spacing.
4. Watch the gallery at a wide window and a narrow one, and record the rule and both observations in answer 1.B.

### Part 2: Application (Aligns with MLO-6.2)

1. Fix the inherited defect. Repaint the footer's links with a descendant combinator and a pairing from the palette's passing list, leaving every other link untouched. Log the rule, its reach, and why `footer a` beats a bare `a` for this job in answer 2.A.
2. Give every link region its states: `:hover` and `:focus` twins for the nav's links and the footer's links, every pairing from the passing list, and no outline removed anywhere. Then put the mouse away, Tab through each page, and log the pass in answer 2.B.
3. Audit your new rules for reach. If any state or color rule catches links you never meant (the guide's source links in `main` are the easy ones to catch by accident), retarget it with a combinator.

### Part 3: Extension (Aligns with MLO-6.3)

1. Build the full navigation bar on all three pages. Strip the markers with `list-style`, zero the list's default spacing, lay the items on a gapped flex line, and pad each link into an underline-free block. The hover and focus states are already wired from Part 2. Scope every rule through `nav`.
2. Make one layout decision of your own: your bar's `justify-content` choice, or a footer or figure arrangement. Copy the declaration into answer 3.A and defend it with the axis vocabulary.
3. Validate everything: all three pages through the W3C HTML validator and `club-styles.css` through the CSS validator, repairing until every report shows zero messages. Log the results in answer 3.B with the critique no validator can make: one thing about your layout you would still improve, and why. Then run the Part II milestone check. Confirm the site shows all four milestone properties, and name where a grader can see each: a multi-section site, one external stylesheet, controlled spacing and type, and a Flexbox navigation bar.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Pick one flex container you built in this lab. Name its main axis and its cross axis. Then explain what one `justify-content` or `align-items` change did to its items, citing what you observed in the browser. Contrast that with what the same value on the other property would have done, and why the axes make those outcomes differ.
2. The accessibility case for `:focus`. Tab through your own nav bar by keyboard alone and describe the experience with your focus styles, then without them. Who does the focus style serve? Devon's screen reader travels the same links without a mouse, and so does every visitor who cannot steer one. What would removing focus outlines without a replacement cost those visitors?

**Submission:** Zip your `skills-lab-6a-lastname` folder containing your three HTML pages, your `images` folder, `club-styles.css`, and `skills-lab-6a-answers.txt`, and submit it as `skills-lab-6a-lastname.zip`. All three pages and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 6A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Code Accuracy and
Efficiency, Output Quality, Documentation and Code Comments, and
Analysis, Interpretation, and Response to QUESTION(s).

---

## 6.7 Review Questions 🔄️

1. **Remember:** Define flex container and flex item, state which elements become items when `display: flex` lands on a parent, and name the two axes every flex container has.

2. **Understand:** Explain why `gap` belongs to the container while margins belong to the items, and why every `:hover` style in this course ships with a `:focus` twin.

3. **Apply:** The tutoring center's site from earlier chapters wants its layout, and three requests came in. The header's logo and title should share one line, centered against each other. The subject-area cards should sit in a row that breaks onto new lines on narrow screens, with 16 pixels between cards. The footer's links need a color of their own without touching any other link on the site. Write the rule or declaration that answers each request, inventing role-based names where needed, and give one reason apiece.

4. **Analyze:** You inherit a stylesheet containing `a { color: #268080; }` and `footer a { color: #fac78d; }`. Three links need calls: one inside the page's footer, one inside the nav, and one in a paragraph inside `main`. For each, state its rendered color and justify the call with reach and the more-specific-wins tie-breaker. Then predict what deleting the `footer a` rule changes.

---

## Further Reading 📖

* [MDN: Flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox) - The reference walk through containers, items, axes, and alignment, at exactly this chapter's depth.
* [CSS-Tricks: A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) - The industry's favorite Flexbox reference card, with a diagram for every property and value.
* [web.dev: Learn CSS: Flexbox](https://web.dev/learn/css/flexbox) - Google's Learn CSS module on Flexbox, extending this chapter's properties with interactive examples.
* [MDN: :focus](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus) - The pseudo-class reference, including the warning never to remove an outline without a visible replacement.
* [WebAIM: Keyboard Accessibility](https://webaim.org/techniques/keyboard/) - Why keyboard support matters and how focus styling serves visitors who never touch a mouse.

---

## Looking Ahead ⏩

Part II is complete. You connected styles to pages, you controlled every box's space and type, and now you arrange the boxes themselves: connect, control, arrange, done. The club's site shows all four milestone properties, and you can build any layout you can sketch. That last word is the point. Chapter 7 opens Part III, Design for Every User, by teaching you to sketch deliberately: user experience, sitemaps, and wireframes. The final project's site plan begins there.
