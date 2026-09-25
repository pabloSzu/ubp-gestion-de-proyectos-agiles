# Gestión de Proyectos Ágiles

## Historial de versiones

Repositorio: https://github.com/pabloSzu/ubp-gestion-de-proyectos-agiles. Ver [cómo guardar versiones y qué incluye el respaldo inicial](VERSIONES.md). Una copia sincronizada de las reglas compartidas se conserva en [docs/referencia](docs/referencia/README.md) para consultar el repositorio por separado.

Materia de UBP producida por Pablo como profesor contenidista. Es la referencia de estructura para Gestión de Proyectos y las materias que se generen a continuación. El nombre oficial confirmado por Pablo es Gestión de Proyectos Ágiles.

## Organización actual

La carrera confirmada por Pablo es **Ingeniería en IA**. Consultar los [criterios de orientación y revisión pedagógica](ORIENTACION-INGENIERIA-IA.md). Los cinco módulos ya siguen el recorrido acordado: vocabulario en orden de aprendizaje, menor densidad, énfasis cromático y un asistente universitario con IA como caso conductor. Las etiquetas visibles indican cuándo el texto trata un concepto general, Scrum, Kanban, XP, Lean, prácticas de ingeniería, herramientas o un caso de IA. El módulo 4 enseña primero el seguimiento en Scrum, cierra ese bloque, desarrolla después Kanban y recién al final compara e integra ambos enfoques. Incorpora referencias visuales oficiales de Trello y Jira y presenta Notion como complemento opcional.

`entregables/` contiene cinco módulos. Cada uno tiene exactamente las cuatro clases requeridas: Glosario, hasta 4 Microobjetivos iniciados por un verbo en infinitivo, Contenido y Actividades. Las Actividades pueden incluir preguntas, autoevaluaciones, casos, videos o prácticas con herramientas externas.

También existen `entregables/EVALUACIONES/` y `entregables/PRESENTACIONES/`, actualmente sin archivos. Deben contener dos parciales —40 puntos para los primeros contenidos y 60 para la segunda parte— y presentaciones de materia, una por módulo y cierre, todas con la misma plantilla y hasta siete diapositivas. Esto describe el inventario; no implica que la materia esté terminada o validada.

El paquete incluye además un mapa conceptual general. Pablo lo genera por separado; debe incorporarse a `entregables/MAPA CONCEPTUAL/` cuando esté disponible y no debe producirse automáticamente.

`scripts/` contiene herramientas de exportación y comprobación, además de scripts de ajustes previos. `output/`, `tmp/` y `.qa/` son carpetas auxiliares de producción y revisión.

## Reglas aplicables

Consultar la [documentación general](../README.md), la [estructura común](../_REGLAS-GENERALES/ESTRUCTURA-MATERIA.md), el [estilo editorial](../_REGLAS-GENERALES/ESTILO-EDITORIAL.md) y el flujo del entregable solicitado.

Esta materia se produce mediante el paquete obligatorio documentado. No requiere plataforma web. Las actividades son formativas y pueden usar preguntas, ejercicios, autoevaluaciones, videos o herramientas externas. La entrega y calificación corresponden a dos evaluaciones: 40 puntos para la primera parte y 60 para la segunda; todavía debe definirse el corte exacto entre módulos.

Los HTML y Markdown son fuentes editoriales. El entregable final de Contenido siempre es Word. HTML se conserva como fuente interna para editar y exportar. PDF no es un entregable de Contenido; solo puede producirse temporalmente para revisión visual. Las presentaciones deben seguir el patrón común de plantilla y estructura documentado.

## Herramientas de exportación

**Modelo vigente (desde el 25 de septiembre de 2026):** los módulos reescritos tienen su fuente en `contenido.md` y se exportan con `scripts/md-a-word.py --modulo N`. Es el modelo que siguen también las materias futuras (ver `../_REGLAS-GENERALES/FLUJOS/CONTENIDO.md`). Lo que sigue describe el exportador histórico, vigente solo para los módulos que todavía conservan `contenido.html`.

La edición del 15 de septiembre de 2026 utiliza `scripts/render-contenido-word-nativo.py`, ejecutado con el Python provisto por `load_workspace_dependencies`. Genera los cinco `Contenido.docx` y actualiza el libro auxiliar de `output/`. Conserva portadas e índices como texto editable, estilos nativos, listas, tablas, enlaces y diagramas. No ejecutar los exportadores históricos para regenerar esta edición: producen un diseño diferente. `scripts/programa-word.py` genera el apartado de contenidos del programa en Word. Todo Word final requiere renderizado y revisión visual.

`npm run render:word` apunta a ese exportador nativo mediante el runtime empaquetado de este equipo; `render:word:historico` conserva el comando anterior solo como referencia. Los scripts de edición puntual registran esta intervención y no son parte del flujo habitual de exportación: no volver a ejecutarlos sobre una fuente ya modificada. El HTML generado del libro completo pertenece al flujo histórico y no controla la edición Word actual.

## Etapa actual

Primero perfeccionar el Contenido; evaluaciones, presentaciones y demás entregables se trabajan después. El [diagnóstico de estructura y diseño](REVISION-CONTENIDO.md) registra el recorrido propuesto y las verificaciones pendientes.


