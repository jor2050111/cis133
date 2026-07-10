# Chapter 1: The Internet and the World Wide Web

You tap a link on your phone and a page appears in under a second. In that moment, your phone asked a directory service to translate a name into a number. It sent a request across fiber optic cable, maybe under an ocean. A computer you will never see found the page and sent it back. Your browser turned the response into text, color, and images. All of that happened faster than you can blink twice.

Web developers work inside this system every day. When you build a page, you decide what a server will send. When you name a file, you shape a URL someone will type or share. When you pick sources for site content, you decide what your visitors will trust. CIS133 exists to make you the person behind the page instead of the person in front of it, and that starts with a working map of the territory.

This chapter builds that map. You will separate the Internet from the web, since they are not the same thing. You will follow a page request from a typed address to a rendered page. You will break URLs into parts and see how DNS connects names to numbers. Then you will practice two judgment skills every developer needs: finding information you can trust, and using the web ethically and safely. No prior experience is expected anywhere in this chapter.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None. This chapter starts from zero.
* **Deliverables:** Skills Lab 1A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-1.1 (Understand):** Explain how the Internet, the web, browsers, and servers work together to deliver a web page
* **MLO-1.2 (Understand):** Describe how IP addresses, DNS, domain names, and the parts of a URL work together to locate a page on the web
* **MLO-1.3 (Analyze):** Compare web sources and practices for reliability, authorship, security, and ethical use when choosing what to trust on a project

---

## 1.1 The Internet and the World Wide Web

People say "the Internet" and "the web" as if they were the same thing. They are not, and the difference matters to you as a developer. One is the road system. The other is one kind of traffic that travels on it.

The **Internet** is the global network of connected devices and the physical infrastructure that links them. That infrastructure is surprisingly physical: copper wire, fiber optic cable, cell towers, and data centers. Thousands of miles of cable run along the ocean floor and carry almost all traffic between continents. Even a wireless connection only stays wireless until the nearest tower or router. From there, your data travels on cable like everything else.

The **World Wide Web** (the web) is the worldwide collection of linked pages and resources you reach through a browser. The web is one service that runs on the Internet. Email is another. File transfer is another. When you check your grades in Canvas, you are using the web. When your phone syncs email in the background, that is the Internet at work without the web.

The two even have different birthdays. The Internet grew out of ARPANET, a research network that made its first connection in 1969. The web arrived more than twenty years later, in 1991, when Tim Berners-Lee created the first web page. He also created the two technologies that made it possible: HTML to write pages and HTTP to deliver them. You will spend most of this course working with HTML and its styling partner, CSS.

| Year | Milestone |
| ---- | --------- |
| 1969 | ARPANET makes the first network connection |
| 1971 | The first network email is sent |
| 1991 | Tim Berners-Lee publishes the first web page |
| 1994 | Early search engines begin indexing the web |

### Servers and Clients

Every web interaction has two sides. A **server** is a computer that stores websites and sends pages to browsers that request them. Servers stay connected to the Internet around the clock, waiting for requests. A **client** is any device that asks a server for something: your laptop, your phone, a smart TV. The client asks. The server answers. That request-and-response pattern is called the **client-server model**, and it runs the entire web.

Think about what this means for your future sites. Your visitors will arrive on large monitors, small phones, fast fiber, and slow cellular connections. Every one of them is a client your server-side files must serve well. Later chapters teach you how to design for that variety.

### Browsers

A **browser** is a program that requests pages from web servers and displays them on your screen. Chrome, Edge, Firefox, and Safari are browsers. Each one does three jobs. It sends your request to the right server. It receives the files the server returns. Then it renders those files, which means it turns HTML and CSS code into the page you see.

Browsers share the same core controls: an address bar, back and forward buttons, a refresh button, bookmarks, and tabs. Modern address bars double as search boxes. Browsers also keep a **cache**, a local store of recently downloaded page files. The cache lets a repeat visit load without downloading everything again. The refresh button tells the browser to check with the server for newer copies, though files that have not changed may still come from the cache.

