"""Web sizes for the client's Drive photographs (originals/drive/*.jpg).
No cropping: EXIF orientation applied, then resized to the listed widths. Writes assets/img/dr-<slug>-<w>.jpg and .webp."""
import os, glob
from PIL import Image, ImageOps
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, "originals", "drive"), os.path.join(ROOT, "assets", "img")
WIDTHS = {"default": (480, 800, 1200), "portrait": (480, 800, 1000)}
for path in sorted(glob.glob(os.path.join(SRC, "*.jpg"))):
    slug = os.path.splitext(os.path.basename(path))[0]
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    w, h = im.size
    widths = WIDTHS["portrait"] if h > w else WIDTHS["default"]
    for tw in widths:
        if tw > w: continue
        r = im.resize((tw, round(h * tw / w)), Image.LANCZOS)
        r.save(os.path.join(OUT, f"dr-{slug}-{tw}.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
        r.save(os.path.join(OUT, f"dr-{slug}-{tw}.webp"), "WEBP", quality=78, method=6)
    print(f"dr-{slug}: {w}x{h} -> {widths}")
