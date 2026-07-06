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

Biblioteca open source de **definições de papéis profissionais** — os modelos mentais reais, os limiares de decisão e os modos de falha de profissionais de verdade, estruturados para que qualquer agente de IA possa carregar um deles e raciocinar como aquele especialista. Peça ao seu agente para "revisar este contrato" e ele responde com o manual de cláusulas e as escadas de recuo de um advogado sênior de contratos, não com o resumo genérico da internet de um generalista.

**Vá direto para:** [Início rápido](#início-rápido) · ["Por que não simplesmente pedir para o agente agir como?"](#não-basta-pedir-para-o-claude-agir-como-um-cfo) · [Visão](#visão--uma-pessoa-todos-os-especialistas) · [Como os papéis são construídos](#como-os-papéis-são-construídos) · [Como verificamos](#como-verificamos--transparente-sem-necessidade-de-confiança) · [Papéis atuais](#papéis-atuais) · [Use com sua ferramenta](#use-com-sua-ferramenta-de-ia) · [Roteiro](#roteiro) · [Contribuindo](#contribuindo--este-repositório-se-multiplica)

## Início rápido

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # instala em ./.claude/skills/
```

Não precisa instalar nada — o `npx` busca direto do npm. Usa com frequência? `npm install -g domain-experts` e tire o `npx` do comando.

**Usa Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code ou Amp?** `npx domain-experts command --tool <id>` instala um comando de barra `/domain-expert` para a sua ferramenta — reinicie a sessão e rode `/domain-expert review this vendor contract`. Ele encontra o papel certo, carrega e raciocina como esse especialista em uma única etapa, sem o vaivém manual de `match`/`add`.

Ou pule a etapa manual por completo: carregue [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) uma vez, e seu agente detecta sozinho de qual especialista a tarefa precisa, puxa automaticamente o contexto completo do papel e avisa com honestidade quando um papel ainda não está coberto, em vez de improvisar. Você continua trabalhando; a expertise certa aparece por conta própria.

## "Não basta pedir para o Claude agir como um CFO?"

Você pode pedir — e vai receber uma imitação rasa: a média de todas as descrições de vaga da internet, regenerada do zero a cada sessão, diferente toda vez, verificada por ninguém.

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

A diferença, em termos concretos:

- **Conteúdo não derivável.** Todo papel precisa passar em um teste de não-derivabilidade: nada que possa ser regenerado a partir só do título do cargo. O que sobra é exatamente o que um prompt não consegue produzir sob demanda — limiares numéricos de alerta, faixas de negociação padrão de mercado, exemplos resolvidos com aritmética que fecha, posições de recuo em ordem de preferência.
- **Um filtro de qualidade, não uma única geração.** Os papéis são construídos por um pipeline de múltiplas etapas ([`AUTHORING.md`](./AUTHORING.md)) — veja o diagrama abaixo. Um prompt de uma linha não passa por nada disso.
- **Estrutura garantida por CI.** Todo PR roda [`scripts/lint_roles.py`](./scripts/lint_roles.py): esquema, seções obrigatórias, links que resolvem, frases de preenchimento banidas, completude dos sinais de alerta, números reais no exemplo resolvido. Texto genérico de descrição de vaga reprova o build.
- **Isso se acumula.** Seu prompt improvisado desaparece quando a sessão termina. Esses arquivos acumulam correções de profissionais, carregam uma escada de maturidade (`draft` → `reviewed-by-practitioner` → `mature`) e uma especificação versionada (`spec: 2` marca papéis no padrão atual), e melhoram a cada PR. As correções alcançam todo mundo.
- **Eficiente em tokens por design.** Cada papel é um núcleo de raciocínio compacto (`SKILL.md`) mais profundidade sob demanda (`references/`). O agente só "paga" pela profundidade quando a tarefa precisa dela:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### Então qual é a vantagem competitiva de verdade?

Contraponto justo: nada do que foi dito acima impede que alguém faça `git clone` deste exato repositório e o lance como produto próprio — licença MIT, zero trava de conteúdo. Resposta honesta: o conjunto de arquivos não é a vantagem competitiva. O que é difícil de copiar é a máquina que continua produzindo e corrigindo isso:

- **O pipeline, não o resultado.** Copiar 97 arquivos leva um comando. Copiar o ciclo de crítica adversarial → rubrica de 9 critérios → autoria travada por lint ([`AUTHORING.md`](./AUTHORING.md)) que continua produzindo e corrigindo esses arquivos não leva — um fork herda a foto de hoje, não as correções de amanhã.
- **Um padrão, não um banco de dados.** O `SKILL.md` já roda em mais de 30 ferramentas de agente. Ser a maior biblioteca em um formato aberto e portátil é uma posição de distribuição, não uma posição de conteúdo — o valor está em ser a resposta padrão que as pessoas encontram, não nos bytes em si.
- **Verificado, não apenas alegado.** Qualquer concorrente pode dizer "escrito por especialistas". Poucos conseguem rodar `python3 evals/run_evals.py` na sua frente e mostrar 13/15 vitórias contrafactuais. A confiança aqui é medida e reproduzível, não afirmada.
- **Atualidade vence recall paramétrico.** Mesmo que um futuro modelo seja treinado com o texto público deste repositório, esse conhecimento congela na data de corte do treinamento. As correções deste repositório entram no ar no mesmo dia em que um profissional as registra — sem ciclo de retreinamento, com versão e rastreadas até a fonte.
- **Disciplina de cobertura.** A espinha dorsal de 1.016 ocupações da O*NET força uma cobertura sistemática de cauda longa (gerente de funerária, operador de energia eólica) que um concorrente oportunista, que só cura papéis em alta, não vai se dar ao trabalho de igualar.
- **Grátis e portátil vence trava por assinatura.** Isso não compete com sua conta de LLM — você continua pagando pela inferência de qualquer forma. Compete com SaaS vertical fechado ("Consultor Jurídico com IA", US$ 99/mês): esses não conseguem igualar grátis, forkável e rodável em modelo local sem custo recorrente.

Nada disso é uma vantagem competitiva ainda com 97 papéis e uma base pequena de contribuidores — é uma trajetória. A aposta: os bens comuns se multiplicam mais rápido do que qualquer fork isolado consegue acompanhar, assim que profissionais suficientes passarem a registrar correções em vez de escrever prompts do zero a cada sessão.

## Visão — uma pessoa, todos os especialistas

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

Hoje, fazer bem algo fora da sua própria área significa contratar, subcontratar ou buscar contatos — encontrar um advogado, esperar na agenda de um CFO, pagar a diária de um estrategista de marketing. Essa fricção é um imposto que recai sobre todo fundador solo, toda equipe pequena, qualquer pessoa que esbarra em um problema fora da sua expertise. Na maioria das vezes, a pessoa simplesmente não faz a tarefa, ou faz mal feito.

Uma pessoa com uma assinatura de IA — ou até um modelo local, sem assinatura nenhuma — e este repositório não paga esse imposto. Carregue o raciocínio real do CFO para uma decisão sobre runway. Carregue o manual de cláusulas do advogado de contratos para uma redação de ajustes. Carregue o julgamento do coordenador de pesquisa clínica para um desvio de protocolo. Troque de papel conforme a tarefa, sob demanda, pelo custo da inferência em vez do custo de uma contratação. Uma pessoa, um agente, o julgamento acumulado de centenas de profissões.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

Esse é o verdadeiro objetivo final aqui, não uma curiosidade: a barreira entre "preciso de um especialista" e "eu tenho um" desaba. E isso fica mais real à medida que a cobertura cresce — 92 papéis contra 1.016 ocupações rastreadas hoje; o roteiro existe para que essa lacuna se feche, não para continuar interessante para sempre.

Isso não substitui o julgamento, a responsabilidade nem a licença profissional onde estes precisam legalmente recair sobre um humano — todo papel regulado (direito, medicina, finanças) diz isso explicitamente. O que ele substitui é a fricção de não ter acesso ao raciocínio, para começo de conversa.

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

## Como os papéis são construídos

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Todo papel segue o mesmo contrato, garantido por especificação e CI:

1. **Três testes de aprovação** — um profissional que lê o papel concorda com a cabeça em vez de dar de ombros; um agente com o papel toma decisões mensuravelmente diferentes do que sem ele; nada nele é derivável apenas do título do cargo.
2. **Anatomia fixa** — identidade, núcleo de primeiros princípios, heurísticas condicionais ("quando X, o padrão é Y a menos que Z"), um framework de decisão executável, modos de falha comuns e um exemplo resolvido com números reais e que fecham, terminando no entregável de fato (o memorando, a redação de ajustes, o relatório).
3. **Trio de referências** — um arquivo de aprofundamento com manual/artefatos preenchidos, `red-flags.md` (sinal → o que significa → primeira pergunta → dado a buscar) e `vocabulary.md` (termos técnicos com o uso incorreto comum explicado).
4. **Proveniência** — as fontes são nomeadas; números específicos remetem a elas ou são identificados como heurísticas declaradas. Papéis regulados (direito, medicina, finanças) trazem avisos explícitos.
5. **Espinha dorsal O*NET** — a cobertura acompanha a taxonomia de ocupações do Departamento do Trabalho dos EUA (1.016 ocupações), então o crescimento é sistemático, não o que pareceu interessante naquela semana.

Especificação completa, rubrica e o pipeline de redação por LLM: [`AUTHORING.md`](./AUTHORING.md).

## Como verificamos — transparente, sem necessidade de confiança

"Escrito por especialistas" é uma alegação; este repositório entrega os comprovantes em vez disso. Quatro camadas independentes, todas executáveis por qualquer pessoa a partir deste checkout:

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

Últimas execuções publicadas (2026-07-06, Haiku 4.5 respondendo, Sonnet 5 julgando às cegas, em ambos os harnesses):

- **Contrafactual:** o skill vence em **13/15 cenários** (1 empate, 1 derrota) — 72% dos critérios de comportamento de especialista atingidos, contra 37% da linha de base generalista.
- **Paridade com humanos:** a resposta do skill foi preferida em relação à resposta aceita de um profissional real no Stack Exchange em **5 de 8** comparações cegas cabeça a cabeça (amostra pequena; os conjuntos de perguntas estão crescendo — trate como um sinal indicativo, não um estudo).

Todo resultado é reproduzível: `python3 evals/run_evals.py` e `python3 evals/parity/run_parity.py`. Quando um papel falha nesses testes, isso também é público — o ponto é medição, não marketing. A revisão por profissionais continua sendo a estrela-de-ouro no topo (`metadata.maturity`), mas o piso de confiança é medido, não simplesmente confirmado por alguém.

## Papéis atuais

<!-- ROLE_COUNTS_START -->
**105 roles drafted** (101 mapped to an O*NET occupation, 4 custom; 63 at spec 2, 42 awaiting upgrade), across 10 categories:

- **design**: 2
- **engineering**: 17
- **finance**: 10
- **healthcare**: 8
- **legal**: 11
- **marketing**: 4
- **operations**: 43
- **other**: 4
- **product**: 1
- **sales**: 5

Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.
<!-- ROLE_COUNTS_END -->

Este bloco é gerado automaticamente — rode `python3 scripts/generate_roadmap.py` depois de adicionar/remover/remapear um papel, não o edite manualmente.

## Use com sua ferramenta de IA

O `SKILL.md` é um formato multiferramenta — o mesmo arquivo de papel funciona no Claude Code, Codex CLI, Cursor e mais de 30 outros agentes. Só o diretório de instalação muda.

### Zero configuração: cole isto no seu agente

Cole isto no Claude Code, Codex, Cursor ou qualquer agente com acesso a shell, descreva sua tarefa no final, e ele instala o especialista certo sozinho:

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

**Usuários de Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code e Amp:** pule a colagem manual — `npx domain-experts command --tool <id>` instala o `/domain-expert` uma vez, depois é só rodar `/domain-expert <tarefa>` a cada vez (veja [comando de barra `/domain-expert`](#comando-de-barra-domain-expert) abaixo).

### Instalação por ferramenta

| Ferramenta | Como |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — vai para `./.claude/skills/<slug>/`, reconhecido automaticamente como skill. |
| **Codex CLI** | Mesmo comando com `--to .codex/skills/<slug>` (projeto) ou `--to ~/.codex/skills/<slug>` (pessoal). Uma nova sessão já reconhece. |
| **Cursor** | Mesmo comando com `--to .cursor/skills/<slug>` — o Cursor lê nativamente o mesmo formato `SKILL.md`. |
| **Windsurf, Roo Code, Goose e outras ferramentas compatíveis com `SKILL.md`** | Mesmo comando com `--to <diretório de skills da sua ferramenta>/<slug>` — confira o caminho na documentação da sua ferramenta. |
| **Ferramentas que leem `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Instale em qualquer lugar do repositório (ex.: `--to skills/<slug>`), depois acrescente uma linha ao `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Qualquer chat de IA (sem shell)** | Abra o papel no GitHub, cole o `SKILL.md` no prompt de sistema ou nas instruções personalizadas; cole os arquivos de `references/` quando a conversa precisar dessa profundidade. |

Toda instalação copia o papel completo — `SKILL.md` mais `references/` — para que os manuais de aprofundamento viajem junto.

### Despacho automático

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) é um meta-skill que elimina até a etapa de `match` — instale-o com `npx domain-experts add domain-expert-router`, carregue-o uma vez, e seu agente encontra sozinho o papel certo para pedidos do tipo "aja como X", e avisa com honestidade quando um papel ainda não está coberto.

### Comando de barra `/domain-expert`

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Reinicie a sessão e depois use `/domain-expert <tarefa>` diretamente — por exemplo, `/domain-expert review this vendor contract`. Ele roda o `match`, carrega o `SKILL.md` do papel vencedor (e `references/` conforme necessário) e responde como esse especialista, ou avisa com honestidade quando nada corresponde ainda. Mesma ideia do skill de roteamento acima, empacotada como um comando de um único disparo em vez de um skill sempre carregado.

| `--tool` | Instala em | Notas |
|---|---|---|
| `claude` (padrão) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | O Codex só lê prompts do diretório em nível de usuário, sem opção local ao projeto; a documentação da OpenAI marca esse mecanismo como descontinuado em favor de "skills", mas ainda funciona |
| `gemini` | `.gemini/commands/domain-expert.toml` | Formato TOML |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | O Windsurf chama isso de "workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | A localização do Amp é fixa na raiz do repositório, sem diretório global separado |

Adicione `--global` para instalar no diretório de nível de usuário da ferramenta (ex.: `~/.claude/commands/`, `~/.cursor/commands/`) em vez do diretório do projeto, ou `--to <caminho>` para um local totalmente personalizado.

### Referência da CLI

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

O `match` pontua os papéis por sobreposição de palavras-chave e reporta uma correspondência confiante, candidatos de baixa confiança, ou um honesto "ainda não coberto" — ele não fica adivinhando silenciosamente. Use `--json` para uso programático.

O pacote npm registra um retrato da biblioteca de papéis a cada release. Para a versão mais recente ainda não lançada, use `npx --yes github:wonsukchoi/domain-experts <comando>` — a mesma CLI, direto da `main`.

## Roteiro

O [`ROADMAP.md`](./ROADMAP.md) é o backlog mestre — todas as 1.016 ocupações da O*NET, agrupadas por categoria, marcadas conforme vão sendo redigidas. Use-o para encontrar um papel ainda não coberto em vez de tentar adivinhar o que falta.

## Contribuindo — este repositório se multiplica

Cada papel adicionado deixa o roteador mais inteligente, cada correção chega a todos os usuários no próximo release, e cada pergunta de avaliação torna o padrão de qualidade mais difícil de simular. Um prompt que você escreve para si mesmo morre com a sua sessão; um papel que você contribui aqui funciona para todo mundo, para sempre, e continua melhorando depois que você sai. Essa é a aposta inteira: **1.016 ocupações não é um projeto solo — é um bem comum.**

Perguntas frequentes (falhas de lint, conflitos de push, processo de release) → [`docs/FAQ.md`](./docs/FAQ.md).

Três formas de entrar, em qualquer nível de habilidade:

1. **Você trabalha em um papel que cobrimos?** Leia-o. Qualquer coisa errada é uma [issue de correção por profissional](../../issues/new/choose) de 2 minutos — a contribuição mais valiosa que este projeto pode receber. Não precisa saber fazer PR.
2. **Quer escrever ou atualizar um papel?** Siga a receita exata em [`CONTRIBUTING.md`](./CONTRIBUTING.md) — está escrita com tanta precisão que um LLM consegue executá-la, então você e seu assistente de IA podem fazer isso juntos. O lint avisa se a estrutura não está à altura antes de qualquer revisão humana. 42 papéis legados estão [disponíveis para adoção agora](../../issues/1).
3. **Você não sabe escrever mas sabe garimpar?** Colete perguntas de paridade (`evals/parity/harvest_stackexchange.py`) ou registre um [pedido de papel](../../issues/new/choose) com as tarefas que você delegaria a ele.

Se a especificação entrar em conflito com a realidade de um profissional, a especificação perde — diga isso no seu PR e nós ajustamos a especificação.

## Licença

MIT — veja [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
