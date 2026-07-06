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

**직무 역할 정의(job role definitions)**의 오픈소스 라이브러리 — 실제 실무자들의 사고 모델, 의사결정 임계값, 실패 패턴을 그대로 담아서 어떤 AI 에이전트든 불러와 그 전문가처럼 추론할 수 있도록 구조화했습니다. 에이전트에게 "이 계약서를 검토해줘"라고 요청하면, 인터넷 요약을 내놓는 제너럴리스트가 아니라 시니어 계약 전문 변호사의 조항 대응 전략과 폴백 사다리로 답합니다.

## 비전 — 한 사람, 모든 전문가

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

지금은 자기 전문 분야 밖의 일을 잘 해내려면 채용하거나, 계약하거나, 아웃리치를 해야 합니다 — 변호사를 찾고, CFO의 일정을 기다리고, 마케팅 전략가의 비용을 지불하는 식으로요. 이 마찰은 모든 1인 창업자, 모든 소규모 팀, 자기 전문성 밖의 문제를 마주한 모든 개인에게 부과되는 세금입니다. 대부분의 사람은 그냥 그 일을 하지 않거나, 형편없이 해냅니다.

AI 구독(또는 로컬 모델, 구독조차 필요 없는)과 이 저장소를 가진 개인은 그 세금을 내지 않습니다. 런웨이 관련 의사결정을 위해 CFO의 실제 추론 과정을 불러오세요. 계약서 수정을 위해 계약 전문 변호사의 조항 대응 전략을 불러오세요. 프로토콜 이탈 문제를 위해 임상연구 코디네이터의 판단력을 불러오세요. 작업마다 역할을 바꿔가며, 필요할 때, 채용 비용 대신 추론(inference) 비용만 지불하면 됩니다. 한 사람, 하나의 에이전트, 그리고 수백 개 직업의 축적된 의사결정 능력.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

이것이 이 프로젝트의 실제 최종 목표입니다. 단순한 호기심거리가 아니라 — "전문가가 필요하다"와 "전문가가 있다" 사이의 장벽이 무너지는 것. 커버리지가 늘어날수록 더 확실해집니다 — 오늘 기준 추적 중인 1,016개 직업 대비 59개 역할; 로드맵이 존재하는 이유는 이 격차를 좁히기 위함이지, 영원히 흥미로운 상태로 남겨두기 위함이 아닙니다.

이 프로젝트는 법적으로 반드시 사람에게 있어야 하는 판단, 책임, 자격(라이선스)을 대체하지 않습니다 — 규제 대상 역할(법률, 의료, 금융) 전부가 이를 명시적으로 밝히고 있습니다. 대체하는 것은 애초에 그 추론에 접근할 수 없었던 마찰입니다.

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

## 빠른 시작

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

별도 설치는 필요 없습니다 — `npx`가 npm에서 바로 가져옵니다. 자주 쓰신다면 `npm install -g domain-experts` 후 `npx`는 생략하세요.

아니면 수동 단계 자체를 건너뛸 수도 있습니다. [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md)를 한 번만 로드해두면, 에이전트가 작업에 어떤 전문가가 필요한지 스스로 감지하고, 해당 역할의 전체 컨텍스트를 자동으로 불러오며, 아직 커버되지 않은 역할이면 즉흥적으로 지어내지 않고 솔직하게 알려줍니다. 여러분은 계속 일하면 되고, 알맞은 전문성이 알아서 나타납니다.

## "그냥 Claude한테 CFO처럼 굴라고 시키면 안 되나요?"

가능은 합니다 — 하지만 얕은 흉내만 얻게 됩니다: 인터넷상의 모든 직무 기술서를 평균 낸 결과물이, 세션마다 처음부터 다시 생성되어, 매번 다르고, 누구의 검증도 거치지 않은 상태로요.

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

구체적인 차이는 다음과 같습니다.

