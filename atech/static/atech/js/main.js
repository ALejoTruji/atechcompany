/* ═══════════════════════════════════════
   ATech – main.js
═══════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Navbar: scroll effect ──────────────── */
  const nav = document.getElementById('mainNav');
  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Active nav link on scroll ─────────── */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.classList.toggle(
            'active',
            link.getAttribute('href') === '#' + entry.target.id
          );
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => observer.observe(s));

  /* ── Back-to-top button ─────────────────── */
  const btn = document.getElementById('backToTop');
  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ── Smooth close navbar on mobile ──────── */
  const navbarCollapse = document.querySelector('#navbarNav');
  document.querySelectorAll('#navbarNav .nav-link').forEach(link => {
    link.addEventListener('click', () => {
      if (navbarCollapse.classList.contains('show')) {
        bootstrap.Collapse.getInstance(navbarCollapse)?.hide();
      }
    });
  });

  /* ── Form submit loading state ──────────── */
  const form = document.querySelector('form[method="POST"]');
  if (form) {
    form.addEventListener('submit', () => {
      const btn = form.querySelector('.btn-submit');
      const textSpan = btn.querySelector('.btn-text');
      const loadSpan = btn.querySelector('.btn-loading');
      if (textSpan && loadSpan) {
        btn.disabled = true;
        textSpan.classList.add('d-none');
        loadSpan.classList.remove('d-none');
      }
    });
  }

  /* ── Fade-in on scroll (lightweight AOS) ── */
  const aosElements = document.querySelectorAll('[data-aos]');
  const aosObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = el.dataset.aosDelay || 0;
        setTimeout(() => el.classList.add('aos-animate'), parseInt(delay));
        aosObserver.unobserve(el);
      }
    });
  }, { threshold: 0.15 });

  aosElements.forEach(el => {
    el.classList.add('aos-init');
    aosObserver.observe(el);
  });

});
