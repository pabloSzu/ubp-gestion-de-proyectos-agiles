import fs from 'node:fs/promises';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const moduleOnePath = path.join(ROOT, 'entregables', 'MODULO 1', 'Contenido', 'contenido.html');

const moduleData = {
  2: {
    title: 'Metodologías y Marcos de Trabajo Ágiles',
    subtitle: 'Scrum, Kanban, XP y Lean como sistemas complementarios para gobernar el trabajo, el flujo y la calidad.',
    map: ['Scrum y empirismo','Responsabilidades','Eventos','Artefactos','Kanban','Límites WIP','Prácticas XP','Pensamiento Lean','Scrumban','Otros marcos','Comparación','Selección contextual'],
    criteria: [
      'Evaluá Scrum como un sistema completo: si falta transparencia, inspección o capacidad real de adaptación, cumplir ceremonias no alcanza para ejercer control empírico.',
      'Separá con precisión las decisiones de valor, de proceso y de construcción. Cuando una misma persona concentra las tres, se pierde responsabilidad clara y autonomía del equipo.',
      'Cada evento debe producir una decisión o una adaptación observable. Si una reunión no modifica el plan, el producto o la forma de trabajar, revisá su propósito antes de agregar más agenda.',
      'Un artefacto es útil solo si refleja el estado real del trabajo y su compromiso asociado orienta decisiones. Un backlog visible pero desactualizado produce una transparencia ficticia.',
      'Antes de implementar Kanban, dibujá el flujo que realmente existe, incluidas esperas y retrabajos. Un tablero idealizado oculta justamente los problemas que el método debe revelar.',
      'Elegí límites WIP para acelerar la finalización, no para mantener a cada persona ocupada. Cuando una etapa se satura, la respuesta profesional es colaborar aguas abajo antes de iniciar más trabajo.',
      'Usá XP para sostener la capacidad de cambio del producto. Sin pruebas, integración frecuente y refactorización, cada iteración agrega funcionalidad pero también aumenta el costo del próximo cambio.',
      'Buscá desperdicio en el tiempo total del sistema, no solo en la actividad de desarrollo. Las esperas, traspasos y trabajo parcialmente terminado suelen costar más que programar una funcionalidad.',
      'Adoptá Scrumban cuando exista una razón operativa concreta —por ejemplo, demanda impredecible— y definí qué conserva de Scrum y qué controla con Kanban; no lo uses como nombre para reglas ambiguas.',
      'Considerá marcos menos difundidos por el problema que resuelven, no por su etiqueta. Criticidad, tamaño, fecha fija y necesidad de modelado son variables más importantes que la popularidad.',
      'Compará enfoques por mecanismo de control, tipo de demanda y disciplina técnica. Una lista de ventajas aisladas no permite decidir qué comportamiento producirá cada opción en el sistema real.',
      'Seleccioná y combiná prácticas a partir de evidencia del contexto. Si no podés explicar qué problema resuelve cada regla adoptada, es probable que estés copiando un marco sin criterio.'
    ],
    images: [
      ['scrum-equipo-empirismo.png','Un equipo Scrum articula dirección de producto, facilitación y construcción dentro de ciclos de inspección y adaptación.','La imagen vuelve visible que Scrum coordina responsabilidades diferentes alrededor de un mismo incremento; no es una secuencia de reuniones aisladas.'],
      ['flujo-kanban-xp-lean.png','Un flujo Kanban limitado expone un cuello de botella mientras el equipo combina colaboración técnica y controles automatizados de calidad.','La escena conecta las tres capas que suelen estudiarse por separado: Kanban gestiona flujo, XP fortalece ingeniería y Lean orienta la eliminación de desperdicio.']
    ],
    videos: [
      ['A Brief Overview of the Scrum Framework','https://www.youtube.com/watch?v=gy1c4_YixCo','Scrum.org presenta en pocos minutos cómo se relacionan responsabilidades, eventos y artefactos; sirve para reconstruir el marco como sistema antes de comparar alternativas.'],
      ['What is Scrum: An Introduction to the Scrum Framework','https://www.youtube.com/watch?v=-xudUyGsNfc','La explicación oficial profundiza empirismo, roles, eventos, artefactos y mitos frecuentes, y muestra cómo Scrum puede complementarse con Kanban y prácticas técnicas.']
    ]
  },
  3: {
    title: 'Planificación Ágil y Gestión del Producto',
    subtitle: 'De la visión a la entrega: decisiones de producto trazables, backlog saludable y aprendizaje validado.',
    map: ['Visión y objetivos','Stakeholders','Roadmap','Product Backlog','Épicas y features','Historias de usuario','Criterios de aceptación','Definition of Ready','Definition of Done','Refinamiento','Priorización','MVP','Release Planning','Alcance','Cambios'],
    criteria: [
      'Formulá una visión que permita descartar opciones, no solo inspirar. Si cualquier funcionalidad puede justificarse con ella, todavía no orienta decisiones de producto.',
      'Gestioná stakeholders según la influencia que ejercen y la evidencia que aportan. Escuchar a todos no significa asignar el mismo peso a todas las opiniones.',
      'Usá el roadmap para comunicar problemas, resultados y secuencia probable. Cuanto más lejano el horizonte, menor debe ser la precisión prometida.',
      'Mantené un único backlog con orden explícito. Un ítem que nadie puede vincular con un objetivo, una necesidad o un riesgo no merece conservar prioridad por inercia.',
      'Agregá niveles de jerarquía solo cuando ayuden a coordinar escala y trazabilidad. En productos chicos, una taxonomía excesiva puede costar más que el problema que intenta resolver.',
      'Leé cada historia como una invitación a conversar sobre valor. El formato “Como… quiero… para…” no compensa una necesidad desconocida ni una solución prescripta sin evidencia.',
      'Escribí criterios que permitan observar éxito, alternativas y bordes. Si dos personas pueden probar la misma historia y llegar a conclusiones distintas, la aceptación todavía es ambigua.',
      'Usá la DoR como protección colaborativa frente a la incertidumbre evitable, nunca como una barrera burocrática para rechazar trabajo al Product Owner.',
      'La DoD debe representar calidad liberable y aplicarse sin excepciones oportunistas. Rebajarla para “cerrar” el Sprint solo desplaza costo y oculta trabajo pendiente.',
      'Refiná lo suficiente para decidir el próximo horizonte, no todo el futuro. El detalle anticipado de ítems lejanos se convierte rápidamente en inventario obsoleto.',
      'Elegí la técnica de priorización según la conversación necesaria: criticidad de alcance, satisfacción, economía de demora o relación valor-esfuerzo. Ninguna fórmula reemplaza el juicio.',
      'Definí el MVP por la hipótesis que debe poner a prueba y la evidencia que decidirá el paso siguiente. “Menos funcionalidades” no es una estrategia de aprendizaje por sí misma.',
      'Planificá releases con rangos y condiciones explícitas. Una fecha sin supuestos de velocidad, alcance y riesgo es una promesa aparente, no un pronóstico profesional.',
      'Protegé tiempo, costo y calidad mediante decisiones transparentes de alcance. Flexibilidad no significa aceptar todo, sino ordenar compensaciones de valor.',
      'Canalizá el cambio hacia el backlog y hacé visible su costo de oportunidad. La agilidad acelera decisiones; no elimina la necesidad de explicar qué se desplaza y por qué.'
    ],
    images: [
      ['vision-roadmap-backlog.png','La evidencia de distintos stakeholders se conecta con una visión, se organiza en horizontes de roadmap y desciende hacia un backlog accionable.','La imagen muestra la trazabilidad que evita dos extremos: una visión sin ejecución y un backlog de tareas sin propósito estratégico.'],
      ['refinamiento-mvp-feedback.png','Un equipo transforma necesidades de pacientes y personal clínico en historias verificables, un experimento mínimo y feedback de uso.','La escena vincula refinamiento, criterios de aceptación y MVP como partes de un mismo circuito de aprendizaje, no como documentos independientes.']
    ],
    videos: [
      ['An Introductory Video Series to Scrum: Product Backlog & Product Goal','https://www.scrum.org/resources/introductory-video-series-scrum-product-backlog-product-goal','Scrum.org explica la relación entre el objetivo de producto y el backlog, clave para evitar listas de trabajo desconectadas de la estrategia.'],
      ['Facilitating Product Backlog Refinement','https://www.scrum.org/resources/product-backlog-refinement','El recurso oficial muestra cómo facilitar conversaciones de refinamiento para crear entendimiento compartido sin convertirlas en especificación exhaustiva.']
    ]
  },
  4: {
    title: 'Estimación, Ejecución y Seguimiento del Proyecto',
    subtitle: 'Estimaciones honestas, flujo visible y métricas usadas para anticipar decisiones, no para controlar personas.',
    map: ['Estimación ágil','Story Points','Planning Poker','T-Shirt Sizes','Sprint Planning','Capacidad','Velocity','Gestión visual','Tableros','Impedimentos','Burndown','Burnup','Lead y Cycle Time','Throughput','CFD','Riesgos','Herramientas'],
    criteria: [
      'Comunicá toda estimación como un pronóstico condicionado por supuestos. La precisión debe crecer con la evidencia; una cifra exacta al inicio suele ocultar incertidumbre, no resolverla.',
      'Calibrá Story Points dentro del mismo equipo y contra historias de referencia. Convertirlos en horas o compararlos entre equipos destruye su valor como escala relativa.',
      'Usá la dispersión del Planning Poker como señal de conocimiento incompleto. El objetivo no es votar rápido, sino descubrir riesgos y supuestos antes de comprometer el trabajo.',
      'Aplicá T-Shirt Sizes cuando la conversación necesita orden de magnitud, no falsa exactitud. Refiná a una escala más fina recién cuando el trabajo se acerque a ejecución.',
      'Cerrá el Sprint Planning con un objetivo coherente, un alcance posible y un plan inicial adaptable. Una colección de historias que “cabe” pero no comparte propósito debilita el foco.',
      'Calculá capacidad con disponibilidad real y trabajo no planificable visible. Planificar sobre horas teóricas garantiza sobrecompromiso aunque la estimación de las historias sea correcta.',
      'Usá velocity para pronosticar al propio equipo y detectar cambios de estabilidad. Nunca la conviertas en meta ni ranking: en cuanto se premia el número, deja de medir entrega.',
      'Diseñá radiadores de información para provocar conversaciones y acciones. Un tablero prolijo que no revela bloqueos, envejecimiento o acumulación ofrece estética, no control.',
      'Configurá columnas según estados que cambian la responsabilidad o la política del trabajo. Agregar etapas sin una decisión asociada solo fragmenta el flujo.',
      'Escalá impedimentos por impacto y antigüedad, y registrá patrones. Resolver el mismo bloqueo cada Sprint sin atacar su causa es administrar síntomas.',
      'Leé el burndown como tendencia del trabajo pendiente, no como mandato de seguir una diagonal. Una meseta exige investigar por qué nada termina antes de exigir “más velocidad”.',
      'Preferí burnup cuando el alcance puede cambiar: separar lo completado del total evita atribuir al equipo un atraso que en realidad proviene de trabajo agregado.',
      'Medí Lead Time desde la experiencia del solicitante y Cycle Time desde el inicio activo. La diferencia revela espera sistémica que la productividad individual no explica.',
      'Interpretá throughput junto con tamaño y clase de servicio. Contar tickets sin controlar su heterogeneidad puede premiar fragmentación artificial y ocultar valor.',
      'Observá el ancho y la tendencia de las bandas del CFD. Un cuello de botella se gestiona limitando su alimentación y aumentando capacidad donde se acumula trabajo.',
      'Reducí primero los riesgos que podrían invalidar el plan. Un spike temprano compra información; dejar la mayor incertidumbre para el final compra urgencia.',
      'Elegí herramientas por la conversación y la disciplina que habilitan. Si actualizar el sistema cuesta más que la información que devuelve, la sofisticación se vuelve desperdicio.'
    ],
    images: [
      ['estimacion-colaborativa-incertidumbre.png','El equipo revela estimaciones relativas en simultáneo mientras la incertidumbre se estrecha a medida que aparece evidencia.','La ilustración subraya que Planning Poker sirve para compartir conocimiento y calibrar riesgos, no para adivinar horas exactas.'],
      ['metricas-flujo-decisiones.png','Un tablero, gráficos de avance y bandas de flujo permiten detectar un bloqueo y discutir una intervención concreta.','La imagen reúne métricas que suelen verse aisladas y muestra su propósito común: orientar decisiones tempranas sobre alcance, capacidad y cuellos de botella.']
    ],
    videos: [
      ['Story points & the evolution of agile estimation','https://www.youtube.com/watch?v=_N5gj9gzOjg','La mesa redonda de Atlassian reúne especialistas y discute por qué el esfuerzo relativo se usa para planificar bajo incertidumbre y qué límites tiene.'],
      ['Agile Estimating Explained: Story Points and Planning Poker','https://www.youtube.com/watch?v=37zfyncCpkA','Mike Cohn desarrolla comparación, puntos de historia y Planning Poker con ejemplos, ideal para consolidar el razonamiento detrás de la técnica.']
    ]
  },
  5: {
    title: 'Equipos, Liderazgo, Mejora Continua y Casos de Estudio',
    subtitle: 'La dimensión humana y organizacional que convierte los marcos ágiles en capacidad sostenida de aprendizaje y entrega.',
    map: ['Equipos ágiles','Autoorganización','Liderazgo ágil','Servant Leadership','Comunicación','Conflictos','Feedback','Stakeholders','Trabajo remoto','Sprint Review','Retrospectivas','Kaizen','Calidad','CI/CD','DevOps','Escalado','Agilidad organizacional','Casos'],
    criteria: [
      'Diseñá equipos alrededor de un flujo de valor y protegé su estabilidad. La especialización sigue siendo valiosa, pero no debería obligar a transferir cada ítem entre silos.',
      'Acordá con claridad qué decisiones puede tomar el equipo y cuáles pertenecen al producto o a la organización. La autonomía crece cuando sus límites son explícitos.',
      'Ajustá el grado de dirección a la madurez y al riesgo del contexto. Liderar ágilmente no es retirarse: es intervenir de manera que el equipo necesite cada vez menos control externo.',
      'Medí el liderazgo de servicio por impedimentos removidos, capacidades desarrolladas y decisiones habilitadas. Ser amable sin cambiar condiciones de trabajo no alcanza.',
      'Elegí el canal por la ambigüedad y urgencia del mensaje, y registrá las decisiones que deben sobrevivir a la conversación. Sin esa combinación, lo sincrónico se pierde y lo asincrónico se malinterpreta.',
      'Tratá el desacuerdo sobre ideas como insumo y el ataque personal como límite. El rol de facilitación es sostener una conversación segura sin diluir la decisión que debe tomarse.',
      'Dá feedback cerca del hecho, describiendo conducta e impacto verificable. Una valoración tardía y general produce defensa; una observación concreta permite experimentar con otro comportamiento.',
      'Construí confianza con transparencia temprana, especialmente ante riesgos. Ocultar una mala noticia para “proteger” al equipo suele multiplicar su impacto cuando finalmente aparece.',
      'Diseñá el trabajo remoto desde la asincronía y reservá el solapamiento para decisiones complejas y vínculo humano. Copiar todas las reuniones presenciales a videollamada genera fatiga, no colaboración.',
      'Llegá a la Sprint Review con preguntas que necesiten evidencia de stakeholders. Si el único resultado es mostrar lo terminado, se perdió la oportunidad de adaptar el producto.',
      'Elegí pocas acciones retrospectivas, asignales responsable y revisalas en el Sprint siguiente. Sin trazabilidad entre reflexión y cambio, la ceremonia erosiona confianza.',
      'Aplicá Kaizen mediante experimentos pequeños con una medida esperada. “Mejorar la comunicación” es una intención; probar una nueva política durante un Sprint es una intervención evaluable.',
      'Integrá calidad en la definición del flujo y hacé visible la deuda técnica. La presión de fecha no desaparece al omitir pruebas: solo traslada el costo hacia el futuro y lo vuelve menos predecible.',
      'Distinguí entrega continua de despliegue continuo y automatizá hasta el nivel que el riesgo permita. La meta es que liberar sea una decisión segura, no necesariamente automática en todos los contextos.',
      'Evaluá DevOps por el tiempo y la confiabilidad del flujo desde el cambio hasta producción. Crear un nuevo silo llamado “equipo DevOps” reproduce el problema con otro nombre.',
      'Escalá únicamente las dependencias que el diseño de equipos y producto no puede eliminar. Cada capa de coordinación debe justificar el costo de decisión que agrega.',
      'Buscá coherencia entre equipos ágiles y sistemas de presupuesto, incentivos y gobierno. La autonomía local tiene un techo cuando la organización recompensa conductas opuestas.',
      'Leé los casos por mecanismos causales, no por recetas. Identificá contexto, intervención, evidencia y efectos secundarios antes de trasladar una práctica a otra organización.'
    ],
    images: [
      ['liderazgo-servicio-equipo.png','Un equipo multidisciplinario decide en conjunto mientras un líder de servicio remueve un obstáculo del camino.','La composición desplaza al líder del centro y hace visible su aporte real: crear condiciones para la autonomía, la seguridad y el trabajo de punta a punta.'],
      ['kaizen-cicd-agilidad-organizacional.png','Retrospectiva, experimento, controles automatizados, entrega y feedback forman un circuito que conecta varios equipos con usuarios reales.','La escena integra Kaizen, CI/CD y agilidad organizacional como un único sistema de aprendizaje, en vez de presentarlos como iniciativas separadas.']
    ],
    videos: [
      ['An Introductory Video Series to Scrum: Self-Management','https://www.scrum.org/resources/introductory-video-series-scrum-self-management','Scrum.org explica por qué la autoorganización necesita apoyo del sistema organizacional y no puede reducirse a “dejar al equipo solo”.'],
      ['How to Facilitate the Sprint Retrospective','https://www.scrum.org/resources/how-facilitate-sprint-retrospective','El recurso de Scrum.org recorre técnicas concretas —Prime Directive, votación y afinidad— para convertir reflexión en acciones de mejora.']
    ]
  }
};

