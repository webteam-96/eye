// Lightbox: keyboard (arrows, Escape), swipe on touch, focus trapped. No library.
import { trapFocus } from './nav.js';

export function initGallery() {
  const links = [...document.querySelectorAll('.gallery a')];
  if (!links.length) return;
  const lb = document.createElement('div');
  lb.className = 'lb'; lb.setAttribute('data-lenis-prevent', ''); lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Photo viewer'); lb.hidden = true;
  lb.innerHTML = `
    <div class="lb__bar"><span class="lb__count t-5"></span><button type="button" class="lb__close">Close</button></div>
    <figure class="lb__stage" aria-live="polite"><img alt="" draggable="false"><figcaption></figcaption></figure>
    <div class="lb__nav"><button type="button" class="lb__prev" aria-label="Previous photo">Previous</button><button type="button" class="lb__next" aria-label="Next photo">Next</button></div>`;
  document.body.append(lb);
  const img = lb.querySelector('img'), cap = lb.querySelector('figcaption'), count = lb.querySelector('.lb__count');
  let i = 0, release = null, opener = null;

  const show = n => {
    i = (n + links.length) % links.length;
    const a = links[i];
    img.src = a.href; img.alt = a.dataset.alt || a.querySelector('img')?.alt || '';
    cap.textContent = a.dataset.caption || '';
    count.textContent = `${i + 1} of ${links.length}`;
  };
  const open = n => {
    opener = document.activeElement;
    show(n); lb.hidden = false; document.body.style.overflow = 'hidden'; document.documentElement.style.overflow = 'hidden';
    requestAnimationFrame(() => lb.classList.add('is-in'));
    release = trapFocus(lb, close);
    lb.querySelector('.lb__close').focus();
    lb.addEventListener('keydown', keys);
  };
  const close = () => {
    lb.classList.remove('is-in'); lb.hidden = true; document.body.style.overflow = ''; document.documentElement.style.overflow = '';
    if (release) release(); lb.removeEventListener('keydown', keys);
    if (opener) opener.focus();
  };
  const keys = e => { if (e.key === 'ArrowRight') show(i + 1); if (e.key === 'ArrowLeft') show(i - 1); };

  links.forEach((a, n) => a.addEventListener('click', e => { e.preventDefault(); open(n); }));
  lb.querySelector('.lb__close').addEventListener('click', close);
  lb.querySelector('.lb__prev').addEventListener('click', () => show(i - 1));
  lb.querySelector('.lb__next').addEventListener('click', () => show(i + 1));
  lb.addEventListener('click', e => { if (e.target === lb) close(); });

  // swipe
  let x0 = null;
  const stage = lb.querySelector('.lb__stage');
  stage.addEventListener('dragstart', e => e.preventDefault()); // native image drag would cancel the pointer
  stage.addEventListener('pointerdown', e => { x0 = e.clientX; });
  stage.addEventListener('pointerup', e => {
    if (x0 === null) return;
    const dx = e.clientX - x0; x0 = null;
    if (Math.abs(dx) > 40) show(dx < 0 ? i + 1 : i - 1);
  });
}
