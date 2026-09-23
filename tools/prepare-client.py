"""Web sizes for the photographs the client supplied in the Drive folder "Dr. Anchal Website Images"
(originals/client/*). Each entry names the site asset base it replaces, the source file, the aspect the
slot needs, where to anchor the crop, and the widths the HTML asks for. Writes assets/img/<base>-<w>.jpg
(and .webp where the page already uses one)."""
import os, sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, "originals", "client"), os.path.join(ROOT, "assets", "img")

#   base            source                                   aspect  anchor  widths          webp
JOBS = [
    # base                source                                    aspect anchor  widths            webp
    ("roshini",            "project-roshni-4.jpg",                    1.5,  0.35, (480, 800),        True),
    ("roshini-school",     "project-roshni-2.jpg",                    2.0,  0.15, (800, 1440),       True),
    ("mission66",          "mission-6-6-3.jpg",                       1.5,  0.50, (480, 800),        True),
    ("mission66-b",        "mission-6-6.jpg",                         1.5,  0.50, (480, 780),        True),
    ("nayan-hans",         "nayan-hans.jpg",                          1.5,  0.50, (480, 800),        True),
    ("medgate",            "medgate.png",                             1.45, 0.30, (480, 800),        False),
    ("transgender",        "transgender.jpg",                         1.5,  0.00, (480, 800),        True),
    ("chashma-bus",        "chashma-bus.jpg",                         1.5,  0.50, (464,),            True),
    ("eye-maitri",         "eye-maitri-2.png",                        1.5,  0.50, (480, 800, 1200),  True),
    ("eye-maitri-b",       "eye-maitri.png",                          1.5,  0.50, (480, 800, 1200),  True),
    ("cii",                "cii-healthcare-summit-panel-2025.jpg",    0.898, 0.60, (480, 800, 1200),  False),
    ("gandhi-samman",      "mahatma-gandhi-samman-bangkok-2017.jpg",  None, 0.50, (480, 800, 960),   False),
    ("bw40",               "40-under-40.jpg",                         0.9,  0.46, (480, 800),        False),
    ("hsbc",               "future-female-3.jpg",                     0.9,  0.50, (480, 800, 1200),  False),
    ("fff-stage",          "future-female.jpg",                       0.9,  0.60, (480, 800, 1200),  False),
    ("fff-close",          "future-female-2.png",                     0.9,  0.50, (480, 800),        False),
    ("roshni-reg",         "project-roshni.jpg",                      1.5,  0.50, (480, 800),        True),
    ("roshni-cards",       "project-roshni-3.jpg",                    1.5,  0.45, (480, 800, 1200),  True),
    ("roshni-class",        "project-roshni-2.jpg",                    1.5,  0.15, (480, 800, 1200),  True),
    ("team-banner",         "team.jpg",                                2.0,  0.85, (800, 1440, 2400), True),
    ("team-clinic",         "team-2.jpg",                              1.48, 0.50, (480, 800, 1200),  True),
    ("garima",             "fusion.jpg",                              1.5,  0.00, (480, 800, 1200),  True),
    ("ipcl-b",              "ipcl-gold-medal-2.jpg",                   1.5,  0.40, (480, 760),        False),
    ("womens-era",         "womens-era.png",                          None, 0.50, (480, 900, 1400, 2000), True),
    ("ot-microscope",      "ot-4.jpg",                                None, 0.50, (480, 800),        True),
    ("ot-laser",           "ot-3.jpg",                                None, 0.50, (480,),            True),
    ("hoa",                "ipcl-gold-medal.jpg",                     2.0,  0.50, (480, 800, 960),   False),
    ("dr-recognition-bg",  "future-female.jpg",                       2.045, 0.40, (480, 800, 1440, 2400), False),
]

def crop(im, aspect, anchor):
    """Cut the largest window of the wanted aspect. anchor 0 = top/left edge, 0.5 = centre, 1 = bottom."""
    if aspect is None:
        return im
    w, h = im.size
    if w / h > aspect:                      # too wide: trim the sides
        nw = round(h * aspect)
        x = round((w - nw) * anchor)
        return im.crop((x, 0, x + nw, h))
    nh = round(w / aspect)                  # too tall: trim top/bottom
    y = round((h - nh) * anchor)
    return im.crop((0, y, w, y + nh))

only = set(sys.argv[1:])
for base, src, aspect, anchor, widths, webp in JOBS:
    if only and base not in only:
        continue
    path = os.path.join(SRC, src)
    im = crop(ImageOps.exif_transpose(Image.open(path)).convert("RGB"), aspect, anchor)
    w, h = im.size
    made = []
    for tw in widths:
        if tw > w:
            continue
        r = im.resize((tw, round(h * tw / w)), Image.LANCZOS)
        r.save(os.path.join(OUT, f"{base}-{tw}.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
        if webp:
            r.save(os.path.join(OUT, f"{base}-{tw}.webp"), "WEBP", quality=78, method=6)
        made.append(f"{tw}x{r.size[1]}")
    print(f"{base:<18} <- {src:<40} {w}x{h} -> {', '.join(made) or 'NOTHING (source too small)'}")
