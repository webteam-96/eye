# Ivory ground + new treatment photos

**Date:** 19 Sep 2026 · **Requested by:** Dr. Anchal Gupta via Kaizen Infotech
**Feedback being addressed:** "the website looks more for a dermatologist" — change the white background; replace some "What I treat" pictures with real clinic photographs.

Scope decided with the client's agency: **brand colours (lavender + pink) stay**; only the page ground changes, plus three named photo swaps. Ground colour **warm ivory `#FAF6EE`** was chosen from three live-tinted previews (ivory / lavender wash / pale sage) screenshotted on 19 Sep 2026.

## 1. Ground colour

Three CSS edits; no HTML changes; all six pages (incl. 404) inherit.

| File | Change |
|---|---|
| `assets/css/tokens.css` | New token `--ground: #FAF6EE;` with a dated comment. Contrast note: body grey `#707070` on it is 4.6:1 (AA for 16px text); `--rose` ≈ 6.6:1; `--amber-text` ≈ 5.7:1 — all still pass. |
| `assets/css/base.css` | `body { background: var(--ground) }` (was `var(--white)`). |
| `assets/css/components.css` | `.navbar` and the mobile `.nav-menu` dropdown: `var(--white)` → `var(--ground)` so the header doesn't sit as a white stripe. |

Left as `--white` on purpose: cards, stats, consultation card, FAQ cards, inputs, hero floating card — they now lift off the ivory ground. Lavender bands, footer, `--paper` washes, buttons: untouched. `.section--light` (#F4F3EE) is defined but used by no page — no conflict; leave it.

## 2. Treatment photos (Home "What I treat" + Expertise specialty cards)

Three tiles change on **both** pages; Cataract, Retina and Comprehensive keep their photos.

| Tile | Source (client-supplied, in `originals/`) | New asset name | Widths |
|---|---|---|---|
| Cornea and refractive | `corneal condition .png` (960×627 RGBA — slit-lamp exam, scan screens) | `dr-cornea-2` | 480, 800 |
| Glaucoma | `Glaucoma.jpg` (4032×3024 — Dr. Anchal with patient beside slit lamp) | `dr-glaucoma-2` | 480, 800, 1200 |
| Children and refractive error | `Children and refractive error.jpg` (1600×900 — young girl examined at slit lamp) | `dr-child-exam` | 480, 800, 1200 |

Pipeline (per README "Swapping in real images"): copy originals into `originals/` (gitignored), add three `SOURCES` entries to `tools/prepare-images.py` (file path, crop box tuned per photo, aspect 3/2, tier "A", `TREAT` stays `"none"`), run the script, reference only widths that exist on disk.

**Small tool improvement** (needed to avoid regenerating every deck asset from the PDF): `prepare-images.py` gains
- optional argv name filter (`python tools/prepare-images.py dr-cornea-2 …` processes only those entries; no args = all, unchanged),
- lazy imports (`fitz` only when a source is a PDF xref, `numpy` only when a treatment tier runs) so a filtered run needs Pillow alone,
- `manifest.json` merge (update processed entries, keep the rest) instead of overwrite.

HTML updates — `index.html` lines 214/216/219 and `expertise.html` lines 103/105/108: `src`, `srcset`, and alt text rewritten to describe the actual scenes. `sizes`, `width`/`height` attributes unchanged (370×247 / 373×249). New file names bust the 1-year image cache.

Cleanup: delete `dr-cornea-*` and `dr-glaucoma-*` from `assets/img` (referenced nowhere else after the edit — verified by grep). **Keep `roshini-*`** (still used on `foundation.html` and `index.html:194`).

## 3. Verification & docs

- Real Chrome, all six pages at 1440 and 390: ivory ground everywhere with no leftover white strips; new photos render crisp; every `src`/`srcset` audited against disk; zero console errors.
- Screenshot set saved for forwarding to Dr. Anchal.
- README: palette paragraph gains the ivory-ground decision (dated); image section notes the three new assets.
- One commit at the end (message in the repo's style).

## Out of scope

Brand colour changes, the other three tile photos, the remaining 14 Drive-folder photos (kept for future sections), form endpoint, deployment.
