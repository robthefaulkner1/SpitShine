# Spit Shine San Antonio — Website

> San Antonio's Mobile Detailing & Ceramic Coating Specialists — We Come to You.

A fast, mobile-first, conversion-focused static website for **Spit Shine San Antonio**
(mobile auto detailing, ceramic coatings, and paint correction). Built to the brand's
copy package, website blueprint, and design rulebook.

No build tooling is required to host it — the `.html`, `css/`, `js/`, and `assets/`
files are plain static assets you can drop on any host.

---

## Pages

| Page | File | Purpose |
|------|------|---------|
| Home | `index.html` | Hero, why-choose, services overview, mobile benefits, process, service area, reviews |
| About | `about.html` | Story, values, philosophy, what sets us apart, commitment |
| Services | `services.html` | Mobile detailing, ceramic coating, paint correction, paint touch-up |
| Ceramic Coatings | `ceramic-coatings.html` | What it is, benefits, myths, process, aftercare |
| Paint Correction | `paint-correction.html` | What it is, defects, process, realistic expectations |
| Reviews | `reviews.html` | Testimonials + social-proof stats |
| FAQ | `faq.html` | Accordion FAQ (with FAQPage schema for rich results) |
| Contact | `contact.html` | Quote request form + contact info + service area |
| Book Appointment | `book.html` | Booking form, how-it-works, service-day expectations |

Plus `sitemap.xml`, `robots.txt`, and a `.nojekyll` flag for GitHub Pages.

---

## Design system

- **Colors** (strict brand palette): Burnt Orange `#CC5500`, Deep Black `#0A0A0A`,
  Metallic Silver `#C0C0C0`, Graphite `#4A4A4A`, Light Gray `#E5E5E5`.
- **Fonts:** Oswald (display/headlines), Inter (body) — loaded from Google Fonts.
- **Premium dark automotive aesthetic**, mobile-first, with:
  - sticky header (transparent → solid on scroll)
  - sticky mobile Call / Free-Quote bar
  - click-to-call links throughout
  - trust bars, CTA bands, FAQ accordion, scroll-reveal animations
  - `LocalBusiness` (AutoDetailing) schema on every page + `FAQPage` schema on the FAQ.

---

## Editing & rebuilding

The HTML pages are **generated** so the shared header, footer, SEO meta, and schema stay
consistent. Source of truth:

- `build.py` — template, design components, SEO/schema, and **`CONFIG`** (phone, email, etc.)
- `pages_content.py` — the copy/body of each page.

To regenerate the HTML after editing either file:

```bash
python3 build.py
```

You can also edit the generated `.html` files directly if you prefer — just note that a
re-run of `build.py` will overwrite them.

### ⚠️ Replace these placeholders before going live
Open `build.py` → `CONFIG` and update:

| Key | Replace with |
|-----|--------------|
| `phone_display` / `phone_tel` | Your real phone number (the `tel:` value must be E.164, e.g. `+12105551234`) |
| `email` | Your real business email |
| `domain` | Your live domain (used in canonical URLs, sitemap, and schema) |
| `form_endpoint` | A [Formspree](https://formspree.io) (or CRM) endpoint to receive form submissions |
| `social` | Your Facebook / Instagram / Google Business URLs |

Then re-run `python3 build.py` and update `sitemap.xml` / `robots.txt` with your domain.

---

## Booking & forms

**Booking → Calendly.** Every "Book" CTA opens the Calendly scheduler in a popup, and the
Book Appointment page (`book.html`) embeds it inline. The scheduling link lives in
`CONFIG["calendly_url"]` — update it there and rebuild to point at a different Calendly. The
popup wiring is in `js/main.js` (it targets links to `book.html` / `#book-form`, or any element
with the `.book-link` class).

**Contact / quote form.** The contact form runs **front-end only** — on submit it shows a
confirmation message. To receive real submissions by email, paste a Formspree endpoint into
`CONFIG["form_endpoint"]` and rebuild; `js/main.js` will POST to it automatically.

---

## Images

Photo slots are marked with labeled placeholders (e.g. *"Ceramic Coating Water-Beading"*).
Drop a real image into a placeholder by replacing the `<div class="media">…</div>` block with:

```html
<div class="media"><img src="assets/your-photo.jpg" alt="Descriptive alt text"></div>
```

High-impact spots to prioritize: **hero backgrounds**, **before/after paint correction**,
and **ceramic water-beading**. (See `js/main.js` and `css/styles.css` `.media` for styling.)

---

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploy

Any static host works — Netlify, Cloudflare Pages, Vercel, GitHub Pages, or traditional
hosting. This repo is set up for **Netlify**.

### Netlify (recommended)

The repo ships a `netlify.toml` that tells Netlify how to publish the site:

- `publish = "."` — serves the static files from the repo root
- `command = "python3 build.py"` — regenerates the pages from `build.py` + `pages_content.py`
  on each deploy, so the live site always matches the source (no pip install needed —
  `build.py` uses only the Python standard library)

**One-time setup (in the Netlify dashboard):**
1. Sign in at [app.netlify.com](https://app.netlify.com) (free).
2. **Add new site → Import an existing project → GitHub**, authorize, and pick
   `robthefaulkner1/SpitShine`.
3. Netlify auto-detects `netlify.toml` — just click **Deploy**. Build settings are filled in
   for you (publish `.`, command `python3 build.py`).
4. Every push to `main` then redeploys automatically. Netlify gives you a free
   `https://<name>.netlify.app` URL.

**Custom domain:** add it under **Site settings → Domain management** in Netlify, then update
`CONFIG["domain"]` in `build.py` (used for canonical URLs, the sitemap, and schema) and rebuild.
