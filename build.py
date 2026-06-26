#!/usr/bin/env python3
"""
Static-site generator for Spit Shine San Antonio.

Run:  python3 build.py
Produces the 9 page HTML files in the project root using a shared
header / footer / SEO template so branding stays consistent.

All business contact details live in CONFIG below — update them in one
place and re-run the build.
"""
import json
import os

# --------------------------------------------------------------------------
# CONFIG  —  EDIT THESE, then re-run `python3 build.py`
# --------------------------------------------------------------------------
CONFIG = {
    "name": "Spit Shine San Antonio",
    "slogan": "San Antonio's Mobile Detailing & Ceramic Coating Specialists — We Come to You.",
    "domain": "https://spitshinesa.com",          # update to your live domain
    "phone_display": "(210) 392-2782",             # business phone (display)
    "phone_tel": "+12103922782",                   # business phone (E.164 for tel: links)
    "email": "hello@spitshinesa.com",              # << REPLACE with real email
    "hours": "Mon–Sat: 7:00 AM – 6:00 PM · Closed Sunday",
    "city": "San Antonio",
    "region": "TX",
    # Optional: paste a Formspree/endpoint URL to make the forms live.
    "form_endpoint": "https://formspree.io/f/REPLACE_ME",
    # Calendly scheduling link. Every "Book" CTA opens this in a popup, and
    # the Book Appointment page embeds it inline.
    "calendly_url": "https://calendly.com/faulkner-rob14?background_color=000000&text_color=cb5b11&primary_color=9a9a9a",
    "social": {
        "Facebook": "#",
        "Instagram": "#",
        "Google": "#",
    },
}

AREAS = ["San Antonio", "Boerne", "New Braunfels", "Schertz", "Cibolo",
         "Converse", "Universal City", "Helotes", "Leon Valley",
         "Alamo Heights", "Stone Oak", "Windcrest", "Live Oak", "Olmos Park"]

# --------------------------------------------------------------------------
# Inline SVG icons (stroke uses currentColor)
# --------------------------------------------------------------------------
I = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "droplet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5C12 2.5 5 9 5 14a7 7 0 0 0 14 0c0-5-7-11.5-7-11.5z"/><path d="M9 14a3 3 0 0 0 3 3"/></svg>',
 "sparkle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.9 4.6L18.5 9.5 13.9 11.4 12 16l-1.9-4.6L5.5 9.5l4.6-1.9L12 3z"/><path d="M19 14l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8.8-2z"/></svg>',
 "spray": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11V6a2 2 0 0 1 2-2h1V2"/><rect x="7" y="11" width="9" height="11" rx="2"/><line x1="16" y1="5" x2="20" y2="5"/><line x1="16" y1="8" x2="22" y2="8"/><line x1="18" y1="2" x2="18" y2="2.01"/><line x1="21" y1="3" x2="21" y2="3.01"/></svg>',
 "brush": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.06 11.9 3.6 17.36a2.05 2.05 0 1 0 3 2.78c.38-.4.6-.92.62-1.47l5.4-5.4"/><path d="m14 6 4 4"/><path d="M21.5 3.5a2.12 2.12 0 0 0-3 0L9 13l2 2 9.5-9.5a2.12 2.12 0 0 0 0-3z"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
 "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
 "image": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-4.35-4.35a2 2 0 0 0-2.83 0L4 21"/></svg>',
 "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M8.21 13.89 7 22l5-3 5 3-1.21-8.11"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "dollar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
 "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17H3v-5l2-5h14l2 5v5h-2"/><path d="M5 12h14"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13c0-5 4-9 16-9 0 9-4 16-9 16z"/><path d="M4 20c4-3 6-6 7-9"/></svg>',
}

STAR = '★'

# brand mark used in the nav / footer
MARK = ('<svg class="mark" viewBox="0 0 64 64" aria-hidden="true">'
        '<rect width="64" height="64" rx="14" fill="#141417" stroke="rgba(192,192,192,.2)"/>'
        '<path d="M32 14c6.5 8.4 12 14.4 12 21.4a12 12 0 1 1-24 0c0-7 5.5-13 12-21.4z" fill="#CC5500"/>'
        '<path d="M27 38a6 6 0 0 0 6 6" fill="none" stroke="#150b02" stroke-width="3" '
        'stroke-linecap="round" opacity=".55"/>'
        '<circle cx="45" cy="20" r="2" fill="#E5E5E5"/></svg>')


