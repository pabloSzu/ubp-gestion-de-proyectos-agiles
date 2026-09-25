"""Genera Contenido.docx de un módulo a partir de su fuente contenido.md.

Uso: python scripts/md-a-word.py --modulo 1 [--tipo contenido|actividades|respuestas|glosario|microobjetivos]
    python scripts/md-a-word.py --parcial 1 --tipo evaluacion|guia [--salida ruta.docx]

Encabezado de la fuente: modulo, titulo, subtitulo y materia (nombre oficial de la
materia; se usa en portada y pie). Para otra materia, copiar este script y
render-contenido-word-nativo.py a su carpeta scripts/.

Sintaxis de la fuente y tipos de recuadro: ver GUIA-CONTENIDO.md.
Reutiliza estilos, tablas, figuras e índice de render-contenido-word-nativo.py.
"""
from pathlib import Path
import argparse, html as htmllib, importlib.util, json, re
from lxml import html
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('nativo', Path(__file__).with_name('render-contenido-word-nativo.py'))
nativo = importlib.util.module_from_spec(spec); spec.loader.exec_module(nativo)

# tipo: (etiqueta por defecto, relleno, borde y títulos)
CAJAS = {
    'ejemplo':   ('', 'FFF4DE', 'C98A12', '8A5500'),
    'ensimple':  ('En simple', 'E3F4EF', '12806D'),
    'clave':     ('', 'E8F1FA', '1F4E86'),
    'preguntas': ('', 'EEF2FB', '3A5BA0'),
    'mito':      ('Mito o realidad', 'FCECEC', 'B04444'),
    'caso':      ('', 'F1ECF8', '6A4A9C'),
    'historia':  ('', 'F5F1EA', '7A6248'),
    'real':      ('Caso real', 'E4F2F5', '0F7A8F', '0B5566'),
    'contexto':  ('', 'EEF1F5', '536173', '2E3B4E'),
}

def inline(text):
    t = htmllib.escape(text, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t

def parse_blocks(lines):
    """Convierte líneas Markdown en una lista de fragmentos HTML y cajas."""
    out = []; i = 0; n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        if not line.strip(): i += 1; continue
        if line.startswith(':::'):
            m = re.match(r':::(\w+)\s*(.*)', line); kind, title = m.group(1), m.group(2).strip()
            j = i + 1; body = []
            while j < n and lines[j].strip() != ':::': body.append(lines[j]); j += 1
            out.append(('caja', kind, title, parse_blocks(body))); i = j + 1; continue
        h = re.match(r'(#{1,4})\s+(.*)', line)
        if h:
            out.append(('h', len(h.group(1)), h.group(2).strip())); i += 1; continue
        img = re.match(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)', line)
        if img:
            out.append(('img', img.group(1), img.group(2), img.group(3) or '')); i += 1; continue
        if line.startswith('|'):
            rows = []
            while i < n and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells): rows.append(cells)
                i += 1
            cap = ''
            if i < n and lines[i].startswith('Tabla:'): cap = lines[i][6:].strip(); i += 1
            out.append(('tabla', rows, cap)); continue
        if re.match(r'(- |\d+\. )', line):
            # Listas; los ítems con sangría de 4 espacios por nivel forman listas anidadas.
            items = []; levels = []; ordered = bool(re.match(r'\d+\. ', line))
            marca = re.compile(r'^( *)(- |\d+\. )')
            while i < n and marca.match(lines[i]):
                m = marca.match(lines[i]); levels.append(len(m.group(1)) // 4)
                txt = lines[i].strip()
                items.append(txt[2:] if txt.startswith('- ') else txt); i += 1
                while i < n and lines[i].startswith('   ') and lines[i].strip() and not marca.match(lines[i]):
                    items[-1] += ' ' + lines[i].strip(); i += 1
            out.append(('lista', ordered, items, levels)); continue
        if line.startswith('> '):
            # Cita destacada: líneas consecutivas que empiezan con '> '.
            cita = []
            while i < n and lines[i].startswith('> '): cita.append(lines[i][2:].strip()); i += 1
            out.append(('cita', ' '.join(cita))); continue
        para = [line.strip()]; i += 1
        while i < n and lines[i].strip() and not re.match(r'(#|:::|\||!\[|- |\d+\. )', lines[i]): para.append(lines[i].strip()); i += 1
        out.append(('p', ' '.join(para)))
    return out

def to_html(blocks):
    """HTML intermedio para el Builder existente; las cajas quedan como marcadores."""
    parts = []; count = 0
    for b in blocks:
        if b[0] == 'h':
            if b[1] == 2: count += 1; parts.append(f'<h2 id="seccion-{count}">{inline(b[2])}</h2>')
            else: parts.append(f'<h{b[1]}>{inline(b[2])}</h{b[1]}>')
        elif b[0] == 'p': parts.append(f'<p>{inline(b[1])}</p>')
        elif b[0] == 'cita': parts.append(f'<p class="cita">{inline(b[1])}</p>')
        elif b[0] == 'img': parts.append(f'<figure><img src="{b[2]}" alt="{htmllib.escape(b[1])}"/><figcaption>{inline(b[3])}</figcaption></figure>')
        elif b[0] == 'tabla':
            rows, cap = b[1], b[2]
            body = ''.join('<tr>' + ''.join(f'<{"th" if k == 0 else "td"}>{inline(c)}</{"th" if k == 0 else "td"}>' for c in r) + '</tr>' for k, r in enumerate(rows))
            parts.append(f'<table>{f"<caption>{inline(cap)}</caption>" if cap else ""}{body}</table>')
        elif b[0] == 'lista':
            if any(b[3]):
                parts.extend(f'<p class="item-anidado" data-nivel="{lv}">{inline(it)}</p>' for it, lv in zip(b[2], b[3]))
            elif b[1]: parts.extend(f'<p class="item-numerado">{inline(it)}</p>' for it in b[2])
            else: parts.append('<ul>' + ''.join(f'<li>{inline(it)}</li>' for it in b[2]) + '</ul>')
        elif b[0] == 'caja': parts.append(f'<div class="caja" data-ref="{id(b)}"></div>')
    return ''.join(parts)

def borde(cell, color):
    pr = cell._tc.get_or_add_tcPr(); borders = OxmlElement('w:tcBorders')
    for side, size, col in (('left', '36', color), ('top', '4', color), ('bottom', '4', color), ('right', '4', color)):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), size); e.set(qn('w:color'), col); borders.append(e)
    pr.append(borders)
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:fill'), CAJAS_FILL[cell]); pr.append(sh)
    mar = OxmlElement('w:tcMar')
    for side, w in (('top', '140'), ('bottom', '100'), ('left', '220'), ('right', '200')):
        m = OxmlElement(f'w:{side}'); m.set(qn('w:w'), w); m.set(qn('w:type'), 'dxa'); mar.append(m)
    pr.append(mar)

