/* Dependency-free interaction layer for Raja Roy's portfolio. */
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const toast = document.querySelector('.toast');
let toastTimer;
function announce(message) {
  clearTimeout(toastTimer);
  toast.textContent = message;
  toast.classList.add('visible');
  toastTimer = setTimeout(() => toast.classList.remove('visible'), 2600);
}
const copyButton = document.querySelector('[aria-label="Copy email address"]');
copyButton?.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(copyButton.dataset.email);
    copyButton.textContent = 'copied!';
    announce('Email address copied');
    setTimeout(() => { copyButton.textContent = 'copy'; }, 2200);
  } catch {
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('.email-link'));
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    announce('Copy the highlighted email address');
  }
});
document.querySelector('[aria-label="Back to top"]')?.addEventListener('click', () => {
  window.scrollTo({top: 0, behavior: reducedMotion.matches ? 'instant' : 'smooth'});
  history.replaceState(null, '', location.pathname);
  document.querySelector('.brand').focus({preventScroll: true});
});
const navLinks = [...document.querySelectorAll('nav a[href^="#"]')];
const sections = [...document.querySelectorAll('main section[id]')];
let scheduled = false;
function updateNavigation() {
  const threshold = innerWidth <= 700 ? 150 : 115;
  const current = [...sections].reverse().find(section => section.getBoundingClientRect().top <= threshold);
  for (const link of navLinks) {
    if (link.hash === '#' + current?.id) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  scheduled = false;
}
function scheduleNavigation() {
  if (!scheduled) { scheduled = true; requestAnimationFrame(updateNavigation); }
}
addEventListener('scroll', scheduleNavigation, {passive: true});
addEventListener('resize', scheduleNavigation);
addEventListener('hashchange', scheduleNavigation);
updateNavigation();
