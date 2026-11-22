# Portfolio site

Static site: plain HTML, CSS and a small vanilla JS file, no framework, no build step needed to host it. Light and dark themes (it follows the visitor's system setting until they pick one with the sun/moon switch or Ctrl+K, and remembers the choice), an interactive dot-grid hero, a skill filter on the projects, and a Ctrl+K palette to jump anywhere.

- `index.html`: home page (intro, projects, experience, skills, contact)
- `projects/*.html`: one case study per project
- `assets/`: `site.css` (styles), `site.js` (interactions), favicon, and WebP images
- `design/`: the design concepts and samples from choosing the look (not published; it's in `.gitignore`)
- `Sathish-Kumar-Resume.pdf`: the resume linked from the site
- `build/`: the generator. Edit text in `build/content.py`, then run `python3 build/build.py` (needs Pillow). It copies images from `../Portfolio/projects` and the PDF from `../resume`.

Works from 320px wide up, by keyboard, and with reduced motion (no typing or moving dots).

## Preview locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Publishing

Live at https://sathishr424.github.io/ (GitHub Pages, from the `main` branch of `sathishr424.github.io`). To update it, rebuild, commit and push:

```bash
python3 build/build.py && git add -A && git commit -m "Update site" && git push origin master:main
```

The previous site (2022-2023) is kept in the `old-portfolio` repo.

## Custom domain (optional, about $10–15 a year)

1. Buy a domain, e.g. `sathishkumar.dev`.
2. At the domain registrar, add DNS records for GitHub Pages: four `A` records for the apex domain pointing to `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`, and a `CNAME` record for `www` pointing to `sathishr424.github.io`.
3. In repo → Settings → Pages → Custom domain, enter the domain and tick "Enforce HTTPS".
4. Set `"url"` in `build/content.py` to the new domain and rebuild, so link previews on LinkedIn and WhatsApp use the right address.

## Before you publish, check

- The resume PDF has your phone number. On a public site it can be found by anyone. Remove the phone line from the PDF you publish if you'd rather not.
- Mock AI and Resume Builder say "available on request" because their repos are private. If you make a repo public or deploy a demo, add it to `links` for that project in `build/content.py`.
- The Price Tracker page says 6 retailers, as your portfolio copy does. Your old resume said 4; make them match.