Here is the developer's angle. You control your code, but you never control which browser a visitor uses. Some visitors run the newest Chrome. Others run an older browser on an aging laptop. Writing standard, valid code is how you serve all of them, and Chapter 2 introduces the validator that checks your work.

Browsers will also let you look behind the page. Every browser can show you the code it received from the server, and most include a full inspection toolkit called browser DevTools that you will start using in Chapter 2. The next exercise gives you a first look.

### Try It Yourself 1.1: See What the Server Sent 🛠️

**Predict:** A rendered web page shows text, colors, and images. If you ask the browser to show you the page's source instead, what do you expect to see? Words? Code? Both?

**Run:** Visit any website. Right-click an empty part of the page and choose View Page Source (on Safari, enable the Develop menu first, or try another browser). Scroll through what appears. Find one piece of text you can also see on the rendered page.

**Explain:** In 1-2 sentences, explain what the browser did between receiving this text and showing you the finished page. Which of the browser's three jobs is that?

### The Round Trip of a Page Request

Put the pieces together and follow one request from start to finish:

1. You type an address into the browser or tap a link.
2. The browser looks up which server holds the page (Section 1.2 covers how).
3. The browser sends a request across the Internet to that server.
4. The server finds the requested page and sends it back.
5. The browser renders the returned HTML and CSS into the page you see.

The exchange at the center of that trip looks like a short conversation:

```text
Browser request:  GET /academics/programs
                  Host: www.phoenixcollege.edu

Server response:  200 OK
                  (the HTML for the page follows)
```

The whole round trip usually finishes in well under a second. When it fails, the browser shows an error instead, and the kind of error tells you which step broke. You will use that clue in Section 1.2.

### Try It Yourself 1.2: Break the Round Trip 🛠️

**Predict:** Suppose you turn on airplane mode and then click refresh on a page you already have open. Will the browser show the same page, a blank page, or an error? Write down your prediction and your reasoning.

**Run:** Open any website. Turn on airplane mode (or turn off Wi-Fi). Refresh the page and note what the browser shows. Then reconnect and refresh again.

**Explain:** In 1-2 sentences, explain what your result says about where pages live. Use the words client and server in your answer. If the page still appeared after your refresh, name the concept from the Browsers subsection that explains it.

### Quick Check 1.1 ✅

1. A friend says "the Internet went down" when a single website stops loading. Using the client-server model, give one other explanation for what might have failed.
2. Explain the difference between the Internet and the web in your own words, without using the word "network."
3. The Internet is about twenty years older than the web. Using the milestone table, name one way people communicated over the Internet before the web existed, and one thing the web added.

---

## 1.2 Web Addresses: From IP Addresses to URLs

Step 2 of the round trip hid some machinery: the browser "looks up which server holds the page." This section opens that box. The web has two addressing systems, one built for computers and one built for people, plus a translation service that connects them.

### IP Addresses

Every device on the Internet needs an address, just as every house on a street needs one. An **IP address** is a numeric label, such as 91.198.174.192, that identifies a device on a network. Routers use IP addresses to move each request and response to the right machine. The common format you will see is four numbers separated by dots. A newer format called IPv6 uses longer addresses because the Internet outgrew the original supply, but the idea is the same: an address routers can deliver to. In practice a home router often shares one public address across the whole household, which is part of how the original supply stretched so far.

Numbers work well for machines and poorly for people. Nobody wants to memorize 91.198.174.192 to look something up. That problem led to domain names.

### Domain Names

A **domain name** is the human-readable name of a website, such as phoenixcollege.edu. Read one from right to left and it breaks into parts:

```text
learn.maricopa.edu

.edu      top-level domain (the category)
maricopa  domain name (the organization)
learn     subdomain (a named section, optional)
```

