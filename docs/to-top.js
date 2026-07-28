// Back-to-top affordance. Lives in its own file rather than inline so the
// pages can ship a Content-Security-Policy without 'unsafe-inline' and
// without a hash that a later edit would silently invalidate.
var toTop = document.getElementById("to-top");
window.addEventListener(
  "scroll",
  function () {
    toTop.classList.toggle("visible", window.scrollY > 400);
  },
  { passive: true }
);