function esc(s) {
  return s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
}

function insertBeforeHeading(html, headingText, insert) {
  const needle = `<h2>${headingText}</h2>`;
  if (!html.includes(needle)) throw new Error(`No se encontró ${needle}`);
  return html.replace(needle, `${insert}\n\n${needle}`);
}

function addCriteria(html, criteria) {
  let index = 0;
  return html.replace(/(<h2>(?!Síntesis del módulo)[\s\S]*?<\/h2>[\s\S]*?<p>[\s\S]*?<\/p>)/g, (match) => {
    const text = criteria[index++];
    if (!text) return match;
    return `${match}\n\n<div class="criterio-profesional"><strong>Criterio profesional:</strong> ${text}</div>`;
  });
}

function imageFigure([src, alt, caption]) {
  return `<figure class="image-figure">\n<img src="assets/${src}" alt="${esc(alt)}">\n<figcaption><strong>Lectura visual.</strong> ${caption}</figcaption>\n</figure>`;
}

function videoSection(videos) {
  return `<h2>Recursos audiovisuales sugeridos</h2>\n<p>Estos recursos fueron seleccionados y verificados para profundizar los núcleos conceptuales del módulo desde fuentes especializadas.</p>\n<ul class="recursos-audiovisuales">\n${videos.map(([t,u,d]) => `<li><strong><a href="${u}">${t}</a></strong><br>${d}</li>`).join('\n')}\n</ul>`;
}

