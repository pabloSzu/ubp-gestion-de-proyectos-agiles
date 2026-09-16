"""Edición puntual autorizada por Pablo. No ejecutarla sobre futuras ediciones."""
from pathlib import Path
from lxml import html, etree
import re, shutil, json

BASE=Path(__file__).resolve().parents[1]
folder=BASE/'entregables/MODULO 1/Contenido'
qa=BASE/'.qa/revision-pedagogica-ia'
qa.mkdir(parents=True,exist_ok=True)
path=folder/'contenido.html'
tree=html.parse(str(path)); article=tree.xpath('//article')[0]
if article.get('data-revision-ia'):
    raise SystemExit('La revisión ya fue aplicada; revisar manualmente antes de modificar.')
for name in ('contenido.html','Contenido.docx'):
    shutil.copy2(folder/name,qa/name)
before=article.text_content()

def fragments(text): return html.fragments_fromstring(text)
def section(n):
    h=article.xpath(f'./h2[@id="seccion-{n}"]')[0]; out=[]
    for e in list(article)[list(article).index(h)+1:]:
        if e.tag=='h2': break
        out.append(e)
    return h,out
def replace(n,text,keep_figures=True):
    h,old=section(n); index=list(article).index(h)+1
    figures=[e for e in old if e.tag=='figure'] if keep_figures else []
    for e in old: article.remove(e)
    for e in fragments(text)+figures: article.insert(index,e); index+=1
def append(n,text):
    h,old=section(n); index=list(article).index(old[-1])+1 if old else list(article).index(h)+1
    for e in fragments(text): article.insert(index,e); index+=1
def change_containing(needle,text):
    found=article.xpath('.//p[contains(string(),"'+needle+'")]|.//li[contains(string(),"'+needle+'")]')
    found=[e for e in found if not e.xpath('.//p[contains(string(),"'+needle+'")]')]
    if len(found)!=1: raise ValueError((needle,len(found)))
    e=found[0]; new=fragments(text)[0]; e.getparent().replace(e,new)

# Apertura: un problema comprensible antes de nombres especializados.
for e in list(article):
    if e.tag=='h2': break
    article.remove(e)
opener='''
<p>Imaginá que una universidad te pide un asistente con inteligencia artificial para responder consultas sobre horarios y trámites. La primera idea parece sencilla: cargar información y abrir un chat. Al probarlo descubrís que algunas preguntas son ambiguas, que ciertos documentos están desactualizados y que una respuesta convincente puede ser incorrecta. ¿Cómo organizás el trabajo para aprender esto a tiempo y entregar algo útil?</p>
<p>En esta materia vas a aprender a <strong>gestionar proyectos de forma ágil</strong>: avanzar con un plan, comprobar resultados y ajustar decisiones a partir de lo que aprendés. El caso del asistente universitario es un <strong>escenario didáctico</strong>. No necesitás saber entrenar modelos ni conocer ninguna herramienta para seguirlo.</p>
<h3>Cómo recorrer este módulo</h3>
<ol><li>Comprender qué gestionamos: proyecto, producto, personas y restricciones.</li><li>Entender qué significa trabajar de forma ágil y por qué surgió esa idea.</li><li>Interpretar los valores y principios del Manifiesto con ejemplos.</li><li>Distinguir las formas de organizar, aprender y entregar el trabajo.</li><li>Elegir un enfoque y justificarlo con evidencia en un proyecto de IA.</li></ol>
<p>Los nombres de los marcos aparecerán en el panorama de la sección 10. Sus roles, reuniones y reglas se explican en el <strong>Módulo 2</strong>, después de comprender para qué sirven. Aquí nos concentramos en los fundamentos.</p>'''
for i,e in enumerate(fragments(opener)): article.insert(i,e)

replace(1,'''<p>¿Crear un asistente y atender consultas todos los días son el mismo trabajo? Para organizarlos bien necesitamos distinguir el esfuerzo de construir una solución de su funcionamiento cotidiano.</p>
<p>Un <strong>proyecto</strong> es un esfuerzo temporal para crear un producto, servicio o resultado único. Tiene un inicio y un cierre. Temporal no significa breve: puede durar semanas o años. Único tampoco significa que nadie haya hecho algo parecido; significa que el resultado responde a condiciones y necesidades particulares.</p>
<div class="analogia"><p><strong>Analogía de una mudanza.</strong> Mudarte tiene un objetivo, un inicio y un final: dejarte instalado en la nueva vivienda. Empacar, contratar transporte y coordinar horarios son actividades del proyecto. Vivir después en esa casa es otra cosa. En tecnología, construir y poner a prueba el asistente es el proyecto; atender consultas una vez disponible pertenece a su funcionamiento.</p></div>
<h3>1.1 Un proyecto necesita límites</h3>
<p>En nuestro caso, un primer proyecto podría ser preparar y evaluar un asistente para consultas sobre inscripciones en seis semanas. Necesitamos acordar qué información utilizará, quién revisará las respuestas, cuánto podemos gastar y cómo reconoceremos un resultado aceptable. La fecha y el alcance son supuestos del ejemplo, no una receta para todos los proyectos de IA.</p>
<h3>1.2 Qué significa gestionar</h3>
<p>La <strong>gestión de proyectos</strong> coordina conocimientos, personas, recursos y decisiones para alcanzar el objetivo. Incluye planificar, gestionar riesgos, comunicar avances y revisar resultados. No alcanza con repartir tareas: podemos completar muchas actividades y aun así entregar una solución que no sirve.</p>
<p>Por ejemplo, “cargar veinte documentos” describe trabajo realizado. “Responder correctamente consultas de inscripción con información vigente” expresa una capacidad que necesitamos comprobar. El tablero ayuda a organizar el trabajo; las pruebas permiten saber si conseguimos el resultado.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Antes de elegir una herramienta, explicá qué problema querés resolver, para quién y cómo vas a reconocer que está resuelto.</p></div>''')

