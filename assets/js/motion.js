// Motion, Save a Child's Heart recipes: reveals (10em fade-up, 1200ms), EKG traces drawn on view or
// scrubbed by scroll, marquee, hero mouse-parallax. Plus the functional bits: slider, accordions.
let io = null;

function observe(selector, onEnter, threshold = 0) {
  const els = [...document.querySelectorAll(selector)];
  if (!els.length) return;
  if (!('IntersectionObserver' in window)) { els.forEach(onEnter); return; }
  const obs = new IntersectionObserver(entries => entries.forEach(e => { if (e.isIntersecting) { onEnter(e.target); obs.unobserve(e.target); } }), { threshold });
  els.forEach(el => obs.observe(el));
  return obs;
}

// Reveals wait for the preloader (SACH: hero text enters 2.3s after page start, i.e. after the loader).
export function startHero() {
  io = observe('.rv', el => el.classList.add('is-in'));
  observe('.ekg:not(.ekg--scrub)', el => el.classList.add('is-in'));
  observe('.bars', el => el.classList.add('is-in'), 0.3);
}

function initScrub() {
  const els = [...document.querySelectorAll('.ekg--scrub:not(.tl-line)')];
  if (!els.length) return;
  const tick = () => {
    const vh = innerHeight;
    els.forEach(el => {
      const host = el.closest('[data-scrub]') || el;
      const r = host.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (vh * 0.8 - r.top) / (r.height + vh * 0.3)));
      el.style.setProperty('--p', p.toFixed(3));
    });
  };
  addEventListener('scroll', tick, { passive: true }); addEventListener('resize', tick); tick();
}

function initMarquee() {
  document.querySelectorAll('.marquee__track').forEach(t => { t.innerHTML += t.innerHTML; });
}

function initParallax(reduced) {
  if (reduced || !matchMedia('(pointer: fine)').matches) return;
  document.querySelectorAll('[data-parallax]').forEach(el => {
    const zone = el.closest('.hero') || el.parentElement;
    zone.addEventListener('pointermove', e => {
      const r = zone.getBoundingClientRect();
      const x = ((e.clientX - r.left) / r.width - .5) * 50, y = ((e.clientY - r.top) / r.height - .5) * 50;
      el.style.transform = `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px)`;
    });
    zone.addEventListener('pointerleave', () => { el.style.transform = ''; });
  });
}

function initSlider() {
  document.querySelectorAll('.slider').forEach(s => {
    const slides = [...s.querySelectorAll('.slide')]; if (slides.length < 2) return;
    let i = slides.findIndex(x => x.classList.contains('is-active')); if (i < 0) i = 0;
    const show = n => { slides[i].classList.remove('is-active'); i = (n + slides.length) % slides.length; slides[i].classList.add('is-active'); };
    s.querySelector('.slider__btn--prev')?.addEventListener('click', () => show(i - 1));
    s.querySelector('.slider__btn--next')?.addEventListener('click', () => show(i + 1));
  });
}

function initAccordions() {
  document.querySelectorAll('.acc-btn').forEach(btn => {
    const panel = document.getElementById(btn.getAttribute('aria-controls'));
    const group = btn.closest('[data-accordion]');
    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') === 'true';
      if (!open && group) group.querySelectorAll('.acc-btn[aria-expanded="true"]').forEach(b => {
        if (b === btn) return;
        b.setAttribute('aria-expanded', 'false');
        document.getElementById(b.getAttribute('aria-controls'))?.classList.remove('is-open');
      });
      btn.setAttribute('aria-expanded', String(!open));
      panel.classList.toggle('is-open', !open);
    });
  });
  document.querySelectorAll('[data-show-all]').forEach(btn => btn.addEventListener('click', () => {
    const rows = document.querySelectorAll(btn.dataset.showAll);
    rows.forEach(el => { el.hidden = false; el.classList.add('is-in'); });
    if (rows[0]) { rows[0].tabIndex = -1; rows[0].focus(); }
    (btn.closest('[data-show-all-wrap]') || btn).remove();
  }));
}

// SACH sticky timeline: the year track slides sideways while the section scrolls; the EKG draws with it.
function initTimeline(reduced) {
  const sec = document.querySelector('[data-timeline]');
  if (!sec) return;
  const track = sec.querySelector('.tl-track'), line = sec.querySelector('.tl-line'), view = sec.querySelector('.tl__viewport');
  const mq = matchMedia('(max-width: 991px)');
  const items = track.querySelectorAll('.tl-item'), n = items.length;
  const tick = () => {
    if (reduced) { track.style.transform = ''; if (line) line.style.setProperty('--p', '1'); return; }
    const r = sec.getBoundingClientRect(), vh = innerHeight;
    const p = Math.min(1, Math.max(0, -r.top / (r.height - vh)));
    if (mq.matches) {
      // phones: one item fills the viewport; the track snaps item by item as the section scrolls
      const w = items[0].getBoundingClientRect().width, idx = Math.min(n - 1, Math.round(p * (n - 1)));
      track.style.transform = `translateX(${(-idx * w).toFixed(1)}px)`;
      if (line) line.style.setProperty('--p', (0.12 + (idx / Math.max(1, n - 1)) * 0.88).toFixed(3));
      return;
    }
    const max = Math.max(0, track.scrollWidth - view.clientWidth);
    track.style.transform = `translateX(${(-p * max).toFixed(1)}px)`;
    if (line) line.style.setProperty('--p', (0.12 + p * 0.88).toFixed(3));
  };
  addEventListener('scroll', tick, { passive: true }); addEventListener('resize', tick); tick();
}

export function initMotion(reduced) {
  initTimeline(reduced);
  initMarquee();
  initSlider();
  initAccordions();
  initScrub();
  initParallax(reduced);
  if (reduced) { document.querySelectorAll('.rv, .ekg, .bars').forEach(el => el.classList.add('is-in')); }
}
