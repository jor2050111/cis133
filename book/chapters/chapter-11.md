# Chapter 11: HTML Forms

Watch the last ten minutes of any drive the PC Computer Club runs. Interested students crowd the table, and an officer collects names on whatever paper is handy. By the next meeting, half the scraps are gone. The officers named this problem in their Chapter 7 brief. Their third request asked for a join page: "collect the name and email of every student who wants to hear from us, so an officer can invite them to the next meeting." The events page shipped in Chapter 10. The join page is the site plan's second promised addition, and this chapter builds it.

The page needs something no page in this book has carried. Every element you own presents content to visitors: headings announce, images show, tables answer questions. A form is the first element that listens back. It hands the visitor the keyboard, collects what they type and pick, and sends the answers on a trip you can watch in the address bar. That trip runs on a term you met in Chapter 1 and have not needed since. The query string comes home in this chapter.

You will build the listening machinery first: inputs, choices, menus, and the label contract Chapter 9 promised by name. Then you will follow the data after the button press, and learn what the browser checks before the trip even starts. You will style the form with tools you already own, because the course's selector set is complete. Skills Lab 11A designs the club's join page, wires it into every page's navigation, and defends every field it collects.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 2-10 (HTML structure, CSS selectors and states, the accessibility standard, and the club site the labs have built)
* **Deliverables:** Skills Lab 11A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **MLO-11.1 (Apply):** Construct labeled form controls: text and email inputs, radio groups, checkboxes, select menus, textareas, and a submit button
* **MLO-11.2 (Apply):** Demonstrate how submitted form data travels: name-value pairs, GET and the query string, POST, and the server's role in concept
* **MLO-11.3 (Create):** Design the club's join page: an accessible, styled signup form that collects only what it needs

---

## 11.1 The Form and the Label Contract

The campus tutoring center is this chapter's test bench, and it arrives with a request of its own. The center wants students to ask for sessions online instead of by hallway conversation. Its finished request form ships in your pack as `assets/code/chapter-11/session-request.html`, complete and correct on purpose. This chapter's exercises do not build that form. They experiment on it. First, meet the elements it is made of.

The **form element** (`<form>`) wraps a page's input controls and owns their shared trip. When the visitor submits, the form is what gathers its controls' answers and sends them off together. The **input element** (`<input>`) is the workhorse control, an empty element like `<img>` and `<meta>`. One attribute picks its personality: `type`. With `type="text"` it renders a single-line text box, the plainest answer a form can collect.

A bare text box has a problem the screen never shows you. The box renders, and nothing announces what it wants. A sighted visitor guesses from whatever words happen to sit nearby. Devon's screen reader has less to go on: it reports an unnamed text box and moves on. The box needs an announcement every tool can find, and Chapter 9 left you exactly one contract for this moment. Forms, it said, are built on "the partnership between every input and the label that announces it." Here is that partnership, paid by name. The **label element** (`<label>`) holds a control's visible name, and its `for` attribute points at the control's `id`. When the two values match, the label and the control belong to each other.

```html
<!-- The label contract: for points at id, and the two values
     match exactly. The form wraps every control it will send. -->
<form>
    <label for="student-name">Full name</label>
    <input type="text" id="student-name" name="student-name">
</form>
```

The pairing buys Devon the announcement the bare box denied. Focus lands on the control, and the screen reader speaks the label with it: "Full name, edit text." No guessing from nearby words, because the words are attached. The contract pays a second audience too, and it takes no screen reader to feel it. The first exercise puts it under your mouse.

### Try It Yourself 11.1: The Label Click Test 🛠️

**Predict:** Open `assets/code/chapter-11/session-request.html` in the browser. What happens when you click the visible words "Email (required)", not the box below them? And what happens when you click the word "Drop-in" beside its small circle? Write both predictions.

**Run:** Click every label on the form, one at a time: the two text labels, the two session-type words, and the notes label. Watch where each click lands.

**Explain:** In 1-2 sentences, name the contract's two beneficiaries: who your mouse served a moment ago, and who the announcement from this section serves.

