# Reference teardown

Measured in Chrome (playwright-cli) on 16 Sep 2026 from the live sites at 1440×900 and 390×700: computed styles read from the DOM, Webflow interaction definitions read from the IX2 store, hover states recorded by hovering. Captures are in `references/` (`medic-1440.png`, `medic-390.png`, `sach-viewports/` for the scroll-driven site, and `measured-*.json` for the raw numbers).

Where the two references disagree, the brief's split applies: **Medic 128 governs the global UI** (header, buttons, cards, forms, footer, inner pages) and **Save a Child's Heart governs the Home scroll story, the timeline and the Foundation page**.

---

## 1. medic-128.webflow.io — the layout system

### 1.1 Container, grid, spacing

| | Desktop 1440 | Mobile 390 |
|---|---|---|
| Container | `max-width: 1200px`, `padding: 0 15px`, centred → **1170px content** (x = 135 → 1305) | 390px, `padding: 0 15px` → **360px content** |
| Section padding | `padding: 0 0 120px` (top 0 — the previous section's bottom padding is the gap); hero `40px 0 120px`; testimonial band `120px 0 200px`; footer `80px 0 40px` | `0 0 60px`; hero `40px 0 60px`; testimonial `60px 0 130px`; footer `60px 0 40px` |
| Grid | Webflow flex rows. Two-column sections split 50/50 inside 1170 (e.g. text 597px, image 573px). Step row: 4 × 281px, `gap 15px`. Department cards: CSS grid `328px 328px`, cards `max-width 271px`, `margin-top 20px`, second column offset upward by one card-margin so the pair staggers. Counter block `max-width 500px`. Consultation card `1170 × 442`, image column 412px + form column 562px | Everything stacks to one column, centred text; step cards stack `margin-top 40px`; department cards full width `margin-top 20px`; counter block 360px; consultation card image on top, form below |
| Element rhythm | h1 `margin 10px 0`; hero p `margin 25px 0 35px`; h2 `margin 10px 0`; card h3 `margin 25px 0 10px`; card p `margin 0 0 15px`; step icon `padding-bottom 30px`; counter number `margin-top 35px`, label `margin 5px 0 30px`; step row `margin-top 70px` after the heading | same |

### 1.2 Type — Poppins throughout, body `16px / 20px` on `body`, paragraphs `16px / 24px`

| Role | Desktop | Mobile | Weight | Colour |
|---|---|---|---|---|
| H1 (hero) | **76 / 91.2** | 50 / 60 | 700 | navy `#223645` |
| H2 (section) | **46 / 59.8** | 40 / 52 | 700 | navy; white on green band |
| Counter figure (h2) | **40 / 52** | 40 / 52 | 700 | teal `#36807F` |
| H3 (card / step title) | **24 / 28.8** (26 / 31.2 in the №1 block) | 24 / 28.8 | 700 | navy; white on teal cards |
| Nav link | 18 / 21.6 | (menu) 18 | 500 | `#222222`, hover teal |
| Button label | 18 / 21.6, `letter-spacing .5px` | same | 700 | white / teal / pink |
| "See more" link | 18 / 21.6 | same | 700 | navy, circle-arrow icon 22px |
| Eyebrow ("FAST SOLUTION", "OUR BENEFITS") | 14 / 16.8, uppercase, centred or left | same | 500 | teal |
| Paragraph (`.paragraph-large`) | **16 / 24** | 16 / 24 | 400 | grey `#707070`; white on teal/green |
| Footer column title | 18 / 21.6 | same | 500 | white |
| Footer link | 16 / 19.2, `padding 10px 0` | same | 400 | white, hover teal |
| Copyright | 14 / 16.8 | same | 500 | white |
| Input text | 14 / 16.8 | same | 400 | `#333333` |
| Accordion row | 16 / 20 | same | 600 | black |

Headings are sentence case. Two H1/H2 lines carry a hand-drawn underline/strike image under one word ("health", "We care", "for you") — a decorative SVG stroke in teal or pink, animated by width on scroll.

### 1.3 Colour

| Role | Value | Where |
|---|---|---|
| Navy | `#223645` rgb(34,54,69) | headings, footer ground, the "answers" block text |
| Body grey | `#707070` | all paragraphs |
| Teal (primary brand) | `#36807F` rgb(54,128,127) | outline button, nav hover, eyebrows, counters, department cards, №1 block, testimonial band, icons |
| Teal tint | `rgba(54,128,127,.2)` | slider arrow discs, icon tiles |
| Deep teal | `#083A3A` rgb(8,58,58) | "When you need answers" block |
| Pink (CTA) | `#E61F57` rgb(230,31,87) | primary button, "International Services" block, strike-through stroke, striped shadow graphic |
| Pink wash | very light pink (`#FDF3F6`-ish) as a large rounded blob behind the step/about sections (`.pink-section`) | decorative |
| White | `#FFFFFF` | page ground, cards |
| Border | `rgba(0,0,0,.2)` nav bottom; `#CCCCCC` inputs; `rgba(34,54,69,.2)` accordion rows | |
| Nav link | `#222222` | |

Ours: teal → **olive `#5E6A42`**, navy → **near-black `#383434`** (logo iris), pink → the second accent (the PRD's amber `#D99A2B`, fills only), deep teal → **moss `#3C4632`**, body grey stays `#707070`-class (we use `#5F6857` for contrast), pink wash → **paper `#F6F4EC`** blob.

### 1.4 Section-by-section inventory (Home)

1. **Navbar** — white, `height 113` (padding 15 0 + 82 container row), `border-bottom 1px rgba(0,0,0,.2)`, `position: relative` (not sticky). Logo 70×70 left; nav links centred-right (`padding 20px`, gap 0); outline pill CTA right (240×64). Mobile: 81px tall, logo 50px, burger right, links in a dropdown menu.
2. **Hero** (`section-top-banner`, padding 40 0 120): two columns. Left 597px: H1 76px (3 lines), paragraph, then a row of primary pink button + "See more" text link with circle-arrow. Right 573×745: portrait cut out on an arched teal-gradient shape (`border-radius` top 50%), with a floating white "Find a doctor" card (264×269, r10, shadow) overlapping bottom-right; a striped-lines graphic behind the button. Mobile: image first (252×328, 70% wide, centred), then H1 50px centred, p, button, link — all centred.
3. **Steps** (`pink-section`, padding 0 0 120, pink blob background): eyebrow "FAST SOLUTION" teal centred, H2 46 centred (2 lines, `max-width 400`), then 4 step cards in a row (281 wide, icon 70×70 on a light teal shape, H3 24 centred, p 16 centred). Mobile: stacked, 40px apart.
4. **About** (same pink-section): text left (H2 with pink strike on "We care", p, outline button), two overlapping photos right (470×470 and 312×434, r10) with a dotted-grid decoration (120×120) bottom-right.
5. **Benefits**: left, white counter card 500×333, r10, `shadow 0 0 20px -1px rgba(0,0,0,.1)`, split into a full-width cell over two half cells by 1px hairlines; figure 40/700 teal centred, label 16 grey. Right: eyebrow, H2, p.
6. **Departments** (padding 0 0 120): left column text (H2, p, "See More" link); right 2×2 grid of teal cards 271×260, r10, padding 30 20 15, white icon tile 64×64 r10 top-left, H3 24 white, p white; the right column sits 20px higher; dotted decoration.
7. **Health service** (padding 0 0 120): image 513×473 left with dots; right H2 (underline stroke on "for you"), p, then 3 accordion rows — pill rows 627×70, `border 1px rgba(34,54,69,.2)`, `radius 80px`, padding 20, numbered circle "1/2/3" left in teal tint, title 16/600, chevron right; `margin-bottom 25px`.
8. **№1 hospital** (padding 0 0 120): three coloured blocks in a 585 + 503 split, rounded on the outer corners only (20px), teal 585×500 padding 50 40, pink 503×250 padding 40 60 50 40, deep-teal 503×250; quarter-circle geometric decorations and a corner arrow icon; H3 26 white, p 16 white.
9. **Testimonials** (green band, teal bg, padding 120 0 200): world-map dot pattern, H2 46 white centred, avatar 110px circle, quote p 16 white centred `max-width 570`, name 16/700, city 16, two arrow discs 80×50 (teal tint, r50).
10. **Free consultation** (padding 0 0 120): white card 1170×442, r10, `shadow 0 20px 40px rgba(0,0,0,.1)`, pulled up over the green band by `margin-top -110px`; photo column left; H2 46, 2×2 inputs (266×52, r10, border 1px #ccc, padding 15, 14px placeholder-as-label, gap 25/30) + select, pink submit 348×64.
11. **Footer** (navy, padding 80 0 40): logo 70 + tagline p 16 white + 4 social icons (18px, 30px apart) in a 326px column; three link columns (251px each: title 18/500, links 16/400 with 10px vertical padding); bottom row centred 14/500 copyright. Mobile: one column, left-aligned, 60 0 40.

### 1.5 Component anatomy

| Component | Spec |
|---|---|
| **Primary button** | pink `#E61F57` bg, white 18/700 `ls .5px`, `padding 20px 78px 20px 40px` (extra right padding for the 20px circle-arrow icon), `radius 50px`, `border 1px` same pink, `shadow 0 5px 30px rgba(230,31,87,.3)`, height 64. Hover 300ms ease: bg → white, text → pink; the arrow icon slides `x +20px` 300ms. Behind the hero button a striped-lines decoration (pink) offset 10px right/down. |
| **Secondary button** | transparent, teal text 18/700, `border 1px teal`, same padding/radius/height. Hover 300ms: bg → teal, text → `#EEF4F8`. |
| **Text link** ("See more") | 18/700 navy + circle-arrow icon 22px, `padding-right 30px`; hover opacity/colour 300ms, icon `x +20px`. |
| **Nav link** | 18/500 `#222`, `padding 20px`, no underline; hover colour → teal 300ms. Dropdown ("Demos", "Pages") with chevron rotating 180° 500ms. |
| **Step card** | no box: icon 70×70 (teal glyph on a soft teal blob), H3 24 centred, p centred, `padding 0 15px`. Hover: text colour → teal. |
| **Department card** | teal bg, `radius 10px`, `padding 30 20 15`, white icon tile 64×64 `radius 10px`, H3 24 white `margin 25 0 10`, p 16 white. No shadow, no hover lift (verified: none). |
| **Counter card** | white, `radius 10px`, `shadow 0 0 20px -1px rgba(0,0,0,.1)`, 1px hairline dividers, figure 40/700 teal, label 16 grey, cells centred, `padding 35 top / 30 bottom`. |
| **Accordion row** | `radius 80px`, `border 1px rgba(34,54,69,.2)`, `padding 20px`, number badge left, title 16/600, chevron right; open: panel height auto 400ms ease + chevron rotate 300ms + title colour 300ms. |
| **Coloured feature block** | 20px radius on outer corners only, padding 40–50, geometric quarter-circle decoration, arrow icon bottom-right. |
| **Input / select** | 52px tall, `padding 15px`, `border 1px #CCCCCC`, `radius 10px`, 14px text, white bg; no visible label (placeholder text with asterisk). |
| **Card shadow** | two values only: `0 0 20px -1px rgba(0,0,0,.1)` (counter) and `0 20px 40px rgba(0,0,0,.1)` (consultation). |
| **Radii** | 10px cards/inputs/icon tiles; 20px feature blocks; 50px buttons; 80px accordion rows; 50% avatars and arrow discs. |
| **Decorations** | dotted 6×6 grid image 120×120 near photos; striped-lines under the primary button; quarter-circles in feature blocks; arched gradient behind the hero portrait; hand-drawn underline strokes under one word in headings. |
| **Footer** | navy `#223645`, 4 columns (326 + 3×251), titles 18/500, links 16 with 10px padding, socials 18px 30px apart, copyright 14 centred. |

### 1.6 Motion (from the IX2 store — 642 events, 70 action lists)

| Trigger | Recipe | Count |
|---|---|---|
| Scroll into view, element top at 0% or 20% of viewport | `opacity 0 → 1` **and** `translateY(100px) → 0`, **1000ms, easeOutQuart**, no stagger (each element has its own trigger) | 289 |
| Scroll into view | `opacity 0 → 1`, 1000ms easeOutQuart (no move) | 60 |
| Scroll into view (heading strokes) | width 0 → 100% 500–700ms + rotate | 3 |
| Hover, buttons/links | icon `x 0 → 20px` 300ms + bg + text colour 300ms (out: 500ms) | 71 |
| Hover, some cards | `translateY 5px` | 9 |
| Dropdown open | height 0 → auto 400ms ease; chevron rotate 180° 300ms; title colour 300ms | 19 |
| Accordion/tab click | rotate 180° 500ms; size 300ms | 17 |
| Slider | Webflow slider, arrows only, no autoplay observed | |
| CSS transitions | `color .3s ease` (links), `all .3s ease` (buttons), `all .2s ease` (icons) | |

Nothing is pinned, nothing parallaxes, no smooth-scroll library. Every block on the page fades up 100px as it enters.

---

## 2. 25.saveachildsheart.org — the storytelling layer

### 2.1 Container, grid, spacing — everything is in **vw** (1vw = 14.4px at 1440)

| | Desktop 1440 | Mobile 390 |
|---|---|---|
| Page | full-bleed, `max-width 1920`; no fixed container | |
| Text block (`section-heading`) | **864px wide = 60vw**, `margin 0 20vw`, `padding 10vw 0` (144px) | 390 wide, `padding 91px 0` (or 70) |
| Description block | 720px = 50vw, `margin 0 10vw`, `padding-top 5vw`, `margin-bottom 5vw` | `padding-top 70px` |
| Three-column grid | wrapper 1152 = 80vw (`margin 0 10vw`), items **360 = 25vw**, gap 72 = 5vw; alternate columns offset by `margin-top 10vw` (144px) — the columns stagger | one column, item 390 wide (full bleed) |
| Two-column feature | 1008 = 70vw, image column 504 = 35vw, gap 5vw | stacked |
| Section paddings | mostly **0** — spacing comes from the inner heading blocks; children grid `padding-top 15vw` (216); story grid `padding-bottom 20vw` (288); `is--video` overlaps the previous section by `-10vw` | 208px, 110px |
| Sticky story | `section-sticky` 3150–3462px tall wrapper containing a **100vh pinned panel** (`position: sticky; top: 0; height: 900`); the scroll distance drives 3 states (map years / founding → access → mission) | same pattern at 2450px |
| Radius | **28.8px = 2vw** on every image tile, card, video frame, side nav | 27.3px |

### 2.2 Type — Montserrat, all display type UPPERCASE, body `1vw`

| Role | Desktop | Mobile | Weight | Colour |
|---|---|---|---|---|
| Stat figure | **72 / 86.4 (5vw)** | 35.1 | 700 | white |
| Timeline year | 57.6 / 57.6 (4vw) | 42.9 | 700 | white |
| Cost figure | 59 | 31.2 | 700 | white |
| H2 (section) | **46.1 / 46.1 (3.2vw)**, uppercase | 25.4 (35 in the footer) | 700 | white |
| H3 (story chapter) | 44.6 / 53.6 (3.1vw), uppercase | 39 | 600 | yellow `#F0C62A`; blue `#35A5E6` in the history chapters |
| H1 "DONATE NOW" / "GET INVOLVED" | 44.6 / 49.1, uppercase | 43.4 | 500 | white |
| Child name (marquee) | 72 / 86.4, uppercase | 35 | 700 | white with red EKG separators |
| Video overlay line | 43.2 / 51.8, uppercase | 22.4 | 400 (bold spans) | white |
| Intro paragraph | **18.7 / 31.8 (1.3vw)**, uppercase, centred | 16.8 | 400, bold red spans | white |
| Eyebrow above H3 (`h4.subhead`) | 17.3 / 24.2, uppercase | 18 | 500 | white / `#D8DAE5` |
| Story paragraph | **14.4 / 24.5 (1vw)**, centred, `padding 1vw 0` | 14 / 22.4 | 400 | white; body default `#C1C1C1` |
| Card caption (child quote) | 14.4 / 17.3, uppercase | 14 | 600 | white |
| Card meta (country) | 14.4 / 18.7, uppercase | | 500 | `#C1C1C1` |
| Stat label | 14.4 / 14.4, uppercase | | 400 | white |
| "LEARN MORE" | 13 / 20.7, uppercase | | 500 | white |
| Nav link (side panel) | 18.7 / 30 | 19.6 | 400 | white |
| Footer copyright | 13.2 / 22.4 | | 400 | white |

### 2.3 Colour

| Role | Value |
|---|---|
| Page ground | navy `#293146` rgb(41,49,70) |
| Lifted ground (side nav, hero band 2) | `#51586B` / `#454B63` |
| Red (accent, CTA, EKG line) | `#E63543` rgb(230,53,67); burger disc 48px |
| Yellow (chapter headings, keywords) | `#F0C62A` rgb(240,198,42) |
| Blue (history chapter headings) | `#35A5E6` rgb(53,165,230) |
| Crimson band (featured section, footer) | `rgba(230,53,67,.55)` over navy → reads `#8E3A4C` |
| Teal-green band (video frames) | `#06EECB` at low opacity over video → reads `#2E8F80` |
| Body text | `#C1C1C1`; headings white; muted `#D8DAE5` |
| Card hover | bg → red `#E63543` |

Ours: navy → **moss `#3C4632`** ground; red → **olive `#5E6A42`** (EKG line, burger disc, hover fill) with amber `#D99A2B` for the yellow keyword/heading role; crimson band → deep moss `#2E3626`; body `#C9CFB8` (mist) on moss.

### 2.4 Section-by-section inventory (Home, in scroll order)

0. **Preloader** — full red screen with the "25 + EKG" lottie, exits `translateY(100%)` 1000ms outSine after 1200ms.
1. **Fixed nav** — transparent bar: logo 130×48 at `3vw / 2vw`; right cluster: heart icon + "DONATE NOW" (44.6/500 uppercase text, not a pill) + red burger disc 48px. Burger opens a **side panel** 317px (22vw) from the right, `#51586B`, radius 28.8 on the left corners, links 18.7/400 stacked. Mobile: "DONATE NOW" rotated vertically on the right edge, burger 53px.
2. **Hero** — full-bleed 100vh photo (a child), text bottom-left at `padding 0 0 5.5vw 12vw`: "CELEBRATING / **25 YEARS OF HOPE**" 44.6px, "SCROLL TO LEARN MORE" 13px; the yellow EKG line animates across on load (elements enter 2300–2500ms after page start, `translateY(20em → 0)` 1000ms). Mouse-parallax ±50px on the image.
3. **Intro + counters** — heading block 864 wide: uppercase paragraph 18.7 with red bold keywords; "DONATE NOW" h1; then a **marquee row of stats** (72/700 figures, 14.4 uppercase labels, red EKG glyph 58×101 between items, 28.8px gaps) scrolling continuously (`marquee 35s` CSS animation).
4. **Sticky timeline** — pinned 100vh: world-map dot image with a red heart pin; years (57.6/700) with 14.4 paragraphs slide horizontally as you scroll (`translateX 0 → −110px` scrubbed between 28–90% progress) while the red EKG line lottie draws (0→100 between keyframes); pin markers pop.
5. **Heading block** "THE FACES OF HOPE…" + eyebrow h4.
6. **Children grid** — 3 columns of 360×504 image cards, r28.8, alternate columns offset 144px; each card: photo, uppercase 14.4/600 quote caption, "LEARN MORE"; hover: bg → red, `translateY 30 → 0`, opacity .7 → 1, 500ms; click opens a story pop-up (slides in from x 100px, 300ms easeOut).
7. **Video band** — 100vh-ish (864px) video frame with r28.8 and a green tint, overlay line 43.2 uppercase, overlapping the grid above by −144px.
8. **Sticky chapters ×3** ("PROVIDING ACCESS", "TAKING ACTION", "NURTURING HEALING", "CULTIVATING RESILIENCE"): pinned panels, each with a photo column (360 wide) and a text column (eyebrow h4 → H3 yellow 44.6 → 14.4 paragraph 360 wide) alternating sides; content fades up as the panel pins.
9. **Names marquee** — two rows of 72/700 uppercase names with red EKG separators, `marquee-name 150s` in opposite directions; intro line 23px below.
10. **Children tiles wall** — dense grid of r28.8 tiles (a Webflow slider, 2 slides), `padding-top 216`.
11. **Crimson featured band** — testimonial pairs: 504×648 photo + quote block with gold quote marks (43×33), 15.8/26.9 paragraph, name 14.4/600 uppercase, EKG rule; alternating.
12. **Countries marquee** + "TOGETHER WE CAN…" 25.9 uppercase block + "DONATE NOW".
13. **Video band 2** (teal-green).
14. **Sticky history ×3** ("OUR FOUNDING", "EXPANDING ACCESS", "GROWING OUR MISSION") — blue H3s, photo/text alternating.
15. **Donation costs** — H2 yellow "HOW YOUR DONATION SAVES HEARTS", four cost rows (59/700 figure + "USD" 28.8, 14.4 paragraph with yellow keywords), EKG lottie lines between, alternating left/right.
16. **"SAVING CHILDREN'S LIVES" + DONATE NOW** block (43.2 uppercase).
17. **Footer** (crimson band): "GET INVOLVED" eyebrow 28.8 → H2 46 uppercase "TO SAVE A LIFE IS TO SAVE THE WORLD." → p → two 432×432 r28.8 image CTAs ("GET INVOLVED", "DONATE") with hover bg; newsletter: 2 inputs 281×56 (r7, transparent, border rgba(216,218,229,.29)) + white submit 130×56 r6.5 uppercase 13px; logo, 4 social icons, copyright 13.2.

### 2.5 Motion (from the IX2 store — 523 events, 33 action lists, 12 scroll-scrubbed)

| Trigger | Recipe | Count |
|---|---|---|
| Scroll into view (top at 0%) | `opacity 0 → 1`, **1200ms ease, 200ms delay** | 73 |
| Scroll into view | `translateY(10em) → 0` **1200ms cubic-bezier(0, .003, 0, 1.003)** + `opacity 0 → 1` 1000ms ease; delay 0 / 300 / 600ms for staggered siblings | 132 |
| Scroll into view (offset 25–45%) | same fade-up, fired later | 14 |
| Scroll progress (scrubbed) | `translateX 0 → −62px` between 5–75%; `0 → −110px` between 28–90% (timeline panels); `translateY 30em → −30em` across 0–100% (parallax); lottie EKG 0 → 100 between chapter keyframes; scale + opacity ramps | 12 lists |
| Mouse move (hero) | `translateX/Y −50 → +50px` following the cursor | 2 |
| Hover, image cards | `scale 1 → 1.3` **4000ms** cubic(0,.024,.17,1.009) + filter + overlay opacity → .4; caption `rotate` 200ms easeOut | 91 |
| Hover, three-column items (CSS) | `background-color .5s ease` → red; `translateY 30 → 0`; opacity .7 → 1 | 19 |
| Page start | hero text: opacity 0 + `translateY(20em)` → in at **2300–2500ms** delay, 1000ms; preloader out at 1200ms | 4 |
| Marquees (CSS keyframes) | stats `35s linear infinite`; names `150s` | 5 |
| Click | story pop-up: `translateX 100px → 0` 300ms easeOut + lottie | 8 |

Sticky pinning is native `position: sticky` (100vh panels inside tall wrappers); no smooth-scroll library.

---

## 3. What "match the reference" means for this build

- **Fonts:** Medic uses Poppins, SACH uses Montserrat. The PRD fixes ours (Satoshi body, a serif display); the references use a single geometric sans for everything. To match the references' *look*, the display face must behave like theirs: bold (700), sentence case on clinical pages, uppercase on the Foundation/story pages. I will keep Satoshi and set headings in **Satoshi 700** at the reference sizes; the serif is dropped (it is the thing that made the previous build look unlike the references). If you want Poppins/Montserrat literally, say so — it is a one-line font swap.
- **Palette:** only the hue changes — teal/navy/pink → olive/near-black/amber; navy story ground → moss. Tints, shadows, borders keep the references' alpha values.
- **Photography:** ours, untreated apart from cropping to the references' shapes (arched hero cut-out, r10 cards, r28.8 story tiles).

---

## 4. Mapping table — every section of our five pages → the reference section it copies

Sizes and behaviours are the reference's; only the words and pictures are ours.

### index.html (Home — SACH scroll story inside Medic chrome)

| # | Our section | Copies | Layout taken verbatim |
|---|---|---|---|
| 1 | Navbar | Medic §1.4-1 | white bar 113px, hairline bottom, logo 70, links 18/500, outline pill CTA "Book a consultation"; mobile 81px + dropdown menu |
| 2 | Hero | Medic §1.4-2 | 2-col: H1 76/700 "Dr. Anchal Gupta" + credential paragraph + pink→amber primary pill "Book a consultation" + "WhatsApp" text link with circle-arrow; portrait on the arched olive-gradient cut-out, floating white "Book / Call" card bottom-right |
| 3 | Intro | Medic §1.4-3 heading block | eyebrow "SENIOR EYE SURGEON" teal→olive 14/500 uppercase, H2 46/700 centred, 2-line intro; then the KGMU → MAMC → Max/Fortis → Netram arc as **4 step cards** (icon 70, H3 24, p 16) |
| 4 | Impact counters | SACH §2.4-3 stat marquee **and** Medic §1.4-5 counter card | on a moss band: figures 72/700 white with an olive EKG glyph between, labels 14.4 uppercase; count-up on view. (Medic's white counter card is used on About instead.) |
| 5 | Areas of expertise | Medic §1.4-6 department cards | text column left (H2, p, "See more" link), 2×2 (six → 3×2) teal→olive cards 271×260 r10 with white icon tile |
| 6 | Netram, the institution | Medic §1.4-4 about | text left (H2 with hand-drawn underline stroke, p, outline button), two overlapping photos right r10 + dotted decoration |
| 7 | Recognition strip | SACH §2.4-9 names marquee | one row of honours 46/700 uppercase with olive EKG separators, `marquee 35s`; "All awards" link below |
| 8 | Foundation teaser | SACH §2.4-7 video band + §2.4-3 intro | full-bleed camp photograph in an r28.8 frame with a green→olive tint, overlay line 43.2 uppercase "SIGHT TO ALL"; below it the project names as a second marquee and an amber "Explore the Foundation" pill |
| 9 | Media coverage | Medic §1.4-9 testimonial band (structure) | teal→olive band 120/200: H2 white centred, publication logos row (grey, 60% opacity, colour on hover) — the band's dot-map pattern is replaced by the logos |
| 10 | Contact band | Medic §1.4-10 consultation card | white card 1170×442 r10 pulled −110px over the band above: photo left, H2 "Book a consultation", 2×2 fields + enquiry-type select, amber submit pill; address + phones under it |
| 11 | Footer | Medic §1.4-11 | navy→near-black, logo + tagline + socials, three link columns, copyright |
| — | Floating WhatsApp / call | (neither reference) — PRD §7 | 56px olive disc bottom-right, enters at 2s |

### about.html (Medic system)

| # | Our section | Copies | Layout |
|---|---|---|---|
| 1 | Hero | Medic §1.4-2 (text-only variant, no arch) | H1 76 + descriptor p; portrait right on the arched cut-out |
| 2 | Long biography | Medic §1.4-4 about, mirrored | two overlapping photos **left**, editorial text right in 2 columns of p 16/24 |
| 3 | Pull-quote "Good Health for All" | SACH §2.4-12 "TOGETHER WE CAN…" block | 25.9 → 46/700 uppercase centred on a moss band, 864 wide, padding 144 |
| 4 | Qualifications | Medic §1.4-7 accordion rows (static) | pill rows r80 with numbered badges — one per qualification |
| 5 | Philosophy of care | Medic §1.4-8 №1 hospital blocks | three coloured blocks (olive / amber / moss) with outer-corner radii: "Sight to All", "Since 2012", "24 states" |
| 6 | Netram's story + reach map | Medic §1.4-5 benefits | white counter card left (3 figures), text right; the India map SVG in place of the photo in a second row |
| 7 | Gallery strip | SACH §2.4-10 tiles | r28.8 tiles, 3 across, alternate columns offset |
| 8 | CTA band | Medic §1.4-10 consultation card (short form) | |
| 9 | Footer | Medic | |

### expertise.html (Medic system + SACH sticky timeline)

| # | Our section | Copies | Layout |
|---|---|---|---|
| 1 | Hero | Medic hero, text-only | H1 76, p, primary pill |
| 2 | Specialties accordion | Medic §1.4-7 | image left (513×473 + dots), H2 with underline stroke, six pill accordion rows r80 with numbered badges; open = height 400ms + chevron rotate |
| 3 | Career timeline | SACH §2.4-4 sticky timeline | moss band, **pinned 100vh panel**: years 57.6/700 + 14.4 paragraphs sliding horizontally as the page scrolls (`translateX` scrubbed), olive EKG line drawing underneath, pin markers popping; mobile: stacked years with the line drawn vertically |
| 4 | Surgical distinction (Gold Medal) | Medic §1.4-8 feature block | one olive block 585×500 r20 (outer corners) with the arrow icon + IPCL stage photo beside it |
| 5 | Academics & conferences | Medic §1.4-3 step cards | eyebrow, H2 centred, 4 step cards: Invited faculty / Drug launches / CII 2025 / TEDx 2026 |
| 6 | Awards & accolades | Medic §1.4-6 department cards | H2 + p left; 3×N grid of cards r10 with the year as the icon tile; "Show all" reveals 2012–2018 |
| 7 | Leadership | Medic №1 block (single, deep-teal→moss) | |
| 8 | Media | Medic testimonial band | H2 white centred, cards with publication + headline, slider arrows |
| 9 | CTA + footer | Medic | |

### foundation.html (SACH layer, moss ground)

| # | Our section | Copies | Layout |
|---|---|---|---|
| 1 | Hero | SACH §2.4-2 | full-bleed field photograph 100vh, text bottom-left at 12vw: "NETRAM EYE FOUNDATION / **SIGHT TO ALL**", "SCROLL TO LEARN MORE"; olive EKG line draws on load; mouse-parallax |
| 2 | Origin | SACH §2.4-3 intro | 864-wide uppercase paragraph 18.7 with amber bold keywords ("SINCE 2012", "24 STATES"), "GET INVOLVED" h1 line |
| 3 | Impact counters | SACH §2.4-3 stat marquee | 72/700 figures, EKG glyphs, `marquee 35s` |
| 4 | Reach map | SACH §2.4-4 sticky map | **pinned panel** with the India SVG, amber pin markers popping state by state as the years/regions slide horizontally |
| 5 | Projects | SACH §2.4-6 children grid | 3-column r28.8 photo cards 360×504, alternate columns offset 144px, uppercase caption, "LEARN MORE"; hover bg → olive, lift 30px; each opens its anchor section |
| 6 | Project detail chapters | SACH §2.4-8 sticky chapters | pinned panels, photo column + eyebrow → H3 amber 44.6 → paragraph 360 wide, alternating sides (Roshini, Eye Mela, Chashma Bus, Nayan Hans) |
| 7 | Eye Maitri | SACH §2.4-11 crimson featured band | deep-moss band, 504×648 photo + text block with the gold quote marks replaced by the lockup, amber "Corporate enquiry" pill |
| 8 | Field gallery | SACH §2.4-10 tiles wall | r28.8 tiles, lightbox |
| 9 | Partners | SACH §2.4-12 countries marquee | partner names in a 72/700 uppercase marquee with EKG separators (logos when supplied) |
| 10 | Get involved | SACH §2.4-17 footer | H2 uppercase, three 432×432 r28.8 image CTAs (Donate / Volunteer / Partner) with hover fill |
| 11 | Foundation contact + newsletter-style strip | SACH footer form | inputs 281×56 r7 transparent, white submit |
| 12 | Footer | Medic (global) | |

### contact.html (Medic system)

| # | Our section | Copies | Layout |
|---|---|---|---|
| 1 | Short hero | Medic hero text column | H1 76 "Book a consultation" + p |
| 2 | Form + details | Medic §1.4-10 consultation card | white card r10 shadow: form left (2×2 + select + textarea + consent, amber submit), clinic details right where the photo sits |
| 3 | Map | Medic §1.4-7 image + text | click-to-load map in a 513×473 r10 frame with dots; address + "Get directions" outline pill |
| 4 | FAQ | Medic §1.4-7 accordion | pill rows r80, numbered |
| 5 | Footer | Medic | |

### 404.html
Medic hero text column: H1 76 "Page not found", p, primary pill "Go to the home page".

---

## 5. Deliberate content-driven differences (the only ones I intend)

1. Medic has one H1 line with a scribbled word; ours carries the name, so the stroke goes under "Gupta".
2. Medic's hero "Find a doctor" card lists three doctors; ours lists the two phone numbers and WhatsApp.
3. Medic has 4 departments; we have 6 areas → 3×2 of the same card.
4. SACH's stat marquee has 5 figures; ours has 5 (years, states, children, beneficiaries, spectacles).
5. SACH's children cards open a pop-up; our project cards scroll to their chapter (no pop-up content exists).
6. The floating WhatsApp/call buttons exist in neither reference; PRD requires them.
7. Fonts per §3 unless you say otherwise.

Everything else that differs from the reference in the build will be treated as drift and fixed in the per-page pass.
