/* Writes the current year into the footer, so nobody has to edit
   the site every January. The page must give the script two
   things: a span with id="footer-year" where the year belongs,
   and a script element for this file just before the closing
   body tag, so the span exists by the time this line runs. */

document.getElementById("footer-year").textContent = new Date().getFullYear();
