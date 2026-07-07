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

**职业角色定义**的开源库——真实从业者的思维模型、决策阈值和失败模式，经过结构化整理，任何 AI agent 都能加载并像那位专家一样推理。让你的 agent "review this contract"，它给出的是一位资深合同律师的条款应对手册和备选方案梯度，而不是一个通才对互联网内容的泛泛总结。

**快速跳转：** [快速开始](#快速开始) · ["我直接让它扮演不就行了？"](#我直接让-claude-扮演-cfo-不就行了吗) · [愿景](#愿景一个人拥有每一位专家) · [角色是如何打造出来的](#角色是如何打造出来的) · [我们如何验证](#我们如何验证透明无需信任) · [当前角色](#当前角色) · [在你的工具中使用](#在你的-ai-工具中使用) · [路线图](#路线图) · [参与贡献](#参与贡献这个仓库会持续复利式增长)

## 快速开始

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

无需安装——`npx` 会直接从 npm 拉取。如果你会经常用到它，`npm install -g domain-experts` 全局安装一下，之后就可以省掉 `npx`。

**在用 Claude Code、Codex、Gemini CLI、Cursor、Windsurf、Roo Code 或 Amp？** `npx domain-experts command --tool <id>` 会为它安装一个 `/domain-expert` 斜杠命令——重启会话后运行 `/domain-expert review this vendor contract` 即可。它会一步完成匹配、加载并以正确的角色进行推理，省去手动 `match`/`add` 的来回操作。

> **如果你是 `git clone` 这个仓库而不是用 CLI：** 不要把你工具的技能发现路径直接指向 `roles/` 目录。这个目录下有 200 多个独立的 `SKILL.md` 文件，而包括 Claude Code 在内的大多数工具会把发现的每个技能的名称和描述都加载进基础系统提示词——你会为一堆用不到的角色，在每个会话里都白白付出这份 token 成本。只安装 [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) 这一个（或者用 CLI 的 `add`/`init` 命令，效果一样）——这是一个轻量的单一技能，只有任务真正需要时才会按需读取具体的 `roles/<slug>/SKILL.md`。

或者干脆跳过手动这一步：加载一次 [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md)，你的 agent 就会自动识别任务需要哪位专家、自动拉取该角色的完整上下文，并且在某个角色还没被覆盖时如实告诉你，而不是硬着头皮临场发挥。你只管继续干活，合适的专业能力会自己出现。

## "我直接让 Claude 扮演 CFO 不就行了吗？"

你当然可以这么做——但你得到的只会是一个肤浅的模仿：互联网上所有职位描述的平均值，每次会话都从零重新生成，每次都不一样，也没有任何人验证过。

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

具体的区别在于：

- **不可派生的内容。** 每个角色都必须通过"不可派生性"测试：不能包含任何仅凭职位名称就能重新生成的内容。留下来的，都是提示词临时生成不出来的东西——数值化的红旗阈值、市场标准的谈判区间、能对得上账的带真实运算的实例，以及按优先级排序的备选方案。
- **一道质量关卡，而非一次性生成。** 角色是通过一条多轮流水线（[`AUTHORING.md`](./AUTHORING.md)）打造出来的——见下方示意图。一句话提示词做不到这些。
- **由 CI 强制执行的结构。** 每个 PR 都会跑一次 [`scripts/lint_roles.py`](./scripts/lint_roles.py)：检查 schema、必需章节、可解析的链接、被禁止的套话、红旗信息的完整性，以及实例中的真实数字。泛泛而谈的职位描述文本会导致构建失败。
- **它会持续复利式增长。** 你的临时提示词在会话结束后就消失了。而这些文件会不断积累从业者的修正意见，拥有一个成熟度阶梯（`draft` → `reviewed-by-practitioner` → `mature`）和一个带版本号的规范（`spec: 2` 标记达到当前标准的角色），并随着每一个 PR 变得更好。修复会惠及所有人。
- **按需付费的 token 效率设计。** 每个角色都是一个精简的推理核心（`SKILL.md`）加上按需加载的深度内容（`references/`）。只有任务真正需要深度时，agent 才会为此付出 token 成本：

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### 真正的护城河是什么？

合理的质疑：上面说的这些都挡不住有人直接 `git clone` 这个仓库，原封不动包装成自己的产品——MIT 许可证，内容零锁定。老实说：这堆文件本身不是护城河。难以复制的是持续产出和修正这些内容的那套机制：

- **是流程，不是产物。** 复制 97 个文件一条命令就行。但复制那套持续产出并修正它们的对抗式评审 → 9 项标准评分表 → lint 强制把关的创作流程（[`AUTHORING.md`](./AUTHORING.md)）做不到——分叉继承的是今天的快照，不是明天的修正。
- **是标准，不是数据库。** `SKILL.md` 已经能在 30 多种智能体工具里运行。在一个可移植的开放格式里做到规模最大，拼的是分发位置，不是内容位置——价值在于成为大家默认找到的答案，而不在字节本身。
- **是验证过的，不是自称的。** 任何竞争对手都能说"专家写的"。但没几个能当场跑 `python3 evals/run_evals.py`，拿出反事实评测 13/15 胜的结果。这里的信任是可测量、可复现的，不是嘴上说说。
- **时效性胜过参数化记忆。** 就算未来某个模型用这个仓库的公开文本训练过，那份知识也会冻结在训练截止日期。这个仓库的修正是从业者提交当天就上线——不用等重新训练，有版本记录，能追溯到来源。
- **覆盖面的纪律性。** O*NET 的 1,016 个职业清单逼着项目系统性地覆盖长尾职位（如 funeral-home-manager、wind-energy-operations-manager），而只挑热门角色做的机会主义竞争者不会费这个劲跟进。
- **免费可移植胜过订阅锁定。** 这不是跟你的 LLM 账单竞争——反正推理成本你都要付。它竞争的对象是封闭的垂直 SaaS（比如"AI 法律顾问"，每月 99 美元）——这些产品拼不过免费、可分叉、能跑在本地模型上且没有持续费用的方案。

在只有 97 个角色、贡献者基数还小的现在，这些都还称不上护城河——只是一条轨迹。赌的是：一旦足够多从业者开始提交修正，而不是每次都从零写提示词，这个共有资源积累的速度会快过任何分叉能跟上的速度。

## 愿景——一个人，拥有每一位专家

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

如今，要把一件明显超出自身专长的事情做好，意味着招聘、找承包商，或者主动对外求助——找一位律师、等 CFO 的日程、支付一位营销策略师的费用。这种摩擦对每一位单打独斗的创始人、每一个小团队、每一个遇到超出自身专长问题的个体，都是一种税。大多数人干脆不做这件事，或者做得很糟糕。

一个拥有 AI 订阅——甚至一个本地模型、完全不需要订阅——再加上这个仓库的个体，不必再交这份税。加载 CFO 应对现金流预警的真实推理逻辑。加载合同律师做 redline 时的条款应对手册。加载临床研究协调员应对方案偏差时的判断力。按任务按需切换角色，付出的只是推理成本，而不是雇人的成本。一个人，一个 agent，汇聚数百种职业积累下来的决策经验。

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

这才是这个项目真正的终局，而不只是个新奇玩意儿："我需要一个专家"和"我已经拥有一个专家"之间的壁垒正在消失。随着覆盖范围扩大，这一点会越来越真实——如今 92 个角色对应着 1,016 个被追踪的职业；路线图的存在就是为了填补这个缺口，而不是为了让它永远显得有趣。

它不会取代那些依法必须由人类承担的判断、责任或执业资质——每一个受监管的角色（法律、医疗、金融）都会明确说明这一点。它取代的，是一开始就无法获得这些推理能力所带来的摩擦。

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

## 角色是如何打造出来的

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

每一个角色都遵循同一套契约，由规范和 CI 共同强制执行：

1. **三项上线测试**——从业者读后会点头认同而不是耸肩敷衍；带上该角色的 agent 与不带该角色相比，会做出可衡量的不同决策；其中没有任何内容是仅凭职位名称就能派生出来的。
2. **固定的结构骨架**——身份定位、第一性原理核心、条件式启发规则（"当出现 X 情况时，默认采用 Y，除非出现 Z"）、一套可执行的决策框架、常见失败模式，以及一个带真实、能对得上账数字的实例，并以真正的交付物收尾（备忘录、redline、汇报材料）。
3. **references 三件套**——一份带有已填好模板的深度实操/工具文件、`red-flags.md`（信号 → 含义 → 首要提问 → 需要拉取的数据），以及 `vocabulary.md`（专业术语及其常见误用说明）。
4. **来源可追溯（Provenance）。** 来源都有明确出处；具体数字要么能追溯到出处，要么被标注为"陈述性经验法则"。受监管的角色（法律、医疗、金融）都带有明确的免责声明。
5. **以 O*NET 为骨架。** 覆盖范围跟随美国劳工部的职业分类体系（1,016 个职业），因此增长是系统化的，而不是这周恰好觉得哪个有意思就做哪个。

完整规范、评分标准与 LLM 撰写流水线，参见 [`AUTHORING.md`](./AUTHORING.md)。在 Claude Code 检出环境中，整条流水线可以直接用 `/generate-role "<need>"` 一键运行——详见下文的[维护者自动化 (Claude Code)](#maintainer-automation-claude-code)。

## 我们如何验证——透明、无需信任

"由专家撰写"只是一句宣称；这个仓库选择提供实打实的凭证。四道相互独立的验证层，任何人从这份代码检出后都可以自行运行：

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

最新发布的运行结果（2026-07-06，Haiku 4.5 作答，Sonnet 5 盲评，两套测试框架均适用）：

- **反事实对照（Counterfactual）：** 加载角色一方在 **15 个场景中赢下 13 个**（1 平、1 负）——角色本身命中了 72% 的专家行为标准，而对照基线（通才）的命中率为 37%。
- **与真人对照（Parity）：** 在 **8 组盲测头对头对比中的 5 组**里，角色给出的答案比真实从业者在 Stack Exchange 上被采纳的答案更受青睐（样本较小；问题集仍在增长中——请把它当作一个初步信号，而非严谨的研究结论）。

每一项结果都可复现：运行 `python3 evals/run_evals.py` 和 `python3 evals/parity/run_parity.py` 即可。当某个角色在这些测试中未达标时，这一点同样会被公开——重点在于测量，而不是营销。从业者审阅仍然是最高等级的认可标志（`metadata.maturity`），但信任的底线是靠测量建立的，而不是靠背书。

## 当前角色

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

这个代码块是自动生成的——在新增/删除/重新映射某个角色后运行 `python3 scripts/generate_roadmap.py`，不要手动修改它。

## 在你的 AI 工具中使用

`SKILL.md` 是一种跨工具的通用格式——同一份角色文件在 Claude Code、Codex CLI、Cursor 以及 30 多种其他 agent 中都能用。不同的只是安装目录。

### 零配置：把这段粘贴给你的 agent

把下面这段内容复制到 Claude Code、Codex、Cursor，或任何具备 shell 访问权限的 agent 中，在末尾描述你的任务，它就会自行安装合适的专家：

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

**Claude Code、Codex、Gemini CLI、Cursor、Windsurf、Roo Code 和 Amp 用户：** 可以跳过粘贴这一步——`npx domain-experts command --tool <id>` 只需安装一次 `/domain-expert`，之后每次直接运行 `/domain-expert <task>` 即可（参见下方 [`/domain-expert` 斜杠命令](#domain-expert-斜杠命令)）。

### 按工具安装

| 工具 | 安装方式 |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` ——会安装到 `./.claude/skills/<slug>/`，作为 skill 自动被识别。 |
| **Codex CLI** | 用同样的命令加上 `--to .codex/skills/<slug>`（项目级）或 `--to ~/.codex/skills/<slug>`（个人级）。新会话会自动识别。 |
| **Cursor** | 用同样的命令加上 `--to .cursor/skills/<slug>`——Cursor 原生支持同样的 `SKILL.md` 格式。 |
| **Windsurf、Roo Code、Goose 及其他兼容 SKILL.md 的工具** | 用同样的命令加上 `--to <你所用工具的 skills 目录>/<slug>`——具体路径请查阅该工具的文档。 |
| **读取 `AGENTS.md` 的工具**（GitHub Copilot、Jules、Amp、Zed 等） | 安装到仓库中的任意位置（例如 `--to skills/<slug>`），然后在 `AGENTS.md` 中加一行：`When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **任意聊天式 AI（无 shell 访问权限）** | 在 GitHub 上打开该角色，把 `SKILL.md` 粘贴进系统提示词或自定义指令中；当对话需要更深的内容时，再粘贴 `references/` 下的文件。 |

每次安装都会复制该角色的完整内容——`SKILL.md` 加上 `references/`——因此深度实操手册会一并带走。

### 自动分派

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) 是一个元技能（meta-skill），它连 `match` 这一步都省去了——运行 `npx domain-experts add domain-expert-router` 安装它，加载一次之后，你的 agent 就会自行为"扮演 X"这类请求找到合适的角色，并在某个角色还未被覆盖时如实告知。

### `/domain-expert` 斜杠命令

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

重启会话，然后直接使用 `/domain-expert <task>`——例如 `/domain-expert review this vendor contract`。它会运行 `match`，加载获胜角色的 `SKILL.md`（以及按需加载的 `references/`），并以该专家的身份作答；如果目前还没有匹配的角色，也会如实告知。思路和上面的路由 skill 一样，只是打包成了一次性命令，而不是常驻加载的 skill。

| `--tool` | 安装位置 | 说明 |
|---|---|---|
| `claude`（默认） | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex 只从用户级目录读取 prompts，没有项目级选项；OpenAI 的文档已把这一机制标记为弃用，转而推荐"skills"，但目前仍然可用 |
| `gemini` | `.gemini/commands/domain-expert.toml` | TOML 格式 |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf 把这类东西称为"workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | Amp 的位置固定在仓库根目录，没有单独的全局目录 |

加上 `--global` 可以安装到该工具的用户级目录（例如 `~/.claude/commands/`、`~/.cursor/commands/`），而不是项目目录；或者用 `--to <path>` 指定一个完全自定义的位置。

### CLI 参考

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` 会根据关键词重合度给角色打分，并给出一个高置信度命中结果、若干低置信度候选，或者如实告知"尚未覆盖"——它不会悄悄地瞎猜。加上 `--json` 可用于程序化调用。

npm 包在每次发布时都会对角色库做一次快照。如果想使用尚未发布的最新版本，可以用 `npx --yes github:wonsukchoi/domain-experts <command>`——同样的 CLI，直接取自 `main` 分支。

### 维护者自动化 (Claude Code)

在本仓库的 Claude Code 检出环境中工作，会额外获得三个斜杠命令，它们是对上述流程的自动化，而非替代——每一个都需要人工 PR 把关，任何一个都不会自行提交到 `main` 或自行发布。

- `/generate-role "<need>"`——将一段自由文本描述的需求，判定为匹配某个已有角色、某个新的细分子角色（leaf），或某个全新的父角色，然后运行 AUTHORING.md 中的 Pass 0-4 流水线（调研 → 起草 → 对抗式评审 → 评分，最多 2 轮修订循环），并开启一个 PR。
- `/audit-roles [batchSize]`——按批次对已上线角色依据评分标准与信息源时效性重新评分；写入 `last_audited`/`audit_score`，标记 `status: needs-refresh`，连续两次评分不达标后会将其下线（移动到 `roles/_deprecated/`）。
- `/scan-project <path>`——以只读方式扫描外部项目（技术栈、README、目录结构、近期提交），提出候选需求并与现有覆盖范围做交叉核对，再把你选中的需求交给 `/generate-role` 处理。被扫描项目的任何信息都不会被写入到任何地方。

置信度不足的 `match` 查询会被记录到 `data/gap-log.jsonl`，并按频率汇总展示在 [`ROADMAP.md`](./ROADMAP.md) 的"有需求但尚缺失"部分——这是下一步该写什么角色的具体信号。

## 路线图

[`ROADMAP.md`](./ROADMAP.md) 是总的待办清单——涵盖全部 1,016 个 O*NET 职业，按类别分组，随着角色被撰写而逐一勾选。想找一个尚未覆盖的角色时，用它来查，而不是靠猜。

## 参与贡献——这个仓库会持续复利式增长

每新增一个角色都会让路由更聪明，每一次修正都会在下一次发布时惠及所有用户，每一道 eval 问题都会让质量标准更难被蒙混过关。你为自己写的一条提示词会随着会话结束而消失；你在这里贡献的一个角色，则会为所有人持续发挥作用，永不停止，而且会在你离开之后继续变得更好。这就是整个赌注所在：**1,016 个职业不是一个人的项目——它是一份共同财富（commons）。**

常见问题（lint 失败、push 冲突、发布流程）→ [`docs/FAQ.md`](./docs/FAQ.md)。

三种参与方式，任何技能水平都能上手：

1. **你所从事的职业正好被我们覆盖了？** 去读一读。任何有问题的地方，提一个 [从业者修正 issue](../../issues/new/choose) 只需两分钟——这是这个项目能获得的最有价值的贡献。不需要任何 PR 技能。
2. **你想撰写或升级一个角色？** 按照 [`CONTRIBUTING.md`](./CONTRIBUTING.md) 中的精确步骤来做——它写得足够精确，连 LLM 都能照着执行，因此你和你的 AI 助手可以一起完成。在任何人类审阅之前，lint 会先告诉你结构是否达标。目前有 42 个遗留角色 [可供认领](../../issues/1)。
3. **你不会写但擅长发掘信息？** 可以去收集 parity 测试的问题集（`evals/parity/harvest_stackexchange.py`），或者提一个 [角色需求 issue](../../issues/new/choose)，说明你会想把哪些任务委托给它。

如果规范和从业者的真实情况相冲突，规范让步——在你的 PR 里说明这一点，我们会去修正规范。

## 许可协议

MIT——详见 [`LICENSE`](./LICENSE)。

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