Name what your clicks proved: a paired label is part of its control's click target. The visible words operate the control they announce, so a small circle or box grows a target the size of its label. Chapter 7 asked for generous touch targets when it made design serve every visitor, and the contract delivers them for free. One contract, two beneficiaries, zero pixels changed, which should ring the Chapter 3 bell: meaning first, looks later.

One attribute in the example still has no story. The `id` serves the label. The **name attribute** serves the data: it is the label the control's answer will travel under when the form submits. Section 11.3 tells that story in full. Until then, give every control a `name` attribute and a paired label, and both jobs are covered.

### Quick Check 11.1 ✅

1. A teammate writes `for="full-name"` on a label while the input below it carries `id="name-field"`. On screen, everything looks right. Name what broke, and name two visitors who pay for it.
2. In one sentence, state the contract's two halves: which element carries `for`, which carries `id`, and what must be true of their values.
3. A newsletter signup ships an email input carrying both `id="signup-email"` and `name="signup-email"`. The values match, but the attributes serve different masters. Name each attribute's job, and state which one the submitted data travels under.

---

## 11.2 The Input Family

One box collects one line of text. The request form needs more shapes of answer: a working email address, one session type out of two, a subject from a fixed list, and a paragraph of notes. HTML has a control for each shape, and choosing the right one is most of the work.

Email addresses earn their own input type. Write `type="email"` and the box looks identical to the text box: same line, same border, same typing. The difference is a promise the browser records: this box expects an email address. Section 11.3 shows the promise coming due.

```html
<!-- Same box on screen, different promise to the browser. -->
<label for="student-email">Email</label>
<input type="email" id="student-email" name="student-email">
```

Some questions offer a few options and allow one answer. Their control is the **radio button**, `type="radio"`, one small circle per option, where picking a second option releases the first. Here is the part that surprises beginners: no wrapper element declares which circles work together. The group is the name. Radios that share a `name` form one group, and each carries its own `value`, the answer it stands for.

```html
<!-- One group, declared by one shared name. Each option keeps
     its own id, its own label, and its own value. -->
<input type="radio" id="type-drop-in"
name="session-type" value="drop-in">
<label for="type-drop-in">Drop-in</label>

<input type="radio" id="type-appointment"
name="session-type" value="appointment">
<label for="type-appointment">Appointment</label>
```

Other questions invite any number of answers. The **checkbox**, `type="checkbox"`, gives each option its own independent yes or no, and checking one box never releases another. A set of related checkboxes may share a `name` the way radios do, each box keeping its own `value`. Only a checked box sends its answer when the form submits.

A group of circles or boxes creates a naming problem one label cannot solve. Each option's label names that option: Monday, Drop-in, Appointment. Nothing yet names the question the whole group answers. Two elements share that job. The **fieldset element** (`<fieldset>`) wraps the group and draws its boundary, and the **legend element** (`<legend>`), written first inside it, names the group's question. Read the pair as the group's own label contract. A screen reader announces the legend alongside each option, so Devon hears "Session type, Drop-in" instead of a bare "Drop-in." One structural habit rides along: wrap each choice in its own paragraph, and the choices stack one per line with no new selector needed.

```html
<!-- The group's own label contract: the legend names the
     question, and every option inside answers it. One box
     per paragraph stacks the choices one per line. -->
<fieldset>
    <legend>Which days can you meet?</legend>
    <p>
        <input type="checkbox" id="day-monday"
        name="meeting-day" value="monday">
        <label for="day-monday">Monday</label>
    </p>
    <p>
        <input type="checkbox" id="day-wednesday"
        name="meeting-day" value="wednesday">
        <label for="day-wednesday">Wednesday</label>
    </p>
</fieldset>
```

The practice form wraps its session-type radios in the same two elements. The fieldset draws a visible border there, and the border tempts a wrong conclusion: that the box is what binds a group. The next exercise settles what does.

### Try It Yourself 11.2: Breaking the Group 🛠️

**Predict:** The practice form's two session-type radios share `name="session-type"`. Suppose you edit one radio's name to `appointment-type`, save, and reload. Both circles still sit in the same fieldset, under the same legend, with the same labels. What will the form now let you do that it would not before? Write your prediction.

