# CLAUDE.md — Spit Shine San Antonio website

Static, mobile-first marketing site for a mobile auto-detailing / ceramic-coating /
paint-correction business. No framework, no build step required to host.

## How it's built
- HTML pages are **generated** by `build.py` (template + components + SEO/schema + `CONFIG`)
  using copy from `pages_content.py`. Run `python3 build.py` to regenerate all 9 pages.
- Shared chrome (header, footer, sticky mobile CTA, schema) lives in `build.py` — edit there,
  not in individual HTML files, or your change will be overwritten on the next build.
- Styling: `css/styles.css` (CSS custom properties for the brand palette). JS: `js/main.js`
  (mobile nav, sticky header, FAQ accordion, scroll-reveal, form handling).

## Brand rules (do not deviate)
- Palette only: Burnt Orange `#CC5500`, Deep Black `#0A0A0A`, Silver `#C0C0C0`,
  Graphite `#4A4A4A`, Light Gray `#E5E5E5`. No bright blues/reds/greens/purple.
- Fonts: Oswald (display), Inter (body). Premium dark automotive aesthetic.
- Every page: trust indicators, primary + secondary CTA, click-to-call, mobile sticky CTA,
  `LocalBusiness`/`AutoDetailing` schema. FAQ page also has `FAQPage` schema.

## Conventions
- Business contact details and the form endpoint live in `CONFIG` at the top of `build.py`.
  Update there, then rebuild. Phone `tel:` values are E.164.
- Image placeholders use `placeholder(label, sub)` → `.media` blocks; replace with `<img>`.
- After editing `build.py` or `pages_content.py`, always run `python3 build.py` and verify
  the generated HTML before committing.
