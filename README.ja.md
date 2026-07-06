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

**[English](./README.md) | [한국어](./README.ko.md) | [日本語](./README.ja.md) | [简体中文](./README.zh-CN.md) | [Español](./README.es.md)**

**職業ロール定義**のオープンソースライブラリ — 実在の実務家が持つ実際のメンタルモデル、判断のしきい値、失敗パターンを構造化し、どんなAIエージェントでも読み込んでその専門家のように推論できるようにするもの。エージェントに「この契約書をレビューして」と頼めば、ジェネラリストがネットの要約を返すのではなく、シニア契約弁護士の条項プレイブックとフォールバックの序列で答える。

## ビジョン — 一人と、あらゆる専門家

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

今、自分の専門外のことをきちんとやろうとすれば、採用、業務委託、あるいは外部への働きかけが必要になる — 弁護士を探し、CFOのスケジュールが空くのを待ち、マーケティング戦略家の報酬を支払う。この摩擦は、一人で起業する人、少人数のチーム、専門外の問題にぶつかったすべての個人にかかる税金のようなものだ。ほとんどの人は、結局それをやらないか、やっても質が低いままになる。

AIのサブスクリプション — あるいはローカルモデルでサブスクリプションすら要らない — とこのリポジトリさえあれば、個人はその税金を払わずに済む。ランウェイの判断が必要ならCFOの実際の推論を読み込む。契約書のレッドラインが必要なら契約弁護士の条項プレイブックを読み込む。プロトコル逸脱の判断が必要なら臨床研究コーディネーターの判断力を読み込む。タスクごとにロールを切り替え、必要なときに、雇用ではなく推論コストだけで済ませる。一人の人間、一つのエージェント、そして何百もの職業が積み上げてきた意思決定の蓄積。

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

これは単なる好奇心の対象ではなく、実際の到達点だ。「専門家が必要だ」と「専門家がいる」の間の壁が消える。カバレッジが広がるほどこれはより真実味を増す — 現時点で1,016のO*NET追跡職業に対して59ロール。ロードマップが存在するのは、その差が興味深いまま放置されるためではなく、縮まっていくためだ。

このリポジトリは、判断力・説明責任・法的に人間が担うべきライセンス資格を代替するものではない — あらゆる規制対象ロール(法律、医療、金融)が明示的にそう述べている。代替するのは、そもそもその推論にアクセスできないという摩擦そのものだ。

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

## クイックスタート

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

インストール不要 — `npx` がnpmから直接取得する。頻繁に使うなら `npm install -g domain-experts` して `npx` を省略してもよい。

あるいは手作業のステップを丸ごとスキップする方法もある。[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) を一度読み込ませておけば、エージェントがタスクにどの専門家が必要かを自動検出し、そのロールの全コンテキストを自動で取り込み、まだカバーされていないロールについては即興で取り繕わず正直に伝えてくれる。あなたは作業を続けるだけで、適切な専門知識が自ずと現れる。

## 「Claudeに『CFOのふりをして』と頼むだけじゃダメなの?」

それもできる — ただし返ってくるのはネット上のあらゆる職務記述書を平均しただけの薄い物真似で、セッションのたびにゼロから再生成され、毎回違う答えになり、誰にも検証されていない。

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

具体的な違いは次のとおり。

- **プロンプトからは導けない内容。** すべてのロールは非導出性テストに合格しなければならない — 職種名だけから再生成できるものは一切含めない。残るのは、プロンプトだけではその場で作り出せないもの、つまり数値化された危険信号のしきい値、市場標準の交渉レンジ、計算が矛盾なく成立する実例、優先順位付けされたフォールバック案だ。
- **単発生成ではなく品質ゲート。** ロールは複数パスのパイプライン([`AUTHORING.md`](./AUTHORING.md))を通じて作られる — 下の図を参照。一行プロンプトではこのどれも得られない。
- **CIで強制される構造。** すべてのPRで [`scripts/lint_roles.py`](./scripts/lint_roles.py) が走る — スキーマ、必須セクション、リンクの解決性、禁止された定型フレーズ、危険信号の網羅性、実例における実数値。ありきたりな職務記述文はビルドに通らない。
- **積み重なっていく。** 場当たりのプロンプトはセッションが終われば消える。これらのファイルは実務家の訂正を蓄積し、成熟度のはしご(`draft` → `reviewed-by-practitioner` → `mature`)とバージョン付きの仕様(現行基準のロールを示す `spec: 2`)を持ち、PRのたびに良くなっていく。修正はすべてのユーザーに届く。
- **トークン効率を意識した設計。** 各ロールはコンパクトな推論コア(`SKILL.md`)とオンデマンドの深掘り情報(`references/`)から成る。エージェントは深さが必要なタスクのときだけそのコストを払う。

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

