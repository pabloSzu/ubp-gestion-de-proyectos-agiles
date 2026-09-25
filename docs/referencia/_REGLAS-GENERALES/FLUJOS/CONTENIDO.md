# Flujo de trabajo — Contenido de un módulo UBP

Este documento es la fuente de verdad para escribir o mejorar el Contenido de cualquier materia. Se aplica junto con `../ESTRUCTURA-MATERIA.md` y `../ESTILO-EDITORIAL.md`; ante una contradicción, prevalecen esos dos documentos generales y la instrucción puntual del usuario.

Modelo vigente desde el 25 de septiembre de 2026, acordado con Pablo al reescribir el Módulo 1 de Gestión de Proyectos Ágiles. Ese módulo es el ejemplo de referencia: `GESTION-PROYECTOS-AGILES/entregables/MODULO 1/Contenido/contenido.md`.

## Piezas del sistema

| Pieza | Ubicación | Función |
|---|---|---|
| Guía central de la materia | `<MATERIA>/GUIA-CONTENIDO.md` | Qué tema va en cada módulo y con qué profundidad, caso conductor, casos reales ya usados y decisiones propias de la materia. Se crea a partir de `../PLANTILLA-GUIA-CONTENIDO.md`. |
| Fuente del módulo | `<MATERIA>/entregables/MODULO <N>/Contenido/contenido.md` | Texto completo en Markdown con recuadros. Es lo único que se edita. |
| Generador de Word | `<MATERIA>/scripts/md-a-word.py` (con `render-contenido-word-nativo.py`) | Produce `Contenido.docx` con portada, índice, estilos, tablas, figuras y recuadros de color. Copiarlos desde Gestión al iniciar una materia. |
| Entregable | `Contenido.docx` en la misma carpeta | Lo único que se entrega. |

Los módulos de materias anteriores que todavía tengan `contenido.html` conservan esa fuente hasta que se reescriban; no convertirlos sin pedido.

## Entrada y alcance

La tarea debe identificar la materia y el número de módulo. Si falta un dato que impide identificar un único archivo, solicitarlo. Editar solamente `contenido.md`, `IMAGENES-PROPUESTAS.md` y, si cambia el reparto de temas o se usan casos nuevos, la `GUIA-CONTENIDO.md` de la materia. No modificar Microobjetivos, Glosario, Actividades, Evaluaciones, Presentaciones ni otros módulos salvo pedido explícito.

## Preparación obligatoria

1. Leer completos `ESTRUCTURA-MATERIA.md`, `ESTILO-EDITORIAL.md` y este flujo.
2. Leer la `GUIA-CONTENIDO.md` de la materia. Si no existe, crearla desde la plantilla antes de escribir el primer módulo, con el mapa de temas derivado del programa o de los contenidos mínimos.
3. Leer completo el contenido actual del módulo, si existe, y los títulos de los módulos vecinos.
4. Comprobar en el mapa de temas qué corresponde a este módulo, con qué profundidad, y qué se desarrolla en otro módulo (esto último se menciona en una línea y se sigue).
5. Revisar la lista de casos reales ya usados para no repetirlos.

## Cómo escribir la fuente

### Encabezado

```text
---
materia: Nombre oficial de la materia
modulo: 1
titulo: Título del módulo
subtitulo: Una línea que resume el módulo.
---
```

### Estructura

- Apertura sin título: una situación reconocible, qué se va a aprender y, en un recuadro `clave`, la presentación del caso conductor de la materia.
- Un recuadro `clave` con lo que el estudiante va a poder hacer al terminar.
- Secciones `## N. Título` y subsecciones `### N.M Título`. Cada sección arranca con un gancho antes de la definición.
- Los conceptos fundamentales de la materia tienen sección propia: definición, cómo reconocerlo, ejemplo, preguntas para aplicarlo y errores típicos.
- Cierre con `## Recursos audiovisuales sugeridos`, `## Para profundizar` y `## Síntesis del módulo` como último título, con un párrafo de próximo paso.

### Sintaxis

