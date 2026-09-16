const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

function findBrowser() {
  const candidates = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  ];
  return candidates.find((candidate) => fs.existsSync(candidate));
}

async function main() {
  const docxPath = path.resolve(process.argv[2] || '');
  const outputDir = path.resolve(process.argv[3] || '');
  if (!process.argv[2] || !process.argv[3]) throw new Error('Uso: node scripts/verify-docx-preview.js <archivo.docx> <directorio-salida>');
  fs.mkdirSync(outputDir, { recursive: true });

  const docxPreview = path.join(path.dirname(require.resolve('docx-preview')), 'docx-preview.min.js');
  const jsZip = require.resolve('jszip/dist/jszip.min.js');
  const docxData = fs.readFileSync(docxPath).toString('base64');
  const htmlPath = path.join(outputDir, 'preview.html');
  const shell = '<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:#777}.docx-wrapper{padding:20px!important}.docx-wrapper>section.docx{box-shadow:0 2px 12px #222;margin:0 auto 20px!important}</style></head><body><div id="container"></div></body></html>';
  fs.writeFileSync(htmlPath, shell);

  const browser = await chromium.launch({ headless: true, executablePath: findBrowser() });
  const page = await browser.newPage({ viewport: { width: 920, height: 1200 }, deviceScaleFactor: 1 });
  await page.setContent(shell);
  await page.addScriptTag({ path: jsZip });
  await page.addScriptTag({ path: docxPreview });
  await page.evaluate(async (base64) => {
    const bytes = Uint8Array.from(atob(base64), (character) => character.charCodeAt(0));
    await window.docx.renderAsync(bytes.buffer, document.getElementById('container'), null, { inWrapper: true, breakPages: true, ignoreLastRenderedPageBreak: false });
  }, docxData);
  await page.waitForTimeout(500);
  const metrics = await page.evaluate(() => {
    const body = document.body;
    const overflowing = [...document.querySelectorAll('table,img,svg,p,h1,h2,h3,h4')].filter((el) => el.getBoundingClientRect().right > document.documentElement.clientWidth + 2).length;
    const overflowDetails = [...document.querySelectorAll('table,img,svg,p,h1,h2,h3,h4')].filter((el) => el.getBoundingClientRect().right > document.documentElement.clientWidth + 2).map(el => ({ tag: el.tagName, text: el.textContent.slice(0, 160), right: el.getBoundingClientRect().right, top: el.getBoundingClientRect().top + window.scrollY }));
    const brokenImages = [...document.images].filter(img => !img.complete || !img.naturalWidth).length;
    const pageOverflows = [...document.querySelectorAll('table,img,p')].filter(el => { const sheet = el.closest('section.docx'); return sheet && el.getBoundingClientRect().right > sheet.getBoundingClientRect().right + 2; }).length;
    return { height: body.scrollHeight, width: body.scrollWidth, images: document.images.length, brokenImages, pageOverflows, tables: document.querySelectorAll('table').length, links: document.querySelectorAll('a').length, h2: document.querySelectorAll('h2').length, h3: document.querySelectorAll('h3').length, overflowing, overflowDetails };
  });
  const sampleStarts = [0, Math.max(0, Math.floor(metrics.height / 2) - 600), Math.max(0, metrics.height - 1200)];
  for (let i = 0; i < sampleStarts.length; i += 1) {
    await page.evaluate((y) => window.scrollTo(0, y), sampleStarts[i]);
    await page.waitForTimeout(100);
    await page.screenshot({ path: path.join(outputDir, `sample-${i + 1}.png`) });
  }
  if (process.argv.includes('--all')) {
    for (let y = 0, i = 1; y < metrics.height; y += 1050, i += 1) {
      await page.evaluate((offset) => window.scrollTo(0, offset), y);
      await page.screenshot({ path: path.join(outputDir, `tile-${String(i).padStart(3, '0')}.png`) });
    }
  }
  await page.evaluate(() => { document.querySelector('.docx-wrapper').style.zoom = '0.22'; });
  await page.setViewportSize({ width: 920, height: 1200 });
  await page.screenshot({ path: path.join(outputDir, 'contact-sheet.png'), fullPage: true });
  await browser.close();
  fs.writeFileSync(path.join(outputDir, 'metrics.json'), JSON.stringify({ docxPath, ...metrics, samples: sampleStarts.length }, null, 2));
  console.log(JSON.stringify({ outputDir, ...metrics, samples: sampleStarts.length }));
}

main().catch((error) => { console.error(error); process.exit(1); });
