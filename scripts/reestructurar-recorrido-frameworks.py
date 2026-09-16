from __future__ import annotations

import re
import shutil
from copy import deepcopy
from pathlib import Path

from lxml import etree, html


BASE = Path(__file__).resolve().parents[1]
BACKUP = BASE / ".qa" / "reestructuracion-frameworks-2026-09-16" / "antes"


LABELS = {
    "general": ("CONCEPTO GENERAL", "Estas ideas sirven para distintos enfoques. Cuando una práctica pertenezca a un marco concreto, lo indicaremos expresamente."),
    "agilidad": ("FUNDAMENTOS DE AGILIDAD", "Este bloque explica por qué surge la agilidad, qué valores la orientan y cómo convierte incertidumbre en aprendizaje y entrega de valor."),
    "scrum": ("CONTEXTO: SCRUM", "Desde aquí trabajamos dentro de Scrum. Sus responsabilidades, eventos y artefactos no deben atribuirse automáticamente a Kanban, Lean u otros enfoques."),
    "kanban": ("CONTEXTO: KANBAN", "Desde aquí analizamos Kanban como sistema de gestión del trabajo y del flujo. Kanban no exige Sprints ni los roles de Scrum."),
    "xp": ("CONTEXTO: EXTREME PROGRAMMING", "Este bloque reúne prácticas técnicas de desarrollo. Pueden complementar otros marcos, pero no forman parte obligatoria de Scrum o Kanban."),
    "lean": ("CONTEXTO: LEAN", "Este bloque observa valor, desperdicio y mejora del sistema completo. Lean aporta principios para decidir; no prescribe los eventos ni los roles de Scrum."),
    "combinacion": ("COMPARACIÓN E INTEGRACIÓN", "Recién después de comprender cada enfoque por separado podemos compararlos o combinarlos sin mezclar sus reglas."),
    "producto": ("GESTIÓN DE PRODUCTO", "Estas prácticas ayudan a decidir qué problema resolver y qué aprender. Algunas son generales y otras se aplican aquí dentro del contexto Scrum."),
    "practicas": ("PRÁCTICAS COMPLEMENTARIAS", "Estas técnicas pueden ayudar a expresar, preparar o priorizar trabajo, pero no son reglas obligatorias de Scrum ni pertenecen a un único framework."),
    "herramientas": ("HERRAMIENTAS DE SEGUIMIENTO", "La herramienta representa el sistema de trabajo que el equipo ya acordó. Un tablero o un informe no determina por sí solo si se usa Scrum o Kanban."),
    "transversal": ("APLICACIÓN TRANSVERSAL", "El tema se aplica en Scrum, Kanban u otros enfoques. Cambian las responsabilidades y las políticas concretas, no la necesidad de gestionarlo."),
    "ingenieria": ("PRÁCTICAS DE INGENIERÍA", "Este bloque conecta la agilidad con calidad técnica, integración y operación. Las prácticas se eligen por el problema que resuelven."),
    "organizacion": ("ESCALA Y ORGANIZACIÓN", "Aquí cambia el nivel de análisis: pasamos del equipo a la coordinación entre equipos y al gobierno de la organización."),
    "caso": ("CASO DE INGENIERÍA EN IA", "El asistente universitario integra las decisiones del módulo. Las métricas de producto, calidad del modelo y riesgo se leen junto con el trabajo del equipo."),
}


def clean_title(text: str) -> str:
    return re.sub(r"^\s*\d+(?:\.\d+)*\.?\s*", "", " ".join(text.split()))


def p(text: str, cls: str | None = None):
    e = etree.Element("p")
    if cls:
        e.set("class", cls)
    e.text = text
    return e


def context(kind: str):
    label, message = LABELS[kind]
    e = etree.Element("div", {"class": f"marco-contexto contexto-{kind}"})
    strong = etree.SubElement(e, "strong")
    strong.text = label
    strong.tail = " " + message
    return e


def transition(text: str):
    e = etree.Element("div", {"class": "transicion-marco"})
    strong = etree.SubElement(e, "strong")
    strong.text = "Cambio de contexto. "
    strong.tail = text
    return e


def direct_sections(article):
    children = list(article)
    starts = [i for i, e in enumerate(children) if e.tag == "h2"]
    result = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(children)
        heading = children[start]
        result.append({"title": clean_title(heading.text_content()), "nodes": children[start:end]})
    prefix = children[: starts[0]] if starts else children
    return prefix, result


