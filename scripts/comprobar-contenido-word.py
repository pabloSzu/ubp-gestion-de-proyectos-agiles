from pathlib import Path
from zipfile import ZipFile
from lxml import html,etree
from PIL import Image,ImageDraw
import re,json
BASE=Path(__file__).resolve().parents[1]; QA=BASE/'.qa/edicion-contenido'
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/package/2006/relationships'}
report=[]
def norm(s): return re.sub(r'\s+','',s)
for n in range(1,6):
    folder=BASE/'entregables'/f'MODULO {n}'/'Contenido'; a=html.parse(str(folder/'contenido.html')).xpath('//article')[0]
    before=html.parse(str(QA/'antes'/f'MODULO {n}'/'contenido.html')).xpath('//article')[0]
    oldtitles=[re.sub(r'^\d+\.\s*','',h.text_content().strip()) for h in before.xpath('./h2')]
    newtitles=[re.sub(r'^\d+\.\s*','',h.text_content().strip()) for h in a.xpath('./h2')]
    removed=[s for s in oldtitles if s not in newtitles]
    assert not removed or removed==['Escenarios de transformación y desafíos de adopción']
    assert len(html.parse(str(folder/'contenido.html')).xpath('//h1'))==1
    assert 'Síntesis' in newtitles[-1]
    with ZipFile(folder/'Contenido.docx') as z:
        doc=etree.fromstring(z.read('word/document.xml')); doc_text=norm(''.join(doc.xpath('//w:t/text()',namespaces=NS)))
        # Todo párrafo, lista, título y celda del artículo debe conservarse en el Word.
        missing=[]
        for e in a.xpath('.//p|.//li|.//h2|.//h3|.//h4|.//td|.//th|.//figcaption|.//caption'):
            if e.xpath('./ul|./ol'): continue
            s=norm(e.text_content())
            if s and s not in doc_text: missing.append(e.text_content()[:100])
        assert not missing,(n,missing)
        rel=etree.fromstring(z.read('word/_rels/document.xml.rels'))
        links=len(rel.xpath('//r:Relationship[@TargetMode="External"]',namespaces=NS))
        lists=len(doc.xpath('//w:numPr',namespaces=NS))
        figures=len(doc.xpath('//w:drawing',namespaces=NS))
        tables=len(doc.xpath('//w:tbl',namespaces=NS))
        bookmarks=doc.xpath('//w:bookmarkStart/@w:name',namespaces=NS)
        assert len(bookmarks)==len(set(bookmarks))
        for paragraph in doc.iter('{'+NS['w']+'}p'):
            pr=paragraph.find('{'+NS['w']+'}pPr')
            assert pr is None or paragraph.index(pr)==0
        assert all(anchor in bookmarks for anchor in doc.xpath('//w:hyperlink/@w:anchor',namespaces=NS))
    assert figures==len(a.xpath('.//figure//img'))
    assert tables==len(a.xpath('.//table'))
    report.append({'modulo':n,'secciones_preservadas':True,'texto_preservado_en_word':True,'listas_nativas':lists,'figuras':figures,'tablas_nativas':tables,'enlaces_externos':links})
    preview=QA/f'vista-modulo-{n}'; tiles=sorted(preview.glob('tile-*.png'))
    for start in range(0,len(tiles),12):
        sheet=Image.new('RGB',(960,1320),'white'); draw=ImageDraw.Draw(sheet)
        for i,file in enumerate(tiles[start:start+12]):
            im=Image.open(file).convert('RGB'); im.thumbnail((230,310))
            x=(i%4)*240; y=(i//4)*440
            sheet.paste(im,(x,y+24)); draw.text((x+4,y+6),f'M{n} {file.stem}',fill='black')
        sheet.save(preview/f'contacto-{start//12+1}.png')
with ZipFile(BASE/'output/GPA - materia-completa.docx') as z:
    d=etree.fromstring(z.read('word/document.xml')); ids=d.xpath('//w:bookmarkStart/@w:id',namespaces=NS); assert len(ids)==len(set(ids))
assert 80-24-7==49 and 4*70+49==329 and round(329*.85,2)==279.65
(QA/'comprobacion-word.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
