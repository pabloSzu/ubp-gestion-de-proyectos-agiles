import sys,re
from pathlib import Path
from lxml import html
p=Path(__file__).resolve().parents[1]/'entregables'/f'MODULO {sys.argv[1]}'/'Contenido'/'contenido.html'
a=html.parse(str(p)).xpath('//article')[0]
active=False
for e in a:
    if e.tag=='h2':
        m=re.match(r'(\d+)\.',e.text_content().strip())
        active=bool(m and int(sys.argv[2])<=int(m[1])<=int(sys.argv[3]))
    if active: print(e.text_content().strip())
