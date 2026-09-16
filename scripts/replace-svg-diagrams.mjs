import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

const assetsByModule = {
  1: [
    'diagrama-ciclo-vida-editorial.png',
    'diagrama-triple-restriccion-editorial.png',
    'diagrama-enfoques-editorial.png',
  ],
  2: [
    'diagrama-scrum-sistema-editorial.png',
    'diagrama-seleccion-enfoques-editorial.png',
  ],
  3: [
    'diagrama-vision-evidencia-editorial.png',
    'diagrama-ready-done-editorial.png',
  ],
  4: [
    'diagrama-horizontes-estimacion-editorial.png',
    'diagrama-metricas-decision-editorial.png',
  ],
  5: [
    'diagrama-liderazgo-equipo-editorial.png',
    'diagrama-kaizen-editorial.png',
  ],
};

function escapeAttribute(value) {
  return value.replaceAll('&', '&amp;').replaceAll('"', '&quot;');
}

for (const [moduleNumber, assets] of Object.entries(assetsByModule)) {
  const htmlPath = path.join(root, 'entregables', `MODULO ${moduleNumber}`, 'Contenido', 'contenido.html');
  let html = fs.readFileSync(htmlPath, 'utf8');
  const figures = [...html.matchAll(/<figure class="diagrama-conceptual">([\s\S]*?)<\/figure>/gi)];

  if (figures.length === 0 && assets.every((asset) => html.includes(asset))) {
    console.log(`Módulo ${moduleNumber}: ya actualizado`);
    continue;
  }
  if (figures.length !== assets.length) {
    throw new Error(`Módulo ${moduleNumber}: se esperaban ${assets.length} SVG y se encontraron ${figures.length}`);
  }

  let index = 0;
  html = html.replace(/<figure class="diagrama-conceptual">([\s\S]*?)<\/figure>/gi, (_figure, inner) => {
    const aria = /aria-label="([^"]+)"/i.exec(inner)?.[1];
    const caption = /<figcaption>([\s\S]*?)<\/figcaption>/i.exec(inner)?.[1];
    if (!aria || !caption) throw new Error(`Módulo ${moduleNumber}: figura ${index + 1} incompleta`);
    const asset = assets[index++];
    return `<figure class="diagrama-conceptual image-figure visual-editorial">\n<img src="assets/${asset}" alt="${escapeAttribute(aria)}">\n<figcaption>${caption}</figcaption>\n</figure>`;
  });

  if (!html.includes('.visual-editorial img{')) {
    html = html.replace(
      '.image-figure img{ width:100%; display:block; aspect-ratio:16/9; object-fit:cover; }',
      '.image-figure img{ width:100%; display:block; aspect-ratio:16/9; object-fit:cover; }\n.visual-editorial{ border-color:#cad8e5; box-shadow:0 10px 28px rgba(21,52,80,.14); }\n.visual-editorial img{ width:100%; display:block; aspect-ratio:16/9; object-fit:cover; background:#fff; }'
    );
  }

  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log(`Módulo ${moduleNumber}: ${assets.length} diagramas reemplazados`);
}
