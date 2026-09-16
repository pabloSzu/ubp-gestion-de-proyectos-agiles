const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

function mdInlineToHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
}

function mdToHtml(md, title) {
  const lines = md.split(/\r?\n/).filter((l) => l.trim().length > 0);
  const items = lines
    .map((l) => l.replace(/^-\s*/, '').trim())
    .filter(Boolean)
    .map((l) => `<li>${mdInlineToHtml(l)}</li>`)
    .join('\n');
  return `<h1 class="no-break">${title}</h1><ul>${items}</ul>`;
}

function main() {
  const mdPath = process.argv[2];
  const docxPath = process.argv[3];
  const title = process.argv[4] || path.basename(mdPath, '.md');
  if (!mdPath || !docxPath) {
    throw new Error('Uso: node scripts/md-to-docx.js <entrada.md> <salida.docx> [titulo]');
  }
  const md = fs.readFileSync(mdPath, 'utf8');
  const html = `<!DOCTYPE html><body>${mdToHtml(md, title)}</body>`;
  const tmpHtml = mdPath.replace(/\.md$/, '.tmp.html');
  fs.writeFileSync(tmpHtml, html, 'utf8');
  execFileSync('node', [path.join(__dirname, 'render-docx.js'), tmpHtml, docxPath], { stdio: 'inherit' });
  fs.unlinkSync(tmpHtml);
}

main();