def numbered_map(sections):
    return {s["title"]: s for s in sections if re.match(r"^\d+\.", " ".join(s["nodes"][0].text_content().split()))}


def supplemental(sections):
    return [s for s in sections if not re.match(r"^\d+\.", " ".join(s["nodes"][0].text_content().split()))]


def add_css(tree):
    style = tree.xpath("//style")[0]
    if ".marco-contexto" in (style.text or ""):
        return
    style.text = (style.text or "") + """
.marco-contexto,.transicion-marco{margin:22px 0 14px;padding:13px 16px;border-radius:9px;break-inside:avoid;font:9.8pt/1.5 \"Segoe UI\",Arial,sans-serif;}
.marco-contexto{background:#eef5fb;border:1px solid #cdddea;border-left:6px solid var(--blue);color:#29465f;}
.marco-contexto strong{display:block;margin-bottom:4px;color:var(--navy);font-size:8.2pt;letter-spacing:.1em;text-transform:uppercase;}
.contexto-scrum{background:#eaf4fa;border-color:#c7dfed;border-left-color:#2878a9;}
.contexto-kanban{background:#e8f6f3;border-color:#c9e8e2;border-left-color:#16877b;}
.contexto-xp,.contexto-ingenieria{background:#f2edf8;border-color:#dfd3ed;border-left-color:#76549f;}
.contexto-lean,.contexto-organizacion{background:#fbf2dd;border-color:#eddbae;border-left-color:#c68a24;}
.contexto-caso{background:#fbeeee;border-color:#ebcccc;border-left-color:#c25555;}
.transicion-marco{background:#fbf8f1;border-top:1px solid #e6dcc8;border-bottom:1px solid #e6dcc8;color:#536173;font-style:italic;}
.transicion-marco strong{color:#815b19;font-style:normal;}
"""


def copy_nodes(nodes, skip_heading=False):
    source = nodes[1:] if skip_heading else nodes
    return [deepcopy(n) for n in source]


def make_heading(title: str):
    h = etree.Element("h2")
    h.text = title
    return h


def composite(title: str, parts, intro: str | None = None):
    nodes = [make_heading(title)]
    if intro:
        nodes.append(p(intro))
    for subtitle, section in parts:
        h = etree.Element("h3")
        h.text = subtitle
        nodes.append(h)
        for node in copy_nodes(section["nodes"], skip_heading=True):
            if node.tag == "h3":
                node.tag = "h4"
                node.text = clean_title(node.text_content())
            nodes.append(node)
    return {"title": title, "nodes": nodes}


def simple_section(title: str, body_html: str):
    container = html.fragment_fromstring(f"<div>{body_html}</div>")
    return {"title": title, "nodes": [make_heading(title)] + [deepcopy(x) for x in container]}


def split_subsection(section, wanted_title: str):
    nodes = section["nodes"]
    positions = [i for i, n in enumerate(nodes) if n.tag == "h3"]
    for idx, start in enumerate(positions):
        title = clean_title(nodes[start].text_content())
        if title == wanted_title:
            end = next((x for x in positions if x > start), len(nodes))
            return [deepcopy(x) for x in nodes[start:end]]
    raise KeyError(wanted_title)


def renumber(article):
    major = 0
    minor = 0
    subminor = 0
    for node in article:
        if node.tag == "h2":
            title = clean_title(node.text_content())
            if title in {"Fuentes para profundizar", "Recursos audiovisuales sugeridos", "Síntesis del módulo"}:
                node.text = title
                slug = {"Fuentes para profundizar": "fuentes", "Recursos audiovisuales sugeridos": "recursos", "Síntesis del módulo": "sintesis"}[title]
                node.set("id", f"seccion-{slug}")
                continue
            major += 1
            minor = 0
            subminor = 0
            node.text = f"{major}. {title}"
            node.set("id", f"seccion-{major}")
        elif node.tag == "h3" and major:
            title = clean_title(node.text_content())
            if title == "Cómo recorrer este módulo":
                node.text = title
                continue
            minor += 1
            subminor = 0
            node.text = f"{major}.{minor} {title}"
        elif node.tag == "h4" and major:
            title = clean_title(node.text_content())
            subminor += 1
            node.text = f"{major}.{minor}.{subminor} {title}"