# No anticipar responsabilidades de Scrum antes de enseñar el marco.
replace(3,'''<p>El equipo construye un asistente que responde con claridad, pero la oficina de alumnos descubre que cita una fecha del año anterior. ¿Quién tenía que revisar la información? La calidad del resultado depende de reconocer a las personas involucradas y acordar cómo participan.</p>
<p>Un <strong>stakeholder</strong>, o parte interesada, es una persona, grupo u organización que puede afectar al proyecto o verse afectado por él. Un <strong>rol</strong> es una función con responsabilidades. Una misma persona puede ser parte interesada y desempeñar un rol.</p>
<h3>3.1 Personas que necesitamos reconocer</h3>
<table><caption>Participantes del asistente universitario</caption><thead><tr><th>Participante</th><th>Qué aporta o necesita</th><th>Ejemplo de participación</th></tr></thead><tbody>
<tr><td>Patrocinador o sponsor</td><td>Respaldo, recursos y decisiones dentro de su autoridad.</td><td>Autorizar el piloto y su presupuesto.</td></tr>
<tr><td>Cliente</td><td>La necesidad por la que encarga la solución.</td><td>La universidad solicita mejorar la atención.</td></tr>
<tr><td>Usuarios</td><td>Experiencia directa de uso.</td><td>Estudiantes prueban si entienden las respuestas.</td></tr>
<tr><td>Equipo que construye</td><td>Habilidades técnicas y de diseño.</td><td>Preparar datos, integrar el sistema y verificarlo.</td></tr>
<tr><td>Especialistas del dominio</td><td>Conocimiento del problema y sus reglas.</td><td>La oficina de alumnos valida fechas y trámites.</td></tr>
<tr><td>Operaciones y seguridad</td><td>Continuidad del servicio y controles necesarios.</td><td>Revisar acceso a información y respuesta a incidentes.</td></tr>
</tbody></table>
<p>El cliente y el usuario pueden ser personas diferentes: la universidad encarga el asistente, mientras los estudiantes lo utilizan. Tampoco alcanza con escuchar a quien paga. Quienes usan, mantienen o resultan afectados por el sistema aportan información que puede cambiar decisiones importantes.</p>
<h3>3.2 Especialidad y responsabilidad son distintas</h3>
<p>Programación, ciencia de datos, diseño y pruebas son especialidades. Decidir prioridades o aprobar un piloto son responsabilidades. Ser especialista en modelos no te convierte automáticamente en quien decide qué problema debe atenderse primero.</p>
<div class="analogia"><p><strong>Analogía de una producción audiovisual.</strong> Saber operar la cámara no equivale a decidir qué historia se quiere contar. Ambas funciones se necesitan y deben coordinarse. En un proyecto de IA, quien conoce los modelos y quien conoce las necesidades de los usuarios tienen que conversar para construir una solución útil.</p></div>
<p>Algunas organizaciones designan a una persona para coordinar la gestión del proyecto. Su autoridad depende de los acuerdos establecidos. Los marcos de trabajo que estudiaremos después pueden distribuir responsabilidades de otra manera; todavía no necesitamos sus nombres para entender quién aporta, quién decide y quién realiza el trabajo.</p>
<h3>3.3 Comunicar y acordar quién decide</h3>
<p>La matriz de <strong>poder e interés</strong> ayuda a pensar qué participación necesita cada parte interesada. Quien puede autorizar recursos y está involucrado requiere una comunicación cercana; un usuario necesita canales para aportar experiencia. La matriz orienta la atención, pero no justifica ignorar a personas con poca autoridad que pueden sufrir las consecuencias de una decisión.</p>
<p>La <strong>matriz RACI</strong> permite aclarar la participación en una actividad: R realiza el trabajo; A responde por el resultado y tiene la autoridad acordada; C aporta conocimiento antes de decidir; I recibe información. Es una herramienta opcional, no una exigencia de toda gestión ágil.</p>
<p>Para revisar los documentos del asistente, una persona del equipo prepara el material (R), la persona autorizada de la oficina de alumnos responde por su vigencia (A), otras áreas aportan aclaraciones (C) y soporte conoce la versión aprobada (I). La letra A no significa que esa persona deba imponer cada decisión técnica.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Para cada decisión importante, identificá quién conoce el problema, quién puede decidir, quién realiza el trabajo y quién necesita conocer el resultado.</p></div>''')

