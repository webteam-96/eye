# Ivory Ground + Treatment Photos Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Change the site's page ground from white to warm ivory `#FAF6EE` and swap three "What I treat" photos (Cornea, Glaucoma, Children) for client-supplied clinic photographs on Home and Expertise.

**Architecture:** Static HTML/CSS site, no build step. The ground colour is one new token consumed by `body`, `.navbar` and `.nav-menu`; everything else keeps its explicit white. Photos go through the repo's own `tools/prepare-images.py` pipeline (crop to 3∶2, emit `-<w>.jpg` + `.webp`), which gains an argv name-filter so a run doesn't regenerate the whole deck.

**Tech Stack:** HTML5/CSS3, Python 3 + Pillow (tooling only), `python -m http.server` for preview, Chrome for verification.

## Global Constraints

- Brand colours are **unchanged**: `--rose #5E4B9E`, `--amber #D6246E`, all tokens except the new `--ground`.
- Ground colour is exactly `#FAF6EE` (approved 19 Sep 2026).
- Never reference an image width that is not on disk (README rule).
- `sizes`, `width`, `height` attributes on the six edited `<img>` tags stay as they are (370×247 Home, 373×249 Expertise).
- Tile `<img>` tags reference `.jpg` only (existing pattern); `.webp` twins are still generated for future use.
- Commit messages in the repo's style: sentence-case clauses joined by semicolons, no `feat:` prefixes; end with the `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` footer.
- There is no automated test suite in this repo; each task's test cycle is the stated CLI/browser verification, run for real, output read before claiming success.
- Local preview: `python -m http.server 8090 --bind 127.0.0.1` from the repo root (check whether it is already running first: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8090/`).

## File Structure

- Modify `assets/css/tokens.css` — add the `--ground` token (single source of truth for the colour).
- Modify `assets/css/base.css` — `body` ground.
- Modify `assets/css/components.css` — `.navbar`, `.nav-menu` grounds.
- Modify `tools/prepare-images.py` — lazy deps, argv filter, manifest merge, 3 new `SOURCES` entries.
- Create `originals/{Glaucoma.jpg, corneal condition .png, Children and refractive error.jpg}` (gitignored source photos).
- Create `assets/img/dr-cornea-2-{480,800}.{jpg,webp}`, `assets/img/dr-glaucoma-2-{480,800,1200}.{jpg,webp}`, `assets/img/dr-child-exam-{480,800,1200}.{jpg,webp}` (generated, committed).
- Modify `index.html:214,216,219` and `expertise.html:103,105,108` — the six `<img>` tags.
- Delete `assets/img/dr-cornea-*` and `assets/img/dr-glaucoma-*` (old widths, both formats).
- Modify `README.md` — record the ivory ground decision and the three new assets.

---

### Task 1: Warm ivory page ground

**Files:**
- Modify: `assets/css/tokens.css:16` (after `--white`)
- Modify: `assets/css/base.css:11`
- Modify: `assets/css/components.css:7,28`

**Interfaces:**
- Produces: CSS custom property `--ground` (`#FAF6EE`), used by later verification; no code interfaces.

- [ ] **Step 1: Add the token**

In `assets/css/tokens.css`, directly under the line `  --white: #FFFFFF;`, add:

```css
  --ground: #FAF6EE;              /* page ground: warm ivory in place of white (client, 19 Sep 2026); --grey body text on it 4.6:1, AA */
```

- [ ] **Step 2: Point body at it**

In `assets/css/base.css` line 11, change only the background value:

```css
body { margin: 0; background: var(--ground); color: var(--ink); font: 400 var(--p) / 20px var(--font); -webkit-font-smoothing: antialiased; overflow-x: hidden; }
```

- [ ] **Step 3: Match the navbar and mobile menu**

In `assets/css/components.css`:
- Line 7: `.navbar { background: var(--white); …` → `.navbar { background: var(--ground); …` (rest of the rule untouched).
- Line 28 (inside the `@media` block): `.nav-menu { … background: var(--white); …` → `background: var(--ground);` (rest untouched).

- [ ] **Step 4: Verify in the browser**

Ensure the local server is up (Global Constraints), hard-reload `http://127.0.0.1:8090/` in the Chrome tab (`Ctrl+Shift+R` or re-navigate), screenshot the hero.
Expected: navbar + hero ground are ivory (visibly warm next to the white "Reach me" card); the floating card and buttons are still pure white surfaces.
Then scroll to the step-cards section and screenshot: white cards visibly lift off the ivory ground. Check the console for errors (there must be none).

- [ ] **Step 5: Commit**

```bash
git add assets/css/tokens.css assets/css/base.css assets/css/components.css
git commit -m "Warm ivory page ground in place of white; navbar and mobile menu sit on the same ground

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 2: Prepare the three clinic photographs

**Files:**
- Create: `originals/Glaucoma.jpg`, `originals/corneal condition .png`, `originals/Children and refractive error.jpg` (copies from `C:\Users\Kalpesh\Downloads\`; `originals/` is gitignored)
- Modify: `tools/prepare-images.py`
- Create (generated): `assets/img/dr-cornea-2-{480,800}.{jpg,webp}`, `assets/img/dr-glaucoma-2-{480,800,1200}.{jpg,webp}`, `assets/img/dr-child-exam-{480,800,1200}.{jpg,webp}`

**Interfaces:**
- Produces: the asset base names `dr-cornea-2` (widths 480, 800), `dr-glaucoma-2` (480, 800, 1200), `dr-child-exam` (480, 800, 1200) — Task 3's `<img>` tags reference exactly these.
- Consumes: nothing from Task 1.

- [ ] **Step 1: Copy the originals in**

```powershell
Copy-Item "C:\Users\Kalpesh\Downloads\Glaucoma.jpg","C:\Users\Kalpesh\Downloads\corneal condition .png","C:\Users\Kalpesh\Downloads\Children and refractive error.jpg" -Destination originals\
```

- [ ] **Step 2: Make the script runnable without the deck deps**

In `tools/prepare-images.py` (current env has Pillow but not `numpy`/`pymupdf`; `TREAT` is `"none"` so neither is exercised for file sources):

a. Delete the two top-level imports `import numpy as np` and `import fitz` (keep `io, json, os, sys` and the PIL imports).

b. Replace the three numpy constants with plain lists:

```python
OLIVE = [0x5E, 0x6A, 0x42]
MOSS = [0x3C, 0x46, 0x32]
PAPER = [0xF6, 0xF4, 0xEC]
```

c. First lines of `load()` become:

```python
def load(src):
    if isinstance(src, str):
        return Image.open(os.path.join(ROOT, src)).convert("RGB")
    import fitz                      # deck extraction only; not needed for file sources
    doc = fitz.open(PDF)
```

d. Give the treatment functions local numpy imports and scaled constants (they only run when `TREAT != "none"`):

```python
def soft_light(cb, cs):
    import numpy as np
    d = np.where(cb <= .25, ((16 * cb - 12) * cb + 4) * cb, np.sqrt(cb))
    return np.where(cs <= .5, cb - (1 - 2 * cs) * cb * (1 - cb), cb + (2 * cs - 1) * (d - cb))


def tier_a(im):
    import numpy as np
    im = ImageEnhance.Color(im).enhance(.85)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    a = np.asarray(im).astype(np.float64) / 255
    a = a * .75 + soft_light(a, np.array(OLIVE) / 255) * .25
    return Image.fromarray((np.clip(a, 0, 1) * 255).round().astype(np.uint8))


def tier_b(im):
    import numpy as np
    g = np.asarray(ImageEnhance.Contrast(im.convert("L")).enhance(1.1)).astype(np.float64) / 255
    a = np.array(MOSS) / 255 + (np.array(PAPER) / 255 - np.array(MOSS) / 255) * g[..., None]
    return Image.fromarray((np.clip(a, 0, 1) * 255).round().astype(np.uint8))
```

e. In `main()`, add the argv filter and manifest merge (replace the first lines and the final dump):

```python
def main():
    os.makedirs(OUT, exist_ok=True)
    names = sys.argv[1:]
    unknown = [n for n in names if n not in SOURCES]
    if unknown:
        sys.exit(f"unknown source name(s): {', '.join(unknown)}")
    todo = {k: v for k, v in SOURCES.items() if not names or k in names}
    mpath = os.path.join(OUT, "manifest.json")
    manifest = json.load(open(mpath)) if os.path.exists(mpath) else {}
    for name, (src, box, aspect, tier, widths) in todo.items():
        ...                          # loop body unchanged
    json.dump(manifest, open(mpath, "w"), indent=1)
```

(The loop body itself is untouched; only `SOURCES.items()` → `todo.items()` and the manifest lines change.)

- [ ] **Step 3: Add the three SOURCES entries**

At the end of the `SOURCES` dict:

```python
    # client's clinic photographs, 19 Sep 2026 (WhatsApp batch; originals/ )
    "dr-cornea-2":   ("originals/corneal condition .png",             (0, 0, 1, 1), 3/2, "A", (480, 800)),
    "dr-glaucoma-2": ("originals/Glaucoma.jpg",                       (0, 0, 1, 1), 3/2, "A", W3),
    "dr-child-exam": ("originals/Children and refractive error.jpg",  (0, 0, 1, 1), 3/2, "A", W3),
```

- [ ] **Step 4: Run the filtered prep and check it fails/succeeds honestly**

```bash
python tools/prepare-images.py dr-cornea-2 dr-glaucoma-2 dr-child-exam
```

Expected output: three lines (name, tier, source width, per-width KB), no traceback. Then confirm exactly 16 new files exist:

```bash
ls assets/img/dr-cornea-2-* assets/img/dr-glaucoma-2-* assets/img/dr-child-exam-*
```

Expected: `dr-cornea-2-{480,800}`, `dr-glaucoma-2-{480,800,1200}`, `dr-child-exam-{480,800,1200}` in both `.jpg` and `.webp`. Also run `python tools/prepare-images.py no-such-name` → exits with `unknown source name(s): no-such-name`.

- [ ] **Step 5: Eyeball the crops**

Read (view) `assets/img/dr-cornea-2-800.jpg`, `assets/img/dr-glaucoma-2-800.jpg`, `assets/img/dr-child-exam-800.jpg`.
Expected: no face is clipped by the 3∶2 crop. The crop helper trims sides when too wide (children photo: 125px each side of 1600) and keeps the *top* when too tall (glaucoma photo: bottom 336 of 3024 rows go). If a face is cut, nudge the crop box fractions (e.g. shift the children entry to `(.02, 0, .98, 1)` or the glaucoma entry to `(0, .05, 1, 1)`), re-run Step 4, re-check.

- [ ] **Step 6: Verify manifest merged, not clobbered**

```bash
python -c "import json; m = json.load(open('assets/img/manifest.json')); print(len(m), 'entries'); print({k: m[k]['widths'] for k in ('dr-cornea-2','dr-glaucoma-2','dr-child-exam')})"
```

Expected: entry count is the pre-existing count + 3 (run `git show HEAD:assets/img/manifest.json | python -c "import json,sys; print(len(json.load(sys.stdin)))"` for the baseline if unsure), and the three new entries list the expected widths.

- [ ] **Step 7: Commit**

```bash
git add tools/prepare-images.py assets/img/dr-cornea-2-* assets/img/dr-glaucoma-2-* assets/img/dr-child-exam-* assets/img/manifest.json
git commit -m "Three clinic photographs prepared for the treatment grids; prepare-images runs a named subset without the deck deps

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 3: Point the six tiles at the new photographs

**Files:**
- Modify: `index.html:214,216,219`
- Modify: `expertise.html:103,105,108`
- Delete: `assets/img/dr-cornea-{480,800,1200}.*`, `assets/img/dr-glaucoma-{480,800,1200}.*`
- Modify: `README.md`

**Interfaces:**
- Consumes: asset names `dr-cornea-2` (480/800), `dr-glaucoma-2` (480/800/1200), `dr-child-exam` (480/800/1200) from Task 2.

- [ ] **Step 1: index.html — Cornea tile (line 214)**

Replace the `<img …>` inside the first tile with (only `src`, `srcset`, `alt` change; note the cornea srcset has **no 1200w** — the source is 960px wide):

```html
<img src="assets/img/dr-cornea-2-800.jpg" srcset="assets/img/dr-cornea-2-480.jpg 480w, assets/img/dr-cornea-2-800.jpg 800w" sizes="(max-width: 991px) 100vw, 370px" width="370" height="247" alt="Dr. Anchal Gupta examining a young patient at the slit lamp, the scans on the screens beside them" loading="lazy" decoding="async">
```

- [ ] **Step 2: index.html — Glaucoma tile (line 216)**

```html
<img src="assets/img/dr-glaucoma-2-800.jpg" srcset="assets/img/dr-glaucoma-2-480.jpg 480w, assets/img/dr-glaucoma-2-800.jpg 800w, assets/img/dr-glaucoma-2-1200.jpg 1200w" sizes="(max-width: 991px) 100vw, 370px" width="370" height="247" alt="Dr. Anchal Gupta with a patient beside the slit lamp after a glaucoma check-up" loading="lazy" decoding="async">
```

- [ ] **Step 3: index.html — Children tile (line 219)**

```html
<img src="assets/img/dr-child-exam-800.jpg" srcset="assets/img/dr-child-exam-480.jpg 480w, assets/img/dr-child-exam-800.jpg 800w, assets/img/dr-child-exam-1200.jpg 1200w" sizes="(max-width: 991px) 100vw, 370px" width="370" height="247" alt="Dr. Anchal Gupta examining a young girl at the slit lamp" loading="lazy" decoding="async">
```

- [ ] **Step 4: expertise.html — the same three cards (lines 103, 105, 108)**

Same three `<img>` replacements as Steps 1–3 but with the Expertise dimensions and `sizes` kept: `sizes="(max-width: 991px) 100vw, 373px" width="373" height="249"`. Alt texts identical to Steps 1–3. (Line 103 = cornea, 105 = glaucoma, 108 = children/roshini.)

- [ ] **Step 5: Delete the superseded assets — after proving they are unreferenced**

```bash
grep -rn "dr-cornea-[0-9]\|dr-glaucoma-[0-9]" --include="*.html" --include="*.css" --include="*.js" .
```

Expected: no matches (the `-[0-9]` keeps `dr-cornea-2-*` names from matching). Then:

```bash
rm assets/img/dr-cornea-480.* assets/img/dr-cornea-800.* assets/img/dr-cornea-1200.* assets/img/dr-glaucoma-480.* assets/img/dr-glaucoma-800.* assets/img/dr-glaucoma-1200.*
```

(If some of those widths/formats don't exist on disk, remove only what's there — `ls assets/img/dr-cornea-* assets/img/dr-glaucoma-*` first. Do **not** touch `roshini-*`: still used on `foundation.html` and `index.html:194`.)

- [ ] **Step 6: Audit every referenced image against disk**

```bash
grep -ho 'assets/img/[^" ]*\.\(jpg\|webp\|svg\|png\)' *.html | sort -u | while read f; do [ -f "$f" ] || echo "MISSING: $f"; done
```

Expected: no output.

- [ ] **Step 7: README**

In `README.md`: append to the design-direction paragraph (the sentence listing what differs from the reference) a note — `the page ground is warm ivory #FAF6EE in place of Medic's white (client, 19 Sep 2026)`. In the `img/` line of the file tree, note the three client clinic photographs (`dr-cornea-2`, `dr-glaucoma-2`, `dr-child-exam`, originals in `originals/`, 19 Sep 2026 batch).

- [ ] **Step 8: Verify both grids in the browser**

Hard-reload `http://127.0.0.1:8090/` and `http://127.0.0.1:8090/expertise.html`; scroll to "What I treat" / the specialty cards; screenshot each.
Expected: the three new photographs render (cornea = exam with scan screens, glaucoma = doctor and patient beside slit lamp, children = young girl at slit lamp); the other three tiles unchanged; no broken-image icons; console clean. Run in the page console via the JS tool: `[...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.currentSrc)` → `[]` on both pages.

- [ ] **Step 9: Commit**

```bash
git add index.html expertise.html README.md
git rm --cached --ignore-unmatch assets/img/dr-cornea-480.jpg  # only if git still tracks deleted files; otherwise plain git add -A assets/img
git add -A assets/img
git commit -m "Cornea, glaucoma and children tiles carry the client's clinic photographs on Home and Expertise; superseded assets removed; ivory ground recorded in the README

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 4: Full-site verification + client screenshots

**Files:** none modified (fixes loop back into the task that owns the file).

**Interfaces:**
- Consumes: everything above.

- [ ] **Step 1: Six pages, desktop width**

For each of `/`, `/about.html`, `/expertise.html`, `/foundation.html`, `/contact.html`, `/404.html`: load in Chrome, screenshot the top, scroll through once.
Expected on every page: ivory ground everywhere white used to be (no stray white strips between sections, no white navbar), cards/forms still white, lavender bands and footer unchanged, console has zero errors.

- [ ] **Step 2: Narrow width**

Resize the Chrome window to its narrowest (or 768px) so the ≤991px styles apply; on `/` open the hamburger menu.
Expected: the dropdown menu ground is ivory (matches the bar), tiles stack full-width, nothing overflows horizontally (`document.documentElement.scrollWidth === document.documentElement.clientWidth` in the console).

- [ ] **Step 3: Save the client screenshot set**

Save screenshots (hero, "What I treat" grid, Expertise cards — with `save_to_disk`) and list the file paths in the final report so Kaizen can forward them to Dr. Anchal on WhatsApp.

- [ ] **Step 4: Verify clean tree and report**

`git status` → clean (everything committed in Tasks 1–3). Report: what changed, the commit hashes, screenshot paths, and the reminder that `?v=<date>` cache-busting on CSS links applies when deploying (per README) — new image filenames need nothing.

## Self-Review

- **Spec coverage:** §1 ground → Task 1; §2 photos/pipeline/HTML/cleanup → Tasks 2–3; §3 verification/README/commits → Tasks 3–4. No gaps.
- **Placeholders:** none — every step carries exact code, commands, or expected output.
- **Type/name consistency:** `--ground`, `dr-cornea-2`, `dr-glaucoma-2`, `dr-child-exam` used identically across Tasks 1–4; widths (480/800 vs 480/800/1200) consistent between Task 2 SOURCES, Task 2 checks, and Task 3 srcsets.