function diagramScrum() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 360" role="img" aria-label="Relación entre pilares, responsabilidades, eventos y artefactos de Scrum">
  <defs><marker id="m2a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2878a9"/></marker></defs>
  <rect x="18" y="18" width="724" height="324" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="50" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">Scrum funciona como un sistema de control empírico</text>
  <g text-anchor="middle" font-size="13" font-weight="700"><rect x="48" y="82" width="190" height="72" rx="10" fill="#eaf4fa" stroke="#2878a9"/><text x="143" y="108" fill="#173f67">Responsabilidades</text><text x="143" y="132" font-size="11" font-weight="400" fill="#536173">Producto · Facilitación · Construcción</text>
  <rect x="285" y="82" width="190" height="72" rx="10" fill="#e8f6f3" stroke="#16877b"/><text x="380" y="108" fill="#12655d">Eventos</text><text x="380" y="132" font-size="11" font-weight="400" fill="#536173">Planificar · Inspeccionar · Adaptar</text>
  <rect x="522" y="82" width="190" height="72" rx="10" fill="#f2edf8" stroke="#76549f"/><text x="617" y="108" fill="#5d3e83">Artefactos</text><text x="617" y="132" font-size="11" font-weight="400" fill="#536173">Backlogs · Incremento · Compromisos</text></g>
  <path d="M238 118 H280M475 118 H517" stroke="#2878a9" stroke-width="3" marker-end="url(#m2a)"/><rect x="170" y="205" width="420" height="82" rx="41" fill="#173f67"/><text x="380" y="234" text-anchor="middle" font-size="16" font-weight="700" fill="#fff">Transparencia → Inspección → Adaptación</text><text x="380" y="260" text-anchor="middle" font-size="12" fill="#dcebf5">evidencia visible que conduce a una decisión</text>
  <path d="M143 154 C143 188 230 190 280 213M380 154 V201M617 154 C617 188 530 190 480 213" fill="none" stroke="#16877b" stroke-width="3" marker-end="url(#m2a)"/><path d="M380 288 C380 325 90 327 90 155" fill="none" stroke="#c68a24" stroke-width="2" stroke-dasharray="7 5" marker-end="url(#m2a)"/>
  </svg><figcaption>Las responsabilidades producen decisiones, los eventos crean oportunidades de inspección y los artefactos aportan evidencia. Los tres elementos solo generan agilidad cuando alimentan el ciclo empírico completo.</figcaption></figure>`;
}

function diagramChoice() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 345" role="img" aria-label="Mapa para seleccionar Scrum, Kanban, XP, Lean o Scrumban según el problema dominante">
  <rect x="18" y="18" width="724" height="309" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="50" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">Elegí el mecanismo según el problema dominante</text>
  <line x1="105" y1="270" x2="675" y2="270" stroke="#536173" stroke-width="2"/><line x1="105" y1="270" x2="105" y2="82" stroke="#536173" stroke-width="2"/><text x="390" y="302" text-anchor="middle" font-size="12" fill="#536173">Demanda previsible ←────────────→ Demanda impredecible</text><text x="42" y="180" transform="rotate(-90 42 180)" text-anchor="middle" font-size="12" fill="#536173">Necesidad de disciplina técnica</text>
  <g text-anchor="middle" font-size="13" font-weight="700"><rect x="150" y="184" width="130" height="55" rx="9" fill="#eaf4fa" stroke="#2878a9"/><text x="215" y="217" fill="#173f67">Scrum</text><rect x="490" y="184" width="130" height="55" rx="9" fill="#e8f6f3" stroke="#16877b"/><text x="555" y="217" fill="#12655d">Kanban</text><rect x="320" y="98" width="130" height="55" rx="9" fill="#f2edf8" stroke="#76549f"/><text x="385" y="131" fill="#5d3e83">XP</text><rect x="490" y="98" width="130" height="55" rx="9" fill="#fbf2dd" stroke="#c68a24"/><text x="555" y="131" fill="#815b19">Lean</text><rect x="320" y="184" width="130" height="55" rx="9" fill="#fbeeee" stroke="#c25555"/><text x="385" y="217" fill="#9b4040">Scrumban</text></g>
  </svg><figcaption>Scrum aporta cadencia y foco cuando el trabajo puede agruparse; Kanban gobierna demanda continua; XP agrega disciplina de ingeniería; Lean ayuda a optimizar el sistema; Scrumban combina cadencia y flujo cuando ambos tipos de demanda conviven.</figcaption></figure>`;
}

