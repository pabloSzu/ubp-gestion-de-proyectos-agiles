const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

function fileUri(filePath) {
  return new URL(`file:///${path.resolve(filePath).replace(/\\/g, '/')}`).href;
}

function findBrowser() {
  const candidates = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  ];
  return candidates.find((candidate) => fs.existsSync(candidate));
}

async function main() {
  const htmlPath = process.argv[2];
  const pdfPath = process.argv[3];
  if (!htmlPath || !pdfPath) {
    throw new Error('Uso: node scripts/render-contenido-pdf.js <entrada.html> <salida.pdf>');
  }

  const executablePath = findBrowser();
  if (!executablePath) {
    throw new Error('No se encontró Google Chrome ni Microsoft Edge para renderizar el PDF.');
  }

  fs.mkdirSync(path.dirname(path.resolve(pdfPath)), { recursive: true });
  const browser = await chromium.launch({ headless: true, executablePath });
  const page = await browser.newPage({ viewport: { width: 1240, height: 1754 } });

  try {
    await page.goto(fileUri(htmlPath), { waitUntil: 'load', timeout: 60000 });
    await page.emulateMedia({ media: 'print' });
    await page.pdf({
      path: path.resolve(pdfPath),
      format: 'A4',
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' },
    });
  } finally {
    await browser.close();
  }

  console.log(`OK: ${path.resolve(pdfPath)}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