- **파생 불가능한 콘텐츠.** 모든 역할은 비파생성(non-derivability) 테스트를 통과해야 합니다: 직무명만으로 다시 만들어낼 수 있는 내용은 배제합니다. 남는 것은 프롬프트만으로는 즉석에서 만들어낼 수 없는 것들입니다 — 수치화된 위험 신호 임계값, 시장 표준 협상 범위, 계산이 맞아떨어지는 실전 예시, 우선순위가 매겨진 폴백 포지션.
- **단발성 생성이 아니라 품질 게이트.** 역할들은 여러 단계를 거치는 파이프라인([`AUTHORING.md`](./AUTHORING.md))을 통해 만들어집니다 — 아래 다이어그램 참고. 한 줄짜리 프롬프트로는 이런 과정을 거칠 수 없습니다.
- **CI로 강제되는 구조.** 모든 PR은 [`scripts/lint_roles.py`](./scripts/lint_roles.py)를 실행합니다: 스키마, 필수 섹션, 링크 유효성, 금지된 상투어구, 위험 신호(red-flag) 완전성, 실전 예시 내 실제 숫자 여부. 뻔한 직무 기술서 텍스트는 빌드에서 실패합니다.
- **복리로 쌓입니다.** 즉흥적으로 쓴 프롬프트는 세션이 끝나면 사라집니다. 이 파일들은 실무자의 교정을 계속 축적하고, 성숙도 사다리(`draft` → `reviewed-by-practitioner` → `mature`)와 버전이 매겨진 스펙(`spec: 2`는 현재 기준을 충족한 역할을 뜻함)을 갖추며, PR마다 더 나아집니다. 수정 사항은 모든 사람에게 전달됩니다.
- **토큰 효율을 고려한 설계.** 각 역할은 압축된 추론 코어(`SKILL.md`)와 필요할 때만 불러오는 심화 자료(`references/`)로 구성됩니다. 에이전트는 작업에 깊이가 필요할 때만 그 비용을 지불합니다.

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### 진짜 모트(moat)는 무엇인가?

타당한 반박: 위 내용 중 어느 것도 누군가 이 저장소를 그대로 `git clone` 해서 자기 제품으로 내놓는 걸 막지 못한다 — MIT 라이선스, 콘텐츠 잠금 없음. 솔직한 답: 파일 자체는 모트가 아니다. 포크하기 어려운 건 그것을 계속 만들고 고쳐나가는 장치 쪽이다.

- **결과물이 아니라 파이프라인.** 97개 파일 복사는 명령어 하나면 끝난다. 하지만 그것들을 계속 만들고 고쳐나가는 적대적 비평 → 9개 기준 루브릭 → lint 필수 통과 저작 루프([`AUTHORING.md`](./AUTHORING.md))는 복사할 수 없다 — 포크는 오늘의 스냅샷만 물려받을 뿐, 내일의 수정은 물려받지 못한다.
- **데이터베이스가 아니라 표준.** `SKILL.md`는 이미 30개 이상의 에이전트 도구에서 동작한다. 이식 가능한 오픈 포맷에서 가장 큰 라이브러리라는 건 콘텐츠 우위가 아니라 배포 우위다 — 가치는 바이트 자체가 아니라 사람들이 찾는 기본 답이 되는 데 있다.
- **주장이 아니라 검증.** "전문가가 썼다"는 어느 경쟁자든 말할 수 있다. 하지만 눈앞에서 `python3 evals/run_evals.py`를 돌려 반사실적 평가 13/15승을 보여줄 수 있는 곳은 드물다. 여기서 신뢰는 측정되고 재현되는 것이지, 주장되는 게 아니다.
- **최신성이 파라메트릭 기억을 이긴다.** 미래의 모델이 이 저장소의 공개 텍스트로 학습한다 해도, 그 지식은 학습 마감 시점에 얼어붙는다. 이 저장소의 수정 사항은 실무자가 보고한 그날 바로 반영된다 — 재학습 주기 없이, 버전 관리되고, 출처까지 추적된다.
- **커버리지 규율.** O*NET의 1,016개 직업 백본이 롱테일 직종(funeral-home-manager, wind-energy-operations-manager 등)까지 체계적으로 다루도록 강제한다 — 유행하는 역할만 골라 큐레이션하는 기회주의적 경쟁자는 여기까지 따라오지 않는다.
- **무료·이식성이 구독 종속을 이긴다.** 이건 LLM 사용료와 경쟁하는 게 아니다 — 어차피 추론 비용은 낸다. 경쟁 상대는 폐쇄형 수직 SaaS("AI 법률 고문" 월 $99 등)다 — 이들은 무료·포크 가능·로컬 모델 구동·반복 비용 제로를 이길 수 없다.

97개 역할, 소규모 기여자 기반인 지금은 아직 모트가 아니다 — 궤적이다. 베팅은 이것: 실무자들이 매 세션 처음부터 프롬프트를 쓰는 대신 수정 사항을 보고하기 시작하면, 커먼즈는 어떤 포크도 따라잡을 수 없는 속도로 복리 성장한다.

## 역할은 어떻게 만들어지는가

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

모든 역할은 스펙과 CI로 강제되는 동일한 규약을 따릅니다.