The **top-level domain** (TLD) is the ending, such as .com, .org, .edu, or .gov. Some endings are open to anyone. Others are restricted, which is why a .gov or .edu address carries weight when you evaluate sources later in this chapter. The middle part is the registered name itself. A **subdomain** is an optional prefix that points to a section of a site, like `learn` in learn.maricopa.edu, the Canvas system you use for this course.

One more practical fact: nobody owns a domain name outright. You rent it, usually by the year, through a company called a registrar. If the renewal lapses, the name goes back on the market.

### DNS: The Translation Service

Domain names exist for people, and IP addresses exist for machines, so something must translate between them. **DNS** (Domain Name System) is the Internet's address book. It translates a domain name you can read into an IP address computers can route.

Every time you visit a site by name, DNS works in the background:

1. You request phoenixcollege.edu.
2. Your browser asks a DNS server for that name's IP address.
3. The DNS server answers with the number, such as 34.193.144.129.
4. Your browser sends the page request to the server at that address.

The lookup takes milliseconds, and your browser remembers recent answers so repeat visits skip the line. You mostly notice DNS when it fails. Mistype a domain and no DNS server can answer the lookup. The Try It below stages two failures side by side, so you can compare what the browser does with each.

### URLs: The Complete Address

With domains in hand, you can read a complete web address. A **URL** (Uniform Resource Locator) is the full address of a resource on the web. Each part directs the browser to the right place:

```text
https://www.phoenixcollege.edu/academics/programs

https://              protocol: how to talk to the server
www                   subdomain
phoenixcollege        domain name
.edu                  top-level domain
/academics/programs   path: which page on the server
```

The **path** is the part after the domain. It names the specific page or file you want, the way an apartment number narrows down a street address. A URL with no path, like `https://www.phoenixcollege.edu`, asks for the site's home page. Some URLs also carry a **query string**, a `?` followed by extra information, such as the search terms in `https://duckduckgo.com/?q=phoenix+college`. You will build multi-page sites later in this course, and every page you add creates a new path.

The **protocol** at the front names the set of rules the browser and server will follow. **HTTP** (HyperText Transfer Protocol) is the set of rules browsers and servers follow to request and deliver web pages. **HTTPS** is the secure version of HTTP that encrypts traffic between the browser and the server. Section 1.4 explains why that encryption matters.

The web's protocols are two members of a larger family. Each protocol on the Internet handles one kind of job:

| Protocol | Job on the Internet |
| -------- | ------------------- |
| HTTP | Requests and delivers web pages |
| HTTPS | Does HTTP's job over an encrypted connection |
| SMTP | Moves email between mail servers |
| FTP | Transfers files between computers |

You will meet the file transfer family again in Chapter 12, when you publish your final project site to a server using a secure transfer method.

### Try It Yourself 1.3: Two Addresses, Two Errors 🛠️

**Predict:** Address one is `https://cis133.invalid`, a domain that does not exist. Address two is a real site with a fake path: `https://www.w3.org/this-page-does-not-exist`. Will the browser show the same error for both? If not, which step of the round trip fails in each case?

**Run:** Type each address into your browser, one at a time, and read each result carefully. Note the exact wording the browser or the site uses.

**Explain:** In 1-2 sentences, use the round trip's steps to explain each result: how far did each request get, and what stopped it?

### Quick Check 1.2 ✅

1. Break the URL `https://scholar.google.com/scholar?q=web+accessibility` into its parts: protocol, subdomain, domain name, top-level domain, path, and query string.
2. Your roommate asks why the web needs both domain names and IP addresses. Answer in two sentences.
3. A page that loaded yesterday shows "server not found" today after you typed the address by hand. Which system most likely failed to find an answer, and what is the first thing you would check?

---

## 1.3 Finding and Evaluating Information

The web holds more pages than any person could read, so two skills separate skilled users from lost ones. The first is knowing how search engines choose what you see. The second is judging whether what you found deserves your trust. Both skills feed directly into your work in this course, because the sites you build will cite, quote, and link to sources.

