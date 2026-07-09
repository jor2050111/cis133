# CIS133 Glossary

This glossary is the single source of truth for all technical terms used in the CIS133 textbook. All chapters must use these exact definitions and capitalizations.

**Usage rules:**
* Define every term on first use in each chapter (bold the term)
* Reference this glossary in Key Terms sections (do not duplicate definitions)
* Add new terms alphabetically as chapters are written
* Use exact capitalizations specified here

---

## A

**absolute URL:** The complete address of a resource: protocol, domain, and path. Use it to link to a page on another site.

**accessibility:** The practice of building sites every visitor can use, including people who rely on screen readers, keyboards, or other assistive tools. One of the five UX principles.

**accessibility evaluator:** A tool that scans a rendered page and flags the accessibility barriers software can detect, such as missing alt text, empty links, and failing contrast. WAVE is the course's evaluator.

**align-items:** The container property that places flex items along the cross axis: `stretch` (the default), `center`, `flex-start`, or `flex-end`. Stretch is why a row's items stand equally tall until you say otherwise.

**alt text:** The text that stands in for an image when its pixels cannot: read aloud by screen readers and shown when the file fails to load. It lives in the `img` element's `alt` attribute.

**article element:** The landmark (`<article>`) that wraps content able to stand alone outside its page, such as a blog post, news story, or review.

**at-rule:** A CSS instruction that begins with an at sign and speaks to the stylesheet itself instead of styling one selector. `@media` is the first one this course teaches.

**attribute:** A name and value pair written inside an opening tag that configures the element, such as `lang="en"`.

## B

**base styles:** The rules in a stylesheet that sit outside every media query and serve every screen size. Query blocks adjust them and never repeat them.

**block-level element:** An element that begins on a new line and claims the page's full width. Headings, paragraphs, and lists are block-level elements.

**body:** The element that holds everything visible in the browser window. All of a page's on-screen content lives inside it.

**border:** The box model layer drawn between an element's padding and its margin: a visible line with a width, style, and color of its own.

**border-collapse:** The CSS property that controls whether neighboring table borders merge. Its `collapse` value replaces the browser's default gap between cell borders with single shared lines.

**border shorthand:** The `border` property, which sets a border's width, style, and color in one declaration, such as `border: 3px solid #268080;`.

**box model:** The browser's model of every element as a rectangular box built from four layers: content, padding, border, and margin. DevTools draws any element's box as a diagram of nested rectangles.

**box-sizing:** The CSS property that decides what `width` measures. Its `border-box` value makes a declared width cover content, padding, and border together, so the number you write is the box you see.

**breakpoint:** The screen width at which a media query changes a layout. Good breakpoints come from where the content stops fitting, not from a chart of device sizes.

**browser:** A program that requests pages from web servers and displays them on your screen. Chrome, Edge, Firefox, and Safari are browsers.

**browser default styles:** The stylesheet every browser ships and applies to pages that bring no CSS of their own. It is why an unstyled page still shows large bold headings and blue links.

## C

**cache:** A browser's local store of recently downloaded page files. The cache lets a repeat visit load without downloading everything again.

**caption element:** The element (`<caption>`) that gives a table its own title, written as the table's first child. It belongs to the table and travels with it, the way a `<figcaption>` belongs to its figure.

**cascade:** The tie-breaking system CSS uses when more than one rule targets the same element. An inline style wins over stylesheet rules, and among rules with an equal claim, the later one wins.

**checkbox:** The form control (`<input type="checkbox">`) that gives one option its own independent yes or no. Only a checked box sends its name-value pair when the form submits.

**child combinator:** The `>` written between two selectors, which matches direct children only. `nav > a` matches an anchor one level inside the nav and nothing deeper.

**child element:** An element nested directly inside another element. Every element inside a `<header>` is a child of that header.

**class attribute:** The attribute that opts an element into a class, written `class="deadline"`. Any number of elements, of any type, can share one class.

**class selector:** The selector that targets every element carrying a given class, written with a leading dot, such as `.deadline`. Use it to style some elements of a kind, chosen by role.

**client:** Any device that asks a server for something, such as a laptop, phone, or smart TV. The client asks, and the server answers.

**client-server model:** The pattern behind every web interaction. A client asks a server for something, and the server answers.

**color name:** A CSS color value written as a predefined keyword, such as `teal`. The web defines more than 140 of them, handy for quick tests but rarely an exact match for a brand color.

