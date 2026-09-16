# Gestión de Proyectos Ágiles

## Historial de versiones

Repositorio: https://github.com/pabloSzu/ubp-gestion-de-proyectos-agiles. Ver [cómo guardar versiones y qué incluye el respaldo inicial](VERSIONES.md). Una copia sincronizada de las reglas compartidas se conserva en [docs/referencia](docs/referencia/README.md) para consultar el repositorio por separado.

Materia de UBP producida por Pablo como profesor contenidista. Es la referencia de estructura para Gestión de Proyectos y las materias que se generen a continuación. El nombre oficial confirmado por Pablo es Gestión de Proyectos Ágiles.

## Organización actual

La carrera confirmada por Pablo es **Ingeniería en IA**. Consultar los [criterios de orientación y revisión pedagógica](ORIENTACION-INGENIERIA-IA.md). Los cinco módulos ya siguen el recorrido acordado: vocabulario en orden de aprendizaje, menor densidad, énfasis cromático y un asistente universitario con IA como caso conductor. Las etiquetas visibles indican cuándo el texto trata un concepto general, Scrum, Kanban, XP, Lean, prácticas de ingeniería, herramientas o un caso de IA. El módulo 4 enseña primero el seguimiento en Scrum, cierra ese bloque, desarrolla después Kanban y recién al final compara e integra ambos enfoques. Incorpora referencias visuales oficiales de Trello y Jira y presenta Notion como complemento opcional.

`entregables/` contiene cinco módulos. Cada uno tiene exactamente las cuatro clases requeridas: Glosario, entre 4 y 6 Microobjetivos iniciados por un verbo en infinitivo, Contenido y Actividades. Las Actividades pueden incluir preguntas, autoevaluaciones, casos, videos o prácticas con herramientas externas.

También existen `entregables/EVALUACIONES/` y `entregables/PRESENTACIONES/`, actualmente sin archivos. Deben contener dos parciales —40 puntos para los primeros contenidos y 60 para la segunda parte— y presentaciones de materia, una por módulo y cierre, todas con la misma plantilla y hasta siete diapositivas. Esto describe el inventario; no implica que la materia esté terminada o validada.

El paquete incluye además un mapa conceptual general. Pablo lo genera por separado; debe incorporarse a `entregables/MAPA CONCEPTUAL/` cuando esté disponible y no debe producirse automáticamente.

`scripts/` contiene herramientas de exportación y comprobación, además de scripts de ajustes previos. `output/`, `tmp/` y `.qa/` son carpetas auxiliares de producción y revisión.

## Reglas aplicables

Consultar la [documentación general](../README.md), la [estructura común](../_REGLAS-GENERALES/ESTRUCTURA-MATERIA.md), el [estilo editorial](../_REGLAS-GENERALES/ESTILO-EDITORIAL.md) y el flujo del entregable solicitado.

Esta materia se produce mediante el paquete obligatorio documentado. No requiere plataforma web. Las actividades son formativas y pueden usar preguntas, ejercicios, autoevaluaciones, videos o herramientas externas. La entrega y calificación corresponden a dos evaluaciones: 40 puntos para la primera parte y 60 para la segunda; todavía debe definirse el corte exacto entre módulos.

Los HTML y Markdown son fuentes editoriales. El entregable final de Contenido siempre es Word. HTML se conserva como fuente interna para editar y exportar. PDF no es un entregable de Contenido; solo puede producirse temporalmente para revisión visual. Las presentaciones deben seguir el patrón común de plantilla y estructura documentado.

## Herramientas de exportación

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
