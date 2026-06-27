/* =========================================================
   Spit Shine San Antonio — site interactions
   ========================================================= */
(function () {
  "use strict";

  /* ---- Sticky header state ---- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    header.classList.toggle("scrolled", window.scrollY > 24);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---- Mobile nav toggle ---- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---- FAQ accordion ---- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.setAttribute("aria-expanded", "false");
    q.addEventListener("click", function () {
      var isOpen = item.classList.toggle("open");
      q.setAttribute("aria-expanded", isOpen ? "true" : "false");
      a.style.maxHeight = isOpen ? a.scrollHeight + "px" : null;
    });
  });

  /* ---- Scroll reveal ---- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Dynamic year ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Calendly booking ----
     Every "Book" CTA (links to book.html / #book-form, or anything tagged
     .book-link) opens the Calendly scheduler in a popup. If Calendly hasn't
     loaded yet, the link falls back to navigating to the Book page.        */
  var calUrl = document.body.getAttribute("data-calendly");
  if (calUrl) {
    var bookLinks = document.querySelectorAll(
      'a[href$="book.html"], a[href$="book.html#book-form"], a[href="#book-form"], .book-link'
    );
    bookLinks.forEach(function (a) {
      a.addEventListener("click", function (e) {
        if (window.Calendly && typeof window.Calendly.initPopupWidget === "function") {
          e.preventDefault();
          window.Calendly.initPopupWidget({ url: calUrl });
        }
      });
    });
  }

  /* ---- Forms ----
     Submits to Netlify Forms via AJAX (POST url-encoded to the site root),
     so the visitor stays on the page and sees an inline confirmation.
     Netlify captures the submission (dashboard + email notification).
     An explicit data-endpoint overrides the target if ever needed.       */
  document.querySelectorAll("form[data-spitshine]").forEach(function (form) {
    var wrap = form.closest(".form-wrap") || form.parentElement;
    var success = (wrap && wrap.querySelector(".form-success")) || form.querySelector(".form-success");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      var endpoint = form.getAttribute("data-endpoint");
      var target = (endpoint && endpoint.indexOf("REPLACE") === -1) ? endpoint : "/";
      var body = new URLSearchParams(new FormData(form)).toString();

      var done = function () {
        if (success) {
          success.classList.add("show");
          success.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        form.reset();
      };

      fetch(target, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body
      }).then(done).catch(done);
    });
  });
})();
