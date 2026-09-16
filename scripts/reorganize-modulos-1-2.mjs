import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
function readModule(n) {
  const file = path.join(root, 'entregables', `MODULO ${n}`, 'Contenido', 'contenido.html');
  const source = fs.readFileSync(file, 'utf8');
  const match = /<article class="content">([\s\S]*?)<\/article>/.exec(source);
  if (!match) throw new Error('Falta article.content');
  const chunks = match[1].split(/(?=<h2>)/);
  return { file, source, intro: chunks.shift(), chunks };
}
function renameSection(section, number, title) {
  let out = section.replace(/<h2>[^<]+<\/h2>/, `<h2>${number}. ${title}</h2>`);
  out = out.replace(/<h3>\d+\.(\d+)\s/g, `<h3>${number}.$1 `);
  return out;
}
function writeModule(module, sections) {
  const before = module.source;
  const body = `${module.intro}\n${sections.join('\n')}`;
  let after = before.replace(/(<article class="content">)[\s\S]*?(<\/article>)/, `$1${body}$2`);
  const titles = [...body.matchAll(/<h2>\d+\. ([^<]+)<\/h2>/g)].map(m => m[1]);
  const items = titles.map(title => `<li>${title}</li>`).join('\n      ');
  after = after.replace(/(<nav class="chapter-map"[\s\S]*?<ol>)[\s\S]*?(<\/ol>)/, `$1\n      ${items}\n    $2`);
  for (const tag of ['figure', 'table', 'p']) {
    const re = new RegExp(`<${tag}(?:\\s|>)`, 'g');
    if ((before.match(re) || []).length !== (after.match(re) || []).length) throw new Error(`La reorganización cambió la cantidad de ${tag}`);
  }
  fs.writeFileSync(module.file, after);
  console.log(`Módulo ${module.file}: ${titles.length} secciones, recursos preservados`);
}

const m1 = readModule(1);
const byNumber = new Map(m1.chunks.filter(s => /<h2>\d+\./.test(s)).map(s => [Number(/<h2>(\d+)\./.exec(s)[1]), s]));
const m1Order = [
  [1, 'Concepto de proyecto y gestión de proyectos'],
  [2, 'Proyecto, producto y operación'],
  [90, 'Qué es la agilidad'],
  [91, 'Enfoques, metodologías y marcos de trabajo'],
  [3, 'Ciclo de vida y procesos de gestión de un proyecto'],
  [6, 'Gestión predictiva y modelo en cascada'],
  [7, 'Enfoques predictivos, iterativos e incrementales'],
  [4, 'Alcance, tiempo, costo y calidad'],
  [5, 'Quiénes participan en un proyecto: stakeholders y roles'],
  [8, 'Origen de la agilidad'],
  [9, 'El Manifiesto Ágil'],
  [10, 'Los 12 principios ágiles'],
  [11, 'Entrega de valor'],
  [12, 'Gestión del cambio en enfoques predictivos y ágiles'],
  [13, 'Comparación y selección de enfoques'],
];
if (byNumber.size !== m1Order.length) throw new Error('Estructura inesperada en Módulo 1');
const m1Sections = m1Order.map(([old, title], i) => {
  if (!byNumber.has(old)) throw new Error(`Falta sección ${old}`);
  return renameSection(byNumber.get(old), i + 1, title);
});
m1Sections.push(...m1.chunks.filter(s => !/<h2>\d+\./.test(s)));
writeModule(m1, m1Sections);

const m2 = readModule(2);
const m2ByNumber = new Map(m2.chunks.filter(s => /<h2>\d+\./.test(s)).map(s => [Number(/<h2>(\d+)\./.exec(s)[1]), s]));
let scrum = m2ByNumber.get(1);
if (!scrum || !m2ByNumber.has(90)) throw new Error('Estructura inesperada en Módulo 2');
const theoryStart = scrum.indexOf('<h3>1.1 El pilar');
const visualsStart = scrum.indexOf('<figure', theoryStart);
if (theoryStart < 0 || visualsStart < 0) throw new Error('No se pudo separar teoría y visión general');
let overview = scrum.slice(0, theoryStart) + scrum.slice(visualsStart);
const complex = /<p>La Guía de Scrum[\s\S]*?<\/p>/.exec(overview)?.[0];
if (!complex) throw new Error('Falta explicación de complejidad');
overview = overview.replace(complex, '').replace('<h3>1.3 Ejemplo inicial', '<h3>1.1 Ejemplo inicial');
const criterion = /<div class="criterio-profesional">[\s\S]*?<\/div>/.exec(overview)?.[0];
overview = overview.replace(criterion, '');
const theory = `<h2>91. Fundamentos de Scrum</h2>\n${complex}\n${criterion}\n${scrum.slice(theoryStart, visualsStart)}`;
m2ByNumber.set(1, overview);
m2ByNumber.set(91, theory);
const caseSection = m2.chunks.find(s => s.startsWith('<h2>Caso resuelto:'));
if (!caseSection) throw new Error('Falta caso resuelto de selección');
m2ByNumber.set(12, m2ByNumber.get(12) + '\n' + caseSection.replace('<h2>Caso resuelto:', '<h3>12.6 Caso resuelto:').replace('</h2>', '</h3>'));
const m2Order = [
  [90, 'Panorama de metodologías y marcos ágiles'],
  [1, 'Scrum: visión general y ejemplo de funcionamiento'],
  [2, 'Roles en Scrum'],
  [4, 'Artefactos y compromisos de Scrum'],
  [3, 'Eventos de Scrum y desarrollo de un Sprint'],
  [91, 'Fundamentos de Scrum: empirismo y valores'],
  [5, 'Kanban: origen, principios y visualización'],
  [6, 'Flujo de trabajo y límites WIP en Kanban'],
  [7, 'Extreme Programming (XP) y prácticas de desarrollo'],
  [8, 'Lean aplicado al desarrollo de software'],
  [9, 'Scrumban y Scrum con Kanban'],
  [10, 'Otros enfoques ágiles: Crystal, FDD y DSDM'],
  [11, 'Comparación entre metodologías y marcos ágiles'],
  [12, 'Selección del enfoque y caso resuelto'],
];
if (m2ByNumber.size !== m2Order.length) throw new Error('Secciones de Módulo 2 sin incluir');
const m2Sections = m2Order.map(([old, title], i) => renameSection(m2ByNumber.get(old), i + 1, title));
m2Sections.push(...m2.chunks.filter(s => !/<h2>\d+\./.test(s) && s !== caseSection));
writeModule(m2, m2Sections);
