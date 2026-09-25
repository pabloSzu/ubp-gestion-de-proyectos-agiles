# Estilo editorial — Materias UBP

Reglas de redacción y diseño que aplican a **todas** las materias dentro de `UBP-Materias/`, salvo que se indique lo contrario para una materia puntual.

## Tono de redacción

- Español rioplatense, voseo natural.
- **Nunca usar "che", "quilombo" ni modismos coloquiales equivalentes** ("boludo", "posta", etc.). Es contenido universitario, no una charla informal.
- **No usar guiones (ni cortos ni largos) como puntuación dentro de la prosa** — ni para incisos ni para acotaciones. Cuando el impulso sea abrir un inciso con guion, resolverlo con punto y aparte, coma, paréntesis o una oración nueva.
- Cada sección de contenido arranca con un gancho (pregunta, situación real, dato curioso, escena cotidiana con la que cualquiera se identifique) antes de explicar el concepto — nada de arrancar directo con la definición de manual. El gancho debe poder entenderse sin conocer nada de la materia todavía: una situación humana y concreta, no un caso de uso corporativo abstracto.
- Frases cortas. Preferir dos oraciones simples a una oración larga con múltiples cláusulas subordinadas y matices encadenados. Si una idea necesita tres aclaraciones ("no significa que... tampoco implica que... aunque...") antes de decir lo que es, hay que reescribirla: primero se dice la idea de forma directa y simple, y solo después, si hace falta, se agrega el matiz en una oración aparte.
- **Los ejemplos se plantan y no se disculpan.** Nunca rotularlos "Analogía": se plantean directamente ("Imaginate…", "Pensá en…", "Por ejemplo…"). Una vez que el ejemplo explica el mecanismo, seguir adelante. No hace falta una frase que le baje el precio ("la comparación termina acá", "esto no sustituye..."): si la analogía es buena, el lector entiende solo hasta dónde llega. Reservar la aclaración únicamente para cuando la comparación pueda inducir a un error concreto y grave.
- Dirigirse al lector en segunda persona con naturalidad ("vos", "te va a pasar", "pensalo como"), no en tercera persona impersonal todo el tiempo.
- Se puede usar humor liviano y observación cotidiana con moderación, sin infantilizar ni perder rigor. El humor entra por la situación o el ejemplo, no por chistes forzados ni exclamaciones.
- Explicaciones con ejemplos concretos (proyectos, código, casos reales), no solo definiciones.
- Rigor académico siempre, aunque el tono sea simple, ameno y directo. Simple no es impreciso: es decir lo mismo con menos rodeos.

## Ejemplos cotidianos y casos reales

Criterio acordado con Pablo el 25 de septiembre de 2026, después de que un borrador con demasiados ejemplos cotidianos (algunos forzados) resultara peor que uno con casos reales.

- **Pocos ejemplos cotidianos, muy bien elegidos.** Solo cuando aclaran un concepto mejor que cualquier otra cosa y la relación es evidente. Orientativo: 4 a 6 por módulo. Si un ejemplo necesita explicarse para que se entienda la relación, sobra.
- **Más casos reales documentados.** Proyectos, empresas u organizaciones reales con datos concretos (fechas, cifras, qué pasó) que muestran las consecuencias de un concepto. Orientativo: 5 a 8 por módulo. Cada uno se verifica con búsqueda web y lleva la fuente al final del recuadro.
- **Casos conocidos o cercanos a la carrera.** Preferir casos que el estudiante reconozca o que se relacionen con su orientación (por ejemplo, IA en Ingeniería en IA). Combinar éxitos y fracasos.
- **Sin repetir casos entre módulos.** Registrarlos en la `GUIA-CONTENIDO.md` de la materia.
- **Ejemplos genéricos, sin detalles personales innecesarios.** "El cumpleaños de un familiar" antes que "el cumpleaños de 15 de tu prima".
- **Cada caso o ejemplo se presenta antes de usarlo.** Si un caso reaparece en otra sección, retomarlo con una frase que lo ubique ("el asistente universitario que presentamos al comienzo").
- **Nada se nombra antes de presentarlo.** La primera vez que aparece una sigla, un marco o una herramienta, se la presenta con una frase breve ("Jira, una de las herramientas de gestión de backlog más usadas hoy"; "SAFe, un marco para coordinar muchos equipos"), aunque se desarrolle en otro módulo. Tampoco se usa en un rótulo o recuadro un término que se explica recién más adelante.
- **Cada concepto de una clasificación se explica por separado.** Si se presentan niveles o tipos (épica, historia, tarea), cada uno lleva qué es, en qué se diferencia de los demás y un ejemplo; la tabla resume, no reemplaza la explicación.
- **Títulos de sección claros y descriptivos.** "Qué incluye el proyecto y qué no" antes que "Adentro y afuera".

## Verificación de contenido

- Usar **web search** para verificar datos, estadísticas, funcionalidades vigentes de herramientas y casos de estudio reales.
- Nunca inventar URLs (ni de videos, ni de fuentes). Si se sugiere un video de YouTube, confirmarlo con búsqueda real antes de incluirlo.

