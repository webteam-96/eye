# Product Requirements Document
## Dr. Anchal Gupta — Senior Eye Surgeon | Personal & Professional Website

**Version:** 2.0 (supersedes v1.0)
**Date:** 16 September 2026
**Prepared by:** Kaizen Infotech Solutions Pvt. Ltd.
**Status:** For client review

**Changes in v2.0:** rebuilt on the client's profile deck and brand logo. Direction reset to a **surgeon/doctor website** (the Foundation is a chapter of her story, not the frame). Palette redrawn from the Netram logo. Real credentials, projects, awards, media and contact details inserted. Asset sources identified.

---

## 1. Project Overview

A premium, custom-built 5-page website positioning **Dr. Anchal Gupta** as a senior cornea and refractive eye surgeon — her clinical authority first, her institution second, her philanthropy third. The site converts the existing 47-page profile deck into a living, scrollable web presence.

The story it tells: a surgeon from Varanasi who trained at KGMU and Maulana Azad, walked away from Max and Fortis in 2013, and built Netram — a super-speciality eye care centre and an all-India foundation now reaching 24 states.

**Deliverable:** 5-page static website — custom HTML5, CSS3, vanilla JavaScript — responsive, animated, SEO-structured, deployed live with SSL.

---

## 2. Verified Profile Facts (source of truth)

Extracted from the client's profile deck. All site copy is to be built from these; nothing invented.

**Identity**
- Dr. Anchal Gupta — Senior Eye Surgeon
- MBBS, MS (Ophthalmology), FVEIRC, Sr. Residency MAMC
- MS Ophthalmology, King George's Medical University, Lucknow — 2009
- Senior Residency, Maulana Azad Medical College, Delhi
- Practising cornea and refractive surgeon since 2012
- Ex-specialist ophthalmologist, Max and Fortis (Gurgaon)
- Founder, Netram Eye Foundation (est. 2013 / society since 2013; camps since 2012)
- Motto: **"Sight to All"** · Vision: **"Good Health for All"**
- Public handle: **@ankhonkidoctor** — usable as a brand device on the site

**Netram (institution)**
- Founded 2013 at C.R. Park, New Delhi — began as a two-room basement clinic
- Now occupies three floors, 50+ staff, panel of 6 super-specialist doctors
- Treats cataract, glaucoma, retinal disorders, corneal disease; general exams to complex surgery
- Reach: 24 states including Delhi & NCR, Haryana, Punjab, Rajasthan, UP, Uttarakhand, Himachal, Bihar, Jharkhand, West Bengal, Assam, Odisha, MP, Maharashtra, Gujarat, Andhra Pradesh, Tamil Nadu

**Foundation projects**

| Project | Description |
|---|---|
| Project Roshini (with IGL) | 1 lakh+ school children screened across Delhi, Haryana, Rajasthan; refractive error, anaemia and mental-health awareness; ~28,000 spectacles distributed |
| Eye Mela | Eye and general health camps in difficult terrain — spectacles, medicines, cataract surgery aid. **5,00,000 beneficiaries, 24 states** |
| Chashma Bus | Mobile community eye care across Delhi NCR — glasses, screening, referral of complex cases |
| Nayan Hans | Doorstep cataract screening and advanced phaco surgery, free of cost |
| Mission 6/6 (Delhi Police) | Eye check-up camps at police stations, free spectacles for personnel |
| I Am 6/6 | Structured programme for truck and commercial drivers at depots — road-safety-led vision correction |
| Transgender Medical Camp | India's first mental health helpline for transgender persons during Covid, with Ministry of Social Justice & Empowerment |
| Oxygen Sewa | Free oxygen concentrators with doorstep delivery and pickup during the pandemic |
| Netram Empower | (Description to be supplied by client) |
| **Eye Maitri** | **Corporate Eye Wellness Program — new; B2B/CSR offering, needs its own block and enquiry route** |

