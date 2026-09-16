const fs = require('fs');
const os = require('os');
const path = require('path');
const HTMLtoDOCX = require('html-to-docx');
const { chromium } = require('playwright');
const JSZip = require('jszip');

const WORD_CSS = `
<style>
body{font-family:Georgia,"Times New Roman",serif;font-size:11pt;line-height:1.5;color:#172333;}
p{margin:0 0 9pt;text-align:justify;}
h2{font-family:Georgia,"Times New Roman",serif;font-size:17pt;color:#173f67;background-color:#eaf4fa;border-left:5pt solid #2878a9;padding:8pt 10pt;margin:20pt 0 9pt;}
h3{font-family:Arial,sans-serif;font-size:12.5pt;color:#12655d;border-left:3pt solid #16877b;padding-left:8pt;margin:15pt 0 6pt;}
h4{font-family:Arial,sans-serif;font-size:11pt;color:#5d3e83;margin:12pt 0 5pt;}
strong{color:#111c29;}
table{width:100%;border-collapse:collapse;margin:9pt 0 13pt;font-family:Arial,sans-serif;font-size:9pt;}
caption{font-weight:bold;text-align:left;color:#536173;margin-bottom:5pt;}
th{background-color:#203d59;color:#ffffff;padding:7pt;text-align:left;vertical-align:middle;border:1pt solid #d9d9d9;}
td{padding:7pt;vertical-align:middle;border:1pt solid #d9d9d9;}
tr:nth-child(even) td{background-color:#f5f8fa;}
figure{margin:12pt 0 15pt;text-align:center;page-break-inside:avoid;}
figcaption{font-family:Arial,sans-serif;font-size:8.5pt;color:#536173;background-color:#fbf8f1;padding:7pt;text-align:left;}
.figure-caption{font-family:Arial,sans-serif;font-size:8.5pt;line-height:1.35;color:#536173;background-color:#fbf8f1;padding:7pt;margin:0 0 13pt;text-align:left;}
img{display:block;margin:0 auto;}
ol,ul{margin:6pt 0 9pt 18pt;padding-left:12pt;}
li{margin-bottom:5pt;}
.caso-resuelto li{margin-bottom:7pt;}
.caso-resuelto{margin-top:8pt;margin-bottom:14pt;}
.epigraph{font-style:italic;color:#374657;background-color:#fbf8f1;border-left:5pt solid #c68a24;padding:10pt;margin:0 0 16pt;}
.content>p:first-child{font-size:11.4pt;color:#374657;}
.page-break{page-break-after:always;}
.video-card{border-left:4pt solid #c25555;background-color:#fffafa;padding:9pt;margin:7pt 0;}
a{color:#a52f29;text-decoration:underline;}
</style>`;

const MODULE_PALETTES = {
  '1': { accent: '2878A9', fill: 'EAF4FA', ink: '173F67', secondary: '16877B', secondaryInk: '12655D' },
  '2': { accent: '16877B', fill: 'E8F6F3', ink: '12655D', secondary: '2878A9', secondaryInk: '173F67' },
  '3': { accent: '76549F', fill: 'F2EDF8', ink: '5D3E83', secondary: '16877B', secondaryInk: '12655D' },
  '4': { accent: 'C68A24', fill: 'FBF2DD', ink: '815B19', secondary: '2878A9', secondaryInk: '173F67' },
  '5': { accent: 'C25555', fill: 'FBEEEE', ink: '8C3838', secondary: '16877B', secondaryInk: '12655D' },
};

function findBrowser() {
  const candidates = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  ];
  return candidates.find((candidate) => fs.existsSync(candidate));
}

function fileUri(filePath) {
  return new URL(`file:///${path.resolve(filePath).replace(/\\/g, '/')}`).href;
}

function dataUri(filePath) {
  const extension = path.extname(filePath).slice(1).toLowerCase();
  const mime = extension === 'jpg' || extension === 'jpeg' ? 'image/jpeg' : 'image/png';
  return `data:${mime};base64,${fs.readFileSync(filePath).toString('base64')}`;
}