**combinator:** A symbol written between two selectors that targets elements by their relationship in the page's tree. The descendant combinator (a space) and the child combinator (`>`) are the common ones.

**conformance level:** The grade of WCAG a page claims to meet: Level A, AA, or AAA. Level AA is the working target for this course and for most of the industry.

**consistency:** The UX principle that the same things look and behave the same way on every page, so nothing has to be relearned. One external stylesheet and a shared navigation bar enforce it.

**contrast ratio:** The measure of how strongly text stands out from its background, running from 1 to 1 (text on its own color) to 21 to 1 (black on white). WCAG Level AA requires 4.5 to 1 for body text.

**cookie:** A small piece of data a website stores in your browser so the site can recognize you on a later visit.

**copyright:** The legal protection a creator automatically holds over their work from the moment it is created. Reusing protected work requires permission or a license.

**Creative Commons:** A family of public licenses an author attaches to a work to spell out what reuse is allowed, such as requiring credit or forbidding commercial use.

**cross axis:** The axis that runs perpendicular to a flex container's main axis. `align-items` places items along it.

**CSS (Cascading Style Sheets):** The stylesheet language of the web. CSS rules control how HTML content looks, including color, spacing, type, and layout.

**CSS comment:** A note wrapped in `/*` and `*/` that browsers skip entirely. Comments document a stylesheet for the humans who read it, explaining why a choice was made.

**CSS rule:** One complete styling instruction: a selector naming which elements to style and a declaration block saying how.

**CSS validator:** The free checking service at jigsaw.w3.org/css-validator that reports every place a stylesheet breaks the CSS standard. It names the defects that browsers skip silently.

## D

**data cell:** The table cell element (`<td>`) that holds one value in a grid. Its meaning comes from its row and its column together.

**declaration:** One property and value pair inside a declaration block, such as `color: #1a5e5e;`. Each declaration ends with a semicolon.

**declaration block:** The part of a CSS rule between the braces, holding the rule's declarations.

**decorative image:** An image that adds no content to its page, such as a border strip. It gets a deliberate empty alt (`alt=""`) so screen readers skip it.

**descendant combinator:** The space between two selectors, as in `footer a`: it matches elements sitting at any depth inside the first selector's matches.

**device mode:** The browser DevTools view that emulates how a chosen phone or tablet renders a page and reports the rendered width. It is how this course tests layouts without owning every device.

**digital certificate:** A file, issued by a trusted authority, that proves a website's identity and enables its encrypted connections.

**div element:** The generic block-level container (`<div>`). It carries no meaning and serves as a hook for styling and scripting when no semantic element fits.

**DNS (Domain Name System):** The Internet's address book. DNS translates a domain name you can read into an IP address computers can route.

**doctype declaration:** The required first line of an HTML document, written `<!DOCTYPE html>`. It tells the browser the file uses modern HTML.

**domain name:** The human-readable name of a website, such as phoenixcollege.edu. You register a domain name so visitors do not need to remember an IP address.

## E

**element:** One piece of page structure, such as a paragraph, heading, or list. Most elements are written as an opening tag, content, and a closing tag.

**element selector:** The selector that targets every instance of an element by its name, such as `h1` or `footer`.

**empty element:** An element with a single tag and no content or closing tag, such as `<meta>` or `<br>`.

**external stylesheet:** A separate `.css` file connected to pages with the link element. One external stylesheet can style every page of a site, which makes it the professional default.

## F

**feedback:** The UX principle that a site answers every visitor action with a visible response, such as a link that lights up for both the pointer and the Tab key.

**fieldset element:** The element (`<fieldset>`) that wraps a group of related form controls, such as a radio group, and draws its boundary. Its legend names the question the group answers.

**figcaption element:** The element (`<figcaption>`) that supplies a figure's visible caption. It lives inside a `<figure>`.

**figure element:** The element (`<figure>`) that wraps self-contained illustrative content, such as a chart or diagram, often paired with a `<figcaption>`.

**file extension:** The ending of a file name after the dot, such as `.html` or `.txt`. It tells the computer and the browser what kind of file it is.

**Flexbox:** CSS's system for arranging elements along a line. One declaration, `display: flex` on a parent, switches it on.

**flex container:** An element that declares `display: flex`. Its direct children become flex items, and all of the line's controls are declared on it.

**flex-direction:** The container property that sets which way the main axis runs: `row` (the default, horizontal) or `column` (vertical).

**flex item:** A direct child of a flex container. The container arranges its items along the main axis.

