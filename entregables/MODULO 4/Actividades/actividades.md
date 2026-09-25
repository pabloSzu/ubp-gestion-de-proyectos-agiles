---
subtitulo: Prácticas autónomas de aplicación
---

En estas actividades vas a planificar con datos, leer el avance de un Sprint, medir un flujo Kanban, representar el trabajo en una herramienta y decidir cómo usar la IA en la gestión.

:::clave Cómo usar estas actividades
- Son prácticas para vos: no se entregan y no tienen nota.
- Resolvé cada consigna en un borrador. Alcanza con papel, un documento o una planilla: no necesitás crear cuentas en ninguna herramienta.
- Todas se pueden resolver con el Contenido del módulo. Los datos de las situaciones son didácticos.
- No hay una única respuesta correcta: lo importante es que cada decisión esté fundamentada en el Contenido.
:::

## Actividad 1: Estimar y planificar un Sprint

**Qué vas a practicar:** calcular la capacidad, usar la velocidad y estimar en forma relativa.

:::caso Situación
Cuatro Developers preparan un Sprint de diez días hábiles. Cada jornada tiene ocho horas, con una hora de reuniones por cada día que la persona trabaja. Una persona tiene dos días de licencia; no hay otros descuentos. En los tres Sprints anteriores, con disponibilidad parecida entre sí, el equipo terminó 24, 27 y 21 puntos.
:::

1. Calculá la capacidad neta de cada persona y la del equipo. ¿Por qué no se descuentan reuniones en los días de licencia?
2. Calculá la velocidad promedio. ¿Podés dividir horas por puntos para obtener una equivalencia? ¿El promedio garantiza terminar lo mismo con menos disponibilidad?
3. Compará dos historias: mostrar el enlace a una fuente usando un componente que el equipo ya conoce, e integrar un repositorio externo cuya forma de acceso nadie conoce. ¿Qué conversarías sobre volumen, complejidad e incertidumbre? Si en Planning Poker aparecen un 3 y un 13, ¿qué harías? ¿Dónde usarías tallas de remera?
4. El objetivo propuesto es "permitir consultar requisitos vigentes con su fuente". Hay cuatro historias ya refinadas: A, mostrar la fuente, 5 puntos; B, consultar requisitos, 8 puntos; C, derivar consultas fuera de alcance, 5 puntos; D, personalizar colores, 8 puntos. Proponé una selección inicial y justificala.

## Actividad 2: Leer el avance de un Sprint

**Qué vas a practicar:** interpretar un burndown y un burnup.

:::caso Situación
En otro Sprint se pronosticaron 30 puntos. En el día 6 de 10, la referencia del burndown indica 12 puntos pendientes y el pendiente real es 22. Los puntos se descuentan cuando una historia cumple la Definition of Done, y hay dos historias esperando validación. Además, el burnup registra estos datos:

- **Día 1:** alcance total 30 puntos; completado 0.
- **Día 4:** alcance total 30 puntos; completado 8.
- **Día 6:** alcance total 38 puntos; completado 16.
:::

1. ¿Qué señal aporta el burndown? ¿Permite sacar conclusiones sobre el desempeño de una persona? Proponé una pregunta y una acción para la Daily Scrum.
2. En el burnup, ¿cuánto creció lo completado y cuánto el alcance entre los días 4 y 6? ¿Por qué el trabajo pendiente no bajó aunque hubo avance?
3. ¿Qué revisarías antes de sumar trabajo o recortar pruebas? Distinguí un ajuste del plan acordado con el Product Owner de un crecimiento del alcance que nadie decidió.

## Actividad 3: Medir el flujo en Kanban

**Qué vas a practicar:** calcular lead time, cycle time y throughput, e interpretar el flujo.

:::caso Situación
El soporte registra, para cada pedido, el día en que llegó, el día en que se empezó y el día en que se terminó (con validación incluida). Calculá los tiempos como diferencia entre los números de día.

- **Pedido A:** llegó el día 1, se empezó el día 3, se terminó el día 7.
- **Pedido B:** llegó el día 2, se empezó el día 5, se terminó el día 9.
- **Pedido C:** llegó el día 4, se empezó el día 4, se terminó el día 10.
:::

