# Cómo hacer una materia nueva, paso a paso

Guía práctica para producir el paquete completo de una materia UBP con el método que se usó en Gestión de Proyectos Ágiles (septiembre de 2026). Las reglas de detalle de cada entregable están en `FLUJOS/`; esta guía dice **en qué orden** hacer las cosas, **con qué comandos** y **qué errores evitar**.

Materia de referencia: `GESTION-PROYECTOS-AGILES/`. Ante la duda, mirar cómo quedó ahí.

## 1. Preparar la carpeta

1. Crear `UBP-Materias/<NOMBRE-MATERIA>/` con la estructura de `ESTRUCTURA-MATERIA.md`:
   `entregables/MODULO 1..N/{Contenido,Glosario,Microobjetivos,Actividades}`, `entregables/EVALUACIONES/PARCIAL 1` y `PARCIAL 2`, `entregables/PRESENTACIONES`, `scripts/`.
2. Copiar desde `GESTION-PROYECTOS-AGILES/scripts/` estos dos archivos: `md-a-word.py` y `render-contenido-word-nativo.py`. Son el generador de todos los Word. En `md-a-word.py`, la materia se toma del encabezado `materia:` de cada `contenido.md`; en evaluaciones está escrita en el código (buscar `'materia': 'Gestión de Proyectos Ágiles'` y cambiarla).
3. Copiar `PLANTILLA-GUIA-CONTENIDO.md` como `<MATERIA>/GUIA-CONTENIDO.md`.
4. Opcional: `git init` en la carpeta de la materia y crear un repositorio propio, como el de Gestión.

## 2. Reunir lo que da la universidad

- Contenidos mínimos o programa oficial. Si solo hay mínimos, se arma el programa a partir de ellos (`FLUJOS/PROGRAMA.md`).
- Carrera a la que pertenece: orienta los ejemplos y el caso conductor (en Gestión, Ingeniería en IA).
- Cantidad de módulos.

Preguntarle a Pablo solo lo que falte y no inventar datos institucionales.

## 3. Orden de trabajo

Cada paso se cierra con la revisión de Pablo antes de seguir.

1. **Guía central** (`GUIA-CONTENIDO.md`): mapa de temas por módulo (qué va en cada uno y con qué profundidad), caso conductor y lista de casos reales. Evita repeticiones entre módulos y es lo que más tiempo ahorra después.
2. **Contenido, un módulo por vez.** Escribir `contenido.md`, generar el Word, revisarlo en páginas y esperar el visto bueno de Pablo. Después del primer módulo aprobado, los demás salen mucho más rápido porque el estilo ya quedó calibrado.
3. **Microobjetivos** (hasta 4, cortos), **Glosario** y **Actividades** de los cinco módulos, derivados del Contenido terminado.
4. **Evaluaciones**: antes de escribir, preguntar a Pablo el corte de módulos, el formato (preguntas, caso o mixto), la modalidad y la política de IA y defensa oral.
5. **Presentaciones** (plantilla común, hasta 7 diapositivas).
6. **Mapa conceptual**: lo genera Pablo; no crearlo.

## 4. Del Markdown al Word

Todo se escribe en Markdown y se convierte a Word con un solo comando, desde la carpeta de la materia:

```text
python scripts/md-a-word.py --modulo N                      → Contenido.docx
python scripts/md-a-word.py --modulo N --tipo actividades   → Actividades.docx
python scripts/md-a-word.py --modulo N --tipo respuestas    → Respuestas-docente.docx
python scripts/md-a-word.py --modulo N --tipo glosario      → Glosario.docx
python scripts/md-a-word.py --modulo N --tipo microobjetivos → Microobjetivos.docx
python scripts/md-a-word.py --parcial N --tipo evaluacion   → Evaluacion.docx
python scripts/md-a-word.py --parcial N --tipo guia         → Guia-docente.docx
```

- **Python que funciona en esta computadora:** `C:/Users/Pablo/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe` (tiene python-docx, lxml, Pillow y pypdfium2). El `python` del sistema no tiene esas librerías.
- **Revisión visual:** convertir el Word a PDF con LibreOffice (`"C:/Program Files/LibreOffice/program/soffice.exe" --headless --convert-to pdf archivo.docx --outdir carpeta-temporal`) y mirar las páginas como imagen (pypdfium2). El PDF es solo para control: no se guarda en `entregables/`.
- **Sintaxis de la fuente** (encabezado, títulos, tablas con `Tabla:`, imágenes, listas anidadas con 4 espacios, citas con `> `, recuadros `:::tipo`): ver `FLUJOS/CONTENIDO.md`.

## 5. Lo que aprendimos (y conviene no repetir)

**Sobre el estilo** (detalle en `ESTILO-EDITORIAL.md`):

- Pocos ejemplos cotidianos (4 a 6 por módulo) y más **casos reales verificados** con fuente (5 a 8). Un borrador lleno de analogías forzadas fue rechazado.
- Nunca rotular "Analogía" ni usar recuadros de "Criterio profesional".
- Nada se nombra antes de presentarlo: siglas, herramientas y marcos llevan una frase de presentación la primera vez.
- Los conceptos centrales tienen sección propia y profunda; en una clasificación, cada nivel se explica por separado.
- Ejemplos genéricos ("un familiar"), títulos claros, sin fechas de consulta en el texto, sin guiones como puntuación.
- Un solo caso conductor para toda la materia, presentado en un recuadro al inicio del Módulo 1.
- No agregar diagramas ni imágenes por iniciativa propia: Pablo genera las imágenes. Proponerlas en `IMAGENES-PROPUESTAS.md`.

**Sobre los entregables:**

- Las respuestas de las actividades **no van en las actividades**: van en `respuestas-docente.md`, y las actividades terminan con una nota para pedírselas al profesor.
- Microobjetivos: hasta 4, de una línea.
- Evaluaciones: 40 y 60 puntos; verificar las sumas con un script; guía docente siempre en un archivo aparte.

**Sobre el proceso:**

- **Word abierto = no se puede guardar.** Si Pablo tiene el `.docx` abierto, el generador falla con "Permission denied": pedirle que lo cierre o generar con `--salida` en otra ruta.
- **Si Pablo edita el Word a mano**, pasar el cambio al `.md`; si no, se pierde en la próxima generación. LibreOffice pregunta el formato al guardar: elegir "Documento de Word".
- Verificar en la web todo dato, cifra, caso y enlace antes de escribirlo.
- Respaldar los archivos anteriores en `.qa/<tarea>-<fecha>/antes/` antes de reemplazarlos.
- Commit y push solo cuando Pablo lo pide, en una rama propia (no directo a `main`).
- Al cerrar cada etapa, actualizar el README de la materia y, si surgió una regla reutilizable, estas reglas generales (y la copia en `docs/referencia/` de la materia, si existe).