CAJAS_FILL = {}

class BuilderMD(nativo.Builder):
    def __init__(self, doc, folder, cajas):
        super().__init__(doc, folder); self.cajas = cajas; self.stats['recuadros'] = 0
    def module(self, tree, number, etiqueta='Contenido de estudio', indice=True, color=None):
        """Portada, índice opcional y cuerpo; adapta Builder.module a los cuatro entregables."""
        article = tree.xpath('//article')[0]; title = tree.xpath('//h1')[0].text_content().strip()
        p = self.doc.add_paragraph('Gestión de Proyectos Ágiles', style='Subtitle'); p.paragraph_format.space_before = Cm(3)
        rot = number if isinstance(number, str) else f'Módulo {number}'
        col = color if color is not None else number - 1
        p = self.doc.add_paragraph(rot); p.runs[0].font.size = Pt(16); p.runs[0].font.color.rgb = RGBColor.from_string(nativo.PALETTE[col])
        self.doc.add_paragraph(title, style='Title')
        sub = tree.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," subtitle ")]')
        if sub and sub[0].text_content().strip(): self.doc.add_paragraph(sub[0].text_content().strip(), style='Subtitle')
        self.doc.add_paragraph(etiqueta, style='Subtitle')
        self.doc.add_page_break()
        if indice and article.xpath('./h2'):
            self.doc.add_paragraph('Recorrido del módulo' if etiqueta.startswith('Contenido') else etiqueta, style='Heading 1')
            for i, h in enumerate(article.xpath('./h2'), 1):
                q = self.doc.add_paragraph(); nativo.hyperlink(q, h.text_content().strip(), '#' + self.prefix + h.get('id', f'seccion-{i}'))
                q.paragraph_format.space_after = Pt(4)
            self.doc.add_page_break()
        elif not indice:
            h = self.doc.add_paragraph(etiqueta, style='Heading 1'); nativo.shade(h, 'EAF4FA')
        for e in article: self.block(e)
    def block(self, e, fill=None, level=0):
        if isinstance(e.tag, str) and e.tag == 'div' and e.get('class') == 'caja':
            return self.caja(self.cajas[e.get('data-ref')])
        if isinstance(e.tag, str) and e.tag == 'p' and e.get('class') == 'cita':
            p = self.doc.add_paragraph(); nativo.runs(p, nativo.clean(nativo.tokens(e)))
            for r in p.runs: r.italic = True
            f = p.paragraph_format; f.left_indent = Cm(.9); f.right_indent = Cm(.6); f.space_before = Pt(4); f.space_after = Pt(10)
            nativo.shade(p, 'F3F6F9')
            return
        if isinstance(e.tag, str) and e.tag == 'p' and e.get('class') == 'item-anidado':
            nivel = int(e.get('data-nivel', '0')); p = self.doc.add_paragraph()
            if nivel == 0 and re.match(r'\d+\.', e.text_content().strip()):
                self.numerado(p, e); return
            mark = p.add_run('•◦▪▫'[min(nivel, 3)] + '\t'); mark.font.color.rgb = RGBColor.from_string('12655D'); mark.bold = True
            nativo.runs(p, nativo.clean(nativo.tokens(e)))
            f = p.paragraph_format; izq = Cm(.65 + .75 * nivel)
            f.left_indent = izq; f.first_line_indent = Cm(-.45); f.tab_stops.add_tab_stop(izq); f.space_after = Pt(3)
            return
        if isinstance(e.tag, str) and e.tag == 'p' and e.get('class') == 'item-numerado':
            p = self.doc.add_paragraph(); self.numerado(p, e); return
        return super().block(e, fill, level)
    def numerado(self, p, e, color=None):
        ts = nativo.clean(nativo.tokens(e)); m = re.match(r'(\d+\.)\s*', ts[0][0]) if ts else None
        if m:
            p.add_run(m.group(1) + '\t').bold = True; ts[0] = (ts[0][0][m.end():], *ts[0][1:])
        nativo.runs(p, ts)
        f = p.paragraph_format; f.left_indent = Cm(.75); f.first_line_indent = Cm(-.55); f.space_after = Pt(5)
        f.tab_stops.add_tab_stop(Cm(.75))
        if color: self.teñir(p, color)
    def teñir(self, p, color):
        for r in p.runs:
            if r.bold: r.font.color.rgb = RGBColor.from_string(color)
    def caja(self, b):
        _, kind, title, blocks = b
        etiqueta, fill, borde_color, *texto = CAJAS.get(kind, CAJAS['clave'])
        color = texto[0] if texto else borde_color
        title = title or etiqueta
        t = self.doc.add_table(rows=1, cols=1); t.autofit = False
        cell = t.cell(0, 0); cell.width = Cm(16.6); CAJAS_FILL[cell] = fill; borde(cell, borde_color)
        first = cell.paragraphs[0]; used = False
        if title:
            r = first.add_run(title); r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = RGBColor.from_string(color); r.font.name = 'Calibri'
            first.paragraph_format.space_after = Pt(5); used = True
        def nuevo():
            nonlocal used
            if not used: used = True; return first
            return cell.add_paragraph()
        for blk in blocks:
            if blk[0] == 'p':
                el = html.fragment_fromstring(f'<p>{inline(blk[1])}</p>')
                p = nuevo(); nativo.runs(p, nativo.clean(nativo.tokens(el))); self.teñir(p, color)
                p.paragraph_format.space_after = Pt(6); p.paragraph_format.line_spacing = 1.15
                if blk[1].startswith('Fuente:'):
                    for r in p.runs: r.font.size = Pt(9); r.italic = True
                    p.paragraph_format.space_before = Pt(2)
            elif blk[0] == 'lista':
                for it in blk[2]:
                    p = nuevo()
                    if blk[1]: self.numerado(p, html.fragment_fromstring(f'<p>{inline(it)}</p>'), color)
                    else:
                        el = html.fragment_fromstring(f'<p>{inline(it)}</p>')
                        mark = p.add_run('•\t'); mark.font.color.rgb = RGBColor.from_string(color); mark.bold = True
                        nativo.runs(p, nativo.clean(nativo.tokens(el))); self.teñir(p, color)
                        f = p.paragraph_format; f.left_indent = Cm(.6); f.first_line_indent = Cm(-.45); f.tab_stops.add_tab_stop(Cm(.6)); f.space_after = Pt(4)
        for p in cell.paragraphs:
            for r in p.runs:
                if r.font.size is None: r.font.size = Pt(10.5)
        # Recuadros cortos: no se parten entre páginas. Largos: el título queda con el texto.
        if len(''.join(p.text for p in cell.paragraphs)) < 750:
            t.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        elif title:
            first.paragraph_format.keep_with_next = True
            if len(cell.paragraphs) > 1: cell.paragraphs[1].paragraph_format.keep_with_next = True
        sp = self.doc.add_paragraph(); sp.paragraph_format.space_after = Pt(4)
        self.stats['recuadros'] += 1

