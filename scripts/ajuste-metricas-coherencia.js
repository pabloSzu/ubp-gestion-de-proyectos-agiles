const fs=require('fs'),path=require('path'),Zip=require('jszip');
const root=path.resolve(__dirname,'..');
const old='Usar las métricas exclusivamente con fines de mejora del propio equipo, nunca para comparar personas o equipos entre sí, y priorizar métricas de valor entregado y de satisfacción del cliente por sobre métricas puramente de actividad interna.';
const updated='No usar velocity para evaluar personas ni rankear equipos. Elegir métricas según la decisión: aprendizaje del equipo, valor del producto o desempeño del servicio. Toda comparación organizacional requiere contexto y límites equivalentes.';
(async()=>{
  for(const relative of ['entregables/MODULO 5/Contenido/contenido.html','output/materia-completa.html']) {
    const file=path.join(root,relative),text=fs.readFileSync(file,'utf8');
    if(!text.includes(old))throw new Error(`Falta texto en ${relative}`);
    fs.writeFileSync(file,text.replace(old,updated));
  }
  for(const relative of ['entregables/MODULO 5/Contenido/Contenido.docx','output/GPA - materia-completa.docx']) {
    const file=path.join(root,relative),zip=await Zip.loadAsync(fs.readFileSync(file));
    const xml=await zip.file('word/document.xml').async('string');
    if(!xml.includes(old))throw new Error(`Falta texto en ${relative}`);
    zip.file('word/document.xml',xml.replace(old,updated));
    fs.writeFileSync(file,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
  }
  console.log('Coherencia de métricas corregida en fuentes y Word.');
})().catch(e=>{console.error(e);process.exit(1)});
