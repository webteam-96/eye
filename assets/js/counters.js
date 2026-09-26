// Counters: count up once on first view, never again. Indian grouping (5,00,000).
// The HTML holds the final value, so no JS = final value; width is reserved so nothing shifts.
// Attributes: data-count (end value), data-suffix (e.g. "+", "K+"), data-decimals (optional, default 0: 1.5K+ uses 1).
const fmts = {};
const fmt = d => fmts[d] || (fmts[d] = new Intl.NumberFormat('en-IN', { minimumFractionDigits: d, maximumFractionDigits: d }));

export function initCounters(reduced) {
  const els = document.querySelectorAll('[data-count]');
  if (!els.length || reduced || !('IntersectionObserver' in window)) return;
  const ease = t => 1 - Math.pow(1 - t, 3);
  const run = el => {
    const end = Number(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const dec = Math.min(3, Math.max(0, parseInt(el.dataset.decimals, 10) || 0));
    const step = Math.pow(10, dec);
    const final = el.textContent;
    el.style.minWidth = el.offsetWidth + 'px';
    el.setAttribute('aria-hidden', 'true');
    const sr = document.createElement('span'); sr.className = 'sr-only'; sr.textContent = final;
    el.after(sr);
    const t0 = performance.now(), d = 800;
    const tick = now => {
      const p = Math.max(0, Math.min(1, (now - t0) / d)); // a frame stamped before t0 would give -0
      el.textContent = fmt(dec).format(Math.round(end * ease(p) * step) / step) + suffix;
      if (p < 1) requestAnimationFrame(tick);
      else { el.textContent = final; el.removeAttribute('aria-hidden'); sr.remove(); el.style.minWidth = ''; }
    };
    requestAnimationFrame(tick);
  };
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) { run(e.target); io.unobserve(e.target); }
  }), { threshold: 0.5 });
  els.forEach(el => io.observe(el));
}
