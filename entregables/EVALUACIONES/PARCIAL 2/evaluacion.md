---
titulo: Producto, seguimiento del trabajo y equipos ágiles
subtitulo: Módulos 3, 4 y 5 · Total: 60 puntos
---

:::clave Datos de la evaluación
- **Contenidos:** Módulo 3 (Planificación Ágil y Gestión del Producto), Módulo 4 (Planificación y Seguimiento del Trabajo en Scrum y Kanban) y Módulo 5 (Equipos, Liderazgo, Mejora Continua y Casos de Estudio).
- **Puntaje total:** 60 puntos. Parte A: 18 puntos. Parte B: 42 puntos.
- **Modalidad:** individual.
- **Estudiante:** ______________________________________________
- **Fecha:** ____________________
:::

:::clave Condiciones
- Podés consultar el material de la materia y usar una calculadora o una planilla.
- Podés usar herramientas de inteligencia artificial como apoyo, siempre que al final declares para qué las usaste (ver el aviso del final). Lo que entregás tiene que ser tu propio razonamiento.
- Mostrá el desarrollo de los cálculos, no solo el resultado. Fundamentá cada decisión con los conceptos de los módulos.
- **Formato y medio de entrega:** a confirmar por la cátedra.
:::

## Parte A: Preguntas conceptuales (18 puntos)

Respondé cada pregunta en un párrafo breve (entre 5 y 10 líneas). Cada pregunta vale 3 puntos.

### Pregunta 1 · Módulo 3 · 3 puntos

Explicá la diferencia entre **criterios de aceptación**, **Definition of Done** y **Definition of Ready**. ¿Cuál de las tres es obligatoria en Scrum?

### Pregunta 2 · Módulo 3 · 3 puntos

¿Qué es un **producto mínimo viable (MVP)**? Explicá por qué no es "la versión barata del producto final" y dá un ejemplo de un tipo de MVP visto en el módulo.

### Pregunta 3 · Módulo 4 · 3 puntos

Distinguí **estimación**, **pronóstico** y **compromiso**. ¿Por qué conviene comunicar los pronósticos como rangos y no como fechas exactas?

### Pregunta 4 · Módulo 4 · 3 puntos

Explicá la diferencia entre **lead time** y **cycle time**. Si el lead time de un equipo es mucho mayor que su cycle time, ¿qué problema indica?

### Pregunta 5 · Módulo 5 · 3 puntos

¿Qué es la **seguridad psicológica** y por qué es importante para un equipo ágil? Relacionala con lo que encontró Google en el Proyecto Aristóteles.

### Pregunta 6 · Módulo 5 · 3 puntos

Distinguí **integración continua**, **entrega continua** y **despliegue continuo**. ¿Qué enseña el caso de Knight Capital sobre la forma de poner el software en producción?

## Parte B: Resolución de un caso (42 puntos)

Leé el caso con atención. Las cuatro actividades se basan en él.

:::caso Caso: la app del comedor universitario, segunda etapa
El comedor de la universidad atiende a unas 1.200 personas por día. La Dirección de Bienestar Estudiantil impulsa una aplicación para **consultar el menú, reservar y pagar** por anticipado, y un **modelo de inteligencia artificial que prediga la demanda** para que la cocina, a cargo de una empresa concesionaria, prepare las porciones justas y tire menos comida.

El equipo de seis personas ya definió el alcance de una primera versión y trabaja con Scrum en Sprints de dos semanas. Una vez que la app esté funcionando, los reclamos y los cambios de menú se atenderán con un tablero Kanban.

La universidad quiere que la app llegue a todas las sedes, pero todavía no está claro qué construir primero, cuándo va a estar lista ni cómo organizar al equipo, que empezó a tener algunos problemas.
:::

### Actividad 1 · Módulo 3 · Gestión del producto · 12 puntos

- **A (3 puntos).** Escribí la **visión** del producto con el formato de Geoffrey Moore visto en el módulo. Proponé un **objetivo** medible para el primer mes de uso, indicando cómo se mediría.
- **B (4 puntos).** Escribí dos **historias de usuario** para la primera versión. Para una de ellas, escribí tres **criterios de aceptación** con el formato Dado, Cuando, Entonces, incluyendo al menos un caso que no sea el "camino feliz".
- **C (3 puntos).** El equipo estimó estos valores en una escala relativa (el tamaño no representa horas):
    - **A. Reservar el menú con anticipación:** valor 13, urgencia 8, reducción de riesgo 3, tamaño 8.
    - **B. Predicción de demanda con IA para la cocina:** valor 13, urgencia 3, reducción de riesgo 8, tamaño 13.
    - **C. Avisar cuando un menú se agota:** valor 5, urgencia 5, reducción de riesgo 2, tamaño 3.
    - **D. Pago con código QR:** valor 8, urgencia 2, reducción de riesgo 1, tamaño 5.

  Calculá el **WSJF** de cada elemento como (valor + urgencia + reducción de riesgo) ÷ tamaño y ordenalos. ¿Seguirías ese orden sin cambios? Explicá qué otro criterio tendrías en cuenta.
- **D (2 puntos).** Proponé un **MVP** para comprobar si la predicción de demanda realmente reduce el desperdicio, antes de construir el modelo completo. Indicá qué tipo de MVP es y qué medirías.

