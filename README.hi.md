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

**जॉब रोल डेफिनिशन्स** की ओपन सोर्स लाइब्रेरी — असली प्रैक्टिशनर्स की वास्तविक मानसिक मॉडल, निर्णय सीमाएँ (decision thresholds), और फेल्योर मोड्स, इस तरह संरचित कि कोई भी AI एजेंट उसे लोड करके उसी एक्सपर्ट की तरह तर्क (reason) कर सके। अपने एजेंट से कहें "इस कॉन्ट्रैक्ट को रिव्यू करो" और वह एक सीनियर कॉन्ट्रैक्ट्स अटॉर्नी की क्लॉज़ प्लेबुक और फॉलबैक लैडर के साथ जवाब देगा, न कि इंटरनेट के किसी जनरलिस्ट सारांश के साथ।

**यहाँ जाएँ:** [क्विक स्टार्ट](#क्विक-स्टार्ट) · ["क्या मैं Claude से बस यह न कहूँ?"](#क्या-मैं-claude-से-बस-यह-नहीं-कह-सकता-कि-cfo-की-तरह-एक्ट-करे) · [विज़न](#विज़न-एक-व्यक्ति-हर-एक्सपर्ट) · [रोल्स कैसे बनते हैं](#रोल्स-कैसे-बनते-हैं) · [हम वेरिफ़ाई कैसे करते हैं](#हम-वेरिफ़ाई-कैसे-करते-हैं-पारदर्शी-भरोसे-की-ज़रूरत-नहीं) · [मौजूदा रोल्स](#मौजूदा-रोल्स) · [अपने टूल के साथ इस्तेमाल करें](#इसे-अपने-ai-टूल-के-साथ-इस्तेमाल-करें) · [रोडमैप](#रोडमैप) · [योगदान](#योगदान-यह-रिपो-जमा-होता-है-compounds)

## क्विक स्टार्ट

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

इंस्टॉल करने की ज़रूरत नहीं — `npx` इसे सीधे npm से लाता है। अक्सर इस्तेमाल करते हैं? `npm install -g domain-experts` करें और `npx` हटा दें।

**Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, या Amp इस्तेमाल कर रहे हैं?** `npx domain-experts command --tool <id>` इसके लिए एक `/domain-expert` स्लैश कमांड इंस्टॉल करता है — अपना सेशन रीस्टार्ट करें और `/domain-expert review this vendor contract` चलाएँ। यह एक ही स्टेप में सही रोल को मैच करता है, लोड करता है, और उसकी तरह तर्क करता है — मैन्युअल `match`/`add` की झंझट नहीं।

या मैन्युअल स्टेप को पूरी तरह छोड़ दें: [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) को एक बार लोड करें, और आपका एजेंट खुद पहचान लेगा कि किसी टास्क को कौन सा एक्सपर्ट चाहिए, रोल का पूरा कॉन्टेक्स्ट अपने आप खींच लेगा, और अगर कोई रोल अभी कवर नहीं है तो सुधार करने के बजाय ईमानदारी से बता देगा। आप काम करते रहें; सही एक्सपर्टीज़ खुद-ब-खुद सामने आ जाती है।

## "क्या मैं Claude से बस यह नहीं कह सकता कि CFO की तरह एक्ट करे?"

कर सकते हैं — और आपको मिलेगी एक सतही नकल: इंटरनेट पर हर जॉब डिस्क्रिप्शन का औसत, हर सेशन में शुरू से दोबारा जनरेट, हर बार अलग, और किसी के द्वारा भी वेरिफाई न किया हुआ।

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

अंतर, ठोस रूप में:

- **नॉन-डिराइवेबल कंटेंट।** हर रोल को नॉन-डिराइवेबिलिटी टेस्ट पास करना होता है: कुछ भी ऐसा नहीं जो सिर्फ़ जॉब टाइटल से दोबारा जनरेट हो सके। जो बचता है वह वही है जो प्रॉम्प्टिंग डिमांड पर नहीं बना सकती — न्यूमेरिक रेड-फ्लैग थ्रेशोल्ड्स, मार्केट-स्टैंडर्ड नेगोशिएशन रेंज, ऐसे वर्क्ड एग्ज़ाम्पल जिनका अंकगणित मिलता है, और प्राथमिकता क्रम में फॉलबैक पोज़िशन्स।
- **एक क्वालिटी गेट, न कि सिंगल जनरेशन।** रोल्स एक मल्टी-पास पाइपलाइन ([`AUTHORING.md`](./AUTHORING.md)) के ज़रिए बनते हैं — नीचे डायग्राम देखें। एक-लाइन प्रॉम्प्ट में इनमें से कुछ भी नहीं मिलता।
- **CI-एनफ़ोर्स्ड स्ट्रक्चर।** हर PR पर [`scripts/lint_roles.py`](./scripts/lint_roles.py) चलता है: स्कीमा, ज़रूरी सेक्शन, रिज़ॉल्व होते लिंक्स, बैन की गई फिलर फ्रेज़ेस, रेड-फ्लैग की पूर्णता, वर्क्ड एग्ज़ाम्पल में असली नंबर। जेनेरिक जॉब-डिस्क्रिप्शन टेक्स्ट बिल्ड फेल कर देता है।
- **यह जमा होता जाता है (compounds)।** आपका फ़ौरी (ad-hoc) प्रॉम्प्ट सेशन खत्म होते ही गायब हो जाता है। ये फ़ाइलें प्रैक्टिशनर करेक्शन्स जमा करती हैं, एक मैच्योरिटी लैडर (`draft` → `reviewed-by-practitioner` → `mature`) और एक वर्ज़न्ड स्पेक (`spec: 2` वर्तमान बार पर मौजूद रोल्स को दिखाता है) साथ रखती हैं, और हर PR के साथ बेहतर होती जाती हैं। सुधार सबतक पहुँचते हैं।
- **डिज़ाइन से ही टोकन-एफिशिएंट।** हर रोल एक कॉम्पैक्ट रीज़निंग कोर (`SKILL.md`) प्लस ऑन-डिमांड गहराई (`references/`) है। एजेंट गहराई के लिए तभी पेमेंट करता है जब टास्क को उसकी ज़रूरत हो:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### असली moat (बढ़त) है क्या?

वाजिब सवाल: ऊपर बताई कोई भी बात किसी को इस पूरे रिपॉज़िटरी का `git clone` लेकर अपने प्रोडक्ट के तौर पर लॉन्च करने से नहीं रोकती — MIT लाइसेंस, कंटेंट पर कोई लॉक-इन नहीं। ईमानदार जवाब: फ़ाइलों का यह सेट ही moat नहीं है। जो कॉपी करना मुश्किल है, वह है वह मशीनरी जो इसे लगातार बनाती और सुधारती रहती है:

- **आउटपुट नहीं, पाइपलाइन।** 97 फ़ाइलें कॉपी करना एक कमांड का काम है। पर adversarial-critique → 9-criterion rubric → lint-gated authoring loop ([`AUTHORING.md`](./AUTHORING.md)) कॉपी करना, जो इन्हें लगातार बनाता और सुधारता रहता है, वैसा नहीं — फ़ोर्क को आज का स्नैपशॉट मिलता है, कल के सुधार नहीं।
- **डेटाबेस नहीं, स्टैंडर्ड।** `SKILL.md` पहले से 30+ एजेंट टूल्स में चलता है। एक पोर्टेबल ओपन फॉर्मेट में सबसे बड़ी लाइब्रेरी होना डिस्ट्रिब्यूशन की पोज़िशन है, कंटेंट की नहीं — वैल्यू बाइट्स में नहीं, बल्कि डिफ़ॉल्ट जवाब बनने में है जो लोगों को मिलता है।
- **दावा नहीं, वेरिफ़ाई किया हुआ।** कोई भी प्रतिस्पर्धी कह सकता है "expert ने लिखा है"। कम ही लोग आपके सामने `python3 evals/run_evals.py` चलाकर 13/15 counterfactual जीत दिखा सकते हैं। यहाँ भरोसा मापा और दोहराया जा सकता है, बस कहा नहीं जाता।
- **ताज़गी parametric recall से बेहतर।** भले ही भविष्य का कोई मॉडल इस रिपॉज़िटरी के पब्लिक टेक्स्ट पर ट्रेन हो जाए, वह जानकारी ट्रेनिंग कटऑफ़ पर फ्रीज़ हो जाती है। इस रिपॉज़िटरी के सुधार उसी दिन शिप होते हैं जिस दिन कोई practitioner उन्हें फ़ाइल करता है — कोई रीट्रेन साइकिल नहीं, वर्ज़न्ड, सोर्स तक ट्रेस किए हुए।
- **कवरेज की डिसिप्लिन।** O*NET का 1,016-occupation बैकबोन long-tail कवरेज को systematic बनाता है (funeral-home-manager, wind-energy-operations-manager) — जो opportunistic प्रतिस्पर्धी सिर्फ़ trending roles क्यूरेट करता है, वह इतनी मेहनत नहीं करेगा।
- **फ्री और पोर्टेबल, सब्सक्रिप्शन-लॉक्ड से बेहतर।** यह आपके LLM बिल से मुक़ाबला नहीं करता — inference का पैसा तो वैसे भी देना है। इसका मुक़ाबला बंद vertical SaaS से है ("AI Legal Advisor," $99/माह) — वो free, forkable, और local model पर बिना recurring cost चलने वाले ऑप्शन को मात नहीं दे सकते।

97 roles और छोटे contributor base के साथ अभी यह moat नहीं है — यह एक trajectory है। दांव यह है: commons किसी भी single fork से तेज़ी से compound करेगा, जैसे ही काफ़ी practitioners हर session prompt से शुरू करने के बजाय corrections file करना शुरू कर दें।

## विज़न — एक व्यक्ति, हर एक्सपर्ट

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

आज, अपने खुद के क्षेत्र से बाहर कुछ अच्छी तरह करने का मतलब है हायरिंग, कॉन्ट्रैक्टिंग, या आउटरीच — कोई वकील ढूँढना, किसी CFO के कैलेंडर का इंतज़ार करना, किसी मार्केटिंग स्ट्रैटेजिस्ट की फीस चुकाना। यह घर्षण (friction) हर सोलो फाउंडर, हर छोटी टीम, और अपनी विशेषज्ञता से बाहर किसी समस्या से जूझने वाले हर व्यक्ति पर लगने वाला एक टैक्स है। ज़्यादातर लोग या तो वह काम करते ही नहीं, या बुरी तरह करते हैं।

एक AI सब्सक्रिप्शन वाला व्यक्ति — या बिना किसी सब्सक्रिप्शन के एक लोकल मॉडल — और यह रिपो, यह टैक्स नहीं चुकाता। रनवे के फैसले के लिए CFO की असली सोच लोड करें। रीडलाइन के लिए कॉन्ट्रैक्ट्स वकील की क्लॉज़ प्लेबुक लोड करें। प्रोटोकॉल डेविएशन के लिए क्लिनिकल रिसर्च कोऑर्डिनेटर का निर्णय (judgment) लोड करें। हर टास्क के हिसाब से, ऑन-डिमांड रोल बदलें — हायरिंग की कीमत की बजाय सिर्फ़ इनफ़रेंस की लागत पर। एक व्यक्ति, एक एजेंट, सैकड़ों प्रोफेशन्स की संचित निर्णय-प्रक्रिया।

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

यही असली अंतिम लक्ष्य है, कोई महज़ जिज्ञासा नहीं: "मुझे एक एक्सपर्ट चाहिए" और "मेरे पास एक है" के बीच की बाधा ढह जाती है। कवरेज बढ़ने के साथ यह और सच होता जाता है — आज 1,016 ट्रैक की गई ऑक्यूपेशन्स के मुकाबले 92 रोल्स; रोडमैप इसी लिए है ताकि यह गैप बंद हो, न कि हमेशा दिलचस्प बना रहे।

यह जजमेंट, जवाबदेही, या लाइसेंसिंग की जगह नहीं लेता जहाँ कानूनन इनका दायित्व किसी इंसान पर ही होना चाहिए — हर रेगुलेटेड रोल (लॉ, मेडिसिन, फाइनेंस) इसे स्पष्ट रूप से कहता है। यह सिर्फ़ उस घर्षण को दूर करता है जो शुरुआत में उस तर्क तक पहुँच न होने से पैदा होता है।

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

## रोल्स कैसे बनते हैं

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

हर रोल एक ही कॉन्ट्रैक्ट फॉलो करता है, जिसे स्पेक और CI दोनों एनफ़ोर्स करते हैं:

1. **तीन शिप टेस्ट** — एक प्रैक्टिशनर इसे पढ़कर सिर हिलाए (nod), कंधे न उचकाए; रोल के साथ एजेंट बिना रोल के मुकाबले नापने योग्य (measurably) अलग फैसले ले; इसमें कुछ भी सिर्फ़ जॉब टाइटल से डिराइव करने लायक न हो।
2. **तय एनाटॉमी** — आइडेंटिटी, फर्स्ट-प्रिंसिपल्स कोर, कंडीशनल हेयुरिस्टिक्स ("जब X हो, तो डिफ़ॉल्ट Y लें जब तक Z न हो"), एक एक्ज़ीक्यूटेबल डिसीज़न फ्रेमवर्क, आम फेल्योर मोड्स, और असली, मिलते-जुलते नंबरों वाला एक वर्क्ड एग्ज़ाम्पल जो असली डिलिवरेबल (मेमो, रीडलाइन, रीडआउट) पर खत्म हो।
3. **रेफरेंस त्रयी (trio)** — भरे हुए टेम्पलेट्स वाली एक डीप-डाइव प्लेबुक/आर्टिफैक्ट्स फ़ाइल, `red-flags.md` (सिग्नल → इसका मतलब क्या है → पहला सवाल → कौन-सा डेटा निकालें), और `vocabulary.md` (टर्म्स ऑफ़ आर्ट, साथ में आम गलत इस्तेमाल का ब्यौरा)।
4. **प्रोवेनेंस** — स्रोत नामित होते हैं; विशिष्ट नंबर या तो उन तक ट्रेस होते हैं या स्टेटेड हेयुरिस्टिक के रूप में लेबल होते हैं। रेगुलेटेड रोल्स (लॉ, मेडिसिन, फाइनेंस) में स्पष्ट डिस्क्लेमर होते हैं।
5. **O*NET बैकबोन** — कवरेज अमेरिकी लेबर डिपार्टमेंट की ऑक्यूपेशन टैक्सोनॉमी (1,016 ऑक्यूपेशन्स) को फॉलो करती है, ताकि ग्रोथ सिस्टेमैटिक हो, न कि जो उस हफ़्ते दिलचस्प लगा वही चुन लिया जाए।

पूरा स्पेक, रूब्रिक, और LLM ड्राफ्टिंग पाइपलाइन: [`AUTHORING.md`](./AUTHORING.md)।

## हम वेरिफ़ाई कैसे करते हैं — पारदर्शी, भरोसे की ज़रूरत नहीं

"एक्सपर्ट्स द्वारा लिखा गया" एक दावा है; यह रिपो इसकी बजाय रसीदें (receipts) देता है। चार स्वतंत्र लेयर्स, जिन्हें कोई भी इस चेकआउट से खुद चला सकता है:

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

नवीनतम प्रकाशित रन (2026-07-06, Haiku 4.5 जवाब दे रहा है, Sonnet 5 ब्लाइंड जज कर रहा है, दोनों हार्नेस):

- **काउंटरफैक्चुअल:** स्किल **13/15 सिनैरियो** में जीतता है (1 टाई, 1 हार) — जनरलिस्ट बेसलाइन के 37% के मुकाबले 72% एक्सपर्ट-बिहेवियर क्राइटेरिया हिट हुए।
- **पैरिटी बनाम इंसान:** ब्लाइंड हेड-टू-हेड में असली प्रैक्टिशनर के स्वीकृत Stack Exchange जवाब के मुकाबले स्किल का जवाब **8 में से 5** बार प्रेफर किया गया (छोटा सैंपल; क्वेश्चन सेट बढ़ रहे हैं — इसे एक अध्ययन नहीं, बल्कि एक शुरुआती संकेत मानें)।

हर नतीजा रीप्रोड्यूसिबल है: `python3 evals/run_evals.py` और `python3 evals/parity/run_parity.py`। जब कोई रोल इन टेस्ट में फेल होता है, वह भी पब्लिक होता है — मकसद मापना है, मार्केटिंग नहीं। प्रैक्टिशनर रिव्यू अब भी ऊपर की गोल्ड स्टार है (`metadata.maturity`), लेकिन भरोसे का फ़्लोर मापा जाता है, महज़ मान लिया नहीं जाता।

## मौजूदा रोल्स

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

यह ब्लॉक ऑटो-जनरेटेड है — कोई रोल जोड़ने/हटाने/री-मैप करने के बाद `python3 scripts/generate_roadmap.py` चलाएँ, इसे हाथ से एडिट न करें।

## इसे अपने AI टूल के साथ इस्तेमाल करें

`SKILL.md` एक क्रॉस-टूल फॉर्मेट है — वही रोल फ़ाइल Claude Code, Codex CLI, Cursor, और 30+ अन्य एजेंट्स में काम करती है। सिर्फ़ इंस्टॉल डायरेक्टरी अलग होती है।

### ज़ीरो सेटअप: इसे अपने एजेंट में पेस्ट करें

इसे Claude Code, Codex, Cursor, या शेल एक्सेस वाले किसी भी एजेंट में कॉपी करें, नीचे अपना टास्क बताएं, और यह खुद सही एक्सपर्ट इंस्टॉल कर लेगा:

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

**Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, और Amp यूज़र्स:** पेस्ट वाला तरीका छोड़ दें — `npx domain-experts command --tool <id>` एक बार `/domain-expert` इंस्टॉल कर देता है, फिर हर बार बस `/domain-expert <task>` चलाएँ (नीचे [`/domain-expert` स्लैश कमांड](#domain-expert-स्लैश-कमांड) देखें)।

### टूल के हिसाब से इंस्टॉल

| टूल | कैसे |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — `./.claude/skills/<slug>/` में जाता है, खुद-ब-खुद एक स्किल के रूप में पहचाना जाता है। |
| **Codex CLI** | वही कमांड `--to .codex/skills/<slug>` (प्रोजेक्ट) या `--to ~/.codex/skills/<slug>` (पर्सनल) के साथ। नया सेशन इसे उठा लेता है। |
| **Cursor** | वही कमांड `--to .cursor/skills/<slug>` के साथ — Cursor वही `SKILL.md` फॉर्मेट नेटिवली पढ़ता है। |
| **Windsurf, Roo Code, Goose और अन्य SKILL.md-कम्पैटिबल टूल्स** | वही कमांड `--to <आपके टूल की स्किल्स डायरेक्टरी>/<slug>` के साथ — पाथ के लिए अपने टूल के डॉक्स देखें। |
| **`AGENTS.md` पढ़ने वाले टूल्स** (GitHub Copilot, Jules, Amp, Zed, …) | रिपो में कहीं भी इंस्टॉल करें (जैसे `--to skills/<slug>`), फिर `AGENTS.md` में एक लाइन जोड़ें: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **कोई भी चैट AI (बिना शेल के)** | GitHub पर रोल खोलें, `SKILL.md` को सिस्टम प्रॉम्प्ट या कस्टम इंस्ट्रक्शन्स में पेस्ट करें; जब बातचीत को उस गहराई की ज़रूरत हो तो `references/` की फ़ाइलें पेस्ट करें। |

हर इंस्टॉल पूरे रोल की कॉपी करता है — `SKILL.md` प्लस `references/` — ताकि गहरी प्लेबुक भी साथ जाएँ।

### ऑटोमैटिक डिस्पैच

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) एक मेटा-स्किल है जो `match` स्टेप को भी हटा देता है — इसे `npx domain-experts add domain-expert-router` से इंस्टॉल करें, एक बार लोड करें, और आपका एजेंट "act as X" जैसी रिक्वेस्ट्स के लिए सही रोल खुद ढूँढ लेगा, और ईमानदारी से बताएगा जब कोई रोल कवर नहीं है।

### `/domain-expert` स्लैश कमांड

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

अपना सेशन रीस्टार्ट करें, फिर सीधे `/domain-expert <task>` इस्तेमाल करें — जैसे `/domain-expert review this vendor contract`। यह `match` चलाता है, जीतने वाले रोल का `SKILL.md` (और ज़रूरत पड़ने पर `references/`) लोड करता है, और उस एक्सपर्ट की तरह जवाब देता है, या ईमानदारी से बताता है जब अभी तक कुछ मैच नहीं होता। ऊपर वाले राउटर स्किल जैसा ही आइडिया, बस हमेशा-लोडेड स्किल की बजाय एक वन-शॉट कमांड के रूप में पैक किया गया।

| `--tool` | इंस्टॉल होता है यहाँ | नोट्स |
|---|---|---|
| `claude` (डिफ़ॉल्ट) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex सिर्फ़ यूज़र-लेवल डायरेक्टरी से prompts पढ़ता है, कोई प्रोजेक्ट-लोकल ऑप्शन नहीं; OpenAI के डॉक्स इस मैकेनिज़्म को "skills" के पक्ष में डेप्रिकेटेड बताते हैं पर यह अभी भी काम करता है |
| `gemini` | `.gemini/commands/domain-expert.toml` | TOML फॉर्मेट |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf इन्हें "workflows" कहता है |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | Amp का लोकेशन रिपो रूट पर फ़िक्स्ड है, कोई अलग ग्लोबल डायरेक्टरी नहीं |

`--global` जोड़ने पर यह प्रोजेक्ट डायरेक्टरी की बजाय टूल की यूज़र-लेवल डायरेक्टरी में इंस्टॉल होता है (जैसे `~/.claude/commands/`, `~/.cursor/commands/`), या पूरी तरह कस्टम लोकेशन के लिए `--to <path>` इस्तेमाल करें।

### CLI रेफरेंस

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` रोल्स को कीवर्ड ओवरलैप के आधार पर स्कोर करता है और एक कॉन्फिडेंट हिट, कम-कॉन्फिडेंस कैंडिडेट्स, या ईमानदार "अभी कवर नहीं" रिपोर्ट करता है — यह चुपचाप अंदाज़ा नहीं लगाता। प्रोग्रामैटिक उपयोग के लिए `--json`।

npm पैकेज हर रिलीज़ पर रोल लाइब्रेरी का स्नैपशॉट लेता है। अनरिलीज़्ड बिलकुल लेटेस्ट के लिए, `npx --yes github:wonsukchoi/domain-experts <command>` इस्तेमाल करें — वही CLI, सीधे `main` से।

## रोडमैप

[`ROADMAP.md`](./ROADMAP.md) मास्टर बैकलॉग है — सभी 1,016 O*NET ऑक्यूपेशन्स, कैटेगरी के हिसाब से समूहित, ड्राफ्ट होते ही चेक-ऑफ किए जाते हैं। जो कवर नहीं है उसे अंदाज़ा लगाने के बजाय इसका इस्तेमाल करके ढूँढें।

## योगदान — यह रिपो जमा होता है (compounds)

हर जोड़ा गया रोल राउटर को स्मार्ट बनाता है, हर करेक्शन अगले रिलीज़ में हर यूज़र तक पहुँचता है, और हर eval क्वेश्चन क्वालिटी बार को नकली बनाना और मुश्किल कर देता है। आप खुद के लिए जो प्रॉम्प्ट लिखते हैं वह आपके सेशन के साथ खत्म हो जाता है; यहाँ आपका योगदान किया गया रोल सबके लिए, हमेशा के लिए काम करता है, और आपके जाने के बाद भी बेहतर होता रहता है। यही पूरी शर्त है: **1,016 ऑक्यूपेशन्स कोई सोलो प्रोजेक्ट नहीं है — यह एक कॉमन्स है।**

आम सवाल (लिंट फ़ेलियर, पुश कॉन्फ्लिक्ट्स, रिलीज़ प्रोसेस) → [`docs/FAQ.md`](./docs/FAQ.md)।

शामिल होने के तीन तरीके, किसी भी स्किल लेवल पर:

1. **आप किसी ऐसे रोल में काम करते हैं जो हम कवर करते हैं?** इसे पढ़ें। कोई भी गलती एक 2-मिनट का [प्रैक्टिशनर-करेक्शन इशू](../../issues/new/choose) है — इस प्रोजेक्ट को मिलने वाला सबसे मूल्यवान योगदान। किसी PR स्किल की ज़रूरत नहीं।
2. **कोई रोल लिखना या अपग्रेड करना चाहते हैं?** [`CONTRIBUTING.md`](./CONTRIBUTING.md) में दी गई एग्ज़ैक्ट रेसिपी फॉलो करें — यह इतनी सटीकता से लिखी गई है कि एक LLM इसे एक्ज़ीक्यूट कर सकता है, ताकि आप और आपका AI असिस्टेंट इसे साथ मिलकर कर सकें। किसी इंसान के रिव्यू करने से पहले ही लिंट बता देता है कि स्ट्रक्चर कहाँ कम पड़ रहा है। 42 लेगेसी रोल्स अभी [क्लेम करने के लिए उपलब्ध हैं](../../issues/1)।
3. **लिख नहीं सकते पर ढूँढ सकते हैं?** पैरिटी क्वेश्चन्स इकट्ठा करें (`evals/parity/harvest_stackexchange.py`) या उन टास्क्स के साथ एक [रोल रिक्वेस्ट](../../issues/new/choose) फ़ाइल करें जो आप उसे सौंपना चाहेंगे।

अगर स्पेक किसी प्रैक्टिशनर की वास्तविकता से टकराता है, तो स्पेक हार जाता है — अपने PR में यह बताएं और हम स्पेक ठीक करेंगे।

## लाइसेंस

MIT — देखें [`LICENSE`](./LICENSE)।

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