replace(6,'''<p>¿Por qué empezó a cuestionarse la idea de definirlo todo al principio? En software, construir y probar una solución suele revelar necesidades que los documentos iniciales no habían previsto. Si esa información llega al final, corregir puede exigir rehacer mucho trabajo.</p>
<p>Durante los años noventa, distintos equipos y profesionales desarrollaron formas de trabajar con colaboración cercana, entregas frecuentes y aprendizaje. No surgió una única receta: había propuestas con énfasis diferentes en organización, calidad técnica y adaptación.</p>
<p>En febrero de <strong>2001</strong>, diecisiete profesionales se reunieron en <strong>Snowbird, Utah</strong>, y formularon el Manifiesto por el Desarrollo Ágil de Software. El encuentro puso en común experiencias previas; no inventó de cero la colaboración ni las entregas parciales.</p>
<p>Para este módulo importa comprender el problema que intentaban resolver: obtener evidencia y responder a ella durante el desarrollo. Los nombres y mecanismos de sus propuestas se estudian después. La <a href="https://agilemanifesto.org/history.html">historia oficial del Manifiesto</a> permite ampliar este contexto.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Una práctica resulta útil por el problema que ayuda a resolver. Comprender su propósito permite adaptarla con criterio.</p></div>''')

replace(7,'''<p>Si el equipo completó cien páginas de documentación, pero el asistente responde con información incorrecta, ¿podemos decir que avanzó lo suficiente? El Manifiesto nos ayuda a pensar qué debemos priorizar cuando distintas actividades compiten por tiempo y atención.</p>
<p>El <strong>Manifiesto Ágil</strong> expresa cuatro valores. No define una herramienta ni prescribe reuniones o roles. Plantea prioridades: procesos, documentación, contratos y planes siguen siendo útiles; su cumplimiento no debe reemplazar la colaboración ni la comprobación del resultado.</p>
<table><caption>Lectura de los cuatro valores aplicada al asistente</caption><thead><tr><th>Qué se prioriza</th><th>Qué se conserva como apoyo</th><th>Ejemplo</th></tr></thead><tbody>
<tr><td>Las personas y sus interacciones.</td><td>Procesos y herramientas.</td><td>Conversar con la oficina de alumnos para resolver una fecha ambigua.</td></tr>
<tr><td>Una solución de software que funciona.</td><td>Documentación suficiente y útil.</td><td>Evaluar respuestas con consultas de prueba y registrar fuentes y resultados.</td></tr>
<tr><td>Colaboración con el cliente.</td><td>Acuerdos contractuales.</td><td>Revisar el piloto con la universidad y negociar cambios explícitamente.</td></tr>
<tr><td>Adaptación a nueva información.</td><td>Planificación.</td><td>Corregir documentos desactualizados antes de agregar más temas.</td></tr>
</tbody></table>
<h3>7.1 Personas y colaboración</h3>
<p>Cuando aparece una duda, necesitamos a las personas capaces de resolverla. Un formulario o un tablero pueden registrar el problema, pero no conocen por sí mismos cuál es la fecha correcta de inscripción. La conversación aclara el significado; registrar la decisión evita que se pierda.</p>
<h3>7.2 Resultado y documentación</h3>
<p>El asistente debe permitir realizar la tarea prevista con calidad suficiente. Una demostración vistosa no acredita que las respuestas sean confiables. La documentación de fuentes, limitaciones y pruebas también aporta valor porque permite revisar y mantener el sistema.</p>
<h3>7.3 Colaboración y acuerdos</h3>
<p>Colaborar significa revisar necesidades y resultados con el cliente durante el trabajo. Los acuerdos siguen fijando responsabilidades, recursos y límites. Si cambia el alcance, se analiza el impacto y se acuerda cómo continuar.</p>
<h3>7.4 Adaptación y planificación</h3>
<p>El plan es una hipótesis de cómo alcanzar el objetivo con lo que sabemos hoy. Si las pruebas muestran un error importante, revisamos prioridades. Cambiar el plan requiere una razón y una decisión; aceptar cualquier pedido de inmediato produciría desorden.</p>
<div class="analogia"><p><strong>Analogía de aprender a cocinar.</strong> La receta orienta, pero necesitás comprobar la cocción antes de servir. Si el resultado todavía no está listo, completar los pasos escritos no lo vuelve adecuado. En un proyecto, el plan guía y las pruebas aportan información para decidir. La analogía no sustituye las evaluaciones técnicas ni las obligaciones del producto.</p></div>
<div class="mito"><p><strong>Mito.</strong> Trabajar de forma ágil significa prescindir de documentación y planes. <strong>Realidad.</strong> Necesitamos los que ayuden a coordinar, verificar y mantener el resultado; también necesitamos revisar lo que hacemos cuando la evidencia contradice el plan.</p></div>
<p>Podés consultar la <a href="https://agilemanifesto.org/iso/es/manifesto.html">redacción original de los cuatro valores</a>. La tabla presenta una explicación aplicada, no una transcripción.</p>''')

