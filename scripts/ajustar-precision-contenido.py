from pathlib import Path
from lxml import html,etree
import re
BASE=Path(__file__).resolve().parents[1]
def replace(a,key,new):
    hits=[e for e in a.xpath('.//p|.//li') if key in ' '.join(e.text_content().split())]
    if len(hits)!=1: raise ValueError((key,len(hits)))
    old=hits[0]; old.getparent().replace(old,html.fragment_fromstring(new))
for n in range(1,6):
    p=BASE/'entregables'/f'MODULO {n}'/'Contenido/contenido.html'; t=html.parse(str(p)); a=t.xpath('//article')[0]
    if n==2:
        replace(a,'Primero veremos Scrum en funcionamiento','<p>En el Módulo 1 aprendimos a elegir un enfoque según incertidumbre, valor y restricciones. Ahora observamos Scrum en funcionamiento y comprendemos sus fundamentos antes de profundizar responsabilidades, artefactos y eventos. Después estudiamos Kanban y Lean, con XP y otros enfoques como ampliación. La finalidad es explicar qué problema resuelve cada mecanismo y qué condiciones necesita para funcionar.</p>')
        for e in a.xpath('.//p'):
            if 'que garantiza que el comportamiento no cambió' in e.text_content():
                s=etree.tostring(e,encoding='unicode').replace('que garantiza que el comportamiento no cambió','que ayuda a detectar cambios de comportamiento, sin garantizar ausencia de defectos'); e.getparent().replace(e,html.fragment_fromstring(s))
    if n==3:
        for e in a.xpath('.//p'):
            if 'garantizando calidad y transparencia' in e.text_content():
                s=etree.tostring(e,encoding='unicode').replace('garantizando calidad y transparencia','haciendo explícito el estándar de calidad y favoreciendo la transparencia'); e.getparent().replace(e,html.fragment_fromstring(s))
        replace(a,'Lo ideal es refinar el backlog','<p>Conviene preparar el trabajo cercano antes de seleccionarlo. Durante el refinamiento se descomponen elementos, aclaran criterios, investigan dudas y dependencias y revisan orden y tamaño. No hay un horizonte obligatorio ni es necesario cumplir una Definition of Ready: si el equipo adoptó ese acuerdo opcional, lo usa para conversar sobre preparación. Los ítems lejanos pueden mantener menos detalle porque todavía es probable que cambien.</p>')
    if n==4:
        replace(a,'donde cada número es aproximadamente la suma','<p>Algunos equipos usan la escala <strong>1, 2, 3, 5, 8, 13, 20, 40, 100</strong>. Se conoce como Fibonacci modificada: coincide al principio con la sucesión, pero 20, 40 y 100 son categorías ampliadas, no sumas exactas de los dos valores anteriores. Separar más los tamaños grandes evita discutir diferencias que no podemos justificar con el conocimiento disponible. Es una convención opcional, no una medición física ni una exigencia de Scrum.</p>')
        replace(a,'Backlogs jerárquicos','<li><strong>Jerarquía de trabajo:</strong> según configuración, Jira organiza épicas, elementos estándar —como historias, tareas o errores— y subtareas. Un bug es un tipo de elemento; no constituye necesariamente un nivel posterior a la subtarea. La trazabilidad debe conectar cada trabajo con su propósito y puede variar según el proyecto y el plan.</li>')
        replace(a,'basada pura y exclusivamente','<p><strong>Trello</strong> organiza trabajo mediante tableros, listas y tarjetas. Podemos representar estados, registrar información y colaborar sobre cada tarjeta. Esta estructura permite implementar diferentes procesos; el tablero no define por sí solo Kanban ni impide trabajar con una cadencia de Sprint. Las políticas, límites y criterios de calidad se acuerdan entre las personas.</p>')
        replace(a,'Trello es especialmente adecuado','<p>Trello puede ser una opción para comenzar con un seguimiento visual sencillo. Si el equipo necesita jerarquías, reportes o automatizaciones, debe comprobar qué ofrece la configuración disponible, qué requiere una integración y cuánto trabajo de administración agrega. Jira ofrece alternativas más especializadas para seguimiento de software, pero elegirlo requiere justificar esa complejidad. La madurez del equipo no se mide por la marca de la herramienta ni exige utilizar Story Points.</p>')
        # La biblioteca es real, pero el título anterior inventaba un video específico.
        for link in a.xpath('.//a[@href="https://www.mountaingoatsoftware.com/videos"]'):
            link.set('href','https://learn.mountaingoatsoftware.com/agile/agile-estimation-estimating-with-story-points')
            link.text='Agile Estimating: How Teams Estimate with Story Points'
    p.write_bytes(etree.tostring(t,method='html',encoding='utf-8',doctype='<!doctype html>'))
print('Precisión técnica y transiciones ajustadas.')