**Awards & recognition** (reverse chronological, as supplied)
Forbes India 2026 — Business Leaders Defining Modern Success · TEDx Speaker 2026, "The Power of Sight" · Speaker, CII Healthcare Summit 2025 · WomanEra July 2025 cover feature · Future Female Forward Award (CNBC, Cognizant, HSBC) · 30 Women Driving Change in Healthcare, Voice of Healthcare 2025 · Outlook Money cover feature 2025 · Top 10 Influential Women of the Year 2024, The Indian Alert · BW Healthcare 40 Under 40, 2022 · Medlife 5 Most Influential Women in Healthcare, 2022 · Medgate Women Leaders in Healthcare, 2021 · Antyodaya Recognition, Ministry of Culture, 2020 · Woman of Social Change, WOS 2019 · India CSR Leadership Awards 2019 (Project Roshini — Best Project in Community Health) · Uddhav Manavsewa Samman 2019 · Women Excellence Award, YWCA 2018 · Youth India Award 2017 · Mahatma Gandhi Samman, Bangkok 2017 · Swastha Sewa Samman 2016 · Pride of India Award, CIPS 2016 · National Healthcare Excellence Award 2016 · Pride of India Award 2015 (conferred by Sheila Dikshit) · Rajiv Gandhi Rashtriya Ekta Samman 2015 & 2014 · RK HIV AIDS Foundation Achievers Award 2013 · Medgate Healthcare Excellence Award 2012
Also: **Gold Medal for the highest number of IPCL surgeries in the North Region**; Chair, Sexual Harassment Commission, STAIRS Foundation (2024).

**Academic standing**
Invited guest speaker and faculty at national and international conferences; has launched multiple new drug formulations in India for national and international pharmaceutical companies.

**Media coverage** (link out with logos)
YourStory · Femina · Amar Ujala · The Better India · Business Standard · Grihshobha

**Contact**
E-98, Greater Kailash-2, Opp. Gurudwara, New Delhi 110048
011-41676655 · 9212646655 · ngonetram@gmail.com · www.netrameyefoundation.com
Instagram: @ankhonkidoctor · LinkedIn: /in/anchal-gupta-6553b516

---

## 3. Objectives

| # | Objective | Measure |
|---|---|---|
| 1 | Establish surgical authority immediately | Credentials, years in practice and specialty visible above the fold |
| 2 | Make contact effortless | WhatsApp, call and enquiry reachable in one tap from any screen |
| 3 | Convert institutional recognition into trust | Awards, media logos and conference standing presented as proof, not a list |
| 4 | Open a corporate/CSR channel | Eye Maitri and Foundation partnership enquiries routed separately from patient enquiries |
| 5 | Rank for name and specialty searches | Semantic HTML, Physician schema, optimised meta and alt text |
| 6 | Load fast on Indian mobile networks | Lighthouse mobile ≥ 90; LCP under 2.5s on 4G |

---

## 4. Audience & Priority

1. **Patients and families** (primary) — referred, searching the name; need reassurance, specialty, location, a phone number.
2. **Referring doctors and institutions** — scanning training, fellowships, surgical volume, publications.
3. **Corporate CSR heads and partners** — Eye Maitri, Project Roshini-style partnerships.
4. **Media, conference organisers, award bodies** — bio, photographs, speaking history.
5. **Donors and volunteers** — Foundation page.

---

## 5. Design Direction

### 5.1 Reference interpretation

**`medic-128.webflow.io` — the base.** Clinical layout discipline, generous whitespace, soft rounded cards, orderly credential and service grids, calm micro-interactions. This governs the global UI: header, buttons, forms, cards, footer, and the About/Expertise/Contact pages.

**`25.saveachildsheart.org` — the storytelling layer.** Scroll-driven narrative, large editorial typography, animated impact counters, full-bleed photography, section-to-section tonal shifts. This governs the Home scroll journey, the professional timeline, and the Foundation page.

**`netrameyefoundation.com` — the visual source.** Per client correction, photography, imagery and visual references are drawn from the existing Netram website wherever suitable, so the new site stays recognisably within the same brand world.

> The design is doctor-first. Netram's identity supports Dr. Gupta's; it does not replace it.

### 5.2 Brand palette (drawn from the Netram logo)

The logo is an olive-green stylised eye with radiating lashes, a solid black iris, Devanagari **नेत्रम्** and "EYE FOUNDATION" set in black. The palette follows it rather than the generic medical blue proposed in v1.

