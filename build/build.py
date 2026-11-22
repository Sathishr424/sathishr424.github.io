#!/usr/bin/env python3
"""Builds the portfolio site into the folder above this one.

Run:  python3 build/build.py
It writes index.html, projects/*.html and assets/img/** (WebP copies of the
images in ../Portfolio/projects). Edit the content in content.py, then re-run.
"""
import html
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
def image(slug, src, alt_w=None):
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


def img_tag(path, w, h, alt, prefix="", cls="", lazy=True, sizes=None):
    attrs = [f'src="{prefix}{path}"', f'width="{w}"', f'height="{h}"', f'alt="{esc(alt)}"']
    if lazy:
        attrs.append('loading="lazy"')
    attrs.append('decoding="async"')
    if cls:
        attrs.append(f'class="{cls}"')
    return f"<img {' '.join(attrs)}>"


# ---------------------------------------------------------------- shared chrome
ICONS = {
    "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.53-1.33-1.28-1.69-1.28-1.69-1.05-.71.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.8 1.19 1.83 1.19 3.09 0 4.42-2.69 5.39-5.26 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5Z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05a3.75 3.75 0 0 1 3.37-1.85c3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M3 5.5h18v13H3z M3.5 6l8.5 7 8.5-7"/></svg>',
    "file": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M6 2.5h8l4 4v15H6z M14 2.5v4h4 M9 12h6 M9 16h6"/></svg>',
    "ext": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M14 4h6v6 M20 4l-9 9 M18 14v6H4V6h6"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M5 12h14 M13 6l6 6-6 6"/></svg>',
    "back": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M19 12H5 M11 6l-6 6 6 6"/></svg>',
}


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
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def nav(prefix, home=False):
    h = "" if home else f"{prefix}index.html"
    return f"""<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="{prefix}index.html" aria-label="{esc(SITE['name'])}, home"><span class="mark">SK</span><span class="brand-name">{esc(SITE['name'])}</span></a>
    <nav aria-label="Main">
      <a href="{h}#work">Work</a>
      <a href="{h}#experience">Experience</a>
      <a href="{h}#contact">Contact</a>
      <a class="nav-cta" href="{prefix}{SITE['resume_pdf']}" target="_blank" rel="noopener">Resume</a>
    </nav>
  </div>
</header>
"""


def footer(prefix):
    return f"""<footer class="foot" id="contact">
  <div class="wrap foot-in">
    <div>
      <p class="eyebrow">Contact</p>
      <h2 class="foot-title">Open to full-stack and backend roles.</h2>
      <p class="foot-sub">{esc(SITE['looking_for'])}</p>
    </div>
    <div class="foot-links">
      <a class="btn btn-primary" href="mailto:{SITE['email']}">{ICONS['mail']}{esc(SITE['email'])}</a>
      <a class="btn" href="{SITE['linkedin']}" target="_blank" rel="noopener">{ICONS['linkedin']}LinkedIn</a>
      <a class="btn" href="{SITE['github']}" target="_blank" rel="noopener">{ICONS['github']}GitHub</a>
      <a class="btn" href="{prefix}{SITE['resume_pdf']}" target="_blank" rel="noopener">{ICONS['file']}Resume (PDF)</a>
    </div>
  </div>
  <div class="wrap legal">© {SITE['year']} {esc(SITE['name'])}. Client projects are shown with client details removed.</div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- pages
def card(p, featured=False):
    path, w, h = p["_cover"]
    tags = "".join(f"<li>{esc(t)}</li>" for t in p["tags"][:5])
    cls = "card card-featured" if featured else "card"
    return f"""<a class="{cls}" href="projects/{p['slug']}.html">
  <div class="card-img">{img_tag(path, w, h, p['title'] + ' cover', lazy=not featured)}</div>
  <div class="card-body">
    <p class="card-kind"><span class="dot dot-{p['kind_key']}"></span>{esc(p['kind'])} · {esc(p['year'])}</p>
    <h3>{esc(p['title'])}</h3>
    <p class="card-line">{esc(p['tagline'])}</p>
    <ul class="tags">{tags}</ul>
    <span class="card-go">Read case study {ICONS['arrow']}</span>
  </div>
</a>"""


def build_index():
    personal = [p for p in PROJECTS if p["kind_key"] == "personal"]
    client = [p for p in PROJECTS if p["kind_key"] == "client"]
    stats = "".join(f'<div class="stat"><b>{esc(n)}</b><span>{esc(l)}</span></div>' for n, l in SITE["stats"])
    exp = "".join(
        f"""<li class="exp">
  <div class="exp-when">{esc(e['when'])}</div>
  <div class="exp-what"><h3>{esc(e['role'])}</h3><p class="exp-where">{esc(e['where'])}</p><ul>{''.join(f"<li>{esc(x)}</li>" for x in e['points'])}</ul></div>
