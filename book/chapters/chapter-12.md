# Chapter 12: Scripting Concepts and Publishing

The join page shipped, and sign-ups already beat the paper scraps. At Tuesday's meeting the officers say thank you, and then they ask the question every stakeholder saves for last: "It works on your machine. When can everyone see it?" The question is fair. Every page you have built lives at a `file://` address, and Chapter 2 named what that address is: your private workshop, readable by exactly one visitor. The club asked for a website, and the web has not met it yet.

This last chapter pays three debts at once. The join page admits the first one right on the page: the officers still owe a behind-the-scenes piece that stores sign-ups. This chapter explains that piece, from the scripts a browser runs to the server work no browser can do. The site plan holds the second debt: Chapter 7 promised six pages, five exist, and the missing one is the front door itself. The whole course carries the third. Chapter 2 promised these files would move to a web server and earn their `https://`, and this is Chapter 12.

You will read your first scripts and watch them run. You will hear the server's half of the web in concept, no server required. You will learn what a web host does, why every link you ever wrote survives the move, and how a pre-flight check protects a site before anything goes public. Then Skills Lab 12A builds the home page, attaches the course's one script, and ships the club's site to a live address. The officers' question gets its answer: everyone, now.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapters 1-11 (the client-server model from Chapter 1, the club site the labs have built, the checking stack from Chapters 2, 4, and 9, and Chapter 8's device-mode habit)
* **Deliverables:** Skills Lab 12A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **12.1 (Understand):** Illustrate what scripting adds to a site: client-side behavior in the browser and server-side processing in concept (Sections 12.1-12.2)
* **12.2 (Apply):** Perform the full pre-flight check and publish the site to a web server with secure file transfer (Sections 12.3-12.4)
* **12.3 (Create):** Produce the complete multi-page club site: the home page, six-page navigation, and every standard the course taught (Sections 12.3-12.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO VI (Apply):** Apply file transfer protocols to upload web pages to a web server
* **CLO XI (Understand):** Illustrate basic scripting concepts in web development
* **CLO XII (Create):** Produce a multi-page website incorporating learned techniques

---

## 12.1 What Scripting Adds: The Client's Half

Every page you own runs on two languages with a clean split. HTML says what content is, and CSS says how it looks. Chapter 3 called that split the division of labor, and it has held for ten chapters.

The web has a third layer, and the course saved it for last. **JavaScript** is the scripting language of the web, and its layer is behavior: the page acting after it loads. Structure, presentation, behavior.

A page without a script sits still once the browser draws it. A page with one can answer a click, rewrite its own text, and know what day it is. You use pages like that every day: a search box that suggests while you type, a map that pans under your finger, or a learning system that marks an item done. Behind every one of those moments, a script is running.

One expectation before the first script. This chapter is a preview, not a tutorial. You will read scripts, run them, and say what ran where. Writing them is a later course's work. Reading turns out to be most of the skill here, because the scripts this course ships are short enough to read whole.

### The Script Element and the One Script We Ship

The **script element** (`<script>`) attaches the behavior layer to a page. It can hold script directly, the way Chapter 4's style element held CSS. The same argument sends both languages to their own files: an external file serves every page that links it and keeps each language in its own home. The external form takes one attribute: `src` names the script file, the way an img's src names its image.

```html
    <!-- A script travels like a stylesheet: in its own file,
         attached by one element. It sits just before the closing
         body tag so every element above it already exists when
         it runs. -->
    <script src="footer-year.js"></script>
</body>
```

The placement gets one mention because the lab depends on it. A script acts on the page's elements, and the browser builds the page from the top down. A script element just before `</body>` runs after everything above it exists.

Here is the file that example names: the one script the club's site will ship. Read it before anything runs it.

```js
/* Writes the current year into the footer, so nobody has to edit
   the site every January. The page must give the script two
   things: a span with id="footer-year" where the year belongs,
   and a script element for this file just before the closing
   body tag, so the span exists by the time this line runs. */

document.getElementById("footer-year").textContent = new Date().getFullYear();
```

One line of working code, readable left to right. `document` is the page itself. `getElementById("footer-year")` finds the one element carrying that id, unique per page, the same rule the label contract leaned on in Chapter 11. `.textContent` is that element's own text, ready to be replaced.

And `new Date().getFullYear()` asks the machine running the script for the current year. Put together: find the span, write this year into it.

The script's comment states its contract, and here is the page's half of it, the shape the lab will build. The span is empty on purpose. The script supplies the digits, so the markup never goes stale.

```html
<!-- The page's half of the contract: the span the script fills,
     then the script element that loads the file. The &copy;
     code is how HTML writes the © mark. -->
<footer>
    <p>&copy; <span id="footer-year"></span> PC Computer Club</p>
</footer>
<script src="footer-year.js"></script>
```

Nothing here upsets the checking stack. The playground page validates with zero messages, script element included, and the home page the lab builds can reach the same zero.

### Whose Machine Runs It

Now the question that matters more than the syntax: which machine runs it? The visitor's. Chapter 1's client-server model returns by name here. The server stores and sends files, and the browser, the client, runs whatever scripts those files attach. Scripting that runs in the visitor's browser is **client-side scripting**, and it is why this footer needs no January edit: every visitor's machine computes the year fresh at every visit.

Client-side scripts do three kinds of work. They respond to events, such as clicks and typing. They read and change the page after it loads. And they know visit-time facts, such as today's date.

You have already watched built-in client-side logic without naming it: the browser's refusal in TIY 11.4 checked your form's claims before the trip started, on your machine. A script lets a page add behavior the browser does not build in.

Reading an unfamiliar script comes down to three questions, and the answers sit in predictable places:

| The question | Where the answer sits |
| --- | --- |
| What does it touch? | The ids it looks up with `getElementById` |
| What does it do? | The writes, such as a `textContent` replacement |
| When does it run? | At load, or on an event a listener names |

The playground in your pack shows all three kinds of work, and it teaches best if you predict before you read the script.

### Try It Yourself 12.1: The Button Does Something 🛠️

**Predict:** Open `assets/code/chapter-12/script-playground.html` in VS Code and read the page, not the script. Demo 1 is a paragraph and a button labeled Press me, and one script element sits at the bottom. Write down what you think pressing the button will do, and which machine will do it.

**Run:** Open the page in the browser and press the button. Then open `playground-script.js` and find the lines that did what you watched.

**Explain:** In 1-2 sentences, name the event the script waited for and the change it made, plus whose machine did the work.

The paragraph began as "Nothing has happened yet." One press later it read "You pressed the button, and this line changed." Three lines did it:

```js
demoButton.addEventListener("click", function () {
    statusLine.textContent = "You pressed the button, and this line changed.";
});
```

Read them with the three questions. `addEventListener` names the event as a plain word, `click`, and hands over the work to do when it happens. The work is a `textContent` replacement, the same move the footer script makes. Notice the names carrying the documentation, too: `demoButton`, `statusLine`. Semantic naming survived the change of language.

And Demo 3 never waited for you at all. By the time the page appeared, its last line already showed today's date:

```js
visitDateLine.textContent = "You opened this page on " + new Date().toDateString() + ".";
```

The file ships that paragraph reading "If you can read this, the script has not run." No working visit ever shows those words, because the script replaces them at load. Events, changes, visit-time facts: all three demos, all on your machine.

!!! tip
    The playground is this chapter's lab bench. If your copies drift during an experiment, re-save `script-playground.html` and `playground-script.js` from the pack and keep going.

### The Public Truth

That location has a consequence the next demo turns into a lesson. For your machine to run a script, the server must send the script to your machine, whole. The same goes for the page and the stylesheet.

Everything sent to the browser is readable by the visitor, and the browser will show it to anyone who asks. Right-click a page and choose View Page Source: there is the markup, with every file it names. Hold that truth while Demo 2 offers you a locked door.

### Try It Yourself 12.2: The Lock Drawn on the Door 🛠️

**Predict:** The playground's Demo 2 is a members corner: type the pass phrase and press Unlock to read a note meant for officers. No server is involved anywhere on this page. So where must the correct phrase live for the check to work? Could a visitor find it without guessing? Write both answers down.

**Run:** Try any wrong phrase first and watch the answer line. Then find the real phrase without guessing: View Page Source shows the script element and the file it names, and VS Code opens that file. Unlock the note.

**Explain:** In 1-2 sentences, state what this proves about secrets in client-side scripts, and name the machine that could have kept the phrase out of your reach.

### Quick Check 12.1 ✅

1. The campus tutoring center wants three changes: its headings recolored in the center's green, a note that tells visitors which subjects meet today, and its enrollment steps renumbered after step two was cut. Assign each job to HTML, CSS, or JavaScript, and defend the middle one.
2. A bakery's page shows a member discount code after a script checks a password. In one sentence, explain where any visitor can read the code, and name the half of the web that could have kept it secret.
3. In one sentence, state where a client-side script runs, and what the server must therefore do with the script file first.

---

## 12.2 The Server's Half

Your wrong guess got an answer: "That is not the pass phrase." The right phrase took no guessing, because the whole gate travels in plain text inside the script file:

```js
gateButton.addEventListener("click", function () {
    if (passPhraseBox.value === "cactus-club-2026") {
        gateAnswer.textContent = "Welcome, officer. The supply closet code is 4141.";
    } else {
        gateAnswer.textContent = "That is not the pass phrase.";
    }
});
```

The `if` and `else` read like the words they are: if the box's value matches the phrase, write the note, and otherwise write the refusal. To run that comparison, your machine needed the phrase, the note, and the refusal, so the server sent all three.

The lock was a drawing of a lock. Client-side scripting can never keep a secret, because the client belongs to the visitor.

The web does keep secrets, your passwords among them. They live on the one machine in the conversation whose insides no visitor can read. They live on the server.

### The Missing Mail Carrier

The club's join page has been waiting for this section since you shipped it. It admits, in the officers' own voice, that something is missing: "While the officers finish the behind-the-scenes piece that stores sign-ups, you can also email" the club. Chapter 11 called the same gap a mailbox with no mail carrier.

Here is the missing piece, in concept. When the form submits for real someday, its name-value pairs travel to a program running on the server, at the address the form's `action` attribute names. That program checks both pairs again and stores them in a **database**: organized storage a program can query later. Receive, re-check, store. That is the entire behind-the-scenes piece, and every real sign-up on the web ends its trip this way.

Two Chapter 11 details click into place the moment a receiver exists. The `action` attribute finally has an address worth naming, and the sign-up switches to POST, the method Chapter 11 fit to private, state-changing trips.

Programs like that receiver are **server-side scripting**: scripts that run on the server and build or process pages before anything travels to a client. Languages exist in plenty for the work, Python and PHP and JavaScript itself running server-side among them. This course ships no server code on purpose.

Your job is to know which half of a task belongs to which machine, and that job takes reading, not writing. The next exercise asks you to draw the trip before this section draws it for you.

### Try It Yourself 12.3: The Trip You Cannot Watch 🛠️

**Predict:** Nothing to open and nothing to run: the server's half exists only on paper in this chapter. On paper, sketch the join list's future as boxes and arrows: every machine a sign-up touches, in order, what each one does with the pairs, and where the trip's one trustworthy check happens.

**Run:** Compare your sketch against the traced version that follows this exercise, one station at a time. Mark every difference.

**Explain:** In 1-2 sentences, name the one station whose insides no visitor can read, and name the Chapter 11 attribute that finally earns its value once a receiver exists.

Here is the join list's future, traced end to end:

```text
The visitor's browser (the client)
    collects the name and email, checks the form's claims,
    and sends the pairs over https
        |
        v
A program on the server (the receiver)
    re-checks both pairs, and only then
        |
        v
The club's database
    stores the sign-up where a later query can find it
```

!!! note
    This course teaches the server's half as a concept and never asks you to run one. Nothing in this chapter needs server code, the lab included. The deliverable is the reading skill: say what runs where, and why it must run there.

### Help Is Not Security

Why check twice? Because the two checks do different jobs, and only one can be trusted. The browser's check from Chapter 11 is convenience: it catches honest mistakes before the trip and saves the visitor a round trip.

It can never be the gate, because everything client-side belongs to the visitor, who can edit the page or disable the script. The server's check is the gate, because the server is the only machine the visitor cannot reach into.

The tutoring center's request form tells the same story. Its receiver would re-check that the subject is one the center teaches, then store the request where tomorrow's staff page can query it. The rule generalizes, and it is worth memorizing. Passwords are checked on the server, secrets live on the server, and client-side validation is help, never security. TIY 11.4's refusal was a kindness, not a lock.

### Static Sites and the HTTPS Law

One breath covers the last distinction this course owes you. The club's site is a **static site**: the server hands every visitor the same ready-made files. That is a strength, because static sites are fast, cheap to host, and leave nothing on the server to break. A **dynamic page** is built per request by a server-side program, the way a search results page assembles itself around your query string. The club needs none of that, and knowing why is the point.

And Chapter 1's collection rule returns with its full weight. Whatever travels between client and server carries visitor data. Chapter 1 set the law: "never send private information through a page whose address starts with `http://`, and never ask your visitors to."

The join page collects names and emails, so the club's live site must serve `https://`. Any independent project with a form owes its visitors the same. Chapter 2 promised your addresses would earn that prefix, and the next section starts the move.

### Quick Check 12.2 ✅

1. The tutoring center's site has four tasks. Light a menu link under the pointer, refuse an empty required field before the trip, check a returning tutor's password, and store every session request for tomorrow's staff. Assign each task to the client or the server, and name the one that needs no script at all.
2. A teammate says the join form is safe to connect anywhere "because Chapter 11's required fields already validate everything." In two sentences, correct the claim: what the browser's check is for, and where the trustworthy check runs.
3. In one sentence, state what a database adds to the club's join story that Chapter 11's query string could not provide.

---

## 12.3 Hosting and the Move

The server's half is someone's job to provide. For a site like the club's, that someone is a **web host**: a business or service that keeps your site's folder on an always-on server with a public address. Hosting is not exotic. You rent a folder the whole world can read, and the host keeps the machine running, connected, and serving `https://`. The options come in a few families:

| Option | What you get |
| --- | --- |
| Shared hosting | A slice of a commercial server, rented, reached by secure file transfer |
| Static site host | Free or low-cost hosting built for ready-made files, no server programs |
| School-provided space | Web space some colleges give students while they are enrolled |

Costs run from free static hosts to monthly shared-hosting fees, and the Further Reading survey walks the range. A custom domain name, Chapter 1's term, is a separate purchase that points at whichever host you choose.

Which host a section uses is deliberately not written here. Your instructor provides the host, address, and credentials separately because those details belong to the course layer, not the textbook. The moves this chapter teaches are the same on every host.

### The Secure Transfer Family

Getting the folder there is the file transfer family's work. Chapter 1 made this meeting an appointment: "You will meet the file transfer family again in Chapter 12, when you publish a site to a server using a secure transfer method." **FTP** (File Transfer Protocol) is the family's original name, one row of Chapter 1's protocol table: transfers files between computers.

The original is also showing its age, because plain FTP moves files and credentials unencrypted, the same sin as plain HTTP.

So the modern law follows a rule you already own: transfer over the secure family members, **SFTP** or FTPS, which encrypt the whole trip. Free transfer clients such as FileZilla speak both. Your instructor provides the client and connection settings for the selected host.

The upload itself is one idea: copy your site folder's contents into the server's public folder, keeping the structure. Your host's instructions name that public folder.

Pages at the top level stay at the top level, and the images folder rides along whole:

```text
Your laptop                        The server's public folder
site-folder/index.html         ->  index.html
site-folder/club-styles.css    ->  club-styles.css
site-folder/images/logo.png    ->  images/logo.png
```

Keeping the structure is not neatness. It is what keeps every address true. Leave the images folder behind, or flatten it into the top level, and every src that steps down into `images/` now points at nothing.

### Why the Site Survives the Move

Now the payoff the course has been arranging since Chapter 2. Why does a site built at `file://` addresses work untouched at `https://`? Because you never wrote an address that mentioned your machine. Every href and src in this course gives directions from the file's own folder: `contact.html`, next door. `images/club-logo.png`, one folder down. Chapter 2 made the promise in these exact words: "Relative links describe files in relation to each other, so they survive the move untouched."

Chapter 3 extended the promise to the whole folder, self-contained enough to zip, move, or publish with every address inside still working. The move keeps the relationships, so the move keeps the links.

Everything travels together. The club's folder carries six pages, one stylesheet, one script, and seven images, and every connection among them survives. The stylesheet publishes along with its pages, exactly as Chapter 4 said it would, and even the borrowed Oswald font rides in each page's head like any other markup.

The address that does not survive is the kind that names a machine:

```text
src="images/club-logo.png"                      directions from this file
src="file:///Users/officer/pictures/photo.png"  one machine's disk, named
```

An absolute local path points at a disk. On every other machine on earth, including the server, that disk does not exist. This course never taught you to write one, and now you know why. Your pack ships a two-photo page that makes the difference visible.

### Try It Yourself 12.4: The Move Test 🛠️

**Predict:** Open `assets/code/chapter-12/path-test.html` in VS Code and read its two img elements. Their src values differ in one way you can read. Predict which photo will render on your machine, and which would survive an upload to a server. Write one sentence of reasoning for each.

**Run:** Open the page in the browser and grade both predictions. Look closely at what the browser drew where each photo belongs.

**Explain:** In 1-2 sentences, state the rule that makes one address portable, and explain why the broken one fails on your machine today and would fail on a server for the same reason.

Photo 1 asked for `volunteer-crew.png`, a neighbor of the page itself, and it rendered. Photo 2 asked for `file:///Users/club-officer/pictures/desert-sunset.png`, a path on a machine you do not own. The browser drew the broken-image mark with the saguaro's alt text standing in: Chapter 3's safety net doing its oldest job.

The second photo is not broken because a file was lost. It is broken because its address names a place instead of a relationship, and the place is not here. Upload the page anywhere and that verdict never changes.

### The Front Door's Name

One more naming convention completes the move, and Chapter 3 banked it for exactly this moment: the web's default name for a site's home page is **index.html**. When a visitor asks for a bare folder, the server looks inside that folder for a file with this name and serves it automatically:

```text
The visitor asks for    https://example.org/
The server serves       the folder's index.html
```

That is why a home page's address never seems to name a file. It does, and the file is index.html. The site plan's missing front door now has its reason and its name. Skills Lab 12A builds the club's home page, the one page whose file name a server convention chooses for you.

### Quick Check 12.3 ✅

1. Your host offers FTP and SFTP on the same credentials. Pick one for the club's upload, and defend the pick with a rule this course taught before this chapter.
2. A visitor types your site's bare address and gets the host's page-not-found screen, yet the same address with `/contact.html` added works. In one sentence, name the missing file and its job.
3. A classmate's gallery page works at home and shows one broken image on the live site. Its src reads `C:\Users\sam\site\images\photo.png`. Diagnose the break in one sentence and write the repaired src.

---

## 12.4 The Pre-Flight and the Publish

The folder is ready to travel, and here a professional habit separates shipping from hoping. Publishing multiplies every defect by the whole audience: the broken link one visitor might have hit at your desk is now live for everyone, on every device, around the clock.

### One Instrument, Eight Checks

So the course's checking stack gets one final promotion. The **pre-flight check** runs every check you own, on every page, before the site goes public, and again before every update after. You built this stack one chapter at a time. Now it flies as one instrument, and your pack ships it as `pre-flight-checklist.txt`, one copy per page:

```text
1. HTML validator: zero messages, every page
2. CSS validator: once per stylesheet
3. Link walk: every link lands where its text promises
4. Accessibility checklist: the Chapter 9 instrument, all seven checks
5. Tab walk: every stop reachable, every stop visible
6. Device-mode walk: phone width, no sideways scroll
7. Second browser: layout, fonts, and images hold
8. Live-URL verify: after the upload, on the real address
```

Checks 1 and 2 are Chapters 2 and 4 doing their oldest jobs. Check 3 exists because a validator checks syntax, not reachability. The move test's page validates with zero messages while one of its photos is broken, and only a click or a look catches what a parser cannot. The tutoring center learned that one the honest way: its pre-flight once caught a menu link pointing at a page that had been renamed, on a page the validator had just called clean.

Check 4 re-runs the Chapter 9 checklist, all seven human checks, because Devon visits live sites too and the audit's guarantees must survive the move. Check 5 walks the Tab key one deliberate last time.

Checks 6 and 7 keep the appointment Chapter 8 made when device mode arrived. The pre-flight, it promised, "renders the finished site in multiple browsers and screen sizes before anything publishes, and a real phone belongs in that check." Check 8 is new, and it runs on the far side of the upload.

### Ship, Then Verify Live

Then the site ships. Connect with the secure transfer method from Section 12.3, copy the folder's contents into the server's public folder, and load the real address.

Verification starts where emulation ends. Open the live URL on a real phone if you can reach one, because device mode predicts and the device decides. Click through every page from the menu.

Then give the HTML validator its third door. Chapter 2 offered three ways in, address, upload, or direct input, and Chapter 4 said the URL door would start mattering once the site had an address. It matters now.

Paste the live `https://` address into the validator's address tab, and the validator fetches the page itself, checking what your server sends instead of what sits in your folder. If the live run reports something the local run did not, the difference is the upload: a file missed, an old copy, a folder left behind.

!!! note
    Judge the live site the way you judged local pages: zero validator messages, every link landing, no sideways scroll at phone width. The address changed. The bar did not.

### The Update Cycle and the Dress Rehearsal

One habit turns the publish from an event into a cycle. A live site is not an archive: content changes, and the officers will ask for edits after the site goes up. The update cycle is the pre-flight in miniature. Edit locally, re-run the pre-flight on what changed, re-upload the changed files, verify live.

Nothing edits the server copy directly, because the server holds the copy everyone sees, and the pre-flight is what keeps that copy worthy.

This chapter's lab is also a dress rehearsal. If your course includes an independent project, the site plan and draft pages meet the pre-flight, the publish, and the live verification you are about to perform for the club. Your instructor maps those milestones to the course calendar and provides the hosting details. The club's site is the last site this book builds with you. The next one is yours.

### Try It Yourself 12.5: The Five-Minute Pre-Flight 🛠️

**Predict:** Pick one club page from the pack's starter site or your own Chapter 11 lab. Estimate, in minutes, how long checks 1 through 7 will take on that single page. Write the number down before you start.

**Run:** Time yourself running the seven local checks on that one page, checklist in hand. Note anything a check catches.

**Explain:** In 1-2 sentences, compare your estimate with your measured time, and state what the result says about "no time to check" as a reason to skip the pre-flight.

### Quick Check 12.4 ✅

1. A classmate finishes edits at midnight and plans to upload first and check in the morning, "since check 8 needs the live site anyway." Order the pre-flight correctly for them: which checks run before the upload, and what the morning plan risks publishing overnight.
2. The soccer league's coach validates a page from direct input and gets zero messages, then runs the validator against the live URL an hour after upload and gets errors. Name two upload-side differences that produce exactly this split, and state which pre-flight step catches each.
3. Recite the update cycle from memory, and name the copy of the site nothing should ever edit directly.

---

## 12.5 Summary and Retrieval 💡

### Key Concepts

* The web runs on three layers with a clean split: HTML is structure, CSS is presentation, and JavaScript is behavior, the page acting after it loads. The script element attaches the layer, external files win for Chapter 4's reasons, and a script just before `</body>` runs after the elements above it exist.
* Client-side scripts run on the visitor's machine, the client from Chapter 1's model. They respond to events, change the loaded page, and know visit-time facts such as the date. Everything sent to the browser is readable by the visitor, so a client-side secret is a drawing of a lock.
* The server's half receives what forms submit: a server-side program re-checks the pairs and stores them in a database. Passwords are checked on the server, secrets live on the server, and client-side validation is help, never security. The club's site is a static site, ready-made files for every visitor, and that is a strength.
* A web host keeps your folder on an always-on server with a public address. The upload copies the folder's contents, structure intact, over the secure transfer family, SFTP or FTPS, never plain FTP. Anything a live page collects travels over HTTPS, Chapter 1's law with a live site to govern.
* Relative addresses describe relationships, so the site that worked at `file://` works at `https://` unchanged. An absolute local path names a disk and dies everywhere else. index.html is the web's default name for a folder's home page, served automatically for the bare address.
* The pre-flight check runs the whole stack on every page before anything publishes: both validators, the link walk, the Chapter 9 audit, the Tab walk, device mode, and a second browser. The live-URL verify runs after the upload, and publishing becomes a cycle: edit locally, re-run the pre-flight, re-upload, verify live.

### Key Terms

See course glossary for full definitions

* JavaScript, script element, client-side scripting (Section 12.1)
* server-side scripting, database, static site, dynamic page (Section 12.2)
* web host, FTP, SFTP, index.html (Section 12.3)
* pre-flight check (Section 12.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the three layers, each one's job, and the element that attaches the third.
2. Explain from memory why a client-side script can never keep a secret, and name the machine that can.
3. Name the secure transfer family's two members, and recite the Chapter 1 rule that disqualifies their older sibling.
4. Recite the pre-flight's eight checks, and name the one that runs after the upload.
5. Explain from memory why every link this course wrote survives the move to a server, and describe the one kind of address that dies.

---

## 12.6 Skills Lab 12A: The Site Ships

**Goal:** Produce and publish the complete six-page club site: build the home page the plan promised, pass the pre-flight on every page, and put the site live at a real `https://` address.

**Dataset:** Provided files in `assets/code/chapter-12/` from the course data pack. `starter-site/` holds the club's five pages, the `images` folder, and `club-styles.css` exactly as Skills Lab 11A finished them. `home-content.txt` is the officers' front-door content: the headline, the what-the-club-is paragraph, three what-we-do blocks, three links with their destinations, and the standing meeting line, so you copy wording instead of inventing it. `footer-year.js` is the lab's one script, finished and readable, with its contract in its own comment. `script-playground.html`, `playground-script.js`, `path-test.html`, and `volunteer-crew.png` are the chapter's Try It Yourself files and stay out of the submission. `pre-flight-checklist.txt` is the publishing instrument, copied once per page. `club-palette.txt` travels with every CSS chapter, and the home page needs no color the site does not already wear. `skills-lab-12a-answers.txt` is your written answers file. Part 3 reuses `accessibility-checklist.txt` from the Chapter 9 pack. The folder's README documents every file. Work at the extracted `cis133` root.

The lab walks the chapter's own path. Part 1 builds the front door and grows Chapter 6's navigation bar to its final six links. Part 2 attaches the script and traces the server's half on paper. Part 3 runs the pre-flight, publishes, and closes the site plan.

!!! note
    If live hosting is unavailable, complete the local pre-flight and package the site. Your instructor will identify alternate publication evidence.

### Part 1: Foundation (Aligns with Objective 12.3)

1. Create a folder named `skills-lab-12a-lastname` at your `cis133` root. Copy in the whole `starter-site` folder, keeping its name, plus `skills-lab-12a-answers.txt`.
2. Create `index.html` inside `starter-site` the Chapter 2 way: open an existing page, save as, and keep everything the pages share. Retitle the head, keep the header, nav, and footer, and clear `main` for the new content. Record in answer 1.A why this page, alone on the site, gets its file name chosen by a server convention.
3. Build the page from `home-content.txt`, block by block. The headline is the page's `h1`, with the what-the-club-is paragraph beside it in the header. The three what-we-do blocks get their own headings. The three links name their destinations the Chapter 7 way, and the standing meeting line sits where a visitor cannot miss it. The officers wrote the words and you decide the markup. Log where each block landed in answer 1.A.
4. The officers asked for Home first in the menu on all six pages, so deliver it: add the Home link at the front of every page's navigation bar, in the site plan's order.
5. Validate all six pages to zero messages. Record the nav update, the pages you touched, and the counts in answer 1.B.

### Part 2: Application (Aligns with Objectives 12.1 and 12.3)

1. Copy `footer-year.js` into your `starter-site` folder, beside the pages. Read its comment first: the script states its own contract.
2. Keep the home page's standard footer paragraph and add a copyright line below it, with the year as an empty span carrying `id="footer-year"`. The script writes the year's digits, never you. Then attach the script with a script element just before `</body>`, where Section 12.1 taught and the contract requires. Only the home page carries the line and the script.
3. Load the page and confirm the footer shows the current year. Record the span, the script element's location and why it sits there, and what the footer shows in answer 2.A.
4. Answer 2.B in writing: whose machine computed that year, and what that means for the club's January maintenance. Then write the trace: one join-list sign-up's full trip, the client's half you built in Chapter 11 and the server's half in concept from Section 12.2.

### Part 3: Extension (Aligns with Objectives 12.2 and 12.3)

1. Run the pre-flight on all six pages: one checklist copy per page, checks 1 through 7, audit first. Log every finding before repairing anything, Chapter 9's habit, then repair what you found and re-validate. Record findings, repairs, and final counts in answer 3.A.
2. Use the hosting details your instructor provides: connect with the secure transfer method the host supports, copy the folder's contents into the server's public folder while keeping the structure, and load the real address.
3. Verify live: open the live URL on a real phone if you can, and click through every page from the menu. Run check 8 by pasting the live address into the HTML validator's address tab. Record the transfer method and why it is the secure choice, the LIVE URL, and the verification in answer 3.B. Then close the site plan from Lab 7A: name each of the six planned pages, now live.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Pick one interactive moment on the finished site: the footer's year, the join form's refusal of an empty required field, or a nav link lighting under the pointer. Trace it across the client-server line: what traveled from the server, what ran or rendered on the client, and which parts of the moment needed no server at all. Cite your own pages as evidence.
2. The officers read your pre-flight log and ask a reasonable question: "It found almost nothing. Can we skip it for next month's update?" Judge the request: name what each layer of the pre-flight guards, weigh what the "almost" would have cost the club live, and state the update policy you would set for the club's next edit.

**Submission:** Zip your `skills-lab-12a-lastname` folder and submit it as `skills-lab-12a-lastname.zip`. It contains the updated `starter-site` folder (six pages, `club-styles.css`, `footer-year.js`, and `images`), your completed checklist copies, and `skills-lab-12a-answers.txt` with the live URL or alternate publication evidence your instructor requires. Every page and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 12A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Technical Accuracy
and Efficiency, Output Quality, Documentation Quality, and Analysis,
Interpretation, and Response to QUESTION(s). Your instructor sets
the point weights in your course. The criteria and levels are the
same everywhere.

---

## 12.7 Review Questions 🔄️

1. **Remember:** A food pantry is rebuilding its site and dividing the work. Name the web's three layers and the job each layer does. Then name the two members of the secure file transfer family the pantry could use for its upload.

2. **Understand:** The soccer league's members page hides its roster behind a password that a script in the page checks. Explain why this protects nothing: where the script travels, who can read it, and where a trustworthy password check runs instead.

3. **Apply:** The food pantry published its site yesterday, and three reports came in this morning. Diagnose each with this chapter's rules and name the repair:

    * The hero photo renders on the coordinator's laptop but breaks on the live site, and its src reads `C:\Users\dana\pantry\images\hero.png`.
    * Typing the site's bare address shows the host's page-not-found screen, but the same address with `/welcome.html` added works.
    * The donation page's address starts with `http://`, and the browser marks the page "Not secure" while visitors type payment details.

4. **Evaluate:** A soccer league volunteer edited tonight's schedule and wants to upload straight to the server, "because the site worked yesterday and it is one small change." Judge the request against the update cycle: name two defects a skipped pre-flight could publish tonight, and state the edit policy you would set for the league.

---

## Further Reading 📖

* [MDN: Publishing your website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website) - The whole hosting, upload, and going-live arc told once more, this chapter's closest companion.
* [MDN: What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) - The gentle next step for anyone the playground hooked, and the page where a later course begins.
* [MDN: What is a web server?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server) - The server's half in longer form, with the static-versus-dynamic split this chapter covers in one breath.
* [MDN: How do you upload your files to a web server?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server) - The concrete upload walkthrough, secure transfer included, with the screenshots this chapter does not carry.
* [MDN: How much does it cost to do something on the Web?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/How_much_does_it_cost) - The honest survey behind this chapter's hosting table, from free static hosts up.

---

## Course Conclusion: Where You Go from Here

For the first time, no chapter waits after this one. The site plan the officers approved in Chapter 7 is complete: six pages promised, six pages live, at an address anyone can visit. If your course includes an independent project, reuse these moves on your own site and let this published site serve as the working pattern. Twelve chapters ago you learned how a page reaches a screen. Now your pages reach everyone's.

Where you go from here is your choice. Publish a site for a club, a family business, or your own portfolio. Learn JavaScript when you are ready to make pages respond to their users, and take the next web course in your program when you want structured depth. You know how to build, validate, and ship accessible sites. Every site you publish from now on carries your name. The course ends where the web begins.
