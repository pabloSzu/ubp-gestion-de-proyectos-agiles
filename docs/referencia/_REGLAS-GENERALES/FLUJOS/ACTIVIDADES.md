# Flujo de trabajo — Actividades formativas

Las actividades de Gestión y de las materias futuras son prácticas autónomas. No se entregan, no tienen nota y no llevan rúbrica porcentual.

## Insumos y alcance

Leer el contenido, los microobjetivos y el glosario del módulo terminado. No introducir teoría que el estudiante todavía no recibió ni usar la actividad para completar omisiones del contenido.

## Formatos posibles

El entregable de Actividades puede combinar, según el contenido del módulo:

- preguntas de comprensión y análisis;
- ejercicios o casos aplicados;
- autoevaluaciones con feedback;
- actividades prácticas en una herramienta externa;
- visualización de un video seguida de preguntas o decisiones;
- comparación de alternativas, diagnóstico o producción breve.

No es obligatorio usar todos los formatos en cada módulo. Variar las propuestas y elegir las que mejor permitan aplicar los microobjetivos.

## Estructura

1. Situación o caso aplicado, breve y concreto.
2. Consigna que indique qué debe analizar, decidir o producir el estudiante.
3. Preguntas, ejercicios o pasos numerados, con al menos una aplicación.
4. Guía de autoevaluación al final (preguntas para que el estudiante revise su trabajo) y una nota que indique que no hay una única respuesta correcta y que puede pedirle al profesor las respuestas orientativas.
5. Aclaración opcional sobre errores frecuentes.

La actividad debe poder resolverse con el material del módulo. Citar las secciones del Contenido por su nombre o número vigente y usar la misma terminología. Incluir al menos una actividad que analice un caso real del módulo, separando contexto, intervención, evidencia y lo que no puede concluirse. Puede reutilizar el caso conductor, pero debe plantear una decisión nueva. Si usa un video, enlace o herramienta externa, verificar disponibilidad, explicar qué debe observarse y prever una alternativa razonable cuando el recurso no sea esencial. No pedir formatos de entrega, defensa oral ni evidencia para calificación.

## Salida y control

La fuente es `entregables/MODULO N/Actividades/actividades.md`, con la misma sintaxis y los mismos recuadros que el Contenido (ver `CONTENIDO.md`): un `## Actividad N: título` por actividad, la situación en un recuadro `caso`, las consignas como lista numerada y una sección final `## Antes de terminar` con la nota sobre las respuestas y la guía de autoevaluación. Las respuestas orientativas **no van en las actividades**, por pedido de Pablo: se guardan en `respuestas-docente.md`, en la misma carpeta, y se exportan con `--tipo respuestas` a `Respuestas-docente.docx`, material del docente que no se entrega a los estudiantes. Generar el Word con `scripts/md-a-word.py --modulo N --tipo actividades`. Verificar correspondencia con los microobjetivos, claridad de la consigna y ausencia de puntajes o lenguaje de evaluación sumativa.
