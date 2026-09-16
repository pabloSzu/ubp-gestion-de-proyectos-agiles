from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from docx.oxml.ns import qn
BASE=Path(__file__).resolve().parents[1]
OLD='Estos recursos fueron seleccionados y verificados para profundizar los núcleos conceptuales del módulo desde fuentes especializadas.'
NEW='Estos recursos complementan las explicaciones y permiten observar otras presentaciones de los conceptos. El contenido esencial está desarrollado en este documento.'
for n in range(2,6):
    p=BASE/'entregables'/f'MODULO {n}'/'Contenido/contenido.html'; s=p.read_text(encoding='utf-8'); assert s.count(OLD)==1; p.write_text(s.replace(OLD,NEW),encoding='utf-8')
for n in [2,3,4,5,0]:
    p=BASE/'output/GPA - materia-completa.docx' if n==0 else BASE/'entregables'/f'MODULO {n}'/'Contenido/Contenido.docx'
    with ZipFile(p) as z: items=[(i,z.read(i.filename)) for i in z.infolist()]
    result=[]
    for info,data in items:
        if info.filename=='word/document.xml':
            root=etree.fromstring(data); hits=[e for e in root.iter(qn('w:t')) if e.text and OLD in e.text]
            assert len(hits)==(4 if n==0 else 1),(n,len(hits))
            for e in hits: e.text=e.text.replace(OLD,NEW)
            data=etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
        result.append((info,data))
    tmp=p.with_suffix('.qa.docx')
    with ZipFile(tmp,'w') as z:
        for info,data in result: z.writestr(info,data)
    tmp.replace(p)
print('El aviso audiovisual no afirma una disponibilidad que no pudo certificarse.')
