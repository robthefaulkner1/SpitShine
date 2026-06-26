# -*- coding: utf-8 -*-
"""Page bodies for Spit Shine San Antonio. Imported by build.py."""


def build(g):
    page = g["page"]; hero = g["hero"]; trustbar = g["trustbar"]; btn = g["btn"]
    icon = g["icon"]; cta_band = g["cta_band"]; checklist = g["checklist"]
    placeholder = g["placeholder"]; stars = g["stars"]; CONFIG = g["CONFIG"]
    AREAS = g["AREAS"]; STAR = g["STAR"]
    PHONE = CONFIG["phone_tel"]; PH_D = CONFIG["phone_display"]

    QUOTE = btn("Get a Free Quote", "contact.html", "primary")
    CALL = btn("Call Us Now", f"tel:{PHONE}", "secondary", ico="phone")
    BOOK = btn("Book Your Appointment", "book.html", "primary")

    def section(inner, cls="section", extra=""):
        return f'<section class="{cls}"{extra}><div class="container">{inner}</div></section>'

    def submit_btn(label, ico="arrow"):
        return (f'<button class="btn btn-primary btn-lg" type="submit">'
                f'{icon(ico)}{label}</button>')

    def head(eyebrow, h2, p="", center=True):
        c = " center" if center else ""
        pp = f"<p>{p}</p>" if p else ""
        return (f'<div class="section-head{c} reveal"><span class="eyebrow">{eyebrow}</span>'
                f'<h2>{h2}</h2><div class="divider-orange"></div>{pp}</div>')

    def card(ic, title, body, link=None, link_href="#"):
        lk = (f'<a class="card-link" href="{link_href}">{link} {icon("arrow")}</a>'
              if link else "")
        return (f'<div class="card reveal"><div class="icon">{icon(ic)}</div>'
                f'<h3>{title}</h3><p>{body}</p>{lk}</div>')

    def review(text, name, meta, n=5):
        return (f'<div class="review reveal">{stars(n)}'
                f'<blockquote>“{text}”</blockquote>'
                f'<div class="who"><div class="name">{name}</div>'
                f'<div class="meta">{meta}</div></div></div>')

    def steps(items):
        out = "".join(
            f'<div class="step reveal"><div class="num"></div><div>'
            f'<h3>{t}</h3><p>{d}</p></div></div>' for t, d in items)
        return f'<div class="steps">{out}</div>'

    def area_chips():
        return '<div class="chips reveal">' + "".join(
            f'<span class="chip">{a}</span>' for a in AREAS) + '</div>'

    # ======================================================================
    # HOME
    # ======================================================================
    home_hero = hero(
        'Your Car Deserves Better.<br><span class="accent">We\'ll Prove It.</span>',
        slogan=CONFIG["slogan"],
        sub="Locally owned mobile detailing, ceramic coatings &amp; paint correction — "
            "delivered to your home, office, or wherever your vehicle is parked. "
            "No drop-offs. No waiting rooms. Just outstanding results.",
        buttons=QUOTE + CALL,
    )

    why_choose = section(
        f'''{head("Why Choose Us", "We Don't Just Clean Cars. We Transform Them.",
        "There's a difference between a quick wash and a real detail. At Spit Shine San Antonio, "
        "we specialize in the kind of work that makes you stop and stare when you walk back to your vehicle.")}
        <div class="grid grid-3">
          {card("car","100% Mobile Service","We work at your home, office, or wherever your vehicle is parked — same professional equipment, zero hassle.")}
          {card("award","Expert Technicians","Trained in professional-grade detailing, ceramic coatings, and paint correction. This is our craft, not a side gig.")}
          {card("droplet","Premium Products Only","We use industry-leading ceramic coating systems and detailing products — never consumer-grade substitutes.")}
          {card("dollar","Honest Pricing","No hidden fees, no upsell pressure. Just clear, transparent quotes before any work begins.")}
          {card("heart","Customer-First Approach","We're not done until you're completely satisfied with the results — guaranteed.")}
          {card("pin","Locally Owned","We're San Antonians serving San Antonians. This community is our community.")}
        </div>''',
        cls="section section--alt")

    services_overview = section(
        f'''{head("What We Do", "Premium Automotive Appearance Services",
        "From a quick refresh to a full ceramic coating system, Spit Shine San Antonio offers a complete lineup of premium services — all delivered to your door.")}
        <div class="grid grid-4">
          {card("spray","Mobile Auto Detailing","Hand washes, full interior &amp; exterior details, and decontamination — performed on-location at your convenience.","Learn More","services.html")}
          {card("droplet","Ceramic Coatings","The most advanced paint protection available. A hydrophobic, scratch-resistant barrier that lasts years, not days.","Learn More","ceramic-coatings.html")}
          {card("sparkle","Paint Correction","Swirl marks, scratches, water spots, and oxidation removed at the microscopic level for mirror-like clarity.","Learn More","paint-correction.html")}
          {card("brush","Paint Touch-Up","Professional touch-up that blends with your factory finish, minimizes damage, and protects exposed metal from rust.","Learn More","services.html#touchup")}
        </div>
        <div class="center" style="margin-top:36px">{btn("View All Services","services.html","secondary",ico="arrow")}</div>''')

    mobile_benefits = section(
        f'''<div class="split">
          <div class="body reveal">
            <span class="eyebrow">Benefits of Mobile Detailing</span>
            <h2>Detailing Without the Drop-Off</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>Traditional detailing shops are inconvenient. You drop your car off, find a ride home,
            wait for a callback, then find another ride back to pick it up. Who has time for that?</p>
            <p>With Spit Shine San Antonio, the whole experience is different — same professional
            equipment, same expert technicians, same outstanding results, just without the hassle.</p>
            {checklist([
              "We schedule at your convenience — mornings, evenings, weekdays, and weekends",
              "We come to your home, your workplace, or anywhere your vehicle is parked",
              "Watch us work, ask questions, or go about your day — whatever works for you",
              "Your vehicle is ready when we're done. No waiting, no coordinating rides",
            ])}
            <div class="btn-row" style="margin-top:8px">{btn("Book a Mobile Detail","book.html","primary")}</div>
          </div>
          {placeholder("Mobile Detail Technician Polishing a Vehicle","[ Image: on-location detail at customer's driveway ]")}
        </div>''',
        cls="section section--panel")

    ceramic_paint = section(
        f'''<div class="split reverse">
          {placeholder("Ceramic Coating Water-Beading Effect","[ Image: water beading on a freshly coated hood ]")}
          <div class="body reveal">
            <span class="eyebrow">Protection That Lasts</span>
            <h2>Ceramic Coating &amp; Paint Correction</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>Car wax lasts a few weeks. A ceramic coating lasts years. If you're serious about
            protecting your vehicle's paint and keeping it looking its best, ceramic coating is the
            single best investment you can make.</p>
            {checklist([
              "<strong>Hydrophobic surface</strong> that repels water, mud, and road grime",
              "<strong>Scratch &amp; swirl resistance</strong> that holds up to daily driving",
              "<strong>UV protection</strong> that prevents paint fade and oxidation",
              "<strong>Deep, glossy finish</strong> that enhances your color and depth",
            ])}
            <div class="btn-row">
              {btn("Explore Ceramic Coatings","ceramic-coatings.html","primary")}
              {btn("Explore Paint Correction","paint-correction.html","secondary")}
            </div>
          </div>
        </div>''')

    process = section(
        f'''{head("Customer Experience", "What to Expect When You Book With Spit Shine",
        "We've made our entire process as smooth as possible — from the first inquiry to the final reveal.")}
        {steps([
          ("Get Your Free Quote","Tell us about your vehicle and what you're looking for. We'll recommend the right service and give you an honest, transparent price."),
          ("We Schedule Around You","Pick the date and time that works for your schedule. Early morning, afternoon, or Saturday — we'll make it work."),
          ("We Come to You","Our team shows up at your location, fully equipped and ready to work. All we need is access to your vehicle and a flat surface."),
          ("Watch the Transformation","Be there the whole time or go about your day. Either way, we'll give you a full walkthrough of the results when we're done."),
          ("Drive Away Smiling","Your vehicle will look better than it has in years — and you'll wonder why you didn't book sooner."),
        ])}''',
        cls="section section--alt")

    service_area = section(
        f'''{head("Service Area", "Serving San Antonio &amp; the Surrounding Area",
        "Spit Shine San Antonio is proud to serve vehicle owners throughout the greater San Antonio metro area.")}
        {area_chips()}
        <p class="center" style="margin-top:26px;color:var(--silver)">Not sure if we cover your area?
        {btn("Just Ask Us","contact.html","secondary").replace("<a ","<a style='margin-left:8px' ")}</p>''')

    home_reviews = section(
        f'''{head("Reviews", "Trusted by San Antonio Vehicle Owners")}
        <div class="grid grid-3">
          {review("My truck looked like it just came off the dealer lot when they were done. They even got the stubborn water spots off my windshield that nobody else could touch.","Marcus T.","San Antonio · 2021 Chevy Tahoe · Full Detail")}
          {review("Hands down the best money I've spent on my truck. The ceramic coating looks incredible and the water just sheets right off now. Professional, on time, and they explained everything.","David R.","Stone Oak · 2023 F-150 · Ceramic Coating")}
          {review("They did a two-step paint correction and I genuinely could not believe the difference. My car looks better than it ever did. Wish I'd called them the day I bought it.","Jennifer M.","Alamo Heights · 2020 Honda Accord · Paint Correction")}
        </div>
        <div class="center" style="margin-top:36px">{btn("Read More Reviews","reviews.html","secondary",ico="arrow")}</div>''',
        cls="section section--panel")

    home_cta = cta_band(
        "Ready to See What Your Vehicle Is Really Capable of Looking Like?",
        "Join hundreds of San Antonio vehicle owners who trust Spit Shine with their pride and joy. "
        "Appointments are limited — book yours today before our schedule fills up.",
        BOOK + QUOTE + CALL)

    page("index.html",
         "Mobile Auto Detailing & Ceramic Coating San Antonio | Spit Shine SA",
         "San Antonio's top-rated mobile detailing, ceramic coating, and paint correction "
         "specialists. We come to you — no drop-off needed. Book your appointment today!",
         "index.html", home_hero,
         trustbar() + why_choose + services_overview + mobile_benefits +
         ceramic_paint + process + service_area + home_reviews + home_cta)

    # ======================================================================
    # ABOUT
    # ======================================================================
    about_hero = hero(
        'We Started Spit Shine Because <span class="accent">San Antonio Deserved Better.</span>',
        sub="Great detailing shouldn't require a trip across town, a wasted afternoon, or a generic "
            "shop that treats your vehicle like a number. So we decided to do something about it.",
        buttons=BOOK + QUOTE, page_class="hero--page")

    about_story = section(
        f'''<div class="split">
          <div class="body reveal">
            <span class="eyebrow">Our Story</span>
            <h2>Born From a Simple Frustration</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>Spit Shine San Antonio was born out of a simple frustration: too many vehicle owners
            were settling for mediocre results from shops that didn't really care about the work they
            were putting out. Too many people were waiting hours at impersonal shops, only to get their
            car back with swirl marks still visible in every sunlight angle.</p>
            <p>We knew there was a better way — to deliver professional-grade detailing, expert ceramic
            coatings, and real paint correction right to your driveway, on your schedule, at a price that
            reflects honest craftsmanship rather than corporate overhead.</p>
            <p>Today, we're proud to be one of San Antonio's most trusted mobile detailing companies,
            serving customers across the city and the surrounding communities.</p>
          </div>
          {placeholder("Founder With a Freshly Detailed Vehicle","[ Image: founder / team portrait on location ]")}
        </div>''')

    about_values = section(
        f'''{head("Our Core Values", "How We Operate Every Single Day")}
        <div class="grid grid-3">
          {card("award","Quality First","Every vehicle gets our full attention and our best work — no shortcuts, no cutting corners.")}
          {card("clock","Respect for Your Time","We come to you, work efficiently, and get the job done without disrupting your day.")}
          {card("heart","Honest Expertise","We educate our customers, set realistic expectations, and never oversell services you don't need.")}
          {card("sparkle","Pride in the Craft","We treat every vehicle like it's our own and take genuine satisfaction in the results.")}
          {card("pin","Local Commitment","We're proud to serve San Antonio and its surrounding communities as a locally owned business.")}
          {card("shield","We Stand Behind Our Work","If something isn't right, we make it right. Every service is backed by our satisfaction guarantee.")}
        </div>''',
        cls="section section--alt")

    about_philosophy = section(
        f'''<div class="split reverse">
          {placeholder("Technician Applying Ceramic Coating","[ Image: close-up of careful, panel-by-panel work ]")}
          <div class="body reveal">
            <span class="eyebrow">Our Philosophy</span>
            <h2>The Right Way, Every Time</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>There are shortcuts in this industry. We don't take them.</p>
            <p>You'll never see us rushing through a paint correction to squeeze in another job. You'll
            never see us applying a ceramic coating to paint that hasn't been properly prepared. You'll
            never see us use subpar products because they're cheaper.</p>
            <p>The Spit Shine way isn't just about a clean car. It's about a car that turns heads,
            holds its value, and makes you proud every time you walk up to it.</p>
          </div>
        </div>''',
        cls="section section--panel")

    about_diff = section(
        f'''{head("What Sets Us Apart", "What Makes Spit Shine San Antonio Different")}
        <div style="max-width:820px;margin:0 auto">
        {checklist([
          "We're <strong>truly mobile</strong> — our setup goes wherever your vehicle is",
          "We invest in <strong>professional-grade equipment and premium products</strong> — not consumer-grade substitutes",
          "We <strong>specialize</strong> in detailing, ceramic coatings, and paint correction — these are our core expertise, not add-ons",
          "We <strong>educate our customers</strong> — we want you to understand what we're doing and why",
          "We <strong>stand behind our work</strong> — if something isn't right, we make it right",
          "We're <strong>locally owned and operated</strong> — your money stays in San Antonio",
        ])}
        </div>''')

    about_commit = section(
        f'''{head("Our Commitment", "Our Commitment to You")}
        <div style="max-width:760px;margin:0 auto;text-align:center">
          <p class="lead">When you book with Spit Shine San Antonio, you're not just getting a detail.
          You're getting a team that's fully invested in making your vehicle look its best.</p>
        </div>
        <div class="grid grid-2" style="max-width:900px;margin:36px auto 0">
          {card("clock","Always On Time","Arriving on time and fully prepared for every appointment.")}
          {card("heart","Honest Communication","Communicating honestly about what your vehicle needs — and what it doesn't.")}
          {card("droplet","Professional Products","Using professional-grade products and techniques on every single service.")}
          {card("shield","Complete Satisfaction","Following up to make sure you're completely satisfied. Your vehicle is an investment — we treat it like one.")}
        </div>''',
        cls="section section--alt")

    about_cta = cta_band(
        "Ready to Experience the Spit Shine Difference?",
        "Schedule your appointment today and find out why San Antonio vehicle owners keep coming back to Spit Shine.",
        BOOK + QUOTE)

    page("about.html",
         "About Spit Shine San Antonio | Locally Owned Mobile Detailing Experts",
         "Learn about Spit Shine San Antonio — a locally owned mobile detailing, ceramic coating, "
         "and paint correction company serving the greater San Antonio area.",
         "about.html", about_hero,
         trustbar() + about_story + about_values + about_philosophy +
         about_diff + about_commit + about_cta)

    # ======================================================================
    # SERVICES
    # ======================================================================
    services_hero = hero(
        'Professional Appearance Services — <span class="accent">Delivered to Your Door</span>',
        sub="From a quick exterior refresh to a full multi-stage paint correction and ceramic coating "
            "system, Spit Shine San Antonio has the expertise and equipment to handle it all. The only "
            "difference between us and a detailing shop? We come to you.",
        buttons=QUOTE + CALL, page_class="hero--page")

    def pkg_card(name, desc, tag=None, featured=False):
        cls = "pkg featured reveal" if featured else "pkg reveal"
        tg = f'<span class="tag">{tag}</span>' if tag else ''
        return (f'<div class="{cls}">{tg}<h3>{name}</h3>'
                f'<p class="desc">{desc}</p>'
                f'<a class="card-link" href="contact.html" style="margin-top:auto;padding-top:14px">'
                f'Get a Quote {icon("arrow")}</a></div>')

    def packages_block(title, items, cols=3):
        cards = "".join(pkg_card(*it) for it in items)
        return (f'<div style="margin-top:48px">'
                f'<h3 class="center" style="font-size:1.4rem;margin-bottom:8px">{title}</h3>'
                f'<div class="divider-orange" style="margin:0 auto 30px"></div>'
                f'<div class="grid grid-{cols}">{cards}</div></div>')

    def service_block(anchor, ic, eyebrow, title, intro, included_title, included, benefits,
                      ideal, process_txt, ctas, reverse=False, ph_label="", ph_sub="",
                      packages_html=""):
        media = placeholder(ph_label, ph_sub)
        body = f'''<div class="body reveal">
            <div class="icon" style="width:54px;height:54px;border-radius:12px;display:grid;place-items:center;background:rgba(204,85,0,.12);border:1px solid rgba(204,85,0,.3);margin-bottom:16px">{icon(ic)}</div>
            <span class="eyebrow">{eyebrow}</span>
            <h2>{title}</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>{intro}</p>
          </div>'''
        split = (f'<div class="split {"reverse" if reverse else ""}">'
                 + (media + body if not reverse else body + media) + '</div>')
        cols = f'''<div class="grid grid-2" style="margin-top:34px">
          <div class="card reveal"><h3 style="font-size:1.15rem;color:var(--orange-bright)">{included_title}</h3>{checklist(included, tight=True)}</div>
          <div class="card reveal"><h3 style="font-size:1.15rem;color:var(--orange-bright)">Benefits</h3>{checklist(benefits, tight=True)}</div>
        </div>
        <div class="grid grid-2" style="margin-top:24px">
          <div class="card reveal"><h3 style="font-size:1.15rem">Ideal For</h3><p style="color:var(--silver)">{ideal}</p></div>
          <div class="card reveal"><h3 style="font-size:1.15rem">Our Process</h3><p style="color:var(--silver)">{process_txt}</p></div>
        </div>'''
        btnrow = f'<div class="btn-row reveal" style="margin-top:30px">{ctas}</div>'
        return (f'<section class="section" id="{anchor}"><div class="container">'
                f'{split}{cols}{packages_html}{btnrow}</div></section>')

    s1 = service_block(
        "detailing", "spray", "Service 01", "Mobile Auto Detailing",
        "A real detail isn't just a car wash with a vacuum. It's a systematic, professional approach to "
        "cleaning and conditioning every surface of your vehicle — from the paint to the leather, from the "
        "glass to the wheel wells. We offer a range of mobile detailing packages to fit your vehicle and schedule.",
        "What's Included (varies by package)",
        ["Hand wash with pH-neutral soap", "Clay bar decontamination", "Foam cannon pre-soak",
         "Wheel &amp; tire cleaning and dressing", "Glass cleaning inside &amp; out",
         "Interior vacuum — seats, carpet, mats, trunk", "Dashboard, console &amp; door panel wipe-down",
         "Leather or vinyl conditioning", "Paint sealant or wax (package dependent)"],
        ["Removes harmful contaminants that damage paint", "Conditions &amp; protects interior surfaces from UV",
         "Restores and maintains your vehicle's appearance", "Protects resale value",
         "Eliminates odors and allergens from the interior"],
        "Any vehicle owner who wants their car to look great and be properly maintained — daily driver, "
        "weekend car, family SUV, or prized classic.",
        "We assess your vehicle's condition, then methodically work top to bottom on the exterior and "
        "front to back on the interior. Every section is inspected before we move to the next.",
        btn("Book a Mobile Detail", "book.html", "primary") + btn("Get a Quote", "contact.html", "secondary"),
        ph_label="Full Interior &amp; Exterior Detail", ph_sub="[ Image: gleaming finished detail ]",
        packages_html=packages_block("Mobile Detailing Packages", [
            ("The Spit Shine Express",
             "The fast-track to a clean, fresh vehicle. Perfect for busy San Antonians who want a polished "
             "look without a full-day commitment. Exterior wash, hand dry, tire dressing, and interior "
             "vacuum and wipe-down."),
            ("The Full Spit Shine",
             "The complete treatment. Interior and exterior detail with hand wash, clay bar, dressing, deep "
             "interior clean, glass treatment, and more. This is the service that makes people turn heads "
             "in the parking lot."),
            ("The Spit Shine Signature",
             "Our flagship premium detail — the works. Everything in The Full Spit Shine, plus a machine "
             "polish, sealant, leather conditioning, and engine bay wipe-down. Reserve this one for special "
             "occasions or when your vehicle needs to look absolutely flawless.", "Flagship", True),
            ("The Shine Time Treatment",
             "A targeted interior or exterior refresh for vehicles that need attention in one specific area. "
             "Great for picking up where the last service left off."),
        ], cols=4))

    s2 = service_block(
        "ceramic", "droplet", "Service 02", "Ceramic Coatings",
        "If you want the best long-term protection available for your vehicle's paint, ceramic coating is "
        "the answer. Unlike wax or sealant that wears off in weeks, a professionally applied ceramic coating "
        "bonds chemically to your paint and provides years of protection.",
        "What Ceramic Coating Does",
        ["Creates a hydrophobic, self-cleaning surface", "Adds scratch &amp; swirl resistance to your clear coat",
         "Blocks UV rays that cause fade and oxidation", "Enhances gloss and color depth",
         "Makes washing dramatically easier", "Protects against bird droppings, sap &amp; chemicals"],
        ["Long-lasting protection — 2 to 7+ years", "Significant reduction in washing time &amp; frequency",
         "Enhanced appearance and resale value", "One-time investment vs. repeated wax costs"],
        "New vehicle owners protecting their investment, enthusiasts with high-value vehicles, daily drivers "
        "tired of constant washing, or anyone who just had paint correction and wants to lock in the results.",
        "Proper paint prep — wash, decontamination, and correction if needed — is performed before every "
        "coating. The coating is applied in a controlled environment, allowed to cure, and we follow up with "
        "detailed aftercare instructions.",
        btn("Learn About Ceramic Coatings", "ceramic-coatings.html", "primary") +
        btn("Get a Ceramic Quote", "contact.html", "secondary"),
        reverse=True, ph_label="Ceramic Coating Water-Beading", ph_sub="[ Image: hydrophobic beading demo ]",
        packages_html=packages_block("Ceramic Coating Packages", [
            ("The Liquid Armor — Entry Coat",
             "A professional-grade single-layer ceramic coating providing 2–3 years of protection. "
             "Hydrophobic barrier, enhanced gloss, and UV protection. Ideal for daily drivers seeking "
             "long-term protection at an accessible price."),
            ("The Liquid Armor — Pro Shield",
             "A two-layer ceramic system with 4–5 years of durability. Superior scratch resistance, deeper "
             "gloss, and advanced hydrophobic performance. Our most popular coating package for enthusiasts "
             "and commuters alike.", "Most Popular", True),
            ("The Mirror Maker — Ultimate Guard",
             "The pinnacle of paint protection. Multi-layer professional ceramic coating system with up to "
             "7+ years of protection, maximum gloss depth, and the kind of reflective clarity that makes "
             "your vehicle look like a mirror on wheels."),
        ], cols=3))

    s3 = service_block(
        "correction", "sparkle", "Service 03", "Paint Correction",
        "Swirl marks, scratches, water spots, and oxidation are not permanent — they just look that way. "
        "Paint correction uses professional machine polishers and specialized compounds to safely remove "
        "these defects from your clear coat, revealing the vibrant, flawless paint underneath.",
        "Common Defects We Correct",
        ["Swirl marks from car washes &amp; improper washing", "Light to deep scratches",
         "Water spots and mineral deposits", "Oxidation and paint fade",
         "Buffer trails from amateur polish attempts", "Haze and light etching from sap or droppings"],
        ["Restores deep gloss and clarity", "Dramatically improves aging or neglected vehicles",
         "Creates an ideal surface for ceramic coating", "Adds value when preparing a vehicle for sale",
         "Results no amount of waxing could achieve"],
        "Vehicles with visible paint defects, older vehicles that have lost their luster, or any owner who "
        "wants to maximize their paint's appearance before a ceramic coating.",
        "We wash and decontaminate, then use a paint thickness gauge to assess clear coat depth. A test spot "
        "determines the right machine, pad, and compound. We then work panel by panel, inspecting under "
        "focused lighting to ensure every defect is addressed.",
        btn("Learn About Paint Correction", "paint-correction.html", "primary") +
        btn("Get a Correction Quote", "contact.html", "secondary"),
        ph_label="Before &amp; After Paint Correction", ph_sub="[ Image: split before/after panel ]",
        packages_html=packages_block("Paint Correction Packages", [
            ("The Gloss Boss — One-Step",
             "Single-stage machine polish targeting light swirl marks, minor scratches, and dull oxidation. "
             "Restores clarity and gloss to paint with moderate imperfections."),
            ("The Showroom Revival — Two-Step",
             "Two-stage paint correction combining a cutting compound and finishing polish. Removes deeper "
             "swirls, water spots, and scratches while refining the surface to near-perfect clarity.",
             "Most Popular", True),
            ("The Glass Act — Full Correction",
             "Multi-stage paint correction for vehicles with severe paint defects, heavy oxidation, or "
             "neglected finishes. This is the transformation package — before and after photos are almost "
             "unbelievable."),
        ], cols=3))

    s4 = service_block(
        "touchup", "brush", "Service 04", "Paint Touch-Up Services",
        "Rock chips, door dings, and paint scuffs happen — especially in a city as busy as San Antonio. "
        "While touch-up isn't always invisible, professional touch-up work significantly reduces the "
        "appearance of paint damage and, more importantly, seals bare metal to prevent rust and corrosion.",
        "What We Address",
        ["Rock chips and road damage", "Key scratches (when not too deep)",
         "Minor door edge chips", "Small scuffs and scrapes"],
        ["Protects exposed metal from rust", "Significantly reduces the look of paint damage",
         "More affordable than a body-shop respray for minor damage", "Done on-location at your home or office"],
        "Vehicle owners with rock chips or minor paint damage who want to protect the affected areas and "
        "improve appearance without a full respray.",
        "We're honest about results — touch-up work won't be invisible under all lighting, but it will "
        "protect your vehicle from rust and dramatically reduce the visual impact. We'll show you what to "
        "expect before we start.",
        btn("Get a Touch-Up Quote", "contact.html", "primary"),
        reverse=True, ph_label="Professional Paint Touch-Up", ph_sub="[ Image: chip repair close-up ]")

    maintenance = section(
        f'''{head("Maintenance Plans", "Keep It Looking New Between Services",
        "Already had a full detail or a ceramic coating? Keep that just-finished look with a recurring "
        "maintenance plan built around your vehicle.")}
        <div class="grid grid-2" style="max-width:860px;margin:0 auto">
          {pkg_card("The Upkeep", "Monthly maintenance wash and detail to keep your vehicle looking freshly "
                    "detailed between full services. Perfect for customers who just had a Spit Shine "
                    "Signature or ceramic coating.")}
          {pkg_card("The Coat Check", "Ceramic coating maintenance service including a pH-neutral hand wash, "
                    "decontamination, and reapplication of a coating booster. Extends the life of your "
                    "ceramic coating and maintains that just-coated look.")}
        </div>''',
        cls="section section--alt", extra=' id="maintenance"')

    services_cta = cta_band(
        "Not Sure Which Service Is Right for You?",
        "Reach out and tell us about your vehicle and what you'd like to accomplish. We'll recommend the "
        "right service, give you an honest quote, and get you scheduled at a time that works for you.",
        QUOTE + BOOK)

    page("services.html",
         "Auto Detailing Services San Antonio | Mobile Detailing, Ceramic Coating & Paint Correction",
         "Explore the full range of mobile auto detailing services from Spit Shine San Antonio — including "
         "ceramic coatings, paint correction, and paint touch-up. We come to you!",
         "services.html", services_hero,
         trustbar() + s1 + s2 + s3 + s4 + maintenance + services_cta)

    # ======================================================================
    # CERAMIC COATINGS
    # ======================================================================
    ceramic_hero = hero(
        'The Last Paint Protection Your Vehicle Will <span class="accent">Need for Years.</span>',
        sub="Professional ceramic coating installation in San Antonio — applied correctly, cured properly, "
            "and backed by our satisfaction guarantee.",
        buttons=btn("Get a Free Ceramic Coating Quote", "contact.html", "primary") + CALL,
        page_class="hero--page")

    ceramic_what = section(
        f'''<div class="split">
          <div class="body reveal">
            <span class="eyebrow">What Is Ceramic Coating?</span>
            <h2>A Liquid Glass Shield for Your Paint</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>Ceramic coating (sometimes called nano-ceramic or 9H coating) is a liquid polymer that
            chemically bonds to your vehicle's clear coat and creates a hard, semi-permanent protective layer.</p>
            <p>This is fundamentally different from wax or sealant. Wax sits on top of the paint and washes
            away within weeks. A ceramic coating bonds at the molecular level and becomes part of your
            vehicle's finish — until it's intentionally removed.</p>
            <p>When professionally prepared and installed by the Spit Shine team, ceramic coating transforms
            the way your vehicle looks, feels, and performs against the elements — for years, not weeks.</p>
          </div>
          {placeholder("Luxury SUV Reflecting Ceramic Finish","[ Image: deep-gloss reflection shot ]")}
        </div>''')

    ceramic_benefits = section(
        f'''{head("The Benefits", "What Ceramic Coating Actually Does for Your Vehicle")}
        <div class="grid grid-3">
          {card("droplet","Hydrophobic Protection","Water beads up and rolls off like never before. Mud and road grime simply don't stick — your car stays cleaner longer and washes in a fraction of the time.")}
          {card("shield","Scratch &amp; Swirl Resistance","The hardened ceramic layer dramatically reduces the fine scratches, swirl marks, and micro-abrasions that accumulate over time.")}
          {card("award","UV &amp; Oxidation Protection","San Antonio sun is intense. A ceramic coating creates a UV-blocking layer that significantly slows paint fade and oxidation.")}
          {card("leaf","Chemical Resistance","A chemical-resistant barrier gives you more time to clean bird droppings, tree sap, and acidic contaminants before they etch your paint.")}
          {card("sparkle","Enhanced Gloss &amp; Depth","The coating amplifies your paint's gloss and color depth in a way wax simply cannot match — like it just rolled off a showroom floor.")}
          {card("dollar","Long-Term Value","Lasts 2–7+ years depending on the package, with far less spent on washes, waxing, and products. An investment that pays for itself.")}
        </div>''',
        cls="section section--alt")

    myths = [
        ("Myth: Ceramic coating is scratch-proof.",
         "It significantly improves scratch resistance but doesn't make your vehicle immune. Deep scratches from keys, rocks, or hard debris can still penetrate. Think improved resistance, not absolute protection."),
        ("Myth: You never have to wash your vehicle again.",
         "A coated vehicle is much easier to wash and stays cleaner longer, but it still needs regular washing. What changes is how easy washing becomes and how infrequently you need to do it."),
        ("Myth: Any ceramic product works just as well.",
         "There's a massive difference between consumer kits and professional systems. SiO2 concentration, application process, prep, and cure time all affect performance significantly."),
        ("Myth: Coating can be applied without paint correction.",
         "Ceramic coating magnifies the surface underneath — including defects. Applying over swirls or contamination locks those defects in. Proper prep is non-negotiable for professional results."),
        ("Myth: Ceramic coating is a permanent fix.",
         "Coatings are semi-permanent and long-lasting, but they degrade over time — especially with improper maintenance. High-quality coatings last many years with proper care."),
    ]
    ceramic_myths = section(
        f'''{head("Myths, Debunked", "Ceramic Coating Myths — Debunked")}
        <div style="max-width:820px;margin:0 auto">''' +
        "".join(f'<div class="myth reveal"><div class="m">{m}</div><div class="r"><b>Reality:</b> {r}</div></div>'
                for m, r in myths) + '</div>')

    ceramic_process = section(
        f'''{head("Our Process", "Our Ceramic Coating Process")}
        {steps([
          ("Inspection &amp; Assessment","We inspect your paint under proper lighting to determine its condition and what prep is needed before coating."),
          ("Wash &amp; Decontamination","A full hand wash followed by clay bar decontamination removes bonded contaminants like iron particles, fallout, and road tar."),
          ("Paint Correction (When Required)","Swirl marks, scratches, and defects are corrected by machine polishing — a coating magnifies whatever is underneath it."),
          ("Panel Wipe &amp; IPA Decontamination","The vehicle is wiped with an isopropyl alcohol solution to remove polish oils and ensure a clean surface ready to bond."),
          ("Coating Application","The ceramic coating is applied panel by panel with precise cross-hatch technique, flashed, and leveled before moving on."),
          ("Initial Cure","The coating enters its cure phase. We provide specific aftercare instructions for the first 7–14 days for maximum durability."),
        ])}''',
        cls="section section--panel")

    ceramic_maint = section(
        f'''<div class="split reverse">
          {placeholder("Maintaining a Ceramic-Coated Vehicle","[ Image: pH-neutral hand wash in progress ]")}
          <div class="body reveal">
            <span class="eyebrow">Aftercare</span>
            <h2>Keeping Your Coating Performing</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            {checklist([
              "Wash every 2–4 weeks with pH-neutral soap — no drive-through car washes",
              "Avoid parking under trees or heavy bird activity when possible",
              "Remove bird droppings, sap, and bug splatter promptly",
              "Use a ceramic-safe spray detailer between washes",
              "Consider an annual coating maintenance service",
              "Do not use wax or sealant on top of your ceramic coating",
            ])}
          </div>
        </div>''')

    ceramic_why = section(
        f'''{head("Why Spit Shine", "Why Trust Us With Your Ceramic Coating?",
        "The difference between a great result and a disappointing one comes down almost entirely to the preparation and the person applying it.")}
        <div style="max-width:820px;margin:0 auto">
        {checklist([
          "We use <strong>professional-grade ceramic coating systems</strong> — not auto-parts-store kits",
          "Every coating is applied over a <strong>properly decontaminated and corrected</strong> surface",
          "We <strong>take our time</strong> and don't rush the application or cure process",
          "We provide <strong>detailed aftercare</strong> and stay available for questions after your service",
          "We <strong>stand behind our work</strong> — if something isn't right, we'll make it right",
        ])}
        </div>''',
        cls="section section--alt")

    ceramic_cta = cta_band(
        "Protect Your Vehicle the Right Way. Book Your Ceramic Coating Today.",
        "Slots for ceramic coating services fill up quickly. Get your free quote today and let's talk about "
        "the right coating package for your vehicle and your budget.",
        btn("Get a Free Ceramic Quote", "contact.html", "primary") +
        btn("Call to Discuss Options", f"tel:{PHONE}", "secondary", ico="phone"))

    page("ceramic-coatings.html",
         "Ceramic Coating San Antonio TX | Professional Installation | Spit Shine SA",
         "Professional ceramic coating installation in San Antonio, TX. Spit Shine SA applies top-grade "
         "coatings that protect your paint for years. Mobile service available. Get a free quote!",
         "services.html", ceramic_hero,
         trustbar() + ceramic_what + ceramic_benefits + ceramic_myths +
         ceramic_process + ceramic_maint + ceramic_why + ceramic_cta)

    # ======================================================================
    # PAINT CORRECTION
    # ======================================================================
    pc_hero = hero(
        'Your Paint Isn\'t Ruined. <span class="accent">It Just Needs the Right Expert.</span>',
        sub="Professional paint correction in San Antonio — removing years of swirls, scratches, and "
            "dullness to reveal the vibrant, flawless paint underneath.",
        buttons=btn("Get a Free Paint Correction Quote", "contact.html", "primary") + CALL,
        page_class="hero--page")

    pc_what = section(
        f'''<div class="split">
          {placeholder("Before &amp; After Paint Correction","[ Image: dramatic split before/after — high-impact ]")}
          <div class="body reveal">
            <span class="eyebrow">What Is Paint Correction?</span>
            <h2>Removing Defects at the Microscopic Level</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>Paint correction uses professional dual-action or rotary machine polishers, combined with
            specialized cutting compounds and finishing polishes, to safely remove defects from your
            vehicle's clear coat.</p>
            <p>Most visible defects — swirl marks, fine scratches, water spots, and haze — live in the clear
            coat layer. Correction carefully removes a microscopic amount of clear coat to level the surface
            and eliminate those defects.</p>
            <p>This is not buffing your car with a $30 orbital from the hardware store. It's a skilled,
            time-intensive process that requires training, the right equipment, and years of experience to
            execute correctly and safely.</p>
          </div>
        </div>''')

    pc_defects = section(
        f'''{head("Common Defects", "Paint Defects We Remove")}
        <div class="grid grid-3">
          {card("sparkle","Swirl Marks","The most common defect — circular fine scratches from improper washing and automatic car washes. That spider-web effect in sunlight? Those are swirls.")}
          {card("droplet","Water Spots","Mineral deposits left when water evaporates on your paint. Over time they etch into the clear coat. San Antonio's hard water makes this especially common.")}
          {card("brush","Light &amp; Medium Scratches","Scratches from fingernails, keys, or twigs can often be fully or partially corrected, depending on depth.")}
          {card("award","Oxidation &amp; Paint Fade","UV exposure breaks down the clear coat, leaving paint dull and chalky. Correction removes the damaged outer layer to reveal healthier paint.")}
          {card("shield","Buffer Trails &amp; Holograms","Improper machine polishing leaves its own defects. A skilled specialist can remove these as well.")}
          {card("leaf","Light Etching","Bird droppings, sap, and road chemicals can etch the clear coat. Depending on depth, light etching can be corrected.")}
        </div>''',
        cls="section section--alt")

    pc_process = section(
        f'''{head("Our Process", "Our Multi-Stage Correction Process")}
        {steps([
          ("Wash &amp; Decontamination","The vehicle is hand washed, clay barred, and chemically decontaminated. Polishing over contamination creates additional defects."),
          ("Paint Thickness Assessment","We use a paint depth gauge to measure clear coat thickness at multiple points, ensuring safe margin to work with."),
          ("Test Spot","We perform a test spot on a less-visible panel to find the optimal machine, pad, and compound for your specific paint."),
          ("Machine Polishing","Working panel by panel: cutting stages remove defects, finishing stages refine the surface. Each panel is inspected under focused lighting."),
          ("Final Inspection","A full walk-around under professional inspection lights verifies defect removal and surface quality."),
          ("Panel Wipe","The vehicle is wiped with IPA solution to remove polish oils and prepare for any protective coating, wax, or sealant."),
        ])}''',
        cls="section section--panel")

    pc_expect = section(
        f'''<div class="split reverse">
          {placeholder("Inspecting Paint Under Focused Lighting","[ Image: technician checking gloss under light ]")}
          <div class="body reveal">
            <span class="eyebrow">Honest Expectations</span>
            <h2>What to Realistically Expect</h2>
            <div class="divider-orange" style="margin-bottom:22px"></div>
            <p>We always set honest expectations before we start work.</p>
            {checklist([
              "<strong>One-step correction</strong> removes 60–70% of light defects and significantly improves gloss",
              "<strong>Two-step correction</strong> addresses deeper defects with greater overall improvement",
              "<strong>Full multi-stage correction</strong> can achieve 90–95%+ defect removal — rivaling a fresh respray from a distance",
            ])}
            <p>Some very deep scratches or chips that go through the clear coat into the base coat cannot be
            corrected through polishing — those require touch-up or respray. We'll identify these during our
            inspection and be upfront with you.</p>
          </div>
        </div>''')

    pc_why = section(
        f'''{head("Why It Matters", "Why Professional Paint Correction Matters",
        "Every time a machine polisher removes clear coat, it's a one-way process. Clear coat doesn't grow back.")}
        <div style="max-width:760px;margin:0 auto;text-align:center">
          <p class="lead">If too much clear coat is removed by an inexperienced operator with the wrong setup,
          you're looking at expensive respray costs.</p>
          <p style="margin-top:18px;color:var(--silver)">Our technicians are trained to work within safe
          limits, monitor paint thickness, and use appropriate techniques for each vehicle's specific paint.
          This isn't something to DIY or trust to someone who picked up a buffer last month. Your vehicle's
          paint deserves professional attention.</p>
        </div>''',
        cls="section section--alt")

    pc_cta = cta_band(
        "See What Your Paint Really Looks Like Under All Those Swirls.",
        "Book a paint correction service with Spit Shine San Antonio and prepare to be genuinely surprised at "
        "the transformation. It's one of those services you have to see to believe.",
        btn("Get a Free Correction Quote", "contact.html", "primary") +
        btn("Call to Discuss Your Vehicle", f"tel:{PHONE}", "secondary", ico="phone"))

    page("paint-correction.html",
         "Paint Correction San Antonio TX | Swirl Removal & Paint Restoration | Spit Shine SA",
         "Professional paint correction in San Antonio, TX. Remove swirl marks, scratches, water spots, and "
         "oxidation. Spit Shine SA restores your vehicle's paint to showroom clarity. Get a quote!",
         "services.html", pc_hero,
         trustbar() + pc_what + pc_defects + pc_process + pc_expect + pc_why + pc_cta)

    # ======================================================================
    # REVIEWS
    # ======================================================================
    reviews_hero = hero(
        'Don\'t Take Our Word for It — <span class="accent">Take Theirs.</span>',
        sub="We could tell you all day that we do great work. But the real story is told by the hundreds of "
            "San Antonio vehicle owners who've trusted Spit Shine with their cars, trucks, and SUVs.",
        buttons=BOOK + QUOTE, page_class="hero--page")

    reviews_stats = f'''<section class="section section--tight section--alt"><div class="container">
      <div class="stats reveal">
        <div class="stat"><div class="n">4.9{STAR}</div><div class="l">Average Rating</div></div>
        <div class="stat"><div class="n">200+</div><div class="l">Verified Reviews</div></div>
        <div class="stat"><div class="n">100%</div><div class="l">Mobile Service</div></div>
        <div class="stat"><div class="n">14+</div><div class="l">Areas Served</div></div>
      </div>
      <p class="center" style="margin-top:22px;color:var(--muted);font-size:.85rem">
      Ratings shown are illustrative placeholders — connect your live Google &amp; Facebook reviews widget here for maximum trust and SEO impact.</p>
    </div></section>'''

    review_data = [
        ("I've been getting my Tahoe detailed for years at different places around San Antonio, and Spit Shine is in a different category. My truck looked like it just came off the dealer lot. They even got the stubborn water spots off my windshield that nobody else could touch. Already booked my next appointment.",
         "Marcus T.", "San Antonio · 2021 Chevy Tahoe · Full Detail"),
        ("Hands down the best money I've spent on my truck since buying it. The ceramic coating looks incredible and the water just sheets right off now. I've washed it maybe twice in three months and it still looks better than the day I bought it. Professional, clear, and right on time.",
         "David R.", "Stone Oak · 2023 F-150 · Ceramic Coating"),
        ("I bought a used car that looked fine in the dealership photos but had swirl marks everywhere in sunlight. Spit Shine did a two-step paint correction and I genuinely could not believe the difference. My car looks better than it ever did.",
         "Jennifer M.", "Alamo Heights · 2020 Honda Accord · Two-Step Correction"),
        ("The mobile aspect alone is worth it to me. Two kids and no time to drop my car off anywhere. They came to my house while I worked from home, and my SUV was completely transformed by the time I went outside. My husband didn't even recognize the car.",
         "Sarah K.", "Helotes · 2022 Kia Telluride · Signature Detail"),
        ("I'm very particular about who touches my car. I did my research and they did not disappoint. They took their time, communicated throughout, and the ceramic coating application was flawless. Six months in and it still beads like the first day. The real deal.",
         "Anthony L.", "The Dominion · 2022 BMW M4 · Coating + Correction"),
        ("I was ready to trade in my car because the paint looked so bad. Someone told me to call Spit Shine first. One full correction service and my car looks better than when I bought it. I literally turned down a trade-in offer.",
         "Raquel V.", "Converse · 2018 Toyota Camry · Full Correction"),
        ("Responsive, on time, professional, and the results speak for themselves. They answered all my questions before I booked, explained exactly what would be done, and followed up after. Great experience start to finish.",
         "Michael B.", "New Braunfels · 2021 RAM 1500 · Full Detail"),
        ("First time using a mobile detailing service and I was skeptical it would be as thorough as a shop. I was completely wrong. My car has never been this clean in the 4 years I've owned it. Never using a drive-through car wash again.",
         "Lisa G.", "Universal City · 2019 Hyundai Tucson · Full Spit Shine"),
        ("Trusted Spit Shine with my 1969 Mustang — basically trusting them with my heart. They treated it with absolute care and respect. The paint correction was incredible and the hand wax gave that old-school finish I've chased for years.",
         "Bob H.", "Boerne · 1969 Ford Mustang · Correction + Hand Wax"),
    ]
    reviews_grid = section(
        f'''{head("Customer Reviews", "What San Antonio Is Saying")}
        <div class="grid grid-3">''' +
        "".join(review(t, n, m) for t, n, m in review_data) + "</div>")

    reviews_why = section(
        f'''{head("Why They Come Back", "Why San Antonio Keeps Choosing Spit Shine")}
        <div style="max-width:820px;margin:0 auto">
        {checklist([
          "We consistently <strong>deliver on our promises</strong>",
          "We <strong>communicate clearly and honestly</strong> before, during, and after every service",
          "Our <strong>mobile service</strong> makes professional detailing genuinely convenient",
          "We treat every vehicle — daily driver to weekend exotic — <strong>with the same care</strong>",
          "We <strong>stand behind our work</strong> and always make things right",
        ])}
        </div>''',
        cls="section section--panel")

    reviews_cta = cta_band(
        "Ready to Add Your Review to Our Wall of Fame?",
        "Book your appointment with Spit Shine San Antonio and experience the service that's earning "
        "five-star reviews across greater San Antonio.",
        BOOK + QUOTE)

    page("reviews.html",
         "Customer Reviews | Spit Shine San Antonio Mobile Detailing & Ceramic Coating",
         "See what San Antonio vehicle owners are saying about Spit Shine San Antonio. Real reviews from "
         "real customers who trust us with their cars, trucks, and SUVs.",
         "reviews.html", reviews_hero,
         trustbar() + reviews_stats + reviews_grid + reviews_why + reviews_cta)

    # ======================================================================
    # FAQ
    # ======================================================================
    faq_hero = hero(
        'Everything You Want to Know <span class="accent">Before You Book</span>',
        sub="We believe in being fully transparent with our customers. Here are the most common questions "
            "we get — answered honestly. Don't see yours? Give us a call or send a message.",
        buttons=btn("Call or Text Us", f"tel:{PHONE}", "primary", ico="phone") +
                btn("Send a Message", "contact.html", "secondary"),
        page_class="hero--page")

    faqs = [
        ("Mobile Detailing", [
          ("What exactly is mobile detailing?",
           "Mobile detailing is professional automotive detailing performed at your location — your home, workplace, or anywhere your vehicle is accessible. We bring all the equipment, products, and supplies needed for a complete detail without you having to drop your vehicle off."),
          ("What do you need to perform a mobile detail at my location?",
           "Access to your vehicle and a flat, reasonably level parking surface. Access to a water source and electrical outlet is helpful, but we come equipped with our own water supply and generator for locations where these aren't available. Just let us know your situation when you book."),
          ("How long does a mobile detail take?",
           "It depends on the service and condition of your vehicle. A basic exterior detail might take 1–2 hours. A full interior and exterior detail typically takes 3–5 hours. Paint correction and ceramic coating services can take a full day or span multiple days. We'll give you a specific estimate when you book."),
          ("Can you detail my vehicle in my apartment complex parking lot?",
           "In most cases, yes. We do ask that you check with your complex management about any restrictions. Many complexes are fine with mobile detailing as long as we don't leave water runoff or residue in shared areas."),
          ("What if it rains on the day of my appointment?",
           "Light rain can sometimes be worked around, but significant rain typically requires rescheduling — particularly for ceramic coating and paint correction where a dry environment is critical. We monitor weather closely and will reschedule at no charge due to weather."),
          ("Do I need to be home during the service?",
           "You don't have to be present the entire time, but we ask that someone be available at the beginning to inspect the vehicle and confirm the service, and at the end for a walk-through. Many customers go about their day while we work."),
          ("What types of vehicles do you detail?",
           "We detail all types: sedans, trucks, SUVs, luxury vehicles, exotics, classics, motorcycles, RVs, and boats. If it has paint or interior surfaces, we can detail it. Just let us know what you have."),
        ]),
        ("Ceramic Coatings", [
          ("How long does ceramic coating last?",
           "It varies by product and maintenance. Entry-level professional coatings typically last 2–3 years, mid-grade systems 4–5 years, and premium multi-layer systems 7+ years with proper care. Consumer-grade kits typically last 6–12 months."),
          ("Is ceramic coating worth the investment?",
           "For most owners who care about their paint, absolutely. A quality coating lasts years, dramatically reduces washing time and cost, protects against damage, and enhances appearance and resale value. Over several years, it often pays for itself."),
          ("Can I go through an automatic car wash after ceramic coating?",
           "We strongly recommend against brush-type washes — they're a leading cause of swirl marks. Touchless washes are better, but the best approach is a regular hand wash with pH-neutral soap. Your coating will last longer and look better."),
          ("How do I care for my ceramic coating?",
           "Wash every 2–4 weeks with pH-neutral soap and a clean microfiber mitt, use a ceramic-safe spray detailer between washes, avoid parking under trees, and remove droppings and sap promptly. We provide a complete aftercare guide after every installation."),
          ("Does my car need paint correction before ceramic coating?",
           "In most cases some level of correction is recommended. A coating magnifies whatever is underneath it — swirls and haze become more visible after coating. We'll assess your paint and recommend the right prep for your situation."),
          ("How long does the coating need to cure before I can drive?",
           "Initial cure typically takes 24–48 hours, during which we ask you to keep the vehicle dry. The coating continues to fully cure over the following 1–2 weeks. We'll give you specific instructions based on the system and weather."),
        ]),
        ("Paint Correction", [
          ("Will paint correction make my car's paint look perfect?",
           "Correction dramatically improves your paint, but the level depends on starting condition and stage performed. One-step significantly improves light defects; two-step or full multi-stage can achieve near-perfect results. Deep scratches through the clear coat can't be corrected by polishing alone."),
          ("Can paint correction damage my vehicle's paint?",
           "In untrained hands with improper equipment, yes. That's why choosing a professional matters. We use paint thickness gauges to monitor clear coat depth throughout, ensuring we work safely within appropriate limits."),
          ("How do I know what stage of correction my car needs?",
           "That's what our inspection is for. We assess your paint under specialized lighting, measure thickness, perform a test spot if needed, and give you a clear recommendation with an explanation of what each stage achieves."),
          ("How long does paint correction take?",
           "A single-stage correction typically takes 4–6 hours, a two-stage 6–8 hours or a full day, and a full multi-stage correction on a heavily defected vehicle 1–2 full days. We don't rush — thorough panel-by-panel work takes time and it shows."),
        ]),
        ("Paint Touch-Up", [
          ("Will paint touch-up make chips invisible?",
           "We'll be completely honest: touch-up work is not invisible. Under close inspection in certain lighting it will be visible. However, it significantly reduces the visual impact and — most importantly — seals exposed metal to prevent rust. The goal is to make damage much less noticeable and protect your vehicle."),
          ("Can all paint chips be touched up?",
           "Most small chips and rock damage can be addressed. Very large chips, deep scratches, or extensive damage typically require professional bodywork and repainting. We'll assess your specific damage and give an honest recommendation."),
        ]),
        ("Pricing &amp; Scheduling", [
          ("How much does mobile detailing cost?",
           "Pricing depends on the service, vehicle size, and condition. We provide free, transparent quotes before every service — no surprises. Contact us with your vehicle details and the service you want for a specific price."),
          ("Do you offer packages or bundle discounts?",
           "Yes. Combining services like paint correction and ceramic coating is common, and we offer combined pricing. Contact us to discuss your vehicle's needs and we'll build the right package at the right price."),
          ("How far in advance do I need to book?",
           "For standard details, we can often accommodate bookings within a few days. For ceramic coating and paint correction, we recommend booking 1–2 weeks in advance as these slots fill quickly. We'll always do our best for urgent requests."),
          ("What days and hours do you work?",
           "We work Monday through Saturday and can typically accommodate early morning and late afternoon appointments. Contact us directly for current availability — our schedule changes weekly."),
          ("What payment methods do you accept?",
           "We accept cash, all major credit and debit cards, and digital payments including Venmo, Zelle, and Apple Pay. Payment is typically collected after service completion unless other arrangements are made for large projects."),
        ]),
    ]

    faq_sections = ""
    schema_faq_items = []
    for cat, items in faqs:
        faq_sections += f'<div class="faq-cat reveal">{cat}</div>'
        for q, a in items:
            faq_sections += (f'<div class="faq-item reveal"><button class="faq-q" type="button">{q}</button>'
                             f'<div class="faq-a"><div class="faq-a-inner">{a}</div></div></div>')
            schema_faq_items.append({
                "@type": "Question", "name": q.replace("&amp;", "&"),
                "acceptedAnswer": {"@type": "Answer", "text": a.replace("&amp;", "&")}})

    faq_body = f'<section class="section"><div class="container"><div class="faq">{faq_sections}</div></div></section>'
    faq_cta = cta_band(
        "Still Have Questions?",
        "We love talking about cars and detailing. Reach out anytime and we'll get back to you quickly.",
        btn("Call or Text Us", f"tel:{PHONE}", "primary", ico="phone") +
        btn("Send a Message", "contact.html", "secondary") + BOOK)

    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": schema_faq_items}

    page("faq.html",
         "FAQ | Mobile Detailing, Ceramic Coating & Paint Correction | Spit Shine SA",
         "Get answers to common questions about mobile detailing, ceramic coatings, paint correction, and "
         "booking with Spit Shine San Antonio. Find out what to expect.",
         "faq.html", faq_hero,
         trustbar() + faq_body + faq_cta, extra_schema=faq_schema)

    # ======================================================================
    # CONTACT
    # ======================================================================
    contact_hero = hero(
        'Let\'s Talk About <span class="accent">Your Vehicle.</span>',
        sub="Getting in touch is the first step toward a vehicle that turns heads everywhere you go. We "
            "respond quickly, we're honest about pricing, and we'll make sure you know exactly what to "
            "expect before we schedule anything.",
        buttons=btn("Call or Text Now", f"tel:{PHONE}", "primary", ico="phone"),
        page_class="hero--page")

    service_checks = "".join(
        f'<label><input type="checkbox" name="services" value="{s}"> {s}</label>'
        for s in ["Mobile Detailing", "Ceramic Coating", "Paint Correction",
                  "Paint Touch-Up", "Maintenance Plan", "Not Sure — Help Me Decide"])

    contact_form = f'''
      <div class="form-wrap reveal">
        <div class="form-success">Thanks — your message is on its way! We aim to respond to all
        inquiries within one business hour during business hours.</div>
        <form data-spitshine data-endpoint="{CONFIG['form_endpoint']}" novalidate>
          <div class="form-grid">
            <div class="field"><label>Full Name <span class="req">*</span></label><input type="text" name="name" required placeholder="Your name"></div>
            <div class="field"><label>Phone Number <span class="req">*</span></label><input type="tel" name="phone" required placeholder="(210) 555-0123"></div>
            <div class="field"><label>Email Address</label><input type="email" name="email" placeholder="you@email.com"></div>
            <div class="field"><label>Vehicle Year / Make / Model</label><input type="text" name="vehicle" placeholder="e.g. 2021 Ford F-150"></div>
            <div class="field full"><label>Services You're Interested In</label>
              <div class="checkgroup">{service_checks}</div>
            </div>
            <div class="field full"><label>Vehicle Condition / Notes</label>
              <textarea name="notes" placeholder="Tell us about your vehicle, any areas of concern, and what you'd like to accomplish."></textarea></div>
            <div class="field"><label>Preferred Contact Method</label>
              <select name="contact_method"><option>Call</option><option>Text</option><option>Email</option></select></div>
            <div class="field"><label>Best Time to Reach You</label>
              <select name="best_time"><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div>
          </div>
          <div style="margin-top:22px">{submit_btn("Send My Message", "mail")}</div>
          <p class="form-note">No live form backend is connected yet. Add your Formspree (or CRM) endpoint in
          <code>build.py → CONFIG["form_endpoint"]</code> to start receiving submissions by email.</p>
        </form>
      </div>'''

    contact_main = f'''<section class="section"><div class="container">
      <div class="split">
        <div class="reveal">
          <span class="eyebrow">Send Us a Message</span>
          <h2>Request Your Free Quote</h2>
          <div class="divider-orange" style="margin:18px 0 22px"></div>
          <p style="color:var(--silver);margin-bottom:26px">Fill out the form and tell us about your vehicle
          and what you're looking for. The more info you share — vehicle type, year, services of interest —
          the more helpful we can be when we respond.</p>
          {contact_form}
        </div>
        <div class="reveal">
          <div class="grid" style="gap:18px">
            <div class="info-card"><div class="icon">{icon("phone")}</div>
              <h3>Call or Text</h3>
              <p>Sometimes you just want to talk. We aim to respond within 1 business hour.</p>
              <a href="tel:{PHONE}" style="color:var(--orange-bright);font-size:1.1rem;margin-top:8px">{PH_D}</a></div>
            <div class="info-card"><div class="icon">{icon("mail")}</div>
              <h3>Email Us</h3>
              <p>For detailed inquiries or photo sharing.</p>
              <a href="mailto:{CONFIG['email']}" style="color:var(--orange-bright);margin-top:8px">{CONFIG['email']}</a></div>
            <div class="info-card"><div class="icon">{icon("clock")}</div>
              <h3>Business Hours</h3>
              <p>{CONFIG['hours']}<br><span style="color:var(--muted);font-size:.85rem">Hours may vary for large projects.</span></p></div>
            <div class="info-card"><div class="icon">{icon("pin")}</div>
              <h3>Where We Work</h3>
              <p>We're a mobile operation — we come to you throughout all of San Antonio and the surrounding communities.</p></div>
          </div>
        </div>
      </div>
    </div></section>'''

    contact_area = section(
        f'''{head("Service Area", "We Come to You — Throughout Greater San Antonio")}
        {area_chips()}
        <p class="center" style="margin-top:24px;color:var(--silver)">Not sure if we cover your location?
        Just ask — we'll let you know.</p>
        <div style="margin-top:30px">{placeholder("Google Map — San Antonio Service Area","[ Embed: interactive Google Map of your service radius ]")}</div>''',
        cls="section section--alt")

    contact_cta = cta_band(
        "No Commitment Required — Just Reach Out.",
        "A free quote costs nothing, and we promise we won't pressure you into anything. Just tell us about "
        "your vehicle and we'll give you an honest recommendation and a transparent price.",
        btn("Call or Text Us Now", f"tel:{PHONE}", "primary", ico="phone") + BOOK)

    page("contact.html",
         "Contact Spit Shine San Antonio | Free Quote for Mobile Detailing & Ceramic Coating",
         "Contact Spit Shine San Antonio to request a free quote or schedule your mobile detailing, ceramic "
         "coating, or paint correction service. We respond quickly!",
         "contact.html", contact_hero,
         trustbar() + contact_main + contact_area + contact_cta)

    # ======================================================================
    # BOOK
    # ======================================================================
    book_hero = hero(
        'Your Vehicle\'s Best Day Is <span class="accent">One Appointment Away.</span>',
        sub="You've been thinking about it. Now it's time. Book your appointment with Spit Shine San Antonio "
            "and let's make it happen.",
        buttons=btn("Check Availability", "#book-form", "primary", ico="calendar") + CALL,
        page_class="hero--page")

    book_scarcity = f'''<section class="section section--tight section--alt"><div class="container reveal" style="text-align:center">
      <p class="eyebrow" style="color:var(--orange-bright)">{icon("clock")} Limited Availability This Week</p>
      <p class="lead" style="max-width:720px;margin:8px auto 0">Our schedule books up quickly, especially on
      weekends — and ceramic coating slots fill fast. Secure your appointment now.</p>
    </div></section>'''

    book_steps = section(
        f'''{head("How Booking Works", "Five Simple Steps")}
        {steps([
          ("Choose Your Service","Select the service (or combination) that best fits your vehicle's needs. Not sure? Pick the closest option and note it — we'll help you confirm."),
          ("Pick Your Date &amp; Time","Choose your preferred appointment from our available schedule. Morning, midday, and afternoon slots, Monday through Saturday."),
          ("Tell Us About Your Vehicle","Enter your vehicle's year, make, model, and color, plus any notes about concerns or areas to focus on."),
          ("Confirm and Lock It In","Review your details and confirm. You'll get an immediate confirmation, and we'll follow up with a call or text."),
          ("Get Ready for the Transformation","We'll show up at the agreed time, fully equipped, and ready to make your vehicle look its absolute best."),
        ])}''')

    book_form = f'''<section class="section section--panel" id="book-form"><div class="container">
      {head("Pick Your Time", "Book Your Appointment Online",
            "Choose a slot that works for you below and get instant confirmation. "
            "Prefer to talk first? Call or text us anytime.", center=True)}
      <div style="max-width:940px;margin:0 auto">
        <div class="calendly-inline-widget reveal" data-url="{CONFIG['calendly_url']}"
             style="min-width:320px;height:720px;border-radius:var(--radius);overflow:hidden;border:1px solid var(--line);background:#000;"></div>
        <p class="center" style="margin-top:22px;color:var(--silver)">Not seeing the scheduler?
          <a href="{CONFIG['calendly_url']}" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
        <div class="btn-row center" style="justify-content:center;margin-top:18px">
          {btn("Call or Text " + PH_D, "tel:" + PHONE, "secondary", ico="phone")}
          {btn("Get a Free Quote First", "contact.html", "ghost")}
        </div>
      </div>
    </div></section>'''

    book_expect = section(
        f'''{head("On Service Day", "What to Expect")}
        <div class="grid grid-3">
          {card("clock","We Arrive On Time","Or we'll contact you if there are any unexpected delays. We do a quick walk-around with you before we start.")}
          {card("shield","Professional &amp; Tidy","We work efficiently and professionally — no blasting music, no leaving messes.")}
          {card("sparkle","Full Walkthrough","When we're done, we walk you through the results and answer any questions about maintaining them.")}
          {card("heart","Pay When Satisfied","Payment is collected after you've inspected the work and are completely satisfied.")}
          {card("car","Easy Prep","Remove personal items from the cabin for interior details, and park where we can access all sides of the vehicle.")}
          {card("calendar","Flexible Rescheduling","Life happens. We just ask for 24 hours' notice when possible so we can open your slot for another customer.")}
        </div>''',
        cls="section section--alt")

    book_cta = cta_band(
        "Spots Fill Fast — Don't Wait.",
        "Your vehicle is ready for its close-up. Secure your appointment now and guarantee your spot with "
        "San Antonio's mobile detailing specialists.",
        btn("Book My Appointment Now", "#book-form", "primary", ico="calendar") +
        btn("Get a Free Quote First", "contact.html", "secondary") + CALL)

    page("book.html",
         "Book Your Mobile Detailing Appointment | Spit Shine San Antonio",
         "Ready to book? Schedule your mobile detailing, ceramic coating, or paint correction appointment "
         "with Spit Shine San Antonio. Fast booking, flexible scheduling. Book now!",
         "book.html", book_hero,
         trustbar() + book_scarcity + book_steps + book_form + book_expect + book_cta)
