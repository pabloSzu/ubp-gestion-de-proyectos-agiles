import fs from 'node:fs';
const base = 'GESTION-PROYECTOS-AGILES/entregables';
for (const n of [3,4,5]) {
  const file = `${base}/MODULO ${n}/Contenido/contenido.html`;
  let html = fs.readFileSync(file,'utf8');
  const para = (start, value) => {
    const match = [...html.matchAll(/<p>([\s\S]*?)<\/p>/g)].find(m => m[1].startsWith(start));
    if (!match) throw new Error(`M${n}: ${start}`);
    html = html.replace(match[0],`<p>${value}</p>`);
  };
  if(n === 3) html = html.replace('cuyo primer "MVP" no fue software funcional sino un video que mostraba cómo funcionaría el producto', 'que utilizó un video de demostración para comunicar una solución de sincronización y comprobar interés antes de ampliar su lanzamiento').replace('antes de construir la tecnología completa de sincronización de archivos','sin confundir registros interesados con uso sostenido o disposición a pagar');
  if(n === 4) {
    html = html.replace('lo que indica un ritmo estable','lo que muestra promedios cercanos; cinco observaciones no demuestran estabilidad estadística');
    para('Un ejemplo concreto: si un equipo de soporte técnico', 'Si cada persona tiene cinco tickets abiertos, empezar otro puede aumentar cambios de contexto y esperas. El equipo prueba un límite de dos ítems en progreso y ayuda a terminar antes de incorporar nuevos. Un ticket bloqueado sigue contando dentro de los límites del sistema: moverlo a “espera” no permite ocultar WIP. Se comparan tiempos y resultados antes y después de la prueba; el límite es una política para aprender y mejorar el flujo, no una garantía automática de reducción de demoras.');
    para('Además de estos mecanismos integrados', 'Un <strong>registro de riesgos vivo</strong> permite describir incertidumbres, probabilidad, impacto, responsable y respuesta. Evitar, mitigar, transferir y aceptar son estrategias útiles; también conviene reconocer oportunidades. La frecuencia de revisión responde a exposición y cambios, tanto en gestión ágil como predictiva. Si una integración externa amenaza el piloto, se investiga temprano, se acuerda una alternativa y se define cuándo escalar la decisión. Un bloqueo actual es un problema que requiere acción; su repetición futura puede permanecer como riesgo.');
    html = html.replace('https://www.youtube.com/watch?v=37zfyncCpkA','https://www.mountaingoatsoftware.com/videos').replace('Agile Estimating Explained: Story Points and Planning Poker','Agile Estimating Explained — Story Points and Planning Poker').replace('Mike Cohn desarrolla comparación, puntos de historia y Planning Poker con ejemplos, ideal para consolidar el razonamiento detrás de la técnica.','Mike Cohn desarrolla comparación, puntos y Planning Poker con ejemplos. En la biblioteca oficial, buscá este título dentro de “Estimating”; es un complemento de profundización, en inglés.');
    html = html.replace('Visibilidad de cambios de alcance</td><td>Confusa: la línea de pendiente sube sin distinguir la causa</td><td>Clara: la línea de alcance sube independientemente del avance','Visibilidad de cambios de alcance</td><td>El pendiente puede cambiar por alcance o reestimación</td><td>Separa alcance total de completado; requiere investigar la causa del cambio');
  }
  if(n === 5) {
    for(const [section,label,description] of [[1,'Personas y colaboración','Comprendé cómo componer el equipo, distribuir decisiones y sostener conversaciones útiles.'],[10,'Aprendizaje y mejora','Distinguí inspeccionar el producto de mejorar la forma de trabajar.'],[13,'Calidad y entrega','Conectá acuerdos de calidad con prácticas que permiten entregar cambios confiables.'],[16,'Organización y coordinación','Examiná dependencias y gobierno antes de elegir una estructura de escalado.']]) html = html.replace(`<h2>${section}.`, `<p><strong>Bloque ${label}.</strong> ${description}</p>\n<h2>${section}.`);
  }
  const sources = n === 5 ? '<li><a href="https://framework.scaledagile.com/planning-interval">SAFe: Planning Interval</a>. Terminología del horizonte de planificación.</li><li><a href="https://less.works/less/framework">LeSS Framework</a>. Coordinación de varios equipos sobre un producto.</li>' : n === 4 ? '<li><a href="https://www.scrum.org/resources/blog/myth-9-story-points-are-required-scrum">Scrum.org: Myth 9 — Story Points are Required in Scrum</a>. Distinción entre el marco y prácticas de estimación.</li>' : '';
  html = html.replace('<h2>Recursos audiovisuales sugeridos</h2>', `<h2>Fuentes para profundizar</h2><ul><li><a href="https://scrumguides.org/scrum-guide.html">The Scrum Guide</a> (Schwaber y Sutherland, 2020). Responsabilidades, artefactos, compromisos y eventos.</li>${sources}</ul>\n<h2>Recursos audiovisuales sugeridos</h2>`);
  fs.writeFileSync(file,html);
  console.log(`M${n}: ajustes finales aplicados`);
}
