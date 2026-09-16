// Control auxiliar del DOCX; no reproduce la paginación de Word o LibreOffice.
const fs=require('fs'),path=require('path');
const {chromium}=require('C:/Users/Pablo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base=path.resolve(__dirname,'..');
async function main(){
 const browser=await chromium.launch({headless:true,executablePath:['C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(fs.existsSync)});
 const moduleArg=process.argv.find(x=>x.startsWith('--modulo='));
 const modulesArg=process.argv.find(x=>x.startsWith('--modulos='));
 const modules=process.argv.includes('--programa')?[0]:moduleArg?[Number(moduleArg.split('=')[1])]:modulesArg?modulesArg.split('=')[1].split(',').map(Number):[1,2,3,4,5];
 if(modules.some(n=>!Number.isInteger(n)||n<0||n>5))throw new Error('Módulo inválido');
 for(let n of modules){
  const file=n?path.join(base,'entregables',`MODULO ${n}`,'Contenido','Contenido.docx'):path.join(base,'Programa - contenidos.docx'),out=path.join(base,'.qa',process.argv.includes('--revision-ia')?'revision-pedagogica-ia':'edicion-contenido',n?`vista-modulo-${n}`:'vista-programa');fs.mkdirSync(out,{recursive:true});
  const page=await browser.newPage({viewport:{width:920,height:1200},deviceScaleFactor:1});
  await page.setContent('<html><head><style>body{margin:0;background:#777}.docx-wrapper{padding:20px!important}.docx-wrapper>section.docx{margin:0 auto 20px!important}</style></head><body><div id="container"></div></body></html>');
  await page.addScriptTag({path:path.join(base,'node_modules/jszip/dist/jszip.min.js')});await page.addScriptTag({path:path.join(base,'node_modules/docx-preview/dist/docx-preview.min.js')});
  await page.evaluate(async b=>{const bytes=Uint8Array.from(atob(b),c=>c.charCodeAt(0));await window.docx.renderAsync(bytes.buffer,document.getElementById('container'),null,{inWrapper:true,breakPages:true});},fs.readFileSync(file).toString('base64'));
  await page.evaluate(()=>document.fonts.ready);await page.waitForTimeout(300);
  const metrics=await page.evaluate(()=>({height:document.body.scrollHeight,images:document.images.length,brokenImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).length,tables:document.querySelectorAll('table').length,overflow:[...document.querySelectorAll('p,table,img')].filter(e=>{const s=e.closest('section.docx');return s&&e.getBoundingClientRect().right>s.getBoundingClientRect().right+2}).map(e=>({tag:e.tagName,text:e.textContent.slice(0,90)}))}));
  for(let y=0,i=1;y<metrics.height;y+=1050,i++){await page.evaluate(y=>window.scrollTo(0,y),y);await page.screenshot({path:path.join(out,`tile-${String(i).padStart(3,'0')}.png`)});}
  for(let [i,y] of [0,Math.floor(metrics.height/2),Math.max(0,metrics.height-1200)].entries()){await page.evaluate(y=>window.scrollTo(0,y),y);await page.screenshot({path:path.join(out,`sample-${i+1}.png`)});}
  fs.writeFileSync(path.join(out,'metrics.json'),JSON.stringify(metrics,null,2));console.log(JSON.stringify({module:n,...metrics}));await page.close();
 }
 await browser.close();
}main().catch(e=>{console.error(e);process.exit(1)});
