# Guía central del Contenido

Archivo de referencia para escribir y revisar el Contenido de los cinco módulos de Gestión de Proyectos Ágiles. Define **qué tema se enseña en cada módulo y con qué profundidad**, cómo se escribe y qué recuadros existen. Antes de agregar un tema a un módulo, comprobar acá dónde corresponde.

Acordado con Pablo el 25 de septiembre de 2026, a partir de su revisión del Módulo 1.

## Flujo de trabajo

1. La fuente de cada módulo es `entregables/MODULO N/Contenido/contenido.md`.
2. `scripts/md-a-word.py --modulo N` genera `Contenido.docx` directamente desde ese Markdown, con el diseño de recuadros de esta guía.
3. La vista de control se obtiene convirtiendo el Word a PDF con LibreOffice (instalado en `C:/Program Files/LibreOffice`). El PDF es solo control temporal.
4. Se trabaja un módulo por vez: se reescribe, Pablo lo revisa y recién después se pasa al siguiente.

Estado: los cinco módulos están migrados a Markdown y se exportan con `md-a-word.py`. Las fuentes HTML anteriores quedan respaldadas en `.qa/` y ya no se usan.

## Estilo y recuadros

Las reglas de estilo, la sintaxis de la fuente y los tipos de recuadro son generales para todas las materias: ver `../_REGLAS-GENERALES/ESTILO-EDITORIAL.md` y `../_REGLAS-GENERALES/FLUJOS/CONTENIDO.md`. Surgieron de la revisión de Pablo sobre este módulo 1: menos ejemplos cotidianos y más casos reales, sin rótulos "Analogía" ni recuadros de "Criterio profesional", sin fechas de consulta en el texto, conceptos centrales con sección propia y sin adelantar temas de otros módulos.

Propio de esta materia: presentar herramientas e IA con gancho (qué se usa hoy, cómo ayuda la IA, hacia dónde van los agentes), sin avisos defensivos.

## Mapa de temas por módulo

Evita duplicaciones. "Profundo" = sección propia; "breve" = presentación o repaso; "mención" = una línea con remisión.

| Tema | M1 | M2 | M3 | M4 | M5 |
|---|---|---|---|---|---|
| Proyecto, producto, operación | Profundo | | | | |
| **Alcance** (definición, dentro/fuera, entregables, EDT simple, scope creep) | Profundo | | Gestión del alcance en backlog y releases | | |
| Alcance, tiempo y costo, con la calidad en el centro (triángulo) | Profundo | | | Capacidad y pronósticos | |
| Riesgo e incertidumbre | Profundo (conceptual) | | | Riesgos y dependencias en el seguimiento | |
| Interesados (stakeholders) | Profundo (quiénes, poder/interés) | | Comunicación con interesados de producto | | Colaboración y expectativas |
| Ciclo de vida y procesos | Breve | | | | |
| Predictivo, iterativo, incremental | Profundo (canción, Empire State, Uber, patineta) | | | | |
| Agilidad, origen, Manifiesto, 12 principios | Profundo | Repaso en una línea | | | |
| **Entrega de valor** y feedback | Profundo (concepto, salida vs resultado, idea de MVP) | | MVP y priorización con técnicas | Medir avance | Review |
| Gestión del cambio | Profundo (cómo decidir un cambio) | | Cambios en backlog y roadmap | | |
| Elegir enfoque (predictivo, ágil, híbrido) | Profundo | Elegir entre marcos ágiles | | | |
| Mapa de marcos (Scrum, Kanban, XP, Lean) | Mención al cierre | Profundo | | | |
| Roles de Scrum | | Profundo | | | Liderazgo |
| Backlog, historias, DoD, DoR | | Presentación | Profundo | | |
| Estimación, métricas, tableros | | | | Profundo | |
| **Herramientas** (Jira, Trello y otras) | | | | Profundo | |
| **IA y agentes en la gestión** | | | | Profundo (ver abajo) | Cierre prospectivo |
| Equipos, liderazgo, mejora continua | | | | | Profundo |
| Casos reales | Mención | Toyota | | | Profundo |

### Caso conductor

El **asistente universitario con IA** se mantiene como caso conductor en los cinco módulos, porque la carrera es Ingeniería en IA. Desde el Módulo 3 es el único caso conductor: se retiró TurnoYa para no mezclar dos productos didácticos. Aparece después del ejemplo cotidiano, no en su lugar. La **app bancaria** del Módulo 1 se conserva como caso resuelto de un cambio de alcance.

### Casos reales usados

Cada caso se usa en un solo módulo.

