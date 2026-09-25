---
subtitulo: Material para el docente. No se entrega a los estudiantes.
---

## Respuestas orientativas de las actividades

### Actividad 1

Tres personas tienen 10 × 7 = **70 horas** cada una; la persona con licencia, 8 × 7 = **56 horas**. Total: **266 horas**. Las reuniones solo se descuentan los días que la persona trabaja: descontar reuniones también en la licencia restaría dos horas de más.

La velocidad promedio es (24 + 27 + 21) ÷ 3 = **24 puntos**. Horas y puntos no son equivalentes: los puntos son una escala relativa. El promedio es una referencia que hay que contrastar con la disponibilidad real; con menos gente disponible, conviene seleccionar menos.

La integración desconocida tiene mucha más incertidumbre: antes de estimarla hay que aclarar cómo se accede al repositorio, quizás con un *spike*. Ante un 3 y un 13, quienes votaron los extremos explican sus razones y se vuelve a votar; no se promedia. Las tallas de remera sirven para el trabajo lejano o todavía poco definido.

A + B + C suman **18 puntos**, son coherentes con el objetivo y quedan por debajo de la velocidad promedio, lo que deja margen. D suma 8 puntos y no aporta al objetivo. La selección es un pronóstico; el compromiso es el Sprint Goal.

### Actividad 2

El burndown muestra más trabajo pendiente que la referencia: el objetivo puede estar en riesgo. No explica la causa ni dice nada sobre personas. Pregunta posible: "¿Qué hace falta para validar las dos historias que están esperando?". Acción: ayudar a validar antes de empezar trabajo nuevo.

Entre los días 4 y 6, lo completado creció **8 puntos** (de 8 a 16) y el alcance también creció **8 puntos** (de 30 a 38). El pendiente quedó en **22** en los dos días: hubo avance, pero entró la misma cantidad de trabajo nuevo.

Antes de decidir, hay que revisar si el trabajo agregado es necesario para el Sprint Goal. Un ajuste acordado con el Product Owner es visible y protege el objetivo; un crecimiento que nadie decidió es expansión descontrolada del alcance. Recortar pruebas nunca es la solución.

### Actividad 3

**A:** lead time 6, cycle time 4, espera 2. **B:** lead time 7, cycle time 4, espera 3. **C:** lead time 6, cycle time 6, espera 0. En los tres casos se cumple la suma.

Entre los días 4 y 10 se terminaron **3 pedidos**. El throughput se expresa en **pedidos**, no en puntos.

Con las dos columnas en su límite, no se empieza nada nuevo: se ayuda a destrabar la validación, empezando por la tarjeta que lleva cuatro días esperando.

Una banda de Validación que se ensancha indica que ahí se acumula trabajo: hay que investigar la capacidad de validación, los bloqueos y las políticas. Tres pedidos son muy pocos datos para prometer una fecha exacta.

### Actividad 4

"Corregir una fecha sin fuente" va en **En curso**, marcada como bloqueada; "validar la respuesta" va en **Validación**; "derivar una consulta" va en **Por hacer**. Criterio de terminación posible: "la fecha está contrastada con la fuente vigente, la respuesta fue corregida y la oficina la validó". En la tarjeta se anota quién sigue el bloqueo y cuándo se revisa.

En Trello, las columnas son listas y los datos de la tarjeta van en su descripción, etiquetas y lista de verificación. En Jira, la tarjeta es un elemento del flujo con campos, estados y responsable, y el bloqueo puede marcarse con una etiqueta o un vínculo.

Para una fila pequeña de soporte, **Trello** alcanza: es simple y rápido de configurar. Para un backlog con Sprints y reportes, **Jira**: tiene Sprints, tipos de elementos y reportes automáticos. En los dos casos, la herramienta no reemplaza las políticas del equipo.

### Actividad 5

El promedio es 3 pedidos por semana: 12 ÷ 3 = **4 semanas** como pronóstico central. Con la mejor semana (4) serían **3 semanas**; con la peor (2), **6 semanas**. Mensaje posible: "Con el ritmo actual, esperamos terminar en 3 a 6 semanas, siempre que no entren pedidos nuevos ni aparezcan bloqueos importantes".

Riesgo: la fuente deja de estar disponible. Impacto: no se pueden validar respuestas. Señal temprana: fallas de acceso o aviso de retiro. Respuesta: acordar una fuente alternativa autorizada y derivar las consultas sin respaldo. Si la fuente ya no está disponible y frena un pedido, deja de ser un riesgo y pasa a ser un bloqueo.

Del mensaje de la IA se puede conservar el cálculo de 4 semanas, pero como pronóstico con rango. Hay que quitar "exactamente" y "cerrar los bloqueos": los bloqueos se cierran cuando alguien comprueba que se resolvieron. Una persona del equipo revisa el mensaje antes de enviarlo.

La propuesta del agente no conviene tal como está: marcar algo como Terminado es **aceptar un resultado**, y esa decisión es de una persona. Además, un error sería difícil de detectar. Alternativa: que el agente **proponga** mover la tarjeta y una persona lo confirme, con permisos limitados y registro de lo que hizo. Klarna mostró que medir solo la cantidad de trabajo que hace la IA puede ocultar problemas de calidad.
