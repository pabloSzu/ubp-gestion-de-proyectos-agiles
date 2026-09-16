# Versionado y entrega de materias UBP

Cada materia nueva debe conservar sus fuentes, entregables finales, recursos, programa, documentación y scripts reproducibles en un repositorio Git propio o claramente delimitado.

## Trabajo habitual

1. Crear un respaldo antes de una migración o edición amplia.
2. Trabajar con cambios locales mientras se revisa el resultado.
3. Consultar `git status`, revisar diferencias y ejecutar los controles del entregable.
4. Hacer un commit por hito coherente únicamente cuando Pablo lo solicite o autorice para esa etapa.
5. Hacer push después del commit autorizado y verificar el remoto.
6. Etiquetar las versiones efectivamente enviadas a la universidad cuando resulte útil.

No usar `git reset --hard`, limpiar archivos no versionados ni sobrescribir fuentes sin respaldo. No mezclar en un mismo commit cambios de materias distintas.

## Qué versionar

- fuentes editoriales;
- Word y PowerPoint finales;
- recursos utilizados;
- programa y documentación;
- mapa conceptual general proporcionado por Pablo;
- scripts y archivos de dependencias necesarios para regenerar;
- README con estado y pendientes.

Excluir dependencias instaladas, temporales, cachés y capturas de control, salvo que una evidencia concreta deba conservarse. Los archivos auxiliares no se presentan como entregables académicos.

## Entrega institucional

Antes de enviar, identificar exactamente cuáles archivos son entregables. Conservar la versión enviada mediante commit y, si se acuerda, una etiqueta. Registrar fecha, alcance y cualquier limitación conocida. PDF, HTML, reportes de QA y libros auxiliares solo se incluyen si fueron solicitados.
