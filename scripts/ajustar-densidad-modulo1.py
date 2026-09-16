"""Separar prosa extensa conservando énfasis y enlaces del módulo 1."""
from pathlib import Path
from lxml import html
import importlib.util, re, json
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('word_native',BASE/'scripts/render-contenido-word-nativo.py')
native=importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
path=BASE/'entregables/MODULO 1/Contenido/contenido.html'
tree=html.parse(str(path)); article=tree.xpath('//article')[0]
for h in article.xpath('./h2[@id="seccion-8"]'):
    e=h.getnext()
    while e is not None and e.tag!='h2':
        if e.tag=='ol': e.tag='ul'
        e=e.getnext()
for p in article.xpath('.//p'):
    if p.text_content().startswith('¿Scrum, Kanban y'):
        p.clear(); p.text='¿Un enfoque, un marco y una herramienta son lo mismo? Para ubicarnos necesitamos distinguir la lógica de organización, la estructura de trabajo y los medios que utilizamos para coordinarlo. Este mapa introduce cada alternativa antes de comparar sus reglas.'
changed=0
for p in list(article.xpath('.//p')):
    ts=native.clean(native.tokens(p)); parts=native.chunks(ts,limit=90)
    if len(parts)<2: continue
    parent=p.getparent(); index=list(parent).index(p)
    old=re.sub(r'\s+','',p.text_content())
    new_text=re.sub(r'\s+','',''.join(s for part in parts for s,*_ in part))
    assert old==new_text
    parent.remove(p)
    for part in parts:
        new=html.Element('p',attrib=dict(p.attrib))
        for s,b,i,url in part:
            node=None
            if url: node=html.Element('a',href=url)
            if b:
                strong=html.Element('strong')
                if node is not None: node.append(strong)
                else: node=strong
            if i:
                em=html.Element('em')
                if node is not None:
                    target=node[-1] if len(node) else node; target.append(em)
                else: node=em
            if node is not None:
                target=node
                while len(target): target=target[-1]
                target.text=s; new.append(node)
            elif len(new): new[-1].tail=(new[-1].tail or '')+s
            else: new.text=(new.text or '')+s
        parent.insert(index,new); index+=1
    changed+=1
path.write_bytes(html.tostring(tree,encoding='utf-8',doctype='<!DOCTYPE html>',pretty_print=True))
print(json.dumps({'parrafos_divididos':changed,'parrafo_mas_extenso':max(len(p.text_content().split()) for p in article.xpath('.//p'))}))