### How Search Engines Work

A **search engine** is a software system that finds pages on the web that match what you ask for. Google, Bing, and DuckDuckGo are search engines. A search engine is not the web itself. It is a guide to the web that works in three stages:

1. Crawling. Automated programs follow links from page to page, reading what they find.
2. Indexing. The engine stores what the crawlers found in a giant, searchable catalog.
3. Ranking. When you search, the engine sorts matching pages by how useful it predicts each one will be.

Ranking is the stage with consequences. Every engine uses its own recipe of signals: how well the page matches your words, how many other sites link to it, how fresh it is, and hundreds more. No two engines weigh the signals the same way. The results page mixes those ranked findings with paid advertisements, and part of reading results well is telling the two apart.

Search predates the web itself, and each generation of engines added a piece of what you now take for granted:

| Year | Engine | What it added |
| ---- | ------ | ------------- |
| 1990 | Archie | Searched file archives before the web went public |
| 1994 | WebCrawler | First search of the full text of web pages |
| 1998 | Google | Ranked results partly by the links pointing at each page |
| 2008 | DuckDuckGo | Search built around not tracking the searcher |

The link-counting idea mattered most. Treating a link as a vote of confidence made rankings harder to fake and made the modern search economy possible. It also gave developers a reason to care how other sites link to theirs.

### SEO: Why Developers Care

**SEO** (search engine optimization) is the practice of improving a page so search engines can find, read, and rank it in unpaid results. Marketing teams treat SEO as a specialty, but a share of it lands on the developer. Clear page titles, descriptive headings, meaningful link text, and well-structured HTML all help crawlers read a page correctly. In Chapter 3 you will write semantic HTML, and search engines are one of its main audiences. Good structure is not a trick. It is honest labeling that machines and people both reward.

### Sharpening a Search

Search engines also accept operators, small additions that narrow the field. Two are worth learning now:

```text
electronics recycling site:.gov     only .gov sites
"electronic waste" recycling        this exact phrase
```

The `site:` operator limits results to one domain or ending, which is a fast way to find government or campus sources. Quotation marks demand an exact phrase. Layer them as needed.

!!! tip
    Search engines also offer specialized views. A News tab favors journalistic sources, and Google Scholar (scholar.google.com) searches academic work. When a claim matters, move up to the more vetted view before you rely on it.

### Evaluating What You Find

Ranking high does not make a page true. Anyone can publish anything, and software can now generate convincing text with no author behind it at all. Before you rely on a page, and long before you cite one on a site you build, test it against five questions:

* **Author:** Is a person or organization named and identifiable? A named author with a track record beats "Editorial Team" or no byline at all.
* **Host:** Who runs the site? Restricted endings like .gov and .edu signal institutional review. A .com or .org can be excellent too, but check who is behind it.
* **Currency:** When was it published or updated? A 2019 page about recycling drop-off locations may send you somewhere that closed.
* **Purpose:** Is the page informing you, or selling and persuading? Bias does not disqualify a source, but you must account for it.
* **Evidence:** Does the page cite sources you can check? Watch for warning signs of machine-generated filler: repetitive phrasing, vague claims, and zero citations.

The strongest test spans sources instead of inspecting one alone. Cross-reference the claim: if several unrelated, reputable sites agree, your confidence rises. If a claim appears in exactly one place, treat it as unconfirmed. Detection tools that promise to spot AI-generated text exist, but they guess wrong often enough that the five questions above remain your primary instrument.

### Try It Yourself 1.4: Two Engines, One Question 🛠️

**Predict:** If you run the same search on Google and DuckDuckGo, how similar will the top three unpaid results be: identical, mostly the same, or mostly different? Commit to a prediction.

**Run:** Search `electronics recycling phoenix` on both engines. Compare the top three unpaid results on each, and note any results marked as ads or sponsored.

