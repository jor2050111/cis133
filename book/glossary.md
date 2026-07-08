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

**alt text:** The text that stands in for an image when its pixels cannot: read aloud by screen readers and shown when the file fails to load. It lives in the `img` element's `alt` attribute.

**article element:** The landmark (`<article>`) that wraps content able to stand alone outside its page, such as a blog post, news story, or review.

**attribute:** A name and value pair written inside an opening tag that configures the element, such as `lang="en"`.

## B

**block-level element:** An element that begins on a new line and claims the page's full width. Headings, paragraphs, and lists are block-level elements.

**body:** The element that holds everything visible in the browser window. All of a page's on-screen content lives inside it.

**browser:** A program that requests pages from web servers and displays them on your screen. Chrome, Edge, Firefox, and Safari are browsers.

## C

**cache:** A browser's local store of recently downloaded page files. The cache lets a repeat visit load without downloading everything again.

**child element:** An element nested directly inside another element. Every element inside a `<header>` is a child of that header.

**client:** Any device that asks a server for something, such as a laptop, phone, or smart TV. The client asks, and the server answers.

**client-server model:** The pattern behind every web interaction. A client asks a server for something, and the server answers.

**cookie:** A small piece of data a website stores in your browser so the site can recognize you on a later visit.

**copyright:** The legal protection a creator automatically holds over their work from the moment it is created. Reusing protected work requires permission or a license.

**Creative Commons:** A family of public licenses an author attaches to a work to spell out what reuse is allowed, such as requiring credit or forbidding commercial use.

**CSS (Cascading Style Sheets):** The stylesheet language of the web. CSS rules control how HTML content looks, including color, spacing, type, and layout.

## D

**decorative image:** An image that adds no content to its page, such as a border strip. It gets a deliberate empty alt (`alt=""`) so screen readers skip it.

**digital certificate:** A file, issued by a trusted authority, that proves a website's identity and enables its encrypted connections.

**div element:** The generic block-level container (`<div>`). It carries no meaning and serves as a hook for styling and scripting when no semantic element fits.

**DNS (Domain Name System):** The Internet's address book. DNS translates a domain name you can read into an IP address computers can route.

**doctype declaration:** The required first line of an HTML document, written `<!DOCTYPE html>`. It tells the browser the file uses modern HTML.

**domain name:** The human-readable name of a website, such as phoenixcollege.edu. You register a domain name so visitors do not need to remember an IP address.

## E

**element:** One piece of page structure, such as a paragraph, heading, or list. Most elements are written as an opening tag, content, and a closing tag.

**empty element:** An element with a single tag and no content or closing tag, such as `<meta>` or `<br>`.

## F

**figcaption element:** The element (`<figcaption>`) that supplies a figure's visible caption. It lives inside a `<figure>`.

**figure element:** The element (`<figure>`) that wraps self-contained illustrative content, such as a chart or diagram, often paired with a `<figcaption>`.

**file extension:** The ending of a file name after the dot, such as `.html` or `.txt`. It tells the computer and the browser what kind of file it is.

**footer element:** The landmark (`<footer>`) that holds a region's closing content, such as contact information or copyright lines.

**functional image:** An image that performs a job, usually as the content of a link. Its alt text names the destination or action, never the picture.

## G

**GIF:** A raster image format limited to 256 colors. It supports simple frame-by-frame animation, which is the main reason it survives.

## H

**head:** The element that holds information about the page, such as its title and character encoding. Nothing inside the head appears in the browser window.

**header element:** The landmark (`<header>`) that holds a region's introductory content, such as a logo, title, or tagline. Not the same element as `<head>`.

**HTML (HyperText Markup Language):** The markup language of the web. HTML elements give a page its structure and meaning.

**HTML comment:** A note wrapped in `<!--` and `-->` that browsers skip entirely. Comments document a file for the humans who read its code.

**HTTP (HyperText Transfer Protocol):** The set of rules browsers and servers follow to request and deliver web pages.

**HTTPS:** The secure version of HTTP. It encrypts traffic between the browser and the server.

**hyperlink:** Text or another element a visitor activates to jump to a different page or resource. The anchor element (`<a>`) with an `href` attribute creates one.

## I

**img element:** The empty element (`<img>`) that embeds an image in a page. Its `src` attribute addresses the image file, and its `alt` attribute carries the alt text.

**informative image:** An image that carries content its page needs. Its alt text describes what matters in about a sentence.

**inline element:** An element that flows along inside a line of text instead of starting a new one, such as `<strong>`, `<em>`, or `<a>`.

**Internet:** The global network of connected devices and the physical infrastructure that links them. The web runs on top of the Internet.

**IP address:** A numeric label, such as 91.198.174.192, that identifies a device on a network.

## J

**JPEG:** A raster image format with lossy compression, the standard choice for photographs. It does not support transparency.

## L

