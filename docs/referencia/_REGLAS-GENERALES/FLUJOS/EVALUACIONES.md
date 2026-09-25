# Flujo de trabajo — Evaluaciones

Las evaluaciones son instancias formales de entrega y calificación. Se producen después de estabilizar contenido, microobjetivos, glosarios y actividades de los módulos involucrados.

## Estructura confirmada

- **Parcial 1: 40 puntos**, sobre los primeros contenidos de la materia.
- **Parcial 2: 60 puntos**, sobre la segunda parte de la materia.
- El corte exacto entre módulos se define según la progresión del programa.
- No se agrega examen final, tercer parcial ni otra evaluación salvo pedido explícito.

## Información particular que todavía puede requerir confirmación

- módulos incluidos en cada parcial;
- modalidad individual o grupal;
- formato y medio de entrega;
- política institucional sobre IA, evidencia propia y defensa oral;
- recuperatorios, aprobación y cualquier requisito especial.

No trasladar automáticamente las reglas históricas de PAI3. Si un dato falta, preparar la estructura y marcar el campo pendiente sin presentarlo como decisión oficial.

## Diseño

1. Construir una tabla de trazabilidad entre microobjetivos, contenidos y consignas.
2. Combinar comprensión, aplicación y justificación; evitar evaluar solo memoria terminológica.
3. Numerar actividades y partes, indicando módulo y puntaje; cada parcial debe sumar exactamente 40 o 60 puntos según corresponda.
4. Verificar que los puntajes parciales sumen exactamente el total.
5. Incluir una rúbrica coherente con las consignas. Los ejes generales pueden ser concepto, aplicación, evidencia y comunicación, adaptados al dominio.
6. Preparar criterios o solución esperada para corrección docente en un archivo separado cuando corresponda.

## Archivos y exportación

Cada parcial vive en `entregables/EVALUACIONES/PARCIAL N/` con dos fuentes Markdown: `evaluacion.md` (para estudiantes) y `guia-docente.md` (trazabilidad, respuestas esperadas y criterios de puntaje, solo para el docente). Se exportan con `scripts/md-a-word.py --parcial N --tipo evaluacion|guia` a `Evaluacion.docx` y `Guia-docente.docx`. Usar la misma sintaxis y recuadros que el Contenido. Verificar con un script que las partes sumen el puntaje de cada actividad y que el total sea exactamente 40 o 60.

## Control

Resolver la evaluación completa antes de entregarla, comprobar tiempos razonables, ambigüedades, dependencias externas y accesibilidad de los recursos. Generar el Word final y revisar todas sus páginas. Mantener claramente separados el documento para estudiantes y la guía docente.