**Explain:** In 1-2 sentences, explain what your comparison reveals about how ranking works. Which stage of the search engine's three-stage process produced the difference? If your results mostly matched, explain what that similarity suggests instead.

### Quick Check 1.3 ✅

1. A well-designed page ranks #1 for your search but names no author, shows no date, and cites no sources. Walk through which of the five evaluation questions it fails.
2. A developer wants a new page to rank well in unpaid results. Name two things the developer controls that help a search engine read and rank the page correctly.
3. Write a search that finds pages about web accessibility only on university sites.

---

## 1.4 Ethics, Security, and Privacy on the Web

The web hands you more free text, images, music, and video than any library in history. It also hands you the ability to copy any of it in seconds. What you may do and what you should do are separate questions, and developers face both every time they build a page. This section covers the ethics of using what you find, the systems that keep traffic secure, and the users the web too often leaves out.

### Copyright and Fair Use of Web Content

Start with the rule that surprises people: **copyright** protection is automatic. The moment someone writes a paragraph, snaps a photo, or records a song, they own it. No copyright symbol is required. Finding an image on the web gives you the technical ability to copy it, not the right to use it.

So ask before you take. Is it acceptable to copy someone's graphic onto your site? Their music into your video? Their page design or their essay into your work? By default, no. You need permission, and the ethical developer looks for it instead of hoping nobody notices.

Permission often already exists in the form of a license. A **Creative Commons** license is a public license an author attaches to a work that spells out what reuse is allowed, such as requiring credit or forbidding commercial use. This textbook practices what it preaches: it adapts material from *HTML & CSS Simply Explained* by Brad Olsen under a Creative Commons BY-NC license, with credit on the cover page. When you reuse licensed work, follow the license and give credit:

```text
Photo: "Saguaro at dusk" by R. Alvarez,
CC BY 4.0, via Wikimedia Commons
```

Ethics online reaches past copyright. Consider three examples: insulting someone on your site, linking to others in a derogatory way, or passing off machine-generated text as your own analysis. All three fail the same test. Would you stand behind the page if your name were on it? On every page you build in this course, your name is on it.

### Security: HTTPS and Digital Certificates

Section 1.2 introduced HTTPS as the secure protocol. Here is what it protects you from. Traffic between your browser and a server passes through many machines you do not control. Over plain HTTP, anyone along the way can read that traffic, including passwords and card numbers. HTTPS encrypts the conversation using a technology called **SSL/TLS**, so intercepted traffic reads as gibberish.

Encryption alone is not enough. You also need proof that the server on the other end is who it claims to be. A **digital certificate** is a file, issued by a trusted authority, that proves a website's identity and enables its encrypted connections. Your browser checks the certificate on every HTTPS visit. When a certificate is missing, expired, or does not match the site, the browser throws a full-page warning instead. Take those warnings seriously.

The developer's rule is simple: never send private information through a page whose address starts with `http://`, and never ask your visitors to. When your final project collects anything from a user, it should travel over HTTPS.

!!! warning
    When the browser shows a full-page certificate warning, do not click past it, and never enter a password or payment details on the other side. The warning means the site's identity could not be verified.

### Privacy

Security protects data in transit. Privacy asks a different question: what happens to data after it arrives? Sites routinely log which pages you visit, what you search, and what you click. One common tool for that is the **cookie**, a small piece of data a site stores in your browser so it can recognize you on your next visit. Cookies keep you logged in and keep carts full between visits. The same mechanism also lets advertising networks follow you from site to site, which is why browsers now give you controls over which cookies to allow.

As a user, you already manage privacy with settings and common sense. This course adds the other role. In Chapter 11 you will build forms that collect user input, and every field you add is a promise to handle someone's information responsibly. Collect only what the page needs, and say what you will do with it.

### Accessibility: The Web for Every User

