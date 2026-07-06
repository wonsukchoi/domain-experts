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

Thư viện mã nguồn mở gồm các **định nghĩa vai trò công việc** — mô hình tư duy thực tế, ngưỡng ra quyết định, và các dạng thất bại thường gặp của những người hành nghề thật, được cấu trúc lại để bất kỳ AI agent nào cũng có thể nạp vào và suy luận như chuyên gia đó. Yêu cầu agent của bạn "xem lại hợp đồng này" và nó sẽ trả lời bằng chiến lược xử lý điều khoản và các nấc phòng vệ của một luật sư hợp đồng dày dạn kinh nghiệm, chứ không phải bản tóm tắt kiểu tổng quát từ internet.

**Chuyển nhanh đến:** [Bắt đầu nhanh](#bắt-đầu-nhanh) · ["Sao không bảo Claude đóng vai luôn?"](#sao-không-bảo-claude-đóng-vai-luôn) · [Tầm nhìn](#tầm-nhìn--một-người-mọi-chuyên-gia) · [Vai trò được xây dựng như thế nào](#vai-trò-được-xây-dựng-như-thế-nào) · [Cách chúng tôi kiểm chứng](#cách-chúng-tôi-kiểm-chứng--minh-bạch-không-cần-tin-suông) · [Danh sách vai trò hiện tại](#danh-sách-vai-trò-hiện-tại) · [Dùng với công cụ của bạn](#dùng-với-ai-tool-của-bạn) · [Lộ trình](#lộ-trình) · [Đóng góp](#đóng-góp--kho-này-sinh-lãi-kép)

## Bắt đầu nhanh

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

Không cần cài đặt gì — `npx` sẽ tự lấy về từ npm. Nếu dùng thường xuyên, hãy `npm install -g domain-experts` rồi bỏ `npx` đi.

**Đang dùng Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, hoặc Amp?** `npx domain-experts command --tool <id>` sẽ cài lệnh slash `/domain-expert` cho công cụ đó — khởi động lại phiên làm việc và chạy `/domain-expert review this vendor contract`. Nó tự tìm, nạp, và suy luận đúng vai trò cần thiết chỉ trong một bước, không cần tự làm thao tác `match`/`add` thủ công.

Hoặc bỏ qua bước thủ công hoàn toàn: nạp [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) một lần duy nhất, agent của bạn sẽ tự phát hiện tác vụ cần chuyên gia nào, tự động kéo toàn bộ ngữ cảnh của vai trò đó, và thẳng thắn báo cho bạn biết khi một vai trò chưa được phủ sóng thay vì tự ứng biến. Bạn cứ tiếp tục làm việc, chuyên môn phù hợp sẽ tự xuất hiện.

## "Sao không bảo Claude đóng vai luôn?"

Bạn có thể — và sẽ nhận được một bản bắt chước hời hợt: mức trung bình của mọi mô tả công việc trên internet, được tạo lại từ đầu mỗi phiên, khác nhau mỗi lần, không ai kiểm chứng.

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

Sự khác biệt cụ thể là:

- **Nội dung không thể suy diễn.** Mỗi vai trò phải vượt qua bài kiểm tra "không thể suy diễn" (non-derivability): loại bỏ bất cứ thứ gì có thể được tái tạo chỉ từ chức danh công việc. Những gì còn lại là thứ mà prompt không thể tạo ra theo yêu cầu — ngưỡng cảnh báo bằng số cụ thể, khoảng đàm phán theo chuẩn thị trường, ví dụ thực tế với phép tính khớp sổ, các phương án dự phòng theo thứ tự ưu tiên.
- **Một cổng kiểm định chất lượng, không phải một lần tạo sinh duy nhất.** Vai trò được xây dựng qua một pipeline nhiều bước ([`AUTHORING.md`](./AUTHORING.md)) — xem sơ đồ bên dưới. Một prompt một dòng không đi qua quy trình đó.
- **Cấu trúc được CI thực thi.** Mỗi PR đều chạy [`scripts/lint_roles.py`](./scripts/lint_roles.py): kiểm tra schema, các mục bắt buộc, liên kết có hoạt động không, các cụm từ sáo rỗng bị cấm, độ đầy đủ của các dấu hiệu cảnh báo, số liệu thực trong ví dụ thực hành. Văn bản mô tả công việc chung chung sẽ khiến build thất bại.
- **Nó sinh lãi kép.** Prompt bạn viết tạm thời sẽ biến mất khi phiên làm việc kết thúc. Các file này tích lũy các chỉnh sửa từ người hành nghề, có một thang trưởng thành (`draft` → `reviewed-by-practitioner` → `mature`) và một spec có phiên bản (`spec: 2` đánh dấu các vai trò đạt chuẩn hiện tại), và tốt lên sau mỗi PR. Các bản sửa lỗi đến được với tất cả mọi người.
- **Thiết kế tối ưu token.** Mỗi vai trò là một lõi suy luận gọn nhẹ (`SKILL.md`) cộng với chiều sâu nạp theo yêu cầu (`references/`). Agent chỉ trả "phí" cho chiều sâu khi tác vụ thực sự cần đến nó:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### Vậy lợi thế cạnh tranh thực sự là gì?

Một phản biện chính đáng: không điều gì ở trên ngăn được ai đó `git clone` chính kho này rồi đóng gói lại thành sản phẩm của riêng họ — giấy phép MIT, không hề bị khóa nội dung. Câu trả lời thẳng thắn: tập hợp file không phải là lợi thế. Cái khó fork chính là bộ máy tiếp tục tạo ra và sửa chữa nó:

- **Pipeline, không phải kết quả đầu ra.** Sao chép 97 file chỉ cần một lệnh. Nhưng sao chép vòng lặp phê bình đối kháng → chấm điểm theo 9 tiêu chí → chỉ xuất bản khi qua lint ([`AUTHORING.md`](./AUTHORING.md)) — thứ liên tục tạo ra và sửa chữa những file đó — thì không thể sao chép được: một bản fork chỉ thừa hưởng ảnh chụp nhanh của hôm nay, không thừa hưởng các bản sửa của ngày mai.
- **Một chuẩn, không phải một cơ sở dữ liệu.** `SKILL.md` đã chạy được trên hơn 30 công cụ agent. Là thư viện lớn nhất theo một định dạng mở, có thể mang đi được, là một vị thế phân phối chứ không phải vị thế nội dung — giá trị nằm ở việc trở thành câu trả lời mặc định mà mọi người tìm đến, không nằm ở bản thân các byte dữ liệu.
- **Được kiểm chứng, không phải được tuyên bố.** Đối thủ nào cũng có thể nói "do chuyên gia viết". Nhưng ít ai có thể chạy `python3 evals/run_evals.py` ngay trước mặt bạn và cho thấy tỉ lệ thắng phản thực (counterfactual) 13/15. Niềm tin ở đây được đo lường và tái tạo được, không phải chỉ là lời khẳng định.
- **Độ mới thắng trí nhớ tham số.** Ngay cả khi một model tương lai được huấn luyện trên văn bản công khai của kho này, kiến thức đó vẫn đóng băng tại thời điểm cắt dữ liệu huấn luyện. Các bản sửa của kho này được đưa ra ngay trong ngày người hành nghề báo cáo — không cần chu kỳ huấn luyện lại, có phiên bản, truy vết được đến nguồn.
- **Kỷ luật về độ phủ.** Bộ khung 1.016 ngành nghề của O*NET buộc việc phủ sóng phải mang tính hệ thống, kể cả các ngành nghề đuôi dài (funeral-home-manager, wind-energy-operations-manager) — điều mà một đối thủ cơ hội chỉ chọn lọc các vai trò đang hot sẽ không buồn theo kịp.
- **Miễn phí và mang đi được thắng mô hình khóa theo gói thuê bao.** Dự án này không cạnh tranh với hóa đơn LLM của bạn — bạn vẫn phải trả phí suy luận (inference) dù thế nào. Nó cạnh tranh với các SaaS chuyên biệt đóng ("AI Legal Advisor" giá 99 USD/tháng): những dịch vụ đó không thể sánh được với miễn phí, có thể fork được, và chạy được trên model cục bộ với chi phí định kỳ bằng 0.

Ở quy mô 97 vai trò và một cộng đồng đóng góp còn nhỏ, chưa có gì ở đây là một lợi thế cạnh tranh thực sự — đó là một quỹ đạo. Cược đặt ra là: cộng đồng chung (commons) sẽ sinh lãi kép nhanh hơn bất kỳ bản fork đơn lẻ nào có thể theo kịp, một khi đủ nhiều người hành nghề bắt đầu gửi bản sửa thay vì viết prompt từ đầu mỗi phiên.

## Tầm nhìn — một người, mọi chuyên gia

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

Hiện tại, làm tốt một việc gì đó ngoài chuyên môn của bạn đồng nghĩa với việc phải thuê, hợp tác, hoặc tiếp cận đối tác — tìm luật sư, chờ lịch của một CFO, trả phí cho một chiến lược gia marketing. Ma sát đó là một loại thuế đánh lên mọi nhà sáng lập một mình, mọi đội nhóm nhỏ, mọi cá nhân gặp phải vấn đề ngoài chuyên môn của họ. Phần lớn mọi người đơn giản là không làm việc đó, hoặc làm không tốt.

Một cá nhân có gói AI thuê bao — hoặc một model chạy cục bộ, thậm chí không cần thuê bao — cùng với kho này thì không phải trả loại thuế đó. Hãy nạp lý luận thực tế của một CFO cho một quyết định về dòng tiền (runway). Hãy nạp chiến lược xử lý điều khoản của một luật sư hợp đồng để chỉnh sửa hợp đồng. Hãy nạp phán đoán của một điều phối viên nghiên cứu lâm sàng để xử lý sai lệch giao thức. Đổi vai trò theo từng tác vụ, theo yêu cầu, với chi phí bằng đúng phí suy luận (inference) thay vì phí thuê người. Một người, một agent, và toàn bộ khả năng ra quyết định tích lũy của hàng trăm ngành nghề.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

Đó chính là đích đến thực sự ở đây, không phải một điều thú vị nhất thời: rào cản giữa "tôi cần một chuyên gia" và "tôi đã có một chuyên gia" sụp đổ. Điều này càng đúng hơn khi độ phủ tăng lên — 92 vai trò trên tổng số 1.016 ngành nghề đang được theo dõi tính đến hôm nay; lộ trình tồn tại để khoảng cách đó khép lại, chứ không phải để mãi mãi là một điều thú vị.

Dự án này không thay thế phán đoán, trách nhiệm giải trình, hay chứng chỉ hành nghề ở những nơi pháp luật bắt buộc phải do con người nắm giữ — mọi vai trò thuộc lĩnh vực bị quản lý (luật, y tế, tài chính) đều nói rõ điều đó. Nó thay thế sự ma sát của việc không có quyền tiếp cận lý luận đó ngay từ đầu.

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

## Vai trò được xây dựng như thế nào

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Mọi vai trò đều tuân theo cùng một quy ước, được spec và CI thực thi:

1. **Ba bài kiểm tra trước khi xuất bản** — người hành nghề đọc vào phải gật đầu chứ không nhún vai; một agent có vai trò này phải đưa ra quyết định khác biệt một cách đo lường được so với khi không có nó; không có gì trong đó có thể suy diễn chỉ từ chức danh công việc.
2. **Cấu trúc cố định** — danh tính (identity), lõi nguyên lý gốc (first-principles core), các quy tắc kinh nghiệm có điều kiện ("khi X, mặc định chọn Y trừ khi Z"), một khung ra quyết định có thể thực thi, các dạng thất bại thường gặp, và một ví dụ thực hành với số liệu thực, khớp sổ, kết thúc bằng chính sản phẩm bàn giao thực tế (bản ghi nhớ, bản chỉnh sửa hợp đồng, báo cáo).
3. **Bộ ba tài liệu tham chiếu** — một file playbook/artifact chuyên sâu với các mẫu đã điền sẵn, `red-flags.md` (tín hiệu → ý nghĩa → câu hỏi đầu tiên cần đặt → dữ liệu cần lấy), và `vocabulary.md` (thuật ngữ chuyên môn cùng cách dùng sai phổ biến).
4. **Nguồn gốc (Provenance)** — nguồn được nêu rõ tên; các con số cụ thể được truy vết về nguồn hoặc được gắn nhãn là quy tắc kinh nghiệm đã nêu. Các vai trò thuộc lĩnh vực bị quản lý (luật, y tế, tài chính) đi kèm tuyên bố miễn trừ trách nhiệm rõ ràng.
5. **Bộ khung O*NET** — độ phủ bám theo hệ thống phân loại ngành nghề của Bộ Lao động Hoa Kỳ (1.016 ngành nghề), nên sự tăng trưởng mang tính hệ thống, không phải chọn bừa những gì có vẻ thú vị trong tuần đó.

Spec đầy đủ, tiêu chí chấm điểm, và pipeline soạn thảo bằng LLM: [`AUTHORING.md`](./AUTHORING.md).

## Cách chúng tôi kiểm chứng — minh bạch, không cần tin suông

"Do chuyên gia viết" chỉ là một lời khẳng định; kho này cung cấp bằng chứng thay vì chỉ nói suông. Bốn lớp độc lập, ai cũng có thể tự chạy từ bản checkout này:

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

Kết quả chạy công khai gần nhất (2026-07-06, Haiku 4.5 trả lời, Sonnet 5 chấm điểm mù, cả hai harness):

- **Phản thực (Counterfactual):** skill thắng **13/15 kịch bản** (1 hòa, 1 thua) — 72% tiêu chí hành vi chuyên gia đạt được so với 37% của baseline tổng quát.
- **Đối sánh với con người (Parity):** câu trả lời của skill được ưa chuộng hơn câu trả lời được chấp nhận trên Stack Exchange của chính người hành nghề thật trong **5 trên 8** lượt so sánh trực tiếp, chấm điểm mù (mẫu còn nhỏ; bộ câu hỏi đang tiếp tục tăng — nên xem đây là tín hiệu ban đầu, chưa phải một nghiên cứu).

Mọi kết quả đều có thể tái tạo: `python3 evals/run_evals.py` và `python3 evals/parity/run_parity.py`. Khi một vai trò không vượt qua các bài kiểm tra này, điều đó cũng được công khai — mục đích là đo lường, không phải tiếp thị. Đánh giá của người hành nghề vẫn là ngôi sao vàng cao nhất (`metadata.maturity`), nhưng ngưỡng tin cậy tối thiểu là thứ được đo lường, không phải được bảo chứng suông.

## Danh sách vai trò hiện tại

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

Khối này được tạo tự động — hãy chạy `python3 scripts/generate_roadmap.py` sau khi thêm/xóa/ánh xạ lại một vai trò, đừng tự tay chỉnh sửa nó.

## Dùng với AI tool của bạn

`SKILL.md` là một định dạng dùng chung cho nhiều công cụ — cùng một file vai trò chạy được trên Claude Code, Codex CLI, Cursor, và hơn 30 agent khác. Chỉ khác nhau ở thư mục cài đặt.

### Không cần cấu hình: dán đoạn này vào agent của bạn

Sao chép đoạn dưới vào Claude Code, Codex, Cursor, hoặc bất kỳ agent nào có quyền truy cập shell, mô tả tác vụ của bạn ở cuối, và nó sẽ tự cài đặt đúng chuyên gia cần thiết:

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

**Người dùng Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, và Amp:** bỏ qua bước dán thủ công — `npx domain-experts command --tool <id>` sẽ cài `/domain-expert` một lần, sau đó chỉ cần chạy `/domain-expert <task>` mỗi khi cần (xem [lệnh slash `/domain-expert`](#lệnh-slash-domain-expert) bên dưới).

### Cài đặt theo từng công cụ

| Công cụ | Cách làm |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — được cài vào `./.claude/skills/<slug>/`, tự động được nhận diện như một skill. |
| **Codex CLI** | Cùng lệnh trên với `--to .codex/skills/<slug>` (theo dự án) hoặc `--to ~/.codex/skills/<slug>` (theo cá nhân). Phiên làm việc mới sẽ tự nhận. |
| **Cursor** | Cùng lệnh trên với `--to .cursor/skills/<slug>` — Cursor đọc trực tiếp cùng định dạng `SKILL.md`. |
| **Windsurf, Roo Code, Goose & các công cụ tương thích SKILL.md khác** | Cùng lệnh trên với `--to <thư mục skill của công cụ>/<slug>` — kiểm tra tài liệu công cụ của bạn để biết đường dẫn chính xác. |
| **Các công cụ đọc `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Cài ở bất kỳ đâu trong repo (ví dụ `--to skills/<slug>`), rồi thêm một dòng vào `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Bất kỳ chat AI nào (không có shell)** | Mở vai trò trên GitHub, dán `SKILL.md` vào system prompt hoặc custom instructions; dán các file trong `references/` khi cuộc hội thoại cần chiều sâu hơn. |

Mỗi lần cài đặt đều sao chép toàn bộ vai trò — cả `SKILL.md` lẫn `references/` — nên các playbook chuyên sâu luôn đi kèm.

### Tự động phân phối

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) là một meta-skill giúp loại bỏ luôn cả bước `match` — cài đặt bằng `npx domain-experts add domain-expert-router`, nạp một lần, và agent của bạn sẽ tự tìm đúng vai trò cho các yêu cầu kiểu "hãy đóng vai X", đồng thời thẳng thắn báo cho bạn biết khi một vai trò chưa được phủ sóng.

### Lệnh slash `/domain-expert`

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Khởi động lại phiên làm việc, sau đó dùng trực tiếp `/domain-expert <task>` — ví dụ `/domain-expert review this vendor contract`. Lệnh này chạy `match`, nạp `SKILL.md` của vai trò thắng cuộc (và `references/` nếu cần), rồi trả lời như chuyên gia đó, hoặc thẳng thắn báo cho bạn biết khi chưa có gì phù hợp. Cùng ý tưởng với router skill ở trên, nhưng đóng gói thành một lệnh chạy một lần thay vì một skill luôn được nạp sẵn.

| `--tool` | Cài vào | Ghi chú |
|---|---|---|
| `claude` (mặc định) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex chỉ đọc prompt từ thư mục cấp người dùng, không có tùy chọn theo dự án; tài liệu của OpenAI đánh dấu cơ chế này là đã lỗi thời, ưu tiên dùng "skills" thay thế, nhưng nó vẫn hoạt động |
| `gemini` | `.gemini/commands/domain-expert.toml` | Định dạng TOML |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf gọi đây là "workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | Vị trí của Amp cố định ở gốc repo, không có thư mục global riêng |

Thêm `--global` để cài vào thư mục cấp người dùng của công cụ (ví dụ `~/.claude/commands/`, `~/.cursor/commands/`) thay vì thư mục dự án, hoặc `--to <path>` để chỉ định vị trí tùy ý.

### Tham chiếu CLI

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` chấm điểm các vai trò dựa trên độ trùng lặp từ khóa và trả về một kết quả khớp đáng tin cậy, các ứng viên có độ tin cậy thấp, hoặc thẳng thắn báo "chưa được phủ sóng" — nó không âm thầm đoán mò. Dùng `--json` để tích hợp theo chương trình.

Gói npm chụp nhanh (snapshot) thư viện vai trò tại mỗi bản phát hành. Để dùng phiên bản mới nhất chưa phát hành, hãy dùng `npx --yes github:wonsukchoi/domain-experts <command>` — cùng một CLI, lấy trực tiếp từ `main`.

## Lộ trình

[`ROADMAP.md`](./ROADMAP.md) là backlog tổng thể — toàn bộ 1.016 ngành nghề theo O*NET, được nhóm theo danh mục, và được đánh dấu hoàn thành khi có bản nháp. Dùng nó để tìm một vai trò chưa được phủ sóng thay vì đoán xem còn thiếu gì.

## Đóng góp — kho này sinh lãi kép

Mỗi vai trò được thêm vào giúp router thông minh hơn, mỗi bản sửa lỗi đến được với mọi người dùng ở bản phát hành tiếp theo, và mỗi câu hỏi đánh giá khiến việc "làm giả" chuẩn chất lượng khó hơn. Một prompt bạn viết cho riêng mình sẽ chết theo phiên làm việc của bạn; một vai trò bạn đóng góp ở đây hoạt động cho tất cả mọi người, mãi mãi, và tiếp tục được cải thiện sau khi bạn rời đi. Đó là toàn bộ cược đặt ra: **1.016 ngành nghề không phải một dự án cá nhân — đó là một cộng đồng chung (commons).**

Các câu hỏi thường gặp (lỗi lint, xung đột khi push, quy trình phát hành) → [`docs/FAQ.md`](./docs/FAQ.md).

Ba cách để tham gia, ở bất kỳ trình độ nào:

1. **Bạn đang làm việc trong một vai trò mà chúng tôi đã có?** Hãy đọc nó. Bất cứ điều gì sai đều là một [issue chỉnh sửa của người hành nghề](../../issues/new/choose) chỉ mất 2 phút — đóng góp giá trị nhất mà dự án này có thể nhận được. Không cần kỹ năng làm PR.
2. **Bạn muốn viết mới hoặc nâng cấp một vai trò?** Hãy làm theo đúng công thức trong [`CONTRIBUTING.md`](./CONTRIBUTING.md) — được viết chính xác đến mức một LLM có thể thực thi được, để bạn và trợ lý AI của bạn có thể cùng nhau thực hiện. Lint sẽ báo cho bạn biết nếu cấu trúc chưa đạt chuẩn trước khi bất kỳ ai xem xét thủ công. 42 vai trò cũ hiện đang [chờ người nhận](../../issues/1).
3. **Bạn không viết được nhưng giỏi tìm kiếm?** Hãy thu thập các câu hỏi đối sánh (`evals/parity/harvest_stackexchange.py`) hoặc gửi một [yêu cầu vai trò](../../issues/new/choose) kèm theo các tác vụ bạn muốn giao cho nó.

Nếu spec xung đột với thực tế của một người hành nghề, spec sẽ thua — hãy nói rõ điều đó trong PR của bạn và chúng tôi sẽ sửa spec.

## Giấy phép

MIT — xem [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