## Elementos visuales

- Tablas comparativas donde ayuden a la comprensión.
- Esquemas/diagramas: si se necesita una imagen nueva, describirla en `IMAGENES-PROPUESTAS.md` y pedir aprobación antes de generarla.
- Videos sugeridos: 1-2 por módulo, relevantes, verificados con búsqueda real, con título + link + una línea de por qué se recomienda.

## Contraste y legibilidad (para versión web)

- Textos dentro de cards: `var(--text)`, no `var(--sub)`.
- Labels pequeños (uppercase tracking): `var(--sub)` está bien.
- `var(--muted)` solo para decorativo, nunca para texto legible.
- Tamaño de fuente mínimo en cards: 14px.

Ver también [[ESTRUCTURA-MATERIA]] para cómo se organiza el contenido en módulos y entregables.

## Narrativa y profundidad del Contenido

- Cada materia conecta sus módulos en una progresión de preguntas y capacidades. Dentro del módulo, enseñar los fundamentos que permiten entender una práctica antes de detallar sus mecanismos.
- Abrir con una situación y explicar qué se va a aprender. Conectar secciones con transiciones que expliciten por qué el próximo tema resulta necesario.
- Desarrollar conceptos gradualmente, definir vocabulario nuevo y no asumir conocimientos que todavía no se enseñaron.
- Usar ejemplos cotidianos que aclaren un mecanismo y volver al concepto técnico. Plantearlos directamente ("Imaginate…", "Por ejemplo…"), sin rotularlos "Analogía" y sin frases que expliquen dónde termina la comparación.
- Los ejemplos deben mostrar razonamiento, supuestos y consecuencias. Reutilizar un caso conductor con datos consistentes y añadir variantes cuando enseñen una diferencia relevante.
- Distinguir casos reales documentados de escenarios didácticos inventados. Cada caso real debe tener fuente, contexto y fecha; no atribuir resultados ficticios a una empresa real. No escribir fechas de consulta en el cuerpo del texto.
- No confundir profundidad con extensión: conservar lo necesario y reducir repeticiones, sin recortar temas oficiales ni reemplazar explicaciones por listas.
- Videos y enlaces son complementarios: el Word debe permitir estudiar los conceptos esenciales sin depender de ellos.

## Contexto pedagógico y separación de enfoques

- Cuando una materia incluya varios frameworks, metodologías, niveles de análisis o herramientas, indicar explícitamente de cuál se habla. No confiar solamente en que el estudiante lo deduzca por el título anterior.
- Usar etiquetas textuales consistentes, por ejemplo: **Concepto general**, **Contexto: Scrum**, **Contexto: Kanban**, **Práctica complementaria**, **Herramienta** o **Caso de IA**. El color acompaña; la etiqueta escrita conserva el significado al imprimir en escala de grises.
- Cerrar un bloque antes de abrir otro y agregar una transición breve que explique qué cambia. Evitar alternar roles, eventos o métricas de distintos enfoques dentro de una misma secuencia sin advertencia.
- Comparar o combinar únicamente después de enseñar cada alternativa por separado. Aclarar qué reglas se conservan, cuáles cambian y qué problema resuelve la combinación.
- Si una técnica es frecuente pero no obligatoria en un framework, decirlo de manera explícita. Una herramienta tampoco equivale al método que puede representar.

## Diseño del Contenido en Word

El entregable final de Contenido siempre es Word. Su diseño debe ser atractivo y facilitar el estudio, por pedido explícito de Pablo.

- Usar estilos nativos de título y subtítulos, con una jerarquía visible, colores de alto contraste y una paleta coherente. El pedido de color prevalece sobre pautas genéricas de documentos monocromáticos.
- Mantener párrafos centrados en una idea y suficiente espacio entre bloques. Usar listas nativas para pasos, criterios y enumeraciones; conservar prosa para explicar relaciones.
- Destacar conceptos con negritas selectivas. Emplear recuadros de color consistentes para ejemplos cotidianos, ideas clave, resúmenes "en simple", preguntas prácticas, mitos y casos resueltos. No usar recuadros de "Criterio profesional".
- Cuando se solicite énfasis cromático, aplicar color oscuro de alto contraste y negrita a palabras clave, con moderación. No limitar el color a títulos ni colorear párrafos completos; conservar significado comprensible también en impresión sin color.
- Tablas solo para comparar o mostrar datos. Incluir encabezados legibles, filas repetidas cuando correspondan y espacio suficiente en las celdas.
- Diagramas e imágenes con función didáctica, pie explicativo y apoyo textual. Conservar títulos y texto académico editables y accesibles; rasterizar únicamente recursos gráficos complejos.
- Comprobar en el Word renderizado la lectura real, tablas, figuras, enlaces, cortes y saltos de página. Una vista previa del HTML no valida el Word; una vista de navegador del DOCX es un control auxiliar y no sustituye la comprobación de su paginación final.
