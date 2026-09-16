# Estructura general de una materia — UBP

Modelo común de organización y entregables para Gestión de Proyectos y todas las materias futuras dentro de `UBP-Materias/<NOMBRE-MATERIA>/`. Gestión es la referencia vigente. PAI3 (Sistemas Interactivos) conserva su estructura histórica y se consulta solo como antecedente compatible; no se modifica retroactivamente. Ver `../README.md` para el contexto del proyecto.

## Carpetas de entregables

```
entregables/
├── MODULO 1.. N/
│   ├── Contenido/       → contenido.html (fuente interna) + Contenido.docx (entregable final obligatorio)
│   ├── Microobjetivos/  → microobjetivos.md (fuente) + Microobjetivos.docx
│   ├── Glosario/        → glosario.md (fuente) + Glosario.docx
│   └── Actividades/     → actividades.html (fuente) + Actividades.docx o .pdf
├── EVALUACIONES/
│   ├── PARCIAL 1/
│   └── PARCIAL 2/
├── PRESENTACIONES/      → .pptx por módulo, clonados de una PLANTILLA.pptx
└── FINAL/                → Examen final integrador (si aplica)
```

Cada materia define además cuántos módulos tiene (PAI3: 7, Gestión de Proyectos Ágiles: 5) según sus contenidos mínimos oficiales — no hay un número fijo, se deriva del temario de la universidad.

## Cómo "se cuenta" la materia (índice narrativo)

Cada módulo no es una lista de temas: es una unidad con arco propio. El arco narrativo común de un módulo es el siguiente. Glosario y Actividades se mantienen como entregables separados:

1. **Apertura/gancho** — una cita (`<blockquote>`) o situación real que engancha antes de entrar en teoría.
2. **Objetivos** — los microobjetivos del módulo, presentados al principio para que el estudiante sepa a dónde va.
3. **Conceptos clave / teoría** — el desarrollo de cada tema del temario, en orden lógico (de lo general a lo específico).
4. **Sección interactiva o aplicada** — en PAI3 esto era un simulador/juego en la versión web; en un formato Word/PDF equivale a un caso resuelto paso a paso, un ejemplo numérico trabajado, o un ejercicio guiado dentro del propio contenido (no solo en Actividades).
5. **Comparaciones/tablas** — cuando hay más de un enfoque, framework o técnica, se compara en tabla, no solo en prosa.
6. **Glosario** — términos clave del módulo, aparte del contenido narrativo.
7. **Actividad formativa con guía de autoevaluación** — práctica autónoma, sin entrega ni nota; ver las reglas de Actividades más abajo.
8. **Síntesis del módulo** — cierre que resume las ideas centrales, siempre al final del contenido.

Ver [[ESTILO-EDITORIAL]] para el tono de la narrativa.

## Microobjetivos

1 a 4 por módulo, formato **verbo + contenido + finalidad**
(ej: "Comprender X para poder Y").

## Glosario

Formato `**Término**: definición de 1-3 líneas.` La cantidad de términos **no es un número fijo** (18-25 es solo orientativo para un módulo "promedio"): depende de cuánto vocabulario técnico propio introduce el módulo. Un módulo que cubre varios marcos, técnicas o herramientas (ej. Scrum + Kanban + XP + Lean) puede requerir 30+ términos sin que eso sea un problema.

Criterio de selección: cada entrada del glosario debe ser un **término técnico propio de la disciplina** —nombre de marco, práctica, métrica, rol, herramienta o sigla en inglés (Sprint, WIP, DoD, Velocity, SAFe, etc.)— nunca una palabra genérica del idioma que no necesita definirse aparte. Si un término no es jerga técnica del módulo, no va en el glosario.

## Contenido (el "libro" de cada módulo)

