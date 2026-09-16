const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const MODULES = [1, 2, 3, 4, 5];

function readBody(htmlPath) {
  const raw = fs.readFileSync(htmlPath, 'utf8');
  return /<body[^>]*>([\s\S]*)<\/body>/i.exec(raw)?.[1] ?? raw;
}

function main() {
  const parts = [];
  for (const n of MODULES) {
    const htmlPath = path.join(ROOT, 'entregables', `MODULO ${n}`, 'Contenido', 'contenido.html');
    if (!fs.existsSync(htmlPath)) {
      console.warn(`Falta: ${htmlPath} (se omite)`);
      continue;
    }
    parts.push(readBody(htmlPath));
  }

  const combined = parts.join('\n<div style="page-break-before: always;"></div>\n');
  const outHtmlDir = path.join(ROOT, 'output');
  fs.mkdirSync(outHtmlDir, { recursive: true });
  const outHtml = path.join(outHtmlDir, 'materia-completa.html');
  fs.writeFileSync(
    outHtml,
    `<!DOCTYPE html><html><head><meta charset="utf-8"><title>Gestion de Proyectos Agiles</title></head><body>${combined}</body></html>`,
    'utf8'
  );

  execFileSync('node', [path.join(__dirname, 'render-materia-word.js')], { stdio: 'inherit' });
}

main();
