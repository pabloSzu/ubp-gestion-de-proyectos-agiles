from pathlib import Path
from lxml import html,etree
import re
BASE=Path(__file__).resolve().parents[1]
for n in range(1,6):
    p=BASE/'entregables'/f'MODULO {n}'/'Contenido/contenido.html'; t=html.parse(str(p)); a=t.xpath('//article')[0]
    section=None; count=0
    for e in a:
        if e.tag=='h2':
            match=re.match(r'(\d+)\.',e.text_content().strip()); section=int(match[1]) if match else None; count=0
        if e.tag=='h3' and section and e.text and re.match(r'\d+\.\d+\s',e.text):
            count+=1; e.text=re.sub(r'^\d+\.\d+',f'{section}.{count}',e.text)
    p.write_bytes(etree.tostring(t,method='html',encoding='utf-8',doctype='<!doctype html>'))
print('Subtítulos correlativos comprobados.')
