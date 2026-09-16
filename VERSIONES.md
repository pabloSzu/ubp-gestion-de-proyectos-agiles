# Versiones de la materia

Este repositorio conserva los entregables Word, fuentes editoriales, imágenes, programa, documentación y scripts. El primer commit registra el estado actual del 15 de septiembre de 2026; no implica aprobación ni revisión definitiva de la materia.

## Trabajo habitual

1. Editar y revisar los archivos de la materia.
2. Consultar `git status` y revisar los cambios antes de guardarlos.
3. Ejecutar `git add -A` y `git commit -m "Descripción concreta del cambio"` desde esta carpeta.
4. Ejecutar `git push` para actualizar la copia remota.

Hacer un commit por una revisión coherente, por ejemplo: mejora de un módulo o actualización del programa. Los cambios sin commit todavía no forman parte del historial. Antes de recuperar una versión anterior, guardar el trabajo en curso. Para entregas institucionales se puede crear una etiqueta que identifique exactamente la versión enviada.

## Qué se conserva

- `entregables/`: archivos finales y sus fuentes y recursos.
- `Programa - contenidos.docx`, temario y documentos de revisión.
- `output/*.docx`: libro Word auxiliar.
- `scripts/`, `package.json` y `package-lock.json`: herramientas de producción.
- `docs/referencia/`: copia de las reglas compartidas y del AGENTS del workspace al crear este repositorio. En el workspace completo siguen rigiendo los originales de la carpeta superior; actualizar esta copia cuando cambien las reglas aplicables.

Dependencias, temporales, capturas de control y el HTML histórico del libro completo están excluidos mediante `.gitignore`; permanecen en el disco.

## Respaldo inicial

Antes de inicializar Git se creó una copia local en `../_RESPALDOS/GPA-2026-09-15-antes-de-git.zip`. Incluye los materiales existentes y la carpeta `antes` con los Word y HTML anteriores a la edición de contenido. Este ZIP está fuera del repositorio. La copia remota conserva los archivos incluidos en cada commit.
