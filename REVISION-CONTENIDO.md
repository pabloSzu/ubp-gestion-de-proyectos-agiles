# Revisión de estructura y criterio editorial del contenido

Fecha: 15 de septiembre de 2026. Primera etapa de revisión de Gestión de Proyectos Ágiles.

Estado vigente: cinco fuentes de Contenido mejoradas, cinco Word actualizados, libro auxiliar y temario en Word generados. Texto, temas, listas, tablas, imágenes y enlaces conservados y comprobados. Paginación definitiva y disponibilidad audiovisual completa pendientes. Los apartados de diagnóstico describen la edición anterior; el trabajo realizado se registra al final.

## Objetivo confirmado

El entregable de Contenido siempre es Word (`Contenido.docx` por módulo). Debe ser un material universitario completo, amable, atractivo y fácil de estudiar: explicación gradual, hilo narrativo, analogías, ejemplos aplicados y casos reales documentados. Evaluaciones, presentaciones y los demás entregables se trabajan después de esta etapa.

## Alcance de esta revisión

Se revisaron los títulos y subtítulos de los cinco HTML, aperturas y muestras de desarrollo, la estructura interna de los Word, los scripts de exportación y una muestra visual previa del libro completo. No se hizo todavía una lectura editorial exhaustiva de las aproximadamente 57.000 palabras ni una nueva revisión visual de todas las páginas. Esta revisión no certifica que el contenido esté terminado.

Hay material valioso ya producido: aperturas con problemas aplicados, diagramas, tablas, casos resueltos y criterios profesionales. La mejora debe conservarlo y articularlo, evitando agregar recursos repetidos por cumplir una cuota.

## Recorrido de la materia

| Módulo | Pregunta que organiza el aprendizaje | Resultado esperado del recorrido |
|---|---|---|
| 1 Fundamentos | ¿Qué gestionamos y por qué trabajar de forma ágil? | Comprender proyecto, producto, incertidumbre, valor y fundamentos de la agilidad. |
| 2 Enfoques | ¿Cómo se organiza concretamente ese trabajo? | Explicar y comparar Scrum, Kanban, XP y Lean, y elegir con criterio. |
| 3 Producto y planificación | ¿Qué conviene construir primero y cómo lo expresamos? | Conectar necesidades, objetivos, backlog, calidad, prioridades y aprendizaje. |
| 4 Ejecución y seguimiento | ¿Cómo planificamos y sabemos si estamos avanzando? | Separar estimaciones de pronósticos y usar evidencia del trabajo para decidir. |
| 5 Equipos y mejora | ¿Cómo sostenemos la colaboración y mejoramos el sistema? | Integrar personas, calidad, operación, coordinación y aprendizaje. |

La secuencia general es coherente. Se recomienda conservar los cinco módulos y mejorar su organización interna. Pablo confirmó que esta materia no tiene un programa previo: debemos elaborarlo a partir de los mínimos suministrados. El cotejo se realiza contra esos mínimos, sin esperar un programa externo. El apartado de contenidos del programa está en `PROGRAMA-CONTENIDOS.txt`.

## Módulo 1

Situación actual: 15 secciones temáticas. “Qué es la agilidad” aparece en la sección 3, pero origen, Manifiesto y principios recién en las secciones 10 a 12. Entre ambos bloques se interponen ciclos de vida, enfoques predictivos, restricciones y stakeholders. Esto interrumpe la explicación del fundamento ágil.

Orden de trabajo propuesto, conservando los temas existentes:

1. Qué es un proyecto y qué significa gestionarlo.
2. Diferencia entre proyecto, producto y operación.
3. Personas involucradas y restricciones de alcance, tiempo, costo y calidad.
4. Incertidumbre y qué significa trabajar de forma ágil.
5. Origen de la agilidad como respuesta a problemas concretos.
6. Manifiesto: explicar cada valor mediante una decisión y un ejemplo.
7. Doce principios: presentar todos y conectarlos en grupos comprensibles.
8. Entrega de valor: distinguir hacer tareas, entregar resultados y producir un beneficio.
9. Enfoques, metodologías, marcos y prácticas: mapa breve hacia el módulo 2.
10. Ciclos de vida; predictivo, iterativo e incremental; cascada y enfoques combinados.
11. Gestión del cambio y comparación de enfoques en un caso resuelto.
12. Fuentes, recursos complementarios y síntesis con conexión al módulo 2.

