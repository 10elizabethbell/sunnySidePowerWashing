#!/usr/bin/env python3
"""Re-embed assets/*.webp into index.html.

Photos live in <script type="text/plain" id="img-NAME"> blocks between the
IMAGE-DATA markers at the end of index.html; the page assigns them lazily.
The logo and mascot are CSS variables (--wordmark, --mascot) in the
<style id="brand-art"> block. Run after replacing a file in assets/.
"""
import base64, pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
page = root / "index.html"
html = page.read_text()
def uri(name):
    return "data:image/webp;base64," + base64.b64encode((root / "assets" / f"{name}.webp").read_bytes()).decode()
art = "\n".join(f"  --{n}: url({uri(n)});" for n in ("wordmark", "mascot"))
html = re.sub(r'(<style id="brand-art">:root\{\n).*?(\n?\}</style>)', lambda m: m.group(1) + art + m.group(2), html, flags=re.S)
names = sorted(p.stem for p in (root / "assets").glob("*.webp") if p.stem not in ("wordmark", "mascot"))
blocks = "\n".join(f'<script type="text/plain" id="img-{n}">{uri(n)}</script>' for n in names)
html = re.sub(r"(<!-- IMAGE-DATA -->\n).*?(\n?<!-- /IMAGE-DATA -->)", lambda m: m.group(1) + blocks + m.group(2), html, flags=re.S)
page.write_text(html)
print(f"embedded {len(names)} photos + 2 brand images; index.html is {page.stat().st_size // 1024} KB")