| Role | Value | Use |
|---|---|---|
| Brand olive (primary) | `#5C6B3C` | Headings accents, buttons, icons, logo lockup |
| Deep moss | `#3A4526` | Header/footer ground, hover states |
| Ink black | `#141414` | Body copy, iris motif, display headings |
| Warm paper | `#F6F4EC` | Alternate section backgrounds |
| Clinical white | `#FFFFFF` | Base surface |
| Support sage | `#9CA97B` | Dividers, muted accents, stat glyphs |
| Signal amber | `#D99A2B` | Foundation/donate CTAs only — used sparingly |

Clinical pages run white and paper; the Foundation page leans deeper olive with amber CTAs to mark the tonal shift.

### 5.3 Typography

- **Display/headings:** a refined high-contrast serif — *Fraunces*, *Instrument Serif* or *Playfair Display*. Carries the editorial weight of the Save a Child's Heart reference.
- **Body/UI:** **Satoshi** — already the typeface of the client's profile deck, so it keeps the web and print identity aligned. Fallback *Inter*.
- Devanagari support required for **नेत्रम्** — pair with *Mukta* or *Noto Sans Devanagari*.
- Scale: H1 `clamp(2.5rem, 5vw, 4.5rem)`, H2 `clamp(2rem, 3.5vw, 3rem)`, body 17–18px, line-height 1.7.
- Self-hosted WOFF2, `font-display: swap`, max two Latin families and four weights.

### 5.4 Art direction

- Real photography only — Dr. Gupta in OT and consultation, camp and field work, award stages, the Chashma Bus. No stock doctors.
- The iris/eye motif from the logo is used as a recurring graphic device: section dividers, counter glyphs, the scroll cue, the loader.
- Layout: 1280px container, 12-column grid, 120–160px desktop section padding (64–80px mobile).
- Negative space is a feature; nothing crowded.

---

## 6. Sitemap & Page Specifications

### 6.1 Home — the scroll narrative

1. **Hero** (full height) — portrait, name, "Senior Eye Surgeon · Cornea & Refractive", credential line (MBBS, MS, FVEIRC), motto *"Sight to All"*. CTAs: **Book a Consultation** and **WhatsApp**. Iris-motif scroll cue.
2. **Introduction** — 2–3 sentences on her practice and the KGMU → MAMC → Max/Fortis → Netram arc. "Read full profile →".
3. **Impact bar** — animated counters: years in practice (since 2012), states reached (24), children screened (1 lakh+), Eye Mela beneficiaries (5,00,000), spectacles distributed (28,000). Client to confirm surgical-volume figure before it is displayed.
4. **Areas of expertise** — cards: Cornea & Refractive Surgery, Cataract & Phaco, Glaucoma, Retinal Disorders, Comprehensive Eye Examination, Paediatric/Refractive Error. Link to Expertise page.
5. **Netram — the institution** — two-room basement to three floors, 50+ staff, 6 super-specialists. Image-led split layout.
6. **Recognition strip** — Forbes India 2026, TEDx 2026, CII 2025, BW 40 Under 40, Outlook Money — as a marquee of five headline honours, with "All awards →".
7. **Foundation teaser** — full-bleed camp photograph, warm tone shift, project names as a ticker, "Explore our work →".
8. **Media coverage** — publication logos (YourStory, Femina, Amar Ujala, The Better India, Business Standard, Grihshobha) linking out.
9. **Contact band** — map, Greater Kailash-2 address, phone numbers, WhatsApp, condensed enquiry form.

### 6.2 About Dr. Anchal Gupta

- Hero — portrait, name, descriptor.
- **The long biography** — editorial two-column, built from the deck: Varanasi origins, KGMU 2009, MAMC senior residency, cornea and refractive practice from 2012, the 2013 decision to leave Max and Fortis, founding Netram.
- **Pull-quote** — *"Good Health for All"* in large display type.
- **Qualifications** — MBBS · MS Ophthalmology (KGMU, 2009) · FVEIRC · Sr. Residency, MAMC · Specialist, Cornea and Refractive Services.
- **Philosophy of care** — "Sight to All" block, quality care regardless of ability to pay.
- **Netram's story** — basement clinic → three floors, with the reach map.
- **Gallery strip** — clinic, OT, team.
- CTA band.

