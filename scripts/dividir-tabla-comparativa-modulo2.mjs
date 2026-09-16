import fs from 'node:fs';
const file = 'GESTION-PROYECTOS-AGILES/entregables/MODULO 2/Contenido/contenido.html';
let html = fs.readFileSync(file, 'utf8');
const table = html.match(/<table[^>]*>\s*<caption>Tabla 4\. Comparación entre Scrum, Kanban, XP, Lean y Scrumban<\/caption>[\s\S]*?<\/table>/)?.[0];
if (!table) throw new Error('No se encontró la tabla original de seis columnas.');
const rows = [...table.matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(row => [...row[1].matchAll(/<(th|td)(?: [^>]*)?>([\s\S]*?)<\/\1>/g)].map(cell => cell[2]));
if (rows.some(row => row.length !== 6)) throw new Error('La tabla debe tener seis columnas.');
function subset(columns, caption) {
  return `<table class="tabla-comparativa">\n<caption>${caption}</caption>\n<thead><tr>${columns.map(c => `<th scope="col">${rows[0][c]}</th>`).join('')}</tr></thead>\n<tbody>\n${rows.slice(1).map(row => `<tr>${columns.map(c => `<td>${row[c]}</td>`).join('')}</tr>`).join('\n')}\n</tbody>\n</table>`;
}
const replacement = '<p>Para facilitar la lectura, la comparación se presenta en dos tablas que mantienen las mismas dimensiones. Leé una misma fila en ambas para contrastar los cinco enfoques.</p>\n' + subset([0, 1, 2, 3], 'Tabla 4A. Comparación: Scrum, Kanban y XP') + '\n\n' + subset([0, 4, 5], 'Tabla 4B. Comparación: Lean y Scrumban');
html = html.replace(table, replacement);
fs.writeFileSync(file, html);
console.log('Comparación dividida sin pérdida de celdas.');