**Run:** Make the edit in VS Code, save, reload, and click both radio labels. Watch what stays selected. Then undo the edit and confirm the old behavior returns, or re-save the file from the pack.

**Explain:** In 1-2 sentences, state what the shared name declares that the shared fieldset and the matching labels cannot.

!!! tip
    The practice form is your lab bench for the whole chapter. If your copy drifts during an experiment, re-save `session-request.html` from the pack and keep going.

When the list of options grows past a handful, radio circles start eating the page. The **select element** (`<select>`) folds one-choice-among-many into a compact menu. Each choice is an `<option>` element inside it, and each option's `value` is the answer it stands for. The label contract works unchanged: `for` on the label, `id` on the select.

```html
<!-- One choice among many, folded into a menu. -->
<label for="subject">Subject</label>
<select id="subject" name="subject">
    <option value="algebra">Algebra</option>
    <option value="biology">Biology</option>
    <option value="chemistry">Chemistry</option>
    <option value="writing">Writing</option>
</select>
```

Those four subjects are the same schedule you tabled in Chapter 10, wearing a new control. Two more elements finish the form. The **textarea element** (`<textarea>`) renders a multi-line box for longer answers, and unlike input it is a container with an opening and closing tag. Its `rows` attribute suggests a visible height. The last control starts the trip: a `<button>` inside a form submits the form when pressed, no attribute required, because submitting is a button's default job there. Write the action on it as its text. Older code spells the same trigger `<input type="submit">`.

```html
<!-- A multi-line box for notes, and the button that starts
     the trip. The button's text names the action. -->
<label for="notes">Notes for your tutor</label>
<textarea id="notes" name="notes" rows="4"></textarea>

<button>Request a session</button>
```

Four more input types get one mention and no more. `password`, `number`, `date`, and `file` exist, the join page needs none of them, and the input reference in Further Reading holds the full table. The whole family compresses into one decision table:

| The answer's shape | The control |
| --- | --- |
| One line of text | `<input type="text">` |
| An email address | `<input type="email">` |
| One choice among a few | Radio buttons sharing one `name` |
| Any number of independent choices | Checkboxes, one yes or no each |
| One choice among many | `<select>` with its options |
| A paragraph or more | `<textarea>` |
| Start the trip | `<button>` |

### Quick Check 11.2 ✅

1. A fitness center's signup asks for one membership level among three, any of six group classes, and a home campus from a list of forty. Name the control each answer earns, and the tell that decides it.
2. In one sentence each, state what a label names and what a legend names. Then state which of the two a screen reader announces with every option in a group.
3. A teammate converts the session-type radios to checkboxes "so a student can pick both." State the claim about the data that the switch changed, and describe a question where the switch would be correct.

---

## 11.3 Where the Data Goes

The request form is complete: labeled controls, one legended group, one button. Now press the button and face the question every form raises. Where does the data go?

The moment a form submits, the browser walks its controls and bundles each one's `name` with its current value. One control makes one **name-value pair**: the name comes from your markup, the value from whatever the visitor typed or picked. The bundle is the whole shipment. A control without a `name` contributes nothing and stays home, however carefully the visitor filled it in. That is why Section 11.1 told you to name every control.

Where the bundle travels is the method's decision, and the default method is **GET**. GET ships the pairs in plain sight, appended to the page's own address in the shape `?name=value&name=value`. You have read that shape before. Chapter 1 named it the query string, and Lab 1A had you dissect live URLs into their parts, query strings included. The term returns with a promotion, because this time your own form writes one.

### Try It Yourself 11.3: Read the Trip 🛠️

**Predict:** You are about to fill in the practice form and press the button. Where will the data appear, and what shape will it take? Write the URL you expect to see after the trip, as much of it as you can guess.

**Run:** In `session-request.html`, type your name, type a made-up email with an `@` in it, pick a session type, and leave the rest alone. Press the button, then read the address bar slowly, all the way to the end.

**Explain:** In 1-2 sentences, name the attribute each pair's left side came from, and name the Chapter 1 term for everything after the question mark.

Here is the trip one filled-out copy of the request form took, exactly as the browser wrote it:

```text
?student-name=Jordan+Ortiz&student-email=jordan%40example.org&subject=algebra&session-type=drop-in&notes=
```