### 6.3 Expertise / Professional Journey

Centrepiece page. Scroll-animated.

- Hero.
- **Specialties** — accordion grid; each opens to the procedures covered (cornea, refractive, phaco cataract/IPCL, glaucoma, retina, general).
- **Career timeline** — vertical, progress line draws on scroll: 2009 MS KGMU → MAMC senior residency → 2012 practising cornea surgeon → Max/Fortis Gurgaon → 2013 Netram founded, C.R. Park → expansion to three floors → national reach across 24 states → 2026 Forbes India and TEDx.
- **Surgical distinction** — Gold Medal, highest number of IPCL surgeries in the North Region, given a dedicated highlight card.
- **Academics, conferences & faculty** — invited speaker and faculty at national and international conferences; drug formulation launches for national and international pharmaceutical companies; CII Healthcare Summit 2025; TEDx 2026.
- **Awards & accolades** — full list from §2, grouped by year, card grid with year badges; "Show all" expansion so the page stays scannable.
- **Leadership positions** — Chair, Sexual Harassment Commission, STAIRS Foundation (2024).
- **Media** — coverage cards with publication, headline and outbound link.
- CTA band.

### 6.4 Netram Eye Foundation & Social Impact

Warmest page; deepest olive; amber CTAs.

- Cinematic hero — full-bleed field photograph, *"Sight to All"*, Netram logo lockup.
- **Origin** — society since 2013, camps since 2012, the mission of care regardless of ability to pay.
- **Impact counters** — 24 states · 5,00,000 Eye Mela beneficiaries · 1 lakh+ children screened · 28,000 spectacles · 50+ staff.
- **Reach map** — interactive or illustrated India map with the states listed in §2; hover reveals state names. Rebuilt as SVG from the deck's map slide.
- **Projects grid** — one card per project from §2 (Roshini, Eye Mela, Chashma Bus, Nayan Hans, Mission 6/6, I Am 6/6, Transgender Medical Camp, Oxygen Sewa, Netram Empower), each with image, description and its own detail modal or anchor section.
- **Eye Maitri — Corporate Eye Wellness** — dedicated block above the fold of the "Get Involved" area: what the programme covers, who it is for, and a **Corporate Enquiry** CTA routing to a separate form subject.
- **Field gallery** — masonry, lightbox, 15–25 photographs from the shared Drive folders.
- **Partners** — logo wall (IGL, Delhi Police, Ministry of Social Justice & Empowerment, and the partner logos on the deck's two "Our Partners" slides — client to supply clean files).
- **Get involved** — Donate / Volunteer / Partner (CSR), three routes, three CTAs.
- Foundation contact strip.

### 6.5 Contact

- Short hero.
- **Two columns:** enquiry form (Name, Phone, Email, **Enquiry type** — Patient appointment / Corporate Eye Maitri / Foundation partnership / Media & speaking / Other — Message, consent checkbox) left; contact details, clinic timings, WhatsApp, call and social icons right.
- **Google Map** — E-98 Greater Kailash-2, lazy-loaded on interaction, "Get Directions" button.
- Secondary location — the Netram centre at C.R. Park, if the client wants it listed with its own pin and timings.
- **FAQ accordion** — appointment process, what to bring, timings, emergency contact, whether camps are open to walk-ins.

---

## 7. Global Components

| Component | Specification |
|---|---|
| **Header** | Transparent over hero, solid white with shadow on scroll. Netram logo left, nav right, "Book Appointment" pill CTA. Mobile: hamburger → full-screen overlay, staggered links. |
| **Footer** | Four columns — short bio, quick links, contact, social. Motto line, copyright, Kaizen credit. |
| **Floating actions** | Persistent WhatsApp button (bottom-right) with pre-filled message; call button on mobile. Enters after 2s, never covers content. |
| **Enquiry form** | Client-side validation, honeypot spam guard, inline success/error, no reload. Routes by enquiry type to the right recipient. |
| **Lightbox** | Keyboard-navigable, swipe on touch, lazy-loaded thumbnails. |
| **Counter block** | Reusable; counts up once on first view. |
| **CTA band** | Reusable full-width block, heading + sub-line + dual CTAs. |

---

## 8. Animation & Interaction

Motion language: **calm, surgical, never bouncy.** Easing `cubic-bezier(0.22, 1, 0.36, 1)`, 400–800ms.

- Scroll reveals — fade-and-rise 24–40px, staggered 80–120ms within a group (IntersectionObserver).
- Hero entrance — sequenced: image, name, credentials, CTAs.
- Line-by-line mask-and-slide reveal on major section headings.
- Counters animate once on view.
- Gentle parallax (max 12%) on full-bleed image bands only.
- Timeline progress line draws on scroll; nodes activate in sequence.
- Reach map: states illuminate progressively as the section enters view.
- Hover: cards lift 4px with softened shadow; buttons shift ground with an arrow nudge; images scale 1.03 inside an overflow-hidden frame.
- Iris-motif loader on first paint (under 800ms, skippable).
- All motion suppressed under `prefers-reduced-motion: reduce`.

**Implementation:** GSAP + ScrollTrigger (CDN) with Lenis for smooth scroll; or a zero-dependency IntersectionObserver + CSS layer if the performance budget demands it. Decided at kickoff.

---

## 9. Technical Specification

- **Markup:** semantic HTML5, single `<h1>` per page, logical heading order.
- **Styling:** custom CSS3 with custom properties for tokens, Flexbox and Grid, `clamp()` fluid type, mobile-first queries.
- **Scripting:** vanilla ES6, modular, deferred. No jQuery.
- **Breakpoints:** 360 / 480 / 768 / 1024 / 1280 / 1440+.
- **Browsers:** latest two of Chrome, Safari, Firefox, Edge; iOS Safari 15+; Chrome Android.
- **Assets:** WebP with JPEG fallback, `srcset` sizing, `loading="lazy"` below fold, inlined SVG icons.
- **Structure:** `/index.html`, `/about.html`, `/expertise.html`, `/foundation.html`, `/contact.html`, `/assets/{css,js,img,fonts}`.

---

## 10. Integrations

| Integration | Detail |
|---|---|
| WhatsApp | `wa.me/919212646655` deep link, pre-filled message; floating button + inline CTAs |
| Click-to-call | `tel:` on 011-41676655 and 9212646655 |
| Enquiry form | PHP mail handler or Formspree/Web3Forms per hosting capability; notification to ngonetram@gmail.com (or a dedicated address); routed by enquiry type |
| Google Maps | Embedded, interaction-deferred, E-98 Greater Kailash-2 pin |
| Social | Instagram @ankhonkidoctor, LinkedIn, plus Facebook/YouTube/X if active — header overlay, footer, Contact |
| Cross-link | netrameyefoundation.com linked from the Foundation page and footer |
| Analytics | GA4 + Search Console verification |

---

## 11. SEO

- Unique `<title>` (≤ 60 chars) and meta description (≤ 155 chars) per page.
- Open Graph and Twitter cards with a designed share image.
- **JSON-LD:** `Physician` + `Person` on About (name, degrees, specialty, affiliation, awards), `MedicalClinic`/`LocalBusiness` with address and hours on Contact, `NGO` on Foundation.
- Descriptive alt text on every image.
- Clean URLs, canonicals, `robots.txt`, `sitemap.xml`.
- Target queries: "Dr Anchal Gupta", "ankhon ki doctor", "cornea specialist Delhi", "refractive surgeon Greater Kailash", "eye surgeon CR Park", "Netram Eye Foundation", plus procedure terms (cataract, phaco, IPCL, glaucoma).

---

## 12. Performance & Accessibility

- Lighthouse: Performance ≥ 90 (mobile), Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95.
- Page weight under 1.5MB first load; hero image under 250KB. Source photographs are large (5MB+ JPEGs in the shared Drive) — all require compression and resizing before use.
- Critical CSS inlined; non-critical CSS and all JS deferred.
- WCAG 2.1 AA — 4.5:1 contrast (olive on white to be checked and darkened if it fails), visible focus states, full keyboard navigation, ARIA labels on icon-only controls, correctly associated form labels.

---

## 13. Hosting, SSL & Deployment

- Deploy to client hosting (or a Kaizen-provisioned plan) via SFTP or Git.
- DNS configuration and domain pointing; decision needed on domain (see §16).
- SSL installation, forced HTTPS, `www` canonicalisation.
- Post-launch: Search Console submission, sitemap ping, form delivery test, cross-device QA, 404 page.
- Handover: source files, credentials document, short editing guide.

---

## 14. Asset Status

**Received**
- Netram Eye Foundation logo (PNG, transparent) — olive eye mark + Devanagari wordmark + "EYE FOUNDATION". Vector (AI/SVG/EPS) still needed for crisp scaling.
- 47-page profile deck (Canva PDF) — the content source for all pages. Embedded images are extractable at print resolution and usable as a fallback where better originals are missing.
- Instagram and LinkedIn profile URLs.
- Eye Maitri programme link.

**Shared Drive folders — status**
- Folder 1 (`1IsXAT…`) — currently contains a single high-resolution portrait, `_B7A0292.JPG` (5.4MB). More expected.
- Folder 2 (`1x2ZcJ…`) — four dated subfolders (25.03.2025, 15.05.2025, 22.09.2025, 23.10.2025), apparently event/camp shoots. Contents not yet readable from our side — access needs to be opened or the files re-shared.

**Still required from client**
1. Vector logo files.
2. 3+ professional portraits, including one vertical hero frame.
3. OT, consultation and clinic photography.
4. Project-wise field photography — ideally foldered by project name rather than by date.
5. Clean partner logos (IGL, Delhi Police, Ministry of Social Justice & Empowerment and the rest of the partner wall).
6. Award and press photographs at usable resolution.
7. Eye Maitri programme details and Netram Empower description.
8. Confirmed surgical volume and any patient-count figures to be published.
9. Clinic timings; confirmation of which addresses go on the site.
10. Dedicated enquiry email address; WhatsApp business number confirmation.
11. Domain and hosting credentials.

---

## 15. Phases & Timeline

| Phase | Work | Duration |
|---|---|---|
| 1 | Kickoff, asset collection, reference and copy sign-off | 3–4 days |
| 2 | Wireframes — 5 pages, desktop + mobile | 3 days |
| 3 | UI design — Home + one inner page approval, then remaining pages | 5–6 days |
| 4 | HTML/CSS/JS development and animation | 8–10 days |
| 5 | Integrations, SEO, responsive and cross-browser QA | 3 days |
| 6 | Deployment, SSL, DNS, go-live, handover | 2 days |

**Indicative total: 4–5 weeks** from receipt of complete content and imagery.

---

## 16. Out of Scope

- Online appointment booking with slot management or payment.
- Patient login, records, teleconsultation.
- Donation payment gateway (quotable separately; current scope links out or uses the enquiry form).
- CMS or admin panel — the site is static; edits handled by Kaizen on request.
- Blog with authoring workflow (a static articles listing can be added on request).
- Content writing, professional photography, videography.
- Ongoing SEO campaigns, ads, social media management.
- Annual hosting, domain and maintenance beyond initial deployment.
- Any rebuild of netrameyefoundation.com.

---

## 17. Open Questions

1. **Domain** — a personal domain (e.g. `dranchalgupta.com` / `ankhonkidoctor.com`) or a subdomain of netrameyefoundation.com?
2. Does this site replace, sit alongside, or feed traffic to netrameyefoundation.com? Their relationship needs to be explicit in the nav.
3. Is the Netram brand logo used as the site's mark, or is a personal monogram to be designed for Dr. Gupta?
4. One address on Contact (Greater Kailash-2) or both, including C.R. Park?
5. Is a donation flow needed at launch or deferred?
6. Are surgical volume and patient numbers approved for publication?
7. Blog/articles at launch or phase 2?
8. Who signs off on design — Dr. Gupta directly, or a coordinator?

---

*Prepared by Kaizen Infotech Solutions Pvt. Ltd.*
