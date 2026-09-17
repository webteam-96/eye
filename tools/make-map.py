"""Asset prep: build assets/img/india.svg (inline-able) from the DataMeet
India states shapefile (CC-BY 2.5 India, https://github.com/datameet/maps).

    python tools/make-map.py <dir containing Admin2.shp>

Equirectangular projection with a cos(22deg) x-scale; rings simplified with
Douglas-Peucker at 0.06 degrees; islands under 0.02 sq-deg dropped.
"""
import html
import sys, os, math, re
import numpy as np, cv2, shapefile

SRC = os.path.join(sys.argv[1], "Admin2")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img", "india.svg")
LON0, LAT1, K = 68.0, 37.6, 20.0
KX = K * math.cos(math.radians(22))


def slug(s):
    return re.sub(r"[^a-z]+", "-", s.lower()).strip("-")


def ring_path(pts):
    a = np.array(pts, dtype=np.float32).reshape(-1, 1, 2)
    a = cv2.approxPolyDP(a, 0.06, True).reshape(-1, 2)
    if len(a) < 4:
        return ""
    xy = [((lon - LON0) * KX, (LAT1 - lat) * K) for lon, lat in a]
    return "M" + " ".join(f"{x:.1f} {y:.1f}" for x, y in xy) + "Z"


def ring_area(pts):
    a = np.array(pts); x, y = a[:, 0], a[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


sf = shapefile.Reader(SRC)
paths = []
for sr in sf.shapeRecords():
    name = sr.record[0]
    pts, parts = sr.shape.points, list(sr.shape.parts) + [len(sr.shape.points)]
    d = ""
    for i in range(len(parts) - 1):
        ring = pts[parts[i]:parts[i + 1]]
        if ring_area(ring) < 0.02:
            continue
        d += ring_path(ring)
    if d:
        paths.append(f'<path id="st-{slug(name)}" data-name="{html.escape(name, quote=True)}" d="{d}"><title>{html.escape(name)}</title></path>')
w, h = (97.6 - LON0) * KX, (LAT1 - 6.4) * K
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" class="india" aria-hidden="true" focusable="false">\n' + "\n".join(paths) + "\n</svg>\n"
open(OUT, "w", encoding="utf-8").write(svg)
print(OUT, os.path.getsize(OUT) // 1024, "KB", len(paths), "states")
