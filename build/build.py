#!/usr/bin/env python3
"""Builds the portfolio site into the folder above this one.

Run:  python3 build/build.py
It writes index.html, projects/*.html and assets/img/** (WebP copies of the
images in ../Portfolio/projects). Edit the content in content.py, then re-run.
Styles live in assets/site.css and interactions in assets/site.js.
"""
import html
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from content import SITE, PROJECTS, EXPERIENCE, SKILLS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent            # portfolio-site/
SRC = ROOT.parent / "Portfolio" / "projects"             # source images
IMG_OUT = ROOT / "assets" / "img"
MAX_W = 1600


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- images
def image(slug, src):
    """Convert ../Portfolio/projects/<src> to assets/img/<slug>/<name>.webp.
    Returns (relative path from site root, width, height)."""
    src_path = SRC / src
    name = Path(src).stem + ".webp"
    out = IMG_OUT / slug / name
    out.parent.mkdir(parents=True, exist_ok=True)
    if not out.exists() or out.stat().st_mtime < src_path.stat().st_mtime:
        im = Image.open(src_path).convert("RGB")
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        im.save(out, "WEBP", quality=86, method=6)
    w, h = Image.open(out).size
    return f"assets/img/{slug}/{name}", w, h


def img_tag(path, w, h, alt, prefix="", lazy=True):
    attrs = [f'src="{prefix}{path}"', f'width="{w}"', f'height="{h}"', f'alt="{esc(alt)}"', 'decoding="async"']
    if lazy:
        attrs.append('loading="lazy"')
    return f"<img {' '.join(attrs)}>"


# ---------------------------------------------------------------- shared chrome
ICONS = {
    "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.53-1.33-1.28-1.69-1.28-1.69-1.05-.71.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.8 1.19 1.83 1.19 3.09 0 4.42-2.69 5.39-5.26 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5Z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05a3.75 3.75 0 0 1 3.37-1.85c3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg>',
    "upwork": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M3 8h18v12H3z M8.5 8V5.5a1.5 1.5 0 0 1 1.5-1.5h4a1.5 1.5 0 0 1 1.5 1.5V8 M3 13h18"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M3 5.5h18v13H3z M3.5 6l8.5 7 8.5-7"/></svg>',
    "file": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M6 2.5h8l4 4v15H6z M14 2.5v4h4 M9 12h6 M9 16h6"/></svg>',
    "ext": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M14 4h6v6 M20 4l-9 9 M18 14v6H4V6h6"/></svg>',
    "search": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M10.5 3.5a7 7 0 1 1 0 14 7 7 0 0 1 0-14z M15.5 15.5 21 21"/></svg>',
    "sun": '<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>',
    "moon": '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/></svg>',
    "back": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M19 12H5 M11 6l-6 6 6 6"/></svg>',
    "next": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M5 12h14 M13 6l6 6-6 6"/></svg>',
}


def nav_data(prefix, home):
    """Entries for the Ctrl+K palette, with URLs relative to the current page."""
    h = "" if home else f"{prefix}index.html"
    items = [
        {"t": "Work", "k": "Section", "u": f"{h}#work"},
        {"t": "Experience", "k": "Section", "u": f"{h}#experience"},
        {"t": "Skills", "k": "Section", "u": f"{h}#skills"},
        {"t": "Contact", "k": "Section", "u": "#contact"},
    ]
    items += [{"t": p["title"], "k": p["kind"], "u": f"{prefix}projects/{p['slug']}.html"} for p in PROJECTS]
    items += [
        {"t": "Resume (PDF)", "k": "Link", "u": f"{prefix}{SITE['resume_pdf']}", "x": 1},
        {"t": "GitHub", "k": "Link", "u": SITE["github"], "x": 1},
        {"t": "LinkedIn", "k": "Link", "u": SITE["linkedin"], "x": 1},
        {"t": "Upwork profile", "k": "Link", "u": SITE["upwork"], "x": 1},
        {"t": "Email me", "k": "Link", "u": f"mailto:{SITE['email']}"},
        {"t": "Switch light / dark theme", "k": "Action", "a": "theme"},
    ]
    return json.dumps(items)


