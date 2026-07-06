```
██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
███████╗██╗  ██╗██████╗ ███████╗██████╗ ████████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝
█████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝   ██║   ███████╗
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ╚════██║
███████╗██╔╝ ██╗██║     ███████╗██║  ██║   ██║   ███████║
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

            a l l   h u m a n   e x p e r t s
              i n t o   A I   a g e n t s
```

[![npm](https://img.shields.io/npm/v/domain-experts.svg?color=black)](https://www.npmjs.com/package/domain-experts)
[![downloads](https://img.shields.io/npm/dm/domain-experts.svg?color=black)](https://www.npmjs.com/package/domain-experts)
[![lint](https://github.com/wonsukchoi/domain-experts/actions/workflows/lint.yml/badge.svg)](https://github.com/wonsukchoi/domain-experts/actions/workflows/lint.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-black.svg)](./LICENSE)
[![spec](https://img.shields.io/badge/authoring_spec-v2-black.svg)](./AUTHORING.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-black.svg)](./CONTRIBUTING.md)

**[English](./README.md) | [한국어](./README.ko.md) | [日本語](./README.ja.md) | [简体中文](./README.zh-CN.md) | [Español](./README.es.md) | [Português](./README.pt-BR.md) | [हिन्दी](./README.hi.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Tiếng Việt](./README.vi.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [Bahasa Indonesia](./README.id.md)**

Biblioteca de código abierto de **definiciones de roles profesionales** — los modelos mentales reales, los umbrales de decisión y los modos de fallo de practicantes de verdad, estructurados para que cualquier agente de IA pueda cargar uno y razonar como ese experto. Pídele a tu agente que "revise este contrato" y responderá con el manual de cláusulas y las escaleras de repliegue de un abogado senior de contratos, no con el resumen genérico de internet de un generalista.

**Ir a:** [Inicio rápido](#inicio-rápido) · [¿No puedo simplemente decirle a Claude que actúe como un CFO?](#no-puedo-simplemente-decirle-a-claude-que-actúe-como-un-cfo) · [Visión](#visión--una-persona-todos-los-expertos) · [Cómo se construyen los roles](#cómo-se-construyen-los-roles) · [Cómo lo verificamos](#cómo-lo-verificamos--transparente-sin-necesidad-de-confiar-a-ciegas) · [Roles actuales](#roles-actuales) · [Úsalo con tu herramienta](#úsalo-con-tu-herramienta-de-ia) · [Hoja de ruta](#hoja-de-ruta) · [Contribuir](#contribuir--este-repositorio-se-acumula)

## Inicio rápido

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

No se necesita instalación — `npx` lo obtiene directamente de npm. ¿Lo usas seguido? Instala con `npm install -g domain-experts` y omite el `npx`.

**¿Usas Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code o Amp?** `npx domain-experts command --tool <id>` instala un comando de barra `/domain-expert` para tu herramienta — reinicia tu sesión y ejecuta `/domain-expert review this vendor contract`. Encuentra el rol, lo carga y razona como el experto correcto en un solo paso, sin la danza manual de `match`/`add`.

O sáltate el paso manual por completo: carga [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) una sola vez, y tu agente detectará qué experto necesita cada tarea, obtendrá automáticamente el contexto completo del rol, y te dirá con honestidad cuando un rol aún no está cubierto en lugar de improvisar. Tú sigues trabajando; la experiencia adecuada aparece por sí sola.

## "¿No puedo simplemente decirle a Claude que actúe como un CFO?"

Puedes — y obtendrás una imitación superficial: el promedio de cada descripción de puesto en internet, regenerada desde cero en cada sesión, distinta cada vez, verificada por nadie.

```
 ── prompt: "act as a CFO" ───────────┬── role: financial-manager ───────────
                                      │
  "I'd start by monitoring cash       │  "DSO went 48 → 56 days with no
   flow and key financial metrics,    │   billing-terms change. Show me the
   ensuring alignment between…"       │   five largest invoices past 60 days
                                      │   — and reconcile bookings to the
                                      │   change in deferred revenue, because
                                      │   flat deferred + 'record bookings'
                                      │   don't coexist."
 ─────────────────────────────────────┴───────────────────────────────────────
```

La diferencia, en concreto:

- **Contenido no derivable.** Cada rol debe pasar una prueba de no-derivabilidad: nada que pueda regenerarse solo a partir del título del puesto. Lo que queda es lo que el prompting no puede producir a demanda — umbrales numéricos de alerta, rangos de negociación estándar del mercado, ejemplos trabajados con aritmética que cuadra, posiciones de repliegue en orden de preferencia.
- **Un filtro de calidad, no una generación única.** Los roles se construyen mediante un pipeline de múltiples pasadas ([`AUTHORING.md`](./AUTHORING.md)) — ver el diagrama abajo. Un prompt de una sola línea no obtiene nada de eso.
- **Estructura reforzada por CI.** Cada PR ejecuta [`scripts/lint_roles.py`](./scripts/lint_roles.py): esquema, secciones obligatorias, enlaces que resuelven, frases de relleno prohibidas, cobertura completa de señales de alerta, números reales en el ejemplo trabajado. El texto genérico de descripción de puesto hace fallar el build.
- **Se acumula con el tiempo.** Tu prompt improvisado desaparece cuando termina la sesión. Estos archivos acumulan correcciones de practicantes, llevan una escalera de madurez (`draft` → `reviewed-by-practitioner` → `mature`) y una especificación versionada (`spec: 2` marca los roles al nivel actual), y mejoran con cada PR. Las correcciones llegan a todos.
- **Eficiente en tokens por diseño.** Cada rol es un núcleo de razonamiento compacto (`SKILL.md`) más profundidad bajo demanda (`references/`). El agente paga por la profundidad solo cuando la tarea la necesita:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### ¿Cuál es el verdadero moat?

Objeción justa: nada de lo anterior impide que alguien haga `git clone` de este mismo repo y lo lance como su propio producto — licencia MIT, cero bloqueo de contenido. Respuesta honesta: el conjunto de archivos no es el moat. Lo difícil de clonar es la maquinaria que sigue produciéndolo y corrigiéndolo:

- **El proceso, no el resultado.** Copiar 97 archivos toma un comando. Copiar el ciclo de autoría con crítica adversarial → rúbrica de 9 criterios → lint obligatorio ([`AUTHORING.md`](./AUTHORING.md)) que sigue produciéndolos y corrigiéndolos, no — un fork hereda la foto de hoy, no las correcciones de mañana.
- **Un estándar, no una base de datos.** `SKILL.md` ya funciona en 30+ herramientas de agentes. Ser la biblioteca más grande en un formato abierto y portable es una posición de distribución, no de contenido — el valor está en ser la respuesta por defecto que la gente encuentra, no en los bytes en sí.
- **Verificado, no afirmado.** Cualquier competidor puede decir "escrito por expertos". Pocos pueden ejecutar `python3 evals/run_evals.py` frente a ti y mostrar 13/15 victorias contrafactuales. La confianza aquí se mide y se reproduce, no se declara.
- **La actualidad le gana al recuerdo paramétrico.** Aunque un futuro modelo entrene con el texto público de este repo, ese conocimiento queda congelado en la fecha de corte del entrenamiento. Las correcciones de este repo se publican el mismo día que un practicante las reporta — sin ciclo de reentrenamiento, versionadas, trazadas a una fuente.
- **Disciplina de cobertura.** La base de 1,016 ocupaciones de O*NET obliga a una cobertura sistemática de nicho (funeral-home-manager, wind-energy-operations-manager) que un competidor oportunista, curando solo roles de moda, no se molestará en igualar.
- **Gratis y portable le gana a atado por suscripción.** Esto no compite con tu factura del LLM — de todos modos pagas la inferencia. Compite con SaaS vertical cerrado ("Asesor Legal IA", $99/mes): esos no pueden igualar gratis, forkeable, y ejecutable en un modelo local sin costo recurrente.

Nada de esto es todavía un moat con 97 roles y una base pequeña de colaboradores — es una trayectoria. La apuesta: el bien común se compone más rápido de lo que cualquier fork puede seguirle el ritmo, una vez que suficientes practicantes reporten correcciones en vez de escribir prompts desde cero cada sesión.

## Visión — una persona, todos los expertos

```
                              ┌───────────────────────┐
                              │   Y O U  +  A G E N T  │
                              └───────────┬───────────┘
                                          │
             ┌──────────────┬────────────┼────────────┬──────────────┐
             │              │            │            │              │
             ▼              ▼            ▼            ▼              ▼
        lawyer-        financial-    data-        marketing-    clinical-
        contracts      manager       scientist    strategist    research-
        │              │             │            │             coordinator
        redline the    defend the    read the     kill the      │
        MSA            runway call   A/B test     dead channel  flag the
                                      right                      deviation

        no résumé screened. no calendar. no invoice. no waiting room.
        just: which role does this task need — load it — reason as it.
```

Hoy en día, hacer bien algo fuera de tu propio ámbito significa contratar, subcontratar o buscar contactos — encontrar un abogado, esperar en la agenda de un CFO, pagar la tarifa de un estratega de marketing. Esa fricción es un impuesto que pagan todos los fundadores en solitario, todos los equipos pequeños, cualquier persona que se topa con un problema fuera de su experiencia. La mayoría simplemente no hace la tarea, o la hace mal.

Una persona con una suscripción de IA —o incluso un modelo local, sin suscripción alguna— y este repositorio no paga ese impuesto. Carga el razonamiento real del CFO para una decisión sobre el runway. Carga el manual de cláusulas del abogado de contratos para una redacción de cambios. Carga el criterio del coordinador de investigación clínica para una desviación de protocolo. Cambia de rol según la tarea, bajo demanda, al costo de la inferencia en lugar del costo de una contratación. Una persona, un agente, el criterio acumulado de cientos de profesiones.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

Ese es el verdadero objetivo final aquí, no una curiosidad: la barrera entre "necesito un experto" y "tengo uno" se derrumba. Y se vuelve más real a medida que crece la cobertura — 92 roles frente a 1,016 ocupaciones rastreadas hoy; la hoja de ruta existe para que esa brecha se cierre, no para que siga siendo interesante para siempre.

No reemplaza el criterio, la responsabilidad ni la licencia profesional donde estos deben recaer legalmente en un humano — cada rol regulado (derecho, medicina, finanzas) lo dice explícitamente. Reemplaza la fricción de no tener acceso al razonamiento en primer lugar.

```
you ─── "review this vendor contract"
              │
              ▼
   ┌──────────────────────┐        ┌─ roles/lawyer-contracts/ ──────────────┐
   │  domain-expert       │        │                                        │
   │  router              │───────▶│  SKILL.md      the reasoning core      │
   │  (finds the expert   │        │  references/                           │
   │   your task needs)   │        │   ├─ clause-playbook.md  fallbacks     │
   └──────────────────────┘        │   ├─ red-flags.md        smell tests   │
                                   │   └─ vocabulary.md       terms of art  │
                                   └────────────────────┬───────────────────┘
                                                        │
                                                        ▼
                                     agent reasons like a senior
                                     contracts attorney — thresholds,
                                     market positions, redline language
```

## Cómo se construyen los roles

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Cada rol sigue el mismo contrato, reforzado por la especificación y por CI:

1. **Tres pruebas de aptitud para publicarse** — un practicante que lo lea asiente en lugar de encogerse de hombros; un agente con el rol toma decisiones medibles distintas de las que tomaría sin él; nada en el rol es derivable solo a partir del título del puesto.
2. **Anatomía fija** — identidad, núcleo de primeros principios, heurísticas condicionales ("cuando X, por defecto Y a menos que Z"), un marco de decisión ejecutable, modos de fallo comunes, y un ejemplo trabajado con números reales que cuadran y terminan en el entregable real (el memo, la redacción de cambios, el informe final).
3. **Trío de referencias** — un archivo de manual/artefactos con plantillas completadas, `red-flags.md` (señal → qué significa → primera pregunta → datos a obtener), y `vocabulary.md` (términos técnicos con el error de uso común explicado).
4. **Procedencia** — las fuentes están identificadas; los números específicos se remontan a ellas o se etiquetan como heurísticas declaradas. Los roles regulados (derecho, medicina, finanzas) llevan descargos de responsabilidad explícitos.
5. **Columna vertebral O*NET** — la cobertura sigue la taxonomía de ocupaciones del Departamento de Trabajo de EE. UU. (1,016 ocupaciones), de modo que el crecimiento es sistemático y no simplemente lo que pareció interesante esa semana.

Especificación completa, rúbrica y el pipeline de redacción con LLM: [`AUTHORING.md`](./AUTHORING.md). En un checkout de Claude Code, todo este pipeline se ejecuta como `/generate-role "<need>"` — ver [Automatización para mantenedores](#maintainer-automation-claude-code) más abajo.

## Cómo lo verificamos — transparente, sin necesidad de confiar a ciegas

"Escrito por expertos" es una afirmación; este repositorio entrega los comprobantes en su lugar. Cuatro capas independientes, todas ejecutables por cualquiera desde este checkout:

```
 layer 1  SOURCING      every threshold traces to a named practitioner
 (input)                source (books, standards, postmortems) or is
                        labeled a stated heuristic — see each role's
                        Sources section
 layer 2  MECHANICAL    scripts/lint_roles.py on every PR: schema,
 (CI)                   required sections, references/ trio, banned
                        filler phrases, real numbers in the worked
                        example — generic text fails the build
 layer 3  COUNTERFACTUAL evals/: same model answers the same scenario
 (measured)             with and without the role, blind judge scores
                        observable expert behaviors in random A/B order
 layer 4  PARITY        evals/parity/: skill answers real questions that
 (measured)             real practitioners already answered publicly —
                        blind judge compares head-to-head
```

Últimas corridas publicadas (2026-07-06, Haiku 4.5 respondiendo, Sonnet 5 juzgando a ciegas, ambos harnesses):

- **Contrafactual:** el skill gana en **13/15 escenarios** (1 empate, 1 derrota) — 72% de los criterios de comportamiento experto alcanzados frente al 37% de la línea base generalista.
- **Paridad frente a humanos:** la respuesta del skill fue preferida sobre la respuesta aceptada del practicante real en Stack Exchange en **5 de 8** comparaciones directas a ciegas (muestra pequeña; los conjuntos de preguntas están creciendo — trátese como una señal preliminar, no como un estudio).

Todo resultado es reproducible: `python3 evals/run_evals.py` y `python3 evals/parity/run_parity.py`. Cuando un rol falla estas pruebas, eso también es público — el objetivo es la medición, no el marketing. La revisión por practicantes sigue siendo la estrella de oro (`metadata.maturity`), pero el piso de confianza se mide, no se da por garantizado.

## Roles actuales

<!-- ROLE_COUNTS_START -->
**106 roles drafted** (102 mapped to an O*NET occupation, 4 custom; 64 at spec 2, 42 awaiting upgrade), across 10 categories:

- **design**: 2
- **engineering**: 17
- **finance**: 10
- **healthcare**: 8
- **legal**: 11
- **marketing**: 4
- **operations**: 43
- **other**: 5
- **product**: 1
- **sales**: 5

Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.
<!-- ROLE_COUNTS_END -->

Este bloque se genera automáticamente — ejecuta `python3 scripts/generate_roadmap.py` después de agregar, eliminar o re-mapear un rol; no lo edites a mano.

## Úsalo con tu herramienta de IA

`SKILL.md` es un formato multi-herramienta — el mismo archivo de rol funciona en Claude Code, Codex CLI, Cursor y más de 30 otros agentes. Solo cambia el directorio de instalación.

### Configuración cero: pega esto en tu agente

Copia esto en Claude Code, Codex, Cursor, o cualquier agente con acceso a shell, describe tu tarea al final, y este instalará el experto correcto por sí mismo:

```text
Install a domain expert for my task from the open-source library
https://github.com/wonsukchoi/domain-experts :

1. Run: npx --yes domain-experts match "<my task>" --json
2. If it returns a confident match, install it:
   npx --yes domain-experts add <slug>
   (default target is ./.claude/skills/<slug>; if you are not Claude Code,
   pass --to <your skills directory>/<slug>, e.g. --to .codex/skills/<slug>)
3. Read the installed SKILL.md fully. Open files under references/ whenever
   the task needs the depth they cover. Then do my task reasoning as that
   expert — apply its thresholds, red flags, and decision framework.
4. If there is no confident match, tell me which roles came closest and
   continue as a generalist — do not pretend to be an expert the library
   does not have.

My task: <describe your task here>
```

**Usuarios de Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code y Amp:** sáltense el pegado — `npx domain-experts command --tool <id>` instala `/domain-expert` una vez, y luego solo ejecuta `/domain-expert <tarea>` cada vez (ver [comando de barra `/domain-expert`](#comando-de-barra-domain-expert) más abajo).

### Instalación por herramienta

| Herramienta | Cómo |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — se ubica en `./.claude/skills/<slug>/`, detectado automáticamente como skill. |
| **Codex CLI** | Mismo comando con `--to .codex/skills/<slug>` (proyecto) o `--to ~/.codex/skills/<slug>` (personal). Una nueva sesión lo detecta. |
| **Cursor** | Mismo comando con `--to .cursor/skills/<slug>` — Cursor lee el mismo formato `SKILL.md` de forma nativa. |
| **Windsurf, Roo Code, Goose y otras herramientas compatibles con SKILL.md** | Mismo comando con `--to <directorio de skills de tu herramienta>/<slug>` — revisa la documentación de tu herramienta para la ruta. |
| **Herramientas que leen `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Instala en cualquier parte del repo (p. ej. `--to skills/<slug>`), luego agrega una línea a `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Cualquier chat de IA (sin shell)** | Abre el rol en GitHub, pega `SKILL.md` en el system prompt o en las instrucciones personalizadas; pega los archivos de `references/` cuando la conversación necesite esa profundidad. |

Cada instalación copia el rol completo — `SKILL.md` más `references/` — de modo que los manuales completos viajan junto con él.

### Despacho automático

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) es un meta-skill que elimina incluso el paso `match` — instálalo con `npx domain-experts add domain-expert-router`, cárgalo una vez, y tu agente encontrará el rol adecuado para peticiones de "actúa como X" por sí mismo, y te avisará con honestidad cuando un rol no esté cubierto todavía.

### Comando de barra `/domain-expert`

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Reinicia tu sesión, y luego usa `/domain-expert <tarea>` directamente — p. ej. `/domain-expert review this vendor contract`. Ejecuta `match`, carga el `SKILL.md` del rol ganador (y `references/` según se necesite), y responde como ese experto, o te avisa con honestidad cuando nada coincide todavía. Misma idea que el skill enrutador de arriba, empaquetada como un comando de un solo uso en lugar de un skill siempre cargado.

| `--tool` | Instala en | Notas |
|---|---|---|
| `claude` (por defecto) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex solo lee prompts desde el directorio a nivel de usuario, sin opción local al proyecto; la documentación de OpenAI marca este mecanismo como obsoleto en favor de "skills", pero todavía funciona |
| `gemini` | `.gemini/commands/domain-expert.toml` | Formato TOML |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf llama a esto "workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | La ubicación de Amp es fija en la raíz del repo, sin directorio global separado |

Agrega `--global` para instalar en el directorio a nivel de usuario de la herramienta (p. ej. `~/.claude/commands/`, `~/.cursor/commands/`) en lugar del directorio del proyecto, o `--to <ruta>` para una ubicación completamente personalizada.

### Referencia de la CLI

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` puntúa los roles por superposición de palabras clave e informa una coincidencia confiable, candidatos de baja confianza, o un honesto "aún no cubierto" — no adivina en silencio. `--json` para uso programático.

El paquete de npm toma una instantánea de la biblioteca de roles en cada release. Para la vanguardia sin publicar, usa `npx --yes github:wonsukchoi/domain-experts <command>` — la misma CLI, directamente desde `main`.

### Automatización para mantenedores (Claude Code)

Trabajar en un checkout de Claude Code de este repositorio añade tres comandos slash que automatizan el pipeline anterior en lugar de reemplazarlo — cada uno está sujeto a una PR revisada por una persona, ninguno hace commit en `main` ni publica por sí solo:

- `/generate-role "<need>"` — resuelve una necesidad en texto libre hacia un rol existente, una nueva hoja de especialización, o un nuevo rol padre, y luego ejecuta el pipeline Pass 0-4 de AUTHORING.md (investigación → borrador → crítica adversarial → puntuación, limitado a 2 ciclos de revisión) y abre una PR.
- `/audit-roles [batchSize]` — re-puntuación por lotes de los roles publicados frente a la rúbrica y la vigencia de las fuentes; marca `last_audited`/`audit_score`, señala `status: needs-refresh`, y deprecia (mueve a `roles/_deprecated/`) tras un segundo fallo consecutivo.
- `/scan-project <path>` — escaneo de solo lectura de un proyecto externo (stack, README, estructura, commits recientes), propone necesidades candidatas cruzadas con la cobertura existente, y entrega las que elijas a `/generate-role`. Nada del proyecto escaneado se escribe en ningún sitio.

Las consultas `match` de baja confianza se registran en `data/gap-log.jsonl` y se muestran, ordenadas por frecuencia, en la sección "Requested but missing" de [`ROADMAP.md`](./ROADMAP.md) — una señal concreta de qué redactar a continuación.

## Hoja de ruta

[`ROADMAP.md`](./ROADMAP.md) es el backlog maestro — las 1,016 ocupaciones de O*NET, agrupadas por categoría, marcadas conforme se van redactando. Úsalo para encontrar un rol no cubierto en lugar de adivinar qué falta.

## Contribuir — este repositorio se acumula

Cada rol agregado hace que el enrutador sea más inteligente, cada corrección llega a todos los usuarios en el próximo release, y cada pregunta de evaluación hace que la barra de calidad sea más difícil de simular. Un prompt que escribes para ti mismo muere con tu sesión; un rol que contribuyes aquí funciona para todos, para siempre, y sigue mejorando después de que te vas. Esa es toda la apuesta: **1,016 ocupaciones no es un proyecto solitario — es un bien común.**

Preguntas frecuentes (fallos de lint, conflictos al hacer push, proceso de release) → [`docs/FAQ.md`](./docs/FAQ.md).

Tres formas de participar, para cualquier nivel de habilidad:

1. **¿Trabajas en un rol que cubrimos?** Léelo. Cualquier error es un [issue de corrección de practicante](../../issues/new/choose) de 2 minutos — la contribución más valiosa que este proyecto puede recibir. No se necesitan habilidades de PR.
2. **¿Quieres escribir o mejorar un rol?** Sigue la receta exacta en [`CONTRIBUTING.md`](./CONTRIBUTING.md) — está escrita con tanta precisión que un LLM puede ejecutarla, así que tú y tu asistente de IA pueden hacerlo juntos. El lint te dice si la estructura se queda corta antes de que cualquier humano la revise. 42 roles heredados están [disponibles para reclamar ahora mismo](../../issues/1).
3. **¿No puedes escribir pero sí encontrar?** Recolecta preguntas de paridad (`evals/parity/harvest_stackexchange.py`) o presenta una [solicitud de rol](../../issues/new/choose) con las tareas que le delegarías.

Si la especificación choca con la realidad de un practicante, la especificación pierde — dilo en tu PR y arreglamos la especificación.

## Licencia

MIT — ver [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
