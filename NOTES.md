# Build notes

Running log: decisions made, things tried and rejected, and what the client still owes. Passes 1 and 2 are the rejected first direction and are kept as history; Pass 3 is the build that ships.

## Pass 6 — review round 2 (17 Sep 2026)

- Home hero uses the client's `_B7A3728.JPG` (landscape, at Netram in front of the I Am 6/6 mural): the arch became a wide 3:2 arch (`.hero__arch--wide`, full width on phones) instead of cropping the frame tall. Expertise hero uses `_B7A1069.JPG` (navy scrubs). Both go through `tools/prepare-drive.py`.
- "Learn more" on the specialty/project cards is the same 22px circle-chevron as every link-arrow, pointing right, and rotates to point down (olive fill, white chevron) when its panel is open.
- About: consultation card removed; "Twenty-four states" is a paper band with the interactive India map (now a shared component), three stat cards and seventeen state chips.
- Contact: the enquiry-type dropdown is a custom-styled select (olive chevron, grey placeholder state); WhatsApp uses the WhatsApp glyph (`#i-whatsapp`, filled icon variant `.ico--fill`) in the chips, the feature card, the Home hero card and the footer; footer contact icons are vertically centred on their text and the foundation website line is gone.
- Section spacing measured on every page at 1440 and 390: no consecutive sections closer than 59px (Medic's own 60/120 rhythm); the only tight spot, the old Contact banner 60px above the form card, was removed by the Contact restructure.
- Final Lighthouse 12 mobile after round 3: Home 95 · About 94 · Expertise 94 · Foundation 93 · Contact 97 for Performance; Accessibility, Best Practices and SEO 100 everywhere; CLS 0. The Contact map is injected 1.2s after `load` (no click needed) so the iframe never delays the largest paint (86 → 97).
- Round 6 (same day): the Expertise timeline is scroll-driven on phones too (pinned 100svh panel, one full-width entry at a time, the track snaps entry by entry with a 500ms ease as the section scrolls; the EKG line spacing follows the entry width). Foundation counters are one per row under 600px so no figure wraps or clips; the field gallery is a single column there. Repository initialised and pushed to https://github.com/webteam-96/eye.git (originals/, references/, .webcheck/, .playwright-cli/ and the deck PDF are ignored).
- Round 5 (same day): the map embed and every address link use the client's Google Maps place link (https://maps.app.goo.gl/3CQNRF2XL87UhUgA7, the "Netram eye hospital" listing at 28.5495, 77.2437); the Contact JSON-LD carries `hasMap` and `geo`. The press section on Expertise has a full top gap.
- Round 4 (same day): Home about-row photos re-stacked (desk portrait in front, building behind); "A few moments" gets a 120px top gap; Expertise opens with the same centred dotted banner as About (title, intro, buttons, 3:2 photo) instead of the split hero; Foundation loses the partners marquee and the Donate/Volunteer/Partner blocks (the "Get involved" button now goes to the Contact form with the Foundation type). Contact map is a plain iframe again at the client's request (they want it visible instantly; Performance on that page drops to the mid-80s because the iframe is above the fold) and the Instagram/LinkedIn line is two icon pills.
- Round 3 (same day): Home banner uses the client's `dr.png` (10:13 portrait) whole, in a rounded frame, with the heading split into "I'm Dr. Anchal Gupta" (one line, 50px) and the subline "an eye surgeon in Delhi"; the floating card keeps `right: 0` below 1300px so it never widens the page. About qualifications follow Save a Child's Heart's "How your donation saves hearts" pattern: moss band, amber uppercase heading, five zig-zag rows of big title + line with an amber EKG spike that draws on view (`.quals`). Contact is heading, chips beside the live map, form, FAQ (duplicate details removed); the enquiry-type select is custom-styled; WhatsApp uses its own glyph; the footer lost the foundation website line and its icons are centred.

## Pass 5 — client's photographs, personal voice, responsive pass (17 Sep 2026)

- **Photographs from the client's Google Drive.** The two link-shared folders ("Dr. Anchal", "Images" with four dated shoots) are not visible to the Drive API, so `scratchpad/drive-list.py` reads the public folder pages and `drive-get.py` downloads the chosen originals (6000×4000 Canon frames, EXIF-rotated where portrait) into `originals/drive/`. `tools/prepare-drive.py` writes `assets/img/dr-<slug>-{480,800,1200}.{jpg,webp}` with no cropping. 19 frames used: consulting-room desk portraits (hero, About banner, about rows, service section, gallery), the two portrait-orientation frames (Home hero arch, consultation card), slit-lamp examinations (glaucoma, retina, examination cards), operating theatre (cornea, cataract cards), scrubs portraits (Expertise hero, CTA photos, gallery).
- **No cropping.** Every frame now takes the photograph's own proportion: 2:3 for the two portraits (hero arch 500×750, consultation column), 3:2 for everything from the Drive, 4:5 for the Netram facade, 2:1 for the school-camp banner and the HOA group, and the Foundation gallery is a CSS-columns masonry with natural heights. `object-fit: cover` remains only where the frame matches the source. The square I Am 6/6 photo uses `object-fit: contain`.
- **Copy** rewritten in Dr. Gupta's first-person voice from the same PRD facts; every visible `TODO:` line, the empty Netram Empower card, the three FAQ answers that had no answer, and the "Site by" credit are gone. Missing facts are listed in README for the client instead.
- **Footer** is three columns: brand, Quick links (amber chevrons), Contact (map, phone, WhatsApp, mail, globe icons).
- **Responsive.** New 992–1199 layer: Medic's fixed pixel columns become percentages, the navbar tightens (the Home link had pushed it past 1024), the blocks grid is fluid, image grids use `minmax(0, 1fr)` so an `<img width>` attribute can never widen a track (that was the Foundation overflow), the CTA box is a flex column with a smaller button below 1200. Verified with `scratchpad/realuser.js` at 360 / 390 / 768 / 1024 / 1280 / 1440 / 1920 on all six pages: no horizontal overflow, no cover-cropped images, plus the real-user pass (phone menu open/Escape, one-open accordion, slider, form validation, FAB, timeline swipe, show-all awards, lightbox open/Escape, live map), 0 console errors.

## Pass 4 — client changes after review (17 Sep 2026)

Requested by the client on seeing the Medic-exact build; each item was built, then verified in real Chrome at 1440 and 390.
- **Menu:** Home link added on every page (current page highlighted).
- **Home:** the four "Senior eye surgeon" steps are now white cards with numbered icon tiles; the counters are an olive band with amber progress rings (SVG dash draw on view) around icons, count-up numbers and an EKG line; "Why patients trust her" is its own section of three photo cards (children screened, Gold Medal, camps since 2012) with amber icon badges; "Areas of expertise" copies the Save a Child's Heart "faces of hope" grid (dark band with a tonal shift, tall 28px-radius photo tiles in a staggered three-column grid, icon + title + description in a gradient overlay, 4-second zoom on hover); the service accordion is redesigned (numbered tiles, olive open state, amber chevron, paper panel) and only one item opens at a time; the three blocks carry an icon tile, a link with arrow and, on the Netram block, a masked photo.
- **Expertise:** the career timeline is the Save a Child's Heart 1995 timeline: a pinned moss panel with the faint India map and a pulsing amber pin at Delhi, big years with descriptions in a row that slides sideways as the section scrolls (`initTimeline` in motion.js, 1800px of scroll), and an amber EKG line that draws under each year; on phones it is a horizontal swipe track. Awards are year cards (three columns, icon per honour, "Show 2012 to 2020"); press items are masthead cards with the publication, headline and link, print covers tagged.
- **Contact:** the address and phone line under the H1 became three contact chips (visit, call, WhatsApp); the Google map now loads directly as an iframe (no "Load the map" button); the FAQ cards align to the top of the grid so an open card no longer stretches its neighbour, and opening one closes the rest.
- **Accordion grouping:** any `[data-accordion]` wrapper closes its other items when one opens (Home service, Expertise and Foundation cards, Contact FAQ, About band).
- The generic EKG scrub (`initScrub`) skips the timeline line, which is driven by the timeline's own progress.

## Pass 3 — Medic 128 rebuild (16–17 Sep 2026)

### The brief changed
Client on 16 Sep: "The current design doesn't match the reference sites and I'm not approving it. […] The references are the brief. Do not substitute your own direction. If a choice in them looks like a generic default to you, build it that way anyway." Then: "make design like https://medic-128.webflow.io/ exact same only animation of electrocardiogram trace and other micro animation … https://25.saveachildsheart.org/". Only the content, the palette and the photography change.

### Method
- Both references measured from the DOM in real Chrome (computed styles, the Webflow IX2 interaction store for the SACH motion, hover states), not from screenshots → `REFERENCE-TEARDOWN.md`, `references/measured-*.json`, page captures at 1440 and 390 (Medic home + about-us, departments, our-doctors, our-process, faq, testimonials, news, contact-us; SACH viewport by viewport because its full-page capture is blank).
- Every page: built, captured at 1440 and 390, pasted beside the Medic reference page (`scratchpad/sbs.py`) and walked section by section; each difference either content-driven or fixed.
- Captures bypass the HTTP cache (`page.route("**/*")`): `python -m http.server` sends no cache headers and Chrome heuristically served day-old CSS, which hid one fix for a full round.

### Design system (tokens.css = Medic's numbers)
Poppins 400–700 self-hosted; H1 76/91.2 (50/60 mobile), H2 46/59.8 (40/52), H3 24/28.8, counters 40/52, p 16/24 `#707070`, nav 18/500, buttons 18/700; container 1200 with 15px gutters; sections padding-bottom 120 (60 mobile), bands 120/200, footer 80/40; radii 10 cards, 20 blocks, 50 buttons, 80 accordion rows; buttons 240×64 with the circle-arrow at right 40px, hover inverts in 300ms and nudges the arrow 20px; navbar 113px static white with a 1px `rgba(0,0,0,.2)` rule.
Palette mapping: teal → olive `#5E6A42`, navy → near-black `#383434`, pink → amber `#D99A2B` (ink text only; never white on amber), deep teal → moss `#3C4632`, pink wash → paper `#F6F4EC` / `#FAF9F4`.
Mobile alignment follows Medic exactly: only the hero, the centred sections and the step columns are centred; everything else stays left-aligned (a global "centre everything under 991px" rule was the first drift found and removed).

### Templates used
- Home = Medic home 1:1 (hero + floating "Reach the clinic" card, 4 steps, about row with two photos, counter card, 6 department cards with the raised even column, accordion service, three coloured blocks, testimonial band → recognition slider, consultation card pulled into the band, footer). The press marquee between steps and about is the one SACH element in the flow.
- About = /about-us (dotted banner + 1170×500 photo, about row, centred philosophy + 3 features, olive band with numbered qualifications + Netram's story accordion, progress bars + the India map as a CSS mask, 4-up cards used as the clinic gallery because the PRD has no named panel).
- Expertise = /departments (circle hero, 6 specialty cards whose "Learn more" opens an in-card accordion instead of a subpage), /our-process rows with alternating paper bands for the career timeline (numbers = years, plus 50+ staff and 24 states), the "high quality" list section for the Gold Medal, the /our-doctors workflow band for academics + the STAIRS chair, /faq cards for the 26 awards (10 shown, "Show all"), /news cards for press (text-only: no press photos supplied), the 2-photo CTA block.
- Foundation = /about-us banner + about row, the Home counter card with 5 figures, inline interactive India map (hover titles, 17 named states shaded on reveal in three waves), /departments cards for the 9 projects, list section for Eye Maitri, 3-column gallery + lightbox, partner marquee, Home blocks for Donate / Volunteer / Partner, CTA photos as the Foundation contact strip.
- Contact = /contact-us (banner, consultation card with the full enquiry form, 3 feature cards) + click-to-load map row + /faq cards.

### Decisions and fixes while building
- The link-arrow icon was set `position: static`, so its absolutely positioned chevron escaped to the top-left of the nearest positioned ancestor and rendered as a stray "›" on every page. Fixed by keeping it `position: relative`.
- `india.svg` had unescaped ampersands ("Jammu & Kashmir"): fine inlined in HTML, fatal as an XML image, so the CSS mask rendered blank. Escaped in the file and in `tools/make-map.py`; `<title>` per state added for native hover tooltips.
- Error-message `<p>`s under form fields inherited the 15px paragraph margins and spread the form; now `margin: 0` and hidden when empty.
- The mobile hero portrait collapsed to zero width (a column-flex child sized only by `max-width`); given an explicit 70% width.
- Progress bars restructured to label / number / track so the number sits under the bar at right on phones, as Medic does.
- Shared inner-page rules (banner photo, about row, `.centre`, `.todo`, `.bullets`, `.btn--amber`, the link-style accordion button) live once in `components.css`; page files hold only placements.
- Tap targets: link-arrows and the link-style accordion buttons have `min-height: 24px`, the consent checkbox is 24px, inline links carry 2px vertical padding.
- `.strip` marquee moved to components (Home press, Foundation partners).
- Photos regenerated untreated (`TREAT = "none"`); Medic uses natural photography.
- Fraunces and Satoshi removed; Poppins only.

### Content notes
- Facts unchanged from Pass 2 (all PRD-sourced). New `TODO:` markers only where a Medic slot needed a fact the PRD lacks: FVEIRC expansion ("Fellowship" only), Netram Empower, Eye Maitri coverage, procedure lists, the seven unnamed states, the MAMC year, the IPCL medal year, clinic timings, emergency contact, second location.
- Bars on About are decorative widths (as Medic's are): 14 years = 100%, 50+ staff = 84%, 24 states = 86% (24 of 28).

### Verified (real Chrome, playwright-cli)
- Per-page side-by-side drift pass at 1440 and 390 for Home, About, Expertise, Foundation, Contact.
- Whole-site sweep (`webcheck.js`) at 1440 / 768 / 390: 0 horizontal overflow, 0 broken images, 0 console errors, 1 h1 per page; the only flags were the tap targets above (fixed) and a screen-reader-only heading reported as "covered" (it is clipped by design).
- Every `src`/`srcset` audited against disk (two references to a non-existent `eye-mela-740.jpg` caught this way).
- EKG scroll scrub on the Expertise timeline measured at 0 → 0.97 across the heading block.
- Lighthouse 12 mobile (simulated 4G, uncompressed local server): Home 97 · About 95 · Expertise 94 · Foundation 93 · Contact 98 for Performance; Accessibility, Best Practices and SEO are 100 on every page. CLS 0 (Contact 0.003), TBT 0ms, LCP 1.9–2.7s. Remaining perf flags are speed-index / LCP on the photo-heavy pages; the .htaccess gzip will help on real hosting.

### Not verified here
- iOS Safari / Android Chrome on real devices; the form endpoint (stub).

---

## Pass 1 — design plan (16 Sep 2026) — rejected direction, kept for the record

### Measured, not assumed
- Logo colours from the JPEG (pixel mode): eye-mark olive `#5E6A42`, wordmark moss `#3C4632`, iris `#383434`. PRD hexes (`#5C6B3C`, `#3A4526`, `#141414`) replaced. Iris is warm charcoal, not black.
- Olive on white = 5.81:1 → passes AA. Sage (2.51) and amber (2.44) fail as text → non-text / fill-only tokens. Olive on moss = 1.71:1 → focus rings on moss grounds are paper.
- Deck images: largest are Canva stock (chalkboard texture, gold trophy, stethoscope) — banned. Real, usable: p2 outdoor portrait 1361×2420 (hero), p4 facade 1116×1128, p30 Roshini screening 960×832, p7 CII 1200×1600, p8 IPCL 768×1024, p27 TEDx 1033×1836, p12 IIRSI 1080×566. Many project photos exist only inside Canva poster composites → crop the photo region.

### Client still owes (PRD §14 + found in Pass 1)
1. Vector logo (AI/SVG/EPS) — the mark is currently rebuilt from the JPEG's measured geometry.
2. Vertical hero portrait (`_B7A0292.JPG` in Drive folder 1 is unreadable from our side) — deck p2 is the fallback.
3. OT, consultation and clinic photography; project-wise field photography foldered by project.
4. Clean partner logos — until then partners are set as text.
5. Award and press photographs at usable resolution.
6. Eye Maitri programme details; Netram Empower description.
7. Confirmed surgical-volume figure (not displayed until confirmed).
8. The 7 states beyond the 17 named in the deck (claim is 24).
9. Timeline years: MAMC senior residency, the IPCL gold medal.
10. Clinic timings; confirmation of which addresses are listed.
11. Dedicated enquiry email; WhatsApp business number confirmation.
12. Domain, hosting credentials, form endpoint choice (PHP mail / Web3Forms).

## Pass 2 — first build (16 Sep 2026) — rejected, kept for the record
The "Snellen chart" editorial build: Fraunces/Satoshi, a centred chart hero, full-bleed named-line grid, baked duotone photo treatments, GSAP + Lenis loaded after `load`. It passed its own verification (Lighthouse 90–99, adversarial review of 64 findings) and was rejected on direction, not quality. Two findings from its review still apply and are kept in Pass 3: audit every `srcset` candidate against disk (a `DPR-1` sweep cannot see a missing retina file), and the fact corrections pulled back to PRD wording ("then Chief Minister" dropped, oxygen cylinders not concentrators in the photographs, Chashma Bus not CSR-funded, GK-2 as the contact address with C.R. Park as the centre).