def rebuild_nav(tree, article):
    nav_ol = tree.xpath('//nav[contains(@class,"chapter-map")]/ol')[0]
    nav_ol.clear()
    for h in article.xpath("./h2"):
        title = " ".join(h.text_content().split())
        li = etree.SubElement(nav_ol, "li")
        a = etree.SubElement(li, "a", href="#" + h.get("id"))
        a.text = clean_title(title)


def replace_article(article, prefix, ordered, extras, labels):
    for child in list(article):
        article.remove(child)
    for node in prefix:
        article.append(deepcopy(node))
    for index, section in enumerate(ordered):
        for marker in labels.get(index, []):
            article.append(marker)
        for node in section["nodes"]:
            article.append(deepcopy(node))
    for section in extras:
        for node in section["nodes"]:
            article.append(deepcopy(node))
    renumber(article)


def update_route_list(article, items):
    h = article.xpath('./h3[normalize-space()="Cómo recorrer este módulo"]')
    if not h:
        return
    e = h[0].getnext()
    if e is not None and e.tag in {"ol", "ul"}:
        e.clear()
        for item in items:
            li = etree.SubElement(e, "li")
            li.text = item


def restructure_standard(n: int, order_titles, labels, route, renames=None):
    path = BASE / "entregables" / f"MODULO {n}" / "Contenido" / "contenido.html"
    tree = html.parse(str(path))
    add_css(tree)
    article = tree.xpath("//article")[0]
    prefix, sections = direct_sections(article)
    mapping = numbered_map(sections)
    extras = supplemental(sections)
    for old, new in (renames or {}).items():
        mapping[old]["nodes"][0].text = new
        mapping[old]["title"] = new
    ordered = [mapping[t] for t in order_titles]
    replace_article(article, prefix, ordered, extras, labels)
    update_route_list(article, route)
    rebuild_nav(tree, article)
    article.set("data-reestructuracion-frameworks", "2026-09-16")
    tree.write(str(path), encoding="utf-8", method="html", pretty_print=True, doctype="<!DOCTYPE html>")