def icon(name):
    return I[name]


def stars(n=5):
    return f'<span class="stars" aria-label="{n} out of 5 stars">{STAR * n}</span>'


def btn(label, href, kind="primary", ico=None, lg=False, block=False):
    cls = f"btn btn-{kind}" + (" btn-lg" if lg else "") + (" btn-block" if block else "")
    inner = (icon(ico) if ico else "") + label
    return f'<a class="{cls}" href="{href}">{inner}</a>'


def placeholder(label, sub=""):
    s = f'<small>{sub}</small>' if sub else ""
    return (f'<div class="media reveal"><div class="ph">{icon("image")}'
            f'{label}{s}</div></div>')

# --------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------
NAV_ITEMS = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Services", "services.html"),
    ("Reviews", "reviews.html"),
    ("FAQ", "faq.html"),
    ("Contact", "contact.html"),
]


def header(active):
    def nav_link(label, href):
        cls = ' class="active"' if href == active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    links = "".join(nav_link(label, href) for label, href in NAV_ITEMS)
    return f'''<a class="skip-link" href="#main" style="position:absolute;left:-9999px;top:0;background:var(--orange);color:#150b02;padding:10px 16px;z-index:200;border-radius:0 0 8px 0;" onfocus="this.style.left='0'" onblur="this.style.left='-9999px'">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="{CONFIG['name']} home">
      <img class="brand-logo brand-logo--nav" src="assets/logo.png" width="512" height="512"
           alt="San Antonio Spit Shine — Mobile Detailing &amp; Ceramic Coating Specialists"
           decoding="async">
    </a>
    <nav class="nav-links" aria-label="Primary">{links}</nav>
    <div class="nav-cta">
      <a class="nav-phone" href="tel:{CONFIG['phone_tel']}">{icon('phone')}{CONFIG['phone_display']}</a>
      {btn('Book Now', 'book.html', 'primary')}
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav"><span></span></button>
    </div>
  </div>
</header>'''


def mobile_cta():
    return f'''<div class="mobile-cta">
  <a class="m-call" href="tel:{CONFIG['phone_tel']}">{icon('phone')} Call</a>
  <a class="m-quote" href="contact.html">{icon('calendar')} Free Quote</a>
</div>'''


def footer():
    svc = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in [
        ("Mobile Auto Detailing", "services.html"),
        ("Ceramic Coatings", "ceramic-coatings.html"),
        ("Paint Correction", "paint-correction.html"),
        ("Paint Touch-Up", "services.html#touchup"),
        ("Maintenance Plans", "services.html"),
    ])
    comp = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in [
        ("About Us", "about.html"),
        ("Reviews", "reviews.html"),
        ("FAQ", "faq.html"),
        ("Contact", "contact.html"),
        ("Book Appointment", "book.html"),
    ])
    socials = " ".join(f'<a href="{url}" aria-label="{n}">{n}</a>'
                       for n, url in CONFIG["social"].items())
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="index.html">
          <img class="brand-logo brand-logo--footer" src="assets/logo.png" width="512" height="512"
               alt="San Antonio Spit Shine — Mobile Detailing &amp; Ceramic Coating Specialists"
               loading="lazy" decoding="async"></a>
        <p>{CONFIG['slogan']} Locally owned and operated — bringing dealership-quality
        detailing, ceramic coatings, and paint correction right to your driveway.</p>
        <p style="margin-top:14px;color:var(--silver);font-size:.85rem">Licensed, insured &amp; professionally trained.</p>
      </div>
      <div class="footer-col"><h4>Services</h4><ul>{svc}</ul></div>
      <div class="footer-col"><h4>Company</h4><ul>{comp}</ul></div>
      <div class="footer-col footer-contact">
        <h4>Get In Touch</h4>
        <a href="tel:{CONFIG['phone_tel']}">{icon('phone')}{CONFIG['phone_display']}</a>
        <a href="mailto:{CONFIG['email']}">{icon('mail')}{CONFIG['email']}</a>
        <p>{icon('clock')}{CONFIG['hours']}</p>
        <p>{icon('pin')}Serving greater San Antonio &amp; the Hill Country</p>
        <p style="margin-top:8px">{socials}</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {CONFIG['name']}. All rights reserved.</span>
      <span class="badges">
        <span>Locally Owned &amp; Operated</span>
        <span>Professional Results Guaranteed</span>
        <span>{STAR}{STAR}{STAR}{STAR}{STAR} 5-Star Rated</span>
      </span>
    </div>
  </div>