**flex-wrap:** The container property that decides whether a full flex line may break. With `wrap`, items that no longer fit move to a new line instead of shrinking.

**:focus:** The pseudo-class that matches an element while it holds keyboard focus, such as a link reached with the Tab key. Every `:hover` style needs a `:focus` twin.

**font-size:** The CSS property that sets how large text renders, in a fixed unit such as `px` or a relative one such as `rem`.

**font stack:** A `font-family` value that lists fonts in order of preference. The browser uses the first font it can supply, so the stack ends with a generic font family as the safety net.

**font-style:** The CSS property that slants text with its `italic` value. It changes the look only: stress emphasis stays the job of `<em>`.

**font-weight:** The CSS property that sets how heavy text strokes render, such as `bold`. It changes the look only: marking importance stays the job of `<strong>`.

**footer element:** The landmark (`<footer>`) that holds a region's closing content, such as contact information or copyright lines.

**form element:** The element (`<form>`) that wraps a page's input controls and owns the submit trip. When the form submits, the browser bundles its controls' names and values and sends them together.

**functional image:** An image that performs a job, usually as the content of a link. Its alt text names the destination or action, never the picture.

## G

**gap:** The container property that sets the space between neighboring flex items. The container owns the spacing, so the items need no margins of their own.

**generic font family:** A font category rather than a font: `serif`, `sans-serif`, or `monospace`. The browser always owns a font in each category, so a font stack ending in one can never come up empty.

**GET:** The default submit method, which sends a form's name-value pairs in the URL as a query string. It fits requests that are safe to repeat, bookmark, and share, such as searches.

**GIF:** A raster image format limited to 256 colors. It supports simple frame-by-frame animation, which is the main reason it survives.

## H

**head:** The element that holds information about the page, such as its title and character encoding. Nothing inside the head appears in the browser window.

**header cell:** The table cell element (`<th>`) that names a column or a row instead of holding data. Tools that read tables announce a header with every cell it governs.

**header element:** The landmark (`<header>`) that holds a region's introductory content, such as a logo, title, or tagline. Not the same element as `<head>`.

**hex color:** A CSS color value written as `#` plus six characters, read as three pairs for red, green, and blue light, such as `#268080`. The industry-standard way to record exact colors.

**:hover:** The pseudo-class that matches an element while the visitor's pointer rests on it.

**HTML (HyperText Markup Language):** The markup language of the web. HTML elements give a page its structure and meaning.

**HTML comment:** A note wrapped in `<!--` and `-->` that browsers skip entirely. Comments document a file for the humans who read its code.

**HTTP (HyperText Transfer Protocol):** The set of rules browsers and servers follow to request and deliver web pages.

**HTTPS:** The secure version of HTTP. It encrypts traffic between the browser and the server.

**hyperlink:** Text or another element a visitor activates to jump to a different page or resource. The anchor element (`<a>`) with an `href` attribute creates one.

## I

**id attribute:** The attribute that gives one element a unique name on its page, written `id="meeting-times"`. An id value may appear on only one element per page.

**id selector:** The selector that targets the one element carrying a given id, written with a leading hash, such as `#meeting-times`.

**img element:** The empty element (`<img>`) that embeds an image in a page. Its `src` attribute addresses the image file, and its `alt` attribute carries the alt text.

**informative image:** An image that carries content its page needs. Its alt text describes what matters in about a sentence.

**inline element:** An element that flows along inside a line of text instead of starting a new one, such as `<strong>`, `<em>`, or `<a>`.

**inline style:** CSS written into a single element's `style` attribute. It styles that one element only and puts presentation back inside the content file.

**input element:** The empty element (`<input>`) that renders a single form control. Its `type` attribute picks the control's personality: `text`, `email`, `radio`, `checkbox`, and more.

**internal stylesheet:** CSS rules written inside a `<style>` element in a page's head. Its rules reach that one page only.

**Internet:** The global network of connected devices and the physical infrastructure that links them. The web runs on top of the Internet.

**IP address:** A numeric label, such as 91.198.174.192, that identifies a device on a network.

## J

**JPEG:** A raster image format with lossy compression, the standard choice for photographs. It does not support transparency.

**justify-content:** The container property that distributes flex items and leftover space along the main axis, with values such as `flex-start`, `center`, `flex-end`, and `space-between`.

## K

**keyboard navigation:** Operating a page entirely from the keyboard, with the Tab key stepping through its interactive elements. Every element a mouse can operate must be reachable this way, with focus visible at every stop.

## L