def head(title, description, prefix, og_image, path):
    url = SITE["url"].rstrip("/") + "/" + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(SITE['url'].rstrip('/') + '/' + og_image)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#0a0f1e" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f5f7fb" media="(prefers-color-scheme: light)">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/site.css">
<script defer src="{prefix}assets/site.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(prefix, home=False):
    h = "" if home else f"{prefix}index.html"
    return f"""<header class="top" id="top">
  <div class="wrap top-in">
    <a class="brand" href="{prefix}index.html" aria-label="{esc(SITE['name'])}, home"><span class="mark">SK</span>{esc(SITE['name'])}</a>
    <nav class="nav" aria-label="Main">
      <a href="{h}#work">Work</a><a href="{h}#experience">Experience</a><a href="{h}#skills">Skills</a><a href="#contact">Contact</a>
      <a href="{prefix}{SITE['resume_pdf']}" target="_blank" rel="noopener">Resume</a>
    </nav>
    <button class="theme-btn" type="button" data-theme-toggle aria-label="Switch theme">{ICONS['sun']}{ICONS['moon']}</button>
    <button class="kbtn" type="button" data-palette aria-haspopup="dialog">{ICONS['search']}<span>Jump to…</span><kbd>Ctrl K</kbd></button>
  </div>
</header>
"""


def palette(prefix, home):
    return f"""<div class="pal" id="pal" role="dialog" aria-modal="true" aria-label="Jump to" hidden>
  <div class="pal-box">
    <input id="pal-in" type="text" placeholder="Search projects, sections and links" autocomplete="off" role="combobox" aria-expanded="true" aria-controls="pal-list">
    <ul id="pal-list" role="listbox" aria-label="Results"></ul>
    <p class="pal-hint"><kbd>↑</kbd><kbd>↓</kbd> to move <kbd>Enter</kbd> to open <kbd>Esc</kbd> to close</p>
  </div>
</div>
<script id="nav-data" type="application/json">{nav_data(prefix, home)}</script>
"""


def footer(prefix, home=False):
    return f"""<div class="wrap">
  <section class="contact" id="contact" aria-labelledby="contact-h">
    <div>
      <h2 id="contact-h">Open to full-stack and backend roles.</h2>
      <p>{esc(SITE['looking_for'])}</p>
    </div>
    <div class="cta">
      <a class="btn btn-primary" href="mailto:{SITE['email']}">{ICONS['mail']}{esc(SITE['email'])}</a>
      <a class="btn" href="{SITE['linkedin']}" target="_blank" rel="noopener">{ICONS['linkedin']}LinkedIn</a>
      <a class="btn" href="{SITE['upwork']}" target="_blank" rel="noopener">{ICONS['upwork']}Upwork</a>
      <a class="btn" href="{SITE['github']}" target="_blank" rel="noopener">{ICONS['github']}GitHub</a>
      <a class="btn" href="{prefix}{SITE['resume_pdf']}" target="_blank" rel="noopener">{ICONS['file']}Resume (PDF)</a>
    </div>
  </section>
</div>
<footer class="foot"><div class="wrap">© {SITE['year']} {esc(SITE['name'])}. Client projects are shown with client details removed.<span class="foot-k"> Press <kbd>Ctrl K</kbd> to jump anywhere.</span></div></footer>
{palette(prefix, home)}</body>
</html>
"""


def chips(skills):
    return '<ul class="chips">' + "".join(f'<li data-skill="{esc(s)}">{esc(s)}</li>' for s in skills) + "</ul>"


