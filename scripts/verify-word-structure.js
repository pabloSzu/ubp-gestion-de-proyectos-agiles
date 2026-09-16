const fs = require('fs');
const path = require('path');
const JSZip = require('jszip');

async function inspect(docxPath) {
  const zip = await JSZip.loadAsync(fs.readFileSync(docxPath));
  const documentXml = await zip.file('word/document.xml').async('string');
  const stylesXml = await zip.file('word/styles.xml').async('string');
  const relsXml = await zip.file('word/_rels/document.xml.rels').async('string');
  const footerNames = Object.keys(zip.files).filter((name) => /^word\/footer\d+\.xml$/.test(name));
  const footerXml = (await Promise.all(footerNames.map((name) => zip.file(name).async('string')))).join('\n');
  const media = Object.keys(zip.files).filter((name) => name.startsWith('word/media/') && !zip.files[name].dir);
  const hyperlinks = [...relsXml.matchAll(/Target="(https?:\/\/[^\"]+)"/g)].map((match) => match[1].replace(/&amp;/g, '&'));
  return {
    file: docxPath,
    sizeMB: Number((fs.statSync(docxPath).size / 1024 / 1024).toFixed(2)),
    paragraphs: (documentXml.match(/<w:p(?:\s|>)/g) || []).length,
    tables: (documentXml.match(/<w:tbl>/g) || []).length,
    drawings: (documentXml.match(/<w:drawing>/g) || []).length,
    mediaFiles: media.length,
    hyperlinks,
    hasHeading2Style: /w:styleId="Heading2"/.test(stylesXml),
    hasHeading3Style: /w:styleId="Heading3"/.test(stylesXml),
    hasPageNumbers: /PAGE/.test(`${documentXml}\n${footerXml}`),
  };
}

async function main() {
  const files = process.argv.slice(2).map((file) => path.resolve(file));
  if (!files.length) throw new Error('Indicá uno o más archivos .docx');
  const results = [];
  for (const file of files) results.push(await inspect(file));
  console.log(JSON.stringify(results, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