1. **세 가지 출시 테스트** — 실무자가 읽었을 때 어깨를 으쓱하는 게 아니라 고개를 끄덕여야 하고, 그 역할을 가진 에이전트는 없을 때와 측정 가능하게 다른 결정을 내려야 하며, 직무명만으로는 그 안의 어떤 내용도 유추할 수 없어야 합니다.
2. **고정된 구조** — 정체성(identity), 제1원칙 핵심(first-principles core), 조건부 휴리스틱("X일 때는 Z가 아닌 한 기본적으로 Y"), 실행 가능한 의사결정 프레임워크, 흔한 실패 패턴, 그리고 실제 결과물(메모, 수정본, 보고서)로 끝나는 실전 예시(계산이 맞아떨어지는 실제 숫자 포함).
3. **참조 자료 3종 세트(references trio)** — 채워진 템플릿을 담은 심화 플레이북/산출물 파일, `red-flags.md`(신호 → 의미 → 첫 질문 → 확인할 데이터), 그리고 `vocabulary.md`(전문 용어와 흔한 오용 사례).
4. **출처(Provenance)** — 출처는 명시됩니다. 구체적인 숫자는 출처를 추적할 수 있거나, 명시된 휴리스틱으로 표시됩니다. 규제 대상 역할(법률, 의료, 금융)에는 명시적인 면책 조항이 포함됩니다.
5. **O*NET 기반 골격** — 커버리지는 미국 노동부의 직업 분류 체계(1,016개 직업)를 따라가므로, 그 주에 흥미로워 보이는 것을 마구잡이로 추가하는 게 아니라 체계적으로 성장합니다.

전체 스펙, 평가 기준, LLM 초안 작성 파이프라인: [`AUTHORING.md`](./AUTHORING.md).

## 검증 방식 — 투명하게, 신뢰를 요구하지 않습니다

"전문가가 작성했다"는 하나의 주장에 불과합니다. 이 저장소는 그 대신 증거를 제공합니다. 이 체크아웃에서 누구나 실행할 수 있는 네 개의 독립적인 계층입니다.

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

최근 공개된 실행 결과 (2026-07-06, Haiku 4.5가 답변, Sonnet 5가 블라인드 심사, 두 하니스 모두):

- **반사실적(Counterfactual) 비교:** 스킬이 **15개 시나리오 중 13개**에서 승리 (무승부 1, 패배 1) — 전문가다운 행동 기준 충족률이 제너럴리스트 기준선의 37% 대비 72%.
- **인간과의 동등성(Parity) 비교:** 블라인드 일대일 비교 **8건 중 5건**에서 스킬의 답변이 실제 실무자가 작성해 채택된 Stack Exchange 답변보다 선호됨 (표본이 작음; 질문 세트는 계속 늘어나고 있으므로 아직 연구가 아닌 신호 정도로 보아야 함).

모든 결과는 재현 가능합니다: `python3 evals/run_evals.py`와 `python3 evals/parity/run_parity.py`. 어떤 역할이 이 테스트를 통과하지 못하면 그것도 공개됩니다 — 요점은 마케팅이 아니라 측정입니다. 실무자 검토는 여전히 최고의 인증(`metadata.maturity`)이지만, 신뢰의 최소 기준은 보증이 아니라 측정된 값입니다.

## 현재 역할 목록

<!-- ROLE_COUNTS_START -->
**90 roles drafted** (86 mapped to an O*NET occupation, 4 custom; 48 at spec 2, 42 awaiting upgrade), across 10 categories:

- **design**: 2
- **engineering**: 15
- **finance**: 10
- **healthcare**: 6
- **legal**: 4
- **marketing**: 4
- **operations**: 39
- **other**: 4
- **product**: 1
- **sales**: 5

Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.
<!-- ROLE_COUNTS_END -->

이 블록은 자동 생성됩니다 — 역할을 추가/제거/재매핑한 뒤에는 `python3 scripts/generate_roadmap.py`를 실행하세요. 직접 수정하지 마세요.

## AI 도구와 함께 사용하기

`SKILL.md`는 도구 간 호환되는 형식입니다 — 동일한 역할 파일이 Claude Code, Codex CLI, Cursor, 그리고 30개 이상의 다른 에이전트에서 동작합니다. 다른 점은 설치 디렉터리뿐입니다.

### 설정 없이 바로 쓰기: 에이전트에 이걸 붙여넣으세요

Claude Code, Codex, Cursor, 또는 셸 접근 권한이 있는 아무 에이전트에나 아래 내용을 복사해 붙여넣고 맨 아래에 작업 내용을 설명하면, 알맞은 전문가를 스스로 설치합니다.

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

### 도구별 설치 방법

