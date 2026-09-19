"""Asset prep (not a build step): extract photographs from the profile deck,
crop to the site's fixed ratios, bake the photo treatment, write WebP + JPEG.

    python tools/prepare-images.py

Re-run when better originals arrive: add a SOURCES entry pointing at a file
instead of a PDF xref and the same crop/treatment applies.

Treatments (the CSS-equivalent is documented in README.md):
  A  her face, clinic, field portraits: saturate .85, contrast 1.05, olive soft-light at .25
  B  stages, crowds, awards:             moss -> paper duotone
"""
import io, json, os, sys
from PIL import Image, ImageEnhance

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "Dr Anchal Gupta Profile._20260822_001712_0000 (1).pdf")
OUT = os.path.join(ROOT, "assets", "img")
OLIVE = [0x5E, 0x6A, 0x42]
MOSS = [0x3C, 0x46, 0x32]
PAPER = [0xF6, 0xF4, 0xEC]

# name: (xref | path, crop box as fractions (l,t,r,b), aspect w/h, tier, widths)
TREAT = "none"   # "none" = natural photography (Medic 128 reference); "tiers" = olive treatments
W3 = (480, 800, 1200)
SOURCES = {
    "hero":            (78,   (0, .05, 1, .755),      4/5, "A", (480, 800, 1000, 1200)),
    "hero-square":     (78,   (0, .06, 1, .6225),     1,   "A", (480, 720)),
    "about-hero":      (87,   (0, 0, 1, 1),           3/2, "A", (480, 800, 1100)),
    "office":          (68,   (0, 0, 1, 1),           3/2, "A", (480, 800)),
    "desk":            (227,  (0, .075, 1, .68),      4/5, "A", (480, 600)),
    "facade":          (98,   (.1, 0, .9, 1),         4/5, "A", (480, 800)),
    "tedx-portrait":   (1342, (.03, .25, .97, .72),   3/2, "A", (480,)),
    "hsbc":            (254,  (0, 0, 1, 1),           4/5, "A", (480, 700)),
    "conference":      (146,  (0, 0, 1, 1),           4/5, "A", (480, 800, 1000)),
    "cii":             (135,  (0, .28, 1, .78),       3/2, "B", W3),
    "ipcl":            (141,  (0, .25, 1, .75),       3/2, "B", (480, 760)),
    "tedx-stage":      (1345, (0, .3, 1, .675),       3/2, "B", (480, 800, 1000)),
    "dos-podium":      (155,  (0, .1, 1, .94),        4/5, "B", (480, 800, 1000)),
    "dos-2023":        (151,  (.13, .46, .84, .86),   4/5, "B", (480, 600)),
    "iirsi":           (159,  (0, 0, 1, .954),        2,   "B", (480, 800, 1080)),
    "hoa":             (168,  (0, 0, 1, 1),           2,   "B", (480, 800, 1080)),
    "voh-stage":       (207,  (0, 0, 1, 1),           2,   "B", (480, 800, 1080)),
    "eye-institute":   (173,  (0, .05, 1, .915),      3/2, "B", (480, 800, 1080)),
    "bw40":            (212,  (0, .35, 1, .92),       4/5, "B", (480, 700)),
    "youth-india":     (185,  (.05, .19, .56, .485),  3/2, "B", (480, 800)),
    "gandhi-samman":   (185,  (.05, .53, .75, .86),   3/2, "B", (480, 800)),
    "csr-2019":        (200,  (.03, .215, .68, .53),  3/2, "B", (480, 750)),
    "roshini":         (301,  (0, .08, 1, .75),       3/2, "A", (480, 800, 960)),
    "roshini-school":  (1409, (0, .055, 1, .945),     2,   "B", (800, 1200, 1440)),
    "chashma-bus":     (311,  (.01, .72, .37, .90),   3/2, "A", (480,)),
    "eye-mela":        (1443, (0, .62, .66, .94),     3/2, "B", (480, 760)),
    "eye-mela-b":      (320,  (.02, .35, .98, .76),   3/2, "B", (480, 740)),
    "nayan-hans":      (331,  (.03, .205, .65, .50),  3/2, "B", (480, 800)),
    "nayan-hans-b":    (331,  (.03, .52, .65, .80),   3/2, "B", (480, 800)),
    "transgender":     (342,  (.36, .375, .99, .68),  3/2, "A", (480, 800)),
    "mission66":       (351,  (.245, .61, .83, .90),  3/2, "B", (480, 750)),
    "mission66-b":     (351,  (0, .385, .49, .60),    3/2, "B", (480, 630)),
    "iam66":           (1510, (0, 0, 1, 1),           1,   "A", (480,)),
    "oxygen":          (371,  (.06, .30, .48, .47),   1,   "B", (450,)),
    "oxygen-b":        (371,  (.06, .585, .48, .74),  3/2, "B", (450,)),
    # client's clinic photographs, 19 Sep 2026 (WhatsApp batch; originals/ )
    "dr-cornea-2":   ("originals/corneal condition .png",             (0, 0, 1, 1), 3/2, "A", (480, 800)),
    "dr-glaucoma-2": ("originals/Glaucoma.jpg",                       (0, 0, 1, 1), 3/2, "A", W3),
    "dr-child-exam": ("originals/Children and refractive error.jpg",  (0, 0, 1, 1), 3/2, "A", W3),
}


def load(src):
    if isinstance(src, str):
        return Image.open(os.path.join(ROOT, src)).convert("RGB")
    import fitz                      # deck extraction only; not needed for file sources
    doc = fitz.open(PDF)
    return Image.open(io.BytesIO(doc.extract_image(src)["image"])).convert("RGB")


def crop(im, box, aspect):
    w, h = im.size
    l, t, r, b = box[0] * w, box[1] * h, box[2] * w, box[3] * h
    cw, ch = r - l, b - t
    if cw / ch > aspect:            # too wide: trim sides
        nw = ch * aspect; l += (cw - nw) / 2; r = l + nw
    else:                            # too tall: trim top/bottom, keep upper part (faces)
        nh = cw / aspect; b = t + nh
    return im.crop((int(l), int(t), int(r), int(b)))


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
        im = crop(load(src), box, aspect)
        im = im if TREAT == "none" else (tier_a(im) if tier == "A" else tier_b(im))
        sw = im.size[0]
        done = []
        for w in widths:
            if w > sw and done:   # never upscale; keep the largest real size once
                break
            ww = min(w, sw)
            out = im.resize((ww, round(ww / aspect)), Image.LANCZOS)
            out.save(os.path.join(OUT, f"{name}-{ww}.webp"), "WEBP", quality=78, method=6)
            out.save(os.path.join(OUT, f"{name}-{ww}.jpg"), "JPEG", quality=80, optimize=True, progressive=True)
            done.append(ww)
        manifest[name] = {"widths": done, "aspect": aspect, "src_w": sw, "tier": tier}
        sizes = ", ".join(f"{w}:{os.path.getsize(os.path.join(OUT, f'{name}-{w}.webp'))//1024}K" for w in done)
        print(f"{name:16} {tier} {sw}px  {sizes}")
    json.dump(manifest, open(mpath, "w"), indent=1)


if __name__ == "__main__":
    main()
