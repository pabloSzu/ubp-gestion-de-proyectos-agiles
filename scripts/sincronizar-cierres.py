from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from docx.oxml.ns import qn
BASE=Path(__file__).resolve().parents[1]
changes={1:[('Finalmente, reconstruimos el origen histórico','También reconstruimos el origen histórico')],2:[('Luego estudiamos sus roles','Después de comprender los fundamentos, estudiamos sus roles'),('Ese recorrido permitió comprender el fundamento empírico:','El fundamento empírico explica por qué funciona:')]}
for n,pairs in changes.items():
    path=BASE/'entregables'/f'MODULO {n}'/'Contenido/contenido.html'; raw=path.read_text(encoding='utf-8')
    for old,new in pairs:
        assert raw.count(old)==1,(n,old); raw=raw.replace(old,new)
    path.write_text(raw,encoding='utf-8')
for n in [1,2,0]:
    p=BASE/'output/GPA - materia-completa.docx' if n==0 else BASE/'entregables'/f'MODULO {n}'/'Contenido/Contenido.docx'
    with ZipFile(p) as z: items=[(i,z.read(i.filename)) for i in z.infolist()]
    result=[]; pairs=changes[n] if n else changes[1]+changes[2]
    for info,data in items:
        if info.filename=='word/document.xml':
            tree=etree.fromstring(data)
            for old,new in pairs:
                hits=[e for e in tree.iter(qn('w:t')) if e.text and old in e.text]
                assert len(hits)==1,(p,old,len(hits)); hits[0].text=hits[0].text.replace(old,new)
            data=etree.tostring(tree,encoding='UTF-8',xml_declaration=True,standalone=True)
        result.append((info,data))
    temp=p.with_suffix('.qa.docx')
    with ZipFile(temp,'w') as z:
        for info,data in result: z.writestr(info,data)
    temp.replace(p)
print('Cierres de módulos 1 y 2 sincronizados con el orden narrativo.')