# Principios completos, con títulos breves y explicación normal: evitar colorear líneas enteras.
replace(8,'''<p>Los valores orientan decisiones. Los <strong>doce principios</strong> desarrollan cómo llevar esa orientación al trabajo. Para estudiarlos, los agrupamos por preguntas; la agrupación es didáctica y conserva la numeración original.</p>
<h3>8.1 Cómo entregar y aprender</h3><ol>
<li><strong>1. Valor temprano.</strong> Entregar capacidades útiles pronto y continuar mejorándolas. En el asistente, empezar por consultas de inscripción bien verificadas puede ayudar antes que abarcar todos los trámites sin comprobarlos.</li>
<li><strong>2. Aceptar cambios.</strong> Aprovechar información nueva, incluso avanzada la construcción. Si cambió una fecha, revisar los documentos importa más que conservar una respuesta ya implementada. Primero evaluamos el impacto.</li>
<li><strong>3. Entregas frecuentes.</strong> Reducir la espera para comprobar software que funciona. En nuestro ejemplo, preparar revisiones periódicas permite descubrir errores antes de ampliar el piloto. La frecuencia depende del contexto.</li>
<li><strong>7. Progreso verificable.</strong> Observar software funcionando como evidencia principal del avance del desarrollo. En IA, comprobar el funcionamiento incluye evaluar respuestas y limitaciones; que el chat se abra no es suficiente.</li></ol>
<h3>8.2 Cómo colaborar</h3><ol>
<li><strong>4. Negocio y construcción juntos.</strong> Quienes conocen los trámites y quienes implementan el asistente colaboran de forma cotidiana. Separarlos hasta la entrega aumenta el riesgo de entender mal las reglas.</li>
<li><strong>5. Apoyo y confianza.</strong> Dar a las personas motivadas el entorno y los recursos que necesitan. Pedir evaluación de respuestas sin acceso a documentos vigentes impide hacer bien el trabajo.</li>
<li><strong>6. Comunicación directa.</strong> La conversación cara a cara es el medio que el texto original prioriza para comunicar información. Una videollamada puede ayudar a aclarar una duda en un equipo remoto; los registros escritos siguen siendo necesarios para compartir acuerdos y trabajar de manera asincrónica.</li>
<li><strong>11. Autoorganización.</strong> Permitir que el equipo aporte su conocimiento para construir requisitos, arquitectura y diseño. La autonomía se ejerce dentro de objetivos, límites y responsabilidades acordadas.</li></ol>
<h3>8.3 Cómo sostener y mejorar el trabajo</h3><ol>
<li><strong>8. Ritmo sostenible.</strong> Mantener una forma de trabajo que pueda sostenerse. Extender jornadas de manera permanente puede deteriorar la revisión y ocultar problemas de organización.</li>
<li><strong>9. Excelencia técnica.</strong> Cuidar diseño y calidad para poder cambiar con confianza. En el asistente, registrar versiones de documentos y repetir pruebas ayuda a reconocer qué modificación provocó un error.</li>
<li><strong>10. Simplicidad.</strong> Evitar trabajo que no contribuye al objetivo. Si un buscador de preguntas frecuentes resuelve la necesidad, sumar un agente complejo necesita una justificación.</li>
<li><strong>12. Reflexión y mejora.</strong> Revisar periódicamente cómo trabajamos y ajustar el proceso. Si la validación de documentos demora las entregas, acordar revisiones más pequeñas puede ser un experimento de mejora.</li></ol>
<p>Estas explicaciones son paráfrasis y ejemplos. La <a href="https://agilemanifesto.org/iso/es/principles.html">redacción original de los doce principios</a> permite reconocer su contexto de desarrollo de software.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Evaluá los principios en comportamientos observables: qué se entrega, cómo se aprende, cómo se colabora y cómo se cuida la calidad.</p></div>''')