Read it against the markup, and four details deserve names:

* The `?` opens the query string, each pair reads `name=value`, and `&` joins the pairs. This is Chapter 1's anatomy, written by a form you can edit.
* Browsers encode characters for travel. The space in Jordan Ortiz travels as `+`, and the email's `@` travels as `%40`. The receiving end decodes them on arrival.
* `subject=algebra` traveled although nobody touched the menu. A select always has a selected option, and by default that is its first one.
* The empty notes box still traveled, as `notes=`. A named control makes the trip whether or not it holds a value. Choice controls are the exception: a radio or checkbox sends its pair only while checked, so a group nobody touched sends nothing at all.

The untouched menu teaches a repair worth owning. The tutoring center can defend `subject=algebra` as a sensible default. An optional menu usually cannot: every visitor who skips it would submit the first real choice as if they had picked it. The repair is a neutral first option with an empty value, `<option value="">Choose one</option>`, so a skipped menu sends an empty answer instead of a false one. The join page's optional menu will want exactly this.

GET has a sibling. **POST** sends the same pairs inside the request itself, out of the address bar entirely. The split between them is a judgment call you now own:

| Method | Where the pairs travel | The requests it fits |
| --- | --- | --- |
| GET | In the URL, as a query string | Safe to repeat, bookmark, and share: a search, a filter, a lookup |
| POST | Inside the request, out of sight | Private or state-changing: a signup, a password, an order |

And Chapter 1's security rule returns with new weight. Whichever method carries the pairs, never collect anything from a visitor over plain `http://`. A query string is only as private as the address bar it sits in, and HTTPS protects the whole trip either way.

!!! note
    This course teaches POST as a concept and never asks you to submit one. A POST needs a receiver, and nothing on your machine is ready to play that part. The demonstrations stay with GET, where the address bar shows you everything.

That admission is the honest heart of this section. A form is a mailbox, and this course ships no mail carrier. Something on a server, a program with storage behind it, must receive the pairs and act on them. Chapter 1's client-server model has been waiting for this: the form is the client's half of a conversation, and Chapter 12 tells the server's half. The form element's `action` attribute names the receiving address. Every form in this chapter omits it, so the pairs travel to the page's own URL, where you can read them and nothing more happens. The join page will admit that plainly, right on the page.

Three attributes make a form kinder before any styling arrives. The first is `required`: write it on a control, and the form declares that this field may not travel empty. Pair it with the email type's promise from Section 11.2, and the browser holds two claims it can check the instant the button is pressed. What the browser does about a broken claim is the next experiment.

```html
<!-- required declares the field may not travel empty, and
     autocomplete invites the browser to offer what it knows. -->
<label for="student-email">Email (required)</label>
<input type="email" id="student-email" name="student-email"
required autocomplete="email">
```

The second is `autocomplete`. Give it a standard token such as `"name"` or `"email"`, and the browser offers to fill the field with what it already knows about its own user. Two keystrokes replace twenty for everyone, and Chapter 9's one-handed visitor feels the difference most. The third is `placeholder`, and it arrives with a law attached. A **placeholder** shows a gray hint inside an empty control, such as an example answer. The law: a placeholder is a hint, never a label. Section 11.4 finishes that argument, and TIY 11.5 lets you watch the reason for yourself.

### Try It Yourself 11.4: The Browser Says No 🛠️

**Predict:** Empty the required name field and press the button. Then fill the name but type an email with no `@` sign, and press it again. For each attempt, predict two things: does the trip start, and what do you see?

**Run:** Run both attempts on `session-request.html`. Watch the form and the address bar.

**Explain:** In 1-2 sentences, name what the browser checked without one line of your CSS and without any server. Then name one thing about the visitor's answer this checking can never verify.

The browser refused twice, and the trip never started: no query string, no page change, only the form insisting. Current Chrome words the first refusal "Please fill out this field.", and every browser words it in its own way. Name what you watched: the browser checked your markup's claims before anything left the machine. Practitioners call that client-side validation, and it always works beside a partner, because a browser can confirm an email's shape but never that the visitor owns it. Real sites re-check everything on the server after the trip. The club's form gets the client's half in this chapter, and the server's half belongs to Chapter 12's story.

