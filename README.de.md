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

Open-Source-Bibliothek von **Job-Rollen-Definitionen** — die tatsächlichen Denkmodelle, Entscheidungsschwellen und Fehlermuster echter Praktiker, so strukturiert, dass jeder AI-Agent eine davon laden und wie dieser Experte denken kann. Bitten Sie Ihren Agenten, "diesen Vertrag zu prüfen", und er antwortet mit dem Klausel-Playbook und den Fallback-Leitern eines erfahrenen Vertragsanwalts — nicht mit der Internet-Zusammenfassung eines Generalisten.

**Direkt zu:** [Schnellstart](#schnellstart) · ["Warum nicht einfach danach fragen?"](#kann-ich-claude-nicht-einfach-bitten-sich-wie-ein-cfo-zu-verhalten) · [Vision](#vision--eine-person-jeder-experte) · [Wie Rollen entstehen](#wie-rollen-entstehen) · [Wie wir verifizieren](#wie-wir-verifizieren--transparent-kein-vertrauensvorschuss-nötig) · [Aktuelle Rollen](#aktuelle-rollen) · [Mit Ihrem Tool nutzen](#mit-ihrem-ai-tool-nutzen) · [Roadmap](#roadmap) · [Mitwirken](#mitwirken--dieses-repo-wächst-mit-zinseszins)

## Schnellstart

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

Keine Installation nötig — `npx` lädt es direkt von npm. Wenn Sie es häufig nutzen: `npm install -g domain-experts` installieren und `npx` weglassen.

**Nutzen Sie Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code oder Amp?** `npx domain-experts command --tool <id>` installiert einen `/domain-expert`-Slash-Befehl dafür — starten Sie Ihre Sitzung neu und führen Sie `/domain-expert review this vendor contract` aus. Er sucht, lädt und denkt in einem Schritt als die passende Rolle — kein manuelles `match`/`add`-Hin-und-her.

Oder überspringen Sie den manuellen Schritt ganz: Laden Sie einmalig [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md), und Ihr Agent erkennt selbst, welchen Experten eine Aufgabe braucht, zieht den vollständigen Kontext der Rolle automatisch heran und sagt Ihnen ehrlich, wenn eine Rolle noch nicht abgedeckt ist, statt zu improvisieren. Sie arbeiten einfach weiter; die passende Expertise erscheint von selbst.

## "Kann ich Claude nicht einfach bitten, sich wie ein CFO zu verhalten?"

Können Sie — und Sie bekommen eine oberflächliche Imitation: den Durchschnitt aller Jobbeschreibungen im Internet, jede Sitzung neu generiert, jedes Mal anders, von niemandem verifiziert.

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

Der Unterschied, konkret:

- **Nicht ableitbarer Inhalt.** Jede Rolle muss einen Nicht-Ableitbarkeits-Test bestehen: nichts, was sich allein aus dem Jobtitel neu erzeugen ließe. Was übrig bleibt, ist genau das, was Prompting nicht auf Abruf produzieren kann — numerische Warnsignal-Schwellen, marktübliche Verhandlungsspannen, durchgerechnete Beispiele mit aufgehender Arithmetik, priorisierte Fallback-Positionen.
- **Ein Qualitäts-Gate, keine Einmal-Generierung.** Rollen entstehen über eine mehrstufige Pipeline ([`AUTHORING.md`](./AUTHORING.md)) — siehe Diagramm unten. Ein Einzeiler-Prompt durchläuft davon nichts.
- **Durch CI erzwungene Struktur.** Jeder PR durchläuft [`scripts/lint_roles.py`](./scripts/lint_roles.py): Schema, Pflichtabschnitte, funktionierende Links, verbotene Floskeln, Vollständigkeit der Warnsignale, echte Zahlen im durchgerechneten Beispiel. Generischer Jobbeschreibungstext lässt den Build scheitern.
- **Es wächst mit Zinseszins.** Ihr Ad-hoc-Prompt verschwindet, wenn die Sitzung endet. Diese Dateien sammeln Korrekturen von Praktikern an, tragen eine Reifeleiter (`draft` → `reviewed-by-practitioner` → `mature`) sowie eine versionierte Spezifikation (`spec: 2` markiert Rollen auf aktuellem Stand) und werden mit jedem PR besser. Korrekturen erreichen alle.
- **Von Grund auf tokeneffizient.** Jede Rolle ist ein kompakter Denkkern (`SKILL.md`) plus bei Bedarf abrufbare Tiefe (`references/`). Der Agent zahlt nur dann für Tiefe, wenn die Aufgabe sie braucht:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### Was ist also der eigentliche Burggraben?

Berechtigter Einwand: Nichts davon hindert jemanden daran, genau dieses Repo per `git clone` zu kopieren und als eigenes Produkt zu verkaufen — MIT-Lizenz, keine Inhaltssperre. Ehrliche Antwort: Der Dateibestand ist nicht der Burggraben. Schwer zu forken ist die Maschine, die ihn weiter produziert und korrigiert:

- **Die Pipeline, nicht das Ergebnis.** 97 Dateien zu kopieren ist ein einziger Befehl. Die adversariale Kritik → 9-Kriterien-Rubrik → lint-gestützte Autorenschleife ([`AUTHORING.md`](./AUTHORING.md)), die sie ständig weiter produziert und korrigiert, lässt sich nicht kopieren — ein Fork erbt den heutigen Schnappschuss, nicht die Korrekturen von morgen.
- **Ein Standard, keine Datenbank.** `SKILL.md` läuft bereits in über 30 Agent-Tools. Die größte Bibliothek in einem portablen offenen Format zu sein, ist eine Vertriebsposition, keine Inhaltsposition — der Wert liegt darin, die Standardantwort zu sein, die Leute finden, nicht in den Bytes selbst.
- **Verifiziert, nicht behauptet.** Jeder Wettbewerber kann sagen "von Experten geschrieben". Wenige können vor Ihren Augen `python3 evals/run_evals.py` ausführen und 13/15 kontrafaktische Siege zeigen. Vertrauen ist hier gemessen und reproduzierbar, nicht behauptet.
- **Aktualität schlägt parametrisches Erinnern.** Selbst wenn ein zukünftiges Modell auf dem öffentlichen Text dieses Repos trainiert, friert dieses Wissen zum Trainings-Stichtag ein. Die Korrekturen dieses Repos gehen live, sobald ein Praktiker sie einreicht — kein Retraining-Zyklus, versioniert, auf eine Quelle rückführbar.
- **Disziplin bei der Abdeckung.** Das 1.016-Berufe-Rückgrat von O*NET erzwingt systematische Long-Tail-Abdeckung (funeral-home-manager, wind-energy-operations-manager), die ein opportunistischer Wettbewerber, der nur Trend-Rollen kuratiert, sich nicht die Mühe macht abzugleichen.
- **Kostenlos und portabel schlägt Abo-Bindung.** Das konkurriert nicht mit Ihrer LLM-Rechnung — Sie zahlen die Inferenz so oder so. Es konkurriert mit geschlossenen vertikalen SaaS-Angeboten ("AI Legal Advisor", 99 $/Monat): Die können mit kostenlos, forkbar und auf einem lokalen Modell ohne wiederkehrende Kosten lauffähig nicht mithalten.

Bei 97 Rollen und einer kleinen Beitragenden-Basis ist das noch kein Burggraben — es ist eine Flugbahn. Die Wette: Die Commons wachsen schneller mit Zinseszins, als jeder einzelne Fork mithalten kann, sobald genügend Praktiker Korrekturen einreichen, statt jede Sitzung Prompts von Grund auf neu zu schreiben.

## Vision — eine Person, jeder Experte

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

Heute bedeutet es, etwas weit außerhalb der eigenen Spur gut zu erledigen, dass man einstellen, beauftragen oder aktiv suchen muss — einen Anwalt finden, auf den Kalender eines CFO warten, den Satz eines Marketingstrategen bezahlen. Diese Reibung ist eine Steuer auf jeden Solo-Gründer, jedes kleine Team, jede Person, die auf ein Problem außerhalb ihrer Expertise stößt. Die meisten Menschen tun die Sache einfach nicht oder machen sie schlecht.

Eine Einzelperson mit einem AI-Abo — oder einem lokalen Modell, ganz ohne Abo — und diesem Repo zahlt diese Steuer nicht. Laden Sie die tatsächliche Argumentation des CFO für eine Runway-Entscheidung. Laden Sie das Klausel-Playbook des Vertragsanwalts für eine Überarbeitung. Laden Sie das Urteilsvermögen des klinischen Studienkoordinators für eine Protokollabweichung. Rollen je nach Aufgabe wechseln, bei Bedarf, zu den Kosten der Inferenz statt einer Einstellung. Eine Person, ein Agent, das angesammelte Entscheidungswissen Hunderter Berufe.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

Das ist hier das eigentliche Endziel, keine Kuriosität: Die Barriere zwischen "Ich brauche einen Experten" und "Ich habe einen" verschwindet. Das wird umso wahrer, je mehr die Abdeckung wächst — heute 92 Rollen gegenüber 1.016 erfassten Berufen; die Roadmap existiert, damit sich diese Lücke schließt, nicht damit sie für immer interessant bleibt.

Es ersetzt weder Urteilsvermögen, Verantwortung noch Zulassung, wo diese rechtlich bei einem Menschen liegen müssen — jede regulierte Rolle (Recht, Medizin, Finanzen) sagt das ausdrücklich. Es ersetzt die Reibung, die entsteht, wenn man überhaupt keinen Zugang zu dieser Argumentation hat.

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

## Wie Rollen entstehen

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Jede Rolle folgt demselben Vertrag, durchgesetzt durch Spezifikation und CI:

1. **Drei Ship-Tests** — ein Praktiker nickt beim Lesen, statt mit den Schultern zu zucken; ein Agent mit der Rolle trifft messbar andere Entscheidungen als ohne; nichts darin lässt sich allein aus dem Jobtitel ableiten.
2. **Feste Anatomie** — Identität, Grundprinzipien-Kern, bedingte Heuristiken ("wenn X, standardmäßig Y, außer bei Z"), ein ausführbares Entscheidungs-Framework, häufige Fehlermuster und ein durchgerechnetes Beispiel mit echten, aufgehenden Zahlen, das im tatsächlichen Liefergegenstand endet (das Memo, die Überarbeitung, der Bericht).
3. **Referenzen-Trio** — eine Tiefen-Playbook-/Artefakte-Datei mit ausgefüllten Vorlagen, `red-flags.md` (Signal → Bedeutung → erste Frage → abzurufende Daten) und `vocabulary.md` (Fachbegriffe mit ausbuchstabiertem häufigem Missbrauch).
4. **Herkunft** — Quellen werden benannt; konkrete Zahlen lassen sich zurückverfolgen oder werden als angegebene Heuristik gekennzeichnet. Regulierte Rollen (Recht, Medizin, Finanzen) tragen explizite Haftungsausschlüsse.
5. **O*NET-Rückgrat** — die Abdeckung folgt der Berufstaxonomie des US-Arbeitsministeriums (1.016 Berufe), sodass das Wachstum systematisch erfolgt und nicht danach, was in einer bestimmten Woche gerade interessant erschien.

Vollständige Spezifikation, Rubrik und die LLM-Entwurfspipeline: [`AUTHORING.md`](./AUTHORING.md). In einem Claude-Code-Checkout läuft diese gesamte Pipeline als `/generate-role "<need>"` — siehe [Automatisierung für Maintainer](#maintainer-automation-claude-code) weiter unten.

## Wie wir verifizieren — transparent, kein Vertrauensvorschuss nötig

"Von Experten geschrieben" ist eine Behauptung; dieses Repo liefert stattdessen die Belege. Vier unabhängige Ebenen, alle von jedem aus diesem Checkout ausführbar:

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

Zuletzt veröffentlichte Durchläufe (2026-07-06, Haiku 4.5 antwortet, Sonnet 5 urteilt blind, beide Harnesses):

- **Kontrafaktisch:** Skill gewinnt **13/15 Szenarien** (1 Unentschieden, 1 Niederlage) — 72 % der Experten-Verhaltenskriterien getroffen gegenüber 37 % bei der Generalisten-Baseline.
- **Parität gegenüber Menschen:** Skill-Antwort gegenüber der akzeptierten Stack-Exchange-Antwort des echten Praktikers in **5 von 8** blinden Kopf-an-Kopf-Vergleichen bevorzugt (kleine Stichprobe; die Fragensets wachsen — als Signal, nicht als Studie zu betrachten).

Jedes Ergebnis ist reproduzierbar: `python3 evals/run_evals.py` und `python3 evals/parity/run_parity.py`. Wenn eine Rolle diese Tests nicht besteht, ist auch das öffentlich — es geht um Messung, nicht um Marketing. Die Praktiker-Überprüfung bleibt die Auszeichnung obendrauf (`metadata.maturity`), aber die Vertrauensbasis ist gemessen, nicht bloß behauptet.

## Aktuelle Rollen

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

Dieser Block wird automatisch generiert — führen Sie nach dem Hinzufügen/Entfernen/Neu-Zuordnen einer Rolle `python3 scripts/generate_roadmap.py` aus, bearbeiten Sie ihn nicht von Hand.

## Mit Ihrem AI-Tool nutzen

`SKILL.md` ist ein tool-übergreifendes Format — dieselbe Rollendatei funktioniert in Claude Code, Codex CLI, Cursor und über 30 weiteren Agenten. Nur das Installationsverzeichnis unterscheidet sich.

### Ohne Einrichtung: fügen Sie dies in Ihren Agenten ein

Kopieren Sie das hier in Claude Code, Codex, Cursor oder einen beliebigen Agenten mit Shell-Zugriff, beschreiben Sie unten Ihre Aufgabe, und er installiert den passenden Experten von selbst:

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

**Nutzer von Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code und Amp:** Sie können sich das Einfügen sparen — `npx domain-experts command --tool <id>` installiert `/domain-expert` einmalig, danach führen Sie einfach jedes Mal `/domain-expert <task>` aus (siehe [`/domain-expert`-Slash-Befehl](#domain-expert-slash-befehl) unten).

### Installation pro Tool

| Tool | Vorgehen |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — landet in `./.claude/skills/<slug>/`, wird automatisch als Skill erkannt. |
| **Codex CLI** | Derselbe Befehl mit `--to .codex/skills/<slug>` (Projekt) oder `--to ~/.codex/skills/<slug>` (persönlich). Wird in der nächsten Sitzung erkannt. |
| **Cursor** | Derselbe Befehl mit `--to .cursor/skills/<slug>` — Cursor liest dasselbe `SKILL.md`-Format nativ. |
| **Windsurf, Roo Code, Goose und andere SKILL.md-kompatible Tools** | Derselbe Befehl mit `--to <Skills-Verzeichnis des Tools>/<slug>` — prüfen Sie den Pfad in der Dokumentation Ihres Tools. |
| **Tools, die `AGENTS.md` lesen** (GitHub Copilot, Jules, Amp, Zed, …) | An beliebiger Stelle im Repo installieren (z. B. `--to skills/<slug>`), dann eine Zeile zu `AGENTS.md` hinzufügen: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Beliebige Chat-AI (ohne Shell)** | Die Rolle auf GitHub öffnen, `SKILL.md` in den System-Prompt oder die benutzerdefinierten Anweisungen einfügen; `references/`-Dateien einfügen, wenn das Gespräch die Tiefe braucht. |

Jede Installation kopiert die vollständige Rolle — `SKILL.md` plus `references/` —, sodass die Tiefen-Playbooks mitreisen.

### Automatisches Dispatching

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) ist ein Meta-Skill, der sogar den `match`-Schritt überflüssig macht — installieren Sie ihn mit `npx domain-experts add domain-expert-router`, laden Sie ihn einmal, und Ihr Agent findet die passende Rolle für "verhalte dich wie X"-Anfragen von selbst und sagt ehrlich, wenn eine Rolle noch nicht abgedeckt ist.

### `/domain-expert`-Slash-Befehl

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Starten Sie Ihre Sitzung neu und nutzen Sie danach direkt `/domain-expert <task>` — z. B. `/domain-expert review this vendor contract`. Er führt `match` aus, lädt die `SKILL.md` der gewinnenden Rolle (und `references/` bei Bedarf) und antwortet als dieser Experte, oder sagt Ihnen ehrlich, wenn noch nichts passt. Dieselbe Idee wie der Router-Skill oben, nur als Einmal-Befehl statt als dauerhaft geladener Skill verpackt.

| `--tool` | Installiert nach | Anmerkungen |
|---|---|---|
| `claude` (Standard) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex liest Prompts nur aus dem nutzerweiten Verzeichnis, keine projektlokale Option; OpenAIs Dokumentation markiert diesen Mechanismus als zugunsten von "Skills" veraltet, er funktioniert aber weiterhin |
| `gemini` | `.gemini/commands/domain-expert.toml` | TOML-Format |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf nennt das "Workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | Amps Speicherort ist fest im Repo-Root, kein separates globales Verzeichnis |

Fügen Sie `--global` hinzu, um in das nutzerweite Verzeichnis des Tools zu installieren (z. B. `~/.claude/commands/`, `~/.cursor/commands/`) statt in das Projektverzeichnis, oder `--to <path>` für einen vollständig eigenen Ort.

### CLI-Referenz

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` bewertet Rollen nach Stichwortüberschneidung und meldet einen sicheren Treffer, Kandidaten mit geringer Zuversicht oder ein ehrliches "noch nicht abgedeckt" — es rät nicht stillschweigend. `--json` für programmatische Nutzung.

Das npm-Paket friert die Rollenbibliothek bei jedem Release als Schnappschuss ein. Für den unveröffentlichten aktuellsten Stand nutzen Sie `npx --yes github:wonsukchoi/domain-experts <command>` — dieselbe CLI, direkt von `main`.

### Automatisierung für Maintainer (Claude Code)

Arbeitet man in einem Claude-Code-Checkout dieses Repos, kommen drei Slash-Befehle hinzu, die die obige Pipeline automatisieren, statt sie zu ersetzen — jeder einzelne ist durch eine von Menschen geprüfte PR abgesichert, keiner committet auf `main` oder veröffentlicht von sich aus:

- `/generate-role "<need>"` — löst einen frei formulierten Bedarf zu einer bestehenden Rolle, einem neuen Spezialisierungs-Blatt oder einer neuen übergeordneten Rolle auf und durchläuft dann die AUTHORING.md-Pipeline Pass 0-4 (Recherche → Entwurf → adversariale Kritik → Bewertung, begrenzt auf 2 Überarbeitungsschleifen) und eröffnet eine PR.
- `/audit-roles [batchSize]` — gestaffelte Neubewertung veröffentlichter Rollen anhand der Rubrik und der Aktualität der Quellen; stempelt `last_audited`/`audit_score`, markiert `status: needs-refresh`, depubliziert (verschiebt nach `roles/_deprecated/`) nach einem zweiten aufeinanderfolgenden Fehlschlag.
- `/scan-project <path>` — rein lesender Scan eines externen Projekts (Stack, README, Struktur, letzte Commits), schlägt Kandidaten-Bedarfe vor, die mit der bestehenden Abdeckung abgeglichen werden, und übergibt die ausgewählten an `/generate-role`. Nichts über das gescannte Projekt wird irgendwo gespeichert.

Nicht eindeutige `match`-Anfragen werden in `data/gap-log.jsonl` protokolliert und, nach Häufigkeit sortiert, im Abschnitt „Requested but missing" von [`ROADMAP.md`](./ROADMAP.md) angezeigt — ein konkretes Signal dafür, was als Nächstes entworfen werden sollte.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) ist der Master-Backlog — alle 1.016 O*NET-Berufe, nach Kategorie gruppiert, abgehakt, sobald sie entworfen sind. Nutzen Sie ihn, um eine noch nicht abgedeckte Rolle zu finden, statt zu raten, was fehlt.

## Mitwirken — dieses Repo wächst mit Zinseszins

Jede hinzugefügte Rolle macht den Router schlauer, jede Korrektur erreicht beim nächsten Release alle Nutzer, und jede Eval-Frage macht es schwerer, die Qualitätslatte vorzutäuschen. Ein Prompt, den Sie für sich selbst schreiben, stirbt mit Ihrer Sitzung; eine Rolle, die Sie hier beitragen, funktioniert für alle, für immer, und wird besser, nachdem Sie gegangen sind. Das ist die ganze Wette: **1.016 Berufe sind kein Solo-Projekt — sie sind ein Gemeingut (Commons).**

Häufige Fragen (Lint-Fehler, Push-Konflikte, Release-Prozess) → [`docs/FAQ.md`](./docs/FAQ.md).

Drei Wege einzusteigen, unabhängig vom Kenntnisstand:

1. **Sie arbeiten in einer Rolle, die wir abdecken?** Lesen Sie sie. Alles, was falsch ist, ist ein 2-Minuten-[Praktiker-Korrektur-Issue](../../issues/new/choose) — der wertvollste Beitrag, den dieses Projekt erhalten kann. Keine PR-Kenntnisse nötig.
2. **Sie möchten eine Rolle schreiben oder aufwerten?** Folgen Sie dem exakten Rezept in [`CONTRIBUTING.md`](./CONTRIBUTING.md) — es ist so präzise geschrieben, dass ein LLM es ausführen kann, sodass Sie und Ihr AI-Assistent es gemeinsam erledigen können. Der Linter sagt Ihnen, bevor irgendein Mensch prüft, ob die Struktur nicht ausreicht. 42 Legacy-Rollen sind [gerade jetzt beanspruchbar](../../issues/1).
3. **Sie können nicht schreiben, aber finden?** Sammeln Sie Paritätsfragen (`evals/parity/harvest_stackexchange.py`) oder reichen Sie eine [Rollenanfrage](../../issues/new/choose) mit den Aufgaben ein, die Sie an sie delegieren würden.

Wenn die Spezifikation der Realität eines Praktikers widerspricht, verliert die Spezifikation — sagen Sie das in Ihrem PR, und wir korrigieren die Spezifikation.

## Lizenz

MIT — siehe [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
