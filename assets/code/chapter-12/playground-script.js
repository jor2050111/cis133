/* Script for script-playground.html: one numbered block per demo
   on the page. The Chapter 12 exercises say when to read this
   file, so run the page first if you have not yet. */

/* Demo 1. */
const statusLine = document.getElementById("status-line");
const demoButton = document.getElementById("demo-button");

demoButton.addEventListener("click", function () {
    statusLine.textContent = "You pressed the button, and this line changed.";
});

/* Demo 2. */
const passPhraseBox = document.getElementById("pass-phrase");
const gateButton = document.getElementById("gate-button");
const gateAnswer = document.getElementById("gate-answer");

gateButton.addEventListener("click", function () {
    if (passPhraseBox.value === "cactus-club-2026") {
        gateAnswer.textContent = "Welcome, officer. The supply closet code is 4141.";
    } else {
        gateAnswer.textContent = "That is not the pass phrase.";
    }
});

/* Demo 3. */
const visitDateLine = document.getElementById("visit-date");
visitDateLine.textContent = "You opened this page on " + new Date().toDateString() + ".";
