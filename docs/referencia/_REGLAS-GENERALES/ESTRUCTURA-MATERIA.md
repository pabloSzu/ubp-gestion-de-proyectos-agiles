# Estructura general de una materia — UBP

Modelo común de organización y entregables para Gestión de Proyectos y todas las materias futuras dentro de `UBP-Materias/<NOMBRE-MATERIA>/`. Gestión es la referencia vigente. PAI3 (Sistemas Interactivos) conserva su estructura histórica y se consulta solo como antecedente compatible; no se modifica retroactivamente. Ver `../README.md` para el contexto del proyecto.

## Carpetas de entregables

```
Programa.docx                 → programa general de la materia
entregables/
├── MODULO 1.. N/
│   ├── Contenido/       → contenido.html (fuente interna) + Contenido.docx (entregable final obligatorio)
│   ├── Microobjetivos/  → microobjetivos.md (fuente) + Microobjetivos.docx
│   ├── Glosario/        → glosario.md (fuente) + Glosario.docx
│   └── Actividades/     → actividades.html (fuente) + Actividades.docx o .pdf
├── EVALUACIONES/
│   ├── PARCIAL 1/       → 40 puntos, primeros contenidos
│   └── PARCIAL 2/       → 60 puntos, segunda parte
├── PRESENTACIONES/      → materia + una por módulo + cierre, hasta 7 diapositivas cada una
└── MAPA CONCEPTUAL/     → mapa general producido por Pablo de manera separada
```

En la raíz también se conservan la documentación particular, los scripts reproducibles y los auxiliares internos necesarios. El programa describe la materia completa y no se guarda dentro de un módulo.

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

Entre **4 y 6 por módulo**. Cada microobjetivo empieza obligatoriamente con un **verbo en infinitivo** y engloba un aprendizaje general del módulo. Puede seguir el formato **verbo + contenido + finalidad**, pero la finalidad no debe volverlo artificialmente largo.

Ejemplo confirmado: “Entender las distintas metodologías ágiles del mercado actual”.

## Glosario

Formato `**Término**: definición de 1-3 líneas.` La cantidad de términos **no es un número fijo** (18-25 es solo orientativo para un módulo "promedio"): depende de cuánto vocabulario técnico propio introduce el módulo. Un módulo que cubre varios marcos, técnicas o herramientas (ej. Scrum + Kanban + XP + Lean) puede requerir 30+ términos sin que eso sea un problema.

Criterio de selección: cada entrada del glosario debe ser un **término técnico propio de la disciplina** —nombre de marco, práctica, métrica, rol, herramienta o sigla en inglés (Sprint, WIP, DoD, Velocity, SAFe, etc.)— nunca una palabra genérica del idioma que no necesita definirse aparte. Si un término no es jerga técnica del módulo, no va en el glosario.

## Contenido (el "libro" de cada módulo)

- HTML semántico como fuente: un único `<h1>` por módulo, `<h2>`/`<h3>` por sección, `<p>`, `<table>`, `<ul>/<ol>`, `<blockquote>` para citas/ganchos. Puede incluir un único bloque `<style>` interno para la vista editorial y la exportación; evitar estilos repetidos en atributos y no incorporar JavaScript al contenido académico.
- Extensión orientativa por módulo: ~9.000-11.000 palabras (~35-40 páginas exportadas). Se puede ajustar según cuántos módulos tenga la materia, para acercarse a un total razonable (PAI3 y GPA apuntaron ambos a ~200 páginas totales).
- Cierra siempre con una sección "Síntesis del módulo".
- Si conviven frameworks, metodologías o prácticas, cada uno forma un bloque cerrado y rotulado. No introducir vocabulario de otro enfoque antes de explicarlo. Las comparaciones y combinaciones aparecen después de los bloques independientes.

## Actividades por módulo

**Regla vigente (corrige el criterio usado en PAI3, que trataba la Actividad como un entregable calificado — no se aplica retroactivamente a PAI3, que ya está cerrada, pero sí a toda materia nueva en adelante):**

La materia es asincrónica y las Actividades **no son un entregable que el estudiante envía ni algo que se califica con rúbrica de nota**. Son práctica formativa: el estudiante las resuelve por su cuenta (mentalmente o en un borrador propio) para consolidar lo visto en el módulo, y se autoevalúa con una guía de criterios — no hay entrega, no hay corrección docente, no hay nota. La instancia formal de entrega y calificación son exclusivamente las **Evaluaciones** (parciales).