## Programa y archivos de revisión

Esta materia no tiene programa previo: Pablo debe elaborarlo a partir de los mínimos universitarios que proporcionó. El [apartado de contenidos del programa](PROGRAMA-CONTENIDOS.txt) registra los cinco módulos, la relación con los mínimos y las ampliaciones ya presentes. No equivale todavía a un programa institucional completo.

El [TXT de contenido reunido](CONTENIDO-COMPLETO-REVISION.txt) es un auxiliar temporal generado desde los cinco HTML mejorados. Preserva su texto y orden actual; no es una fuente editorial alternativa. Los gráficos, enlaces y diseño se consultan en las fuentes y en Word. El temario también está disponible en `Programa - contenidos.docx`.

## Edición de contenido del 15 y 16 de septiembre de 2026

Los cinco módulos fueron mejorados y exportados a Word. Se reorganizaron fundamentos y mecanismos en los módulos 1 y 2, se incorporaron analogías y ejemplos resueltos, se corrigieron capacidad, interpretación de métricas y diferencias entre prácticas opcionales y reglas de Scrum, y se añadieron casos documentados de Toyota, Sentinel e ING. Los tres escenarios simulados del módulo 5 permanecen identificados como didácticos.

La revisión del 16 de septiembre separó cada framework en bloques cerrados y añadió transiciones de contexto. El módulo 3 distingue el Product Backlog y la Definition of Done de Scrum de historias, INVEST y DoR como prácticas complementarias. El módulo 4 se titula **Planificación y Seguimiento del Trabajo en Scrum y Kanban** y contiene casos completos separados para un Sprint y para soporte continuo, una comparación explícita y un caso de integración. El módulo 5 distingue Sprint Review, Sprint Retrospective y Kaizen antes de pasar a ingeniería, escala y casos.

Las fuentes previas están respaldadas en `.qa/edicion-contenido/antes/` y la versión inmediatamente anterior a la separación de frameworks en `.qa/reestructuracion-frameworks-2026-09-16/antes/`. Los controles acreditan conservación del contenido exportado, listas y tablas nativas, imágenes, enlaces y marcadores internos únicos. La vista auxiliar completa de los cinco Word no detectó imágenes rotas ni desbordes horizontales. La paginación definitiva está pendiente: el renderizador empaquetado no encuentra LibreOffice. La vista de navegador ayuda a revisar legibilidad y ancho, pero no acredita los cortes de página de Word. La comprobación de disponibilidad de todos los videos también queda pendiente por bloqueos de los sitios consultados; las explicaciones esenciales están en el contenido.

## Actividades revisadas el 19 de septiembre de 2026

Por pedido de Pablo se avanzó a Actividades. Los cinco módulos contienen 22 prácticas autónomas (4, 5, 4, 5 y 4), con preguntas, casos, cálculos, decisiones y respuestas orientativas. Las fuentes están en cada carpeta `Actividades/actividades.html` y sus versiones editables en `Actividades.docx`. No requieren entrega, calificación ni cuentas externas. El módulo 4 incorpora una práctica de tablero con alternativa completa en papel.

Los enlaces complementarios del Manifiesto, la Guía Scrum y las guías de Trello y Jira se comprobaron por consulta web. Las respuestas se resuelven con el módulo aunque esos recursos no estén disponibles. La lista de videos actuales, sus temas y los focos propuestos para reemplazarlos está en [Videos para reemplazar](VIDEOS-PARA-REEMPLAZAR.md). Los videos de Contenido todavía no se modificaron: falta la selección de Pablo.

Exportación exclusiva de actividades: `scripts/render-actividades-word.py`, con el Python empaquetado. No regenera Contenido ni otros entregables. Se verificaron conservación del texto, listas, tablas, enlaces y cálculos. La vista auxiliar de los cinco Word se revisó completa y no mostró desbordes horizontales. La paginación nativa sigue pendiente porque no hay LibreOffice disponible; los Word son versiones para revisión, no una entrega institucional certificada. Controles y respaldos en `.qa/actividades-2026-09-19/`.

## Reescritura del Módulo 1 (25 de septiembre de 2026)

A partir de la revisión de Pablo se creó [GUIA-CONTENIDO.md](GUIA-CONTENIDO.md), archivo central con el mapa de temas por módulo, el estilo y los recuadros. El Módulo 1 se reescribió en `entregables/MODULO 1/Contenido/contenido.md` y se exporta con `scripts/md-a-word.py --modulo 1`: alcance y riesgo como secciones propias, ejemplos cotidianos en recuadros de color, sin rótulos de "Analogía" ni recuadros de "Criterio profesional", sin fechas de consulta. Se retiraron el panorama de marcos (ya está en el Módulo 2) y la sección de IA y herramientas, que pasa al Módulo 4 (ver la guía). El Word se revisó página por página mediante conversión a PDF con LibreOffice.

