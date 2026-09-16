const fs = require('fs');
const os = require('os');
const path = require('path');
const HTMLtoDOCX = require('html-to-docx');
const { chromium } = require('playwright');
const { WORD_CSS, MODULE_PALETTES, dataUri, patchWordStyles, findBrowser } = require('./render-contenido-word');
const JSZip = require('jszip');

const ROOT = path.resolve(__dirname, '..');
const OUTPUT_DIR = path.join(ROOT, 'output');
const MODULES = [
  { number: 1, title: 'Gestión de Proyectos y Fundamentos de Agilidad', accent: '#2878a9' },
  { number: 2, title: 'Metodologías y Marcos de Trabajo Ágiles', accent: '#16877b' },
  { number: 3, title: 'Planificación Ágil y Gestión del Producto', accent: '#76549f' },
  { number: 4, title: 'Estimación, Ejecución y Seguimiento del Proyecto', accent: '#c68a24' },
  { number: 5, title: 'Equipos, Liderazgo, Mejora Continua y Casos de Estudio', accent: '#c25555' },
];

function extractArticle(source) {
  const article = /<article class="content">([\s\S]*?)<\/article>/i.exec(source)?.[1];
  if (!article) throw new Error('No se encontró article.content');
  return article;
}

function transformBody(source, htmlPath) {
  let body = extractArticle(source);
  body = body.replace(/src="assets\/([^"]+)"/gi, (_match, filename) =>
    `src="${dataUri(path.join(path.dirname(htmlPath), 'assets', filename))}"`);
  body = body.replace(/<div class="criterio-profesional">([\s\S]*?)<\/div>/gi,
    '<table><tbody><tr><td style="background-color:#e8f6f3;border-left:5pt solid #16877b;padding:10pt;font-family:Arial,sans-serif;font-size:9.5pt;">$1</td></tr></tbody></table>');
  body = body.replace(/<div class="mito">([\s\S]*?)<\/div>/gi,
    '<table><tbody><tr><td style="background-color:#fbeeee;border-left:5pt solid #c25555;padding:10pt;font-family:Arial,sans-serif;font-size:9.5pt;">$1</td></tr></tbody></table>');
  body = body.replace(/<ul class="recursos-audiovisuales">([\s\S]*?)<\/ul>/gi, (_match, items) =>
    items.replace(/<li>([\s\S]*?)<\/li>/gi,
      '<table><tbody><tr><td style="background-color:#fffafa;border-left:5pt solid #c25555;padding:9pt;font-family:Arial,sans-serif;font-size:9.5pt;">$1</td></tr></tbody></table>'));
  body = body.replace(/<figcaption>([\s\S]*?)<\/figcaption>/gi,
    '<p class="figure-caption" style="font-family:Arial,sans-serif;font-size:8.5pt;line-height:1.35;color:#536173;background-color:#fbf8f1;padding:7pt;margin:0 0 13pt;text-align:left;">$1</p>');
  body = body.replace(/<table([^>]*)>\s*<caption>([\s\S]*?)<\/caption>/gi, '<p style="font-family:Arial,sans-serif;font-size:9pt;color:#536173;text-align:left;"><strong>$2</strong></p><table$1>');
  body = body.replace(/<\/?figure(?:\s[^>]*)?>/gi, '');
  body = body.replace(/<img([^>]*?)>/gi, '<img$1 width="640" style="width:640px;height:auto">');
  body = body.replace(/width="640" style="width:640px;height:auto"([^>]*?)width="640" style="width:640px;height:auto"/gi,
    'width="640" style="width:640px;height:auto"$1');
  return body;
}