One more rule belongs here, because it governs what should travel at all. Chapter 1 made this chapter a promise to keep: "every field you add is a promise to handle someone's information responsibly. Collect only what the page needs, and say what you will do with it." The officers' notes honor that rule from their side. They ask for a name and an email, they wrote an explicit "and nothing else" list, and they supplied the one-sentence promise the page must display. The lab will hand you a chance to break the rule, and Part 3 asks you to defend refusing it.

### Quick Check 11.3 ✅

1. Assign a method to each: a recipe site's search box, and a page where members change their password. Defend both calls, and name the Chapter 1 rule both pages must obey while collecting anything.
2. A URL ends in `?meal=vegetarian&guests=2`. Describe the two controls the form must contain: what each control's `name` attribute says, and where each value came from.
3. A study-group signup works with a name and an email. A teammate wants to add a student ID field "in case we need it someday." Judge the addition against this section's rule, and quote the promise it strains.

---

## 11.4 The Accessible, Styled Form

Open the practice form beside the club's pages and the gap is plain. The controls work, and nothing about them says they belong to anyone. The join page has to match the site, and the styling takes no new machinery at all. Chapter 10 declared `:nth-child()` the course's last new selector, and that promise holds. Element selectors you have owned since Chapter 4, plus the `:hover` and `:focus` pair from Chapter 6, style everything a form needs.

Start with geometry. A form reads best as one column: each label on its own line above its control, eyes then fingers, straight down. Labels render inline by default, so one declaration builds the column. The exception lives inside the fieldset, where each choice's word belongs beside its own circle or box, and one more rule keeps a checkbox at its own small size instead of the column's width.

```css
/* Labels above controls: one question per line, with air
   between questions. */
label {
    display: block;
    margin: 16px 0 4px;
}

/* Inside the fieldset, a choice's word stays beside its box. */
fieldset label {
    display: inline;
    margin: 0;
}
```

The controls take the other half of the geometry: full column width, padded, and told what type to wear.

```css
/* Controls fill the readable column, and padding keeps typed
   text off the walls. Form controls ignore the page's font
   settings unless told, so the type is restated on purpose. */
input, select, textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #333333;
    font-family: Verdana, Arial, sans-serif;
    font-size: 1rem;
}

/* A checkbox needs its own small box, not the column. */
fieldset input {
    width: auto;
}
```

Two lines carry the surprises. The `width: 100%` claim is safe because the readable column from Chapter 5 already caps the form's width. And the type restatement is not decoration: form controls ship with a small font of their own and ignore the body's rules until a rule speaks to them directly. Inside the controls, ink on white sits on the palette's passing list at 12.63 to 1.

The choice group asks for three small rules of its own: a boundary, a bold name, and a little air between choices.

```css
/* The group's boundary, its name, and one choice per line. */
fieldset {
    border: 1px solid #333333;
    padding: 16px;
    margin: 16px 0;
}

legend {
    font-weight: bold;
    padding: 0 8px;
}

fieldset p {
    margin: 8px 0;
}
```

Now the law this course will not bend. Tab into any control on the unstyled practice form and the browser draws its own focus ring, no CSS required. That default is the signal keyboard visitors steer by. Chapter 6 wrote the rule for links, and it covers form controls unchanged: never remove the signal without a replacement at least as visible. On the club's site, the replacement earns its keep by wearing the palette.

```css
/* Focus made visible on every control: a club-teal ring
   replaces the browser's default instead of removing it. */
input:focus, select:focus, textarea:focus {
    outline: 2px solid #268080;
}
```

Club teal on white sits on the passing list at 4.69 to 1. Against the site's light sand page background, the ring computes 3.04 to 1, past the 3 to 1 minimum WCAG sets for non-text marks. Measured, never eyeballed, as always.

The button is the page's call to action, and it dresses like one. White on club teal carries the passing list's 4.69 to 1. Hover and focus are equal citizens, Chapter 6's oldest law, and the swap reads like the nav links' inversion turned around. One trick keeps the button steady: the border matches the background, so the edge exists in both states and the button never changes size.

