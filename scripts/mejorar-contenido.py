"""Edición pedagógica reproducible. Conserva una copia previa y no se aplica dos veces."""
from pathlib import Path
from lxml import html, etree
import re, shutil, json

BASE=Path(__file__).resolve().parents[1]
QA=BASE/'.qa/edicion-contenido'
QA.mkdir(parents=True,exist_ok=True)
LOG=[]

def text(e): return ' '.join(e.text_content().split())
def fragment(s): return html.fragment_fromstring(s)
def add_after(e,s):
    for n in reversed(html.fragments_fromstring(s)): e.addnext(n)
def para(a,key,s):
    found=[e for e in a.xpath('.//p|.//li') if key in text(e)]
    if len(found)!=1: raise ValueError(f'{key}: {len(found)} coincidencias')
    e=found[0]; new=fragment(s); e.getparent().replace(e,new)
    LOG.append(key)
    return new
def section(a,n):
    return next(e for e in a if e.tag=='h2' and re.match(rf'{n}\.',text(e)))
def before_section(a,n,s):
    e=section(a,n)
    for f in html.fragments_fromstring(s): e.addprevious(f)
def reorder(a,order):
    children=list(a); start=next(i for i,e in enumerate(children) if e.tag=='h2')
    groups={}; current=None; end=len(children)
    for i in range(start,len(children)):
        e=children[i]
        if e.tag=='h2':
            m=re.match(r'(\d+)\.',text(e))
            if not m: end=i; break
            current=int(m[1]); groups[current]=[]
        groups[current].append(e)
    for e in children[start:end]: a.remove(e)
    offset=start
    for new,old in enumerate(order,1):
        for e in groups[old]:
            for heading in [e]+list(e.xpath('.//h3|.//h4')):
                if heading.tag in ('h2','h3','h4') and heading.text:
                    heading.text=re.sub(rf'^{old}(?=\.)',str(new),heading.text)
            a.insert(offset,e); offset+=1

