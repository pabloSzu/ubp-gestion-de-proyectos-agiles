---
subtitulo: Material para el docente. No se entrega a los estudiantes.
---

## Respuestas orientativas de las actividades

### Actividad 1

Visión posible: "Para estudiantes que necesitan conocer los requisitos de inscripción vigentes, el asistente es un servicio de consultas en la web que responde con información oficial e indica su fuente. A diferencia de buscar en documentos dispersos, responde al instante y deriva a una persona cuando no está seguro."

Comunicado posible: "Ahora podés resolver tu inscripción en minutos. El nuevo asistente de la universidad responde tus dudas con la información oficial y te dice de dónde sale cada dato."

La **línea de base** es 10 de 20, el 50 %. Una **meta** posible es que 16 de 20 participantes de una prueba comparable encuentren la información correcta sin ayuda al final del piloto. Es una meta propuesta, no un resultado.

Métrica de beneficio: porcentaje de estudiantes que completan la tarea sin ayuda. Métrica de calidad: porcentaje de respuestas correctas y con fuente. Cargar documentos solo informa actividad. Roadmap posible: **ahora**, inscripciones; **próximo**, corregir las dificultades observadas; **después**, explorar becas. Para avanzar hace falta evidencia de utilidad y calidad, no solo que llegue una fecha.

### Actividad 2

Épica posible: consultas sobre inscripciones. Funcionalidad: requisitos de inscripción. Historias: "Como estudiante, quiero conocer los requisitos de inscripción de mi carrera, para preparar la documentación a tiempo" y "Como estudiante, quiero que el asistente me avise cuando no tiene la respuesta, para saber a quién consultar". Tarea: conectar el reglamento vigente.

INVEST obliga a revisar si la historia es independiente, negociable, valiosa, estimable, pequeña y testeable. Si falta conocer la fuente, no es estimable; si no hay criterios, no es testeable.

Criterios posibles: **dado** un trámite con fuente vigente, **cuando** consulto, **entonces** veo los requisitos y el enlace oficial; **dado** que no hay fuente vigente, **cuando** consulto, **entonces** el asistente me lo informa y me deriva; **dado** que consulto algo fuera del piloto, **cuando** pregunto, **entonces** me informa el alcance y el canal de atención.

El enlace (a) es un **criterio de aceptación**; las pruebas y la revisión (b) forman parte de la **Definition of Done**; conocer la fuente antes (c) puede ser parte de la **Definition of Ready**. Si una historia cumple sus criterios pero no la Definition of Done, **no está terminada** y no forma parte del incremento.

### Actividad 3

A y C son **Must have**, por las condiciones del piloto. B puede ser **Could have** y D **Won't have this time**. Una categoría no define el orden dentro de ella.

WSJF: A = 21 ÷ 3 = **7**; B = 4 ÷ 2 = **2**; C = 21 ÷ 3 = **7**; D = 10 ÷ 5 = **2**. A y C empatan, igual que B y D. Para desempatar sirven las dependencias (por ejemplo, si derivar requiere primero saber cuándo no hay fuente) o la evidencia de los usuarios. Un número no reemplaza el criterio.

En la matriz, A tiene mucho valor y poco esfuerzo (victoria rápida); B, poco valor y poco esfuerzo (relleno); D, valor medio y más esfuerzo. Que algo sea chico no lo vuelve prioritario.

Kano requiere preguntar a los usuarios. Una hipótesis razonable es que la información correcta sea una característica **básica**: nadie la valora cuando está, pero su ausencia genera mucha insatisfacción. Se comprueba con una encuesta que pregunte cómo se sentiría el estudiante si la característica estuviera y si faltara.

### Actividad 4

Hipótesis: "Los estudiantes van a resolver sus consultas de inscripción con el asistente en lugar de escribir a la oficina". Incluir: consultas de inscripción, fuentes, derivación y observación del uso, en una sola carrera. Dejar afuera: becas e inscripción automática. Observar: respuestas correctas, tareas completadas sin ayuda y consultas que igual llegan a la oficina. El criterio para decidir se fija antes de empezar.

Un MVP **conserje** permite que una persona responda por el chat durante una semana para aprender qué preguntan los estudiantes, como Zappos comprobó la demanda comprando cada par a mano antes de invertir en stock (en su caso, un MVP tipo mago de Oz). Si se usa, hay que avisar que es un piloto y proteger los datos.

Lanzamiento posible: primero una carrera durante una inscripción; si se cumplen los criterios, todas las carreras en la siguiente. HealthCare.gov mostró que habilitar un sistema para todos el mismo día, sin comprobar que esté listo, puede hacerlo colapsar.

La inscripción automática cambia los riesgos: acceso a datos personales, permisos e integración con otros sistemas. Conviene registrarla en el backlog e investigarla (por ejemplo, con una investigación acotada) antes de prometerla. En el roadmap puede ir en "después", sujeta a lo que se aprenda. Aceptar una necesidad no obliga a empezarla de inmediato.