function diagramProduct() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 350" role="img" aria-label="Trazabilidad desde la visión de producto hasta la evidencia de usuario">
  <defs><marker id="m3a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2878a9"/></marker></defs><rect x="18" y="18" width="724" height="314" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="48" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">De la intención estratégica al aprendizaje observable</text>
  <g text-anchor="middle"><rect x="55" y="92" width="125" height="60" rx="10" fill="#173f67"/><text x="117" y="118" font-size="14" font-weight="700" fill="#fff">Visión</text><text x="117" y="138" font-size="10" fill="#dcebf5">cambio deseado</text><rect x="230" y="92" width="125" height="60" rx="10" fill="#eaf4fa" stroke="#2878a9"/><text x="292" y="118" font-size="14" font-weight="700" fill="#173f67">Objetivos</text><text x="292" y="138" font-size="10" fill="#536173">resultado medible</text><rect x="405" y="92" width="125" height="60" rx="10" fill="#e8f6f3" stroke="#16877b"/><text x="467" y="118" font-size="14" font-weight="700" fill="#12655d">Roadmap</text><text x="467" y="138" font-size="10" fill="#536173">horizontes</text><rect x="580" y="92" width="125" height="60" rx="10" fill="#f2edf8" stroke="#76549f"/><text x="642" y="118" font-size="14" font-weight="700" fill="#5d3e83">Backlog</text><text x="642" y="138" font-size="10" fill="#536173">próxima decisión</text></g><g stroke="#2878a9" stroke-width="3" marker-end="url(#m3a)"><path d="M180 122 H225"/><path d="M355 122 H400"/><path d="M530 122 H575"/></g>
  <rect x="160" y="218" width="440" height="64" rx="12" fill="#fbf2dd" stroke="#c68a24"/><text x="380" y="244" text-anchor="middle" font-size="14" font-weight="700" fill="#815b19">Incremento + medición + feedback</text><text x="380" y="264" text-anchor="middle" font-size="11" fill="#536173">la evidencia puede cambiar backlog, roadmap y objetivos</text><path d="M642 152 C642 194 550 202 500 217" fill="none" stroke="#c68a24" stroke-width="3" marker-end="url(#m3a)"/><path d="M160 250 C72 250 72 126 52 126" fill="none" stroke="#c68a24" stroke-width="2" stroke-dasharray="7 5" marker-end="url(#m3a)"/>
  </svg><figcaption>La planificación ágil conserva trazabilidad sin congelar el futuro: cada nivel agrega detalle, y la evidencia obtenida al entregar puede obligar a revisar decisiones estratégicas previas.</figcaption></figure>`;
}

function diagramReadyDone() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 330" role="img" aria-label="Flujo de una historia desde la necesidad hasta Done con filtros de Ready y aceptación">
  <defs><marker id="m3b" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#16877b"/></marker></defs><rect x="18" y="18" width="724" height="294" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="48" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">Una historia cruza dos acuerdos de calidad diferentes</text>
  <g text-anchor="middle"><rect x="45" y="108" width="120" height="62" rx="9" fill="#eaf4fa" stroke="#2878a9"/><text x="105" y="135" font-size="13" font-weight="700" fill="#173f67">Necesidad</text><text x="105" y="154" font-size="10" fill="#536173">valor esperado</text><polygon points="230,82 315,139 230,196 145,139" fill="#fbf2dd" stroke="#c68a24" stroke-width="2"/><text x="230" y="135" font-size="13" font-weight="700" fill="#815b19">Ready</text><text x="230" y="153" font-size="10" fill="#536173">¿podemos empezar?</text><rect x="330" y="108" width="120" height="62" rx="9" fill="#f2edf8" stroke="#76549f"/><text x="390" y="135" font-size="13" font-weight="700" fill="#5d3e83">Construcción</text><text x="390" y="154" font-size="10" fill="#536173">conversación + prueba</text><polygon points="535,82 620,139 535,196 450,139" fill="#e8f6f3" stroke="#16877b" stroke-width="2"/><text x="535" y="135" font-size="13" font-weight="700" fill="#12655d">Done</text><text x="535" y="153" font-size="10" fill="#536173">¿es liberable?</text><rect x="600" y="108" width="115" height="62" rx="9" fill="#173f67"/><text x="657" y="135" font-size="13" font-weight="700" fill="#fff">Evidencia</text><text x="657" y="154" font-size="10" fill="#dcebf5">uso y aprendizaje</text></g><g stroke="#16877b" stroke-width="3" marker-end="url(#m3b)"><path d="M165 139 H180"/><path d="M315 139 H325"/><path d="M450 139 H465"/><path d="M620 139 H595"/></g><rect x="180" y="238" width="400" height="40" rx="8" fill="#fff" stroke="#c25555"/><text x="380" y="263" text-anchor="middle" font-size="12" fill="#9b4040">Ready reduce incertidumbre evitable · Done impide ocultar trabajo pendiente</text>
  </svg><figcaption>La DoR protege la entrada al Sprint y la DoD protege la salida. Los criterios de aceptación acompañan la historia entre ambos puntos y especifican el comportamiento funcional esperado.</figcaption></figure>`;
}

