# Instrucciones del proyecto

## Propósito y alcance

Pablo es profesor contenidista de UBP. Este workspace reúne materias y sus entregables académicos. Leer `README.md` antes de trabajar y consultar las reglas generales y la documentación de la materia afectada.

- Priorizar los entregables solicitados: Contenido, Glosario, Microobjetivos, Actividades, Evaluaciones y Presentaciones.
- Gestión de Proyectos y las materias futuras usan el modelo común de `_REGLAS-GENERALES/ESTRUCTURA-MATERIA.md` y `_REGLAS-GENERALES/ESTILO-EDITORIAL.md`.
- PAI3 (`SISTEMAS-INTERACTIVOS/`) tiene una estructura histórica propia. No migrarla ni rehacerla sin pedido.
- `SISTEMAS-INTERACTIVOS/Materia_Web/` es un complemento particular de PAI3. No crear ni replicar una plataforma web para otras materias sin pedido explícito.
- No confundir una fuente editorial (Markdown o HTML) con una aplicación web, ni archivos auxiliares con archivos finales para la universidad.
- Tratar `_REGLAS-GENERALES/PAQUETE-OBLIGATORIO.md` como lista cerrada: no agregar entregables por analogía con PAI3 ni por iniciativa propia.
- El mapa conceptual general forma parte del paquete, pero Pablo lo genera por separado. Registrarlo en el inventario y no crearlo ni modificarlo salvo pedido explícito.

## Producción

Toda materia nueva crea su `GUIA-CONTENIDO.md` desde `_REGLAS-GENERALES/PLANTILLA-GUIA-CONTENIDO.md` y escribe el Contenido en Markdown según `_REGLAS-GENERALES/FLUJOS/CONTENIDO.md`: pocos ejemplos cotidianos, casos reales documentados, recuadros de color, sin rótulos "Analogía" ni recuadros de "Criterio profesional".


Usar el flujo específico de `_REGLAS-GENERALES/FLUJOS/` y las skills pertinentes al entregable solicitado. Aplicar también `_REGLAS-GENERALES/CONTROL-DE-CALIDAD.md` y `_REGLAS-GENERALES/VERSIONADO-Y-ENTREGA.md`. Consultar primero Gestión como referencia de estructura vigente; usar PAI3 solo para ejemplos pedagógicos o técnicos compatibles.

Conservar la estructura común también para evaluaciones y presentaciones. Las dos evaluaciones suman 40 y 60 puntos respectivamente; no proponer 50/50 ni un examen final. No inventar políticas de IA, modalidades de defensa ni otros requisitos institucionales. Identificar lo que falte y pedir únicamente la información necesaria para la tarea concreta.

Las actividades de Gestión y futuras materias son práctica formativa con autoevaluación; la entrega y calificación corresponden a las evaluaciones. No trasladar las actividades calificadas históricas de PAI3.

Modificar solo la materia y los entregables incluidos en el pedido. No regenerar exportaciones o ejecutar scripts históricos de ajustes sin verificar su alcance. Para Word final, seguir la exportación y revisión visual documentadas.

Si se acuerda una nueva regla reutilizable, actualizar la documentación general correspondiente; si es una excepción de una materia, registrarla en esa materia. Mantener diferenciados los requisitos confirmados y las decisiones pendientes.

Cuando convivan varios marcos, métodos o prácticas, enseñarlos en bloques cerrados y rotulados. Definir cada contexto antes de usar su vocabulario; anunciar el cambio de contexto y comparar o combinar solo después de explicar cada alternativa por separado. El color refuerza la etiqueta, pero el texto debe identificar siempre el contexto.

## Decisiones confirmadas de Contenido

Gestión de Proyectos Ágiles pertenece a Ingeniería en IA, confirmado por Pablo. Consultar `GESTION-PROYECTOS-AGILES/ORIENTACION-INGENIERIA-IA.md`: adaptar ejemplos y aplicaciones sin inventar nuevos mínimos universitarios. Definir cada marco antes de sus roles o comparaciones; usar énfasis cromático selectivo en palabras clave de Word. Distinguir proyectos que construyen IA y uso de IA como apoyo de gestión. Pedido vigente: no hacer commit ni push sin nueva autorización explícita.

El nombre oficial es Gestión de Proyectos Ágiles. El entregable final de Contenido siempre es Word para Gestión y futuras materias. La fuente de cada módulo reescrito es `contenido.md` y se exporta con `scripts/md-a-word.py`; los módulos aún no reescritos conservan su HTML como fuente interna. Consultar `GESTION-PROYECTOS-AGILES/GUIA-CONTENIDO.md` antes de escribir: define qué tema va en cada módulo, el estilo y los recuadros. PDF solo para control temporal. Prioridad actual: perfeccionar el Contenido de los cinco módulos con hilo narrativo, explicación gradual, analogías, ejemplos y diseño Word atractivo. Los demás entregables se trabajan después de esta etapa. Consultar GESTION-PROYECTOS-AGILES/REVISION-CONTENIDO.md para el diagnóstico inicial, sin confundirlo con una revisión completa.


Gestión de Proyectos Ágiles no tiene programa previo, según confirmó Pablo. Elaborar el programa a partir de los mínimos registrados en `GESTION-PROYECTOS-AGILES/PROGRAMA-CONTENIDOS.txt`, sin pedir un programa externo. Revisar y mejorar los contenidos que ya existen; no recrearlos desde cero. El TXT de contenido reunido es temporal y generado; las fuentes son `contenido.md` (módulos reescritos) o `contenido.html` (pendientes) y el entregable final sigue siendo Word.