# ---------------------------------------------------------------- pages
def card(p, i):
    path, w, h = p["_cover"]
    size = "c-wide" if i < 2 or i >= len(PROJECTS) - 2 else "c-third"
    return f"""<a class="card {size}" href="projects/{p['slug']}.html" data-skills="{esc('|'.join(p['skills']))}">
  <div class="card-img">{img_tag(path, w, h, p['title'] + ' cover', lazy=i >= 2)}</div>
  <div class="card-body">
    <p class="kind kind-{p['kind_key']}">{esc(p['kind'])} · {esc(p['year'])}</p>
    <h3>{esc(p['title'])}</h3>
    <p class="card-line">{esc(p['tagline'])}</p>
    {chips(p['skills'])}
  </div>
</a>"""


def job(e, i):
    pts = "".join(f"<li>{esc(x)}</li>" for x in e["points"])
    now = '<span class="now"><span class="live" aria-hidden="true"></span>Current</span>' if "Present" in e["when"] else ""
    return f"""<article class="job">
  <div class="job-meta">
    <p class="when">{esc(e['when'])}{now}</p>
    <h3>{esc(e['role'])}</h3>
    <p class="at">{esc(e['where'])}</p>
  </div>
  <ul>{pts}</ul>
</article>"""


def build_index():
    stats = "".join(
        (f'<a class="stat stat-link" href="{SITE["upwork"]}" target="_blank" rel="noopener"><b>{esc(n)}</b><span>{esc(l)} {ICONS["ext"]}</span></a>'
         if "Upwork" in l else f'<div class="stat"><b>{esc(n)}</b><span>{esc(l)}</span></div>')
        for n, l in SITE["stats"])
    filters = '<button type="button" class="on" aria-pressed="true" data-f="all">All</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{esc(f)}">{esc(f)}</button>' for f in SITE["filters"])
    skills = "".join(
        f'<div class="skill"><h3>{esc(k)}</h3><ul class="chips">{"".join(f"<li>{esc(x)}</li>" for x in v)}</ul></div>'
        for k, v in SKILLS)

    out = head(f"{SITE['name']} · {SITE['role']}", SITE["meta_description"], "", PROJECTS[0]["_cover"][0], "")
    out += header("", home=True)
    out += f"""<main id="main">
<section class="hero" aria-labelledby="hero-h">
  <canvas id="dots" aria-hidden="true"></canvas>
  <div class="wrap hero-in">
    <p class="who"><span class="live" aria-hidden="true"></span>{esc(SITE['role'])} · {esc(SITE['location'])}</p>
    <h1 id="hero-h" data-type>{esc(SITE['headline'])}</h1>
    <p class="lede">{esc(SITE['intro'])}</p>
    <div class="cta">
      <a class="btn btn-primary" href="#work">See my work</a>
      <a class="btn" href="{SITE['resume_pdf']}" target="_blank" rel="noopener">{ICONS['file']}Resume</a>
      <a class="btn" href="{SITE['github']}" target="_blank" rel="noopener">{ICONS['github']}GitHub</a>
      <a class="btn" href="{SITE['linkedin']}" target="_blank" rel="noopener">{ICONS['linkedin']}LinkedIn</a>
      <a class="btn" href="{SITE['upwork']}" target="_blank" rel="noopener">{ICONS['upwork']}Upwork</a>
      <a class="btn" href="mailto:{SITE['email']}">{ICONS['mail']}Email</a>
    </div>
    <div class="stats">{stats}</div>
  </div>
</section>

<section class="section wrap" id="work" aria-labelledby="work-h">
  <div class="sec-head"><h2 id="work-h">Selected work</h2><p>Pick a skill to see where I've used it. Each project opens a short case study.</p></div>
  <div class="filters" role="group" aria-label="Filter projects by skill">{filters}</div>
  <p class="filter-note" id="filter-note" aria-live="polite"></p>
  <div class="grid" id="grid">{''.join(card(p, i) for i, p in enumerate(PROJECTS))}</div>
</section>

<section class="section wrap" id="experience" aria-labelledby="exp-h">
  <div class="sec-head"><h2 id="exp-h">Experience</h2></div>
  <div class="jobs">{''.join(job(e, i) for i, e in enumerate(EXPERIENCE))}</div>
</section>

<section class="section wrap" id="skills" aria-labelledby="skills-h">
  <div class="sec-head"><h2 id="skills-h">Skills</h2></div>
  <div class="skills">{skills}</div>
</section>
</main>
"""
    out += footer("", home=True)
    (ROOT / "index.html").write_text(out)