function diagramEstimate() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 330" role="img" aria-label="Selección de técnica de estimación según horizonte e incertidumbre">
  <rect x="18" y="18" width="724" height="294" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="48" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">La escala correcta depende de cuánto sabés y para qué decidís</text>
  <polygon points="90,92 670,92 540,260 220,260" fill="#eaf4fa" stroke="#2878a9" stroke-width="2"/><line x1="165" y1="175" x2="595" y2="175" stroke="#fff" stroke-width="3"/><g text-anchor="middle"><text x="380" y="120" font-size="14" font-weight="700" fill="#173f67">Horizonte lejano · alta incertidumbre</text><text x="380" y="148" font-size="12" fill="#536173">T-Shirt Sizes · rangos · supuestos explícitos</text><text x="380" y="205" font-size="14" font-weight="700" fill="#12655d">Próximo Sprint · entendimiento compartido</text><text x="380" y="233" font-size="12" fill="#536173">Story Points · Planning Poker · historias de referencia</text><text x="380" y="291" font-size="11" fill="#76549f">Las horas sirven para coordinar tareas cercanas; no convierten puntos relativos en duración fija.</text></g>
  </svg><figcaption>La estimación se refina al acercarse la ejecución. Pedir detalle de Sprint para trabajo lejano agrega una precisión que la evidencia todavía no puede sostener.</figcaption></figure>`;
}

function diagramMetrics() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 355" role="img" aria-label="Qué pregunta responde cada métrica ágil de avance y flujo">
  <rect x="18" y="18" width="724" height="319" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="48" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">Una métrica es útil cuando responde una pregunta de decisión</text>
  <g font-size="12"><rect x="55" y="85" width="205" height="92" rx="10" fill="#eaf4fa" stroke="#2878a9"/><text x="75" y="111" font-weight="700" fill="#173f67">Burndown / Burnup</text><text x="75" y="137" fill="#536173">¿El alcance y el avance convergen?</text><text x="75" y="157" fill="#536173">¿Cambió el total o cambió el ritmo?</text><rect x="278" y="85" width="205" height="92" rx="10" fill="#e8f6f3" stroke="#16877b"/><text x="298" y="111" font-weight="700" fill="#12655d">Lead / Cycle Time</text><text x="298" y="137" fill="#536173">¿Cuánto espera quien solicita?</text><text x="298" y="157" fill="#536173">¿Cuánto tarda el trabajo activo?</text><rect x="500" y="85" width="205" height="92" rx="10" fill="#f2edf8" stroke="#76549f"/><text x="520" y="111" font-weight="700" fill="#5d3e83">Throughput / CFD</text><text x="520" y="137" fill="#536173">¿Cuánto termina el sistema?</text><text x="520" y="157" fill="#536173">¿Dónde se acumula el trabajo?</text></g>
  <rect x="125" y="225" width="510" height="60" rx="12" fill="#173f67"/><text x="380" y="250" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">Decisión: ajustar alcance, WIP, capacidad o política</text><text x="380" y="271" text-anchor="middle" font-size="11" fill="#dcebf5">no evaluar productividad individual</text><path d="M158 177 L255 222M380 177 V222M603 177 L505 222" stroke="#c68a24" stroke-width="3"/>
  </svg><figcaption>Cada indicador ilumina una dimensión distinta. Combinarlos permite distinguir cambio de alcance, demora, variabilidad y acumulación antes de intervenir.</figcaption></figure>`;
}

