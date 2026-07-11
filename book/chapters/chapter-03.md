# Chapter 3: Semantic HTML and Images

The recycling guide you built in Chapter 2 works. It validates with zero errors, its links resolve, and the club president approved it. Then a club member named Devon sent the officers an email. Devon uses a screen reader, and reaching the drop-off steps means listening through everything above them, every visit, because the page offers no way to skip ahead. The validator never flagged that. Valid markup and meaningful markup are two different standards, and this chapter raises your work to the second one.

Here is the surprising part: the fix changes almost nothing on screen. HTML has a set of elements whose whole job is to name what each region of a page IS, the way `<ol>` already names a sequence. Screen readers like Devon's use those names to jump straight to the content a visitor wants. Search engines use them to decide which part of your page is the part worth indexing, a ranking audience you met in Chapter 1. This is the deeper half of CLO V, creating well-structured pages, and it begins CLO VIII, building accessibility into everything you ship.

The president also had a request: "The pages look bare. Add some pictures." So this chapter delivers the images Chapter 2 promised. You will place images with the `img` element and write the alt text that keeps them meaningful for every visitor. You will pick file formats the way developers do, by matching format properties to the image's content. And you will organize a real multi-file site, because pages plus pictures equals folders to manage.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapter 2 (the HTML skeleton, elements and attributes, relative URLs, and the W3C validator)
* **Deliverables:** Skills Lab 3A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-3.1 (Apply):** Structure page content with semantic elements, choosing landmarks and text-level elements by the meaning of their content
* **MLO-3.2 (Apply):** Embed images with the `img` element, writing alt text that matches each image's purpose on the page
* **MLO-3.3 (Analyze):** Differentiate the web's image file formats by their properties to select the right format and folder home for a given image

### This chapter aligns with the following Course Learning Outcomes

* **CLO V (Create):** Create web pages using HTML for structure and CSS for presentation

---

## 3.1 From Valid to Meaningful: Semantic HTML

Chapter 2 taught you to choose elements by meaning: `<ol>` when order matters, `<ul>` when it does not. You were already practicing semantics without the name. A **semantic element** is an element whose name describes what its content IS, not how it looks. This section gives that idea its name, its audience, and its most misunderstood pair of elements.

### Three Readers, One File

Every HTML file you write has three kinds of readers, and only one of them has eyes on your pixels.

* **Browsers rendering for sighted visitors.** They would display almost anything. Chapter 2 showed you a browser silently guessing through broken markup.
* **Assistive technology.** Chapter 1 introduced screen readers. They do not see your page. They read your markup and announce what each element says it is: "heading level 2," "list, three items," "link."
* **Software that never draws the page at all.** Search engine crawlers, browser reader modes, and translation tools all parse your markup looking for meaning.

Pixels serve the first reader only. Semantics serve all three. When Devon's screen reader hits your `<ol>`, it announces a numbered list of three steps before reading one word of them. That announcement came from your element choice, nowhere else.

### The Full Story of strong and em

Chapter 2 borrowed `<strong>` to demonstrate nesting and promised the full story. Here it is, together with its partner `<em>`. The pair are text-level elements, markup that carries meaning inside a sentence rather than labeling a whole block.

The `<strong>` element marks content of **strong importance**: a warning, a deadline, the one fact the reader must not miss. Browsers show it bold. The `<em>` element marks **stress emphasis**: the word you would lean on if you read the sentence aloud. Browsers show it italic. Read these two aloud and stress the marked word:

```html
<p>Drop-offs end <em>this</em> Friday.</p>
<p><strong>Back up your data before the reset.</strong> The club
cannot recover it afterward.</p>
```

The first sentence stresses which Friday. The second flags a warning that protects the visitor's data. Both choices are about meaning, and the bold and italic rendering is the browser's default costume for that meaning.