The web's founding promise is access for everyone, and that includes people who see, hear, and move differently. A **screen reader** is software that reads page content aloud, or renders it as braille, for users who are blind or have low vision. Screen readers can only describe what the page's code tells them. An image with no text description is invisible to them. A page with a scrambled structure reads like a shuffled deck.

Laws in many countries require accessible websites for the same reason buildings require ramps. In this book, accessibility is not an afterthought chapter you may skim. You will write text alternatives for images in Chapter 3, and Chapter 9 is devoted to accessibility standards and testing. Every page you build from here forward gets judged partly on who can use it.

### Try It Yourself 1.5: Read the Padlock 🛠️

**Predict:** Click the padlock (or tune) icon next to a site's address and you will see connection details. What do you expect it to tell you: that the site is safe, that the connection is encrypted, or who issued the site's certificate? More than one may be right.

**Run:** Visit `https://www.phoenixcollege.edu`, click the padlock or tune icon in the address bar, and open the connection or certificate details. Note who issued the certificate and when it expires.

**Explain:** In 1-2 sentences, explain what the padlock does and does not promise. Does an encrypted connection make a site's content trustworthy?

### Quick Check 1.4 ✅

1. A classmate found the perfect photo for their project site and says "it was on a public web page, so it's public domain." Correct the misunderstanding in two sentences.
2. Explain the difference between what HTTPS protects and what a digital certificate proves.
3. Give one example of a page choice that would lock a screen reader user out of content, and name the chapter of this book that addresses it.

---

## 1.5 Summary and Retrieval 💡

### Key Concepts

* The Internet is the physical global network. The web is one service running on it: linked pages delivered over HTTP and HTTPS. The web arrived in 1991, more than two decades after the Internet's first connections.
* The web runs on the client-server model. Clients (browsers on your devices) request pages. Servers store sites and answer requests around the clock. Browsers then render the returned HTML and CSS into what you see.
* Every device has a numeric IP address. Domain names give those numbers human-readable names, and DNS translates between the two on every visit. A URL combines protocol, subdomain, domain name, top-level domain, and path into one complete address.
* Search engines crawl, index, and rank the web, and each engine ranks differently. Evaluate what you find with five questions: author, host, currency, purpose, and evidence, then cross-reference claims across unrelated sources.
* Copyright protects web content automatically, so reuse requires permission or a license such as Creative Commons, plus credit. HTTPS with a valid digital certificate encrypts traffic and verifies identity. Accessible pages serve users who rely on tools like screen readers.

### Key Terms

See course glossary for full definitions

