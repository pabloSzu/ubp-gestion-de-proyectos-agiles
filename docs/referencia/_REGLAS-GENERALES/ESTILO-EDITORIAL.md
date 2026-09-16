# Estilo editorial — Materias UBP

Reglas de redacción y diseño que aplican a **todas** las materias dentro de `UBP-Materias/`, salvo que se indique lo contrario para una materia puntual.

## Tono de redacción

- Español rioplatense, voseo natural.
- **Nunca usar "che" ni modismos coloquiales equivalentes** ("boludo", "posta", etc.). Es contenido universitario, no una charla informal.
- Cada sección de contenido arranca con un gancho (pregunta, situación real, dato curioso) antes de explicar el concepto — nada de arrancar directo con la definición de manual.
- Explicaciones con ejemplos concretos (proyectos, código, casos reales), no solo definiciones.
- Rigor académico siempre, aunque el tono sea ameno.

## Verificación de contenido

- Usar **web search** para verificar datos, estadísticas, funcionalidades vigentes de herramientas y casos de estudio reales.
- Nunca inventar URLs (ni de videos, ni de fuentes). Si se sugiere un video de YouTube, confirmarlo con búsqueda real antes de incluirlo.

## Elementos visuales

- Tablas comparativas donde ayuden a la comprensión.
- Esquemas/diagramas: si se necesita una imagen generada (no solo HTML/tabla), pedirla explícitamente antes de seguir — no asumir que se puede generar sola.
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
- Usar analogías que aclaren un mecanismo, explicar dónde termina la comparación y volver al concepto técnico.
- Los ejemplos deben mostrar razonamiento, supuestos y consecuencias. Reutilizar un caso conductor con datos consistentes y añadir variantes cuando enseñen una diferencia relevante.
- Distinguir casos reales documentados de escenarios didácticos inventados. Cada caso real debe tener fuente, contexto y fecha; no atribuir resultados ficticios a una empresa real.
- No confundir profundidad con extensión: conservar lo necesario y reducir repeticiones, sin recortar temas oficiales ni reemplazar explicaciones por listas.
- Videos y enlaces son complementarios: el Word debe permitir estudiar los conceptos esenciales sin depender de ellos.

## Diseño del Contenido en Word

El entregable final de Contenido siempre es Word. Su diseño debe ser atractivo y facilitar el estudio, por pedido explícito de Pablo.

- Usar estilos nativos de título y subtítulos, con una jerarquía visible, colores de alto contraste y una paleta coherente. El pedido de color prevalece sobre pautas genéricas de documentos monocromáticos.
- Mantener párrafos centrados en una idea y suficiente espacio entre bloques. Usar listas nativas para pasos, criterios y enumeraciones; conservar prosa para explicar relaciones.
- Destacar conceptos con negritas selectivas. Emplear tratamientos consistentes y moderados para analogías, ejemplos, mitos y criterios profesionales; el patrón académico del proyecto prevalece sobre pautas genéricas que los excluyan.
- Tablas solo para comparar o mostrar datos. Incluir encabezados legibles, filas repetidas cuando correspondan y espacio suficiente en las celdas.
- Diagramas e imágenes con función didáctica, pie explicativo y apoyo textual. Conservar títulos y texto académico editables y accesibles; rasterizar únicamente recursos gráficos complejos.
- Comprobar en el Word renderizado la lectura real, tablas, figuras, enlaces, cortes y saltos de página. Una vista previa del HTML no valida el Word; una vista de navegador del DOCX es un control auxiliar y no sustituye la comprobación de su paginación final.