## ロールの作り方

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

すべてのロールは、仕様とCIによって強制される同じ契約に従う。

1. **3つの出荷テスト** — 実務家が読んで肩をすくめるのではなくうなずくこと、ロールを持つエージェントが持たない場合と比べて明確に違う判断を下すこと、職種名だけからは何一つ導き出せないこと。
2. **固定された構成** — アイデンティティ、第一原理のコア、条件付きヒューリスティクス(「Xの場合、Zでない限りYをデフォルトにする」)、実行可能な意思決定フレームワーク、よくある失敗パターン、そして実際に矛盾なく成立する数値を伴い、実際の成果物(メモ、レッドライン、報告書)で終わる実例。
3. **references三点セット** — 記入済みテンプレートを伴う深掘りプレイブック/成果物ファイル、`red-flags.md`(シグナル → その意味 → 最初に問うべき質問 → 取得すべきデータ)、`vocabulary.md`(専門用語とよくある誤用の説明)。
4. **出典の明示。** 出典は名指しされ、具体的な数値はその出典まで遡れるか、明示的な経験則として明記される。規制対象ロール(法律、医療、金融)には明示的な免責事項が付く。
5. **O*NETを背骨とする。** カバレッジは米国労働省の職業分類(1,016職業)に沿って進む。そのため成長はその週たまたま面白そうだったものではなく、体系的なものになる。

完全な仕様、評価ルーブリック、LLMによる草稿パイプラインは [`AUTHORING.md`](./AUTHORING.md) を参照。

## 検証方法 — 透明性があり、信頼を前提にしない

「専門家が書いた」というのは主張にすぎない。このリポジトリはその代わりに証拠そのものを提供する。誰でもこのチェックアウトから実行できる、独立した4つの層。

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

最新の公開実行結果(2026-07-06、回答はHaiku 4.5、判定は盲検でSonnet 5、両ハーネスとも):

- **反事実比較:** ロールが**15シナリオ中13勝**(1引き分け、1敗) — 専門家的振る舞いの基準を満たした割合は、ジェネラリストのベースラインが37%だったのに対し72%。
- **実務家とのパリティ:** 盲検の一対一比較**8件中5件**で、ロールの回答が実際の実務家によるStack Exchangeの採用済み回答より好まれた(サンプルは小さく、質問セットは増え続けている — 研究結果としてではなく、あくまで兆候として扱うこと)。

すべての結果は再現可能: `python3 evals/run_evals.py` と `python3 evals/parity/run_parity.py`。ロールがこれらのテストに落ちた場合もそれは公開される — 狙いはマーケティングではなく測定にあるからだ。実務家によるレビューは依然として最高の格付け(`metadata.maturity`)であり続けるが、信頼の下限は保証ではなく測定によって決まる。

## 現在のロール一覧

<!-- ROLE_COUNTS_START -->
**89 roles drafted** (85 mapped to an O*NET occupation, 4 custom; 47 at spec 2, 42 awaiting upgrade), across 10 categories:

- **design**: 2
- **engineering**: 14
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

このブロックは自動生成されている — ロールの追加・削除・再マッピングを行った後は `python3 scripts/generate_roadmap.py` を実行すること。手動編集はしないこと。

## お使いのAIツールで使う

`SKILL.md` はツール横断の共通フォーマットだ — 同じロールファイルがClaude Code、Codex CLI、Cursor、その他30以上のエージェントで動く。異なるのはインストール先ディレクトリだけ。

### セットアップ不要: これをエージェントに貼り付けるだけ

以下をClaude Code、Codex、Cursor、あるいはシェルアクセスを持つ任意のエージェントに貼り付け、末尾に自分のタスクを記述すれば、適切な専門家を自動でインストールしてくれる。

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