</li>""" for e in EXPERIENCE)
    skills = "".join(f"<div class=\"skill\"><h3>{esc(k)}</h3><p>{esc(v)}</p></div>" for k, v in SKILLS)

    out = head(f"{SITE['name']} · {SITE['role']}", SITE["meta_description"], "", PROJECTS[0]["_cover"][0], "")
    out += nav("", home=True)
    out += f"""<main id="main">
<section class="hero wrap">
  <p class="eyebrow">{esc(SITE['role'])} · {esc(SITE['location'])}</p>
  <h1>{SITE['headline']}</h1>
  <p class="lede">{esc(SITE['intro'])}</p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="#work">See my work {ICONS['arrow']}</a>
    <a class="btn" href="{SITE['resume_pdf']}" target="_blank" rel="noopener">{ICONS['file']}Resume</a>
    <a class="btn btn-icon" href="{SITE['github']}" target="_blank" rel="noopener" aria-label="GitHub">{ICONS['github']}</a>
    <a class="btn btn-icon" href="{SITE['linkedin']}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICONS['linkedin']}</a>
    <a class="btn btn-icon" href="mailto:{SITE['email']}" aria-label="Email">{ICONS['mail']}</a>
  </div>
  <div class="stats">{stats}</div>
</section>

<section class="section wrap" id="work" aria-labelledby="work-h">
  <div class="sec-head"><p class="eyebrow">Selected work</p><h2 id="work-h">Projects</h2>
  <p class="sec-sub">Each project has a short case study: the problem, what I built, and the engineering behind it.</p></div>
  <h3 class="group-h"><span class="dot"></span>Personal projects <span>designed and built end to end, on my own</span></h3>
  <div class="grid-featured">{''.join(card(p, i < 2) for i, p in enumerate(personal))}</div>
  <h3 class="group-h"><span class="dot dot-client"></span>Client work <span>freelance, with client names and data removed</span></h3>
  <div class="grid">{''.join(card(p) for p in client)}</div>
</section>

<section class="section wrap" id="experience" aria-labelledby="exp-h">
  <div class="two">
    <div>
      <div class="sec-head"><p class="eyebrow">Experience</p><h2 id="exp-h">Where I've worked</h2></div>
      <ol class="exps">{exp}</ol>
    </div>
    <div>
      <div class="sec-head"><p class="eyebrow">Toolkit</p><h2>Skills</h2></div>
      <div class="skills">{skills}</div>
    </div>
  </div>
</section>
</main>
"""
    out += footer("")
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
    tags = "".join(f"<li>{esc(t)}</li>" for t in p["tags"])

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
            wide = " wide" if iw / ih > 1.2 else ""
            body.append(f'<figure class="fig{wide}">{img_tag(ip, iw, ih, block[2] if len(block) > 2 else p["title"], prefix)}{cap}</figure>')
        elif kind == "note":
            body.append(f'<p class="note">{block[1]}</p>')

    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]

    out = head(f"{p['title']} · {SITE['name']}", p["tagline"], prefix, path, f"projects/{p['slug']}.html")
    out += nav(prefix)
    out += f"""<main id="main" class="proj">
<div class="wrap">
  <a class="back" href="../index.html#work">{ICONS['back']}All projects</a>
  <header class="proj-head">
    <p class="card-kind"><span class="dot dot-{p['kind_key']}"></span>{esc(p['kind'])} · {esc(p['year'])}</p>
    <h1>{esc(p['title'])}</h1>
    <p class="lede">{esc(p['tagline'])}</p>
    <div class="proj-links">{links}</div>
  </header>
  <figure class="proj-cover">{img_tag(path, w, h, p['title'] + ' cover', prefix, lazy=False)}</figure>
  <div class="proj-grid">
    <aside class="proj-side">
      <dl class="facts">{facts}</dl>
      <ul class="tags">{tags}</ul>
    </aside>
    <article class="prose">{''.join(body)}</article>
  </div>
  <nav class="pn" aria-label="More projects">
    <a href="{prev_p['slug']}.html"><span>{ICONS['back']}Previous</span><b>{esc(prev_p['title'])}</b></a>
    <a class="pn-next" href="{next_p['slug']}.html"><span>Next{ICONS['arrow']}</span><b>{esc(next_p['title'])}</b></a>
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
    # resume PDF
    pdf = Path(SITE["resume_source"])
    if pdf.exists():
        shutil.copy2(pdf, ROOT / SITE["resume_pdf"])
    print(f"Built index.html and {len(PROJECTS)} project pages into {ROOT}")


if __name__ == "__main__":
    main()