Now the misunderstood part. HTML also has `<b>` and `<i>`, two holdovers that mark text for visual distinction while promising nothing about meaning. They are typographic conventions without emphasis: `<b>` for drawing the eye (a product name in a review), `<i>` for text set off from normal prose (a book title, a ship's name, a foreign phrase).

The decision rule: if removing the markup would change what the sentence MEANS, use `<strong>` or `<em>`. If it would only change how the text LOOKS, you are probably reaching for presentation, and Chapter 4 gives you CSS, the right tool for looks.

### The Non-Semantic Pair: div and span

HTML keeps two deliberately meaningless elements, and you will meet them everywhere in professional code. A **div element** (`<div>`) is a generic block-level container. A **span element** (`<span>`) is a generic inline container. There is Chapter 2's block-versus-inline distinction back at work: a `div` stacks like a brick, and a `span` flows inside a line of text.

```html
<div>
    <p>A div groups content but says nothing about it.</p>
</div>
<p>A span marks <span>a few words</span> and says nothing
about them.</p>
```

Render that page and the div and span change nothing you can see. They exist as hooks for CSS styling and scripting, jobs that start mattering in Chapter 4. The professional habit you start now: reach for a semantic element first, and use `div` or `span` only when no element with meaning fits. A page built entirely of divs is called div soup, and to Devon's screen reader it is one long unlabeled hallway.

### Try It Yourself 3.1: The Pixel Test 🛠️

**Predict:** One paragraph contains `<strong>reset your device</strong>` and another contains `<b>reset your device</b>`. Will a sighted visitor see any difference between the two? Will every reader of the page treat them the same?

**Run:** Add both paragraphs to a practice file in your `cis133` folder, save, and refresh. Look closely. Then right-click each phrase and Inspect to confirm which element produced which pixels.

**Explain:** In 1-2 sentences, state whether your findings make the two elements interchangeable, and defend your call with one specific reader of your file.

One honest caution now that you have looked: most screen readers, at their default settings, voice all four elements the same way. The durable difference is what the file records. `<strong>` and `<em>` store meaning where any reader, human or software, can find it. `<b>` and `<i>` store only a look.

### Quick Check 3.1 ✅

1. A teammate writes `<i>Warning: unplug the device first.</i>` because italics "look right" for warnings. Name the element this content calls for, and state what the content means that the markup fails to say.
2. Your page renders perfectly in your browser. Name two readers of the same file that never see those pixels, and state what they read instead.
3. When is `<div>` the right choice, given that it means nothing?

---

## 3.2 Page Landmarks: Naming Your Regions

Semantic choices at the sentence level help, but Devon's complaint was about whole regions: no way to tell the banner from the content from the footer. HTML gives every page region a name. A **landmark** is a semantic element that labels a major region of the page, and assistive technology builds a jump menu out of them. This section introduces the six elements you will use on nearly every page you ever build: four landmarks that shape the page, and two organizing elements that structure the content inside `<main>`.

### The Big Four: header, nav, main, footer

Four landmarks give almost any page its top-level shape.

* The **header element** (`<header>`) holds a region's introductory content: a logo, the page title, a tagline.
* The **nav element** (`<nav>`) holds major navigation: the set of links that move visitors around your site.
* The **main element** (`<main>`) holds the page's primary content, the material this page exists to deliver. Every page gets exactly one `<main>`, and that uniqueness is the point: it marks the single spot where the real content starts.
* The **footer element** (`<footer>`) holds closing content: contact information, copyright lines, related links.

Do not confuse `<header>` with `<head>` from Chapter 2. The `<head>` holds invisible information about the document. A `<header>` is visible content that introduces a region.

Here is the shape, as a complete body:

```html
<body>
    <header>
        <h1>Recycle Your Old Electronics</h1>
    </header>
    <nav>
        <ul>
            <li><a href="recycling-guide.html">Recycling Guide</a></li>
            <li><a href="contact.html">Contact the Club</a></li>
        </ul>
    </nav>
    <main>
        <!-- The page's actual content lives here -->
    </main>
    <footer>
        <p>Email the club with questions.</p>
    </footer>
</body>
```

Notice the pattern inside `<nav>`: the links ride in a list. A screen reader announces the list's size ("list, two items"), so visitors hear how many destinations exist before visiting any of them. Notice also what the landmarks did to Chapter 2's nesting: `<body>` is now the **parent element** of four children, and every element inside `<header>` is a **child element** of it. Parent and child are the standard names for Chapter 2's containment rule, and CSS will lean on them heavily starting next chapter.

With this structure, Devon's screen reader offers a landmark menu: banner, navigation, main, contentinfo. One keystroke jumps to `<main>`. The hallway has doors now, and every door has a label.

### Inside main: section and article

Two more semantic elements organize the content within. Neither is a landmark. They give the markup structure any reader of the file can use, but they do not join the jump menu Devon's screen reader builds.

* The **section element** (`<section>`) groups one thematically related chunk of a page, and it should always contain a natural heading. Your guide's "Why It Matters" block, its `<h2>` plus its paragraphs, is a section.
* The **article element** (`<article>`) wraps content that could stand alone: a blog post, a news story, a product review. The test is portability. If you handed the content to someone with no idea what site it came from, would it still make sense?

The two confuse everyone at first, so use the tests in order. Could it stand alone? Article. Is it one themed chunk of this page with its own heading? Section. Neither, and you only need a container to style? That is what `div` is for.

```html
<main>
    <section>
        <h2>Why It Matters</h2>
        <p>Electronics contain metals worth recovering.</p>
    </section>
    <section>
        <h2>What the Club Accepts</h2>
        <p>Bring any item on the list to a collection event.</p>
    </section>
</main>
```

One more landmark exists, `<aside>`, for content related to but separate from the main flow, like a sidebar. You will meet it in the wild, and it can wait until you need it.

A caution before the lab: adding these structural elements changes almost nothing visually. They are block-level containers, and your headings and paragraphs were already stacking as blocks. The payoff is real but invisible, which is exactly why beginners skip it and professionals do not.

### Try It Yourself 3.2: The Landmark Census 🛠️

**Predict:** Wikipedia articles are enormous pages built by professionals. On one article page, how many `<main>` elements will you find? How many `<nav>` elements: zero, one, or several?

**Run:** Open [en.wikipedia.org/wiki/Recycling](https://en.wikipedia.org/wiki/Recycling) and open DevTools with Inspect, as in Chapter 2. New trick: click once inside the Elements panel and press Ctrl+F (Cmd+F on Mac), and DevTools opens a search box that hunts through the markup instead of the page. Search for `<main` and count the matches, then search for `<nav`.

**Explain:** In 1-2 sentences, explain why one of those counts must be exactly 1 while the other can grow with the page's complexity.

### Quick Check 3.2 ✅

1. A classmate wraps their entire page, banner and footer included, in `<main>` because "it is all the main page." What does that markup claim, and what does a screen reader user lose?
2. The club wants to publish meeting recaps that members share by direct link. Choose `<section>` or `<article>` for each recap and defend the choice with this section's test.
3. In the landmark skeleton above, name one parent-child pair and state which element is which.

---

## 3.3 Images and Alt Text

Structure delivered. Now the pictures. The club's design team drew a matching set of flat illustrations for the site, and they ship in your data pack's `chapter-03` folder. Everything in this section works with those files.

### The img Element

The **img element** (`<img>`) embeds an image into a page. It is an empty element, like `<meta>` and `<br>` from Chapter 2: there is no content to wrap, so there is no closing tag. Attributes do all the work, and two are required by the standard.

* The `src` attribute holds the address of the image file. It accepts the same two address forms links use: absolute URLs for images on other sites, relative URLs for your own files. Your own images should travel with your site, so relative is the professional default.
* The `alt` attribute holds the image's **alt text**, the text that stands in for the image when the pixels cannot. Alt text serves screen reader users, broken file paths, and the moments before a slow connection delivers the file.

```html
<img src="assets/code/chapter-03/cactus-garden.png"
alt="Three green cacti in a gravel garden under an orange sky">
```

Save a practice page with that line at your `cis133` root and the browser displays the club's cactus illustration. A screen reader reads the alt text aloud, then says "image." What happens when the pixels cannot arrive at all? The next exercise breaks the path on purpose. The validator's opinion hints at the stakes: it treats a missing `alt` as an error, not a style complaint.

`<img>` has one more surprise: it is an inline element. Chapter 2's rule still holds. An image flows along inside a line of text like one oversized character, and it starts no new line on its own.

### Try It Yourself 3.3: Break the Path 🛠️

**Predict:** Change the `src` to `cactus-gardens.png`, one letter wrong. What will the browser show where the image was: an error page, an empty gap, or something else?

**Run:** Break the file name, save, and refresh. Note exactly what appears. Then remove the entire `alt` attribute, save, and refresh again.

**Explain:** In 1-2 sentences, describe what the alt text did for the broken page, and what the second refresh tells you about pages whose images carry no alt at all.

### Sizing with width and height

Two more attributes declare the image's dimensions in pixels.

```html
<img src="assets/code/chapter-03/cactus-garden.png"
alt="Three green cacti in a gravel garden under an orange sky"
width="400" height="400">
```

The numbers should state the image's true size, 400 by 400 for this file. Whose numbers win when your markup and the file disagree? The next exercise settles it. Why declare at all? Because the browser reserves that space before the file arrives. Without declared dimensions, a slow-loading image shoves the whole page downward when it lands, the jump you have felt on sluggish sites a hundred times.

Where do the true numbers come from? Your data pack's README lists every image's pixels, and your operating system shows them in a file's properties or Get Info panel.

### Try It Yourself 3.4: Lie About the Size 🛠️

**Predict:** `cactus-garden.png` is a 400 by 400 square. If you keep `width="400"` but change the height to `150`, what will the cacti look like?

**Run:** Change the height, save, and refresh. Then fix it.

**Explain:** In 1-2 sentences, state whose numbers won, yours or the file's, and write the rule you will follow for every width and height you declare.

### Writing Alt Text That Works

The `alt` attribute is required. Good alt text is a judgment call, and the judgment starts with one question: what job is this image doing on this page?

* An **informative image** carries content. Describe what matters, in about a sentence, the way you would over the phone. For the cactus garden you placed earlier: `alt="Three green cacti in a gravel garden under an orange sky"`. Not "image of a garden" (the screen reader already says "image") and not a pixel-by-pixel inventory.
* A **decorative image** carries no content. The club's diamond divider strip separates sections the way a horizontal line would. Write `alt=""`, empty and deliberate. A screen reader skips the image entirely, which is the kind choice: forcing Devon to hear "decorative border, decorative border" between sections helps no one. Never omit the attribute. Empty alt is a decision, and a missing alt is an error.
* A **functional image** does a job, usually inside a link. Describe the destination, not the picture: a logo linking home gets `alt="PC Computer Club home"`, not a description of the logo's arrows.

The same image can be informative on one page and decorative on another. The cactus garden as a page's only illustration of desert planting is informative. The same file used as page decoration deserves `alt=""`. Alt text describes a purpose, not a file, which is why no tool can write it for you.

### Complex Images: figure and figcaption

Some images need more than a sentence, and some deserve a visible caption. The **figure element** (`<figure>`) wraps self-contained illustrative content, and the **figcaption element** (`<figcaption>`) supplies its visible caption. The pack's membership chart wants both:

```html
<figure>
    <img src="assets/code/chapter-03/membership-chart.png"
    alt="Bar chart of club membership across four semesters,
    growing every term from 18 to 39 members."
    width="640" height="400">
    <figcaption>The club keeps growing. Recruiting at the fall
    involvement fair drove most of the gain.</figcaption>
</figure>
```

Notice the division of labor. The alt text replaces the chart for someone who cannot see it, so it delivers the finding: growth every semester, 18 to 39. The figcaption is visible to everyone and comments on the chart without repeating it. Caption and alt text answering the same question word for word is the telltale of alt text written without thought.

### Quick Check 3.3 ✅

1. Write the alt attribute for the club logo in two situations: sitting unlinked in a page header, and serving as the link to the home page.
2. A teammate declares `width="800" height="450"` for an image that is truly 800 by 533. Describe what visitors see and name the one source of truth for those numbers.
3. Your page's chart has `alt="Chart of drive results"` and a figcaption reading "Chart of drive results." Diagnose both problems.

---

## 3.4 Image Formats and Site Organization

Every image on your pages so far has been a PNG. The web runs on several formats, each engineered with different trade-offs, and choosing among them is a decision you will make on every project. This section gives you the properties that drive the choice, and then puts your growing pile of files into professional order.

### Raster and Vector

Image formats split into two families. A **raster image** stores a grid of colored pixels. Zoom in far enough and you see the squares, and scaling a raster image up past its true size turns it soft and blocky. A **vector image** stores drawing instructions instead: shapes, points, and curves as mathematics. The computer redraws it at any size, so a vector logo is as sharp on a stadium screen as on a phone.

Photographs are raster by nature, because cameras capture pixels. Logos, icons, and diagrams are the natural home of vector formats.

### The Four Formats You Will Choose Between

* **PNG (Portable Network Graphics):** raster, with **lossless compression**, meaning the file shrinks without discarding any pixel data. PNG supports **transparency**, so an image can have see-through regions that let the page background show. The club logo uses exactly that: its corners are transparent, so the round logo sits cleanly on any background color. PNG is the workhorse for screenshots, illustrations with flat color, and anything needing transparency.
* **JPEG:** raster, with **lossy compression**, meaning it shrinks files by permanently discarding detail your eye is unlikely to miss. For photographs, the trade is spectacular: a fraction of the file size for nearly identical appearance. Two costs travel with it: no transparency, and quality that degrades a little more with each re-save.
* **GIF:** raster, limited to 256 colors, and capable of simple frame-by-frame animation. That color limit makes it a poor choice for photos, and PNG beats it for flat graphics. It survives on animation convenience alone.
* **SVG (Scalable Vector Graphics):** the web's vector format. Logos, icons, and diagrams built as SVG stay sharp at every size, and the files are often tiny. It is the wrong tool for photographs, which have no shapes to describe.

One name you will meet in the wild: WebP, a modern raster format that compresses smaller than PNG and JPEG and handles transparency and animation. Evergreen browsers support it, and you will see it constantly in DevTools on commercial sites.

So why does your data pack ship only PNGs? The club's images are flat-color illustrations, PNG's sweet spot, and the logo needs its transparent corners. One format, honestly chosen. When the club starts posting camera photos of real drives, that choice gets revisited, and that is one of your Skills Lab questions.

| Format | Family | Compression | Transparency | Animation | Reach for it when |
| ------ | ------ | ----------- | ------------ | --------- | ----------------- |
| PNG | Raster | Lossless | Yes | No | Illustrations, screenshots, transparency |
| JPEG | Raster | Lossy | No | No | Photographs |
| GIF | Raster | Lossless within its 256 colors | Limited | Yes | Simple animations |
| SVG | Vector | Not applicable | Yes | Possible | Logos, icons, diagrams |

File size is the recurring stake in every row. Chapter 1 traced a page request across the Internet, and every image is one more file making that trip. Oversized images are the single most common reason student pages load slowly.

### Try It Yourself 3.5: The File Size Detective 🛠️

**Predict:** Rank these three pack images by file size, largest first: `club-logo.png` (240 by 240), `recycling-drive.png` (800 by 450), `devices-collected-chart.png` (640 by 400). What did you base the ranking on?

**Run:** Find the three files in your `cis133` folder and check their sizes in your file manager (List view on Mac, Details view on Windows).

**Explain:** Your file manager just handed you the true ranking. In 1-2 sentences, explain what besides pixel count drives a PNG's size, using the pair whose order surprised you most.

### Organizing a Real Site

Your project is now pages plus images, and professional sites keep the two sorted. The convention is simple: one folder for the whole site, HTML files at its top level, and an `images` folder beside them.

```text
skills-lab-3a-ortiz/
├── recycling-guide.html
├── contact.html
├── drive-gallery.html
└── images/
    ├── club-logo.png
    ├── desert-divider.png
    ├── devices-collected-chart.png
    └── recycling-drive.png
```

Chapter 2's relative URL rules carry over unchanged, because a `src` is an address like any `href`. From any page at the folder's top level, a folder name and a slash steps down into the images folder:

```html
<img src="images/desert-divider.png" alt="" width="800"
height="24">
```

Compare that with the practice pages earlier in this chapter, which reached the same kind of file at `assets/code/chapter-03/cactus-garden.png`. Same file idea, different address, because a relative URL always starts from where YOUR page sits. When you copy pack images into your lab site's `images` folder, every src on your pages uses the short form. The folder becomes self-contained: zip it, move it, or publish it in Chapter 12, and every address inside still works.

One more convention to bank for later: the web's default name for a site's home page is `index.html`. Web servers serve it automatically when a visitor asks for a bare folder. Your lab site's pages keep their descriptive names this week, and `index.html` takes over when your final project builds a true multi-page site.

### Quick Check 3.4 ✅

1. The club has four files to publish: a phone photo of the fall drive, a logo that must stay sharp at every size, a three-second animated demo, and a screenshot of the sign-up form. Assign each a format and one property that justifies it.
2. A classmate's page at the top of their site folder shows a broken image with `src="C:\Users\sam\site\images\logo.png"`. Explain both what breaks when the site is zipped and shared, and what the src should be.
3. Why does a 4,000-pixel-wide photo straight off a phone camera make a bad web image even when it looks fine on screen?

---

## 3.5 Summary and Retrieval 💡

### Key Concepts

* Semantic elements name what content IS, and that meaning serves three readers: browsers, assistive technology, and software like search crawlers that never draws pixels. `<strong>` marks importance and `<em>` marks spoken stress, while `<b>` and `<i>` copy the looks and promise nothing. The meaningless containers `<div>` and `<span>` are last resorts, not defaults.
* Landmarks label page regions: `<header>` introduces, `<nav>` holds the site's links in a list, `<main>` holds the primary content exactly once per page, and `<footer>` closes. Assistive technology turns those four into a jump menu. Inside `<main>`, the organizing elements `<section>` (one themed chunk under a heading) and `<article>` (content that could stand alone) add structure without joining the menu.
* The empty `<img>` element embeds images through attributes. `src` addresses the file (relative URLs for your own images), `alt` stands in when pixels cannot, and `width` and `height` declare the true dimensions so the browser reserves honest space.
* Alt text follows the image's job. Informative images get a one-sentence description of what matters, decorative images get a deliberate `alt=""`, functional images describe their destination, and complex images pair a finding-level alt with a visible `<figcaption>` inside a `<figure>`.
* Formats are trade-offs: PNG (lossless, transparency) for illustrations and screenshots, JPEG (lossy) for photographs, GIF for simple animation, SVG (vector) for logos and diagrams that must scale. File size rides on every choice. Sites stay portable when pages sit at the folder top with an `images` folder beside them, addressed by relative URLs.

### Key Terms

See course glossary for full definitions

* semantic element, strong importance, stress emphasis, div element, span element (Section 3.1)
* landmark, header element, nav element, main element, footer element, section element, article element, parent element, child element (Section 3.2)
* img element, alt text, informative image, decorative image, functional image, figure element, figcaption element (Section 3.3)
* raster image, vector image, lossless compression, lossy compression, transparency, PNG, JPEG, GIF, SVG (Section 3.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Sketch the four-landmark page skeleton from memory: the elements in order inside `<body>`, and the one landmark that may appear only once.
2. State the decision rule that separates `<strong>` and `<em>` from `<b>` and `<i>`, and give one sentence where `<em>` changes the meaning.
3. An image's alt text should depend on the image's job on the page. Name the three jobs from this chapter and the alt approach each one gets.
4. A photograph, a logo, and a short animation need formats. Assign one each and name the property that decided it.
5. Explain why `src="images/logo.png"` keeps working after the site folder is zipped and moved, while an absolute path to your own disk does not.

---

## 3.6 Skills Lab 3A: Give the Club's Site Structure and Pictures

**Goal:** Retrofit the club's two finished pages with semantic landmarks, place the club's images with alt text you write yourself, and build the site's new gallery page.

**Dataset:** Provided files in `assets/code/chapter-03/` from the course data pack: `recycling-guide-start.html` and `contact-start.html` (the finished Chapter 2 pages), `gallery-content.txt` (every piece of the gallery page's text, labeled), and `skills-lab-3a-answers.txt` (your written answers file). Nine PNG images ship in the same folder, documented in its README. Work at the extracted `cis133` root. Copy provided text instead of retyping it: you type only the markup.

### Part 1: Foundation (Aligns with MLO-3.1)

1. Create a folder named `skills-lab-3a-lastname` at your `cis133` root with an `images` folder inside it, and copy `skills-lab-3a-answers.txt` into it.
2. Copy `recycling-guide-start.html` into your lab folder and rename it `recycling-guide.html`. Update the comment at the top of the body with the lab number, your name, and the date.
3. Wrap the page's regions in landmarks: a `header` for the title and intro paragraphs, a `main` for the page's content, and a `footer` for the closing paragraph. Add one `section` per themed block inside the main. Indent one extra level, as Chapter 2 taught, so the new nesting stays readable.
4. Add a `nav` between the header and the main, holding a list of three links: Recycling Guide (`recycling-guide.html`), Spring Drive Gallery (`drive-gallery.html`), and Contact the Club (`contact.html`). Two of the three pages do not exist yet. Part 3 pays that debt.
5. Give two phrases their text-level elements: the phrase "in order" in the drop-off instructions, and the word "not" in the Why It Matters paragraph. Choose between `<strong>` and `<em>` for each by meaning.
6. Record your landmark map in answer 1.A and your hardest landmark call in answer 1.B. Validate the page and fix anything the validator reports.

### Part 2: Application (Aligns with MLO-3.2)

1. Copy `club-logo.png`, `recycling-drive.png`, `devices-collected-chart.png`, and `desert-divider.png` from the data pack into your lab site's `images` folder.
2. Place the logo at the top of the header, the collection-scene illustration inside the Why It Matters section, and the divider between the main and the footer. Every `src` uses the short relative form from Section 3.4.
3. Write each image's alt text yourself, matching it to the image's job on this page. At least one image on the finished page should carry a deliberate `alt=""`.
4. Add `devices-collected-chart.png` inside a `figure` in the Why It Matters section, with alt text that delivers the chart's finding and a `figcaption` you write that adds to it without repeating it.
5. Give every image `width` and `height` attributes that state its true pixels (the pack README and your file manager both know them).
6. Log every alt decision in answer 2.A and your dimension source in answer 2.B. Save, refresh, validate, and confirm every image renders.

### Part 3: Extension (Aligns with MLO-3.1, MLO-3.2, MLO-3.3)

1. Build `drive-gallery.html` in your lab folder from `gallery-content.txt`: the full Chapter 2 skeleton, then the same header-nav-main-footer landmark pattern as the guide, with the logo in the header.
2. Copy the three gallery images into your `images` folder. Present each as a `figure` with its provided caption as the `figcaption` and alt text you write yourself. The content file gives you no alt text on purpose.
3. Copy `contact-start.html` in as `contact.html` and give it the same landmarks and the same nav. This page has no closing paragraph, so it earns no footer, and that absence is a semantic decision too.
4. Test the site as a site: starting from the guide, reach every page and return using only your nav links. Then validate all three pages until each reports zero messages.
5. Answer 3.A (your gallery alt text log) and 3.B (format choices for the club's three planned media files) in the answers file.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Open your finished `recycling-guide.html` beside the starter file in your browser. The two render nearly identical pixels, yet Part 1 took real work. Citing your landmark map from 1.A, name two audiences from this chapter that now read your page differently, and explain what each one gained.
2. Your alt log in 2.A contains at least one empty alt and several written ones. Pick one written alt and the empty one, and justify each by the job that image does on the page. Then describe a change to the page's content that would force you to replace the empty alt with real alt text.

**Submission:** Zip your `skills-lab-3a-lastname` folder containing your three HTML pages, your `images` folder, and `skills-lab-3a-answers.txt`, and submit it as `skills-lab-3a-lastname.zip`. All three pages must validate with zero errors, every image must render, and every answer in the answers file must sit under its numbered prompt.

### Rubric: Skills Lab 3A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s).

---

## 3.7 Review Questions 🔄️

1. **Remember:** List the four landmarks that shape a page's top level, in their conventional order, and state one job of each.

2. **Understand:** A classmate says "I skip landmarks and alt text when a page looks finished, because nothing changes on screen." Using this chapter's three readers of an HTML file, explain what "finished" is missing.

3. **Apply:** The tutoring center's page from Chapter 2 is getting media. The additions: a phone photo of the tutoring room, the center's logo (which must sit on a colored banner and stay sharp when reused on posters), and a decorative border strip between sections. For each, name the file format you would request and write the alt attribute you would ship, with one reason apiece.

4. **Analyze:** A page passes the validator with zero errors, yet its markup is one `<h1>` followed by forty `<div>` elements, and its images all carry `alt="image"`. Contrast what the validator checked with what it never checked, and describe the experience this page hands a screen reader user, citing two specific failures.

---

## Further Reading 📖

* [MDN: Structuring documents](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents) - A beginner-level walkthrough of header, nav, main, and the rest of the landmark family, with live examples.
* [MDN: HTML images](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_images) - The img element, alt text, and figure with figcaption, at exactly this chapter's depth.
* [W3C Web Accessibility Initiative: Images Tutorial](https://www.w3.org/WAI/tutorials/images/) - The standards body's own decision tree for informative, decorative, functional, and complex images. Bookmark it for every alt text call you ever make.
* [WebAIM: Alternative Text](https://webaim.org/techniques/alttext/) - A deeper guide to writing alt text that serves real screen reader users, from a leading accessibility organization.
* [web.dev: Learn HTML](https://web.dev/learn/html) - Google's free HTML course. The semantic HTML and images modules extend this chapter with industry examples.

---

## Looking Ahead ⏩

Your pages now say what every region and image means, and the club's site finally looks like a site, if a plain one. Chapter 4 hands you CSS, the language that controls how all of it looks: colors, type, and the styling that Chapter 2 told you to stop faking with heading levels. The landmarks you built this week become the exact hooks your stylesheets grab first. Structure this week, presentation next.
