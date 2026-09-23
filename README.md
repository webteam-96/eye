# Dr. Anchal Gupta — website

Five static pages plus a 404. Custom HTML5 + CSS3 + vanilla ES modules. No build step, no npm install, no runtime dependencies: upload the folder over SFTP and it runs.

**Design direction (approved 16 Sep 2026):** the layout, components and type are [Medic 128](https://medic-128.webflow.io/) rebuilt one-to-one (home, about-us, departments, our-process, our-doctors band, faq, news, contact-us templates). Only three things differ from the reference: the content (from the PRD), the palette (saree gold `#9E6210` with a dark gold `#5C3707` for deep blocks, carnation pink `#D6246E` as the accent, bright gold `#D4912E` for lines on dark bands, near-black `#383434`; both colours sampled from the client's photograph on 18 Sep 2026; the logo keeps its original olive) and the photography; the page ground is warm ivory `#FAF6EE` in place of Medic's white (client, 19 Sep 2026). Motion comes from [Save a Child's Heart](https://25.saveachildsheart.org/): the electrocardiogram trace (drawn on load, under heading words, scrubbed by scroll on the Expertise timeline), the rise-and-fade reveals, the marquee strips, the card lift and image-zoom hovers, and the one-second preloader. `REFERENCE-TEARDOWN.md` holds the measured teardown of both references and the section-by-section mapping.

**To preview locally**, serve the folder rather than double-clicking `index.html` (browsers block ES modules from `file://`): `python -m http.server 8090` in this folder, then open http://127.0.0.1:8090/.

## Files

```
index.html          Home — Medic home: hero (client portrait in a rounded frame) + floating card, step cards, press marquee, about row, ring counters band, trust cards,
                    SACH-style expertise tile grid, accordion service, coloured blocks, recognition band + slider, consultation card
about.html          Medic about-us: dotted banner + photo, biography row, philosophy + 3 features, SACH-style qualifications band (EKG zig-zag),
                    olive band with Netram's story accordion, states band (interactive India map, stat cards, state chips), gallery cards
expertise.html      Medic about-us banner + departments + SACH timeline + our-doctors band: 6 specialty cards (accordion), pinned career
                    timeline sliding over an EKG line, Gold Medal list section, academics band, award year cards, press cards, CTA photos
foundation.html     Medic about-us banner, origin row, 5-figure counter card, interactive India map, 8 project cards, Eye Maitri
                    list section, field gallery + lightbox, Foundation CTA photos
contact.html        Medic contact-us: dotted banner, contact chips beside the live Google map, consultation card (full enquiry form), FAQ cards
404.html            Not-found page (noindex)
.htaccess           404 routing, MIME types, caching, gzip (Apache)
robots.txt, sitemap.xml
assets/
  css/tokens.css      Medic's measured system: colours, Poppins type scale (76/46/24/16), container 1200/15, section 120 (60 mobile),
                      radii 10/20/50/80, shadows, SACH easings and durations; mobile overrides at ≤991px
  css/base.css        @font-face (Poppins 400–700, Noto Devanagari for नेत्रम्), reset, headings, .container/.section/.row, .dots
  css/components.css  navbar + mobile menu, buttons (+stripes), link-arrow, hero (arch + card), steps, cards, counter card, accordions,
                      FAQ cards, coloured blocks, band + slider, consultation card + form, team/dept/feature cards, process rows,
                      banner + dots, progress bars, numbered list, CTA photos, footer, FAB, marquee strip, motion (.rv reveals, EKG, loader),
                      gallery + lightbox, mapbox
  css/pages/*.css     one file per page: section placements and the few page-only components (news cards, awards, India map states)
  js/main.js          boot: preloader (once per session, skippable), nav, motion, counters, lazy imports of gallery/form, FAB after 2s,
                      year + years-in-practice
  js/nav.js           mobile menu + trapFocus (shared with the lightbox)
  js/motion.js        IntersectionObserver reveals, EKG draw + scroll scrub, marquee, hero pointer parallax, slider, accordions, show-all
  js/counters.js      count-up once, Indian digit grouping
  js/gallery.js       lightbox: keyboard, swipe, focus trap
  js/form.js          validation, honeypot, the stubbed submit, ?type= pre-select
  fonts/              poppins-400/500/600/700.woff2 (Latin subsets), noto-devanagari.woff2
  img/                photographs: dr-*.{jpg,webp} from the client's Drive shoots (480/800/1200, uncropped, tools/prepare-drive.py),
                      dr-cornea-2, dr-glaucoma-2 and dr-child-exam are the client's clinic photographs for the cornea, glaucoma and
                      children tiles (originals in originals/, 19 Sep 2026 batch), the Foundation project and award
                      photographs from the client's "Dr. Anchal Website Images" Drive folder (originals/client,
                      tools/prepare-client.py, 23 Sep 2026 batch), the remaining deck photos (tools/prepare-images.py),
                      logo SVGs, india.svg, og.jpg, favicon.svg
tools/                asset-prep scripts (Python): prepare-drive.py and prepare-client.py size the client's photographs,
                      make-tedx-collage.py builds the 2026 award tile, prepare-logos.py normalises the partner logos.
                      Not needed to deploy or edit the site.
```

## Editing

- **Copy** lives in the HTML. Every page carries the same head block, navbar, footer and FAB; a change to those must be made in all six files (they were generated from `index.html`, so a diff against it shows the shared parts).
- **Sizes and colours** are the tokens in `tokens.css`. They are Medic's measured numbers; change them only if the reference changes.
- **Sections** are `<section class="section">` (padding-bottom 120) inside which sits one `.container` (1200 max, 15px gutters). Olive bands use `section--band`. Rows are flex: text column 585/597px + image column, stacking under 991px.
- **Heading stroke**: wrap one word in `<span class="stroke-word">word<svg class="ekg ekg--stroke">…</svg></span>` (copy an existing one).
- **Reveals**: add `class="rv"` (rise + fade) or `rv rv--fade` (fade only); `data-d="1|2|3"` staggers 300/600/900ms. Reduced motion shows everything at once.
- **Photos**: `<img>` with `width`/`height`, `srcset` where several widths exist (never reference a width that is not on disk), `loading="lazy"` below the fold.
- **Logo**: `tools/inject-svg.py` inlines the logo blocks at the `<!--LOCKUP-->`-style markers in every page (re-runnable). When the vector logo arrives, regenerate `assets/img/_logo-paths.json` and re-run.
- **India map**: `assets/img/india.svg` is both inlined (Foundation, `<!--INDIA-->`) and used as a CSS mask (About, Home band), so it must stay valid XML. `tools/make-map.py` regenerates it; the shaded states are the id list in `pages/foundation.css`.

## Swapping in real images

1. Drop the original in the project and add a line to `SOURCES` in `tools/prepare-images.py` (crop box as fractions, aspect, widths).
2. `python tools/prepare-images.py` writes `assets/img/<name>-<w>.webp` and `.jpg` (untreated; `TREAT = "none"`).
3. Reference them in the page. Needs Python 3 with `pillow` (and `pymupdf` only for deck extraction).

The hero (`hero-1000.webp`) is under the 250KB budget. **Still to replace** when the client's originals arrive: a vertical studio portrait, OT and clinic photographs, project-wise field photographs (several field images are crops from Canva posters at 460–800px and are soft at full width), award photographs at usable resolution, partner logos.

## The form endpoint

`assets/js/form.js`, function `sendEnquiry(data)` is a stub that resolves `{ ok: true }` after 600ms and logs the payload. Replace its body with a `fetch` to Web3Forms / Formspree / a PHP mailer (the comment shows both). `data.type` is one of `patient | corporate | foundation | media | other` and should drive the recipient. The honeypot field is `website`. `contact.html?type=corporate#enquiry` pre-selects the enquiry type (the Eye Maitri and Foundation links use this).

## Deployment

Upload everything except `tools/`, the PDF, `references/` and the `*.md` files. CSS/JS are cached for one day by `.htaccess`; after an edit either wait a day or append `?v=<date>` to the `<link>`/`<script>` paths. Then: point the domain, force HTTPS, replace `https://www.dranchalgupta.com/` in the canonical/OG tags, `sitemap.xml` and `robots.txt`; submit the sitemap in Search Console; test the form delivery.

## Verified (17 Sep 2026)

- Each page screenshotted at 1440 and 390 beside its Medic reference page and walked section by section; drift fixed (see NOTES.md, Pass 3).
- Real Chrome at 1440 / 768 / 390 on all six pages: 0 horizontal overflow, 0 broken images (every `src`/`srcset` audited against disk), 0 console errors, 1 `h1`.
- Lighthouse 12 mobile (17 Sep 2026): Performance 93–95 (Contact mid-80s because its Google map iframe is above the fold, at the client's request), Accessibility 100, Best Practices 100, SEO 100 on every page.
- Not tested here: iOS Safari and Android Chrome on real devices.

## Still needed from the client

Photographs (the Drive folders only cover the doctor herself; these sections use the deck's low-resolution crops until better files arrive): the Netram building and clinic interiors; each Foundation project (Roshini, Eye Mela, Chashma Bus, Nayan Hans, Mission 6/6, I Am 6/6, Transgender Medical Camp, Oxygen Sewa, Netram Empower); Eye Maitri corporate camps; awards and stage moments (Forbes India, TEDx, BW 40 Under 40, IPCL Gold Medal, CII, IIRSI, HOA); partner logos.

Facts that were removed from the pages because they were unconfirmed (nothing is shown until they arrive)

1. Domain in canonical / OG / sitemap / robots.
2. Clinic timings; whether consultations are only at E-98 Greater Kailash-2 or also at Netram, C.R. Park.
3. Emergency contact; what a patient should bring.
4. Netram Empower description; Eye Maitri coverage, formats and pricing; the canonical Eye Maitri URL.
5. The seven states beyond the seventeen named.
6. MAMC senior residency year; year and conferring body of the IPCL Gold Medal; Future Female Forward Award year; the FVEIRC expansion.
7. Full procedure list per specialty.
8. Form endpoint (`sendEnquiry`) and the recipient per enquiry type.