- Tablas Markdown con una línea `Tabla: título` inmediatamente debajo.
- Imágenes: `![texto alternativo](assets/archivo.png "pie de figura")`.
- Listas con `- ` o numeradas (la numeración escrita se respeta tal cual).
- Listas anidadas con 4 espacios de sangría por nivel.
- Citas o frases destacadas con `> ` al inicio de la línea (se muestran con sangría, cursiva y fondo suave).
- Negrita para conceptos clave: el generador las colorea automáticamente.

### Recuadros

```text
:::tipo Título del recuadro
Párrafos o listas.
:::
```

| Tipo | Uso | Cantidad orientativa por módulo |
|---|---|---|
| `ejemplo` | Situación cotidiana que aclara un concepto mejor que cualquier otra cosa. Se escribe "Imaginate…", "Pensá en…" o se plantea directo. Nunca se rotula "Analogía". | 4 a 6 |
| `real` | Caso real documentado: qué pasó, datos concretos, qué enseña, y al final `Fuente: [nombre](url)`. | 5 a 8 |
| `clave` | Definición o idea que hay que recordar. | Una por concepto central |
| `ensimple` | Resumen de dos o tres líneas, en criollo. | 3 a 5 |
| `preguntas` | Preguntas prácticas para aplicar el concepto. Reemplaza al antiguo "Criterio profesional". | 3 a 6 |
| `mito` | Párrafo `**Mito:** …`, línea en blanco, `**Realidad:** …`. | 1 a 3 |
| `caso` | Caso resuelto paso a paso (puede ser didáctico, identificado como tal). | 1 a 2 |
| `historia` | Dato histórico o anécdota de origen. | 0 a 2 |
| `contexto` | Rótulo breve al abrir el bloque de un marco o enfoque ("Contexto: Scrum"), con una línea sobre qué reglas rigen. | Uno por bloque, solo si conviven varios marcos |

No usar recuadros de "Criterio profesional". Un recuadro que no agrega comprensión se elimina.

## Investigación

Usar búsqueda web para todo dato, cifra, fecha, caso real, funcionalidad de herramienta y video. Preferir fuentes primarias o institucionales. No inventar URLs. Los casos reales llevan su fuente al final del recuadro; los escenarios inventados se identifican como didácticos. No escribir fechas de consulta en el cuerpo del texto.

Cuando un módulo necesite una imagen nueva, describirla en `IMAGENES-PROPUESTAS.md` (qué muestra, dónde va, para qué sirve) y no generarla sin aprobación.

## Generar y revisar el Word

1. Ejecutar `python scripts/md-a-word.py --modulo N` desde la carpeta de la materia. Si el Word está abierto, cerrar el archivo o usar `--salida` con otra ruta temporal.
2. Convertir el Word a PDF con LibreOffice (`C:/Program Files/LibreOffice/program/soffice.exe --headless --convert-to pdf`) en una carpeta auxiliar y revisar todas las páginas como imagen.
3. Controlar: recuadros sin títulos huérfanos al pie de página, filas de tabla sin cortes, imágenes completas, enlaces activos, índice correcto y ausencia de huecos grandes.
4. El PDF es solo control temporal: no se guarda en `entregables/` ni se entrega.

## Verificación final

- alcance de archivos respetado y temas coherentes con el mapa de la guía;
- conceptos centrales desarrollados, no solo nombrados;
- cantidades de recuadros dentro de lo orientativo, sin rótulos "Analogía" ni "Criterio profesional";
- casos reales verificados, con fuente, y registrados en la guía;
- ningún guion usado como puntuación en la prosa;
- `Síntesis del módulo` como último título;
- Word generado y revisado página por página.

Si el módulo presenta varios enfoques, comprobar además que cada bloque identifica su contexto, que el vocabulario aparece después de su definición, que hay transiciones al cambiar de enfoque y que las comparaciones aparecen después de enseñar cada alternativa por separado.

Informar qué cambió por sección, los casos reales incorporados, los videos, las propuestas de imágenes y las verificaciones realizadas.
