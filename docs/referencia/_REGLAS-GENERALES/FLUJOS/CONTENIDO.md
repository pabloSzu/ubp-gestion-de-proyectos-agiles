# Flujo de trabajo — Contenido de un módulo UBP

Este documento es la fuente de verdad para escribir o enriquecer el archivo de Contenido de cualquier materia. Se aplica junto con `../ESTRUCTURA-MATERIA.md` y `../ESTILO-EDITORIAL.md`; ante una contradicción, prevalecen esos dos documentos generales y la instrucción puntual del usuario.

## Entrada y alcance

La tarea debe identificar la carpeta de la materia y el número de módulo. El archivo objetivo habitual es `<MATERIA>/entregables/MODULO <N>/Contenido/contenido.html`.

Si falta un dato que impide identificar un único archivo, solicitarlo. Editar solamente el HTML de Contenido y, cuando corresponda, `IMAGENES-PROPUESTAS.md` junto a él. No modificar Microobjetivos, Glosario, Actividades, Evaluaciones, Presentaciones, exportaciones ni otros módulos salvo pedido explícito. Cuando el pedido abarque la materia completa, también pueden actualizarse el programa, la documentación y los exportadores necesarios para conservar coherencia.

## Preparación obligatoria

Antes de escribir:

1. Leer completos `ESTRUCTURA-MATERIA.md` y `ESTILO-EDITORIAL.md`.
2. Leer completo el contenido del módulo si existe, junto con el temario o documentación propia de la materia que resulte necesaria.
3. Revisar módulos vecinos para conservar convenciones de títulos, formato y profundidad.
4. Usar Gestión como referencia de estructura y diseño vigente. Para ejemplos pedagógicos o técnicos compatibles, estudiar como referencia real los HTML de `SISTEMAS-INTERACTIVOS/entregables/MODULO 1/Contenido/` y los scripts `SISTEMAS-INTERACTIVOS/scripts/enrich-contenido-modulo*.mjs` pertinentes. Tomar el nivel pedagógico, no el CSS ni `Materia_Web`.
5. Preservar cambios previos del usuario y registrar la estructura original para comprobar luego que no se haya perdido contenido.

## Dos modalidades

### Enriquecimiento de contenido existente

Conservar la narrativa válida y su sentido. No resumir ni reescribir desde cero. Integrar los recursos en puntos donde completen una relación, un razonamiento aplicado o un criterio que la prosa todavía no aporta.

Cuando el usuario solicite el patrón de enriquecimiento completo, incorporar:

- Entre 2 y 3 diagramas SVG inline para procesos, relaciones, ciclos, capas o comparaciones. Usar `<figure><svg viewBox="..." role="img" aria-label="...">...</svg><figcaption>...</figcaption></figure>`, sin CSS ni JavaScript inline. El pie debe explicar qué muestra y por qué importa.
- Un caso resuelto paso a paso, retomando una situación ya presentada. Mostrar datos o supuestos, criterio, decisiones intermedias, resultado y lectura profesional. Verificar cálculos y unidades.
- Entre 1 y 2 cajas con estructura `<div class="mito"><strong>Mito:</strong> ... <strong>Realidad:</strong> ...</div>`. La realidad debe explicar el mecanismo correcto.
- Un recuadro por sección grande con estructura `<div class="criterio-profesional"><strong>Criterio profesional:</strong> ...</div>`. Debe orientar una decisión, no resumir la sección.
- Una sección `Recursos audiovisuales sugeridos` inmediatamente antes de `Síntesis del módulo`, con 1 o 2 videos. Buscar cada video en la web, abrir el resultado y verificar URL, disponibilidad y título exacto durante la ejecución actual. Incluir una justificación específica.
- Entre 2 y 4 propuestas en `IMAGENES-PROPUESTAS.md`: qué debe mostrar cada imagen, ubicación exacta y función didáctica. No generar imágenes sin aprobación.

### Escritura desde cero

Si el archivo no existe o el usuario pide crearlo nuevamente, desarrollar el temario completo siguiendo el arco narrativo de `ESTRUCTURA-MATERIA.md`: apertura, objetivos o propósito, teoría en orden lógico, aplicación guiada, comparaciones pertinentes y síntesis final. Definir con el usuario cualquier insumo oficial ausente que pueda alterar sustancialmente el temario.

Usar HTML semántico limpio con un solo `h1`, jerarquía coherente, tablas cuando comparen dimensiones reales y `Síntesis del módulo` como último `h2`. Puede conservarse un bloque `<style>` interno común para la edición y exportación; no agregar JavaScript ni dispersar estilos en cada elemento. La extensión orientativa no es una cuota que deba rellenarse.

## Investigación y estilo

Usar búsqueda web para datos actuales, estadísticas, funcionalidades de herramientas, casos reales y videos. No inventar URLs ni presentar como hecho una afirmación que no pudo verificarse. Preferir fuentes primarias o institucionales.

Escribir en español rioplatense con voseo natural, rigor académico y tono ameno. Evitar coloquialismos e infantilización. Cada recurso agregado debe ganarse su lugar por comprensión, transferencia o criterio profesional.

## Verificación y entrega

Antes de terminar, comprobar:

- alcance de archivos respetado;
- contenido original preservado cuando se trató de un enriquecimiento;
- un solo `h1` y `Síntesis del módulo` como cierre;
- cantidades, estructura semántica y accesibilidad de los elementos pedidos;
- ausencia de atributos `style` dispersos y de JavaScript nuevo; el bloque `<style>` editorial común sí puede conservarse;
- videos abiertos y verificados en la ejecución actual;
- ninguna imagen generada sin aprobación.

Si el módulo presenta varios enfoques, comprobar además:

- cada bloque identifica por texto el contexto vigente;
- el vocabulario aparece después de su definición;
- existe una transición antes de cambiar de framework, nivel o sistema de trabajo;
- las prácticas opcionales se distinguen de las reglas obligatorias;
- la comparación y la combinación aparecen después de enseñar las alternativas por separado.

El Contenido final siempre se entrega en Word para Gestión y futuras materias. Si la tarea es solo diagnóstico o edición de fuente, indicar que la exportación final sigue pendiente. Para toda entrega de Contenido terminado, aplicar estas comprobaciones:

- usar el HTML como fuente editorial, no como entregable sustituto;
- convertir SVG y recursos complejos a imágenes de buena resolución, manteniendo el texto y las tablas editables;
- conservar portada, jerarquía cromática, imágenes, pies de figura, cajas y enlaces activos;
- renderizar el `.docx` resultante y revisar visualmente todas sus páginas o tramos antes de entregarlo;
- tratar el PDF exclusivamente como control temporal cuando el renderizador lo necesite, sin entregarlo ni mantener una edición paralela.

Informar qué se agregó o escribió por número de sección, los videos con enlace, las propuestas de imágenes y las verificaciones realizadas. No declarar completa una tarea que exigía videos si no se verificaron mediante búsqueda real.

## Revisión narrativa antes de profundizar

Cuando el pedido abarque la calidad del Contenido de una materia completa, revisar primero el recorrido entre módulos y los títulos/subtítulos de cada uno. Registrar diagnóstico, orden propuesto, cobertura pendiente de cotejo con el programa y problemas de diseño. Luego leer íntegramente y mejorar módulo por módulo. Reordenar cuando el pedido lo autorice, conservando el desarrollo válido y actualizando numeración, índice, referencias y transiciones. Una revisión de estructura no acredita una revisión editorial completa ni autoriza declarar perfectos los Word.