function extractCaption(figure) {
  return /<figcaption>([\s\S]*?)<\/figcaption>/i.exec(figure)?.[1] || '';
}

function textFromXml(xml) {
  return [...xml.matchAll(/<w:t(?: [^>]*)?>([\s\S]*?)<\/w:t>/g)]
    .map((match) => match[1].replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>'))
    .join('');
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function escapeXml(value) {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function addCellFill(cell, fill) {
  return cell.replace(/<w:tcPr>([\s\S]*?)<\/w:tcPr>/, (_match, properties) => {
    const cleaned = properties.replace(/<w:shd[^>]*\/>/g, '');
    return `<w:tcPr>${cleaned}<w:shd w:val="clear" w:color="auto" w:fill="${fill}"/></w:tcPr>`;
  });
}

function styleHeaderRuns(xml) {
  return xml.replace(/<w:r>([\s\S]*?)<\/w:r>/g, (run) => {
    if (/<w:rPr\/>/.test(run)) {
      return run.replace('<w:rPr/>', '<w:rPr><w:b/><w:color w:val="FFFFFF"/><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="18"/></w:rPr>');
    }
    if (/<w:rPr>/.test(run)) {
      return run.replace('<w:rPr>', '<w:rPr><w:b/><w:color w:val="FFFFFF"/>');
    }
    return run.replace('<w:r>', '<w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="18"/></w:rPr>');
  });
}

async function patchWordStyles(buffer, videoLinks = [], moduleNumber = '1') {
  const palette = MODULE_PALETTES[moduleNumber] || MODULE_PALETTES['1'];
  const zip = await JSZip.loadAsync(buffer);
  let styles = await zip.file('word/styles.xml').async('string');
  const heading2 = `<w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="9"/><w:unhideWhenUsed/><w:qFormat/>
    <w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="1"/><w:shd w:val="clear" w:color="auto" w:fill="${palette.fill}"/><w:pBdr><w:left w:val="single" w:sz="28" w:space="6" w:color="${palette.accent}"/></w:pBdr><w:ind w:left="120"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/><w:b/><w:color w:val="${palette.ink}"/><w:sz w:val="34"/><w:szCs w:val="34"/></w:rPr>
  </w:style>`;
  const heading3 = `<w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="9"/><w:semiHidden/><w:unhideWhenUsed/><w:qFormat/>
    <w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="260" w:after="80"/><w:outlineLvl w:val="2"/><w:pBdr><w:left w:val="single" w:sz="18" w:space="5" w:color="${palette.secondary}"/></w:pBdr><w:ind w:left="100"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="${palette.secondaryInk}"/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr>
  </w:style>`;
  styles = styles.replace(/<w:style[^>]*w:styleId="Heading2"[\s\S]*?<\/w:style>/, heading2);
  styles = styles.replace(/<w:style[^>]*w:styleId="Heading3"[\s\S]*?<\/w:style>/, heading3);
  zip.file('word/styles.xml', styles);

  let documentXml = await zip.file('word/document.xml').async('string');
  documentXml = documentXml.replace(/<w:tbl>[\s\S]*?<\/w:tbl>/g, (table) => {
    const label = textFromXml(table).trim();
    const cellCount = (table.match(/<w:tc>/g) || []).length;
    if (/^01Módulo 1/.test(label)) {
      table = table.replace(/<w:tblGrid>[\s\S]*?<\/w:tblGrid>/, '<w:tblGrid><w:gridCol w:w="1040"/><w:gridCol w:w="9278"/></w:tblGrid>');
      return table.replace(/<w:tr>[\s\S]*?<\/w:tr>/g, row => {
        let column = 0;
        return row.replace(/<w:tc>[\s\S]*?<\/w:tc>/g, cell => cell.replace(/<w:tcW[^>]*\/>/, `<w:tcW w:w="${column++ === 0 ? 1040 : 9278}" w:type="dxa"/>`));
      });
    }
    if (cellCount === 1 || /^(Criterio profesional|Mito|The Agile Manifesto|Agile vs Waterfall)/i.test(label)) return table;
    return table.replace(/<w:tr>[\s\S]*?<\/w:tr>/, (row) => {
      const filled = row.replace(/<w:tc>[\s\S]*?<\/w:tc>/g, (cell) => addCellFill(cell, '203D59'));
      return styleHeaderRuns(filled).replace('<w:trPr>', '<w:trPr><w:tblHeader/>');
    });
  });
  let relationshipsXml = await zip.file('word/_rels/document.xml.rels').async('string');
  videoLinks.forEach(({ title, url }, index) => {
    if ([...documentXml.matchAll(/<w:hyperlink[^>]*>[\s\S]*?<\/w:hyperlink>/g)].some(m => textFromXml(m[0]).trim() === title)) return;
    const relationshipId = `rIdVideo${index + 1}`;
    const titlePattern = escapeRegExp(escapeXml(title));
    const runPattern = new RegExp(`<w:r>(?:(?!<w:r>)[\\s\\S])*?<w:t[^>]*>${titlePattern}<\\/w:t>(?:(?!<w:r>)[\\s\\S])*?<\\/w:r>`);
    documentXml = documentXml.replace(runPattern, (run) => {
      const styledRun = run.replace('<w:rPr>', '<w:rPr><w:color w:val="A52F29"/><w:u w:val="single"/>');
      return `<w:hyperlink r:id="${relationshipId}" w:history="1">${styledRun}</w:hyperlink>`;
    });
    relationshipsXml = relationshipsXml.replace('</Relationships>', `<Relationship Id="${relationshipId}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="${escapeXml(url)}" TargetMode="External"/></Relationships>`);
  });
  zip.file('word/document.xml', documentXml);
  zip.file('word/_rels/document.xml.rels', relationshipsXml);
  return zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' });
}

async function buildWordHtml(htmlPath, workDir) {
  const browserPath = findBrowser();
  if (!browserPath) throw new Error('No se encontró Chrome ni Edge para rasterizar los recursos visuales.');

  const browser = await chromium.launch({ headless: true, executablePath: browserPath });
  const page = await browser.newPage({ viewport: { width: 1100, height: 1500 }, deviceScaleFactor: 1.5 });
  await page.goto(fileUri(htmlPath), { waitUntil: 'load', timeout: 60000 });

  const coverPath = path.join(workDir, 'portada-word.png');
  await page.locator('.opener').screenshot({ path: coverPath });

  const diagramPaths = [];
  const diagrams = page.locator('.diagrama-conceptual svg');
  for (let index = 0; index < await diagrams.count(); index += 1) {
    const diagramPath = path.join(workDir, `diagrama-${index + 1}.png`);
    await diagrams.nth(index).screenshot({ path: diagramPath });
    diagramPaths.push(diagramPath);
  }
  await browser.close();

  let source = fs.readFileSync(htmlPath, 'utf8');
  let body = /<article class="content">([\s\S]*?)<\/article>/i.exec(source)?.[1];
  if (!body) throw new Error('No se encontró el cuerpo editorial del contenido.');

  body = body.replace(/<figure class="diagrama-conceptual">[\s\S]*?<\/figure>/gi, (figure) => {
    const diagramPath = diagramPaths.shift();
    return `<figure><img src="${dataUri(diagramPath)}" width="640" style="width:640px;height:auto"><figcaption>${extractCaption(figure)}</figcaption></figure>`;
  });

  body = body.replace(/src="assets\/([^"]+)"/gi, (_match, filename) => {
    return `src="${dataUri(path.join(path.dirname(htmlPath), 'assets', filename))}"`;
  });

  body = body.replace(/<div class="criterio-profesional">([\s\S]*?)<\/div>/gi,
    '<table><tbody><tr><td style="background-color:#e8f6f3;border-left:5pt solid #16877b;padding:10pt;font-family:Arial,sans-serif;font-size:9.5pt;">$1</td></tr></tbody></table>');
  body = body.replace(/<div class="mito">([\s\S]*?)<\/div>/gi,
    '<table><tbody><tr><td style="background-color:#fbeeee;border-left:5pt solid #c25555;padding:10pt;font-family:Arial,sans-serif;font-size:9.5pt;">$1</td></tr></tbody></table>');
  body = body.replace(/<ul class="recursos-audiovisuales">([\s\S]*?)<\/ul>/gi, (_match, items) => {
    return items.replace(/<li>([\s\S]*?)<\/li>/gi,
      '<table><tbody><tr><td style="background-color:#fffafa;border-left:5pt solid #c25555;padding:9pt;font-family:Arial,sans-serif;font-size:9.5pt;">$1</td></tr></tbody></table>');
  });
  body = body.replace(/<figcaption>([\s\S]*?)<\/figcaption>/gi,
    '<p class="figure-caption" style="font-family:Arial,sans-serif;font-size:8.5pt;line-height:1.35;color:#536173;background-color:#fbf8f1;padding:7pt;margin:0 0 13pt;text-align:left;">$1</p>');
  body = body.replace(/<table([^>]*)>\s*<caption>([\s\S]*?)<\/caption>/gi, '<p style="font-family:Arial,sans-serif;font-size:9pt;color:#536173;text-align:left;"><strong>$2</strong></p><table$1>');
  body = body.replace(/<\/?figure(?:\s[^>]*)?>/gi, '');
  body = body.replace(/<img([^>]*?)>/gi, '<img$1 width="640" style="width:640px;height:auto">');
  body = body.replace(/width="640" style="width:640px;height:auto"([^>]*?)width="640" style="width:640px;height:auto"/gi,
    'width="640" style="width:640px;height:auto"$1');

  const cover = `<p style="text-align:center;margin:0;"><img src="${dataUri(coverPath)}" width="640" style="width:640px;height:auto"></p><div class="page-break" style="page-break-after:always;"></div>`;
  return `<!doctype html><html lang="es"><head><meta charset="utf-8">${WORD_CSS}</head><body>${cover}${body}</body></html>`;
}

