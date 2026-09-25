---
subtitulo: Material para el docente. No se entrega a los estudiantes.
---

## Respuestas orientativas de las actividades

### Actividad 1

El **Product Owner** responde por el valor y por el orden del Product Backlog. Los **Developers** construyen el Incremento y deciden cómo hacer el trabajo. El **Scrum Master** ayuda a que Scrum funcione y a remover impedimentos. Los pares son Product Backlog con **Product Goal**, Sprint Backlog con **Sprint Goal** e Incremento con **Definition of Done**. El Sprint Backlog hace visible el plan del Sprint.

Registrar la respuesta sin respaldo y su causa es **transparencia**; compararla con los criterios acordados es **inspección**; corregir la causa y ajustar el plan es **adaptación**. Mostrar el problema apenas aparece requiere **apertura** y **coraje**.

La Sprint Planning acuerda el objetivo y el plan; la Daily Scrum revisa el avance hacia el Sprint Goal; la Sprint Review inspecciona el resultado con los interesados; la retrospectiva mejora la forma de trabajar. La funcionalidad con pruebas pendientes **no** forma parte del Incremento, porque no cumple la Definition of Done. La Daily Scrum **no** es un informe al Scrum Master: es una conversación entre Developers.

### Actividad 2

En curso y Validación están en su límite. No corresponde empezar otra tarjeta: conviene ayudar a validar o a conseguir el documento pendiente. Una tarjeta bloqueada sigue siendo trabajo empezado.

Política posible para entrar a Validación: la respuesta está implementada, tiene su fuente identificada y pasó las pruebas del equipo. Para pasar a Terminado: la especialista confirmó la respuesta y está publicada. El bloqueo se marca en la tarjeta con la causa, quién lo sigue y la próxima acción.

El pedido urgente necesita una clase de servicio acordada (por ejemplo, un carril urgente con un solo lugar), que haga visible qué trabajo se posterga para atenderlo.

En el caso de Microsoft cambió **cómo entraba el trabajo**: el equipo empezó a tomar un pedido nuevo recién cuando terminaba otro. **No** cambió la cantidad de personas ni la forma de programar. Eso muestra que la mejora vino de gestionar el flujo, no de trabajar más ni de sumar gente.

### Actividad 3

Integrar varias veces por día con pruebas automáticas (**integración continua**) evita que los conflictos se acumulen. Escribir primero la prueba (**TDD**) deja una red de seguridad que detecta cuando reaparece un error conocido. Trabajar en **pareja** distribuye el conocimiento de la parte difícil. **Refactorizar** mejora la estructura sin cambiar lo que hace el código.

Ciclo: **rojo**, se escribe una prueba con una consulta que menciona datos personales y se espera una derivación, y falla porque todavía no hay código; **verde**, se escribe lo mínimo para que pase; **refactorizar**, se mejora el diseño y se comprueba que todas las pruebas sigan pasando.

Que el programa no se caiga no dice nada sobre la calidad de las respuestas. Hace falta una **evaluación** con consultas conocidas y fuentes acordadas.

### Actividad 4

Las tres versiones sin consultar son **funciones extra**; la espera de cuatro días es un desperdicio de **espera**; el error en el documento produce **defectos** y retrabajo. Acciones posibles: mostrar un boceto a estudiantes antes de desarrollar, acordar con la oficina un horario fijo de validación y revisar las fuentes antes de construir las respuestas.

Reducir la espera no es lo mismo que eliminar la validación: la validación evita respuestas incorrectas. Para comprobar la mejora del sistema completo, conviene medir el tiempo total desde que se pide un cambio hasta que está publicado y validado, y la cantidad de correcciones posteriores. Acelerar la programación a costa de más errores empeoraría el conjunto.

### Actividad 5

**Scrum** puede organizar el desarrollo, **Kanban** el soporte, **XP** aporta las prácticas técnicas (integración continua, pruebas) para los errores de integración y **Lean** ayuda a detectar desperdicios. Otras elecciones pueden ser válidas si están bien justificadas.

Con límites WIP, el equipo conserva todo Scrum: responsabilidades, artefactos, eventos y compromisos. Es Scrum con Kanban. Si elimina los Sprints y sus eventos, ya no es Scrum completo; podría llamarse Scrumban, pero tendría que escribir qué reglas conserva de cada enfoque.

Adaptar el proceso al tamaño y la criticidad es **Crystal**; organizar por funcionalidades con modelado es **FDD**; fijar tiempo y costo y ajustar el alcance es **DSDM**.