# Entregables del módulo: carpeta, fuente, archivo final, rótulo de portada y si lleva índice.
TIPOS = {
    'contenido': ('Contenido', 'contenido.md', 'Contenido.docx', 'Contenido de estudio', True),
    'actividades': ('Actividades', 'actividades.md', 'Actividades.docx', 'Actividades formativas', True),
    'respuestas': ('Actividades', 'respuestas-docente.md', 'Respuestas-docente.docx', 'Respuestas orientativas para el docente', False),
    'evaluacion': ('', 'evaluacion.md', 'Evaluacion.docx', 'Evaluación parcial', False),
    'guia': ('', 'guia-docente.md', 'Guia-docente.docx', 'Guía de corrección para el docente', False),
    'glosario': ('Glosario', 'glosario.md', 'Glosario.docx', 'Glosario', False),
    'microobjetivos': ('Microobjetivos', 'microobjetivos.md', 'Microobjetivos.docx', 'Microobjetivos', False),
}

def leer_fuente(ruta):
    """Devuelve (metadatos, texto sin encabezado)."""
    src = ruta.read_text(encoding='utf-8').replace('\r\n', '\n'); meta = {}
    fm = re.match(r'---\n(.*?)\n---\n', src, re.S)
    if fm:
        for l in fm.group(1).splitlines():
            k, _, v = l.partition(':'); meta[k.strip()] = v.strip()
        src = src[fm.end():]
    return meta, src

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--modulo', type=int, choices=range(1, 6))
    ap.add_argument('--parcial', type=int, choices=(1, 2))
    ap.add_argument('--tipo', choices=TIPOS, default='contenido')
    ap.add_argument('--salida', type=Path)
    a = ap.parse_args()
    carpeta, fuente, final, etiqueta, indice = TIPOS[a.tipo]
    if a.tipo in ('evaluacion', 'guia'):
        if not a.parcial: ap.error('--parcial es obligatorio para evaluaciones')
        folder = BASE / 'entregables' / 'EVALUACIONES' / f'PARCIAL {a.parcial}'
        meta = {'materia': 'Gestión de Proyectos Ágiles'}; rotulo = f'Parcial {a.parcial}'; color = a.parcial + 2
    else:
        if not a.modulo: ap.error('--modulo es obligatorio')
        modulo_dir = BASE / 'entregables' / f'MODULO {a.modulo}'
        folder = modulo_dir / carpeta
        # Los datos del módulo (materia, título) salen del Contenido; la fuente propia puede ampliarlos.
        meta, _ = leer_fuente(modulo_dir / 'Contenido' / 'contenido.md'); rotulo = f'Módulo {a.modulo}'; color = a.modulo - 1
    propio, src = leer_fuente(folder / fuente)
    if a.tipo in ('evaluacion', 'guia', 'respuestas'):
        nativo.chunks.__defaults__ = (10**6,)  # sin dividir párrafos: las consignas y criterios se leen enteros
    meta.update({k: v for k, v in propio.items() if v})
    if a.tipo != 'contenido' and 'subtitulo' not in propio: meta['subtitulo'] = ''
    blocks = parse_blocks(src.splitlines())
    cajas = {}
    for bl in blocks:
        if bl[0] == 'caja': cajas[str(id(bl))] = bl
    doc_html = (f'<html><body><h1>{inline(meta.get("titulo", ""))}</h1><p class="subtitle">{inline(meta.get("subtitulo", ""))}</p>'
                f'<article>{to_html(blocks)}</article></body></html>')
    tree = html.fromstring(doc_html).getroottree()
    doc = Document(); nativo.styles(doc, nativo.PALETTE[color])
    b = BuilderMD(doc, folder, cajas); b.module(tree, rotulo, etiqueta, indice, color)
    # El exportador base rotula con el nombre de Gestión; se reemplaza por el de la materia.
    base_nombre = 'Gestión de Proyectos Ágiles'; materia = meta.get('materia', base_nombre)
    if materia != base_nombre:
        for par in list(doc.paragraphs) + list(doc.sections[0].footer.paragraphs):
            for r in par.runs: r.text = r.text.replace(base_nombre, materia)
    doc.core_properties.title = f'{materia} {rotulo} {etiqueta}'
    doc.core_properties.subject = f'{etiqueta} de {materia}'
    # Filas de tablas comparativas sin cortes entre páginas (los recuadros sí pueden partirse).
    for t in doc.tables:
        if len(t.rows) > 1:
            for row in t.rows: row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
    nativo.finalize(doc)
    out = a.salida or folder / final; doc.save(out)
    print(json.dumps({'rotulo': rotulo, 'tipo': a.tipo, 'archivo': str(out), **b.stats}, ensure_ascii=False))

if __name__ == '__main__': main()