function diagramTeam() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 340" role="img" aria-label="Evolución de un equipo y adaptación del liderazgo">
  <defs><marker id="m5a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2878a9"/></marker></defs><rect x="18" y="18" width="724" height="304" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="48" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">La autonomía se construye; el liderazgo cambia con el equipo</text>
  <g text-anchor="middle"><rect x="50" y="92" width="135" height="62" rx="9" fill="#eaf4fa" stroke="#2878a9"/><text x="117" y="119" font-size="13" font-weight="700" fill="#173f67">Formación</text><text x="117" y="139" font-size="10" fill="#536173">más estructura</text><rect x="225" y="92" width="135" height="62" rx="9" fill="#fbeeee" stroke="#c25555"/><text x="292" y="119" font-size="13" font-weight="700" fill="#9b4040">Conflicto</text><text x="292" y="139" font-size="10" fill="#536173">facilitación segura</text><rect x="400" y="92" width="135" height="62" rx="9" fill="#fbf2dd" stroke="#c68a24"/><text x="467" y="119" font-size="13" font-weight="700" fill="#815b19">Normalización</text><text x="467" y="139" font-size="10" fill="#536173">acuerdos propios</text><rect x="575" y="92" width="135" height="62" rx="9" fill="#e8f6f3" stroke="#16877b"/><text x="642" y="119" font-size="13" font-weight="700" fill="#12655d">Desempeño</text><text x="642" y="139" font-size="10" fill="#536173">liderazgo distribuido</text></g><g stroke="#2878a9" stroke-width="3" marker-end="url(#m5a)"><path d="M185 123 H220"/><path d="M360 123 H395"/><path d="M535 123 H570"/></g>
  <path d="M90 235 C250 190 510 190 675 235" fill="none" stroke="#76549f" stroke-width="5"/><text x="95" y="267" font-size="11" fill="#536173">Dirección y acompañamiento</text><text x="550" y="267" font-size="11" fill="#536173">Autonomía y responsabilidad</text><circle cx="90" cy="235" r="8" fill="#76549f"/><circle cx="675" cy="235" r="8" fill="#16877b"/>
  </svg><figcaption>El liderazgo situacional no abandona al equipo ni conserva control indefinidamente: aporta estructura al inicio, facilita el conflicto y transfiere decisiones a medida que crecen capacidad y confianza.</figcaption></figure>`;
}

function diagramKaizen() {
  return `<figure class="diagrama-conceptual"><svg viewBox="0 0 760 365" role="img" aria-label="Ciclo de mejora continua desde retrospectiva hasta evidencia de usuario">
  <defs><marker id="m5b" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#16877b"/></marker></defs><rect x="18" y="18" width="724" height="329" rx="16" fill="#f7f9fc" stroke="#c9d5e2"/><text x="380" y="48" text-anchor="middle" font-size="18" font-weight="700" fill="#173f67">Mejora continua: una hipótesis que debe cerrar el ciclo</text>
  <g text-anchor="middle"><circle cx="380" cy="192" r="60" fill="#173f67"/><text x="380" y="185" font-size="14" font-weight="700" fill="#fff">Aprendizaje</text><text x="380" y="207" font-size="11" fill="#dcebf5">producto + proceso</text><rect x="60" y="95" width="145" height="58" rx="9" fill="#eaf4fa" stroke="#2878a9"/><text x="132" y="122" font-size="13" font-weight="700" fill="#173f67">Observar</text><text x="132" y="141" font-size="10" fill="#536173">hechos y percepciones</text><rect x="555" y="95" width="145" height="58" rx="9" fill="#fbf2dd" stroke="#c68a24"/><text x="627" y="122" font-size="13" font-weight="700" fill="#815b19">Experimentar</text><text x="627" y="141" font-size="10" fill="#536173">cambio pequeño</text><rect x="555" y="250" width="145" height="58" rx="9" fill="#e8f6f3" stroke="#16877b"/><text x="627" y="277" font-size="13" font-weight="700" fill="#12655d">Entregar</text><text x="627" y="296" font-size="10" fill="#536173">calidad integrada</text><rect x="60" y="250" width="145" height="58" rx="9" fill="#f2edf8" stroke="#76549f"/><text x="132" y="277" font-size="13" font-weight="700" fill="#5d3e83">Medir</text><text x="132" y="296" font-size="10" fill="#536173">efecto y feedback</text></g>
  <g fill="none" stroke="#16877b" stroke-width="3" marker-end="url(#m5b)"><path d="M205 124 C330 65 445 65 550 124"/><path d="M627 153 V245"/><path d="M555 279 C450 335 320 335 210 279"/><path d="M132 250 V158"/></g>
  </svg><figcaption>Una acción de retrospectiva solo produce mejora cuando se prueba, atraviesa el flujo con calidad y se mide su efecto. El aprendizaje obtenido alimenta la siguiente decisión del equipo y de la organización.</figcaption></figure>`;
}

const diagrams = {2:[diagramScrum(),diagramChoice()],3:[diagramProduct(),diagramReadyDone()],4:[diagramEstimate(),diagramMetrics()],5:[diagramTeam(),diagramKaizen()]};

const myths = {
  2: [`<div class="mito"><strong>Mito:</strong> Scrum y Kanban son recetas rivales entre las que hay que elegir una sola. <strong>Realidad:</strong> Scrum organiza ciclos de inspección y responsabilidades; Kanban gestiona el flujo. Pueden complementarse si cada regla conserva un propósito explícito.</div>`,`<div class="mito"><strong>Mito:</strong> Poner un límite WIP reduce productividad porque deja gente sin tareas nuevas. <strong>Realidad:</strong> el límite desplaza el foco de iniciar hacia terminar y hace que el equipo ayude donde el sistema está bloqueado.</div>`],
  3: [`<div class="mito"><strong>Mito:</strong> Un roadmap ágil es un cronograma con fechas menos precisas. <strong>Realidad:</strong> comunica dirección, resultados e hipótesis por horizontes; su valor está en alinear decisiones y cambiar cuando aparece evidencia.</div>`,`<div class="mito"><strong>Mito:</strong> Un MVP es la versión barata e incompleta del producto final. <strong>Realidad:</strong> es el experimento mínimo que permite validar una hipótesis con usuarios y decidir si conviene invertir, cambiar o detenerse.</div>`],
  4: [`<div class="mito"><strong>Mito:</strong> Un Story Point equivale a una cantidad acordada de horas. <strong>Realidad:</strong> expresa tamaño relativo combinando volumen, complejidad e incertidumbre; la duración emerge del ritmo histórico del equipo.</div>`,`<div class="mito"><strong>Mito:</strong> Una velocity más alta demuestra que un equipo es más productivo. <strong>Realidad:</strong> la escala pertenece a cada equipo y puede inflarse; sirve para pronosticar su propio trabajo, no para comparar ni premiar.</div>`],
  5: [`<div class="mito"><strong>Mito:</strong> Autoorganización significa que el liderazgo deja de intervenir. <strong>Realidad:</strong> el liderazgo define contexto y límites, remueve obstáculos y desarrolla capacidades para que las decisiones migren hacia quien posee la mejor información.</div>`,`<div class="mito"><strong>Mito:</strong> Hacer retrospectivas garantiza mejora continua. <strong>Realidad:</strong> solo hay mejora cuando una observación se convierte en un experimento concreto, se prueba y se revisa con evidencia.</div>`]
};

const cases = {
  2: `<h2>Caso resuelto: elegir un enfoque para un equipo con producto e incidentes</h2><p>Un equipo de seis personas desarrolla mejoras planificadas para una plataforma de pagos, pero también recibe incidentes de producción impredecibles. Sus Sprints se interrumpen, Testing acumula trabajo y la integración manual genera defectos. La decisión no se resuelve preguntando “¿Scrum o Kanban?”, sino separando problemas.</p><ol class="caso-resuelto"><li><strong>Diagnosticar la demanda.</strong> Las nuevas funcionalidades pueden planificarse; los incidentes no. Mantener un único compromiso rígido hace que cada urgencia parezca un fracaso del Sprint.</li><li><strong>Conservar la cadencia útil.</strong> El equipo mantiene objetivo de Sprint, Review y Retrospectiva para las mejoras de producto, porque esas instancias alinean valor y aprendizaje.</li><li><strong>Gestionar el trabajo reactivo como flujo.</strong> Reserva una capacidad explícita y crea una clase de servicio urgente con política visible. Limita WIP en Desarrollo y Testing para impedir acumulación.</li><li><strong>Agregar disciplina técnica.</strong> Incorpora integración continua, pruebas automatizadas y revisión en pares para reducir el defecto que alimenta nuevos incidentes.</li><li><strong>Medir y adaptar.</strong> Durante cuatro semanas compara frecuencia de interrupciones, Cycle Time y defectos. Si la vía urgente domina, revisa capacidad o separa un servicio; si baja, ajusta el límite.</li></ol><p><strong>Decisión:</strong> un Scrumban explícito, complementado con prácticas de XP. No es una mezcla por conveniencia: cada elemento responde a un mecanismo de falla observado.</p>`,
  3: `<h2>Caso resuelto: priorizar un cambio regulatorio sin perder la estrategia</h2><p>Durante el desarrollo de TurnoYa aparece una obligación provincial: ciertas especialidades deben registrar consentimiento informado digital antes de confirmar el turno. El Product Owner debe decidir cómo incorporarla sin convertir la urgencia en caos.</p><ol class="caso-resuelto"><li><strong>Reformular el pedido como resultado.</strong> El objetivo no es “agregar una pantalla”, sino permitir que los turnos regulados queden confirmados con consentimiento trazable antes de la fecha de vigencia.</li><li><strong>Identificar stakeholders y restricciones.</strong> Se consulta a legales, personal clínico, pacientes y seguridad. Surgen requisitos de accesibilidad, auditoría y protección de datos.</li><li><strong>Dividir la épica.</strong> Se crean historias para presentar el consentimiento, capturar aceptación, conservar evidencia y contemplar rechazo o revocación, cada una con criterios verificables.</li><li><strong>Comparar costo de demora.</strong> El incumplimiento impediría operar esas especialidades; su criticidad temporal supera funcionalidades comerciales del release. El cambio sube en el backlog.</li><li><strong>Proteger el Sprint.</strong> Si la fecha permite esperar, entra al próximo Sprint ya refinado. Si debe ingresar al actual, se negocia sacar trabajo equivalente y se comunica el efecto sobre el roadmap.</li><li><strong>Definir evidencia de éxito.</strong> Además de cumplir la DoD, se mide porcentaje de consentimientos completados sin asistencia y errores de confirmación durante el piloto.</li></ol><p><strong>Resultado:</strong> la regulación cambia la prioridad, pero no saltea el sistema de producto: pasa por evidencia, refinamiento, compensación de alcance y medición posterior.</p>`,
  4: `<h2>Caso resuelto: construir un pronóstico de release con evidencia</h2><p>Un equipo debe comunicar cuándo podría terminar un backlog de 180 puntos. Sus últimas cinco velocidades fueron 28, 31, 25, 30 y 32 puntos, pero el próximo Sprint tiene una licencia planificada y existe riesgo en una integración externa.</p><ol class="caso-resuelto"><li><strong>Estimar la base empírica.</strong> El promedio de cinco Sprints es 29,2 puntos y la mediana es 30. Ambos valores muestran un ritmo cercano, con una variación relevante en el Sprint de 25.</li><li><strong>No ocultar capacidad futura.</strong> La licencia reduce disponibilidad del próximo Sprint; el equipo no usa 29 como compromiso automático y planifica menos trabajo para ese ciclo.</li><li><strong>Reducir el riesgo temprano.</strong> Antes de prometer el release, incorpora un spike breve sobre la integración externa. El resultado puede cambiar tamaño y orden del backlog.</li><li><strong>Calcular un rango.</strong> Con ritmos observados de 25 a 32 puntos, 180 puntos requieren aproximadamente entre 6 y 8 Sprints. El valor central es 180/29,2 ≈ 6,2, pero no se comunica como certeza de 6.</li><li><strong>Explicitar condiciones.</strong> El rango supone equipo estable, DoD sin cambios y alcance de 180 puntos. Un burnup permitirá distinguir avance de nuevo alcance agregado.</li><li><strong>Actualizar el pronóstico.</strong> Después de cada Sprint se recalculan trabajo restante y distribución reciente; el pronóstico mejora a medida que se estrecha la incertidumbre.</li></ol><p><strong>Comunicación profesional:</strong> “Con el alcance actual y el ritmo observado, esperamos completar en 6 a 8 Sprints; revisaremos el rango luego del spike y de cada Sprint”.</p>`,
  5: `<h2>Caso resuelto: transformar una retrospectiva repetitiva en mejora verificable</h2><p>Un equipo remoto repite hace tres Sprints la misma queja: “la comunicación con negocio falla”. La retrospectiva produce listas extensas, pero ninguna acción cambia el siguiente Sprint.</p><ol class="caso-resuelto"><li><strong>Reemplazar opiniones generales por hechos.</strong> El equipo reconstruye una línea de tiempo y encuentra cuatro historias detenidas más de dos días por criterios de aceptación ambiguos.</li><li><strong>Separar síntoma e hipótesis.</strong> El problema no parece ser “falta de comunicación” en abstracto, sino que dudas críticas se descubren después de iniciar el trabajo y no existe un canal con tiempo de respuesta acordado.</li><li><strong>Diseñar un experimento pequeño.</strong> Durante un Sprint, Product Owner y una persona de calidad revisarán criterios de las tres historias próximas; las dudas bloqueantes tendrán respuesta en la misma jornada laboral.</li><li><strong>Asignar responsabilidad y medida.</strong> El Scrum Master registra antigüedad de bloqueos; el equipo espera reducir de cuatro a no más de una las historias detenidas por ambigüedad.</li><li><strong>Proteger seguridad psicológica.</strong> Se evalúa el sistema de trabajo, no quién “comunicó mal”. Esto permite incluir al Product Owner sin convertir la retro en búsqueda de culpables.</li><li><strong>Inspeccionar en la próxima retrospectiva.</strong> Si bajan los bloqueos, la política se incorpora al acuerdo de trabajo; si no, se revisa la hipótesis y se prueba otra intervención.</li></ol><p><strong>Resultado:</strong> la mejora deja de ser una intención y se convierte en un ciclo Kaizen completo: observar, formular, probar, medir y adaptar.</p>`
};

async function enrich(moduleNumber, css) {
  const data = moduleData[moduleNumber];
  const file = path.join(ROOT, 'entregables', `MODULO ${moduleNumber}`, 'Contenido', 'contenido.html');
  let html = await fs.readFile(file, 'utf8');
  if (html.includes('<!doctype html>')) return;
  html = html.replace(/^<h1>[\s\S]*?<\/h1>\s*/i, '').replace('<blockquote>', '<blockquote class="epigraph">');
  html = addCriteria(html, data.criteria);

  const placements = {
    2: ['2. Roles en Scrum','8. Lean aplicado al desarrollo de software'],
    3: ['3. Product Roadmap','10. Refinamiento del backlog (Backlog Grooming/Refinement)'],
    4: ['2. Story Points: qué son, escala de Fibonacci, relatividad de la estimación','11. Burndown Chart: qué muestra, cómo se lee, ejemplo'],
    5: ['3. Liderazgo ágil: diferencias con el liderazgo tradicional','13. Calidad en proyectos ágiles']
  }[moduleNumber];
  html = insertBeforeHeading(html, placements[0], `${imageFigure(data.images[0])}\n\n${diagrams[moduleNumber][0]}\n\n${myths[moduleNumber][0]}`);
  html = insertBeforeHeading(html, placements[1], `${imageFigure(data.images[1])}\n\n${diagrams[moduleNumber][1]}\n\n${myths[moduleNumber][1]}`);

  const caseBefore = {2:'12. Selección del enfoque según el tipo de proyecto, equipo y contexto organizacional',3:'13. Release Planning',4:'16. Gestión de riesgos en proyectos ágiles',5:'18. Casos de estudio en gestión ágil: proyectos exitosos y desafíos comunes'}[moduleNumber];
  html = insertBeforeHeading(html, caseBefore, cases[moduleNumber]);
  html = insertBeforeHeading(html, 'Síntesis del módulo', videoSection(data.videos));

  const cover = `<header class="opener">\n  <div class="module-number">${String(moduleNumber).padStart(2,'0')}</div>\n  <div class="eyebrow">Gestión de Proyectos Ágiles · UBP</div>\n  <h1>${data.title}</h1>\n  <p class="subtitle">${data.subtitle}</p>\n  <nav class="chapter-map" aria-label="Contenidos del módulo"><div class="label">En este módulo</div><ol>${data.map.map(x => `<li>${x}</li>`).join('')}</ol></nav>\n</header>`;
  const full = `<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Gestión de Proyectos Ágiles · Módulo ${moduleNumber}</title>\n${css}\n</head>\n<body>\n<main class="page">\n${cover}\n<article class="content">\n${html.trim()}\n</article>\n</main>\n</body>\n</html>\n`;
  await fs.writeFile(file, full, 'utf8');

  const proposals = `# Imágenes del Módulo ${moduleNumber}\n\nLas siguientes ilustraciones fueron aprobadas de manera general por el usuario, generadas e incorporadas al contenido.\n\n${data.images.map(([src,alt,caption],i)=>`${i+1}. **${src}**\n   - Qué muestra: ${alt}\n   - Ubicación: ${i===0 ? `antes de «${placements[0]}»` : `antes de «${placements[1]}»`}.\n   - Valor didáctico: ${caption}`).join('\n\n')}\n`;
  await fs.writeFile(path.join(ROOT, 'entregables', `MODULO ${moduleNumber}`, 'Contenido', 'IMAGENES-PROPUESTAS.md'), proposals, 'utf8');
}

const moduleOne = await fs.readFile(moduleOnePath, 'utf8');
const css = moduleOne.match(/<style>[\s\S]*?<\/style>/)?.[0];
if (!css) throw new Error('No se pudo recuperar el sistema visual del Módulo 1.');
for (const n of [2,3,4,5]) await enrich(n, css);
console.log('Módulos 2 a 5 enriquecidos.');