**landmark:** A semantic element that labels a major region of a page, such as `<header>`, `<nav>`, `<main>`, or `<footer>`. Assistive technology builds a jump menu from a page's landmarks.

**lossless compression:** File compression that shrinks a file without discarding any data. PNG uses it.

**lossy compression:** File compression that shrinks a file by permanently discarding detail the eye is unlikely to miss. JPEG uses it.

## M

**mailto link:** A link whose `href` value begins with `mailto:` and an email address. Activating it opens the visitor's mail app with the address filled in.

**main element:** The landmark (`<main>`) that holds a page's primary content. Every page uses exactly one.

## N

**nav element:** The landmark (`<nav>`) that holds a set of major navigation links, conventionally written as a list of links.

**nesting:** Placing elements inside other elements. A nested element must close before the element that contains it closes.

## O

**ordered list:** The list element (`<ol>`) that numbers its items because their sequence matters, such as the steps of a procedure.

## P

**parent element:** An element that directly contains another element. The `<body>` is the parent of a page's top-level landmarks.

**path:** The part of a URL after the domain. It names the specific page or file requested on the server.

**plain text:** A file format that contains nothing but characters, with no hidden formatting data. HTML files are plain text.

**PNG (Portable Network Graphics):** A raster image format with lossless compression and transparency support. The standard choice for illustrations, screenshots, and any image that needs see-through regions.

**protocol:** A set of rules computers follow to exchange data. HTTP, HTTPS, SMTP, and FTP are protocols.

## Q

**query string:** The optional part of a URL that follows a question mark. It carries extra information, such as search terms, to the server.

## R

**raster image:** An image stored as a grid of colored pixels. Scaling it past its true size turns it soft and blocky. PNG, JPEG, and GIF are raster formats.

**relative URL:** An address that gives directions from the current file, with no protocol or domain, such as `contact.html`. Use it to link between files on the same site.

## S

**screen reader:** Software that reads page content aloud, or renders it as braille, for users who are blind or have low vision.

**search engine:** A software system that finds pages on the web that match what you ask for. It works in three stages: crawling, indexing, and ranking.

**section element:** The landmark (`<section>`) that groups one thematically related chunk of a page under its own heading.

**semantic element:** An element whose name describes what its content is, not how it looks. `<nav>`, `<strong>`, and `<figure>` are semantic elements.

**SEO (search engine optimization):** The practice of improving a page so search engines can find, read, and rank it in unpaid results.

**server:** A computer that stores websites and sends pages to browsers that request them.

**span element:** The generic inline container (`<span>`). It carries no meaning and marks a run of text for styling or scripting.

**SSL/TLS:** The encryption technology behind HTTPS. It scrambles traffic between the browser and the server so intercepted data cannot be read.

**stress emphasis:** The meaning the `<em>` element marks: the word a reader would stress aloud, which can change what the sentence means. Browsers render it italic.

**strong importance:** The meaning the `<strong>` element marks: content the reader must not miss, such as a warning or deadline. Browsers render it bold.

**subdomain:** An optional prefix on a domain name that points to a section of a site, such as `learn` in learn.maricopa.edu.

**SVG (Scalable Vector Graphics):** The web's vector image format. It stays sharp at every size, which makes it ideal for logos, icons, and diagrams.

## T

**tag:** An element's name inside angle brackets. An opening tag such as `<p>` starts an element, and a closing tag such as `</p>` ends it.

**text editor:** A program that saves exactly the characters you type and nothing else. Code editors such as VS Code are text editors with extra help for writing code.

**title element:** The head element that names the page. Its text appears in the browser tab, in bookmarks, and as the headline of a search result.

**top-level domain (TLD):** The ending of a domain name, such as .com, .org, .edu, or .gov. Some endings are open to anyone, and others are restricted to certain kinds of organizations.

**transparency:** An image property that lets regions of the image be see-through so the page behind shows. PNG supports it fully, and JPEG does not support it at all.

## U

**unordered list:** The list element (`<ul>`) that bullets its items because their order does not matter, such as a collection of accepted donations.

**URL (Uniform Resource Locator):** The full address of a resource on the web. Each part of a URL directs the browser to the right place.

## V

**valid markup:** Markup that follows the rules of the HTML standard: required elements present, tags closed, nesting legal. The W3C validator checks for it.

**vector image:** An image stored as drawing instructions instead of pixels, so the computer can redraw it sharp at any size.

**VS Code (Visual Studio Code):** The free code editor from Microsoft used throughout this course. It runs on Windows, macOS, and Linux.

## W

**W3C (World Wide Web Consortium):** The organization that maintains the web's standards, including HTML and CSS.

**W3C validator:** The free checking service at validator.w3.org that reports every place a page breaks the HTML standard, by line and column.

**whitespace collapsing:** The browser behavior that renders any run of spaces, tabs, and line breaks in a file as a single space on the page.

**World Wide Web (the web):** The worldwide collection of linked pages and resources you reach through a browser. The web is one service that runs on the Internet.