### ツールごとのインストール方法

| ツール | 方法 |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — `./.claude/skills/<slug>/` に配置され、スキルとして自動的に認識される。 |
| **Codex CLI** | 同じコマンドに `--to .codex/skills/<slug>`(プロジェクト用)または `--to ~/.codex/skills/<slug>`(個人用)を付ける。新しいセッションで読み込まれる。 |
| **Cursor、Windsurf、Roo Code、Goose、その他SKILL.md互換ツール** | 同じコマンドに `--to <ツールのスキルディレクトリ>/<slug>` を付ける — パスはお使いのツールのドキュメントを確認すること。 |
| **`AGENTS.md` を読むツール**(GitHub Copilot、Jules、Amp、Zed など) | リポジトリ内の任意の場所にインストールし(例: `--to skills/<slug>`)、`AGENTS.md` に一行追加する: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **シェルを持たないチャットAI全般** | GitHub上でロールを開き、`SKILL.md` をシステムプロンプトまたはカスタム指示に貼り付ける。会話がさらなる深さを必要とするときは `references/` のファイルを貼り付ける。 |

インストールのたびに `SKILL.md` と `references/` を含むロール全体がコピーされるため、深いプレイブックも一緒についてくる。

### 自動ディスパッチ

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) は `match` ステップそのものを不要にするメタスキルだ。`npx domain-experts add domain-expert-router` でインストールし、一度読み込ませておけば、「Xのふりをして」というリクエストに対してエージェントが自分で適切なロールを見つけ出し、まだカバーされていない場合は正直にそう伝える。

### CLIリファレンス

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
```

`match` はキーワードの重なりでロールを採点し、確信度の高い一致、確信度の低い候補、あるいは正直な「まだカバーされていません」のいずれかを返す — 黙って推測することはない。プログラムから使う場合は `--json` を指定する。

npmパッケージは各リリース時点のロールライブラリのスナップショットだ。最新の未リリース版を使いたい場合は `npx --yes github:wonsukchoi/domain-experts <command>` を使う — CLIは同じで、`main` ブランチから直接取得する。

## ロードマップ

[`ROADMAP.md`](./ROADMAP.md) はマスターバックログだ — すべての1,016のO*NET職業がカテゴリ別にグループ化され、ドラフトが完成するごとにチェックが入る。何が不足しているか当てずっぽうで探すのではなく、これを使って未カバーのロールを見つけること。

## コントリビューション — このリポジトリは積み重なっていく

追加されたロール一つひとつがルーターを賢くし、訂正一つひとつが次のリリースですべてのユーザーに届き、評価用の質問一つひとつが品質基準をごまかしにくくする。自分のために書いたプロンプトはセッションが終われば消えるが、ここに貢献したロールはすべての人のために、永遠に機能し続け、あなたが去った後も改善され続ける。これこそがこのプロジェクトの賭けそのものだ。**1,016の職業は個人プロジェクトではなく、コモンズだ。**

参加の入り口は3つ、スキルレベルは問わない。

1. **あなたが担当しているロールがすでにカバーされている?** それを読んでほしい。何か間違いがあれば2分でできる[実務家による訂正issue](../../issues/new/choose)を — これはこのプロジェクトが受け取れる最も価値のある貢献だ。PRのスキルは不要。
2. **ロールを新しく書いたり、アップグレードしたい?** [`CONTRIBUTING.md`](./CONTRIBUTING.md) にある正確なレシピに従ってほしい — LLMが実行できるほど精密に書かれているので、あなたとあなたのAIアシスタントが一緒に進められる。人間のレビュアーに届く前に、lintが構造の不足を教えてくれる。42件のレガシーロールが[今すぐ着手可能](../../issues/1)だ。
3. **書けないが探すことならできる?** パリティ用の質問を収集する(`evals/parity/harvest_stackexchange.py`)か、委任したいタスクを添えて[ロールリクエスト](../../issues/new/choose)を出してほしい。

仕様が実務家の現実と食い違う場合は、仕様のほうが負ける — PRでそう指摘してくれれば、仕様を直す。

## ライセンス

MIT — [`LICENSE`](./LICENSE) を参照。

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
