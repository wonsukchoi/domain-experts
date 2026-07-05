# Management-analyst artifacts — templates with real structure

Filled with the Meridian Fastener Corp engagement numbers ($480M-revenue manufacturer, 3 plants + HQ, $15M savings mandate). Figures in $000s unless noted.

## 1. MECE issue tree

Root question sized and scoped before any data pull: **"Where can Meridian find $15M in run-rate savings within 18 months, without touching shop-floor direct labor or R&D?"**

```
$15M savings target
├── 1. Organization design (layers & span)
│   ├── 1.1 Dept Head layer — coordination-only, span 2.8 → eliminate/absorb
│   └── 1.2 Manager layer — span 4.3 in standardized work → widen to 7-9
├── 2. Shared-services consolidation (transactional staff)
│   ├── 2.1 Finance/Accounting (AP, payroll processing, month-end close)
│   ├── 2.2 HR administration (onboarding, benefits admin, records)
│   ├── 2.3 Procurement transaction processing (PO issuance, invoice match)
│   └── 2.4 IT tier-1/2 helpdesk (excludes plant-embedded tier-1 for line-down escalations)
└── 3. Indirect (non-labor) spend
    ├── 3.1 MRO and maintenance contracts
    ├── 3.2 Travel & contract services
    └── 3.3 Software/license true-up across 3 disparate ERP instances
```

**Rule applied:** branches 1 and 2 both touch headcount but at different layers (management vs. transactional) — verified no double-counted FTE by cross-checking the org chart role list against both branches before pricing either one. Branch 3 is spend, not headcount, and is priced independently.

## 2. Span-and-layers workbook

| Layer | Roles (n) | Current avg span | Target span | Benchmark basis | FTE eliminated | Avg fully loaded cost | Savings |
|---|---|---|---|---|---|---|---|
| Dept Head (Finance/HR/Procurement/IT) | 14 | 2.8 | n/a (layer removed, 4 retained as transition leads) | Coordination-only layer, no direct output | 10 | $145K | $1,450K |
| Manager (transactional functions) | 68 | 4.3 | 8.0 | Standardized/homogeneous work benchmark (7-9) | 31 | $110K | $3,410K |
| SSC transactional staff | 338 | n/a (process consolidation, not span) | n/a | 22% reduction from eliminating triplicated month-end close, payroll, PO processing across 3 sites | 74 | $72K | $5,328K |
| **Subtotal — org design + SSC** | | | | | **115** | | **$10,188K** |

**Reading it like an analyst:** the Dept Head layer's low span (2.8) is the tell that it exists to coordinate Managers rather than manage distinct output — that's the delayering candidate. The Manager layer's span (4.3) is too narrow *given the work is standardized*; if the underlying work were heterogeneous (e.g., plant engineering leads), 4.3 would be defensible and the fix would be wrong.

## 3. SIPOC — AP invoice processing (one of the three consolidated processes)

| Supplier | Input | Process | Output | Customer |
|---|---|---|---|---|
| Vendor | Invoice (paper/email, 3 different formats by plant) | 1. Receive → 2. Match to PO (manual, 3 separate ERPs) → 3. Approve (plant Dept Head signoff) → 4. Post to GL → 5. Pay (weekly run, per-plant bank account) | Paid invoice, GL entry | Vendor, plant Finance, corporate consolidation |

**Standardization gap found:** step 2 (PO match) takes 22 minutes/invoice at the Texas plant (manual three-way match) vs. 6 minutes at Ohio (automated match in the newer ERP module already licensed but unused at Texas/Mexico). This single gap accounts for roughly a third of the AP-related FTE savings in the workbook above — turning on an existing license, not new headcount removal.

## 4. RACI — top recurring decisions in the target-state org

| Decision | Plant GM | SSC Director | Corporate Finance | Category Manager (Procurement) |
|---|---|---|---|---|
| Approve invoice >$50K | C | A | I | C |
| Set indirect-spend category strategy (e.g., MRO sourcing) | C | I | I | A/R |
| Hire/replace SSC transactional role | I | A/R | C | I |
| Plant-specific process exception (deviate from standard SSC workflow) | A/R | C | I | I |
| Month-end close sign-off | I | R | A | I |
| Vendor contract renewal >$500K | C | I | C | A/R |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed. Rule applied: every row has exactly one A — the most common defect in a first-draft RACI is two or zero accountable parties on the same decision, which is exactly what re-litigates the redesign six weeks after go-live.

## 5. Business case / savings bridge (steering committee page)

| Line | Run-rate savings | One-time cost | Notes |
|---|---|---|---|
| Dept Head delayering | $1,450K | included below | 10 of 14 roles eliminated |
| Manager span widening | $3,410K | included below | 68 → 37 roles |
| SSC transactional consolidation | $5,328K | included below | 338 → 264 roles, 22% reduction |
| Indirect procurement (top 5 categories, 9% of $28M) | $2,520K | $600K | category management, contract rebid |
| **Total run-rate** | **$12,708K** | | vs. $15,000K mandate — **$2,292K gap**, explained below |
| Severance (115 FTE avg $22K) | | $2,530K | |
| SSC standup (ERP/process redesign, change mgmt) | | $3,200K | |
| **Total one-time cost** | | **$6,330K** | |
| **Payback** | | | $6,330K ÷ $12,708K ≈ 0.50 years (~6 months) |
| **Year-1 realized (60% of run-rate, ramp/notice periods)** | $7,625K | | Full run-rate by month 18 |

**Gap explanation carried on the same page, not buried in an appendix:** closing the remaining $2,292K requires either (a) consolidating the plant-embedded Quality function into the SSC — breaches the CEO's own safety-critical exclusion — or (b) widening support-role spans in IT/HR past 12 direct reports, at which point plant line-down escalations start queueing. Recommendation: do neither; take the $12.7M program and reopen scope explicitly if the board wants the last $2.3M.

## 6. Zero-based staffing worksheet (Procurement, illustrative)

| Category | Current FTE | Spend managed | Zero-based question answer | Target FTE |
|---|---|---|---|---|
| Strategic sourcing (top 5 categories, $28M) | 3 (1 per plant, uncoordinated) | $28M | One category manager per category, not per plant — 5 categories | 5* |
| Transactional PO processing | 15 (5/plant) | n/a (process, not spend) | Standardizable via SSC | 7 |
| Tail-spend/ad hoc buying | 7 (split across plants) | $14M | Consolidate into 2 buyers with a p-card program for <$5K purchases | 2 |

\* Category manager headcount rises from 3 to 5 (specialization), while transactional and tail-spend headcount falls — net procurement FTE moves from 25 to 14, matching the SSC branch total in the span-and-layers workbook (Procurement's share of the 74 FTE reduction).