Atención: `entregables/MODULO 1/Contenido/contenido.html` quedó sobrescrito el 22 de septiembre con una copia de `Contenido.docx` (es un Word con extensión .html). La fuente HTML anterior está en git y en `.qa/reescritura-modulo1-2026-09-25/antes/`. Ya no es la fuente del módulo. El libro completo de `output/` no se regeneró.

## Reescritura del Módulo 2 (25 de septiembre de 2026)

Fuente en `entregables/MODULO 2/Contenido/contenido.md`, exportada con `scripts/md-a-word.py --modulo 2`. Bloques rotulados por contexto (Scrum, Kanban, XP, Lean) y comparación al final. Casos reales: origen de Scrum (Takeuchi y Nonaka, Sutherland y Schwaber), State of Agile 2023, Microsoft XIT (Kanban), Chrysler C3 (XP) y Toyota (Lean). Respaldo previo en `.qa/reescritura-modulo2-2026-09-25/antes/`. El `contenido.html` anterior se conserva pero ya no es la fuente.

## Reescritura del Módulo 3 (25 de septiembre de 2026)

Fuente en `entregables/MODULO 3/Contenido/contenido.md`. Se retiró el caso TurnoYa: todo el módulo usa el asistente universitario. Se quitaron las repeticiones con módulos anteriores (matriz de poder e interés, Dropbox y explicación de la Definition of Done). Casos reales: Amazon Working Backwards, Jeffries y Wake (historias e INVEST), Pendo 2019, Zappos y HealthCare.gov. La imagen `refinamiento-mvp-feedback.png` (contexto clínico) dejó de usarse; hay una propuesta de reemplazo en `IMAGENES-PROPUESTAS.md`. Respaldo en `.qa/reescritura-modulo3-2026-09-25/antes/`.

## Reescritura del Módulo 4 (25 de septiembre de 2026)

Fuente en `entregables/MODULO 4/Contenido/contenido.md`. Se redujo de 18 a 10 secciones: se quitó lo que ya enseña el Módulo 2 (tablero Kanban, límites WIP, Ley de Little) y se unificaron impedimentos, riesgos y dependencias. Incorpora las secciones de herramientas (panorama, Trello, Jira) e IA en la gestión (asistentes, agentes, comparación con el ciclo ágil, límites). Casos reales: falacia de la planificación (1994), Planning Poker, agentes en Jira y Notion, ReAct y Klarna. El generador ahora soporta citas con "> ". Respaldo en `.qa/reescritura-modulo4-2026-09-25/antes/`.

## Reescritura del Módulo 5 (25 de septiembre de 2026)

Fuente en `entregables/MODULO 5/Contenido/contenido.md`. De 19 a 13 secciones, organizadas en equipo y colaboración, inspección y mejora, calidad y entrega, organización y escala, y casos. Se quitaron repeticiones (matriz de interesados, escenario Kanban de soporte, bases de integración continua) y el ejemplo de TurnoYa. Casos reales: Proyecto Aristóteles, Sculley y otros (2015), Knight Capital, DORA, modelo Spotify, ING y Sentinel, que cierra la historia del Virtual Case File del Módulo 1. El caso integrador recorre los cinco módulos. Respaldo en `.qa/reescritura-modulo5-2026-09-25/antes/`.

Con esto, los cinco módulos de Contenido quedaron reescritos con el modelo de `GUIA-CONTENIDO.md`. Pendientes: imágenes que Pablo generará por su cuenta, revisión de videos y actualización de glosarios, microobjetivos y actividades para alinearlos con los nuevos contenidos.

## Actividades, glosarios y microobjetivos (25 de septiembre de 2026)

Alineados con el Contenido reescrito. Los tres entregables tienen fuente Markdown (`actividades.md`, `glosario.md`, `microobjetivos.md`) y se exportan con `scripts/md-a-word.py --modulo N --tipo actividades|glosario|microobjetivos`, con el mismo diseño que el Contenido.

- **Microobjetivos:** 4 por módulo, cortos, con verbo en infinitivo. Pablo fijó el máximo en 4 (antes la regla decía de 4 a 6); se actualizaron las reglas generales.
- **Glosarios:** rehechos a partir del Contenido nuevo (40, 48, 32, 32 y 25 términos), con la misma terminología y en orden de aparición. Se agregaron los términos nuevos (alcance, riesgo, WBS, agentes de IA, seguridad psicológica, métricas DORA, entre otros) y se quitaron los que ya no aparecen.
- **Actividades:** 22 prácticas autónomas (5, 5, 4, 5 y 4) con situación, consignas numeradas y una guía de autoevaluación. Las respuestas orientativas no van en las actividades: están en `Actividades/respuestas-docente.md` y `Respuestas-docente.docx`, material del docente que no se entrega; los estudiantes pueden pedírselas al profesor. Retoman el asistente universitario, sin TurnoYa, y cada módulo incluye al menos una actividad sobre un caso real (Virtual Case File, Microsoft y Kanban, Zappos y HealthCare.gov, Klarna, Sentinel, ING, Spotify y Knight Capital). Las fuentes HTML anteriores se retiraron del repositorio y quedan respaldadas en `.qa/actividades-glosario-micro-2026-09-25/antes/`. `scripts/render-actividades-word.py` queda como exportador histórico.