for module in range(1,6):
    folder=BASE/'entregables'/f'MODULO {module}'/'Contenido'
    path=folder/'contenido.html'
    tree=html.parse(str(path)); a=tree.xpath('//article')[0]
    if a.get('data-edicion')=='2026-09-15':
        LOG.append({'modulo':module,'estado':'Edición aplicada previamente; no se duplica'})
        continue
    original=[text(e) for e in a if e.tag=='h2']
    backup=QA/'antes'/f'MODULO {module}'; backup.mkdir(parents=True,exist_ok=True)
    for name in ('contenido.html','Contenido.docx'):
        if not (backup/name).exists(): shutil.copy2(folder/name,backup/name)

    if module==1:
        para(a,'Como ya ubicamos a Scrum', '<p>En el Módulo 2 vamos a estudiar Scrum en profundidad. Por ahora, reconocé tres responsabilidades de ese marco: <strong>Product Owner</strong>, orientado a maximizar el valor; <strong>Scrum Master</strong>, responsable de establecer Scrum y favorecer la efectividad; y <strong>Developers</strong>, quienes construyen un resultado utilizable y sostienen su calidad. No son cargos obligatorios en todo proyecto ágil. Developers reúne las habilidades necesarias para construir el producto, además de programación.</p>')
        para(a,'A diferencia de un puente o un edificio', '<p>La incertidumbre no pertenece exclusivamente al software: también puede aparecer en obras, servicios y proyectos científicos. En productos digitales suele ser importante porque construir una primera versión revela necesidades y comportamientos que no conocíamos. El problema de gestión es decidir qué podemos anticipar con confianza y qué debemos aprender mediante pruebas, sin suponer que una industria siempre trabaja de una sola manera.</p>')
        # Mantener las definiciones iniciales y enseñar los valores antes del catálogo de enfoques.
        reorder(a,[1,2,9,8,3,10,11,12,13,4,5,6,7,14,15])
        before_section(a,5,'<p class="bloque-narrativo"><strong>Del proyecto al aprendizaje.</strong> Ya sabemos qué buscamos, quién participa y qué restricciones existen. Ahora podemos preguntar cómo avanzar cuando todavía no conocemos toda la solución.</p>')
        e=section(a,5)
        add_after(e,'<div class="analogia"><p><strong>Analogía: un viaje con GPS.</strong> La agilidad se parece a elegir un destino, iniciar una ruta razonable y recalcular al encontrar un corte. Recalcular no cambia automáticamente el destino ni autoriza ignorar las reglas de tránsito. En un proyecto, el destino es el resultado buscado; la ruta es el plan; las observaciones del equipo y de los usuarios permiten ajustarlo. La comparación termina ahí: el valor de un producto no está definido tan claramente como una dirección. También debemos comprobar si el destino elegido resuelve una necesidad real.</p></div>')
        before_section(a,10,'<p class="bloque-narrativo"><strong>De los valores a las decisiones de trabajo.</strong> El Manifiesto orienta nuestras prioridades. Los enfoques y marcos ofrecen maneras de organizar el trabajo para ponerlas a prueba.</p>')
        # Reemplazar una transición desactualizada sin tocar los desarrollos.
        for e in a.xpath('.//p'):
            if 'manifiesto' in text(e).lower() and 'después' in text(e).lower() and 'alternativas' in text(e).lower():
                para(a,text(e)[:90],'<p>Primero vamos a comprender la agilidad, su origen y el Manifiesto. Después compararemos enfoques y veremos cómo organizar ciclos de aprendizaje y entrega. Así podremos elegir una forma de trabajo por su propósito y sus límites.</p>'); break

    if module==2:
        para(a,'si ya hay tres tareas en desarrollo', '<p>Un <strong>límite WIP</strong> establece cuántos ítems pueden permanecer iniciados en una etapa o en todo el sistema. Si Desarrollo admite tres y contiene tres, no ingresa una cuarta tarjeta. Si una pasa a Testing y quedan dos, el límite de Desarrollo permite incorporar otra; pero si Testing está saturado, la política del equipo puede priorizar ayudar a terminar antes de iniciar más. Son dos acuerdos relacionados: limitar la cantidad de trabajo y decidir cómo atender el cuello de botella. Mover una tarjeta bloqueada no la convierte en trabajo terminado.</p>')
        for e in a.xpath('.//p|.//li'):
            if 'exponencial' in text(e):
                s=etree.tostring(e,encoding='unicode'); s=re.sub(r'crece exponencialmente','puede aumentar al propagarse el defecto y ampliar su impacto',s); s=s.replace('aumenta exponencialmente','puede aumentar con el retrabajo y el impacto'); e.getparent().replace(e,fragment(s))
        para(a,'la única forma de generar conocimiento confiable', '<p>Scrum es un marco ligero para generar valor mediante soluciones adaptativas a problemas complejos. Cuando no podemos predecir con confianza cómo responderán los usuarios o cuál solución funcionará, necesitamos combinar conocimiento disponible con experimentos, observación y ajustes. No todo trabajo de software tiene el mismo nivel de incertidumbre: una rutina conocida puede convivir con una necesidad de negocio todavía desconocida. Scrum ayuda a gestionar esa incertidumbre; no elimina el análisis ni sustituye el conocimiento técnico.</p>')
        para(a,'en la inmensa mayoría de los casos', '<p>En un proceso definido, condiciones conocidas permiten anticipar resultados con suficiente confianza. En un proceso empírico, el plan se contrasta regularmente con resultados y se adapta al aprendizaje. Un producto digital puede combinar ambos: automatizar una operación conocida y experimentar con una experiencia de usuario nueva. Scrum se apoya en <strong>empirismo y pensamiento Lean</strong>; por eso conviene estudiar sus fundamentos antes de memorizar roles y reuniones.</p>')
        reorder(a,[1,2,6,3,4,5,7,8,9,10,11,12,13,14])
        add_after(section(a,4),'<div class="analogia"><p><strong>Analogía: una expedición compartida.</strong> El Product Owner ayuda a definir qué resultado merece alcanzarse y ordenar opciones; los Developers deciden cómo avanzar y producen un resultado utilizable; el Scrum Master ayuda a que la colaboración y el marco funcionen. Ninguno puede resolver solo todos los problemas. La analogía no crea una jerarquía de comandante y subordinados: Scrum reúne esas responsabilidades en un equipo autogestionado, y la seguridad y la calidad siguen siendo condiciones del trabajo.</p></div>')
        before_section(a,11,'<h3>10.3 Caso real: Toyota y la calidad dentro del proceso</h3><p>Toyota explica su sistema de producción a partir de dos pilares: <strong>jidoka</strong>, detener y atender anormalidades para evitar que los defectos continúen, y <strong>Just in Time</strong>, producir lo necesario, cuando se necesita y en la cantidad necesaria. También destaca la mejora cotidiana. Es un caso industrial real, no un equipo de software que utiliza Scrum. Fuente: <a href="https://global.toyota/en/company/vision-and-philosophy/production-system/">Toyota Production System</a>, consulta del 15 de septiembre de 2026.</p><p><strong>Aplicación razonada:</strong> si una prueba importante falla, seguir agregando funcionalidades puede ampliar el retrabajo. Investigar la falla antes de continuar traduce una preocupación por calidad en una decisión de trabajo. La transferencia es conceptual: las necesidades digitales pueden cambiar y el proceso de una fábrica no se copia literalmente a un equipo de producto.</p>')

    if module==3:
        para(a,'Toda iniciativa de producto exitosa', '<p>Una <strong>visión de producto</strong> expresa el futuro deseado para usuarios y negocio: por qué existe el producto y qué cambio busca producir. Ayuda a elegir entre alternativas, aunque no garantiza éxito. Si TurnoYa busca facilitar el acceso a turnos médicos, una decisión de diseño debería poder explicarse por su aporte a ese propósito, además de por su viabilidad. La visión se contrasta con la investigación y el aprendizaje del equipo.</p>')
        e=para(a,'reduciendo el ausentismo a turnos en un 15%', '<p>Un objetivo convierte la visión en un resultado observable. Para el semestre del piloto de TurnoYa proponemos que el 60 % de las reservas se realice por la aplicación y que el ausentismo disminuya un 15 % <strong>respecto de la tasa inicial</strong>. Son metas del escenario didáctico, no resultados obtenidos. Hay que definir el período, la población y cómo se medirá cada dato; un objetivo no demuestra que una funcionalidad causará esa mejora.</p>')
        add_after(e,'<div class="caso-resuelto"><p><strong>Ejemplo resuelto: porcentaje y puntos porcentuales.</strong> Suponé que inicialmente faltan 20 pacientes de cada 100: la tasa es 20 %. Reducirla un 15 % relativo significa calcular 20 % × 0,85 = <strong>17 %</strong>, una disminución de 3 puntos porcentuales. Bajar 15 puntos porcentuales sería llegar al 5 %, una meta muy diferente. Antes de priorizar recordatorios, acordamos la definición y verificamos qué otras causas influyen en el ausentismo.</p></div>')
        para(a,'Valiosa (Valuable):', '<li><strong>Valiosa (Valuable):</strong> explicá el beneficio para usuarios, negocio o sostenibilidad del producto. Una mejora técnica puede reducir riesgo, habilitar capacidad o proteger la confiabilidad. Puede ser un elemento propio del backlog; no es obligatorio esconderla dentro de una historia funcional ni inventar un usuario. Lo importante es hacer explícito su propósito y acordar cómo verificar el resultado.</li>')
        para(a,'para evitar dobles reservas y la valoración post-turno', '<p>En el roadmap de TurnoYa, <strong>Ahora</strong> incluye reservar y cancelar sobre una agenda confiable, evitando dobles reservas desde el piloto. <strong>Próximo</strong> puede incorporar sincronización automática con calendarios externos y valoración post-turno. <strong>Después</strong> mantiene telemedicina y pagos como opciones sujetas a investigación. Automatizar más integraciones puede esperar; la consistencia esencial de las reservas no puede omitirse. Los horizontes expresan dirección y aprendizaje, y se revisan con las clínicas sin convertir las iniciativas lejanas en promesas de fecha.</p>')
        para(a,'difuminando el concepto tradicional', '<p>Planificar un <strong>release</strong> significa decidir qué resultado se pondrá a disposición de usuarios, bajo qué condiciones y con qué pronóstico. Puede abarcar uno o varios Sprints, y una liberación no tiene que esperar a la Review. La <strong>entrega continua</strong> mantiene cambios listos para desplegar mediante un proceso confiable; todavía puede existir una decisión de liberación. En el <strong>despliegue continuo</strong>, los cambios que cumplen las verificaciones acordadas llegan automáticamente a producción. Son prácticas relacionadas, con distintos controles y niveles de automatización.</p>')
        add_after(section(a,3),'<div class="analogia"><p><strong>Analogía: preparar una comida y revisar la despensa.</strong> La visión explica para qué ocasión cocinamos; el backlog reúne opciones; el refinamiento permite entender ingredientes, trabajo y restricciones antes de elegir. Comprar todo lo imaginable no mejora la cena. La comparación ayuda a entender selección y preparación, pero un backlog no es una lista de compras cerrada: también contiene investigaciones, riesgos y necesidades que pueden cambiar al observar el producto.</p></div>')
        before_section(a,11,'<p class="bloque-narrativo"><strong>De describir pedidos a comprobar valor.</strong> Ya podemos escribir, preparar y ordenar trabajo. Ahora necesitamos decidir qué experimento mínimo y qué horizonte de entrega justifican invertir en esas opciones.</p>')

    if module==4:
        raw=etree.tostring(a,encoding='unicode')
        raw=raw.replace('10 h (reuniones) + 24 h (licencia)</td><td>46','7 h (reuniones) + 24 h (licencia)</td><td>49')
        raw=raw.replace('326','329').replace('277,1','279,65').replace('260-290','263-296')
        a_new=fragment(raw); a.getparent().replace(a,a_new); a=a_new
        para(a,'muy estable estadísticamente', '<p>El <strong>throughput</strong> se obtiene contando ítems terminados por período, sin exigir puntos ni estimación previa. Su estabilidad debe comprobarse con datos: tamaño, mezcla de trabajo, bloqueos y disponibilidad pueden modificarla. Si el promedio observado es ocho tarjetas semanales, 60/8 = 7,5 semanas ofrece una referencia inicial, no una fecha garantizada. Para comunicar un pronóstico necesitamos estudiar variación y condiciones futuras; contar tarjetas no mide por sí solo beneficio para usuarios.</p>')
        para(a,'de puntos comprometidos hasta cero', '<p>El burndown compara trabajo restante con una referencia descendente para el período. La línea uniforme es una simplificación visual, no una predicción estadística. Estar por encima pide revisar qué está ocurriendo: puede haber trabajo que termina en lotes, cambios de alcance o un bloqueo. Los puntos seleccionados son un pronóstico; el compromiso del Sprint Backlog es el Sprint Goal. Evaluamos el objetivo y la calidad, además del gráfico, antes de decidir.</p>')
        add_after(section(a,11),'<div class="analogia"><p><strong>Analogía: la espera en una cafetería.</strong> Desde que pedís hasta que recibís el café transcurre el Lead Time. Desde que el pedido entra al proceso de preparación hasta que se entrega transcurre el Cycle Time. Ese segundo intervalo incluye esperas internas: la máquina ocupada también cuenta. Medir cuánto tardó la persona en mover sus manos no equivale a medir el tiempo de flujo. En proyectos debemos acordar qué eventos representan solicitud, inicio y entrega; sin esas fronteras, comparar tiempos puede resultar engañoso.</p></div>')
        before_section(a,13,'<h3>12.1 Ejemplo resuelto: leer tiempos y salidas juntos</h3><p>Usamos días calendario transcurridos, sin contar ambos extremos. Los datos son didácticos y todos los ítems tienen la misma definición de terminado.</p><table><thead><tr><th>Ítem</th><th>Solicitud</th><th>Inicio</th><th>Entrega</th><th>Lead Time</th><th>Cycle Time</th></tr></thead><tbody><tr><td>A</td><td>Día 1</td><td>Día 2</td><td>Día 5</td><td>4 días</td><td>3 días</td></tr><tr><td>B</td><td>Día 1</td><td>Día 3</td><td>Día 7</td><td>6 días</td><td>4 días</td></tr><tr><td>C</td><td>Día 2</td><td>Día 4</td><td>Día 8</td><td>6 días</td><td>4 días</td></tr></tbody></table><p><strong>Cálculo:</strong> el Lead Time promedio es (4 + 6 + 6)/3 = 5,33 días; el Cycle Time promedio es (3 + 4 + 4)/3 = 3,67 días. La diferencia promedio, 1,67 días, corresponde a espera anterior al inicio. Entre los días 5 y 8 inclusive se entregan tres ítems: ese es el throughput de esa ventana, no una tasa semanal calculada con otro período.</p><p><strong>Lectura profesional:</strong> observamos espera previa y tiempos internos antes de proponer una intervención. Tres observaciones no permiten asegurar un plazo para todos los pedidos futuros. También investigamos si existen tickets muy antiguos todavía sin terminar, porque no aparecen en el promedio de finalizados.</p>')
        add_after(section(a,17),'<div class="criterio-profesional"><p><strong>Antes de elegir una herramienta:</strong> acordá estados, políticas de selección, criterios de terminado, límites WIP y eventos de medición. Un tablero en Trello no constituye por sí solo un sistema Kanban; Jira tampoco establece automáticamente Scrum. Las funcionalidades dependen de configuración y plan, y deben revisarse al momento de utilizarlas. Fuentes: <a href="https://trello.com/en/guide/trello-101">guía oficial de Trello</a> y <a href="https://www.atlassian.com/software/jira/features/reports">reportes oficiales de Jira</a>, consulta del 15 de septiembre de 2026.</p></div>')
        # El cálculo ya incluye reuniones únicamente en los días de presencia.
        before_section(a,6,'<p class="criterio-profesional"><strong>Lectura del cálculo de capacidad.</strong> Para C contamos siete días de presencia: 80 − 24 − 7 = 49 horas. Las cuatro personas restantes aportan 70 cada una, por lo que el total es 329. Reservar un 15 % deja 279,65 horas orientativas. Son supuestos del ejemplo; las reuniones reales y las habilidades disponibles deben revisarse antes de planificar.</p>')
        # Explicitar cambios de selección cuando el completado supera la cifra inicial.
        before_section(a,7,'<p><strong>Cómo leer la tabla de velocidad:</strong> la selección registrada al inicio puede renegociarse durante el Sprint con el Product Owner sin poner en peligro el objetivo. Por eso un período puede terminar más puntos que los seleccionados inicialmente. Registramos ese cambio de alcance y contamos únicamente trabajo terminado según la DoD.</p>')

    if module==5:
        para(a,'Bruce Tuckman', '<p>El modelo de <strong>Tuckman</strong> propone una lectura del desarrollo grupal mediante formación, conflicto, acuerdos y desempeño. Es una orientación para reconocer necesidades de colaboración, no una secuencia obligatoria que todos los equipos atraviesan de la misma manera. Pueden reaparecer tensiones al cambiar integrantes, objetivos o contexto. No necesitamos provocar conflictos para “avanzar de etapa”: necesitamos conversaciones seguras y acuerdos revisables.</p>')
        # Dos casos documentados y separación inequívoca de las simulaciones existentes.
        h=section(a,18); h.text='18. Casos reales, escenarios de transformación y desafíos de adopción'
        for e in list(a):
            if e.tag=='h3' and e.text and re.match(r'18\.[1-4] ',e.text):
                e.text=re.sub(r'18\.([1-4])',lambda m:f'18.{int(m[1])+2}',e.text,count=1)
        add_after(h,'<h3>18.1 Caso real: Sentinel y el FBI</h3><p><strong>Contexto documentado.</strong> En octubre de 2010, el FBI explicó que había identificado problemas de desempeño y costos en Sentinel y elegido desarrollo ágil para completar funciones pendientes, revisando requisitos y prioridades. La declaración es la posición de la organización ante una auditoría, no una evaluación independiente. Fuente: <a href="https://archives.fbi.gov/archives/news/pressrel/press-releases/mediaresponse_102010">respuesta del FBI sobre Sentinel, 20 de octubre de 2010</a>.</p><p><strong>Resultado documentado.</strong> El comunicado publicado el 31 de julio de 2012 informa que Sentinel se desplegó para todos los empleados el 1 de julio de ese año. Permitía gestionar registros y flujos de aprobación digitalmente, y la organización preveía continuar mejorándolo mediante comentarios de usuarios. Fuente: <a href="https://archives.fbi.gov/archives/news/pressrel/press-releases/fbi-announces-deployment-of-sentinel">anuncio oficial del despliegue de Sentinel</a>.</p><p><strong>Análisis para la materia.</strong> El resultado observable es un despliegue organizacional de un sistema relevante. Las fuentes no permiten atribuirlo exclusivamente a Scrum ni concluir que la agilidad garantiza ahorro. El caso permite discutir priorización de funciones, evidencia de producto utilizable y continuidad del aprendizaje en un entorno con supervisión formal.</p><h3>18.2 Caso real: colaboración de liderazgo en ING</h3><p>El informe de experiencia <em>The Power of Three</em>, publicado por Agile Alliance, relata el trabajo de un Agile Coach con Product Owners y Chapter Leads de cuatro squads de ING, en Países Bajos, entre 2015 y 2017. Describe tensiones entre entrega a corto plazo y desarrollo de capacidades técnicas a más largo plazo, y reuniones para hacerlas explícitas y construir un enfoque compartido. Fuente: <a href="https://agilealliance.org/resources/experience-reports/the-power-of-three-the-journey-of-an-agile-leadership-team/">informe de experiencia sobre el equipo de liderazgo de ING</a>.</p><p><strong>Lectura profesional.</strong> Es un testimonio situado, no una prueba de que copiar squads mejorará cualquier organización. Sirve para reconocer un desafío: los responsables pueden perseguir objetivos legítimos que compiten por el mismo tiempo. Antes de cambiar títulos, acordamos cómo se conversan prioridades, capacidades y consecuencias. Chapter Lead y Agile Coach pertenecen a esa organización; no son responsabilidades obligatorias de Scrum.</p><p><strong>Los tres casos que siguen son escenarios didácticos.</strong> Sus organizaciones y resultados se usan para practicar análisis; no constituyen datos comprobados de empresas reales.</p>')
        add_after(section(a,11),'<div class="analogia"><p><strong>Analogía: revisar una receta después de cocinar.</strong> En la Review conversamos con quienes probaron el plato: si resuelve la ocasión, qué necesitan y qué conviene ofrecer después. En la Retrospective observamos cómo trabajó la cocina: esperas, coordinación, herramientas y calidad. Las conversaciones pueden relacionarse, pero sus propósitos son distintos. En un equipo, la retrospectiva produce una mejora concreta con seguimiento; no se limita a opinar si la experiencia fue agradable.</p></div>')
        before_section(a,12,'<h3>11.4 Ejemplo resuelto: transformar una queja en experimento</h3><p>En TurnoYa se repite “las revisiones tardan demasiado”. El equipo observa cinco cambios terminados: sus esperas de revisión fueron 1, 2, 2, 3 y 7 días, con mediana de 2. Decide probar durante un Sprint una política: cada día alguien revisa las solicitudes abiertas y se evita acumular cambios muy grandes. Se define quién registra las fechas y se compara espera, defectos y carga de trabajo al finalizar. Si la espera baja pero aumentan errores, la intervención debe revisarse. Una muestra pequeña y un solo Sprint no demuestran causalidad; sí permiten aprender y decidir el siguiente ajuste.</p>')
        before_section(a,18,'<p class="bloque-narrativo"><strong>De los acuerdos de equipo a la evidencia de adopción.</strong> Los casos permiten contrastar fundamentos, marcos, planificación y seguimiento con decisiones organizacionales. Buscamos qué se hizo, qué resultado está documentado y qué no podemos concluir.</p>')

    # Índice sincronizado, enlaces internos estables y cierre narrativo.
    nav=tree.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," chapter-map ")]//ol')
    if nav:
        nav=nav[0]; nav.clear()
        for i,e in enumerate(a.xpath('./h2'),1):
            e.set('id',f'seccion-{i}')
            li=etree.SubElement(nav,'li'); link=etree.SubElement(li,'a',href=f'#seccion-{i}')
            link.text=re.sub(r'^\d+\.\s*','',text(e))
    a.set('data-edicion','2026-09-15')
    last=a.xpath('./h2')[-1]
    assert 'Síntesis' in text(last)
    closes={1:'En el próximo módulo pasamos de los criterios de agilidad a sus formas de trabajo: primero fundamentos de Scrum, luego responsabilidades, artefactos y eventos, y después Kanban y Lean para comparar decisiones con contexto.',2:'Conocemos qué problema busca resolver cada marco y cómo colaboran sus participantes. En el Módulo 3 vamos a convertir necesidades en objetivos, opciones de backlog y experimentos de producto, sin confundir una práctica opcional con una regla de Scrum.',3:'Ahora tenemos una dirección, criterios de valor y trabajo preparado. El Módulo 4 incorpora disponibilidad, estimación y métricas para contrastar el plan con evidencia y comunicar pronósticos condicionados.',4:'Las métricas hacen visibles resultados y esperas; las personas convierten esa información en decisiones. En el Módulo 5 veremos cómo colaborar, liderar y sostener mejoras, y contrastaremos la materia con casos documentados.',5:'El recorrido conecta propósito, fundamentos, marcos, planificación, seguimiento y colaboración. Los casos reales y los escenarios didácticos permiten practicar una lectura crítica: explicitar contexto, decisiones, evidencia y límites antes de recomendar una forma de trabajo.'}
    a.append(fragment(f'<p class="cierre-narrativo"><strong>Conexión del recorrido.</strong> {closes[module]}</p>'))
    path.write_bytes(etree.tostring(tree,method='html',encoding='utf-8',doctype='<!doctype html>'))
    LOG.append({'modulo':module,'secciones_originales':original,'secciones_actuales':[text(e) for e in a.xpath('./h2')],'palabras':len(text(a).split())})

(QA/'cambios-editoriales.json').write_text(json.dumps(LOG,ensure_ascii=False,indent=2),encoding='utf-8')
print('Fuentes mejoradas: cinco módulos. Copias previas y registro en',QA)