replace(9,'''<p>El asistente genera respuestas más largas y usa un modelo más grande. ¿Eso significa que es más útil? Solo podemos responder si sabemos qué problema queríamos resolver y qué cambió para las personas que lo utilizan.</p>
<p>El <strong>valor</strong> es el beneficio que una solución aporta a sus usuarios o a la organización. No equivale a la cantidad de funcionalidades ni al tamaño del modelo. En nuestro caso puede ser que los estudiantes encuentren información vigente y sepan cuándo consultar a una persona.</p>
<h3>9.1 Actividad, capacidad y beneficio</h3>
<table><caption>Tres formas de describir el avance</caption><thead><tr><th>Nivel</th><th>Ejemplo</th><th>Qué falta comprobar</th></tr></thead><tbody>
<tr><td>Actividad</td><td>Cargar documentos.</td><td>Si son correctos y están vigentes.</td></tr>
<tr><td>Capacidad entregada</td><td>Responder consultas con referencia al documento utilizado.</td><td>Si las respuestas permiten resolver la consulta.</td></tr>
<tr><td>Beneficio</td><td>Estudiantes encuentran la respuesta correcta con menos dificultad.</td><td>Si ocurre en condiciones reales y para distintos grupos.</td></tr></tbody></table>
<p>Antes de construir, expresamos una <strong>hipótesis de valor</strong>: “si ofrecemos respuestas verificadas sobre inscripción, los estudiantes podrán resolver esas consultas con menos dificultad”. Elegimos señales para evaluarla, como corrección de respuestas, tiempo para resolver la tarea y necesidad de asistencia. Los resultados de un conjunto pequeño de pruebas no garantizan el comportamiento de todos los usuarios.</p>
<p>Priorizar implica comparar beneficio esperado, esfuerzo, riesgo y dependencias. Podemos apoyarnos en análisis costo-beneficio o en categorías de prioridad. En el Módulo 3 estudiaremos estas técnicas con detalle; aquí importa entender por qué algunas necesidades deben atenderse antes que otras.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Antes de proponer una funcionalidad, escribí para quién sería útil, qué mejoraría y con qué evidencia evaluarías esa mejora.</p></div>
<p class="bloque-narrativo">Ya tenemos criterios para juzgar las decisiones. Ahora podemos conocer las formas de organizar el trabajo sin confundirlas con herramientas.</p>''')

replace(11,'''<p>¿El trabajo empieza cuando programamos o cuando reconocemos el problema? El <strong>ciclo de vida</strong> abarca el recorrido del proyecto desde su inicio hasta su cierre. Sus fases dependen del contexto: explorar, construir y poner en funcionamiento es una organización posible.</p>
<p>Para gestionar ese recorrido necesitamos iniciar, planificar, ejecutar, monitorear y controlar, y cerrar. Son <strong>funciones de gestión</strong> que pueden repetirse y superponerse; no cinco etapas obligatorias que se realizan una sola vez.</p>
<h3>11.1 Inicio</h3><p>Reconocemos la necesidad, el resultado buscado, las personas involucradas y las primeras restricciones. En el asistente, acordamos qué consultas abordar y quién puede autorizar el piloto. Un acta de constitución, también llamada project charter, puede registrar la autorización y los acuerdos de alto nivel.</p>
<h3>11.2 Planificación</h3><p>Decidimos cómo avanzar, qué recursos necesitamos y qué riesgos debemos investigar. Una estructura de descomposición del trabajo (EDT o WBS) divide el trabajo en partes para facilitar su planificación. Según el contexto, utilizamos esa u otras formas de organizarlo. Para el piloto planificamos preparar documentos, construir una primera capacidad y evaluar respuestas; revisamos el detalle a medida que aprendemos.</p>
<h3>11.3 Ejecución</h3><p>Realizamos el trabajo previsto. En un proyecto de IA incluye preparar datos, integrar componentes, diseñar la interacción y efectuar pruebas. Entrenar o elegir un modelo es solo una parte del sistema.</p>
<h3>11.4 Monitoreo y control</h3><p>Comparamos resultados con objetivos, reconocemos problemas y decidimos ajustes. Si la respuesta usa un documento obsoleto, investigamos la causa y revisamos el trabajo. Seguimos tiempo y recursos, pero también calidad y utilidad. Un porcentaje de tareas completadas no basta para describir la confiabilidad del asistente.</p>
<h3>11.5 Cierre</h3><p>Acordamos la aceptación del resultado, registramos aprendizajes y dejamos claras las responsabilidades siguientes. Puede terminar el proyecto piloto mientras el producto sigue evolucionando y operaciones atiende incidentes. Cerrar una entrega tampoco significa necesariamente cerrar todo el proyecto.</p>
<div class="analogia"><p><strong>Analogía de organizar una expedición.</strong> Necesitás acordar el destino, preparar recursos, avanzar y comprobar las condiciones. Si una ruta deja de ser segura, revisás el plan durante el viaje. Llegar también exige verificar el resultado y ordenar el regreso. Las funciones se conectan; no son compartimentos sin comunicación.</p></div>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Volver a planificar cuando aparece evidencia relevante es una forma de control responsable.</p></div>''')

# Mantener la explicación de cascada, retirar la digresión estadística no necesaria para principiantes.
h,old=section(12)
for e in list(old):
    if e.tag=='h3' and 'CHAOS' in e.text_content():
        idx=old.index(e)
        for x in old[idx:]:
            if x.tag=='div' and 'criterio-profesional' in x.get('class',''): continue
            article.remove(x)
        break
