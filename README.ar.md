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

مكتبة مفتوحة المصدر من **تعريفات الأدوار الوظيفية** — النماذج الذهنية الفعلية، وعتبات اتخاذ القرار، وأنماط الفشل الخاصة بممارسين حقيقيين، مُهيكَلة بحيث يستطيع أي عميل ذكاء اصطناعي تحميلها والتفكير كذلك الخبير. اطلب من عميلك "راجع هذا العقد" وسيجيبك بدليل بنود ومسارات بديلة كما يفعل محامٍ متخصص أول في العقود، لا بملخّص عام مستقى من الإنترنت.

**انتقل إلى:** [البدء السريع](#quick-start) · ["أليس بإمكاني فقط أن أطلب من الوكيل ذلك؟"](#cant-i-just-tell-claude-to-act-like-a-cfo) · [الرؤية](#vision--one-person-every-expert) · [كيف تُبنى الأدوار](#how-roles-are-built) · [كيف نتحقق](#how-we-verify--transparent-no-trust-required) · [الأدوار الحالية](#current-roles) · [الاستخدام مع أداتك](#use-it-with-your-ai-tool) · [خارطة الطريق](#roadmap) · [المساهمة](#contributing--this-repo-compounds)

## البدء السريع

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

لا حاجة لأي تثبيت — تجلبه `npx` مباشرة من npm. تستخدمها كثيرًا؟ نفّذ `npm install -g domain-experts` واستغنِ عن `npx`.

**تستخدم Claude Code أو Codex أو Gemini CLI أو Cursor أو Windsurf أو Roo Code أو Amp؟** يقوم الأمر `npx domain-experts command --tool <id>` بتثبيت أمر شرطة مائلة `/domain-expert` فيها — أعد تشغيل الجلسة ثم نفّذ `/domain-expert review this vendor contract`. يقوم بالمطابقة والتحميل والتفكير كالدور الصحيح في خطوة واحدة، دون الحاجة لتكرار خطوتي `match` و`add` يدويًا.

أو تخطَّ الخطوة اليدوية كليًا: حمّل [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) مرة واحدة، وسيكتشف عميلك تلقائيًا أي خبير تحتاجه المهمة، ويسحب سياق الدور الكامل تلقائيًا، ويخبرك بصدق حين لا يكون الدور مُغطّى بعد بدلًا من الارتجال. تستمر أنت في العمل، وتظهر الخبرة المناسبة من تلقاء نفسها.

## "أليس بإمكاني فقط أن أطلب من Claude أن يتصرف كمدير مالي؟"

يمكنك ذلك — لكنك ستحصل على محاكاة سطحية: متوسط كل وصف وظيفي على الإنترنت، يُعاد توليده من الصفر في كل جلسة، مختلف في كل مرة، لا يتحقق منه أحد.

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

والفرق، بشكل ملموس:

- **محتوى غير قابل للاشتقاق.** يجب أن يجتاز كل دور اختبار عدم القابلية للاشتقاق: لا شيء يمكن توليده من مجرد المسمى الوظيفي. ما يتبقى هو ما لا يستطيع التلقين إنتاجه عند الطلب — عتبات رقمية للإنذارات، نطاقات تفاوض معيارية في السوق، أمثلة عملية بحسابات متّسقة، ومواقف بديلة مرتّبة حسب الأولوية.
- **بوابة جودة، لا توليد واحد.** تُبنى الأدوار عبر خط أنابيب متعدد المراحل ([`AUTHORING.md`](./AUTHORING.md)) — انظر المخطط أدناه. سطر تلقين واحد لا يمرّ بأي من ذلك.
- **بنية مفروضة عبر التكامل المستمر (CI).** كل طلب سحب (PR) يشغّل [`scripts/lint_roles.py`](./scripts/lint_roles.py): المخطط، الأقسام المطلوبة، صحة الروابط، العبارات الحشوية الممنوعة، اكتمال إشارات الإنذار، والأرقام الحقيقية في المثال العملي. النص العام لوصف وظيفي يفشل في البناء.
- **يتراكم مع الوقت.** يختفي تلقينك المرتجل بانتهاء الجلسة. هذه الملفات تتراكم فيها تصويبات الممارسين، وتحمل سلّم نضج (`draft` ← `reviewed-by-practitioner` ← `mature`) ومواصفة مرقّمة (`spec: 2` تعني الأدوار عند المعيار الحالي)، وتتحسّن مع كل طلب سحب. الإصلاحات تصل إلى الجميع.
- **مصمَّم لكفاءة الرموز (tokens).** كل دور هو نواة استدلال مضغوطة (`SKILL.md`) بالإضافة إلى عمق عند الطلب (`references/`). يدفع العميل ثمن العمق فقط حين تحتاجه المهمة:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### إذن ما هي الميزة التنافسية (moat) الحقيقية؟

اعتراض عادل: لا شيء مما سبق يمنع أحدًا من عمل `git clone` لهذا المستودع بالضبط وطرحه كمنتج خاص به — رخصة MIT، بلا أي قفل على المحتوى. الإجابة الصادقة: مجموعة الملفات ليست هي الميزة التنافسية. الصعب في تفريعه (fork) هو الآلة التي تواصل إنتاجه وتصحيحه:

- **خط الأنابيب، لا الناتج.** نسخ 97 ملفًا يتطلب أمرًا واحدًا. أما نسخ حلقة التأليف من النقد التنافسي ← معيار من 9 محاور ← بوابة فحص إلزامية ([`AUTHORING.md`](./AUTHORING.md)) التي تواصل إنتاجها وتصحيحها فلا يمكن نسخه — يرث التفريع لقطة اليوم، لا إصلاحات الغد.
- **معيار، لا قاعدة بيانات.** يعمل `SKILL.md` بالفعل في أكثر من 30 أداة عميل. كونك أكبر مكتبة بتنسيق مفتوح قابل للنقل هو موقع توزيع، لا موقع محتوى — القيمة في أن تكون الإجابة الافتراضية التي يجدها الناس، لا في البايتات نفسها.
- **مُتحقَّق منه، لا مُدَّعى.** يستطيع أي منافس أن يقول "كُتب بواسطة خبراء". قلّة يستطيعون تشغيل `python3 evals/run_evals.py` أمامك وإظهار فوز 13 من أصل 15 في اختبارات مضادة للواقع. الثقة هنا مُقاسة وقابلة لإعادة الإنتاج، لا مُدَّعاة.
- **الحداثة تتفوّق على الذاكرة المُدرَّبة مسبقًا.** حتى لو تدرّب نموذج مستقبلي على النص العلني لهذا المستودع، تتجمّد تلك المعرفة عند حدّ التدريب. تصويبات هذا المستودع تُشحن في اليوم الذي يُقدّمها فيه الممارس — بلا دورة إعادة تدريب، مع ترقيم للإصدارات، وتتبّع للمصدر.
- **انضباط في التغطية.** يفرض العمود الفقري لـ O*NET المكوّن من 1,016 مهنة تغطيةً منهجية للذيل الطويل (مدير دار جنازات، مسؤول عمليات طاقة الرياح) لا يكلّف نفسه بها منافس انتهازي يختار فقط الأدوار الرائجة.
- **المجانية والقابلية للنقل تتفوّقان على الاشتراك المُقيَّد.** هذا لا ينافس فاتورة نموذج اللغة الكبير لديك — ستدفع تكلفة الاستدلال على أي حال. إنه ينافس منتجات SaaS العمودية المغلقة ("مستشار قانوني بالذكاء الاصطناعي" بسعر 99 دولارًا شهريًا) — تلك لا يمكنها منافسة المجانية والقابلية للتفريع والتشغيل على نموذج محلي بلا تكلفة متكررة.

لا شيء من هذا ميزة تنافسية بعد عند 97 دورًا وقاعدة مساهمين صغيرة — إنه مسار. الرهان: يتراكم المشترك (commons) أسرع من أي تفريع منفرد بمجرد أن يبدأ عدد كافٍ من الممارسين بتقديم التصويبات بدلًا من كتابة التلقينات من الصفر في كل جلسة.

## الرؤية — شخص واحد، كل الخبراء

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

في الوقت الحالي، فعل شيء ما بإتقان خارج مجال خبرتك يعني التوظيف أو التعاقد أو التواصل الخارجي — إيجاد محامٍ، أو انتظار موعد على تقويم مدير مالي، أو دفع أجر استراتيجي تسويق. هذا الاحتكاك ضريبة تُفرض على كل مؤسِّس منفرد، وكل فريق صغير، وكل فرد يواجه مشكلة خارج تخصصه. معظم الناس ببساطة لا يقومون بالأمر، أو يقومون به بشكل سيّئ.

الفرد الذي لديه اشتراك ذكاء اصطناعي — أو نموذج محلي، بلا اشتراك على الإطلاق — وهذا المستودع، لا يدفع تلك الضريبة. حمّل الاستدلال الفعلي لمدير مالي لاتخاذ قرار حول السيولة (runway). حمّل دليل بنود محامي العقود لإجراء تعديل. حمّل حكم منسّق الأبحاث السريرية للتعامل مع انحراف في بروتوكول. بدّل الأدوار حسب المهمة، عند الطلب، بتكلفة الاستدلال بدلًا من تكلفة التوظيف. شخص واحد، عميل واحد، وخبرة اتخاذ القرار المتراكمة لدى مئات المهن.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

هذا هو الهدف النهائي الفعلي هنا، وليس مجرد فضول: الحاجز بين "أحتاج خبيرًا" و"لديّ خبير" ينهار. ويصبح ذلك أكثر واقعية مع نمو التغطية — 92 دورًا مقابل 1,016 مهنة مُتتبَّعة اليوم؛ خارطة الطريق موجودة لسدّ تلك الفجوة، لا لإبقائها مثيرة للاهتمام إلى الأبد.

هذا لا يحلّ محلّ الحكم المهني أو المساءلة أو الترخيص حيث يجب قانونًا أن يبقى ذلك بيد إنسان — كل دور خاضع للتنظيم (القانون، الطب، المالية) يوضّح ذلك صراحة. ما يحلّ محلّه هو احتكاك عدم القدرة على الوصول إلى ذلك الاستدلال أصلًا.

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

## كيف تُبنى الأدوار

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

يتّبع كل دور نفس العقد، مفروضًا بالمواصفة والتكامل المستمر:

1. **ثلاثة اختبارات إطلاق** — يجب أن يقرأه الممارس فيومئ برأسه لا أن يهزّ كتفيه؛ وأن يتخذ العميل المزوّد بالدور قرارات مختلفة بشكل قابل للقياس عمّا بدونه؛ وألّا يكون أي شيء فيه قابلًا للاشتقاق من مجرد المسمى الوظيفي.
2. **بنية ثابتة** — الهوية، ونواة المبادئ الأولى، والاستدلالات الشرطية ("عند X، الافتراضي هو Y ما لم يكن Z")، وإطار قرار قابل للتنفيذ، وأنماط الفشل الشائعة، ومثال عملي بأرقام حقيقية متّسقة ينتهي بالمُخرَج الفعلي (المذكّرة، التعديل، التقرير).
3. **ثلاثية المراجع** — ملف دليل/مواد متعمّق بقوالب مُعبَّأة، و`red-flags.md` (الإشارة ← ما تعنيه ← السؤال الأول ← البيانات الواجب سحبها)، و`vocabulary.md` (مصطلحات فنية مع توضيح سوء الاستخدام الشائع لها).
4. **إثبات المصدر (Provenance)** — المصادر مُسمّاة؛ الأرقام المحدَّدة إمّا تُنسب إلى مصادرها أو تُوسم كاستدلالات مذكورة. الأدوار الخاضعة للتنظيم (القانون، الطب، المالية) تحمل تنويهات صريحة.
5. **العمود الفقري لـ O*NET** — تتبع التغطية تصنيف وزارة العمل الأمريكية للمهن (1,016 مهنة)، بحيث يكون النمو منهجيًا لا عشوائيًا حسب ما بدا مثيرًا للاهتمام في أسبوع ما.

المواصفة الكاملة، ومعيار التقييم، وخط أنابيب الصياغة بواسطة نماذج اللغة الكبيرة: [`AUTHORING.md`](./AUTHORING.md).

## كيف نتحقّق — بشفافية، دون الحاجة إلى الثقة

"كُتب بواسطة خبراء" ادّعاء؛ هذا المستودع يقدّم الإيصالات بدلًا من ذلك. أربع طبقات مستقلة، يمكن لأي شخص تشغيلها جميعًا من هذه النسخة المحلية:

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

آخر عمليات التشغيل المنشورة (2026-07-06، Haiku 4.5 يجيب، Sonnet 5 يحكم بشكل أعمى، كلا المحرّكين):

- **مضاد للواقع (Counterfactual):** يفوز الدور في **13 من 15 سيناريو** (تعادل واحد، خسارة واحدة) — إصابة 72% من معايير سلوك الخبير مقابل 37% لخط الأساس العام (generalist).
- **التكافؤ مقابل البشر (Parity):** الإجابة المُنتَجة عبر الدور مُفضَّلة على إجابة الممارس الحقيقي المقبولة في Stack Exchange في **5 من أصل 8** مقارنات مباشرة عمياء (عيّنة صغيرة؛ مجموعات الأسئلة في تزايد — اعتبرها إشارة أولية لا دراسة).

كل نتيجة قابلة لإعادة الإنتاج: `python3 evals/run_evals.py` و`python3 evals/parity/run_parity.py`. حين يفشل دور في هذه الاختبارات، فذلك أيضًا معلن للعموم — الهدف هو القياس لا التسويق. تبقى مراجعة الممارس هي النجمة الذهبية في الأعلى (`metadata.maturity`)، لكن الحد الأدنى للثقة مقاس لا موثوق به بمجرد الشهادة.

## الأدوار الحالية

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

هذه الكتلة مُولَّدة تلقائيًا — نفّذ `python3 scripts/generate_roadmap.py` بعد إضافة أو حذف أو إعادة تخطيط أي دور، ولا تُعدّلها يدويًا.

## الاستخدام مع أداة الذكاء الاصطناعي لديك

`SKILL.md` تنسيق عابر للأدوات — نفس ملف الدور يعمل في Claude Code وCodex CLI وCursor وأكثر من 30 عميلًا آخر. الفرق الوحيد هو مجلد التثبيت.

### بلا إعداد: الصق هذا في عميلك

انسخ هذا إلى Claude Code أو Codex أو Cursor أو أي عميل لديه صلاحية وصول للطرفية (shell)، صف مهمتك في الأسفل، وسيقوم بتثبيت الخبير المناسب من تلقاء نفسه:

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

**مستخدمو Claude Code وCodex وGemini CLI وCursor وWindsurf وRoo Code وAmp:** تخطَّ عملية اللصق — يقوم `npx domain-experts command --tool <id>` بتثبيت `/domain-expert` مرة واحدة، ثم فقط نفّذ `/domain-expert <task>` في كل مرة (انظر [أمر `/domain-expert`](#domain-expert-slash-command) أدناه).

### التثبيت حسب الأداة

| الأداة | الطريقة |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — يُثبَّت في `./.claude/skills/<slug>/`، ويُلتقط تلقائيًا كمهارة (skill). |
| **Codex CLI** | نفس الأمر مع `--to .codex/skills/<slug>` (على مستوى المشروع) أو `--to ~/.codex/skills/<slug>` (شخصي). تلتقطه الجلسة الجديدة تلقائيًا. |
| **Cursor** | نفس الأمر مع `--to .cursor/skills/<slug>` — يقرأ Cursor نفس تنسيق `SKILL.md` أصلًا. |
| **Windsurf وRoo Code وGoose وغيرها من الأدوات المتوافقة مع SKILL.md** | نفس الأمر مع `--to <مجلد مهارات الأداة>/<slug>` — راجع وثائق أداتك لمعرفة المسار الصحيح. |
| **الأدوات التي تقرأ `AGENTS.md`** (GitHub Copilot، Jules، Amp، Zed، ...) | ثبّت في أي مكان داخل المستودع (مثلًا `--to skills/<slug>`)، ثم أضف سطرًا واحدًا إلى `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **أي ذكاء اصطناعي محادثة (بلا وصول للطرفية)** | افتح الدور على GitHub، والصق `SKILL.md` في تلقين النظام أو التعليمات المخصّصة؛ الصق ملفات `references/` عندما تحتاج المحادثة إلى ذلك العمق. |

كل عملية تثبيت تنسخ الدور بالكامل — `SKILL.md` مع `references/` — بحيث تنتقل الأدلة المتعمّقة معه.

### التوجيه التلقائي

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) مهارة وصفية (meta-skill) تزيل حتى خطوة `match` — ثبّتها بـ `npx domain-experts add domain-expert-router`، حمّلها مرة واحدة، وسيجد عميلك الدور الصحيح لطلبات "تصرّف كـ X" من تلقاء نفسه، ويخبرك بصدق حين لا يكون دور ما مُغطّى.

### أمر `/domain-expert`

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

أعد تشغيل جلستك، ثم استخدم `/domain-expert <task>` مباشرة — مثلًا `/domain-expert review this vendor contract`. يُنفّذ `match`، ويحمّل `SKILL.md` الخاص بالدور الفائز (و`references/` عند الحاجة)، ويجيب كذلك الخبير، أو يخبرك بصدق حين لا تتطابق أي مهارة بعد. نفس فكرة مهارة التوجيه أعلاه، لكن مُعبَّأة كأمر لمرة واحدة بدلًا من مهارة محمَّلة دائمًا.

| `--tool` | يُثبَّت في | ملاحظات |
|---|---|---|
| `claude` (افتراضي) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | يقرأ Codex التلقينات فقط من المجلد على مستوى المستخدم، ولا خيار محلي للمشروع؛ توثيق OpenAI يشير إلى أن هذه الآلية مهجورة لصالح "المهارات (skills)" لكنها لا تزال تعمل |
| `gemini` | `.gemini/commands/domain-expert.toml` | تنسيق TOML |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | يسمّيها Windsurf "سير عمل (workflows)" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | موقع Amp ثابت عند جذر المستودع، ولا يوجد مجلد عام منفصل |

أضف `--global` للتثبيت في مجلد المستخدم الخاص بالأداة (مثل `~/.claude/commands/`، `~/.cursor/commands/`) بدلًا من مجلد المشروع، أو `--to <path>` لموقع مخصّص بالكامل.

### مرجع سطر الأوامر (CLI)

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

يقيّم `match` الأدوار بحسب تداخل الكلمات المفتاحية ويُبلغ إمّا عن تطابق واثق، أو مرشّحين بثقة منخفضة، أو "غير مُغطّى بعد" بصدق — لا يخمّن بصمت. استخدم `--json` للاستخدام البرمجي.

تلتقط حزمة npm نسخة من مكتبة الأدوار عند كل إصدار. للحصول على أحدث ما لم يُنشر بعد، استخدم `npx --yes github:wonsukchoi/domain-experts <command>` — نفس الواجهة، مباشرة من `main`.

## خارطة الطريق

[`ROADMAP.md`](./ROADMAP.md) هي قائمة المهام الرئيسية — جميع مهن O*NET البالغة 1,016، مُجمَّعة حسب الفئة، ومُؤشَّر عليها كلما صيغت مسودة. استخدمها لإيجاد دور غير مُغطّى بدلًا من التخمين حول ما هو ناقص.

## المساهمة — هذا المستودع يتراكم

كل دور يُضاف يجعل المُوجِّه أذكى، وكل تصويب يصل إلى كل مستخدم في الإصدار التالي، وكل سؤال تقييم يجعل معيار الجودة أصعب على التحايل. التلقين الذي تكتبه لنفسك يموت بانتهاء جلستك؛ أمّا الدور الذي تساهم به هنا فيعمل للجميع، إلى الأبد، ويستمر في التحسّن بعد رحيلك. هذا هو الرهان بأكمله: **1,016 مهنة ليست مشروعًا فرديًا — إنها مشترك (commons).**

الأسئلة الشائعة (فشل الفحص، تعارضات الدفع، عملية الإصدار) ← [`docs/FAQ.md`](./docs/FAQ.md).

ثلاث طرق للمشاركة، بأي مستوى مهارة:

1. **هل تعمل في دور نُغطّيه؟** اقرأه. أي خطأ فيه هو [قضية تصويب من ممارس](../../issues/new/choose) تستغرق دقيقتين — أقيَم مساهمة يمكن أن يتلقّاها هذا المشروع. لا حاجة لمهارات طلبات السحب (PR).
2. **تريد كتابة دور جديد أو ترقيته؟** اتّبع الوصفة الدقيقة في [`CONTRIBUTING.md`](./CONTRIBUTING.md) — مكتوبة بدقة تكفي لأن ينفّذها نموذج لغة كبير، بحيث يمكنك أنت ومساعدك الذكي إنجازها معًا. يخبرك الفحص (lint) إن كانت البنية قاصرة قبل أن يراجعها أي إنسان. 42 دورًا قديمًا [متاحة للمطالبة بها الآن](../../issues/1).
3. **لا تستطيع الكتابة لكن تستطيع البحث؟** اجمع أسئلة التكافؤ (`evals/parity/harvest_stackexchange.py`) أو قدّم [طلب دور](../../issues/new/choose) بالمهام التي كنت ستُفوّضها إليه.

إذا تعارضت المواصفة مع واقع الممارس، فالمواصفة هي التي تخسر — اذكر ذلك في طلب السحب الخاص بك وسنُصلح المواصفة.

## الرخصة

MIT — انظر [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
</content>
