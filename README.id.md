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

Perpustakaan **definisi peran pekerjaan (job role definitions)** open source — model mental, ambang batas keputusan, dan pola kegagalan praktisi sungguhan, disusun agar AI agent apa pun bisa memuatnya dan bernalar layaknya sang ahli tersebut. Minta agent Anda "tinjau kontrak ini" dan ia akan menjawab dengan playbook klausul dan tangga fallback seorang pengacara kontrak senior, bukan rangkuman internet ala generalis.

**Langsung ke:** [Mulai cepat](#mulai-cepat) · ["Kenapa tidak tinggal prompt saja?"](#tidak-bisakah-saya-tinggal-bilang-ke-claude-untuk-berperan-sebagai-cfo) · [Visi](#visi--satu-orang-semua-ahli) · [Bagaimana peran dibangun](#bagaimana-peran-dibangun) · [Bagaimana kami memverifikasi](#bagaimana-kami-memverifikasi--transparan-tanpa-perlu-percaya-begitu-saja) · [Peran saat ini](#peran-saat-ini) · [Gunakan dengan tool Anda](#gunakan-dengan-ai-tool-anda) · [Roadmap](#roadmap) · [Berkontribusi](#berkontribusi--repo-ini-tumbuh-berlipat)

## Mulai cepat

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

Tidak perlu instalasi — `npx` mengambilnya langsung dari npm. Sering dipakai? Jalankan `npm install -g domain-experts` lalu hilangkan `npx`.

**Menggunakan Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, atau Amp?** `npx domain-experts command --tool <id>` memasang slash command `/domain-expert` untuknya — mulai ulang sesi Anda lalu jalankan `/domain-expert review this vendor contract`. Perintah ini mencocokkan, memuat, dan bernalar sebagai peran yang tepat dalam satu langkah, tanpa perlu proses manual `match`/`add`.

> **Jika Anda meng-`git clone` repo ini alih-alih pakai CLI:** jangan arahkan penemuan skill alat Anda langsung ke direktori `roles/`. Direktori ini berisi lebih dari 200 file `SKILL.md` individual, dan sebagian besar alat (termasuk Claude Code) memuat nama dan deskripsi setiap skill yang ditemukan ke system prompt dasar — Anda akan membayar biaya token itu di setiap sesi untuk peran-peran yang tidak pernah Anda pakai. Instal hanya [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) (atau gunakan perintah `add`/`init` dari CLI, yang melakukan hal sama) — ini satu skill ringan yang membaca `roles/<slug>/SKILL.md` tertentu sesuai kebutuhan, hanya saat tugas benar-benar memerlukannya.

Atau lewati langkah manual sepenuhnya: muat [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) sekali saja, dan agent Anda akan mendeteksi sendiri ahli mana yang dibutuhkan suatu tugas, menarik konteks penuh peran tersebut secara otomatis, dan memberi tahu Anda dengan jujur saat suatu peran belum tercakup alih-alih mengarang jawaban. Anda tetap bekerja seperti biasa; keahlian yang tepat muncul dengan sendirinya.

## "Tidak bisakah saya tinggal bilang ke Claude untuk berperan sebagai CFO?"

Bisa saja — tapi Anda hanya akan mendapat tiruan dangkal: rata-rata dari semua deskripsi pekerjaan di internet, dibuat ulang dari nol setiap sesi, berbeda setiap kali, dan tidak diverifikasi oleh siapa pun.

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

Perbedaannya, secara konkret:

- **Konten yang tidak bisa diturunkan (non-derivable).** Setiap peran wajib lolos uji non-derivability: tidak ada yang bisa dibuat ulang hanya dari nama jabatannya. Yang tersisa adalah hal-hal yang tidak bisa dihasilkan prompting begitu saja — ambang batas numerik red-flag, rentang negosiasi standar pasar, contoh kerja dengan hitungan yang benar-benar cocok, posisi fallback yang berurutan sesuai prioritas.
- **Gerbang kualitas, bukan sekali generate.** Peran dibangun lewat pipeline multi-tahap ([`AUTHORING.md`](./AUTHORING.md)) — lihat diagram di bawah. Prompt satu baris tidak melalui proses itu sama sekali.
- **Struktur yang ditegakkan CI.** Setiap PR menjalankan [`scripts/lint_roles.py`](./scripts/lint_roles.py): skema, bagian wajib, tautan yang valid, frasa pengisi (filler) yang dilarang, kelengkapan red-flag, angka nyata dalam contoh kerja. Teks deskripsi pekerjaan yang generik akan gagal build.
- **Ia tumbuh berlipat (compounds).** Prompt ad-hoc Anda hilang begitu sesi berakhir. File-file ini mengakumulasi koreksi dari praktisi, memiliki tangga kematangan (`draft` → `reviewed-by-practitioner` → `mature`) dan spesifikasi berversi (`spec: 2` menandai peran yang sudah memenuhi standar terkini), dan menjadi lebih baik di setiap PR. Perbaikan menjangkau semua orang.
- **Dirancang hemat token.** Setiap peran adalah inti penalaran yang ringkas (`SKILL.md`) plus kedalaman sesuai kebutuhan (`references/`). Agent hanya "membayar" kedalaman itu saat tugasnya memang memerlukan:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

### Jadi apa sebenarnya moat-nya?

Sanggahan yang wajar: tidak ada satu pun dari poin di atas yang mencegah orang lain melakukan `git clone` pada repo ini persis dan merilisnya sebagai produk mereka sendiri — lisensi MIT, tanpa penguncian konten sama sekali. Jawaban jujurnya: kumpulan file bukanlah moat-nya. Yang sulit ditiru adalah mesin yang terus memproduksi dan mengoreksinya:

- **Pipeline-nya, bukan hasilnya.** Menyalin 97 file cukup satu perintah. Menyalin loop penulisan berlapis kritik-adversarial → rubrik 9-kriteria → gerbang lint ([`AUTHORING.md`](./AUTHORING.md)) yang terus memproduksi dan mengoreksinya — itu tidak bisa disalin begitu saja: sebuah fork mewarisi snapshot hari ini, bukan perbaikan hari esok.
- **Sebuah standar, bukan database.** `SKILL.md` sudah berjalan di 30+ tool agent. Menjadi perpustakaan terbesar dalam format terbuka yang portabel adalah posisi distribusi, bukan posisi konten — nilainya ada pada menjadi jawaban default yang orang temukan, bukan pada byte-byte itu sendiri.
- **Terverifikasi, bukan sekadar klaim.** Setiap kompetitor bisa bilang "ditulis oleh para ahli." Hanya sedikit yang bisa menjalankan `python3 evals/run_evals.py` di depan Anda dan menunjukkan kemenangan 13/15 dalam uji kontrafaktual. Kepercayaan di sini terukur dan bisa direproduksi, bukan sekadar diklaim.
- **Kesegaran mengalahkan ingatan parametrik.** Bahkan jika suatu model masa depan dilatih dengan teks publik repo ini, pengetahuan itu membeku pada titik cutoff pelatihannya. Koreksi di repo ini dirilis pada hari yang sama saat praktisi mengajukannya — tanpa siklus retrain, berversi, dan bisa dilacak ke sumbernya.
- **Disiplin cakupan.** Backbone 1.016 occupation dari O*NET memaksa cakupan long-tail yang sistematis (funeral-home-manager, wind-energy-operations-manager) yang tidak akan repot-repot dikejar kompetitor oportunis yang cuma mengkurasi peran-peran yang sedang tren.
- **Gratis dan portabel mengalahkan yang terkunci langganan.** Ini tidak bersaing dengan tagihan LLM Anda — Anda tetap membayar biaya inferensi apa pun yang terjadi. Ini bersaing dengan SaaS vertikal tertutup ("AI Legal Advisor", $99/bulan): mereka tidak bisa menandingi gratis, bisa di-fork, dan bisa dijalankan di model lokal tanpa biaya berulang.

Semua ini belum menjadi moat pada 97 peran dan basis kontributor yang masih kecil — ini adalah sebuah lintasan (trajectory). Taruhannya: commons ini akan tumbuh berlipat lebih cepat daripada fork mana pun bisa mengejar, begitu cukup banyak praktisi mulai mengajukan koreksi alih-alih menulis prompt dari nol setiap sesi.

## Visi — satu orang, semua ahli

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

Saat ini, untuk melakukan sesuatu dengan baik di luar bidang keahlian Anda sendiri berarti harus merekrut, mengontrak, atau melakukan outreach — mencari pengacara, menunggu jadwal seorang CFO, membayar tarif seorang strategis pemasaran. Friksi itu adalah pajak bagi setiap founder solo, setiap tim kecil, setiap individu yang menghadapi masalah di luar keahliannya. Kebanyakan orang akhirnya tidak melakukan hal itu sama sekali, atau melakukannya dengan buruk.

Seseorang dengan langganan AI — atau bahkan model lokal, tanpa langganan sama sekali — ditambah repo ini tidak perlu membayar pajak tersebut. Muat penalaran nyata seorang CFO untuk keputusan runway. Muat playbook klausul pengacara kontrak untuk sebuah redline. Muat penilaian seorang koordinator riset klinis untuk deviasi protokol. Ganti peran per tugas, sesuai kebutuhan, dengan biaya inferensi, bukan biaya merekrut. Satu orang, satu agent, akumulasi pengambilan keputusan dari ratusan profesi.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

Itulah endgame sesungguhnya di sini, bukan sekadar keingintahuan: batas antara "saya butuh seorang ahli" dan "saya punya seorang ahli" runtuh. Ini makin nyata seiring cakupan bertambah — 92 peran dari 1.016 occupation yang dilacak saat ini; roadmap ada agar celah itu menutup, bukan agar tetap menarik selamanya.

Ini tidak menggantikan penilaian, akuntabilitas, atau lisensi di mana hal-hal itu secara hukum harus tetap berada di tangan manusia — setiap peran yang teregulasi (hukum, kedokteran, keuangan) menyatakannya secara eksplisit. Yang digantikan adalah friksi karena tidak memiliki akses ke penalaran itu sejak awal.

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

## Bagaimana peran dibangun

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Setiap peran mengikuti kontrak yang sama, yang ditegakkan oleh spesifikasi dan CI:

1. **Tiga uji kelayakan rilis** — seorang praktisi yang membacanya mengangguk, bukan mengangkat bahu; sebuah agent dengan peran ini membuat keputusan yang secara terukur berbeda dibanding tanpa peran itu; tidak ada satu pun isinya yang bisa diturunkan hanya dari nama jabatannya.
2. **Anatomi tetap** — identitas, inti berbasis prinsip pertama (first-principles), heuristik kondisional ("kalau X, defaultnya Y kecuali Z"), kerangka keputusan yang bisa langsung dieksekusi, pola kegagalan umum, dan sebuah contoh kerja dengan angka nyata yang benar-benar cocok, berakhir pada deliverable sungguhan (memo, redline, laporan hasil).
3. **Trio referensi** — file playbook/artifact mendalam berisi template yang sudah terisi, `red-flags.md` (sinyal → artinya → pertanyaan pertama → data yang perlu diambil), dan `vocabulary.md` (istilah teknis lengkap dengan kesalahan pemakaian yang umum).
4. **Provenans (asal-usul)** — sumber disebutkan secara eksplisit; angka spesifik dapat dilacak ke sumbernya atau diberi label sebagai heuristik yang dinyatakan. Peran yang teregulasi (hukum, kedokteran, keuangan) menyertakan disklaimer eksplisit.
5. **Backbone O*NET** — cakupan mengikuti taksonomi occupation Departemen Tenaga Kerja AS (1.016 occupation), sehingga pertumbuhannya sistematis, bukan sekadar apa yang terlihat menarik minggu itu.

Spesifikasi lengkap, rubrik, dan pipeline penulisan draf berbasis LLM: [`AUTHORING.md`](./AUTHORING.md). Dalam checkout Claude Code, seluruh pipeline ini berjalan sebagai `/generate-role "<need>"` — lihat [Otomatisasi maintainer](#maintainer-automation-claude-code) di bawah.

## Bagaimana kami memverifikasi — transparan, tanpa perlu percaya begitu saja

"Ditulis oleh para ahli" hanyalah sebuah klaim; repo ini justru menyajikan buktinya. Empat lapisan independen, semuanya bisa dijalankan siapa pun dari checkout ini:

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

Hasil terbaru yang dipublikasikan (2026-07-06, Haiku 4.5 menjawab, Sonnet 5 menilai secara blind, kedua harness):

- **Kontrafaktual:** skill menang **13/15 skenario** (1 seri, 1 kalah) — 72% dari kriteria perilaku ahli yang teramati tercapai, dibanding 37% pada baseline generalis.
- **Parity vs manusia:** jawaban skill lebih disukai dibanding jawaban praktisi sungguhan yang diterima di Stack Exchange pada **5 dari 8** perbandingan head-to-head secara blind (sampel masih kecil; kumpulan pertanyaan terus bertambah — anggap ini sebagai sinyal awal, bukan sebuah studi).

Setiap hasil dapat direproduksi: `python3 evals/run_evals.py` dan `python3 evals/parity/run_parity.py`. Ketika sebuah peran gagal dalam pengujian ini, itu juga dipublikasikan — intinya adalah pengukuran, bukan pemasaran. Tinjauan praktisi tetap menjadi bintang emas di puncaknya (`metadata.maturity`), tapi ambang kepercayaan dasarnya terukur, bukan sekadar dijamin begitu saja.

## Peran saat ini

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

Blok ini dibuat secara otomatis — jalankan `python3 scripts/generate_roadmap.py` setelah menambah/menghapus/memetakan ulang sebuah peran, jangan mengeditnya secara manual.

## Gunakan dengan AI tool Anda

`SKILL.md` adalah format lintas tool — file peran yang sama berfungsi di Claude Code, Codex CLI, Cursor, dan 30+ agent lainnya. Yang berbeda hanyalah direktori instalasinya.

### Tanpa setup: tempelkan ini ke agent Anda

Salin teks ini ke Claude Code, Codex, Cursor, atau agent mana pun yang punya akses shell, jelaskan tugas Anda di bagian bawah, dan ia akan memasang ahli yang tepat dengan sendirinya:

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

**Pengguna Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, dan Amp:** lewati langkah tempel — `npx domain-experts command --tool <id>` memasang `/domain-expert` sekali saja, lalu tinggal jalankan `/domain-expert <task>` setiap kali (lihat [slash command `/domain-expert`](#slash-command-domain-expert) di bawah).

### Instalasi per tool

| Tool | Cara |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — masuk ke `./.claude/skills/<slug>/`, otomatis dikenali sebagai skill. |
| **Codex CLI** | Perintah yang sama dengan `--to .codex/skills/<slug>` (proyek) atau `--to ~/.codex/skills/<slug>` (personal). Dikenali otomatis di sesi baru. |
| **Cursor** | Perintah yang sama dengan `--to .cursor/skills/<slug>` — Cursor membaca format `SKILL.md` yang sama secara native. |
| **Windsurf, Roo Code, Goose & tool lain yang kompatibel dengan SKILL.md** | Perintah yang sama dengan `--to <direktori skill tool Anda>/<slug>` — cek dokumentasi tool Anda untuk mengetahui path-nya. |
| **Tool yang membaca `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Pasang di mana saja dalam repo (misalnya `--to skills/<slug>`), lalu tambahkan satu baris ke `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **AI chat mana pun (tanpa shell)** | Buka peran di GitHub, tempelkan `SKILL.md` ke system prompt atau custom instructions; tempelkan juga file `references/` saat percakapan membutuhkan kedalaman tersebut. |

Setiap instalasi menyalin peran secara utuh — `SKILL.md` beserta `references/` — sehingga playbook mendalamnya ikut terbawa.

### Dispatch otomatis

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) adalah meta-skill yang menghilangkan bahkan langkah `match` — pasang dengan `npx domain-experts add domain-expert-router`, muat sekali saja, dan agent Anda akan menemukan peran yang tepat untuk permintaan "berperan sebagai X" dengan sendirinya, dan memberi tahu Anda dengan jujur saat suatu peran belum tercakup.

### Slash command `/domain-expert`

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Mulai ulang sesi Anda, lalu langsung gunakan `/domain-expert <task>` — misalnya `/domain-expert review this vendor contract`. Perintah ini menjalankan `match`, memuat `SKILL.md` dari peran yang menang (beserta `references/` sesuai kebutuhan), dan menjawab sebagai ahli tersebut, atau memberi tahu Anda dengan jujur saat belum ada yang cocok. Idenya sama dengan router skill di atas, hanya dikemas sebagai perintah sekali pakai alih-alih skill yang selalu dimuat.

| `--tool` | Terpasang ke | Catatan |
|---|---|---|
| `claude` (default) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex hanya membaca prompt dari direktori level user, tidak ada opsi project-local; dokumentasi OpenAI menandai mekanisme ini sudah deprecated demi "skills," tapi masih berfungsi |
| `gemini` | `.gemini/commands/domain-expert.toml` | Format TOML |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf menyebutnya sebagai "workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | Lokasi Amp tetap di root repo, tidak ada direktori global terpisah |

Tambahkan `--global` untuk memasang ke direktori level user milik tool tersebut (misalnya `~/.claude/commands/`, `~/.cursor/commands/`) alih-alih direktori proyek, atau `--to <path>` untuk lokasi kustom sepenuhnya.

### Referensi CLI

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` memberi skor pada peran berdasarkan kecocokan kata kunci dan melaporkan hasil yang cocok dengan yakin, kandidat dengan keyakinan rendah, atau pengakuan jujur "belum tercakup" — tanpa menebak diam-diam. Gunakan `--json` untuk pemakaian terprogram.

Paket npm menyimpan snapshot perpustakaan peran pada setiap rilis. Untuk versi terkini yang belum dirilis, gunakan `npx --yes github:wonsukchoi/domain-experts <command>` — CLI yang sama, langsung dari `main`.

### Otomatisasi maintainer (Claude Code)

Bekerja di checkout Claude Code dari repo ini menambahkan tiga slash command yang mengotomatisasi pipeline di atas, bukan menggantikannya — masing-masing tetap digerbangi PR manusia, tidak ada yang commit ke `main` atau publish dengan sendirinya:

- `/generate-role "<need>"` — mencocokkan kebutuhan berupa teks bebas ke peran yang sudah ada, leaf spesialisasi baru, atau peran induk baru, lalu menjalankan pipeline Pass 0-4 dari AUTHORING.md (riset → draf → kritik adversarial → skor, dibatasi maksimal 2 loop revisi) dan membuka PR.
- `/audit-roles [batchSize]` — penilaian ulang berkelompok atas peran yang sudah rilis terhadap rubrik dan kesegaran sumber; menandai `last_audited`/`audit_score`, memberi flag `status: needs-refresh`, dan men-deprecate (memindahkan ke `roles/_deprecated/`) setelah kegagalan kedua berturut-turut.
- `/scan-project <path>` — pemindaian read-only atas proyek eksternal (stack, README, struktur, commit terbaru), mengusulkan kandidat kebutuhan yang sudah dicek silang dengan cakupan yang ada, dan menyerahkan yang Anda pilih ke `/generate-role`. Tidak ada apa pun tentang proyek yang dipindai yang ditulis ke mana pun.

Query `match` yang tidak yakin dicatat ke `data/gap-log.jsonl` dan ditampilkan, diurutkan berdasarkan frekuensi, di bagian "Requested but missing" pada [`ROADMAP.md`](./ROADMAP.md) — sinyal konkret soal apa yang perlu ditulis berikutnya.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) adalah backlog utama — seluruh 1.016 occupation O*NET, dikelompokkan per kategori, dicentang seiring dibuatnya draf. Gunakan ini untuk menemukan peran yang belum tercakup alih-alih menebak apa yang hilang.

## Berkontribusi — repo ini tumbuh berlipat

Setiap peran yang ditambahkan membuat router semakin pintar, setiap koreksi menjangkau semua pengguna di rilis berikutnya, dan setiap pertanyaan evaluasi membuat standar kualitas makin sulit dipalsukan. Prompt yang Anda tulis untuk diri sendiri mati bersama sesi Anda; peran yang Anda kontribusikan di sini bekerja untuk semua orang, selamanya, dan terus membaik setelah Anda pergi. Itulah taruhan utamanya: **1.016 occupation bukan proyek solo — ini adalah commons.**

Pertanyaan umum (kegagalan lint, konflik push, proses rilis) → [`docs/FAQ.md`](./docs/FAQ.md).

Tiga cara berkontribusi, apa pun level keahlian Anda:

1. **Anda bekerja di peran yang kami cakup?** Bacalah. Apa pun yang salah bisa menjadi [issue koreksi praktisi](../../issues/new/choose) yang hanya butuh 2 menit — kontribusi paling berharga yang bisa diterima proyek ini. Tidak perlu keahlian membuat PR.
2. **Ingin menulis atau meng-upgrade sebuah peran?** Ikuti resep tepat di [`CONTRIBUTING.md`](./CONTRIBUTING.md) — ditulis dengan begitu presisi sehingga LLM pun bisa mengeksekusinya, jadi Anda dan asisten AI Anda bisa mengerjakannya bersama. Lint akan memberi tahu Anda jika strukturnya belum memenuhi standar sebelum ditinjau manusia. 42 peran lawas [siap diklaim sekarang juga](../../issues/1).
3. **Tidak bisa menulis tapi jago mencari?** Kumpulkan pertanyaan parity (`evals/parity/harvest_stackexchange.py`) atau ajukan [permintaan peran](../../issues/new/choose) berisi tugas-tugas yang ingin Anda delegasikan ke peran tersebut.

Jika spesifikasi bertentangan dengan realita seorang praktisi, spesifikasilah yang kalah — sampaikan itu di PR Anda dan kami akan memperbaiki spesifikasinya.

## Lisensi

MIT — lihat [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