Las Actividades pueden combinar preguntas, ejercicios guiados, casos, autoevaluaciones, prácticas en una herramienta externa, visualización de un video seguida de preguntas u otras experiencias aplicadas. Elegir el formato por su valor pedagógico y no repetir mecánicamente la misma actividad en todos los módulos.

Cuando una actividad utilice un video, enlace o herramienta externa, verificar que esté disponible y ofrecer el contexto necesario para comprender qué debe observarse o realizarse. Incluir feedback, respuestas orientativas o criterios de autoevaluación cuando la actividad sea autónoma. No usar rúbricas porcentuales: la calificación corresponde a las Evaluaciones.

## Evaluaciones (parciales)

La materia tiene exactamente dos evaluaciones parciales. La primera vale **40 puntos** y corresponde a los primeros contenidos; la segunda vale **60 puntos** y corresponde a la segunda parte. El corte concreto entre módulos se decide según el programa. Las referencias a IA y defensa oral deben confirmarse para cada materia y no se asumen por analogía con PAI3.

- **Portada**: nombre del parcial, puntaje total, módulos que abarca, datos del estudiante y reglas de modalidad que estén confirmadas para la materia.
- **Actividades numeradas**, cada una etiquetada con el módulo de origen y su puntaje. Cada actividad se puede dividir en partes (A, B, C...) con puntaje parcial que suma el total de la actividad.
- **Rúbrica de corrección al final**, con 4 ejes fijos que se repiten en todas las evaluaciones de la materia (adaptar el nombre/contenido de cada eje al dominio, pero mantener la lógica de 4 ejes):
  1. **Concepto** — dominio del vocabulario técnico, usado en contexto (no solo nombrado).
  2. **Aplicación** — que el ejercicio/código/análisis funcione o resuelva el caso real, no solo en teoría.
  3. **Evidencia** — capturas, documentos, artefactos propios que respalden lo entregado.
  4. **Comunicación** — que la entrega sea clara, organizada y defendible oralmente.
  - Cada eje con 3 niveles de logro (completo / parcial / insuficiente).
- **Avisos finales** (cajas destacadas) con formatos de entrega y condiciones confirmadas. Incluir reglas sobre IA o defensa oral únicamente si Pablo o la universidad las confirmaron para esa materia.
- **Distribución de puntaje fija**: Parcial 1 = 40 puntos; Parcial 2 = 60 puntos. Las actividades y partes de cada parcial deben sumar exactamente su total.

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

**Estructura de hasta 7 diapositivas por presentación**, basada en el patrón real usado en PAI3:

1. **Portada** — título del módulo + carrera + universidad.
2. **Apertura (slide "MÓDULO N")** — hook corto de dos líneas que anticipa qué se va a comprender/entender en el módulo.
3-6. **Cuatro slides de contenido**, cada una con:
   - `heading`: un concepto o subtema central del módulo (frase corta, no una oración larga).
   - `body`: 2 líneas — una explicativa y, en al menos una slide, una analogía o cita breve entre comillas que aterrice el concepto (ej. "El mutex es la llave del único baño del bar...").
   - `hook`: frase de transición corta que conecta con la próxima slide ("Comprenderemos...", "Nos servirá para entender...", "Analizaremos...", "Las actividades nos van a ayudar a...").
   - La última de las cuatro (slide 6) suele orientarse a la práctica/actividades del módulo ("Manos a la obra").
7. **Cierre** — cierre o agradecimiento cuando la presentación utilice siete diapositivas.

El paquete obligatorio contiene una **presentación de la materia**, **una presentación por módulo** con sus ideas principales y una **presentación de cierre de la materia**. Todas reutilizan la misma plantilla y respetan el máximo de siete diapositivas.

## Lista cerrada

El paquete obligatorio se limita al Programa, los cuatro entregables por módulo, las dos evaluaciones 40/60, las presentaciones indicadas y un mapa conceptual general producido por Pablo. No agregar examen final, plataforma web, ebook ni otros materiales salvo pedido explícito. Ver `PAQUETE-OBLIGATORIO.md`.

## Plataforma web de PAI3 (caso particular)

El trabajo exigido por la universidad son los entregables académicos finales en el formato solicitado. Las fuentes HTML/Markdown, los recursos auxiliares y las herramientas de producción no se envían automáticamente por estar dentro de `entregables/`.

PAI3 tiene una plataforma web complementaria en `SISTEMAS-INTERACTIVOS/Materia_Web/`, creada por iniciativa propia. Sus simuladores, juegos, quizzes y convenciones técnicas pertenecen a esa experiencia particular. Gestión y las materias futuras se trabajan mediante entregables; no crear plataformas ni replicar `Materia_Web/` salvo pedido explícito.