def build_project(i, p):
    prefix = "../"
    path, w, h = p["_cover"]
    links = "".join(
        f'<a class="btn{" btn-primary" if j == 0 else ""}" href="{esc(u)}" target="_blank" rel="noopener">{ICONS["github"] if "github.com" in u else ICONS["ext"]}{esc(t)}</a>'
        for j, (t, u) in enumerate(p.get("links", [])))
    if p.get("link_note"):
        links += f'<span class="link-note">{esc(p["link_note"])}</span>'
    facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in p["facts"])

    body = []
    for block in p["body"]:
        kind = block[0]
        if kind == "h":
            body.append(f"<h2>{esc(block[1])}</h2>")
        elif kind == "p":
            body.append(f"<p>{block[1]}</p>")
        elif kind == "ul":
            body.append("<ul>" + "".join(f"<li>{x}</li>" for x in block[1]) + "</ul>")
        elif kind == "img":
            ip, iw, ih = image(p["slug"], block[1])
            cap = f"<figcaption>{esc(block[2])}</figcaption>" if len(block) > 2 and block[2] else ""
            body.append(f'<figure class="fig">{img_tag(ip, iw, ih, block[2] if len(block) > 2 else p["title"], prefix)}{cap}</figure>')
        elif kind == "note":
            body.append(f'<p class="note">{block[1]}</p>')

    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]

    out = head(f"{p['title']} · {SITE['name']}", p["tagline"], prefix, path, f"projects/{p['slug']}.html")
    out += header(prefix)
    out += f"""<main id="main" class="proj">
<div class="wrap">
  <a class="back" href="../index.html#work">{ICONS['back']}All projects</a>
  <header class="proj-head">
    <p class="kind kind-{p['kind_key']}">{esc(p['kind'])} · {esc(p['year'])}</p>
    <h1>{esc(p['title'])}</h1>
    <p class="lede">{esc(p['tagline'])}</p>
    <div class="cta">{links}</div>
  </header>
  <figure class="proj-cover">{img_tag(path, w, h, p['title'] + ' cover', prefix, lazy=False)}</figure>
  <div class="proj-grid">
    <aside class="proj-side">
      <dl class="facts">{facts}</dl>
      {chips(p['tags'])}
    </aside>
    <article class="prose">{''.join(body)}</article>
  </div>
  <nav class="pn" aria-label="More projects">
    <a href="{prev_p['slug']}.html"><span>{ICONS['back']}Previous</span><b>{esc(prev_p['title'])}</b></a>
    <a class="pn-next" href="{next_p['slug']}.html"><span>Next{ICONS['next']}</span><b>{esc(next_p['title'])}</b></a>
  </nav>
</div>
</main>
"""
    out += footer(prefix)
    (ROOT / "projects" / f"{p['slug']}.html").write_text(out)


def main():
    (ROOT / "projects").mkdir(exist_ok=True)
    for p in PROJECTS:
        p["_cover"] = image(p["slug"], p["cover"])
    build_index()
    for i, p in enumerate(PROJECTS):
        build_project(i, p)
    pdf = Path(SITE["resume_source"])
    if pdf.exists():
        shutil.copy2(pdf, ROOT / SITE["resume_pdf"])
    print(f"Built index.html and {len(PROJECTS)} project pages into {ROOT}")


if __name__ == "__main__":
    main()
