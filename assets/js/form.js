// Enquiry form: inline validation, honeypot, no reload. The endpoint is one function below.

/**
 * sendEnquiry — swap this for the real endpoint.
 * `data` is a plain object: { name, phone, email, type, message, consent }.
 * Return { ok: true } or { ok: false, error: 'message' }.
 *
 * Web3Forms example:
 *   const r = await fetch('https://api.web3forms.com/submit', { method: 'POST',
 *     headers: { 'Content-Type': 'application/json' },
 *     body: JSON.stringify({ access_key: 'YOUR_KEY', subject: `Enquiry: ${data.type}`, ...data }) });
 *   return { ok: r.ok };
 * PHP mail example: fetch('/enquiry.php', { method: 'POST', body: new URLSearchParams(data) })
 */
async function sendEnquiry(data) {
  await new Promise(r => setTimeout(r, 600)); // TODO: replace with the real request
  console.info('Enquiry (stub, not sent):', data);
  return { ok: true };
}

const RULES = {
  name: v => v.trim().length >= 2 || 'Please enter your name.',
  phone: v => { const d = v.replace(/\D/g, ''); return (/^\+?[\d\s()-]+$/.test(v.trim()) && d.length >= 10 && d.length <= 13) || 'Please enter a phone number we can call.'; },
  email: v => !v.trim() || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) || 'That email address does not look right.',
  type: v => !!v || 'Please choose what the enquiry is about.',
  message: v => v.trim().length >= 10 || 'Please tell us a little more (at least 10 characters).',
  consent: (v, el) => el.checked || 'Please agree so we can contact you back.',
};

export function initForm() {
  document.querySelectorAll('form[data-enquiry]').forEach(form => {
    form.noValidate = true;
    const msg = form.querySelector('.form__msg');
    // pre-select from ?type=corporate etc.
    const wanted = new URLSearchParams(location.search).get('type');
    const type = form.elements.type;
    if (wanted && type && [...type.options].some(o => o.value === wanted)) type.value = wanted;

    const validate = el => {
      const rule = RULES[el.name]; if (!rule) return true;
      const res = rule(el.value, el);
      const field = el.closest('.field'), err = field.querySelector('.field__err');
      field.classList.toggle('is-invalid', res !== true);
      err.textContent = res === true ? '' : res;
      el.setAttribute('aria-invalid', res !== true);
      return res === true;
    };
    form.querySelectorAll('[name]').forEach(el => {
      if (el.name === 'website') return;
      el.addEventListener('blur', () => validate(el));
      el.addEventListener('input', () => { if (el.closest('.field').classList.contains('is-invalid')) validate(el); });
    });

    form.addEventListener('submit', async e => {
      e.preventDefault();
      msg.textContent = ''; msg.className = 'form__msg';
      if (form.elements.website && form.elements.website.value) return; // honeypot: silently drop
      const fields = [...form.querySelectorAll('[name]')].filter(el => el.name !== 'website');
      const bad = fields.filter(el => !validate(el));
      if (bad.length) { bad[0].focus(); return; }
      const btn = form.querySelector('[type="submit"]');
      btn.disabled = true; const label = btn.textContent; btn.textContent = 'Sending';
      const data = Object.fromEntries(fields.map(el => [el.name, el.type === 'checkbox' ? el.checked : el.value.trim()]));
      const res = await sendEnquiry(data).catch(() => ({ ok: false }));
      btn.disabled = false; btn.textContent = label;
      if (res.ok) {
        form.reset();
        msg.textContent = 'Thank you. We have your enquiry and will call or write back within one working day.';
        msg.classList.add('is-ok');
      } else {
        msg.textContent = 'The message could not be sent. Please call 011-41676655 or WhatsApp 92126 46655.';
        msg.classList.add('is-err');
      }
      msg.focus();
    });
  });
}