### Actividad 2 · Módulo 4 · Planificación y seguimiento · 14 puntos

- **A (4 puntos).** El próximo Sprint dura diez días hábiles de ocho horas. Cada persona dedica una hora por día trabajado a reuniones. De las seis personas, una tiene cuatro días de licencia. Calculá la **capacidad neta** de cada persona y del equipo. Después, calculá la capacidad para planificar si el equipo reserva un 15 % para imprevistos.
- **B (4 puntos).** En los últimos cuatro Sprints, el equipo terminó 30, 34, 26 y 32 puntos. El backlog que falta para llevar la app a todas las sedes suma 210 puntos. Calculá la **velocidad** promedio y construí un **pronóstico** con un rango, usando el mejor y el peor Sprint. Escribí el mensaje que le darías a la Dirección de Bienestar.
- **C (4 puntos).** El soporte, gestionado con Kanban, registró estos pedidos (tiempos calculados como diferencia entre los números de día):
    - **Pedido A:** llegó el día 2, se empezó el día 4, se terminó el día 9.
    - **Pedido B:** llegó el día 3, se empezó el día 3, se terminó el día 6.
    - **Pedido C:** llegó el día 5, se empezó el día 8, se terminó el día 12.
    - **Pedido D:** llegó el día 6, se empezó el día 9, se terminó el día 11.

  Calculá el **lead time** y el **cycle time** de cada pedido y sus promedios. Calculá el **throughput** entre los días 6 y 12. ¿Qué interpretás de la diferencia entre ambos promedios?
- **D (2 puntos).** El equipo evalúa que un **agente de IA** dentro de su herramienta de gestión reordene automáticamente el Product Backlog cada semana según los reclamos recibidos. ¿Lo aprobarías? Fundamentá con las preguntas vistas en el módulo para decidir qué delegar en un agente.

### Actividad 3 · Módulo 5 · Equipo y mejora continua · 10 puntos

:::caso Situación del equipo
En el último mes aparecieron problemas. Solo una persona sabe configurar el modelo de predicción. En la Daily Scrum, cada uno le informa su avance al Scrum Master, que además asigna las tareas. Nadie se animó a decir que las predicciones de la última semana fueron muy malas. En las tres últimas retrospectivas se repitió la queja "falta comunicación con la cocina", sin ninguna acción concreta. Además, para llegar a una fecha, el equipo se salteó las pruebas automáticas en varias entregas.
:::

- **A (3 puntos).** Identificá tres problemas y relacioná cada uno con un concepto del Módulo 5 (por ejemplo, liderazgo de servicio, seguridad psicológica o equipo multifuncional).
- **B (4 puntos).** Transformá la queja repetida de las retrospectivas en un experimento de mejora con el ciclo PDCA: planificar, hacer, verificar y actuar. Indicá responsable, plazo y qué dato se va a revisar.
- **C (3 puntos).** Explicá qué **deuda técnica** generó saltearse las pruebas y cómo la gestionarías. Proponé dos criterios que agregarías a la Definition of Done, teniendo en cuenta que el producto incluye un modelo de IA.

### Actividad 4 · Módulo 5 · Análisis de un caso real · 6 puntos

Elegí **uno** de estos casos vistos en el Módulo 5: **Sentinel (FBI)**, el **modelo Spotify** o la **transformación de ING**.

- **A (4 puntos).** Describí el contexto, qué se hizo, qué resultado está documentado y qué **no** se puede concluir a partir del caso.
- **B (2 puntos).** ¿Qué lección de ese caso aplicarías al proyecto del comedor si la universidad decide llevarlo a todas sus sedes con varios equipos?

## Criterios de corrección

Cada consigna se corrige con estos cuatro ejes. El peso de cada eje depende de lo que pide la consigna.

| Eje | Completo | Parcial | Insuficiente |
|---|---|---|---|
| **Concepto:** usa el vocabulario de la materia con precisión y en contexto | Usa los conceptos con precisión y los relaciona entre sí | Usa los conceptos con errores menores | Menciona términos sin explicarlos o los usa mal |
| **Aplicación:** lleva los conceptos al caso y resuelve los cálculos | Decisiones y cálculos correctos, basados en los datos del caso | Aplica con errores menores o con poca relación con el caso | Responde en abstracto o con cálculos incorrectos |
| **Evidencia y fundamentación:** respalda cada decisión con datos, cálculos o el contenido de los módulos | Cada decisión está justificada y los cálculos muestran su desarrollo | Algunas decisiones no están justificadas | Afirma sin fundamentar |
| **Comunicación:** la respuesta es clara y ordenada | Clara, ordenada y precisa | Comprensible con algún esfuerzo | Confusa o desordenada |
Tabla: Criterios de corrección

:::ensimple No hay una única respuesta correcta
En las consignas de análisis y diseño no hay una solución única. Se evalúa la calidad del razonamiento. En las consignas con cálculos, se evalúa tanto el resultado como el desarrollo y su interpretación.
:::

:::preguntas Uso de inteligencia artificial
Podés usar herramientas de IA como apoyo: para ordenar ideas, revisar la redacción o consultar dudas. Al final de tu entrega, agregá una línea que indique qué herramientas usaste y para qué. Lo que entregás tiene que reflejar tu propio análisis del caso.
:::