change_containing('El origen formal de este modelo', '<p>El artículo de Winston Royce de 1970 sobre grandes sistemas de software suele citarse al discutir este modelo. Su propuesta también advertía riesgos del desarrollo puramente secuencial y planteaba revisiones. Por eso debemos evaluar cómo trabaja un proyecto concreto, en lugar de suponer que todas las organizaciones aplican una cascada idéntica.</p>')
change_containing('Los informes CHAOS documentaron', '<p>Cuando la solución contiene mucha incertidumbre, esperar hasta el final para comprobarla puede hacer costosa la corrección. En el asistente, decidir todas las respuestas antes de probar consultas reales podría ocultar documentos contradictorios o necesidades mal comprendidas. Necesitamos obtener esa información antes de ampliar la construcción.</p>')

replace(14,'''<p>Durante el piloto, los estudiantes piden que el asistente inscriba automáticamente a una materia. ¿Alcanza con agregar esa tarea? El pedido transforma una solución que informa en otra que actúa sobre un trámite; cambia el riesgo y requiere revisar permisos, validación y alcance.</p>
<p>La <strong>gestión del cambio</strong> permite registrar una necesidad nueva, analizar sus consecuencias y decidir qué hacer. En una gestión predictiva se evalúa cómo afecta a las referencias acordadas de alcance, tiempo y costo. El procedimiento de aprobación depende de la organización y de la importancia de la decisión.</p>
<p>En una gestión adaptativa revisamos las necesidades con frecuencia y ajustamos prioridades según evidencia. Eso no elimina acuerdos contractuales, controles de seguridad ni decisiones de autorización. Aceptar un cambio tampoco significa comenzarlo de inmediato.</p>
<h3>14.1 Una secuencia para decidir</h3><ol>
<li>Comprender qué problema resuelve el pedido y para quién.</li>
<li>Identificar impacto, riesgos, dependencias y controles necesarios.</li>
<li>Comparar el pedido con el trabajo pendiente y la capacidad disponible.</li>
<li>Acordar si se incorpora, se investiga, se posterga o se rechaza.</li>
<li>Registrar la decisión y comprobar después si produce el beneficio esperado.</li></ol>
<p>La <strong>expansión descontrolada del alcance</strong>, o scope creep, aparece cuando se incorpora trabajo sin revisar los acuerdos y sus efectos. La alternativa ágil requiere hacer visible la decisión. Para nuestro piloto podemos investigar la inscripción automática y continuar ofreciendo información validada; todavía no prometemos una función cuya viabilidad no comprobamos.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Ante un pedido nuevo, explicá qué cambia, qué trabajo se desplazaría y quién tiene autoridad para acordarlo.</p></div>''')

# Reducir anticipaciones en los desarrollos válidos conservados.
change_containing('Scrum, Kanban y XP aportan mecanismos', '<p>La expresión <strong>metodologías ágiles</strong> agrupa distintas maneras de organizar ese trabajo. No existe una única receta llamada Agile ni una lista universal de reuniones o roles. En la sección 10 vamos a conocer el mapa de alternativas.</p>')
for e in article.xpath('.//td'):
    if e.text_content().startswith('Puede fijarse la duración del ciclo, como en Scrum'):
        e.text='Puede acordarse un ciclo de trabajo breve; eso no fija por sí solo la fecha final del producto.'
    if e.text_content()=='Planificación detallada al inicio, ejecución secuencial':
        e.text='Establecer referencias de alcance, tiempo y recursos con información confiable; no obliga a una ejecución secuencial.'
change_containing('Scrum es el ejemplo paradigmático', '<p>Podemos <strong>iterar e incrementar</strong> al mismo tiempo. El asistente mejora sus respuestas de inscripción después de las pruebas (iteración) y luego agrega consultas sobre becas verificadas (incremento). La combinación permite aprender sobre lo construido y ampliar la capacidad del producto. Un experimento que no produce una mejora todavía puede aportar aprendizaje; no lo confundimos con una entrega utilizable.</p>')
change_containing('Los marcos de escalado, como SAFe', '<p>Un <strong>enfoque híbrido</strong> combina formas de gestión cuando diferentes partes del trabajo lo justifican. En el asistente, podemos planificar anticipadamente la revisión de permisos y trabajar en ciclos de prueba sobre las respuestas. La combinación necesita acuerdos claros. Planificar a largo plazo no convierte automáticamente un trabajo ágil en híbrido.</p>')
change_containing('Cynefin, desarrollado', '<p>El marco <strong>Cynefin</strong> ayuda a pensar el contexto de una decisión. Cuando conocemos relaciones causa-efecto podemos aplicar prácticas establecidas; cuando el problema exige experiencia técnica necesitamos análisis; cuando el resultado depende de interacciones difíciles de anticipar necesitamos experimentar de manera acotada; ante una crisis primero debemos estabilizar. No selecciona automáticamente una metodología. En el asistente, configurar un permiso conocido y explorar si una respuesta ayuda al estudiante son problemas diferentes.</p>')
change_containing('si se utiliza Scrum, esa responsabilidad corresponde', '<li><strong>Renegociar alcance con transparencia.</strong> La persona autorizada para decidir prioridades compara QR con funcionalidades no iniciadas y consulta la viabilidad con el equipo. Para este caso se supone que postergar cupones libera esfuerzo suficiente para una primera versión. Sin esa comprobación, intercambiar funcionalidades no demuestra que se cumpla la fecha.</li>')
change_containing('el backlog se vuelve a priorizar', '<li><strong>Revisar la decisión.</strong> Si las pruebas tempranas muestran que QR no resuelve el problema o introduce un riesgo que no puede mitigarse, se reordena el trabajo pendiente. La decisión inicial se contrasta con evidencia.</li>')