def restructure_m4():
    path = BASE / "entregables" / "MODULO 4" / "Contenido" / "contenido.html"
    tree = html.parse(str(path))
    add_css(tree)
    article = tree.xpath("//article")[0]
    prefix, sections = direct_sections(article)
    m = numbered_map(sections)

    scrum_board = split_subsection(m["Tableros, carriles y límites WIP"], "El tablero Scrum")
    kanban_board_all = copy_nodes(m["Tableros, carriles y límites WIP"]["nodes"], skip_heading=True)
    kept = []
    skipping = False
    for node in kanban_board_all:
        if node.tag == "h3":
            name = clean_title(node.text_content())
            skipping = name == "El tablero Scrum"
            if name != "El tablero Scrum":
                skipping = False
        if not skipping:
            kept.append(node)

    sections_new = []
    general_nodes = []
    planning_visuals = []
    inserted_general_bridge = False
    for source_node in m["Estimar y pronosticar bajo incertidumbre"]["nodes"]:
        node = deepcopy(source_node)
        text = " ".join(node.text_content().split())
        if node.tag == "p" and text.startswith(("La gestión ágil parte", "La estimación relativa", 'Es importante aclarar que "estimación ágil"')):
            if not inserted_general_bridge:
                general_nodes.append(p("Estimar no es adivinar ni prometer una cifra inmóvil. Es formular una hipótesis útil para decidir y actualizarla cuando aparece evidencia. Podemos estimar tamaño, esfuerzo o duración y también pronosticar fechas o cantidad de entregas; cada respuesta necesita datos y supuestos diferentes. En los bloques de Scrum y Kanban veremos técnicas concretas sin presentarlas como universales."))
                inserted_general_bridge = True
            continue
        if node.tag == "figure" and "Planning Poker" in text:
            planning_visuals.append(node)
            continue
        if node.tag == "div" and "mito" in node.get("class", "") and "Story Point" in text:
            planning_visuals.append(node)
            continue
        general_nodes.append(node)
    sections_new.append({"title": "Estimar y pronosticar bajo incertidumbre", "nodes": general_nodes})
    sections_new.append({"title": "Cómo se planifica el trabajo en Scrum", "nodes": [make_heading("Cómo se planifica el trabajo en Scrum")] + copy_nodes(m["Planificar un Sprint"]["nodes"], True)})
    estimation_section = composite(
        "Prácticas complementarias de estimación en Scrum",
        [
            ("Tallas de remera", m["Tallas de remera: estimación inicial"]),
            ("Story Points", m["Story Points: tamaño relativo del trabajo"]),
            ("Planning Poker", m["Planning Poker: estimación colaborativa"]),
        ],
        "Scrum no exige Story Points, Fibonacci ni Planning Poker. Algunos equipos los usan para conversar sobre tamaño e incertidumbre; otros pronostican con datos de flujo. La técnica debe ayudar a decidir, no convertirse en una regla del marco."
    )
    estimation_section["nodes"].extend(planning_visuals)
    sections_new.append(estimation_section)
    sections_new.append(composite(
        "Capacidad, velocidad y pronósticos en Scrum",
        [
            ("Capacidad y disponibilidad", m["Capacidad y disponibilidad del equipo"]),
            ("Velocidad y sus límites", m["Velocidad del equipo y pronósticos"]),
        ],
        "En este bloque seguimos dentro de Scrum. Capacidad describe disponibilidad futura; velocidad resume una observación histórica del mismo equipo. Ninguna de las dos mide productividad individual."
    ))
    follow_nodes = [make_heading("Seguimiento de un Sprint")]
    follow_nodes += copy_nodes(m["Hacer visible el trabajo"]["nodes"], True)
    follow_nodes += scrum_board
    for title in ["Burndown: observar trabajo pendiente", "Burnup: separar avance y alcance"]:
        h = etree.Element("h3"); h.text = clean_title(title); follow_nodes.append(h)
        follow_nodes += copy_nodes(m[title]["nodes"], True)
    sections_new.append({"title": "Seguimiento de un Sprint", "nodes": follow_nodes})
    sections_new.append(simple_section("Caso completo: planificar y seguir un Sprint del asistente", """
<p>El Scrum Team define como Sprint Goal: <strong>“permitir que estudiantes de primer año encuentren requisitos de inscripción vigentes y comprendan la fuente de cada respuesta”</strong>. Los Developers seleccionan trabajo después de revisar capacidad, dependencias, Definition of Done y evidencia del Sprint anterior.</p>
<ol class="caso-resuelto"><li><strong>Planificación:</strong> acuerdan el objetivo y construyen un Sprint Backlog; la selección es un pronóstico adaptable.</li><li><strong>Seguimiento:</strong> el Daily Scrum inspecciona avance hacia el Sprint Goal. El tablero y el burnup revelan que creció el alcance al aparecer una nueva fuente.</li><li><strong>Decisión:</strong> protegen el objetivo, negocian dejar una mejora visual fuera del Sprint y prueban temprano la fuente más riesgosa.</li><li><strong>Aprendizaje:</strong> en la Sprint Review contrastan respuestas con estudiantes y autoridades; en la retrospectiva revisan cómo reducir esperas por validación.</li></ol>
<div class="criterio-profesional"><strong>Lectura correcta:</strong> cumplir puntos no reemplaza alcanzar el Sprint Goal, entregar un incremento utilizable y aprender con stakeholders.</div>"""))

    sections_new.append(simple_section("Cómo se gestiona el trabajo en Kanban", """
<p>Ahora cambia el sistema de trabajo. En Kanban no planificamos un Sprint ni necesitamos un Scrum Master. Gestionamos una <strong>demanda continua</strong>, hacemos explícitas las políticas y tomamos nuevo trabajo cuando existe capacidad disponible.</p>
<ul><li><strong>Visualizar:</strong> representar el flujo real desde la solicitud hasta la entrega.</li><li><strong>Limitar WIP:</strong> evitar que comenzar sea más fácil que terminar.</li><li><strong>Gestionar el flujo:</strong> observar bloqueos, envejecimiento, tiempos y ritmo de salida.</li><li><strong>Políticas explícitas:</strong> acordar qué significa entrar, avanzar, bloquear y terminar.</li><li><strong>Bucles de feedback:</strong> revisar servicio y políticas con una cadencia adecuada al contexto.</li></ul>
<p>El ejemplo será el soporte del asistente universitario: llegan incidentes, consultas y pedidos regulatorios sin esperar al inicio de un Sprint. El equipo toma el siguiente ítem según prioridad, clase de servicio y capacidad del sistema.</p>"""))
    kanban_nodes = [make_heading("Tablero Kanban, políticas y límites WIP")] + kept
    sections_new.append({"title": "Tablero Kanban, políticas y límites WIP", "nodes": kanban_nodes})
    sections_new.append(composite(
        "Métricas de flujo en Kanban",
        [
            ("Lead Time y Cycle Time", m["Lead Time y Cycle Time"]),
            ("Throughput", m["Throughput: ritmo de finalización"]),
        ],
        "Estas métricas describen el comportamiento del sistema de flujo. Se interpretan como distribuciones y tendencias; una cifra aislada no explica la causa de una demora."
    ))
    sections_new.append({"title": "Diagrama de flujo acumulado", "nodes": [deepcopy(x) for x in m["Diagrama de flujo acumulado"]["nodes"]]})
    sections_new.append(simple_section("Pronósticos basados en flujo", """
<p>Kanban permite pronosticar sin convertir cada tarjeta a Story Points. Si conservamos fechas de inicio y finalización, podemos usar la distribución histórica de <strong>Cycle Time</strong> para responder cuánto podría tardar un ítem, y el <strong>Throughput</strong> para estimar cuántos ítems podrían terminarse en un período.</p>
<p>Un pronóstico profesional comunica probabilidad y condiciones: “el 85 % de los incidentes comparables terminó en hasta seis días durante las últimas doce semanas”. Si cambian la mezcla de trabajo, el equipo o las políticas, el pronóstico debe recalibrarse.</p>
<div class="criterio-profesional"><strong>Criterio profesional:</strong> No sumes promedios como si fueran promesas. Usá percentiles o simulaciones con datos comparables y explicá qué supuestos podrían alterar el resultado.</div>"""))
    sections_new.append(simple_section("Caso completo: soporte del asistente gestionado con Kanban", """
<p>Después del lanzamiento, el asistente recibe incidentes de fuentes vencidas, pedidos de actualización y mejoras menores. La demanda es continua y de tamaño variable.</p>
<ol class="caso-resuelto"><li>El equipo dibuja el flujo real: <strong>Solicitado → Análisis → En curso → Validación académica → Terminado</strong>.</li><li>Define límites WIP y una política: ningún cambio de fuente se termina sin registrar vigencia, responsable y prueba de respuesta.</li><li>Marca los ítems bloqueados y revisa su antigüedad diariamente; una acumulación en validación conduce a acordar una guardia rotativa con referentes académicos.</li><li>Usa Cycle Time y Throughput históricos para comunicar un rango de servicio, sin inventar Sprints ni velocidad.</li></ol>
<div class="criterio-profesional"><strong>Resultado:</strong> el tablero muestra dónde espera el trabajo y las métricas ayudan a revisar el servicio; no se utilizan para comparar personas.</div>"""))
    impediments = [deepcopy(x) for x in m["Gestionar impedimentos y bloqueos"]["nodes"]]; impediments[0].text = "Impedimentos y bloqueos"
    risks = [deepcopy(x) for x in m["Gestionar riesgos y dependencias"]["nodes"]]; risks[0].text = "Riesgos y dependencias"
    sections_new.append({"title": "Impedimentos y bloqueos", "nodes": impediments})
    sections_new.append({"title": "Riesgos y dependencias", "nodes": risks})
    sections_new.append({"title": "Herramientas para gestionar el trabajo", "nodes": [deepcopy(x) for x in m["Herramientas para gestionar el trabajo"]["nodes"]]})
    sections_new.append(simple_section("Scrum y Kanban: qué cambia y qué se conserva", """
<table><caption>Comparación para evitar mezclar contextos</caption><thead><tr><th>Pregunta</th><th>Scrum</th><th>Kanban</th></tr></thead><tbody>
<tr><td>¿Cómo organiza el tiempo?</td><td>Sprints de duración fija.</td><td>Flujo continuo; las cadencias de revisión se acuerdan.</td></tr>
<tr><td>¿Qué orienta el trabajo?</td><td>Product Goal y Sprint Goal.</td><td>Propósito del servicio, demanda y políticas explícitas.</td></tr>
<tr><td>¿Qué responsabilidades exige?</td><td>Product Owner, Scrum Master y Developers dentro del Scrum Team.</td><td>No prescribe roles; las responsabilidades se definen en el sistema.</td></tr>
<tr><td>¿Cómo limita trabajo?</td><td>Selección para el Sprint y foco en el Sprint Goal; puede sumar límites WIP.</td><td>Límites WIP explícitos por estado o sistema.</td></tr>
<tr><td>¿Qué datos suelen ayudar?</td><td>Progreso hacia el objetivo, incremento, burndown o burnup y evidencia de valor.</td><td>WIP, antigüedad, Lead Time, Cycle Time, Throughput y CFD.</td></tr>
</tbody></table>
<p>Un tablero con columnas no convierte a un equipo en Kanban, y usar Jira no convierte a un equipo en Scrum. Primero se define el sistema de trabajo; después se configura la herramienta para hacerlo visible.</p>"""))
    sections_new.append(simple_section("Cuándo y cómo combinar prácticas", """
<p>Un Scrum Team puede usar prácticas de Kanban para mejorar el flujo dentro del Sprint: visualizar estados reales, limitar WIP, observar antigüedad y medir Cycle Time. La combinación no elimina el Sprint Goal, los eventos, los artefactos ni las responsabilidades de Scrum.</p>
<p>También puede existir un producto con dos sistemas coordinados: desarrollo de nuevas capacidades mediante Scrum y atención de incidentes mediante Kanban. En ese caso se explicitan personas, políticas, prioridades y capacidad disponible para evitar que la urgencia destruya el foco.</p>
<div class="mito"><strong>Mezcla confusa:</strong> Llamar “Kanban” a cualquier tablero o cancelar eventos de Scrum sin reemplazar su propósito. <strong>Integración consciente:</strong> Identificar qué problema resuelve cada práctica y conservar reglas coherentes.</div>"""))
    sections_new.append(simple_section("Caso integrador: un producto, dos tipos de demanda", """
<p>El equipo del asistente desarrolla una nueva capacidad para explicar correlatividades. Ese trabajo necesita objetivo compartido, validación con estudiantes y un incremento integrado: se gestiona mediante Scrum. Al mismo tiempo, el servicio en producción recibe incidentes por documentos desactualizados: se atienden mediante un flujo Kanban con políticas de prioridad.</p>
<ol class="caso-resuelto"><li><strong>Separar:</strong> cada demanda entra al sistema que corresponde; no se esconde soporte dentro del Sprint.</li><li><strong>Conectar:</strong> incidentes repetidos pueden generar oportunidades para el Product Backlog.</li><li><strong>Reservar capacidad:</strong> el equipo acuerda quién atiende el flujo operativo y cuándo una urgencia justifica renegociar el Sprint.</li><li><strong>Aprender:</strong> compara valor, calidad de respuestas, riesgo y comportamiento del flujo antes de cambiar políticas.</li></ol>
<p>La integración funciona porque cada contexto se entiende primero por separado. La herramienta puede mostrar ambos tableros, pero no decide las políticas por el equipo.</p>"""))

    labels = {
        0: [context("general")],
        1: [transition("Pasamos de conceptos generales a Scrum."), context("scrum")],
        6: [transition("Cerramos el seguimiento basado en Sprints. Ahora cambia el sistema: estudiaremos flujo continuo en Kanban."), context("kanban")],
        12: [transition("Terminamos el bloque específico de Kanban. Los siguientes temas son transversales y se adaptan al sistema de trabajo elegido."), context("transversal")],
        14: [transition("Las herramientas implementan acuerdos; no definen por sí solas el enfoque."), context("herramientas")],
        15: [transition("Con Scrum y Kanban ya estudiados por separado, ahora sí podemos compararlos e integrarlos."), context("combinacion")],
        17: [context("caso")],
    }
    replace_article(article, prefix, sections_new, supplemental(sections), labels)
    update_route_list(article, [
        "Distinguir estimación, pronóstico y compromiso.",
        "Planificar y seguir un Sprint dentro del contexto Scrum.",
        "Gestionar demanda continua y métricas de flujo dentro del contexto Kanban.",
        "Tratar bloqueos, riesgos y dependencias como prácticas transversales.",
        "Configurar Trello, Jira o Notion a partir del sistema de trabajo.",
        "Comparar e integrar Scrum y Kanban mediante un caso de Ingeniería en IA.",
    ])
    intro = article.xpath("./p[1]")
    if intro:
        intro[0].text = "Tenemos un backlog ordenado. Ahora aprenderemos dos formas diferentes de conducir el trabajo sin fingir certeza: primero Scrum, con Sprints y objetivos; después Kanban, con flujo continuo y políticas explícitas. Al final compararemos ambos contextos y recién entonces veremos cómo combinarlos."
    title = tree.xpath("//header[contains(@class,'opener')]/h1")[0]
    title.text = "Planificación y Seguimiento del Trabajo en Scrum y Kanban"
    subtitle = tree.xpath("//header[contains(@class,'opener')]//*[contains(@class,'subtitle')]")[0]
    subtitle.text = "Dos sistemas de trabajo explicados por separado, métricas usadas con criterio y herramientas configuradas a partir del proceso."
    rebuild_nav(tree, article)
    article.set("data-reestructuracion-frameworks", "2026-09-16")
    tree.write(str(path), encoding="utf-8", method="html", pretty_print=True, doctype="<!DOCTYPE html>")