function contentsHtml() {
  const rows = MODULES.map((module) =>
    `<tr><td style="width:52pt;text-align:center;background-color:${module.accent};color:#ffffff;font-size:17pt;font-weight:bold;">${String(module.number).padStart(2, '0')}</td><td><p style="margin:0;text-align:left;"><strong>Módulo ${module.number}</strong></p><p style="margin:0;text-align:left;">${module.title}</p></td></tr>`
  ).join('');
  return `<section style="page-break-after:always;">
    <p style="font-family:Arial,sans-serif;font-size:8pt;letter-spacing:1.5pt;color:#536173;text-transform:uppercase;margin:0 0 8pt;">Gestión de Proyectos Ágiles</p>
    <h1 style="font-family:Georgia,serif;font-size:25pt;color:#173f67;margin:0 0 10pt;">Recorrido de la materia</h1>
    <p style="font-size:12pt;color:#374657;text-align:left;margin:0 0 18pt;">Cinco módulos conectados para pasar de los fundamentos de un proyecto a la toma de decisiones, la entrega de valor y el aprendizaje organizacional.</p>
    <table style="font-family:Arial,sans-serif;font-size:10pt;">${rows}</table>
    <h2>Cómo aprovechar este manual</h2>
    <p>Primero comprendé qué problema plantea cada sección; después estudiá sus conceptos y contrastalos con el ejemplo. Los diagramas muestran relaciones, las tablas comparan alternativas y los casos resueltos hacen visible el razonamiento. Las cajas de criterio profesional te ayudan a decidir cuando una receta no alcanza.</p>
    <ol><li><strong>Fundamentos.</strong> Distinguí proyecto, producto y operación, y comprendé por qué la incertidumbre cambia la forma de gestionar.</li><li><strong>Enfoques.</strong> Compará Scrum, Kanban y otras propuestas antes de asumir que agilidad significa usar Scrum.</li><li><strong>Producto.</strong> Conectá necesidades, prioridades y aprendizaje con decisiones de planificación.</li><li><strong>Ejecución.</strong> Separá estimación, capacidad y pronóstico; observá el flujo y gestioná riesgos.</li><li><strong>Personas y organización.</strong> Integrá colaboración, calidad, mejora y gobierno. El caso final de TurnoYa reúne el recorrido completo.</li></ol>
    <p><strong>Una distinción que atraviesa la materia.</strong> El proyecto tiene un propósito y un cierre; el producto puede seguir evolucionando. Scrum ayuda a desarrollar productos y no reemplaza por sí solo contratos, presupuesto, cumplimiento ni gobierno. Historias de usuario, puntos y Planning Poker son prácticas que podés elegir, no obligaciones universales.</p>
    <p style="color:#536173;font-size:9.5pt;text-align:left;">Al cerrar cada módulo, volvé a su síntesis: explicá una decisión del caso con tus palabras, reconocé sus supuestos y considerá qué evidencia te haría cambiarla. Los videos son complementarios; el texto desarrolla los conceptos necesarios para estudiar.</p>
  </section>`;
}