```css
/* The call to action: white on club teal, with hover and
   focus twins. The border matches the background so the
   button keeps its exact size in both states. */
button {
    background-color: #268080;
    color: #ffffff;
    border: 2px solid #268080;
    padding: 12px 24px;
    font-family: Verdana, Arial, sans-serif;
    font-size: 1rem;
}

button:hover, button:focus {
    background-color: #ffffff;
    color: #268080;
}
```

Two writing rules finish the form, and the first settles the placeholder. Section 11.3 stated the law: a hint, never a label. The reason is a behavior you have not watched yet, and the last exercise hands it to you.

### Try It Yourself 11.5: The Vanishing Hint 🛠️

**Predict:** The practice form's notes box carries a gray example sentence. Type one word into the box. Where does the hint go? Can you get it back without deleting your word? And which visitor never saw the hint at all?

**Run:** Type a word into the notes box and watch the hint. Then empty the box again and watch what returns.

**Explain:** In 1-2 sentences, explain why the label above the box survives every state the placeholder cannot.

The label survives because it never shared the box. It stands beside the control in its own element, present while the box is empty, full, or focused. A placeholder lives inside the box, exists only while the box is empty, and speaks only to visitors who can see it. Anything a visitor must know, starting with the field's name, belongs in the label. An example answer may ride along as a hint, and the notes box shows a hint done right: the label carries the name, and the placeholder only adds a sample.

The second rule reapplies Chapter 9. Mark required fields in text: the word "(required)" in or near the label, the way the practice form writes it. Never mark them in color alone. A red label is invisible to Devon's ears, to the visitor who cannot tell red from another dark tone, and to anyone reading through glare. The word survives them all.

The chapter's habits compress into a checklist, ready for the lab and every form after it:

* Every control paired with a label through `for` and `id`
* Every choice group wrapped in a fieldset and named by a legend
* Focus visible on every control and on the button
* Required fields marked in label text, never in color alone
* Placeholders as hints only, never as a control's only name
* Tab order matching source order, proved by a Tab walk

### Quick Check 11.4 ✅

1. A form ships `<input type="text" name="pet-name" placeholder="Pet's name">` and nothing else. Name the two repairs the field needs, and the visitor each repair serves.
2. A checkout form marks its required fields by coloring their labels red, and only that. Name the Chapter 9 rule this breaks, the POUR principle behind it, and the repair.
3. A teammate proposes `input:focus { outline: none; }` because the default ring "clashes with the brand." Amend the proposal so the brand improves and the law holds, and name the visitor your amendment protects.

---

## 11.5 Summary and Retrieval 💡

### Key Concepts

* A form is the first element that listens back. The form element wraps the controls and owns the submit trip, and the input element's `type` picks each control's personality. Every control needs a `name` attribute, because the name is the label its answer travels under.
* The label contract pairs every control with the words that announce it: `for` on the label matches `id` on the control. It serves two audiences at once: screen readers announce the label with the control, and the label joins the control's click target.
* Control choice follows the data's shape. Radios offer one choice among a few, and the group is the shared name. Checkboxes give each option its own yes or no. A select folds one choice among many into a menu, a textarea takes multi-line answers, and a button starts the trip. Fieldset and legend name the question a whole group answers.
* Submitting bundles name-value pairs. With GET they ride the URL as Chapter 1's query string, encoded for travel. With POST they ride inside the request. GET fits repeatable requests, POST fits private or state-changing ones, and nothing is collected over plain HTTP.
* The browser checks markup claims like `required` and `type="email"` before the trip starts, with no server involved. That checking can never verify honesty or ownership, and this course ships no server: the trip ends at the query string until Chapter 12 tells the server's story.
* Forms are styled with element selectors and the owned pseudo-classes only: labels stacked above sized controls, focus visible on everything, the button dressed from the palette. Required is marked in text, a placeholder is never a label, and a form collects only what its page needs.

### Key Terms

See course glossary for full definitions

