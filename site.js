// Sections ease in as they scroll into view; the phone in "How it works" changes screen with the step
// being read; the play button plays the voice clip.
(function () {
  var root = document.documentElement;
  var still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if ("IntersectionObserver" in window) {
    if (!still) {
      root.classList.add("js");
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
      }, { rootMargin: "0px 0px -8% 0px" });
      document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
    }
    var screens = document.querySelectorAll(".story .pin img");
    if (screens.length) {
      var steps = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          var n = +e.target.getAttribute("data-step");
          screens.forEach(function (img, i) { img.classList.toggle("on", i === n); });
        });
      }, { rootMargin: "-45% 0px -45% 0px" });
      document.querySelectorAll(".story [data-step]").forEach(function (el) { steps.observe(el); });
    }
  }
  document.querySelectorAll("[data-play]").forEach(function (btn) {
    var audio = new Audio(btn.getAttribute("data-play"));
    var box = btn.closest(".voice") || btn.parentNode;
    var label = btn.getAttribute("aria-label");
    btn.addEventListener("click", function () { if (audio.paused) { audio.currentTime = 0; audio.play(); } else { audio.pause(); } });
    audio.addEventListener("play", function () { box.classList.add("playing"); btn.setAttribute("aria-label", "Stop"); });
    ["pause", "ended"].forEach(function (ev) {
      audio.addEventListener(ev, function () { box.classList.remove("playing"); btn.setAttribute("aria-label", label); });
    });
  });
})();