**label element:** The element (`<label>`) that holds a form control's visible name. Its `for` attribute matches the control's `id`, so tools announce the label with the control and clicks on the label operate it.

**landmark:** A semantic element that labels a major region of a page, such as `<header>`, `<nav>`, `<main>`, or `<footer>`. Assistive technology builds a jump menu from a page's landmarks.

**legend element:** The element (`<legend>`), written first inside a fieldset, that names the question the group of controls answers. A screen reader announces it alongside each option in the group.

**line-height:** The CSS property that sets the vertical room each line of text occupies. A unitless value multiplies the element's own font size, and 1.5 is a readable default for body text.

**link element:** The empty head element (`<link>`) that connects a page to another file. With `rel="stylesheet"`, its `href` names the stylesheet the page loads.

**list-style:** The CSS property that controls a list's markers. `list-style: none` removes bullets and numbers, the first move in turning a nav list into a navigation bar.

**lossless compression:** File compression that shrinks a file without discarding any data. PNG uses it.

**lossy compression:** File compression that shrinks a file by permanently discarding detail the eye is unlikely to miss. JPEG uses it.

## M

**mailto link:** A link whose `href` value begins with `mailto:` and an email address. Activating it opens the visitor's mail app with the address filled in.

**main axis:** The direction a flex container lays its items along, chosen by `flex-direction`. `justify-content` distributes items along it.

**main element:** The landmark (`<main>`) that holds a page's primary content. Every page uses exactly one.

**margin:** The outermost box model layer: transparent space an element claims outside its border to keep neighboring elements at a distance.

**max-width:** The CSS property that caps how wide a box may grow while letting it shrink in narrower windows. Paired with auto side margins, it builds a centered readable column.

**media feature:** The condition a media query tests, written in parentheses after `@media`. It looks like a declaration but asks a question about the viewport, such as `(max-width: 720px)`.

**media query:** A CSS at-rule, written `@media (condition) { ... }`, whose rules apply only while the screen satisfies the condition, such as a maximum or minimum viewport width.

**mobile-first:** The design order that plans and styles the narrow screen first, letting wider screens be the enhancement. In CSS it reads as base styles for phones plus `min-width` overrides.

## N

**name attribute:** The attribute that labels a control's answer for the trip: submitted data travels as the control's `name` paired with its current value. A control without one sends nothing.

**name-value pair:** One piece of submitted form data: a control's `name` joined to its current value, such as `subject=algebra`. Pairs travel joined by `&`.

**nav element:** The landmark (`<nav>`) that holds a set of major navigation links, conventionally written as a list of links.

**navigation label:** The visible text of a navigation bar link. A good label lets a visitor predict the page behind it before clicking.

**nesting:** Placing elements inside other elements. A nested element must close before the element that contains it closes.

**:nth-child():** The structural pseudo-class that matches elements by position among their siblings, using keywords such as `even` and `odd`. `tbody tr:nth-child(even)` selects a table's even data rows.

## O

**operable:** The POUR principle that every control works for every input. Keyboard reachability and visible focus styles are its core demands.

**ordered list:** The list element (`<ol>`) that numbers its items because their sequence matters, such as the steps of a procedure.

**override:** A rule inside a media query that changes a base rule's value for the widths the query names. An override carries only the differences and sits below the base rule it adjusts.

## P

**padding:** The box model layer between an element's content and its border. The element's background paints it, so padding keeps text from touching the edges of its own box.

**parent element:** An element that directly contains another element. The `<body>` is the parent of a page's top-level landmarks.

**path:** The part of a URL after the domain. It names the specific page or file requested on the server.

**perceivable:** The POUR principle that content must be able to reach every visitor's senses in some form, such as alt text standing in for images and text that contrasts with its background.

**placeholder:** The attribute that shows a gray hint inside an empty form control and disappears once the visitor types. A placeholder may supplement a label but never replace one.

**plain text:** A file format that contains nothing but characters, with no hidden formatting data. HTML files are plain text.

**PNG (Portable Network Graphics):** A raster image format with lossless compression and transparency support. The standard choice for illustrations, screenshots, and any image that needs see-through regions.

**POST:** The submit method that sends a form's name-value pairs inside the request instead of the URL. It fits private or state-changing submissions, such as a signup.

**POUR:** The four principles WCAG organizes its rules under: perceivable, operable, understandable, and robust.

**property:** The aspect of an element a CSS declaration styles, such as `color` or `background-color`. It sits before the colon in a declaration.