</footer>'''


def local_business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "AutoDetailing",
        "name": CONFIG["name"],
        "image": f"{CONFIG['domain']}/assets/favicon.svg",
        "url": CONFIG["domain"],
        "telephone": CONFIG["phone_tel"],
        "email": CONFIG["email"],
        "priceRange": "$$",
        "slogan": CONFIG["slogan"],
        "address": {"@type": "PostalAddress", "addressLocality": "San Antonio",
                    "addressRegion": "TX", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": a} for a in AREAS],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "07:00", "closes": "18:00"}],
        "sameAs": [u for u in CONFIG["social"].values() if u != "#"],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
            ["Mobile Auto Detailing", "Ceramic Coating", "Paint Correction", "Paint Touch-Up"]
        ],
    }


# --------------------------------------------------------------------------
# Page assembler
# --------------------------------------------------------------------------
def page(filename, title, desc, active, hero_html, body_html, extra_schema=None):
    schema_blocks = [local_business_schema()]
    if extra_schema:
        schema_blocks.append(extra_schema)
    schema_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s)}</script>'
        for s in schema_blocks)
    canonical = f"{CONFIG['domain']}/{'' if filename == 'index.html' else filename}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="{CONFIG['name']}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{CONFIG['domain']}/assets/logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{CONFIG['domain']}/assets/logo.png">
<link rel="icon" type="image/png" sizes="64x64" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>
{schema_html}
</head>
<body data-calendly="{CONFIG['calendly_url']}">
{header(active)}
<main id="main">
{hero_html}
{body_html}
</main>
{footer()}
{mobile_cta()}
<script src="js/main.js" defer></script>
</body>
</html>'''
    with open(filename, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", filename)


# --------------------------------------------------------------------------
# Reusable section builders
# --------------------------------------------------------------------------
def hero(h1, slogan=None, sub=None, buttons=None, page_class=""):
    sl = f'<p class="slogan">{slogan}</p>' if slogan else ""
    sb = f'<p class="hero-sub">{sub}</p>' if sub else ""
    bt = f'<div class="btn-row">{buttons}</div>' if buttons else ""
    return f'''<section class="hero {page_class}">
  <div class="hero-bg"></div>
  <div class="container"><div class="hero-inner reveal">
    <h1>{h1}</h1>{sl}{sb}{bt}
  </div></div>
</section>'''


def trustbar(items=None):
    items = items or [
        ("award", "Trusted by San Antonio Vehicle Owners"),
        ("car", "Mobile Service Throughout Greater SA"),
        ("shield", "Professional Results Guaranteed"),
        ("stars", f"{STAR}{STAR}{STAR}{STAR}{STAR} 5-Star Rated"),
    ]
    out = []
    for ic, txt in items:
        if ic == "stars":
            out.append(f'<div class="trust-item"><span class="stars">{txt}</span></div>')
        else:
            out.append(f'<div class="trust-item">{icon(ic)}<span>{txt}</span></div>')
    return f'<section class="trustbar"><div class="container">{"".join(out)}</div></section>'


def cta_band(h2, p, buttons):
    return f'''<section class="section cta-band">
  <div class="container reveal">
    <h2>{h2}</h2><p>{p}</p>
    <div class="btn-row">{buttons}</div>
  </div></section>'''


def checklist(items, tight=False):
    cls = "checklist checklist--tight" if tight else "checklist"
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<ul class="{cls}">{lis}</ul>'


# --------------------------------------------------------------------------
# Build everything
# --------------------------------------------------------------------------
import pages_content  # noqa: E402  (content lives in a sibling module)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pages_content.build(globals())
    print("\nDone. Open index.html in a browser.")
