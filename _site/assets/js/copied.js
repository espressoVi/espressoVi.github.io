document.addEventListener('click', (e) => {
  // Accept clicks on the <i> icon *or* the surrounding button
  const btn = e.target.closest('.copy-bib');
  if (!btn) return;

  const bib = btn.dataset.bib.replace(/&quot;/g, '"');

  navigator.clipboard.writeText(bib).then(() => {
    const originalHTML = btn.innerHTML;          // <-- keep icon + label
    btn.innerHTML = '<i class="fas fa-check"></i> Copied!';  // ✔ icon
    btn.classList.add('copied');                 // optional colour change

    setTimeout(() => {
      btn.innerHTML = originalHTML;              // restore icon + label
      btn.classList.remove('copied');
    }, 1500);
  });
});