**protocol:** A set of rules computers follow to exchange data. HTTP, HTTPS, SMTP, and FTP are protocols.

**prototype:** A clickable mockup built from wireframes wired together, so a test visitor can tap through a site before any code exists.

**pseudo-class:** A selector piece, written with a leading colon, that matches an element by its current state or its position among siblings instead of its identity, such as `:hover`, `:focus`, or `:nth-child()`.

## Q

**query string:** The optional part of a URL that follows a question mark. It carries extra information, such as search terms, to the server.

## R

**radio button:** The form control (`<input type="radio">`) for one choice among a few. Radios that share a `name` form one group, and the group allows a single selection.

**raster image:** An image stored as a grid of colored pixels. Scaling it past its true size turns it soft and blocky. PNG, JPEG, and GIF are raster formats.

**relative URL:** An address that gives directions from the current file, with no protocol or domain, such as `contact.html`. Use it to link between files on the same site.

**rem:** A CSS unit equal to the visitor's base text size, so `1.5rem` means 1.5 times whatever base the visitor's browser is set to. Sizes in rem respect a visitor who raises that base.

**responsive design:** The practice of building one page that adapts its layout to every screen size, built from fluid content and media queries at content-driven breakpoints.

**responsiveness:** The UX principle that a layout adapts to the visitor's screen instead of demanding one screen size.

**RGB:** The color model behind every screen color: a mix of red, green, and blue light. CSS states the mix directly with the `rgb()` function, such as `rgb(38, 128, 128)`.

**robust:** The POUR principle that markup must be valid and semantic enough for any tool to parse, including assistive technology and tools not yet built.

## S

**scope attribute:** The attribute that tells tools what a header cell governs: `scope="col"` for the cells below it, `scope="row"` for the cells beside it.

**screen reader:** Software that reads page content aloud, or renders it as braille, for users who are blind or have low vision.

**search engine:** A software system that finds pages on the web that match what you ask for. It works in three stages: crawling, indexing, and ranking.

**section element:** The landmark (`<section>`) that groups one thematically related chunk of a page under its own heading.

**select element:** The element (`<select>`) that offers one choice among many in a compact menu. Each choice is an `<option>` with its own value, and an untouched menu submits its first option.

**selector:** The part of a CSS rule that names which elements the rule styles.

**selector list:** Several selectors sharing one declaration block, separated by commas, such as `h1, h2`.

**semantic element:** An element whose name describes what its content is, not how it looks. `<nav>`, `<strong>`, and `<figure>` are semantic elements.

**SEO (search engine optimization):** The practice of improving a page so search engines can find, read, and rank it in unpaid results.

**separation of concerns:** The design principle of keeping content and presentation in separate languages and files: HTML says what content is, CSS says how it looks. It lets one stylesheet edit restyle a whole site without touching content.

**server:** A computer that stores websites and sends pages to browsers that request them.

**shorthand property:** A CSS property that sets several longhand properties in one declaration, such as `padding: 12px 24px` or `border: 3px solid #268080`.

**site plan:** The planning document a site is built from: goals, target audience, sitemap, wireframes, navigation plan, and consistency rules, assembled for stakeholders to approve before building.

**sitemap:** A diagram of a site's structure: every page, branching from the home page, with connections showing how the pages relate.

**span element:** The generic inline container (`<span>`). It carries no meaning and marks a run of text for styling or scripting.

**SSL/TLS:** The encryption technology behind HTTPS. It scrambles traffic between the browser and the server so intercepted data cannot be read.

**stress emphasis:** The meaning the `<em>` element marks: the word a reader would stress aloud, which can change what the sentence means. Browsers render it italic.

**strong importance:** The meaning the `<strong>` element marks: content the reader must not miss, such as a warning or deadline. Browsers render it bold.

**structural pseudo-class:** A pseudo-class that matches an element by its position among its siblings instead of its current state. `:nth-child()` is the one this course teaches.

**style element:** The head element (`<style>`) that holds a page's internal stylesheet.

**subdomain:** An optional prefix on a domain name that points to a section of a site, such as `learn` in learn.maricopa.edu.

**SVG (Scalable Vector Graphics):** The web's vector image format. It stays sharp at every size, which makes it ideal for logos, icons, and diagrams.

## T

**table element:** The element (`<table>`) that presents tabular data as a grid of rows and columns. It presents data only: page layout belongs to CSS.

**table row:** The element (`<tr>`) that holds one horizontal run of cells. A table's columns emerge from the position of cells across its rows.