* Internet, World Wide Web, server, client, client-server model, browser, cache (Section 1.1)
* IP address, domain name, top-level domain, subdomain, DNS, URL, path, query string, protocol, HTTP, HTTPS (Section 1.2)
* search engine, SEO (Section 1.3)
* copyright, Creative Commons, SSL/TLS, digital certificate, cookie, screen reader (Section 1.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. List the five steps of a page request's round trip, from typing an address to seeing the page.
2. Explain what DNS does and what you would see in the browser if it could not do its job.
3. Break a URL of your choosing into its five parts from memory.
4. Name the five source-evaluation questions and state, in one sentence, why ranking position is not one of them.
5. Explain to an imaginary client why their site's contact form must use HTTPS.

---

## 1.6 Skills Lab 1A: Trace the Web, Then Judge It

**Goal:** Trace how pages reach your browser, break real URLs into their parts, and recommend trustworthy sources for a campus club's website project.

**Dataset:** Provided files in `assets/code/chapter-01/` from the course data pack: `skills-lab-1a-worksheet.txt` (your answer file), `url-inventory.txt` (12 URLs to dissect), and `source-profiles.txt` (five source profiles for Part 3). Download the data pack from Canvas, extract it, and work at the extracted `cis133` root. Open each file in any text editor. Never retype the file contents.

### Part 1: Foundation (Aligns with MLO-1.1)

Work in `skills-lab-1a-worksheet.txt`, which contains numbered spaces for every answer below.

1. The worksheet lists the five steps of a page request in scrambled order. Number them into the correct sequence.
2. In 2-3 sentences of your own words, explain the difference between the Internet and the web to someone who uses both every day but has never thought about it.
3. The worksheet describes three short scenarios. For each, identify which device is acting as the client and which as the server, and note the clue that told you.

### Part 2: Application (Aligns with MLO-1.2)

1. Choose six URLs from `url-inventory.txt`. Include at least one URL that does not use `https://`, at least one that contains a query string, and at least one that lacks a subdomain or a path.
2. For each chosen URL, fill in the worksheet's dissection table: protocol, subdomain, domain name, top-level domain, path, and query string. Write NONE for any part a URL does not have.
3. Two of your six URLs should share something: pick any pair from your set with the same top-level domain or the same domain name. In 2-3 sentences, state what the shared part tells you and what the differing parts change about where the browser goes.

### Part 3: Extension (Aligns with MLO-1.3)

Your campus computer club is building a resource page about recycling old electronics, and the club president asked you to vet the research. `source-profiles.txt` describes five web sources the club found.

1. Choose three of the five profiles. Score each one against the chapter's five evaluation questions (author, host, currency, purpose, evidence), one short line per question, in the worksheet's evaluation grid.
2. Write a recommendation memo to the club president (about 150-200 words): name the source(s) the club should use, the source(s) it should reject, and the evidence that decided each call.
3. One profile offers images the club wants to reuse on its page. Using this chapter's copyright section, tell the president whether the club may use them, and what the club must do if it does.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. In Part 2, at least one of your URLs lacked a subdomain or a path. Citing that specific URL, explain what the browser does when those parts are absent and why the URL still works.
2. In Part 3, which single evaluation question did the most work in separating your recommended source from your rejected one? Justify the choice, and describe what the rejected source would have to change for you to reverse your decision.

**Submission:** Submit your completed worksheet as one file named `skills-lab-1a-lastname.txt`. Keep every numbered answer under its part heading, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 1A

Every Skills Lab in this book is graded with the same 16-point rubric.
Bookmark the [Skills Lab Rubric](../skills-lab-rubric.md) page for
quick reference in later chapters.

--8<-- "skills-lab-rubric.md:rubric"

---

## 1.7 Review Questions 🔄️

1. **Remember:** List the five parts of a full URL in order and state what each part tells the browser.

2. **Understand:** A page fails to load. Explain how you would tell a DNS failure apart from a missing page on a working server, and which step of the round trip breaks in each case.

3. **Apply:** Break the URL `https://library.canyonstate.edu/guides/citations` into its parts, then rewrite it so it would request that site's home page instead.

4. **Analyze:** Two pages cover the same topic. One is a dated university guide by a named librarian that cites its sources. The other is an undated, unsigned page that ranks higher in your search. Compare the two using the five evaluation questions and state which you would cite on a client's site.

---

## Further Reading 📖

* [MDN: How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) - A beginner-level walkthrough of clients, servers, DNS, and what happens when you request a page.
* [Cloudflare Learning Center: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/) - A clear, illustrated explanation of the Domain Name System and each step of a lookup.
* [Google: How Search Works](https://www.google.com/search/howsearchworks/) - Google's own plain-language tour of crawling, indexing, and ranking.
* [W3C: Ethical Web Principles](https://www.w3.org/TR/ethical-web-principles/) - The web standards body's short statement of what the web should do for its users, including privacy and accessibility.
* [Creative Commons: About the licenses](https://creativecommons.org/licenses/) - The license family this textbook itself uses, explained by the organization that maintains it.

---

## Looking Ahead ⏩

You can now read the web's map: what the Internet carries, how an address finds a server, and how a page makes its round trip. In Chapter 2 you cross to the other side of that trip: you will set up VS Code, write your first HTML document, and check it with the W3C validator. The pages you request today become pages you build next week.