| 도구 | 방법 |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — `./.claude/skills/<slug>/`에 설치되며, 스킬로 자동 인식됩니다. |
| **Codex CLI** | 동일한 명령에 `--to .codex/skills/<slug>`(프로젝트) 또는 `--to ~/.codex/skills/<slug>`(개인)를 추가하세요. 새 세션에서 바로 인식됩니다. |
| **Cursor, Windsurf, Roo Code, Goose 등 SKILL.md 호환 도구** | 동일한 명령에 `--to <해당 도구의 스킬 디렉터리>/<slug>`를 추가하세요 — 정확한 경로는 각 도구의 문서를 확인하세요. |
| **`AGENTS.md`를 읽는 도구들** (GitHub Copilot, Jules, Amp, Zed 등) | 저장소 어디에나 설치한 뒤(예: `--to skills/<slug>`), `AGENTS.md`에 한 줄을 추가하세요: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **셸이 없는 채팅 AI** | GitHub에서 해당 역할을 열어 `SKILL.md`를 시스템 프롬프트나 커스텀 인스트럭션에 붙여넣으세요. 대화에 더 깊은 내용이 필요하면 `references/` 파일도 붙여넣으세요. |

설치할 때마다 전체 역할이 함께 복사됩니다 — `SKILL.md`와 `references/` 모두 — 그래서 심화 플레이북도 함께 이동합니다.

### 자동 디스패치

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md)는 `match` 단계마저 없애주는 메타 스킬입니다 — `npx domain-experts add domain-expert-router`로 설치하고 한 번만 로드해두면, 에이전트가 "X처럼 행동해줘" 요청에 알맞은 역할을 스스로 찾아주고, 아직 커버되지 않은 역할이면 솔직하게 알려줍니다.

### CLI 레퍼런스

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
```

`match`는 키워드 중복도로 역할 점수를 매겨 확신도 높은 매치, 낮은 확신도의 후보들, 또는 솔직한 "아직 커버되지 않음" 중 하나를 알려줍니다 — 조용히 추측하지 않습니다. 프로그래밍 방식으로 쓰려면 `--json`을 사용하세요.

npm 패키지는 각 릴리스 시점의 역할 라이브러리를 스냅샷으로 담고 있습니다. 아직 릴리스되지 않은 최신 상태를 쓰려면 `npx --yes github:wonsukchoi/domain-experts <command>`를 사용하세요 — 동일한 CLI를, `main`에서 바로.

## 로드맵

[`ROADMAP.md`](./ROADMAP.md)는 마스터 백로그입니다 — 1,016개 O*NET 직업 전체를 카테고리별로 정리하고, 초안이 작성될 때마다 체크 표시를 합니다. 무엇을 추측하기보다, 아직 커버되지 않은 역할을 찾을 때 이 문서를 활용하세요.

## 기여하기 — 이 저장소는 복리로 성장합니다

역할이 하나 추가될 때마다 라우터는 더 똑똑해지고, 수정 사항 하나하나가 다음 릴리스에서 모든 사용자에게 전달되며, 평가 질문 하나하나가 품질 기준을 속이기 더 어렵게 만듭니다. 자신을 위해 쓴 프롬프트는 세션이 끝나면 사라지지만, 여기에 기여한 역할은 모두를 위해 영원히 작동하며 여러분이 떠난 뒤에도 계속 개선됩니다. 그것이 이 프로젝트의 전제입니다: **1,016개 직업은 혼자 하는 프로젝트가 아니라 커먼즈(commons)입니다.**

참여하는 세 가지 방법, 실력 수준에 상관없이:

1. **여러분이 우리가 다루는 역할로 실제 일하고 계신가요?** 읽어보세요. 잘못된 부분이 있다면 2분이면 끝나는 [실무자 교정 이슈](../../issues/new/choose)를 남겨주세요 — 이 프로젝트가 받을 수 있는 가장 가치 있는 기여입니다. PR 관련 기술은 필요 없습니다.
2. **역할을 새로 쓰거나 업그레이드하고 싶으신가요?** [`CONTRIBUTING.md`](./CONTRIBUTING.md)의 정확한 레시피를 따르세요 — LLM이 그대로 실행할 수 있을 만큼 정밀하게 작성되어 있어서, 여러분과 여러분의 AI 어시스턴트가 함께 작업할 수 있습니다. 사람이 검토하기 전에 lint가 구조가 기준에 미달하는지 알려줍니다. 42개의 레거시 역할을 [지금 바로 맡을 수 있습니다](../../issues/1).
3. **글은 못 쓰지만 찾는 건 잘하시나요?** 동등성 비교 질문을 수집하거나(`evals/parity/harvest_stackexchange.py`) 위임하고 싶은 작업을 담아 [역할 요청](../../issues/new/choose)을 남겨주세요.

스펙이 실무자의 현실과 충돌한다면 스펙이 집니다 — PR에 그렇게 밝혀주시면 스펙을 고치겠습니다.

## 라이선스

MIT — [`LICENSE`](./LICENSE) 참고.

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
