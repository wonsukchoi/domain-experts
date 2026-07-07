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

Bibliothèque open source de **définitions de rôles professionnels** — les modèles mentaux réels, les seuils de décision et les modes d'échec de véritables praticiens, structurés pour qu'un agent IA puisse en charger un et raisonner comme cet expert. Demandez à votre agent de « relire ce contrat » et il vous répond avec la stratégie de traitement des clauses et les positions de repli d'un avocat d'affaires senior, pas avec le résumé générique d'un généraliste.

**Aller à :** [Démarrage rapide](#démarrage-rapide) · [« Pourquoi ne pas simplement le demander à Claude ? »](#pourquoi-ne-pas-simplement-dire-à-claude-dagir-comme-un-directeur-financier) · [Vision](#vision--une-personne-tous-les-experts) · [Comment les rôles sont construits](#comment-les-rôles-sont-construits) · [Comment nous vérifions](#comment-nous-vérifions--transparent-aucune-confiance-aveugle-requise) · [Rôles actuels](#rôles-actuels) · [Utiliser avec votre outil](#utiliser-avec-votre-outil-ia) · [Feuille de route](#feuille-de-route) · [Contribuer](#contribuer--ce-dépôt-fonctionne-par-intérêts-composés)

## Démarrage rapide

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

Aucune installation nécessaire — `npx` le récupère directement depuis npm. Vous l'utilisez souvent ? Faites `npm install -g domain-experts` et laissez tomber le `npx`.

**Vous utilisez Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code ou Amp ?** `npx domain-experts command --tool <id>` installe une commande slash `/domain-expert` pour votre outil — redémarrez votre session et lancez `/domain-expert review this vendor contract`. Elle trouve le bon rôle, le charge, et raisonne comme lui en une seule étape, sans passer manuellement par `match` puis `add`.

> **Si vous faites un `git clone` de ce dépôt au lieu d'utiliser la CLI :** ne pointez pas la découverte de skills de votre outil directement vers `roles/`. Ce répertoire contient plus de 200 fichiers `SKILL.md` individuels, et la plupart des outils (dont Claude Code) chargent le nom et la description de chaque skill découvert dans le prompt système de base — vous paieriez ce coût en tokens à chaque session pour des rôles que vous n'utilisez jamais. Installez uniquement [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) (ou utilisez les commandes `add`/`init` de la CLI, qui font la même chose) — c'est un unique skill léger qui lit un `roles/<slug>/SKILL.md` précis à la demande, uniquement quand une tâche en a réellement besoin.

Ou sautez complètement l'étape manuelle : chargez une fois [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md), et votre agent détecte de lui-même quel expert la tâche nécessite, récupère automatiquement le contexte complet du rôle, et vous dit honnêtement quand un rôle n'est pas encore couvert plutôt que d'improviser. Vous continuez à travailler ; l'expertise adéquate apparaît d'elle-même.

## « Pourquoi ne pas simplement dire à Claude d'agir comme un directeur financier ? »

Vous pouvez — et vous obtiendrez une imitation superficielle : la moyenne de toutes les fiches de poste trouvées sur Internet, régénérée à partir de zéro à chaque session, différente à chaque fois, vérifiée par personne.

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

La différence, concrètement :

- **Contenu non dérivable.** Chaque rôle doit réussir un test de non-dérivabilité : rien de ce qui peut être régénéré à partir du seul intitulé du poste. Ce qui reste, c'est ce qu'un prompt ne peut pas produire à la demande — seuils numériques de signaux d'alerte, fourchettes de négociation conformes au marché, exemples travaillés dont l'arithmétique se recoupe, positions de repli classées par ordre de préférence.
- **Un filtre qualité, pas une génération unique.** Les rôles sont construits via un pipeline multi-passes ([`AUTHORING.md`](./AUTHORING.md)) — voir le schéma ci-dessous. Un prompt d'une ligne n'obtient rien de tout cela.
- **Structure imposée par la CI.** Chaque PR exécute [`scripts/lint_roles.py`](./scripts/lint_roles.py) : schéma, sections obligatoires, liens qui résolvent, formules creuses interdites, exhaustivité des signaux d'alerte, chiffres réels dans l'exemple travaillé. Un texte de fiche de poste générique fait échouer le build.
- **Ça s'accumule avec intérêts composés.** Votre prompt improvisé disparaît à la fin de la session. Ces fichiers, eux, accumulent les corrections des praticiens, suivent une échelle de maturité (`draft` → `reviewed-by-practitioner` → `mature`) et une spec versionnée (`spec: 2` marque les rôles au niveau actuel), et s'améliorent à chaque PR. Les corrections profitent à tout le monde.
- **Conçu pour l'efficacité en tokens.** Chaque rôle est un noyau de raisonnement compact (`SKILL.md`) plus une profondeur à la demande (`references/`). L'agent ne paie cette profondeur que lorsque la tâche en a besoin :

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### Alors, c'est quoi la vraie barrière à l'entrée ?

Objection légitime : rien de tout ça n'empêche quelqu'un de faire un `git clone` de ce dépôt exact et de le vendre comme son propre produit — licence MIT, aucun verrouillage de contenu. Réponse honnête : l'ensemble des fichiers n'est pas la barrière. Ce qui est difficile à copier, c'est la machine qui continue à le produire et à le corriger :

- **Le pipeline, pas le résultat.** Copier 97 fichiers prend une commande. Copier la boucle de rédaction critique adverse → grille à 9 critères → verrouillée par le lint ([`AUTHORING.md`](./AUTHORING.md)) qui continue à les produire et à les corriger, ça ne se copie pas — un fork hérite de l'instantané d'aujourd'hui, pas des correctifs de demain.
- **Un standard, pas une base de données.** `SKILL.md` fonctionne déjà dans plus de 30 outils agentiques. Être la plus grande bibliothèque dans un format ouvert et portable, c'est une position de distribution, pas une position de contenu — la valeur est d'être la réponse par défaut que les gens trouvent, pas dans les octets eux-mêmes.
- **Vérifié, pas prétendu.** N'importe quel concurrent peut dire « écrit par des experts ». Peu peuvent lancer `python3 evals/run_evals.py` devant vous et montrer 13/15 victoires en contrefactuel. Ici, la confiance est mesurée et reproductible, pas affirmée.
- **La fraîcheur bat la mémoire paramétrique.** Même si un futur modèle s'entraîne sur le texte public de ce dépôt, cette connaissance se fige à la date limite d'entraînement. Les corrections de ce dépôt sont publiées le jour même où un praticien les signale — sans cycle de réentraînement, versionnées, tracées à une source.
- **Discipline de couverture.** L'ossature de 1 016 métiers d'O*NET impose une couverture systématique de la longue traîne (funeral-home-manager, wind-energy-operations-manager) qu'un concurrent opportuniste, qui ne curerait que les rôles à la mode, ne prendra pas la peine de suivre.
- **Gratuit et portable bat l'abonnement verrouillé.** Ceci ne concurrence pas votre facture de LLM — vous payez l'inférence de toute façon. Ça concurrence les SaaS verticaux fermés (« conseiller juridique IA », 99 $/mois) : ceux-là ne peuvent pas rivaliser avec du gratuit, forkable, exécutable sur un modèle local à coût récurrent nul.

Rien de tout cela n'est encore une barrière à l'entrée à 97 rôles et une petite base de contributeurs — c'est une trajectoire. Le pari : les biens communs s'accumulent plus vite que n'importe quel fork ne peut suivre, une fois qu'assez de praticiens signalent des corrections au lieu d'écrire des prompts à partir de zéro à chaque session.

## Vision — une personne, tous les experts

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

Aujourd'hui, faire bien quelque chose en dehors de son propre domaine implique d'embaucher, de contracter, ou de faire du démarchage — trouver un avocat, attendre l'agenda d'un directeur financier, payer le tarif d'un stratège marketing. Cette friction est une taxe qui pèse sur chaque fondateur solo, chaque petite équipe, chaque individu confronté à un problème hors de son expertise. La plupart des gens ne font tout simplement pas la chose, ou la font mal.

Un individu avec un abonnement IA — ou un modèle local, sans abonnement du tout — et ce dépôt ne paie pas cette taxe. Chargez le raisonnement réel du directeur financier pour une décision de trésorerie. Chargez la stratégie de traitement des clauses de l'avocat d'affaires pour une relecture de contrat. Chargez le jugement du coordinateur de recherche clinique pour un écart de protocole. Changez de rôle selon la tâche, à la demande, pour le coût de l'inférence plutôt que celui d'une embauche. Une personne, un agent, la prise de décision accumulée de centaines de métiers.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

C'est là le véritable objectif final, pas une simple curiosité : la barrière entre « j'ai besoin d'un expert » et « j'en ai un » s'effondre. Cela devient de plus en plus vrai à mesure que la couverture s'étend — 92 rôles sur 1 016 métiers suivis aujourd'hui ; la feuille de route existe pour combler cet écart, pas pour rester indéfiniment intéressante.

Cela ne remplace pas le jugement, la responsabilité, ni les habilitations légales là où celles-ci doivent revenir à un humain — chaque rôle réglementé (droit, médecine, finance) le dit explicitement. Ce que ça remplace, c'est la friction de ne pas avoir accès au raisonnement en premier lieu.

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

## Comment les rôles sont construits

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Chaque rôle suit le même contrat, imposé par la spec et la CI :

1. **Trois tests de mise en production** — un praticien qui lit le rôle hoche la tête au lieu de hausser les épaules ; un agent avec ce rôle prend des décisions mesurablement différentes de celles qu'il prendrait sans ; rien dans le rôle n'est dérivable du seul intitulé du poste.
2. **Anatomie fixe** — identité, noyau de premiers principes, heuristiques conditionnelles (« si X, alors par défaut Y sauf si Z »), un cadre de décision exécutable, les modes d'échec courants, et un exemple travaillé avec des chiffres réels et cohérents se terminant par le livrable concret (le mémo, la relecture, le compte rendu).
3. **Trio de références** — un fichier d'approfondissement/de modèles remplis, `red-flags.md` (signal → signification → première question → données à consulter), et `vocabulary.md` (termes techniques avec l'erreur d'usage courante précisée).
4. **Provenance** — les sources sont nommées ; les chiffres précis se retracent jusqu'à elles ou sont étiquetés comme heuristiques déclarées. Les rôles réglementés (droit, médecine, finance) portent des avertissements explicites.
5. **Ossature O*NET** — la couverture suit la taxonomie des métiers du Département du Travail des États-Unis (1 016 métiers), afin que la croissance soit systématique, et non fonction de ce qui semblait intéressant cette semaine-là.

Spec complète, grille d'évaluation, et pipeline de rédaction assistée par LLM : [`AUTHORING.md`](./AUTHORING.md). Dans un checkout Claude Code, tout ce pipeline s'exécute via `/generate-role "<need>"` — voir [Automatisation pour les mainteneurs](#maintainer-automation-claude-code) ci-dessous.

## Comment nous vérifions — transparent, aucune confiance aveugle requise

« Écrit par des experts » est une affirmation ; ce dépôt fournit les preuves à la place. Quatre couches indépendantes, toutes exécutables par n'importe qui à partir de ce checkout :

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

Derniers résultats publiés (2026-07-06, Haiku 4.5 répondant, Sonnet 5 jugeant en aveugle, les deux harnais) :

- **Contrefactuel :** le skill l'emporte dans **13/15 scénarios** (1 égalité, 1 défaite) — 72 % des critères de comportement expert atteints contre 37 % pour la base de référence généraliste.
- **Parité face aux humains :** réponse du skill préférée à celle du praticien réel, acceptée sur Stack Exchange, dans **5 duels sur 8** en aveugle (échantillon faible ; les ensembles de questions s'étoffent — à considérer comme un signal, pas une étude).

Chaque résultat est reproductible : `python3 evals/run_evals.py` et `python3 evals/parity/run_parity.py`. Quand un rôle échoue à ces tests, c'est public aussi — le but est la mesure, pas le marketing. La relecture par un praticien reste l'étoile d'or au sommet (`metadata.maturity`), mais le seuil de confiance est mesuré, pas simplement garanti sur parole.

## Rôles actuels

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

Ce bloc est généré automatiquement — lancez `python3 scripts/generate_roadmap.py` après avoir ajouté, supprimé ou remappé un rôle ; ne le modifiez jamais à la main.

## Utiliser avec votre outil IA

`SKILL.md` est un format compatible entre outils — le même fichier de rôle fonctionne dans Claude Code, Codex CLI, Cursor, et plus de 30 autres agents. Seul le répertoire d'installation change.

### Zéro configuration : collez ceci dans votre agent

Copiez ceci dans Claude Code, Codex, Cursor, ou tout agent ayant accès au shell, décrivez votre tâche en bas, et il installe le bon expert tout seul :

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

**Utilisateurs de Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code et Amp :** pas besoin de coller quoi que ce soit — `npx domain-experts command --tool <id>` installe `/domain-expert` une seule fois, puis lancez simplement `/domain-expert <task>` à chaque fois (voir [la commande slash `/domain-expert`](#commande-slash-domain-expert) ci-dessous).

### Installation par outil

| Outil | Comment |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — atterrit dans `./.claude/skills/<slug>/`, reconnu automatiquement comme un skill. |
| **Codex CLI** | Même commande avec `--to .codex/skills/<slug>` (projet) ou `--to ~/.codex/skills/<slug>` (personnel). Une nouvelle session le reconnaît. |
| **Cursor** | Même commande avec `--to .cursor/skills/<slug>` — Cursor lit nativement le même format `SKILL.md`. |
| **Windsurf, Roo Code, Goose et autres outils compatibles SKILL.md** | Même commande avec `--to <répertoire de skills de l'outil>/<slug>` — vérifiez la documentation de votre outil pour le chemin exact. |
| **Outils qui lisent `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Installez n'importe où dans le dépôt (par ex. `--to skills/<slug>`), puis ajoutez une ligne à `AGENTS.md` : `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **N'importe quel chat IA (sans shell)** | Ouvrez le rôle sur GitHub, collez `SKILL.md` dans le prompt système ou les instructions personnalisées ; collez les fichiers de `references/` quand la conversation nécessite cette profondeur. |

Chaque installation copie le rôle complet — `SKILL.md` plus `references/` — pour que les playbooks approfondis voyagent avec lui.

### Répartition automatique

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) est un méta-skill qui supprime même l'étape `match` — installez-le avec `npx domain-experts add domain-expert-router`, chargez-le une fois, et votre agent trouve tout seul le bon rôle pour les demandes du type « agis comme X », et vous dit honnêtement quand un rôle n'est pas encore couvert.

### Commande slash `/domain-expert`

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Redémarrez votre session, puis utilisez directement `/domain-expert <task>` — par exemple `/domain-expert review this vendor contract`. Elle exécute `match`, charge le `SKILL.md` du rôle gagnant (et `references/` si besoin), et répond en tant que cet expert, ou vous dit honnêtement que rien ne correspond encore. Même principe que le skill routeur ci-dessus, packagé comme une commande à usage unique plutôt qu'un skill toujours chargé.

| `--tool` | Installe dans | Notes |
|---|---|---|
| `claude` (par défaut) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex ne lit les prompts que depuis le répertoire au niveau utilisateur, aucune option projet-local ; la documentation d'OpenAI marque ce mécanisme comme obsolète au profit des « skills », mais il fonctionne encore |
| `gemini` | `.gemini/commands/domain-expert.toml` | Format TOML |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf appelle ça des « workflows » |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | L'emplacement d'Amp est fixé à la racine du dépôt, sans répertoire global séparé |

Ajoutez `--global` pour installer dans le répertoire au niveau utilisateur de l'outil (par ex. `~/.claude/commands/`, `~/.cursor/commands/`) plutôt que dans le répertoire du projet, ou `--to <path>` pour un emplacement entièrement personnalisé.

### Référence CLI

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` note les rôles par recouvrement de mots-clés et vous indique une correspondance sûre, des candidats à faible confiance, ou un honnête « pas encore couvert » — il ne devine jamais en silence. `--json` pour un usage programmatique.

Le paquet npm capture un instantané de la bibliothèque de rôles à chaque sortie. Pour la version de pointe non publiée, utilisez `npx --yes github:wonsukchoi/domain-experts <command>` — même CLI, directement depuis `main`.

### Automatisation pour les mainteneurs (Claude Code)

Travailler dans un checkout Claude Code de ce dépôt ajoute trois commandes slash qui automatisent le pipeline ci-dessus sans le remplacer — chacune est soumise à validation humaine via PR, aucune ne commit sur `main` ni ne publie de sa propre initiative :

- `/generate-role "<need>"` — résout un besoin en texte libre vers un rôle existant, une nouvelle feuille de spécialisation, ou un nouveau rôle parent, puis exécute le pipeline Pass 0-4 d'AUTHORING.md (recherche → rédaction → critique adverse → notation, plafonné à 2 boucles de révision) et ouvre une PR.
- `/audit-roles [batchSize]` — renotation par lots des rôles publiés au regard de la grille d'évaluation et de la fraîcheur des sources ; horodate `last_audited`/`audit_score`, marque `status: needs-refresh`, déprécie (déplace vers `roles/_deprecated/`) après un deuxième échec consécutif.
- `/scan-project <path>` — scan en lecture seule d'un projet externe (stack, README, structure, commits récents), propose des besoins candidats recoupés avec la couverture existante, et transmet ceux que vous choisissez à `/generate-role`. Rien du projet scanné n'est écrit où que ce soit.

Les requêtes `match` peu sûres sont journalisées dans `data/gap-log.jsonl` et remontées, classées par fréquence, dans la section « Requested but missing » de [`ROADMAP.md`](./ROADMAP.md) — un signal concret de ce qu'il faut rédiger ensuite.

## Feuille de route

[`ROADMAP.md`](./ROADMAP.md) est le backlog principal — les 1 016 métiers O*NET, regroupés par catégorie, cochés au fur et à mesure qu'ils sont rédigés. Utilisez-le pour trouver un rôle non couvert plutôt que de deviner ce qui manque.

## Contribuer — ce dépôt fonctionne par intérêts composés

Chaque rôle ajouté rend le routeur plus intelligent, chaque correction profite à tous les utilisateurs dès la prochaine version, et chaque question d'évaluation rend la barre de qualité plus difficile à tricher. Un prompt que vous écrivez pour vous-même meurt avec votre session ; un rôle que vous contribuez ici fonctionne pour tout le monde, pour toujours, et continue de s'améliorer après votre départ. C'est tout le pari : **1 016 métiers, ce n'est pas un projet solo — c'est un bien commun.**

Questions fréquentes (échecs de lint, conflits de push, processus de sortie) → [`docs/FAQ.md`](./docs/FAQ.md).

Trois façons de contribuer, quel que soit votre niveau :

1. **Vous travaillez dans un rôle que nous couvrons ?** Lisez-le. Toute erreur constitue une [issue de correction par un praticien](../../issues/new/choose) de deux minutes — la contribution la plus précieuse que ce projet puisse recevoir. Aucune compétence en PR nécessaire.
2. **Vous voulez écrire ou améliorer un rôle ?** Suivez la recette exacte dans [`CONTRIBUTING.md`](./CONTRIBUTING.md) — elle est écrite avec une précision telle qu'un LLM peut l'exécuter, donc vous et votre assistant IA pouvez le faire ensemble. Le lint vous indique si la structure est insuffisante avant même qu'un humain ne la relise. 42 rôles hérités sont [disponibles à revendiquer dès maintenant](../../issues/1).
3. **Vous ne savez pas écrire mais savez chercher ?** Récoltez des questions de parité (`evals/parity/harvest_stackexchange.py`) ou déposez une [demande de rôle](../../issues/new/choose) avec les tâches que vous lui délègueriez.

Si la spec entre en conflit avec la réalité d'un praticien, c'est la spec qui perd — dites-le dans votre PR et nous corrigerons la spec.

## Licence

MIT — voir [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