async function makeBookCover(page, workDir) {
  const coverArt = dataUri(path.join(OUTPUT_DIR, 'assets', 'portada-ebook-gestion-proyectos-agiles.png'));
  await page.setViewportSize({ width: 794, height: 1123 });
  await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>
    *{box-sizing:border-box}body{margin:0}.book-cover{width:794px;height:1123px;position:relative;overflow:hidden;background:#102d4a;font-family:Arial,sans-serif;color:#fff}.book-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,39,64,.92) 0%,rgba(12,39,64,.67) 33%,rgba(12,39,64,.08) 62%,rgba(12,39,64,.28) 100%)}.copy{position:absolute;left:72px;right:72px;top:68px}.eyebrow{font-size:14px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:#f2bd55;margin-bottom:20px}.title{font-family:Georgia,serif;font-size:52px;line-height:1.05;max-width:610px;margin:0 0 18px}.subtitle{font-family:Georgia,serif;font-size:21px;line-height:1.4;max-width:590px;color:rgba(255,255,255,.9);font-style:italic}.meta{position:absolute;left:72px;bottom:56px;font-size:14px;letter-spacing:1.4px;text-transform:uppercase;color:rgba(255,255,255,.9);border-top:1px solid rgba(255,255,255,.55);padding-top:14px;width:650px}
  </style></head><body><section class="book-cover"><img src="${coverArt}" alt=""><div class="veil"></div><div class="copy"><div class="eyebrow">Universidad Blas Pascal</div><h1 class="title">Gestión de Proyectos Ágiles</h1><div class="subtitle">Fundamentos, marcos de trabajo, planificación, ejecución y liderazgo para entregar valor en contextos de incertidumbre.</div></div><div class="meta">Material integral de estudio · Módulos 1 a 5</div></section></body></html>`);
  const output = path.join(workDir, 'portada-ebook.png');
  await page.locator('.book-cover').screenshot({ path: output });
  return output;
}

async function main() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  const workDir = fs.mkdtempSync(path.join(os.tmpdir(), 'ubp-ebook-'));
  const browser = await chromium.launch({ headless: true, executablePath: findBrowser() });
  const page = await browser.newPage({ viewport: { width: 1100, height: 1500 }, deviceScaleFactor: 1.5 });

  const bookCover = await makeBookCover(page, workDir);
  await page.setViewportSize({ width: 1100, height: 1500 });
  const parts = [`<p style="text-align:center;margin:0;"><img src="${dataUri(bookCover)}" width="640" style="width:640px;height:auto"></p><div class="page-break"></div>`, contentsHtml()];
  const links = [];

  for (const [moduleIndex, module] of MODULES.entries()) {
    const htmlPath = path.join(ROOT, 'entregables', `MODULO ${module.number}`, 'Contenido', 'contenido.html');
    const source = fs.readFileSync(htmlPath, 'utf8');
    await page.goto(new URL(`file:///${htmlPath.replace(/\\/g, '/')}`).href, { waitUntil: 'load', timeout: 60000 });
    const openerPath = path.join(workDir, `modulo-${module.number}-apertura.png`);
    await page.locator('.opener').screenshot({ path: openerPath });
    const pageBreakBefore = moduleIndex === 0 ? '' : '<div class="page-break"></div>';
    parts.push(`${pageBreakBefore}<p style="text-align:center;margin:0;"><img src="${dataUri(openerPath)}" width="640" style="width:640px;height:auto"></p><div class="page-break"></div><h1>Módulo ${module.number} · ${module.title}</h1>${transformBody(source, htmlPath)}`);
    for (const match of source.matchAll(/<a href="(https?:\/\/[^"']+)">([\s\S]*?)<\/a>/gi)) {
      links.push({ url: match[1], title: match[2].replace(/<[^>]+>/g, '').trim() });
    }
  }
  await browser.close();

  const completeHtml = `<!doctype html><html lang="es"><head><meta charset="utf-8">${WORD_CSS}</head><body>${parts.join('\n')}</body></html>`;
  fs.writeFileSync(path.join(OUTPUT_DIR, 'materia-completa.html'), completeHtml, 'utf8');
  const initial = await HTMLtoDOCX(completeHtml, null, {
    title: 'Gestión de Proyectos Ágiles',
    subject: 'Material integral de estudio de los módulos 1 a 5',
    creator: 'Universidad Blas Pascal',
    lastModifiedBy: 'Universidad Blas Pascal',
    lang: 'es-AR',
    font: 'Georgia',
    fontSize: 22,
    pageSize: { width: 11906, height: 16838 },
    margins: { top: 794, right: 794, bottom: 794, left: 794, header: 360, footer: 360 },
    footer: true,
    pageNumber: true,
    skipFirstHeaderFooter: true,
    table: { row: { cantSplit: true } },
  });
  const styled = await patchWordStyles(initial, links, '1');
  const zip = await JSZip.loadAsync(styled);
  let xml = await zip.file('word/document.xml').async('string');
  let active = 0;
  xml = xml.replace(/<w:p>[\s\S]*?<\/w:p>/g, p => {
    const title = [...p.matchAll(/<w:t[^>]*>([\s\S]*?)<\/w:t>/g)].map(m => m[1]).join('');
    const module = title.match(/^Módulo ([1-5]) · /);
    if (module) {
      active = Number(module[1]);
      p = p.replace('</w:pPr>', `<w:keepNext/><w:outlineLvl w:val="0"/></w:pPr>`);
      p = p.replace('</w:pPr>', `</w:pPr><w:bookmarkStart w:id="${900 + active}" w:name="GPA_Modulo_${active}"/><w:bookmarkEnd w:id="${900 + active}"/>`);
    }
    const palette = MODULE_PALETTES[String(active)];
    if (palette && /<w:pStyle w:val="Heading2"\/>/.test(p)) p = p.replace('</w:pPr>', `<w:shd w:val="clear" w:fill="${palette.fill}"/><w:pBdr><w:left w:val="single" w:sz="28" w:space="6" w:color="${palette.accent}"/></w:pBdr></w:pPr>`);
    if (palette && /<w:pStyle w:val="Heading[23]"\/>/.test(p)) p = p.replace(/<w:color w:val="[^"]+"\/>/g, `<w:color w:val="${/Heading2/.test(p) ? palette.ink : palette.secondaryInk}"/>`);
    if (!active && /^Módulo [1-5]$/.test(title)) p = p.replace(/(<w:r>[\s\S]*?<w:t[^>]*>Módulo ([1-5])<\/w:t>[\s\S]*?<\/w:r>)/, (_m, r, n) => `<w:hyperlink w:anchor="GPA_Modulo_${n}" w:history="1">${r}</w:hyperlink>`);
    return p;
  });
  zip.file('word/document.xml', xml);
  const buffer = await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' });
  const output = path.join(OUTPUT_DIR, 'GPA - materia-completa.docx');
  fs.writeFileSync(output, buffer);
  fs.rmSync(workDir, { recursive: true, force: true });
  console.log(`OK: ${output} (${Math.round(buffer.length / 1024)} KB)`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