- HTML semántico puro como fuente (sin CSS/JS inline): un único `<h1>` por módulo, `<h2>`/`<h3>` por sección, `<p>`, `<table>`, `<ul>/<ol>`, `<blockquote>` para citas/ganchos.
- Extensión orientativa por módulo: ~9.000-11.000 palabras (~35-40 páginas exportadas). Se puede ajustar según cuántos módulos tenga la materia, para acercarse a un total razonable (PAI3 y GPA apuntaron ambos a ~200 páginas totales).
- Cierra siempre con una sección "Síntesis del módulo".

## Actividades por módulo

**Regla vigente (corrige el criterio usado en PAI3, que trataba la Actividad como un entregable calificado — no se aplica retroactivamente a PAI3, que ya está cerrada, pero sí a toda materia nueva en adelante):**

La materia es asincrónica y las Actividades **no son un entregable que el estudiante envía ni algo que se califica con rúbrica de nota**. Son práctica formativa: el estudiante las resuelve por su cuenta (mentalmente o en un borrador propio) para consolidar lo visto en el módulo, y se autoevalúa con una guía de criterios — no hay entrega, no hay corrección docente, no hay nota. La instancia formal de entrega y calificación son exclusivamente las **Evaluaciones** (parciales).

Patrón fijo de una Actividad:
- **Consigna** con un caso o escenario aplicado al tema del módulo (no abstracta), que da contexto a lo que sigue.
- **Preguntas o ejercicios guiados**, numerados: mezcla de preguntas conceptuales cortas y al menos un ejercicio aplicado (analizar un caso, resolver un problema breve, redactar una propuesta corta), todo pensado para resolverse sin necesidad de producir un archivo entregable.
- **Guía de autoevaluación**: al cierre, una lista de puntos clave que una buena respuesta debería cubrir, para que el estudiante compare su propia resolución — no una rúbrica de puntaje.
- Opcional: un "tip" o aclaración destacada para evitar errores comunes.
- **Nunca incluir**: formato de archivo de entrega, ni tabla de rúbrica con % que sume 100 (eso es exclusivo de Evaluaciones).

## Evaluaciones (parciales)

Estructura común de evaluaciones. Los elementos de portada, consignas numeradas y rúbrica se conservan entre materias; las condiciones institucionales y la distribución de puntaje deben confirmarse para cada programa. Las referencias a IA y defensa oral que siguen provienen de PAI3 y están pendientes de confirmación para Gestión y futuras materias; no tratarlas como requisitos oficiales generales:

- **Portada**: nombre del parcial, puntaje total, módulos que abarca, datos del estudiante, y reglas de modalidad (individual, uso de IA permitido pero con defensa oral, evidencia propia y original).
- **Actividades numeradas**, cada una etiquetada con el módulo de origen y su puntaje. Cada actividad se puede dividir en partes (A, B, C...) con puntaje parcial que suma el total de la actividad.
- **Rúbrica de corrección al final**, con 4 ejes fijos que se repiten en todas las evaluaciones de la materia (adaptar el nombre/contenido de cada eje al dominio, pero mantener la lógica de 4 ejes):
  1. **Concepto** — dominio del vocabulario técnico, usado en contexto (no solo nombrado).
  2. **Aplicación** — que el ejercicio/código/análisis funcione o resuelva el caso real, no solo en teoría.
  3. **Evidencia** — capturas, documentos, artefactos propios que respalden lo entregado.
  4. **Comunicación** — que la entrega sea clara, organizada y defendible oralmente.
  - Cada eje con 3 niveles de logro (completo / parcial / insuficiente).
- **Avisos finales** (cajas destacadas) aclarando: uso de IA permitido con defensa oral, formatos de entrega aceptados, y que en actividades de análisis no hay una única respuesta correcta (se evalúa el razonamiento).
- **Distribución de puntaje**: a definir según cantidad de módulos de la materia. PAI3 usó 40/60 sobre 7 módulos (Parcial 1 = módulos 1-4, Parcial 2 = módulos 5-7). Para una materia de 5 módulos conviene repensar el corte y puede convenir 50/50 en vez de 40/60.

## Contenido final en Word y fuentes internas