**tabular data:** Content in which every value takes its meaning from two directions at once, its row and its column. The two-axes test that identifies it decides when a table is the right element.

**tag:** An element's name inside angle brackets. An opening tag such as `<p>` starts an element, and a closing tag such as `</p>` ends it.

**target audience:** The people a site is built to serve, described by what they already know, what they come to do, and what would make them leave.

**tbody element:** The element (`<tbody>`) that groups a table's data rows apart from its header row. Browsers build one silently when a file omits it, so writing it keeps the file honest with the page the browser serves.

**text-align:** The CSS property that sets how lines of text sit inside their box: `left`, `center`, or `right`.

**textarea element:** The element (`<textarea>`) that renders a multi-line text box for longer answers. Unlike input it is a container element, and its `rows` attribute suggests a visible height.

**text-decoration:** The CSS property that controls lines drawn on text, such as the underline every browser gives links. Removing link underlines removes a signal visitors rely on.

**text editor:** A program that saves exactly the characters you type and nothing else. Code editors such as VS Code are text editors with extra help for writing code.

**text-transform:** The CSS property that recases text for display, such as `uppercase` for short labels, without changing the characters in the markup.

**thead element:** The element (`<thead>`) that groups a table's header row apart from its data rows, so tools and style rules can treat the namers and the named differently.

**title element:** The head element that names the page. Its text appears in the browser tab, in bookmarks, and as the headline of a search result.

**top-level domain (TLD):** The ending of a domain name, such as .com, .org, .edu, or .gov. Some endings are open to anyone, and others are restricted to certain kinds of organizations.

**transparency:** An image property that lets regions of the image be see-through so the page behind shows. PNG supports it fully, and JPEG does not support it at all.

## U

**understandable:** The POUR principle that content and controls must make sense: plain language, labels that predict what follows, and pages that behave consistently.

**universal selector:** The selector `*`, which matches every element on the page. Its everyday job is delivering `box-sizing: border-box` to a whole stylesheet.

**unordered list:** The list element (`<ul>`) that bullets its items because their order does not matter, such as a collection of accepted donations.

**URL (Uniform Resource Locator):** The full address of a resource on the web. Each part of a URL directs the browser to the right place.

**usability:** The UX principle that visitors can complete their tasks without instructions or guesswork.

**user experience (UX):** The quality of a visitor's whole visit to a site: whether they find what they came for, how much guesswork it takes, and whether they would come back.

**user interface (UI):** The controls and visuals a visitor operates: the buttons, links, menus, and forms, and how each one looks.

## V

**valid markup:** Markup that follows the rules of the HTML standard: required elements present, tags closed, nesting legal. The W3C validator checks for it.

**value:** The setting a CSS declaration assigns to its property, such as `#1a5e5e` in `color: #1a5e5e;`. It sits after the colon in a declaration.

**vector image:** An image stored as drawing instructions instead of pixels, so the computer can redraw it sharp at any size.

**viewport:** The area a browser gives a page to lay out in. On a desktop it matches the window's page area, and on a phone it matches the device only when the page asks with the viewport meta tag.

**viewport meta tag:** The head line `<meta name="viewport" content="width=device-width, initial-scale=1">`, which tells a phone browser to lay the page out at the device's true width instead of a legacy wide canvas.

**VS Code (Visual Studio Code):** The free code editor from Microsoft used throughout this course. It runs on Windows, macOS, and Linux.

## W

**W3C (World Wide Web Consortium):** The organization that maintains the web's standards, including HTML and CSS.

**W3C validator:** The free checking service at validator.w3.org that reports every place a page breaks the HTML standard, by line and column.

**WCAG (Web Content Accessibility Guidelines):** The W3C's standard for accessible web content, organized under the POUR principles and graded in conformance levels A, AA, and AAA.

**web-safe font:** A font installed on nearly every device, such as Arial, Verdana, or Georgia. Web-safe fonts anchor font stacks because a stack can rely on them without downloading anything.

**whitespace collapsing:** The browser behavior that renders any run of spaces, tabs, and line breaks in a file as a single space on the page.

**wireframe:** A grayscale sketch of one page's layout: labeled boxes for each region, with no colors or fonts. Planning draws one at desktop width and one at phone width.

**World Wide Web (the web):** The worldwide collection of linked pages and resources you reach through a browser. The web is one service that runs on the Internet.

## Z

**zebra striping:** The readability pattern that tints alternating table rows so the eye can hold a line across many columns. One rule builds it: `tbody tr:nth-child(even)` with a background color.