1. Calculá el lead time, el cycle time y la espera antes de empezar de cada pedido. Comprobá que espera más cycle time es igual a lead time.
2. Calculá el throughput entre el día 4 y el día 10 inclusive. ¿Se expresa en puntos o en pedidos?
3. Hoy hay tres tarjetas en Validación, cuyo límite es tres; una lleva cuatro días esperando una confirmación. En curso hay dos tarjetas, con límite dos. ¿Qué harías antes de empezar otra?
4. Si en el diagrama de flujo acumulado la banda de Validación se ensancha durante varios días, ¿qué investigarías? Con tres pedidos terminados, ¿podés prometer una fecha exacta para los siguientes?

## Actividad 4: Representar el trabajo en Trello y Jira

**Qué vas a practicar:** llevar el flujo a un tablero y elegir la herramienta según la necesidad.

:::caso Situación
Tenés que representar el flujo de soporte de la actividad 3 con tres tarjetas: "corregir una fecha sin fuente", que espera una fuente autorizada; "validar la respuesta sobre documentación", lista para validar; y "derivar una consulta fuera de alcance", todavía sin empezar.
:::

1. Dibujá un tablero con las columnas Por hacer, En curso, Validación y Terminado. Ubicá las tres tarjetas y anotá los límites y las políticas. La tarjeta bloqueada sigue dentro del trabajo en curso.
2. Completá una tarjeta con: título, resultado esperado, criterio de terminación, responsable del seguimiento, estado del bloqueo y próxima acción.
3. Con las imágenes y la explicación de la sección 8 del Contenido, indicá cómo representarías esa información en Trello y en Jira.
4. Elegí entre Trello y Jira para dos necesidades distintas: ver una fila pequeña de pedidos de soporte, y gestionar un backlog con Sprints y reportes. Dá dos razones para cada elección.

## Actividad 5: Pronosticar, gestionar un riesgo y usar la IA con criterio

**Qué vas a practicar:** construir un pronóstico con rangos, registrar un riesgo y decidir qué delegar en un agente de IA.

:::caso Situación
Quedan doce pedidos de soporte de tamaño parecido a los anteriores. En cuatro semanas comparables se terminaron 3, 4, 2 y 3 pedidos. Una fuente de información importante podría dejar de estar disponible. Un asistente de IA redacta este mensaje para la universidad: "Todo estará listo exactamente en cuatro semanas y ya podemos cerrar los bloqueos". Además, el equipo evalúa asignarle a un agente de IA la tarea de mover automáticamente las tarjetas a Terminado cuando detecte que una respuesta fue corregida.
:::

1. Construí un pronóstico central y un rango a partir de las semanas observadas. Aclaralo como escenarios, no como una fecha garantizada.
2. Registrá el riesgo de la fuente con su causa, impacto, señal temprana y respuesta. ¿En qué se diferencia de un bloqueo que ya ocurrió?
3. Corregí el mensaje del asistente de IA: qué dato conservarías, qué afirmación cambiarías y quién tiene que revisar el estado antes de enviarlo.
4. Aplicá las preguntas del módulo antes de delegar una tarea en un agente a la propuesta de mover tarjetas automáticamente. ¿La aprobarías tal como está? ¿Qué cambiarías? Relacionalo con la lección del caso Klarna.

## Antes de terminar

Estas actividades no tienen una única respuesta correcta: cada resolución puede ser distinta si está bien fundamentada en el Contenido del módulo. Si querés comparar tu trabajo, podés pedirle al profesor sus respuestas orientativas.

:::preguntas Para revisar tu trabajo
- ¿Tus cálculos tienen las unidades correctas (horas, puntos, pedidos, días)?
- ¿Comunicaste los pronósticos como rangos con supuestos, y no como fechas exactas?
- ¿Cada métrica que usaste llevó a una pregunta o una decisión concreta?
- ¿Mantuviste las decisiones de aceptación y prioridad en manos de personas?
:::
