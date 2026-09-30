"""Generate the profile images (all SVG, stored in this repo so nothing depends on outside services).

    python assets/make_assets.py

banner.svg   animated banner: name, a typing line that cycles through three messages, role line
glance_v2.svg   four "at a glance" facts (renamed when counts change so GitHub drops its cached copy)
tools.svg    row of tool logos (official Simple Icons shapes; Power BI, Excel and AWS drawn as simple marks)
"""
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def banner():
    lines = ["I turn data into decisions.", "Dashboards, SQL and machine learning.",
             "Real data. Clear answers."]
    n, per = len(lines), 4.0                     # seconds each line is shown
    total = n * per
    msgs = []
    for i, text in enumerate(lines):
        start, end = i * per / total, (i + 1) * per / total
        chars = len(text)
        width = chars * 11.1
        # each line: types in over 1.6s, holds, then disappears
        k = lambda t: f"{min(max(t, 0), 1):.4f}"
        typed = start + 1.6 / total
        msgs.append(f'''
    <g opacity="0">
      <animate attributeName="opacity" dur="{total}s" repeatCount="indefinite" calcMode="discrete"
               keyTimes="0;{k(start)};{k(end)}" values="0;1;0"/>
      <clipPath id="c{i}"><rect x="54" y="118" height="34" width="0">
        <animate attributeName="width" dur="{total}s" repeatCount="indefinite"
                 keyTimes="0;{k(start)};{k(typed)};1" values="0;0;{width:.0f};{width:.0f}"/>
      </rect></clipPath>
      <text x="56" y="143" clip-path="url(#c{i})" font-family="Consolas, Menlo, monospace" font-size="20"
            font-weight="700" fill="#FFD166">{text}</text>
      <rect y="122" width="2.5" height="26" fill="#FFFFFF">
        <animate attributeName="x" dur="{total}s" repeatCount="indefinite"
                 keyTimes="0;{k(start)};{k(typed)};1" values="58;58;{58 + width:.0f};{58 + width:.0f}"/>
        <animate attributeName="opacity" dur="0.9s" repeatCount="indefinite" values="1;1;0;0" keyTimes="0;0.5;0.51;1"/>
      </rect>
    </g>''')
    dots = "".join(f'<circle cx="{620 + x * 16}" cy="{14 + y * 16}" r="1.6" fill="#FFFFFF" opacity="{0.10 + 0.25 * (x / 16):.2f}"/>'
                   for x in range(16) for y in range(13))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="220" viewBox="0 0 900 220" role="img" aria-label="Isaac Agyapong, Data Scientist, Health Informatics">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0B2447"/><stop offset="0.55" stop-color="#19376D"/><stop offset="1" stop-color="#576CBC"/>
    </linearGradient>
  </defs>
  <rect width="900" height="220" rx="18" fill="url(#bg)"/>
  {dots}
  <text x="56" y="58" font-family="{FONT}" font-size="16" font-weight="600" fill="#A5D7E8">Hi, I'm</text>
  <text x="54" y="102" font-family="{FONT}" font-size="40" font-weight="800" fill="#FFFFFF">Isaac Agyapong</text>
  {"".join(msgs)}
  <text x="56" y="188" font-family="{FONT}" font-size="16" fill="#D6E4FF">Data Scientist  ·  Data Analyst  ·  Health Informatics  ·  M.S. Data Science, Florida Poly (May 2027)</text>
</svg>'''


def glance():
    facts = [("5+", "years of clinical data work"), ("500K+", "patient records managed"),
             ("7", "dashboard, analytics &amp; ML projects")]
    gap = 16
    w = (900 - gap * (len(facts) - 1)) / len(facts)     # cards share the full width, however many there are
    cells = ""
    for i, (num, lab) in enumerate(facts):
        x = i * (w + gap) + 1
        cells += f'''<rect x="{x}" y="1" width="{w}" height="86" rx="12" fill="#FFFFFF" stroke="#D0D7DE"/>
  <text x="{x + w / 2}" y="44" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="800" fill="#19376D">{num}</text>
  <text x="{x + w / 2}" y="68" text-anchor="middle" font-family="{FONT}" font-size="{13.5 if len(lab) < 30 else 12.5}" fill="#59636E">{lab}</text>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="902" height="90" viewBox="0 0 902 90" role="img" aria-label="At a glance">{cells}</svg>'


def icon_path(slug):
    req = urllib.request.Request(f"https://cdn.simpleicons.org/{slug}/ffffff", headers={"User-Agent": "Mozilla/5.0"})
    svg = urllib.request.urlopen(req, timeout=30).read().decode()
    return re.search(r'<path d="([^"]+)"', svg).group(1)


def tools():
    items = [("Python", "python", "#3776AB"), ("PostgreSQL", "postgresql", "#336791"), ("pandas", "pandas", "#150458"),
             ("NumPy", "numpy", "#013243"), ("scikit-learn", "scikitlearn", "#F7931E"), ("PyTorch", "pytorch", "#EE4C2C"),
             ("R", "r", "#276DC3"), ("Jupyter", "jupyter", "#F37626"), ("Streamlit", "streamlit", "#FF4B4B"),
             ("Power BI", None, "#F2C811"), ("Excel", None, "#217346"), ("Git", "git", "#F05032"),
             ("Docker", "docker", "#2496ED"), ("AWS", None, "#232F3E")]
    size, gap = 56, 8
    out = ""
    for i, (name, slug, colour) in enumerate(items):
        x = i * (size + gap)
        out += f'<g><title>{name}</title><rect x="{x}" y="0" width="{size}" height="{size}" rx="12" fill="{colour}"/>'
        if slug:
            out += f'<g transform="translate({x + 14},14) scale(1.1667)"><path d="{icon_path(slug)}" fill="#FFFFFF"/></g>'
        elif name == "Power BI":       # three rising bars
            out += "".join(f'<rect x="{x + 15 + j * 9}" y="{40 - h}" width="7" height="{h}" rx="2" fill="#1F1F1F"/>'
                           for j, h in enumerate([12, 19, 26]))
        elif name == "Excel":
            out += (f'<rect x="{x + 13}" y="13" width="30" height="30" rx="4" fill="none" stroke="#FFFFFF" stroke-width="2.5"/>'
                    f'<text x="{x + 28}" y="35" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="800" fill="#FFFFFF">X</text>')
        else:                          # AWS wordmark + smile
            out += (f'<text x="{x + 28}" y="31" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="800" fill="#FFFFFF">aws</text>'
                    f'<path d="M{x + 16} 37 q12 8 24 0" stroke="#FF9900" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
        out += f'<text x="{x + size / 2}" y="{size + 17}" text-anchor="middle" font-family="{FONT}" font-size="11" fill="#59636E">{name}</text></g>'
    width = len(items) * (size + gap) - gap
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{size + 24}" viewBox="0 0 {width} {size + 24}" role="img" aria-label="Tools">{out}</svg>'


if __name__ == "__main__":
    (OUT / "banner.svg").write_text(banner(), encoding="utf-8")
    (OUT / "glance_v3.svg").write_text(glance(), encoding="utf-8")
    (OUT / "tools.svg").write_text(tools(), encoding="utf-8")
    print("wrote banner.svg, glance_v3.svg, tools.svg")