- El contenido se redacta primero en HTML, que funciona como fuente de verdad editorial y guía visual. El entregable final de Contenido **siempre es Word (.docx)** para Gestión de Proyectos Ágiles y las materias futuras, por decisión explícita de Pablo. HTML es fuente interna, no otro entregable.
- Para el **Word obligatorio de Contenido**, no alcanza con una conversión básica de texto. El exportador debe reproducir con la mayor fidelidad estable posible la jerarquía visual del HTML: portada, títulos, paleta, tablas, recuadros, imágenes, pies de figura, enlaces y saltos de página.
- Los elementos que Word no interpreta de manera confiable —en especial SVG inline, gradientes o composiciones complejas— se rasterizan a PNG de buena resolución durante la exportación. El cuerpo narrativo, los títulos, las listas, los enlaces y las tablas deben permanecer nativos y editables en el `.docx`.
- La conversión puede partir de `html-to-docx`, pero debe incluir el preprocesamiento y los ajustes OOXML necesarios para conservar el sistema visual. Ver `scripts/render-contenido-word.js` de Gestión de Proyectos Ágiles como patrón actualizado.
- Todo Word final debe renderizarse y revisarse visualmente después de generarlo. No se considera terminado con una validación de estructura o con la sola apertura del archivo.
- PDF no es un entregable de Contenido. Puede producirse temporalmente si el renderizador lo necesita para revisar el Word; se guarda en carpetas auxiliares y no se entrega. No mantener una edición académica paralela en PDF.
- Referencia técnica histórica de conversión a **PDF**, para otro alcance solicitado explícitamente: Playwright headless (`scripts/render-ebook-support-pdfs.js`, patrón usado en PAI3).
- El "libro completo" de la materia (todos los módulos de Contenido unidos) se arma con un script tipo `build-book.js` que concatena los HTML de cada módulo y genera un único .docx; no reemplaza los Word por módulo.

## Presentaciones (.pptx)

Se clonan desde una `PLANTILLA.pptx` reemplazando solo texto (no se generan desde cero, se preserva tema/layouts/logo del archivo original). Ver script `generate-presentaciones-plantilla.js` usado en PAI3 como referencia — portar el enfoque, no necesariamente el archivo, a cada materia nueva.

**Estructura fija por módulo: 7 slides**, patrón real usado en PAI3:

1. **Portada** — título del módulo + carrera + universidad.
2. **Apertura (slide "MÓDULO N")** — hook corto de dos líneas que anticipa qué se va a comprender/entender en el módulo.
3-6. **Cuatro slides de contenido**, cada una con:
   - `heading`: un concepto o subtema central del módulo (frase corta, no una oración larga).
   - `body`: 2 líneas — una explicativa y, en al menos una slide, una analogía o cita breve entre comillas que aterrice el concepto (ej. "El mutex es la llave del único baño del bar...").
   - `hook`: frase de transición corta que conecta con la próxima slide ("Comprenderemos...", "Nos servirá para entender...", "Analizaremos...", "Las actividades nos van a ayudar a...").
   - La última de las cuatro (slide 6) suele orientarse a la práctica/actividades del módulo ("Manos a la obra").
7. **Cierre** — slide fija de agradecimiento ("Gracias."), no se modifica por módulo.

Además del set por módulo, hay una **presentación de apertura de la materia** y una **de cierre de la materia** (además de las presentaciones por módulo), con el mismo patrón de plantilla clonada.

## Plataforma web de PAI3 (caso particular)

El trabajo exigido por la universidad son los entregables académicos finales en el formato solicitado. Las fuentes HTML/Markdown, los recursos auxiliares y las herramientas de producción no se envían automáticamente por estar dentro de `entregables/`.

PAI3 tiene una plataforma web complementaria en `SISTEMAS-INTERACTIVOS/Materia_Web/`, creada por iniciativa propia. Sus simuladores, juegos, quizzes y convenciones técnicas pertenecen a esa experiencia particular. Gestión y las materias futuras se trabajan mediante entregables; no crear plataformas ni replicar `Materia_Web/` salvo pedido explícito.

