const fs = require('fs');
const path = require('path');
const HTMLtoDOCX = require('html-to-docx');

const STYLE = `
<style>
  body { font-family: Calibri, Arial, sans-serif; font-size: 11pt; line-height: 1.5; color: #1a1a1a; }
  h1 { font-size: 22pt; color: #1f3864; page-break-before: always; margin-top: 0; }
  h1.no-break { page-break-before: avoid; }
  h2 { font-size: 16pt; color: #2e5395; margin-top: 22pt; }
  h3 { font-size: 13pt; color: #333; margin-top: 14pt; }
  p { text-align: justify; }
  table { border-collapse: collapse; width: 100%; margin: 10pt 0; }
  table, th, td { border: 1px solid #999; }
  th, td { padding: 6pt 8pt; font-size: 10pt; }
  th { background: #dbe5f1; }
  blockquote { border-left: 3px solid #2e5395; margin: 10pt 0; padding: 6pt 12pt; background: #f2f6fb; font-style: italic; }
  ul, ol { margin: 6pt 0 6pt 18pt; }
  code { font-family: Consolas, monospace; background: #f0f0f0; padding: 1pt 3pt; }
</style>`;

async function renderOne(htmlPath, docxPath) {
  const raw = fs.readFileSync(htmlPath, 'utf8');
  const body = /<body[^>]*>([\s\S]*)<\/body>/i.exec(raw)?.[1] ?? raw;
  const html = `<!DOCTYPE html><html><head><meta charset="utf-8">${STYLE}</head><body>${body}</body></html>`;
  const buffer = await HTMLtoDOCX(html, null, {
    footer: false,
    pageNumber: true,
    margins: { top: 1134, right: 1134, bottom: 1134, left: 1134 },
  });
  fs.mkdirSync(path.dirname(docxPath), { recursive: true });
  fs.writeFileSync(docxPath, buffer);
  console.log(`OK: ${docxPath} (${(buffer.length / 1024).toFixed(0)} KB)`);
}

async function main() {
  const htmlPath = process.argv[2];
  const docxPath = process.argv[3];
  if (!htmlPath || !docxPath) {
    throw new Error('Uso: node scripts/render-docx.js <entrada.html> <salida.docx>');
  }
  await renderOne(htmlPath, docxPath);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