def main():
    BACKUP.mkdir(parents=True, exist_ok=True)
    for n in range(1, 6):
        src = BASE / "entregables" / f"MODULO {n}" / "Contenido" / "contenido.html"
        dst = BACKUP / f"modulo-{n}-contenido.html"
        if not dst.exists():
            shutil.copy2(src, dst)
        else:
            shutil.copy2(dst, src)

    restructure_standard(
        1,
        [
            "Concepto de proyecto y gestión de proyectos", "Proyecto, producto y operación", "Quiénes participan en un proyecto: stakeholders y roles", "Alcance, tiempo, costo y calidad",
            "Ciclo de vida y procesos de gestión de un proyecto", "Gestión predictiva y modelo en cascada", "Enfoques predictivos, iterativos e incrementales", "Gestión del cambio en enfoques predictivos y ágiles",
            "Qué es la agilidad", "Origen de la agilidad", "El Manifiesto Ágil", "Los 12 principios ágiles", "Entrega de valor", "Enfoques, metodologías y marcos de trabajo", "Comparación y selección de enfoques",
        ],
        {
            0: [context("general")],
            4: [transition("Con los límites del proyecto claros, comparamos cómo organizar su ciclo de vida y responder al cambio."), context("general")],
            8: [transition("Ya entendemos el problema de gestión. Ahora podemos presentar la agilidad como una respuesta a contextos con incertidumbre."), context("agilidad")],
            14: [transition("Cerramos los fundamentos. Aplicaremos criterios para elegir sin convertir un enfoque en una receta universal."), context("combinacion")],
        },
        ["Comprender qué es un proyecto, qué se gestiona y quiénes intervienen.", "Reconocer límites, ciclo de vida y decisiones de cambio.", "Comparar enfoques predictivos, iterativos e incrementales.", "Comprender la agilidad, su origen, valores y principios.", "Elegir un enfoque según incertidumbre, riesgo y evidencia, incluido un proyecto de IA."],
    )
    restructure_standard(
        2,
        ["Panorama de metodologías y marcos ágiles", "Scrum: visión general y ejemplo de funcionamiento", "Fundamentos de Scrum: empirismo y valores", "Roles en Scrum", "Artefactos y compromisos de Scrum", "Eventos de Scrum y desarrollo de un Sprint", "Kanban: origen, principios y visualización", "Flujo de trabajo y límites WIP en Kanban", "Extreme Programming (XP) y prácticas de desarrollo", "Lean aplicado al desarrollo de software", "Scrumban y Scrum con Kanban", "Otros enfoques ágiles: Crystal, FDD y DSDM", "Comparación entre metodologías y marcos ágiles", "Selección del enfoque y caso resuelto"],
        {
            0: [context("general")], 1: [transition("El primer bloque completo corresponde a Scrum."), context("scrum")],
            6: [transition("Cerramos Scrum. Cambian las reglas: Kanban gestiona flujo y no prescribe los roles ni los eventos de Scrum."), context("kanban")],
            8: [transition("Cerramos Kanban. Ahora observaremos prácticas técnicas propias de XP."), context("xp")],
            9: [transition("XP se concentró en ingeniería. Lean amplía la mirada al valor y al sistema completo."), context("lean")],
            10: [transition("Ya estudiamos Scrum, Kanban, XP y Lean por separado. Recién ahora analizamos combinaciones."), context("combinacion")],
            12: [transition("Completado el panorama, comparamos y seleccionamos según el contexto."), context("combinacion")],
        },
        ["Ubicar cada enfoque en un mapa común.", "Comprender Scrum completo: fundamentos, responsabilidades, artefactos y eventos.", "Comprender Kanban como sistema de gestión del flujo.", "Distinguir las prácticas técnicas de XP y los principios Lean.", "Comparar, combinar y elegir enfoques sin mezclar sus reglas."],
        {"Roles en Scrum": "Responsabilidades del Scrum Team"},
    )
    restructure_standard(
        3,
        ["Visión y objetivos del producto", "Comprender necesidades e interesados", "Product Backlog: organizar las necesidades", "Épicas, funcionalidades, historias y tareas", "Historias de usuario", "Criterios de aceptación", "Calidad y Definition of Done", "Preparación del trabajo y Definition of Ready", "Refinamiento del backlog", "Priorizar necesidades y oportunidades", "Producto mínimo viable y aprendizaje", "Roadmap: comunicar la evolución del producto", "Planificación de lanzamientos", "Gestión del alcance", "Evaluar y gestionar cambios"],
        {
            0: [context("producto")],
            2: [transition("Con visión y necesidades claras, entramos al contexto Scrum para estudiar el Product Backlog y sus compromisos."), context("scrum")],
            3: [transition("Las siguientes técnicas ayudan a expresar y preparar trabajo. Son prácticas complementarias: Scrum no exige historias, INVEST, DoR ni un formato único de refinamiento."), context("practicas")],
            10: [transition("Cerramos la preparación del backlog. Volvemos a decisiones de producto y aprendizaje que pueden aplicarse en distintos enfoques."), context("producto")],
            14: [context("caso")],
        },
        ["Definir visión, objetivos y evidencia de éxito para un producto de IA.", "Comprender usuarios, stakeholders y necesidades.", "Organizar el Product Backlog dentro del contexto Scrum.", "Usar historias, criterios, calidad, refinamiento y priorización como prácticas complementarias.", "Diseñar MVP, roadmap, releases y decisiones de cambio con una narrativa de producto."],
        {"Product Backlog: organizar las necesidades": "Product Backlog en Scrum: organizar las necesidades", "Calidad y Definition of Done": "Definition of Done en Scrum y calidad"},
    )
    restructure_m4()
    restructure_standard(
        5,
        ["Composición y estabilidad del equipo", "Autogestión y autoorganización", "Liderazgo y decisiones del equipo", "Liderazgo de servicio", "Comunicación efectiva", "Gestionar conflictos", "Feedback continuo", "Colaboración con interesados", "Trabajo remoto y equipos distribuidos", "Sprint Review: inspeccionar y adaptar el producto", "Retrospectivas: mejorar la forma de trabajar", "Mejora continua y Kaizen", "Calidad y deuda técnica", "Integración, entrega y despliegue continuos", "DevOps y responsabilidad compartida", "Coordinar varios equipos: Scrum of Scrums, SAFe y LeSS", "Agilidad y gobierno de la organización", "Casos reales, escenarios de transformación y desafíos de adopción", "Caso integrador: gestionar un asistente universitario con IA"],
        {
            0: [context("general")],
            9: [transition("Cerramos las prácticas generales de colaboración. La Sprint Review pertenece específicamente a Scrum."), context("scrum")],
            10: [transition("La Sprint Review inspecciona el producto. La Sprint Retrospective, también dentro de Scrum, inspecciona cómo trabaja el equipo."), context("scrum")],
            11: [transition("Cerramos los eventos de Scrum. Kaizen amplía la mejora continua más allá de una retrospectiva."), context("lean")],
            12: [transition("La mejora requiere sostén técnico. Ahora observamos calidad, entrega y operación."), context("ingenieria")],
            15: [transition("Cambiamos de nivel: del equipo y su producto a la coordinación y al gobierno organizacional."), context("organizacion")],
            17: [transition("Con los conceptos ya diferenciados, analizamos evidencia, límites y desafíos de adopción."), context("combinacion")],
            18: [context("caso")],
        },
        ["Construir equipos estables, autónomos y responsables de un resultado.", "Comunicarse, gestionar conflictos y colaborar con stakeholders.", "Distinguir Sprint Review, retrospectiva y mejora continua.", "Conectar agilidad con calidad, deuda técnica, CI/CD y DevOps.", "Comprender coordinación y gobierno a escala.", "Analizar casos y cerrar el recorrido con el asistente universitario de IA."],
        {"Retrospectivas: mejorar la forma de trabajar": "Sprint Retrospective: mejorar la forma de trabajar"},
    )
    print("Reestructuración pedagógica aplicada a los módulos 1 a 5.")


if __name__ == "__main__":
    main()