append(15,'''<h3>15.2 Gestión ágil de un proyecto de IA</h3>
<p>Retomemos el asistente universitario. Elegir un modelo no resuelve por sí solo la vigencia de los documentos, la calidad de las respuestas ni la experiencia de los estudiantes. Necesitamos gestionar el <strong>sistema completo</strong> y comprobarlo en su contexto de uso.</p>
<p>En proyectos de IA pueden aparecer incertidumbres sobre datos disponibles y comportamiento del sistema. El trabajo ágil permite planificar pruebas acotadas, aprender y decidir si conviene continuar. No garantiza que el siguiente experimento mejore el resultado ni elimina la necesidad de controles.</p>
<ol><li><strong>Definir un problema pequeño.</strong> Empezar por consultas de inscripción con documentos autorizados y vigentes.</li>
<li><strong>Preparar una referencia sencilla.</strong> Probar primero un buscador de preguntas frecuentes. Esa referencia, llamada línea de base o baseline, permite comparar si una solución más compleja aporta una mejora.</li>
<li><strong>Acordar la evaluación.</strong> Seleccionar consultas de prueba, describir qué cuenta como respuesta correcta y revisar fuentes, errores y límites. Las preguntas usadas para ajustar el sistema no deben ser la única evidencia para evaluarlo.</li>
<li><strong>Comparar antes de ampliar.</strong> Probar el asistente con revisión humana. Registrar resultados y condiciones para poder repetir la evaluación.</li>
<li><strong>Decidir el siguiente paso.</strong> Corregir problemas, ampliar gradualmente o mantener la referencia sencilla si resuelve mejor la necesidad.</li></ol>
<p>Los experimentos generan <strong>aprendizaje</strong>; una entrega genera una capacidad utilizable. Si el asistente falla en las pruebas, aprendimos qué revisar, pero todavía no contamos con un resultado apto para ampliar a todos los estudiantes.</p>
<p>El <a href="https://airc.nist.gov/airmf-resources/airmf/5-sec-core/">AI RMF de NIST</a> plantea gestionar y evaluar riesgos durante el ciclo de vida de los sistemas de IA. Es un marco voluntario, no una metodología ágil ni una exigencia de esta materia. Nos ayuda a reconocer que la evaluación debe acompañar la construcción y el uso.</p>
<h3>15.3 IA que ayuda a gestionar el trabajo</h3>
<p>Hay una segunda relación: podemos utilizar IA para apoyar la gestión. Un asistente puede preparar un resumen de consultas o un borrador de tareas. Un <strong>agente de IA</strong> puede, según su configuración y permisos, encadenar acciones y utilizar herramientas para completar un objetivo. Que un producto se anuncie como agente no significa que sea infalible o que trabaje sin límites.</p>
<div class="analogia"><p><strong>Analogía de una persona que prepara una agenda.</strong> Puede reunir propuestas, detectar asuntos pendientes y redactar un orden del día. Quienes tienen responsabilidad deben comprobar la información y decidir. Un agente puede ahorrar parte de esa preparación, pero un resumen incorrecto también puede orientar mal el trabajo.</p></div>
<p>Un ejemplo de apoyo sería agrupar consultas repetidas y proponer borradores de tareas para mejorar el asistente. Una persona revisa si esos borradores representan necesidades reales antes de incorporarlos. El equipo mantiene claras las responsabilidades, los permisos y qué acciones requieren revisión.</p>
<p>En el <strong>Módulo 4</strong> estudiaremos herramientas de seguimiento con ejemplos visuales: Trello para comprender tableros, Jira para organizar y seguir trabajo más completo, y Notion como opción complementaria de documentación y tareas. Jira y Notion ofrecen funciones de IA y agentes; la disponibilidad depende de la configuración y del acceso contratado. No es necesario contar con funciones pagas para comprender los fundamentos.</p>
<p>Fuentes de herramientas consultadas el 15 de septiembre de 2026: <a href="https://trello.com/en/guide/trello-101">tableros y tarjetas en Trello</a>, <a href="https://www.atlassian.com/software/jira/ai">IA en Jira</a> y <a href="https://www.notion.com/help/notion-agent">Notion Agent</a>. Estas capacidades pueden cambiar; los ejemplos deben explicar la decisión de gestión que apoyan.</p>
<div class="criterio-profesional"><p><strong>Criterio profesional.</strong> Separá qué estás gestionando de con qué lo gestionás: un proyecto que construye IA puede usar un tablero sencillo, y un proyecto sin IA puede utilizar un agente como apoyo.</p></div>''')