Usar una situación inicial que haga visible la incertidumbre antes de introducir nombres de marcos. Evitar que la cita de apertura dé por enseñado el Manifiesto. El caso bancario existente puede conservarse; no atribuirlo a un banco real sin evidencia.

## Módulo 2

Situación actual: 14 secciones temáticas. Scrum tiene ejemplos, responsabilidades, artefactos y eventos desarrollados, pero su empirismo y valores aparecen después de esos mecanismos.

Secuencia recomendada: panorama de enfoques → definición de Scrum y ejemplo sencillo → empirismo, pensamiento Lean y valores → equipo y responsabilidades → artefactos y compromisos → Sprint y sus eventos → recorrido completo de un Sprint → Kanban y flujo → XP y prácticas → Lean y desperdicios → combinaciones y otras alternativas → comparación y selección aplicada.

Para cada enfoque, seguir preguntas comunes: qué problema aborda, cómo funciona, quién participa, qué trabajo o evidencia hace visible, cómo adapta decisiones, cuándo ayuda y cuáles son sus límites. No inventar roles o eventos obligatorios para hacer que todas las alternativas tengan la misma forma. Scrum se presenta como marco, Kanban como método de gestión del flujo y Lean como pensamiento/principios; explicar las diferencias de alcance.

Los fundamentos antes del funcionamiento son compatibles con la secuencia de la [Guía de Scrum](https://scrumguides.org/scrum-guide.html), que presenta teoría y valores antes del equipo y los eventos.

## Módulo 3

Situación actual: 15 secciones temáticas, con una progresión mayormente clara desde visión hasta cambios y lanzamientos.

Conservar la estructura, fortaleciendo la relación entre comprender necesidades y formular la visión: una visión inicial orienta la investigación y se ajusta con lo aprendido. Conectar backlog → historias → criterios de aceptación → calidad → refinamiento → priorización. Comparar criterios de aceptación, Definition of Done y Definition of Ready con el mismo ejemplo; distinguir requisito de Scrum de práctica opcional.

El caso didáctico TurnoYa ya permite integrar buena parte del módulo. Reutilizar sus usuarios y decisiones con consistencia; introducir variantes solo cuando agreguen una dificultad nueva. Aclarar supuestos de los métodos de priorización y evitar que fórmulas sustituyan el razonamiento.

## Módulo 4

Situación actual: 17 secciones temáticas. El orden es razonable, pero la sucesión de nombres de técnicas y métricas puede leerse como un catálogo.

Organizar la navegación en cuatro bloques: estimar y pronosticar; planificar según capacidad; observar el flujo y resolver bloqueos; interpretar avances, riesgos y dependencias. Presentar herramientas al final como soporte de decisiones ya comprendidas.

Mantener los subtítulos específicos y añadir transiciones entre bloques. Usar un conjunto pequeño y consistente de datos del caso para calcular tamaño relativo, capacidad, velocidad, tiempos y throughput. Cada métrica debe explicar qué pregunta responde, sus unidades, cómo se calcula, qué permite inferir y qué no. Mostrar cómo se leen burndown, burnup y flujo acumulado con datos; una definición aislada no alcanza.

## Módulo 5

Situación actual: 19 secciones temáticas y 53 subtítulos de nivel 3 en el Word. Es el módulo de mayor extensión y combina personas, ingeniería y gobierno organizacional.

Hacer visibles cuatro bloques: equipo y colaboración; inspección y mejora; calidad y entrega sostenible; coordinación y organización. Finalizar con el caso integrador existente. Mantener el desarrollo válido y equilibrar la profundidad mediante los mínimos recibidos y el programa que estamos elaborando, sin eliminar temas solo por su extensión.

Review y retrospectiva se retoman desde situaciones problemáticas, remitiendo a su definición en el módulo 2. CI, entrega continua, despliegue continuo y DevOps deben explicarse desde sus efectos sobre calidad, riesgo y feedback, sin asumir formación previa en infraestructura. Escalado se introduce por el problema de dependencias entre equipos antes de enumerar SAFe, LeSS o Scrum of Scrums.

## Criterio narrativo para revisar cada sección

Problema concreto → explicación del concepto → analogía con alcance y límites → ejemplo trabajado → interpretación del resultado → conexión con el próximo concepto. Aplicarlo con flexibilidad: no repetir mecánicamente la misma plantilla en cada página.

Las analogías deben aclarar mecanismos y volver al vocabulario técnico. Los casos resueltos hacen explícitos datos, supuestos, decisiones, alternativas y evidencia. Los casos reales requieren fuente primaria, fecha, contexto y límites; los escenarios inventados deben identificarse como didácticos.

Como posible caso histórico para colaboración y autonomía, existe una [publicación de Spotify Engineering de 2014](https://engineering.atspotify.com/2014/03/spotify-engineering-culture-part-1). Su inclusión requiere estudiar el material completo y contextualizar la fecha; no convertir ese retrato histórico en una receta universal ni en una descripción de Spotify actual.

## Diseño del Word

Los archivos ya contienen estilos Heading2/Heading3, listas, tablas e imágenes. La muestra visual revisada también muestra títulos coloreados y recuadros. El problema no se resuelve solo agregando color: se debe mejorar el ritmo de lectura y comprobar qué versión de Word está usando el alumno.

- Títulos y subtítulos con estilos nativos, jerarquía reconocible y color de alto contraste.
- Párrafos centrados en una idea; dividirlos cuando acumulan conceptos o pasos diferentes.
- Listas reales para secuencias, criterios y enumeraciones; prosa conectada para explicar causas y relaciones.
- Negritas selectivas para conceptos y decisiones, evitando resaltar párrafos completos.
- Tablas para comparaciones y datos, con encabezados repetidos y celdas legibles.
- Diagramas con pie explicativo y texto de apoyo; no depender de una imagen para enseñar un concepto esencial.
- Analogías, ejemplos y criterios con tratamientos visuales consistentes y moderados.
- Apertura orientadora e índice navegable; cierre que responda la pregunta inicial y anticipe el módulo siguiente.

Revisar espaciado, tamaño de letra, ancho de texto y saltos de página en el Word renderizado. El exportador actual rasteriza las portadas; en la mejora se debe mantener el título y la información académica como texto nativo editable y accesible, aunque conserve ilustraciones.

La vista previa actual usa `docx-preview` en navegador: ayuda a detectar problemas, pero no acredita por sí sola la paginación final de Word. La revisión final necesita un renderizador de documentos y revisión visual de todas las páginas.

## Archivos que conviene conservar

Word es el único entregable final de Contenido. Conservar `contenido.html` como fuente interna: los exportadores y diagramas existentes dependen de él. Conservar las imágenes utilizadas, los scripts y los registros editoriales necesarios. No generar un PDF académico paralelo. Un PDF temporal producido por el renderizador y las imágenes de páginas pertenecen al control interno.

No borrar archivos existentes en esta etapa: primero identificar referencias y versiones. El HTML del libro completo es generado y puede reconstruirse; su existencia no crea otro entregable ni obliga a mantener una plataforma web.

## Orden de ejecución de la mejora

1. Módulo 1: revisar íntegramente, reordenar conservando contenido válido, mejorar explicación y aplicar el diseño Word común.
2. Renderizar y revisar todas sus páginas; corregir narrativa y maquetación.
3. Repetir por módulos 2, 3, 4 y 5, controlando continuidad y progresión de dificultad.
4. Cotejar cobertura de los mínimos recibidos y del temario elaborado, coherencia terminológica, fuentes, ejemplos y cálculos entre módulos.
5. Regenerar el libro Word completo si se mantiene como archivo de consulta, sin sustituir los Word por módulo.

Estado del diagnóstico inicial: este apartado describía la materia antes de la edición. Consultar la actualización de trabajo realizado al final para el estado vigente.

## Actualización posterior a la entrega de mínimos

Pablo suministró los cinco mínimos: fundamentos y Manifiesto; Scrum, Kanban y Lean; roles y equipos; Jira, Trello y seguimiento; proyectos exitosos y desafíos comunes. No hay programa previo. Se elaboró el apartado de contenidos por módulo en `PROGRAMA-CONTENIDOS.txt`, siguiendo el formato de PAI3 y usando el desarrollo existente, sin rehacerlo.

`CONTENIDO-COMPLETO-REVISION.txt` reúne el texto actual de los cinco módulos. Es auxiliar temporal: no incluye el diseño ni reproduce los gráficos, y no debe utilizarse para certificar la calidad visual del Word. Se genera con `scripts/exportar-contenido-revision.py`; no editarlo como fuente alternativa.

El apartado de contenidos del programa está elaborado; los demás campos institucionales no se definieron todavía. La actualización siguiente registra las mejoras efectivamente realizadas y distingue los controles completados de las comprobaciones pendientes.

## Trabajo realizado el 15 de septiembre de 2026

- Módulo 1: se conservaron los quince temas; se ubicaron interesados y restricciones como contexto y agilidad, origen, Manifiesto, principios y valor antes del catálogo de enfoques. Se actualizaron transiciones, numeración e índice y se añadió una analogía con alcance y límites.
- Módulo 2: fundamentos de Scrum antes de responsabilidades, artefactos y eventos; corrección del ejemplo WIP y de afirmaciones absolutas sobre empirismo y pruebas; analogía de colaboración y caso industrial de Toyota con fuente y transferencia explícita.
- Módulo 3: metas ilustrativas claramente diferenciadas de resultados, ejemplo numérico sobre porcentajes y puntos porcentuales, valor del trabajo técnico, DoR opcional, consistencia de reservas desde el piloto y distinción entre entrega y despliegue continuos.
- Módulo 4: capacidad neta corregida a 329 horas, con 49 para C al descontar reuniones solo en días de presencia; reserva del 15 %: 279,65 horas. Se precisaron escala modificada, throughput, burndown, selección inicial frente a trabajo terminado, jerarquía de Jira y alcance de Trello. Se incorporó un ejemplo resuelto de lead time, cycle time y salidas.
- Módulo 5: Tuckman como orientación, no secuencia inevitable; analogía Review/Retrospective y experimento de mejora con datos. Se incorporaron Sentinel e ING con fuentes primarias, fechas, evidencia y límites. Se separaron expresamente los tres escenarios didácticos.

Los cinco Word se generaron con un exportador nativo común: título y portada editables, índice con enlaces internos, títulos coloreados, listas reales, tablas con encabezados repetidos, destacados moderados, figuras con pies y enlaces externos. Se dividieron 101 párrafos extensos en bloques menores conservando el texto. Se actualizó el libro auxiliar completo, se generó `Programa - contenidos.docx` y se refrescó el TXT temporal.

El control automático acredita conservación en Word de los párrafos, títulos, listas, celdas y pies de la fuente; conservación de los temas originales; 22 figuras, 37 tablas y 171 elementos de lista nativos entre los cinco módulos. Las vistas del DOCX no detectan imágenes rotas ni desbordes horizontales. No se modificaron otros entregables.

Pendiente de certificación final: `render_docx.py` falla porque no existe `soffice.exe` en el entorno empaquetado. Sin ese motor no puede acreditarse la paginación final con el control exigido. Las vistas del navegador son auxiliares. Los enlaces audiovisuales se consultaron, pero los bloqueos de YouTube y Scrum.org y el error de acceso de Mountain Goat impidieron certificar disponibilidad completa. No afirmar que esta edición es perfecta o que todos los videos están verificados.
