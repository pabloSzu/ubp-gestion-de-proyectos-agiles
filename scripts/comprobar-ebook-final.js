const fs=require('fs'),path=require('path'),Zip=require('jszip');
const root=path.resolve(__dirname,'..');
const plain=s=>s.replace(/<[^>]*>/g,'').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/\s+/g,' ').trim();
(async()=>{
  const summaries=[];
  for(const n of [1,2,3,4,5]) {
    const dir=path.join(root,`entregables/MODULO ${n}/Contenido`);
    const source=fs.readFileSync(path.join(dir,'contenido.html'),'utf8');
    const zip=await Zip.loadAsync(fs.readFileSync(path.join(dir,'Contenido.docx')));
    const xml=await zip.file('word/document.xml').async('string');
    const text=plain([...xml.matchAll(/<w:t(?: [^>]*)?>([\s\S]*?)<\/w:t>/g)].map(m=>m[1]).join(''));
    const captions=[...source.matchAll(/<(figcaption|caption)>([\s\S]*?)<\/\1>/g)].map(m=>plain(m[2]));
    const missing=captions.filter(t=>!text.includes(t));
    const nested=[...xml.matchAll(/<w:hyperlink[^>]*>[\s\S]*?<\/w:hyperlink>/g)].filter(m=>(m[0].match(/<w:hyperlink/g)||[]).length>1).length;
    const images=(xml.match(/<w:drawing>/g)||[]).length;
    if(missing.length||nested)throw new Error(`M${n}: epígrafes ausentes ${JSON.stringify(missing)}, enlaces anidados ${nested}`);
    summaries.push({modulo:n,imagenes:images,epigrafes:captions.length,enlacesAnidados:nested});
  }
  const book=await Zip.loadAsync(fs.readFileSync(path.join(root,'output/GPA - materia-completa.docx')));
  const xml=await book.file('word/document.xml').async('string');
  const bookmarks=(xml.match(/w:bookmarkStart/g)||[]).length,nav=(xml.match(/w:anchor="GPA_Modulo_/g)||[]).length;
  if(bookmarks!==5||nav!==5)throw new Error('Navegación incompleta');
  const report={modulos:summaries,ebook:{imagenes:(xml.match(/<w:drawing>/g)||[]).length,marcadores:bookmarks,enlacesIndice:nav}};
  fs.writeFileSync(path.join(root,'.qa/revision-ebook/comprobacion-final.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify(report));
})().catch(e=>{console.error(e);process.exit(1)});