replace(17,'''<p>Gestionar un proyecto requiere reconocer el resultado buscado, las personas involucradas y las restricciones. Proyecto, producto y operación tienen horizontes distintos; completar el primero no demuestra por sí solo que el producto resulte útil o pueda mantenerse.</p>
<ul><li><strong>Agilidad.</strong> Planificar, obtener evidencia y adaptar decisiones.</li><li><strong>Manifiesto.</strong> Priorizar colaboración, software que funciona y respuesta a nueva información, conservando los apoyos necesarios.</li><li><strong>Valor.</strong> Comprobar el beneficio para quienes usan o reciben la solución.</li><li><strong>Iteración e incremento.</strong> Mejorar lo construido y agregar capacidades utilizables.</li><li><strong>Elección de enfoque.</strong> Considerar incertidumbre, restricciones y costo de corregir.</li><li><strong>Ingeniería en IA.</strong> Gestionar datos, evaluaciones, integración y operación como partes de un sistema.</li></ul>
<p>Los casos del asistente universitario y de la app bancaria muestran cómo revisar prioridades sin ignorar calidad ni acuerdos. La IA también puede ayudar a preparar información de gestión; esa ayuda necesita verificación y responsabilidades claras.</p>
<p class="cierre-narrativo"><strong>Próximo paso.</strong> En el Módulo 2 vamos a comprender Scrum antes de sus roles y reglas. Después estudiaremos Kanban y Lean para comparar cómo organizan y mejoran el trabajo.</p>''',False)

# Subtítulos que cortan desarrollos conservados en unidades de aprendizaje.
for n,needle,title in [
    (2,'Un proyecto, como vimos','2.1 Diferentes horizontes'),
    (2,'En el mundo del desarrollo','2.2 Equipos y continuidad'),
    (4,'El alcance define','4.1 Qué limita el proyecto'),
    (4,'La lógica de la triple','4.2 Cómo negociar un cambio'),
    (5,'Trabajar de manera ágil','5.1 Aprender con evidencia'),
    (12,'Este enfoque presenta ventajas','12.1 Cuándo aporta y qué riesgo tiene'),
    (13,'El enfoque iterativo, en cambio','13.1 Mejorar y ampliar son movimientos distintos')]:
    h,els=section(n)
    matches=[e for e in els if e.tag=='p' and needle in e.text_content()]
    if matches:
        heading=html.Element('h3'); heading.text=title
        article.insert(list(article).index(matches[0]),heading)

# Palabras clave: hasta dos por párrafo, sin colorear párrafos completos.
terms=['proyecto','producto','operación','alcance','tiempo','costo','calidad','incertidumbre','iterativo','incremental','predictivo','valor','agilidad','aprendizaje','evidencia','feedback']
for p in article.xpath('.//p'):
    if p.xpath('.//strong|.//a') or p.text is None: continue
    text=p.text; matches=[]
    for match in re.finditer(r'\b('+ '|'.join(terms)+r')\b',text,re.I):
        if match.group(0).lower() not in [m.group(0).lower() for m in matches]: matches.append(match)
        if len(matches)==2: break
    if not matches: continue
    p.text=text[:matches[0].start()]
    for i,m in enumerate(matches):
        strong=html.Element('strong'); strong.text=m.group(0)
        strong.tail=text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)]
        p.insert(i,strong)

# Párrafos largos se separan por oración sin perder ninguna palabra.
for p in list(article.xpath('.//p')):
    if len(p.text_content().split())<=100 or len(p): continue
    sentences=re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡])',p.text or '')
    if len(sentences)<2: continue
    parent=p.getparent(); idx=list(parent).index(p); batch=[]; chunks=[]
    for s in sentences:
        batch.append(s)
        if len(' '.join(batch).split())>=55: chunks.append(' '.join(batch)); batch=[]
    if batch: chunks.append(' '.join(batch))
    if len(chunks)>1:
        parent.remove(p)
        for chunk in chunks:
            new=html.Element('p',attrib=dict(p.attrib)); new.text=chunk; parent.insert(idx,new); idx+=1

article.set('data-revision-ia','2026-09-15')
nav=tree.xpath('//nav//ol')[0]
for e in list(nav): nav.remove(e)
for h in article.xpath('./h2'):
    li=etree.SubElement(nav,'li'); a=etree.SubElement(li,'a',href='#'+h.get('id')); a.text=re.sub(r'^\d+\.\s*','',h.text_content())
path.write_bytes(html.tostring(tree,encoding='utf-8',doctype='<!DOCTYPE html>',pretty_print=True))
report={'palabras_antes':len(before.split()),'palabras_despues':len(article.text_content().split()),'h2':len(article.xpath('./h2')),'figuras':len(article.xpath('.//figure')),'enfasis':len(article.xpath('.//strong'))}
(qa/'cambios.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