| Módulo | Caso | Qué enseña | Fuente |
|---|---|---|---|
| 1 | FBI Virtual Case File (2000 a 2005) | Alcance que crece sin control | [IEEE Spectrum](https://spectrum.ieee.org/who-killed-the-virtual-case-file) |
| 1 | Ópera de Sídney (1959 a 1973) | Triángulo: alcance incierto arrastra tiempo y costo | [Sydney Opera House](https://www.sydneyoperahouse.com/building/interesting-facts-about-sydney-opera-house) |
| 1 | OS/360 y la ley de Brooks (1975) | Sumar gente no acelera | *The Mythical Man-Month* |
| 1 | Mars Climate Orbiter (NASA, 1999) | Responsabilidades entre equipos | [NASA](https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf) |
| 1 | Empire State Building (1930 a 1931) | Cuándo funciona el enfoque predictivo | [History](https://www.history.com/articles/empire-state-building-construction) |
| 1 | Uber (desde 2010) | Enfoque incremental | [Timeline of Uber](https://en.wikipedia.org/wiki/Timeline_of_Uber) |
| 1 | Video de Dropbox (2007) | Producto mínimo viable | [Shortform](https://www.shortform.com/blog/dropbox-mvp-explainer-video/) |
| 1 | Lanzamiento de ChatGPT (2022) | Ciclo de feedback en IA | [OpenAI](https://openai.com/index/chatgpt/) |
| 2 | Del rugby a Scrum: Takeuchi y Nonaka (1986), Sutherland y Schwaber (1993 a 1995) | Origen de Scrum | [HBR](https://hbr.org/1986/01/the-new-new-product-development-game) |
| 2 | State of Agile, edición 17 (2023): Scrum 63 % | Qué marcos se usan | [Digital.ai](https://digital.ai/resource-center/analyst-reports/state-of-agile-report/) |
| 2 | Microsoft XIT y David J. Anderson (2004) | Origen de Kanban y efecto de limitar el WIP | [djaa.com](https://djaa.com/brief-history-kanban-knowledge-work/) |
| 2 | Chrysler C3 y Kent Beck (1996 a 2000) | Origen de XP | [Wikipedia](https://en.wikipedia.org/wiki/Chrysler_Comprehensive_Compensation_System) |
| 2 | Toyota: jidoka, andon y just in time | Lean y calidad dentro del proceso | [Toyota](https://global.toyota/en/company/vision-and-philosophy/production-system/) |
| 3 | Amazon Working Backwards (PR/FAQ) | Visión del producto desde el cliente | [Colin Bryar](https://docs.superhuman.com/@colin-bryar/working-backwards-how-write-an-amazon-pr-faq) |
| 3 | Historias: Ron Jeffries (3C, 2001) y Bill Wake (INVEST, 2003) | Origen de historias e INVEST | [Agile Alliance](https://agilealliance.org/glossary/three-cs/), [XP123](https://xp123.com/invest-in-good-stories-and-smart-tasks/) |
| 3 | Pendo 2019: 80 % de funciones rara vez usadas | Por qué priorizar | [Pendo](https://www.pendo.io/resources/the-2019-feature-adoption-report/) |
| 3 | Zappos (1999) | MVP tipo mago de Oz | [Fortune](https://fortune.com/2012/09/05/nick-swinmurn-zappos-silent-founder/) |
| 3 | HealthCare.gov (2013) | Riesgo de lanzar todo de golpe | [GAO](https://www.gao.gov/products/gao-14-694) |
| 4 | Falacia de la planificación: Buehler, Griffin y Ross (1994) | Por qué subestimamos | [JPSP 1994](https://web.mit.edu/curhan/www/docs/Articles/biases/67_J_Personality_and_Social_Psychology_366,_1994.pdf) |
| 4 | Planning Poker: James Grenning (2002) y Mike Cohn (2005) | Origen de la técnica | [Wikipedia](https://en.wikipedia.org/wiki/Planning_poker) |
| 4 | Agentes de Rovo en Jira (2025 a 2026) y Notion 3.0 (2025) | IA y agentes en herramientas de gestión | [Atlassian](https://www.atlassian.com/blog/rovo/ai-agents-in-jira), [Notion](https://www.notion.com/releases/2025-09-18) |
| 4 | ReAct (Yao y otros, 2022) | Ciclo pensar, actuar, observar de los agentes | [arXiv](https://arxiv.org/pdf/2210.03629) |
| 4 | Klarna (2024 a 2025) | Límites de la automatización con IA | [Klarna](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/), [Forbes](https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/) |
| 5 | Google Proyecto Aristóteles (2012 a 2015) | Seguridad psicológica | [re:Work](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness) |
| 5 | Deuda técnica oculta en IA: Sculley y otros (2015) | Deuda técnica en sistemas de IA | [NeurIPS](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) |
| 5 | Knight Capital (2012) | Riesgo del despliegue manual | [SEC](https://www.sec.gov/Archives/edgar/data/0001060749/000119312512346917/d361681d10q.htm) |
| 5 | DORA y *Accelerate* (2018) | Entrega rápida y segura | [DORA](https://dora.dev/research/) |
| 5 | "Modelo Spotify" (2012) | Copiar estructuras no copia la cultura | [Atlassian](https://www.atlassian.com/agile/agile-at-scale/spotify) |
| 5 | ING (2015) | Agilidad organizacional | [McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/ings-agile-transformation) |
| 5 | FBI Sentinel (2006 a 2012) | Continuación del Virtual Case File con enfoque ágil | [Wikipedia](https://en.wikipedia.org/wiki/Sentinel_%28FBI%29) |

### Herramientas e IA (resuelto en el Módulo 4)

El contenido retirado del Módulo 1 se desarrolló en las secciones 8 y 9 del Módulo 4: panorama de herramientas, Trello y Jira, IA en la gestión, agentes, comparación entre el ciclo de un agente y el de un equipo ágil, y el caso Klarna sobre los límites de la automatización. El Módulo 5 puede retomar el tema solo como cierre prospectivo, sin repetirlo.
