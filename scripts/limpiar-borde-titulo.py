from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from docx.oxml.ns import qn
BASE=Path(__file__).resolve().parents[1]
paths=[BASE/'entregables'/f'MODULO {n}'/'Contenido/Contenido.docx' for n in range(1,6)]+[BASE/'output/GPA - materia-completa.docx',BASE/'Programa - contenidos.docx']
for p in paths:
    with ZipFile(p) as z:
        items=[(i,z.read(i.filename)) for i in z.infolist()]
    new=[]
    for info,data in items:
        if info.filename=='word/styles.xml':
            root=etree.fromstring(data)
            for style in root.iter(qn('w:style')):
                if style.get(qn('w:styleId'))=='Title':
                    for border in list(style.iter(qn('w:pBdr'))): border.getparent().remove(border)
            data=etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
        if info.filename=='word/document.xml':
            root=etree.fromstring(data)
            for paragraph in root.iter(qn('w:p')):
                pr=paragraph.find(qn('w:pPr'))
                if pr is not None and paragraph.index(pr)!=0:
                    paragraph.remove(pr); paragraph.insert(0,pr)
            data=etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
        new.append((info,data))
    temp=p.with_suffix('.qa.docx')
    with ZipFile(temp,'w') as z:
        for info,data in new: z.writestr(info,data)
    temp.replace(p)
print('Borde heredado del título eliminado en siete Word.')
