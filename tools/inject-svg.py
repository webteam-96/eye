"""Asset prep: inline the logo/lash/map SVGs into the HTML pages at their placeholders.

    python tools/inject-svg.py

Placeholders (HTML comments) — leave them in place; the script replaces a placeholder
only when it is still present, and re-replaces a previously injected block that is
wrapped in <!--LOCKUP-->…<!--/LOCKUP--> markers, so re-running after a logo update works.
"""
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
P = json.load(open(os.path.join(IMG, "_logo-paths.json")))
lash = json.load(open(os.path.join(IMG, "_lash.json")))
india = open(os.path.join(IMG, "india.svg"), encoding="utf-8").read().strip()
subs = re.findall(r"M[^M]+?Z", P["mark"])

BLOCKS = {
    "LOCKUP": f'<svg class="lockup" viewBox="20 18 660 224" aria-hidden="true" focusable="false"><path class="mark" fill="#5E6A42" fill-rule="evenodd" d="{P["mark"]}"/><path class="iris" fill="#383434" fill-rule="evenodd" d="{P["iris"]}"/><path class="word" fill="#3C4632" fill-rule="evenodd" d="{P["word"]}"/></svg>',
    "MARK": '<svg class="chart__mark" viewBox="20 18 314 224" aria-hidden="true" focusable="false">' + "".join(f'<path class="lash" style="--i:{i}" fill="#F6F4EC" d="{s}"/>' for i, s in enumerate(subs)) + f'<path class="iris" fill="#383434" fill-rule="evenodd" d="{P["iris"]}"/></svg>',
    "MARKSMALL": f'<svg viewBox="20 18 314 224" aria-hidden="true" focusable="false"><path fill="#9CA97B" fill-rule="evenodd" d="{P["mark"]}"/><path fill="#F6F4EC" fill-rule="evenodd" d="{P["iris"]}"/></svg>',
    "LASH": f'<svg viewBox="{lash["bbox"][0]:.0f} {lash["bbox"][1]:.0f} {lash["bbox"][2]-lash["bbox"][0]:.0f} {lash["bbox"][3]-lash["bbox"][1]:.0f}" preserveAspectRatio="xMaxYMax meet" aria-hidden="true" focusable="false"><path fill="#3C4632" d="{lash["d"]}"/></svg>',
    "SPINEEND": '<svg class="spine__end" viewBox="20 18 314 224" aria-hidden="true" focusable="false">' + "".join(f'<path class="lash" fill="#9CA97B" d="{s}"/>' for s in subs) + f'<path class="iris" fill="#383434" fill-rule="evenodd" d="{P["iris"]}"/></svg>',
    "MARKWHITE": '<svg class="mark" viewBox="20 18 314 224" aria-hidden="true" focusable="false"><path fill="#FFFFFF" fill-rule="evenodd" d="' + P["mark"] + '"/><path fill="#383434" fill-rule="evenodd" d="' + P["iris"] + '"/></svg>',
    "LOCKUPWHITE": '<svg class="lockup" viewBox="20 18 660 224" aria-hidden="true" focusable="false"><path fill="#9CA97B" fill-rule="evenodd" d="' + P["mark"] + '"/><path fill="#FFFFFF" fill-rule="evenodd" d="' + P["iris"] + '"/><path fill="#FFFFFF" fill-rule="evenodd" d="' + P["word"] + '"/></svg>',
    "INDIA": india,
}

for path in glob.glob(os.path.join(ROOT, "*.html")):
    html = open(path, encoding="utf-8").read()
    orig = html
    for key, block in BLOCKS.items():
        wrapped = f"<!--{key}-->{block}<!--/{key}-->"
        html = re.sub(rf"<!--{key}-->.*?<!--/{key}-->", lambda m: wrapped, html, flags=re.S)
        html = html.replace(f"<!--{key}-->", wrapped) if f"<!--/{key}-->" not in html else html
    if html != orig:
        open(path, "w", encoding="utf-8").write(html)
        print("injected", os.path.basename(path))
