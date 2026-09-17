// Mobile menu: Medic's dropdown panel under the navbar. Focus trap shared with the lightbox.
const FOCUSABLE = 'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])';

export function trapFocus(container, onEscape) {
  const keydown = e => {
    if (e.key === 'Escape') { onEscape(); return; }
    if (e.key !== 'Tab') return;
    const items = [...container.querySelectorAll(FOCUSABLE)].filter(el => el.offsetParent !== null);
    if (!items.length) return;
    const first = items[0], last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  };
  container.addEventListener('keydown', keydown);
  return () => container.removeEventListener('keydown', keydown);
}

export function initNav() {
  const burger = document.querySelector('.navbar__burger');
  const menu = document.querySelector('.nav-menu');
  if (!burger || !menu) return;
  const open = () => { menu.classList.add('is-open'); burger.setAttribute('aria-expanded', 'true'); burger.setAttribute('aria-label', 'Close menu'); };
  const close = () => { menu.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', 'Open menu'); };
  burger.addEventListener('click', () => (menu.classList.contains('is-open') ? close() : open()));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu.classList.contains('is-open')) { close(); burger.focus(); } });
  document.addEventListener('click', e => { if (menu.classList.contains('is-open') && !e.target.closest('.navbar')) close(); });
  matchMedia('(min-width: 992px)').addEventListener('change', e => { if (e.matches) close(); });
}
