const fs = require('fs');
const path = require('path');
const JSZip = require('jszip');
(async () => {
  const root = path.resolve(__dirname,'..');
  const files = [1,2,3,4,5].map(n=>path.join(root,`entregables/MODULO ${n}/Contenido/Contenido.docx`));
  files.push(path.join(root,'output/GPA - materia-completa.docx'));
  for(const file of files) {
    const zip = await JSZip.loadAsync(fs.readFileSync(file));
    let xml = await zip.file('word/document.xml').async('string');
    let count = 0;
    xml = xml.replace(/<w:hyperlink[^>]*>\s*(<w:hyperlink[^>]*>[\s\S]*?<\/w:hyperlink>)\s*<\/w:hyperlink>/g,(_m,inner)=>{count++;return inner;});
    zip.file('word/document.xml',xml);
    fs.writeFileSync(file,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
    console.log(`${path.basename(path.dirname(path.dirname(file)))}: ${count} enlaces normalizados`);
  }
})().catch(e=>{console.error(e);process.exit(1)});
