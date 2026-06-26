# Business Listings Kit — Spit Shine San Antonio

A checklist of every place to list the business online, plus the exact info to use.
**Use the identical details below on every listing** — Google rewards consistent
Name / Address / Phone (NAP) across the web ("citations"). Inconsistent info hurts ranking.

As you create each profile, paste its public URL into `CONFIG["social"]` in `build.py`
and run `python3 build.py` — it auto-adds the link to the footer and to the site's
`sameAs` schema (which tells Google all these profiles are the same business).

---

## 📋 Canonical business info (copy-paste this everywhere)

| Field | Value |
|-------|-------|
| **Business name** | Spit Shine San Antonio |
| **Phone** | (210) 392-2782 |
| **Website** | https://getspitshined.com |
| **Email** | hello@getspitshined.com *(confirm this inbox works)* |
| **Address** | Service-area business — no storefront. List as **San Antonio, TX** and hide the street address. |
| **Primary category** | Auto detailing service |
| **Other categories** | Car detailing service · Ceramic coating · Auto restoration service · Mobile car wash |
| **Hours** | Mon–Sat 7:00 AM – 6:00 PM · Sun closed |
| **Service areas** | San Antonio, Boerne, New Braunfels, Schertz, Cibolo, Converse, Universal City, Helotes, Leon Valley, Alamo Heights, Stone Oak, Windcrest, Live Oak, Olmos Park |
| **Payment** | Cash, all major cards, Venmo, Zelle, Apple Pay |
| **Year started** | *(fill in)* |

**Short description (≤160 chars):**
> San Antonio's mobile detailing, ceramic coating & paint correction specialists. We come to you — no drop-off needed. Free quotes.

**Long description:**
> Spit Shine San Antonio brings dealership-quality detailing, professional ceramic coatings, and expert paint correction right to your driveway. As a locally owned mobile service, we work at your home, office, or wherever your vehicle is parked — no drop-offs, no waiting rooms. We use professional-grade products and stand behind every job. Serving San Antonio and the surrounding Hill Country communities. Call or text (210) 392-2782 for a free quote.

**Assets to upload:** logo (`assets/logo.png`), plus real before/after and finished-vehicle photos as you collect them.

---

## ✅ The listing checklist (work top to bottom)

### Tier 1 — Essential (free, do these first)
These are the highest-impact and feed Maps, Siri, and most "near me" searches.

- [ ] **Google Business Profile** — https://business.google.com — *the #1 local-SEO asset.* Set as a **service-area business**, add categories, hours, service areas, photos. Then request reviews here first.
- [ ] **Bing Places for Business** — https://www.bingplaces.com — powers Bing/Copilot maps. You can import from Google.
- [ ] **Apple Business Connect** — https://businessconnect.apple.com — Apple Maps + Siri ("detailing near me" on iPhones).
- [ ] **Yelp for Business** — https://biz.yelp.com — major for service businesses & reviews.
- [ ] **Facebook Business Page** — https://facebook.com/business — also enables reviews/recommendations.
- [ ] **Instagram (Business account)** — best channel for before/after photos.
- [ ] **Nextdoor Business** — https://business.nextdoor.com — huge for neighborhood/local word-of-mouth.

### Tier 2 — Strong directories & trust signals (mostly free)
- [ ] **Better Business Bureau (BBB)** — https://www.bbb.org — trust badge + citation.
- [ ] **Angi** (formerly Angie's List) — https://www.angi.com
- [ ] **Thumbtack** — https://www.thumbtack.com — lead generation for services.
- [ ] **Yellow Pages** — https://www.yellowpages.com
- [ ] **Foursquare** — https://foursquare.com/products/claim — feeds many apps/aggregators.
- [ ] **Mapquest** — https://www.mapquest.com
- [ ] **Alignable** — https://www.alignable.com — local B2B networking.
- [ ] **Manta** — https://www.manta.com
- [ ] **Hotfrog**, **Cylex**, **Brownbook**, **EZlocal**, **iBegin**, **Superpages**, **Citysearch** — quick general directories.

### Tier 3 — Local San Antonio & industry-specific
- [ ] **Greater San Antonio Chamber of Commerce** — https://www.sachamber.org (membership has a fee but strong local authority).
- [ ] **San Antonio Hispanic Chamber / local chambers** (Schertz, Boerne, New Braunfels, etc. — your service areas).
- [ ] **Nextdoor neighborhood recommendations** in each service-area city.
- [ ] Local FB groups / "Do210" / SA Current community listings.
- [ ] Auto-detailing directories & enthusiast forums (e.g., DetailingWiki business listings, local car-club pages).
- [ ] **Waze** — claim via the Waze Local / partner program for in-app pin.

### Data aggregators (optional power move)
Most directories pull from a few aggregators. A paid service can push your NAP to dozens at once and keep them in sync:
- [ ] **BrightLocal**, **Yext**, or **Moz Local** (paid) — submit once, sync everywhere. Worth it if you don't want to do Tier 2/3 by hand.

### Review platforms (set up, then actively ask customers)
Reviews are the single biggest ongoing ranking + conversion lever.
- [ ] Google · Yelp · Facebook · BBB · Nextdoor
- [ ] After every job: text the customer a direct link to your **Google review** page.

---

## 🔁 Keeping it in sync with the site
1. Create a listing → copy its public profile URL.
2. Paste it into the matching key in `CONFIG["social"]` (`build.py`). Add new keys for any others.
3. Run `python3 build.py` and deploy. The footer links + `sameAs` schema update automatically.
4. Re-check that the **name, phone, and website are byte-for-byte identical** to the table above.
