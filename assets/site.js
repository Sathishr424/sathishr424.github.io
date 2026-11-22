// Interactions: header border, typed headline, dot grid, skill filter, Ctrl+K palette.
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header border once the page scrolls
  const top = $('.top');
  const onScroll = () => top && top.classList.toggle('scrolled', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Typed headline. The full text stays in the page for screen readers and search engines,
  // and an invisible copy reserves the space so nothing below it jumps while it types.
  const h1 = $('[data-type]');
  if (h1) {
    const text = h1.textContent.trim();
    h1.innerHTML = `<span class="sr-only">${text}</span><span class="tw tw-ghost" aria-hidden="true">${text}</span><span class="tw tw-live" aria-hidden="true">${still ? text : ''}</span>`;
    if (!still) {
      const live = $('.tw-live', h1); let i = 0;
      h1.classList.add('typing');
      const tick = () => { live.textContent = text.slice(0, ++i); if (i < text.length) setTimeout(tick, 26); else setTimeout(() => h1.classList.remove('typing'), 1600); };
      setTimeout(tick, 250);
    }
  }

  // Dot grid behind the hero: dots drift gently and move away from the cursor
  const cv = $('#dots');
  if (cv) {
    const cx = cv.getContext('2d'); const G = 28; let W = 0, H = 0, mx = -999, my = -999, raf = 0, visible = true;
    const size = () => { const r = devicePixelRatio || 1; W = cv.clientWidth; H = cv.clientHeight; cv.width = W * r; cv.height = H * r; cx.setTransform(r, 0, 0, r, 0, 0); };
    const draw = t => {
      cx.clearRect(0, 0, W, H);
      for (let x = G / 2; x < W; x += G) for (let y = G / 2; y < H; y += G) {
        const dx = x - mx, dy = y - my, d = Math.hypot(dx, dy), f = Math.max(0, 1 - d / 170);
        const wave = still ? .5 : Math.sin(t / 900 + x / 140 + y / 180) * .5 + .5;
        const ox = d ? dx / d * f * 14 : 0, oy = d ? dy / d * f * 14 : 0;
        cx.fillStyle = f > 0 ? `rgba(52,211,153,${.25 + f * .75})` : `rgba(143,155,184,${.08 + wave * .12})`;
        cx.beginPath(); cx.arc(x + ox, y + oy, 1.2 + f * 2.2, 0, 7); cx.fill();
      }
    };
    const loop = t => { draw(t); raf = visible ? requestAnimationFrame(loop) : 0; };
    size(); addEventListener('resize', () => { size(); if (still) draw(0); });
    const hero = cv.parentElement;
    hero.addEventListener('pointermove', e => { const r = cv.getBoundingClientRect(); mx = e.clientX - r.left; my = e.clientY - r.top; if (still) draw(0); });
    hero.addEventListener('pointerleave', () => { mx = my = -999; if (still) draw(0); });
    if (still) draw(0);
    else {
      // pause the animation while the hero is off screen
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; if (visible && !raf) raf = requestAnimationFrame(loop); }).observe(hero);
    }
  }

  // Skill filter: dim projects that don't use the chosen skill
  const filters = $$('.filters button'), cards = $$('.card[data-skills]'), note = $('#filter-note');
  filters.forEach(b => b.addEventListener('click', () => {
    const f = b.dataset.f; let n = 0;
    filters.forEach(x => { const on = x === b; x.classList.toggle('on', on); x.setAttribute('aria-pressed', on); });
    cards.forEach(c => {
      const has = f === 'all' || c.dataset.skills.split('|').includes(f); if (has) n++;
      c.classList.toggle('dim', !has);
      $$('.chips li', c).forEach(li => li.classList.toggle('match', li.dataset.skill === f));
    });
    if (note) note.textContent = f === 'all' ? '' : `${n} of ${cards.length} projects use ${f}.`;
  }));

  // Ctrl+K palette
  const pal = $('#pal'), input = $('#pal-in'), list = $('#pal-list');
  const data = JSON.parse(($('#nav-data') || {}).textContent || '[]');
  let shown = data, sel = 0, opener = null;
  const render = () => {
    list.innerHTML = shown.length
      ? shown.map((c, i) => `<li role="option" id="opt-${i}" aria-selected="${i === sel}" data-i="${i}">${c.t}<span>${c.k}</span></li>`).join('')
      : '<li class="empty">No matches</li>';
    input.setAttribute('aria-activedescendant', shown.length ? `opt-${sel}` : '');
    const cur = $(`#opt-${sel}`); if (cur) cur.scrollIntoView({ block: 'nearest' });
  };
  const go = c => { close(); if (c.x) window.open(c.u, '_blank', 'noopener'); else location.href = c.u; };
  const open = () => { opener = document.activeElement; pal.hidden = false; input.value = ''; shown = data; sel = 0; render(); input.focus(); document.body.style.overflow = 'hidden'; };
  const close = () => { if (pal.hidden) return; pal.hidden = true; document.body.style.overflow = ''; if (opener && opener.focus) opener.focus(); };
  if (pal) {
    $$('[data-palette]').forEach(b => b.addEventListener('click', open));
    pal.addEventListener('click', e => { if (e.target === pal) close(); });
    list.addEventListener('click', e => { const li = e.target.closest('li[data-i]'); if (li) go(shown[+li.dataset.i]); });
    list.addEventListener('mousemove', e => { const li = e.target.closest('li[data-i]'); if (li && +li.dataset.i !== sel) { sel = +li.dataset.i; render(); } });
    input.addEventListener('input', () => { const q = input.value.trim().toLowerCase(); shown = data.filter(c => (c.t + ' ' + c.k).toLowerCase().includes(q)); sel = 0; render(); });
    addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); pal.hidden ? open() : close(); return; }
      if (pal.hidden) return;
      if (e.key === 'Escape') { e.preventDefault(); close(); }
      else if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(shown.length - 1, sel + 1); render(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(0, sel - 1); render(); }
      else if (e.key === 'Enter' && shown[sel]) { e.preventDefault(); go(shown[sel]); }
      else if (e.key === 'Tab') { e.preventDefault(); input.focus(); }
    });
  }
})();