* form element, input element, label element, name attribute (Section 11.1)
* radio button, checkbox, fieldset element, legend element, select element, textarea element (Section 11.2)
* name-value pair, GET, POST, placeholder (Section 11.3)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Recite the label contract: the two elements, the two attributes, what must match, and the two beneficiaries.
2. Pick the control for four data shapes from memory: one choice among three, any of five options, one choice among forty, and a paragraph-length answer.
3. Trace the submit trip from memory: what the browser bundles, what a control without a name contributes, and where the bundle appears under GET.
4. State when GET fits and when POST fits, one example each, and recite the Chapter 1 rule about collecting over plain HTTP.
5. Recite the collection promise Chapter 1 made and this chapter paid, and name the two fields the officers' notes declared required.

---

## 11.6 Skills Lab 11A: The Join Page

**Goal:** Design the club's join page: an accessible signup form that collects only what the officers asked for, styled from the palette's passing list. Linking it from every page's navigation closes the site plan's second promised addition.

**Dataset:** Provided files in `assets/code/chapter-11/` from the course data pack. `starter-site/` holds the club's four pages, the `images` folder, and `club-styles.css` exactly as Skills Lab 10A finished them. The events page is live in the nav, and the stylesheet carries the table block with the query block below it. `join-page-notes.txt` is the officers' field list for the join page: the two required fields, the optional menu, checkboxes, and question box, the "and nothing else" rule, and the data-promise sentence the page must display. `club-palette.txt` travels with every CSS chapter, and its passing list supplies every color this lab's form wears. `session-request.html` and `request-styles.css` are the chapter's Try It Yourself files and stay out of the submission. `skills-lab-11a-answers.txt` is your written answers file. Part 3 reuses `accessibility-checklist.txt` from the Chapter 9 pack. The folder's README documents every file. Work at the extracted `cis133` root.

The lab walks the chapter's own path. Part 1 builds the page and its labeled controls. Part 2 adds the helping attributes and the style block. Part 3 demonstrates the trip, passes the Chapter 9 habit, and defends what the form refuses to collect.

### Part 1: Foundation (Aligns with MLO-11.1)

1. Create a folder named `skills-lab-11a-lastname` at your `cis133` root. Copy in the whole `starter-site` folder, keeping its name, plus `join-page-notes.txt` and `skills-lab-11a-answers.txt`.
2. Create `join.html` inside `starter-site` the Chapter 2 way: open an existing page, save as, and keep everything the pages share. Retitle the head, keep the header, nav, and footer, and clear `main` down to one short intro paragraph you write.
3. Build the form from the officers' notes, one control per item. Use labeled text and email inputs for the two required fields. Open the how-did-you-hear select with Section 11.3's empty-value neutral option, then the notes' five choices. Wrap the four interest checkboxes in a fieldset with a legend you write, stacked one per paragraph and sharing one `name`. Finish with the questions textarea and a submit button whose text names the action. Pair every label through the contract, and record the build in answer 1.A.
4. Put the officers' data-promise sentence on the page, word for word, where a visitor reads it before typing.
5. Add the join link to the navigation bar on all five pages, between the events link and the contact link, the site plan's order. Choose the link text yourself, and let Chapter 7's label law choose with you.
6. Validate all five pages to zero messages. Record the nav update, the promise sentence's location, and the counts in answer 1.B.

### Part 2: Application (Aligns with MLO-11.3, MLO-11.1)

1. Add the helping attributes: `required` on the two fields the officers cannot work without, `autocomplete="name"` and `autocomplete="email"` on the matching inputs, and the word "(required)" in each of those labels, in text. Decide whether any control earns a placeholder, and hold the law: a hint, never a label. Record every decision in answer 2.A.
2. In `club-styles.css`, add a commented form block below the table block and above the query block, so the query block keeps the bottom of the file. Stack the labels above their controls, size and pad the controls to the column, keep the fieldset's boxes at their own size, and restate the site's type on the controls. Record the block's decisions in answer 2.B.
3. Make focus visible on every control, and dress the button as the page's call to action with hover and focus twins. Shop every pairing from the palette's passing list, and quote each ratio in answer 2.B. Validate the stylesheet to zero messages.

### Part 3: Extension (Aligns with MLO-11.2, MLO-11.3)

