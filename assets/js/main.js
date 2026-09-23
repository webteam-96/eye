// Boot. Medic 128 chrome; Save a Child's Heart motion (preloader, reveals, EKG traces, marquee).
import { initNav } from './nav.js';
import { initMotion, startHero } from './motion.js';
import { initCounters } from './counters.js';

const html = document.documentElement;
html.classList.add('js');
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

// Preloader — olive screen, EKG draws, slides down after 1.2s. Once per session, skippable.
const loader = document.querySelector('.loader');
const finish = () => { html.classList.add('done'); startHero(); };
if (loader) {
  let seen = false;
  try { seen = !!sessionStorage.getItem('seen'); sessionStorage.setItem('seen', '1'); } catch (e) { /* private mode */ }
  if (reduced || seen) { loader.remove(); finish(); }
  else {
    let out = false;
    const leave = () => { if (out) return; out = true; loader.classList.add('is-out'); startHero(); setTimeout(() => { loader.remove(); html.classList.add('done'); }, 800); };
    setTimeout(leave, 1200);
    ['keydown', 'pointerdown', 'wheel', 'touchstart'].forEach(e => addEventListener(e, leave, { once: true, passive: true }));
  }
} else finish();

initNav();
initMotion(reduced);
initCounters(reduced);
if (document.querySelector('.gallery, a.js-lb')) import('./gallery.js').then(m => m.initGallery());
if (document.querySelector('form[data-enquiry]')) import('./form.js').then(m => m.initForm());

// Floating WhatsApp / call — enters after 2s (PRD §7).
const fab = document.querySelector('.fab');
if (fab) setTimeout(() => { fab.hidden = false; requestAnimationFrame(() => fab.classList.add('is-in')); }, 2000);

// Google Map: shown without a click, but injected only after the page has loaded so it never delays the first paint.
const mountMap = box => {
  if (box.querySelector('iframe')) return;
  const f = document.createElement('iframe');
  f.src = box.dataset.mapSrc || box.dataset.src; f.title = 'Map: ' + box.dataset.label; f.referrerPolicy = 'no-referrer-when-downgrade'; f.allowFullscreen = true;
  const ph = box.querySelector('.mapbox__in'); if (ph) ph.replaceWith(f); else box.appendChild(f);
};
const autoMaps = document.querySelectorAll('[data-map-src]');
if (autoMaps.length) {
  const go = () => setTimeout(() => autoMaps.forEach(mountMap), 1200);
  if (document.readyState === 'complete') go(); else addEventListener('load', go, { once: true });
}

// Deferred Google Map: nothing loads until asked for.
document.querySelectorAll('.mapbox__load').forEach(btn => btn.addEventListener('click', () => {
  const box = btn.closest('.mapbox');
  const f = document.createElement('iframe');
  f.src = box.dataset.src; f.title = 'Map: ' + box.dataset.label; f.loading = 'lazy'; f.referrerPolicy = 'no-referrer-when-downgrade'; f.allowFullscreen = true;
  box.querySelector('.mapbox__in').replaceWith(f);
}));

document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
document.querySelectorAll('[data-since]').forEach(el => { const y = new Date().getFullYear() - Number(el.dataset.since); el.dataset.count = y; el.textContent = y; });