async function main() {
  const htmlPath = path.resolve(process.argv[2] || '');
  const docxPath = path.resolve(process.argv[3] || '');
  if (!process.argv[2] || !process.argv[3]) {
    throw new Error('Uso: node scripts/render-contenido-word.js <entrada.html> <salida.docx>');
  }

  const source = fs.readFileSync(htmlPath, 'utf8');
  const title = /<header class="opener">[\s\S]*?<h1>([\s\S]*?)<\/h1>/i.exec(source)?.[1].replace(/<[^>]+>/g, '').trim()
    || /<title>([\s\S]*?)<\/title>/i.exec(source)?.[1].trim()
    || 'Gestión de Proyectos Ágiles';
  const moduleNumber = /MODULO\s+(\d+)/i.exec(htmlPath)?.[1] || '';
  const videoLinks = [...source.matchAll(/<a href="(https?:\/\/[^"']+)">([\s\S]*?)<\/a>/gi)].map((match) => ({
    url: match[1],
    title: match[2].replace(/<[^>]+>/g, '').trim(),
  }));
  const workDir = fs.mkdtempSync(path.join(os.tmpdir(), 'ubp-word-render-'));
  const html = await buildWordHtml(htmlPath, workDir);
  const initialBuffer = await HTMLtoDOCX(html, null, {
    title,
    subject: `Gestión de Proyectos Ágiles${moduleNumber ? ` · Módulo ${moduleNumber}` : ''}`,
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
  const buffer = await patchWordStyles(initialBuffer, videoLinks, moduleNumber);
  fs.writeFileSync(docxPath, buffer);
  fs.rmSync(workDir, { recursive: true, force: true });
  console.log(`OK: ${docxPath} (${Math.round(buffer.length / 1024)} KB)`);
}

if (require.main === module) {
  main().catch((error) => {
    console.error(error);
    process.exit(1);
  });
}

module.exports = { WORD_CSS, MODULE_PALETTES, dataUri, patchWordStyles, findBrowser };