1. The demonstration: fill in your form, check any two interest boxes, press the button, and read the address bar. Log in answer 3.A what you typed, the URL the browser wrote, which name-value pairs traveled, and whether any control stayed home. Audit first: log everything before you repair anything a missing pair reveals.
2. Run the Chapter 9 habit on the new page: a checklist copy, the Tab walk, and both validators to zero messages. Then answer in 3.B where the pairs would go if the club had a server, and why the page as shipped makes no promise it cannot keep.
3. Close with the collection defense in answer 3.B: name one field a lesser form would have added, and defend the refusal with Chapter 1's promise and the officers' own "and nothing else" rule.

### Questions & Analysis 🤔

Answer both questions in the answers file. These answers carry significant rubric weight.

1. Your finished form carries the label contract on every control, a legend over the interest group, a visible focus signal, and required fields marked in text. Assign each feature one visitor it serves and one failure it prevents, citing your own page as evidence.
2. The officers could have asked for a phone number, a student ID, and a class schedule "to know members better." Judge that request against Chapter 1's promise and this chapter's collection rule. Then write the two-sentence reply you would send the officers.

**Submission:** Zip your `skills-lab-11a-lastname` folder containing the updated `starter-site` folder (five pages, `club-styles.css`, and `images`), your completed checklist copy, and `skills-lab-11a-answers.txt`, and submit it as `skills-lab-11a-lastname.zip`. Every page and the stylesheet must validate with zero messages, and every answer must sit under its numbered prompt.

### Rubric: Skills Lab 11A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria at
4 points each, 16 points total. The criteria are Code Accuracy and
Efficiency, Output Quality, Documentation and Code Comments, and
Analysis, Interpretation, and Response to QUESTION(s).

---

## 11.7 Review Questions 🔄️

1. **Remember:** A food pantry is building its volunteer signup form. Name the control you would reach for to collect each answer: the volunteer's full name, one T-shirt size among four, any of five available shifts, and a few sentences of prior experience. Then name the two attributes that bind a label to its control.

2. **Understand:** A soccer league's registration form submits with GET. Explain the trip: what the browser bundles when the button is pressed, where each pair's left side comes from, where the pairs appear after the trip, and what a control without a `name` contributes.

3. **Apply:** The food pantry's form contains the fragment below. Repair it: fix the broken label pairing, give the email field the contract and an honest input type instead of a hint, and make the two shifts one working group with a named question.

    ```html
    <label for="volunteer">Full name</label>
    <input type="text" id="vol-name" name="volunteer-name">

    <input type="text" name="volunteer-email" placeholder="Email address">

    <p>Pick your Saturday shift:</p>
    <input type="radio" id="shift-morning" name="morning-shift" value="morning">
    <label for="shift-morning">Morning</label>
    <input type="radio" id="shift-afternoon" name="afternoon-shift" value="afternoon">
    <label for="shift-afternoon">Afternoon</label>
    ```

4. **Evaluate:** The soccer league's registration form asks for full name, email, jersey size, birthday, student ID, home address, and phone number. The league emails a weekly schedule, and jerseys come in four sizes. Critique the form against this chapter's collection rule and Chapter 1's promise, propose the minimal field set, and state the one sentence the page owes its visitors about the data it keeps.

---

## Further Reading 📖

* [MDN: Your first form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form) - The gentlest full build of a working form: a second telling of Sections 11.1 and 11.2 with its own styling pass.
* [MDN: The form element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form) - The wrapper element's full reference, including the `action` attribute this course leaves to Chapter 12's server story.
* [MDN: The input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input) - The complete input-type table, where the one-mentioned password, number, date, and file types live for the curious.
* [W3C WAI: Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/) - The accessibility source this chapter's label, group, and instruction teaching follows.
* [WebAIM: Creating Accessible Forms](https://webaim.org/techniques/forms/) - The screen-reader-first telling of the label contract, with the failure cases Section 11.4 warns against.

---

## Looking Ahead ⏩

One chapter remains, and it keeps three promises at once. Chapter 12 builds the home page and publishes the whole site, behind a pre-flight check that re-runs every validator and audit this course has taught. The form's missing mail carrier finally gets its story there: what a server does with the pairs, how hosting and secure transfer work, and what scripting adds to a page. The book's last chapter ships the site the plan promised.
