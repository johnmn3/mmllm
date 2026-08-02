# harvest-7way-r1096 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1096 ctrl_bpc |
|--------|--------|--------------:|
| iBR0C | fork-joly-os-mmllm-claude-train-sym24-b974aea9-iBR0C | 2.3998 |
| IHhRU | fork-SeniorCareMarket-mmllm-claude-train-sym24-576136bf-IHhRU | 2.4201 |
| icBHd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-57de3591-icBHd | 2.4208 |
| 29Nmi | fork-slaa-us-mmllm-claude-train-sym24-6b1ce837-29Nmi | 2.5960 |
| v37mt | fork-slaa-us-mmllm-claude-train-sym24-2d860dcf-v37mt | 2.6043 |
| YIOAY | fork-joly-os-mmllm-claude-train-sym24-e7421406-YIOAY | 2.6113 |
| 6oZs5 | origin/claude/train-sym24-dc06721c-6oZs5 | 2.7965 |
| **mean** | | **2.5498** |
| **best** | | **2.3998** |

## Chain progression R1095 → R1096

Previous harvest: `workers/dispatcher/harvest-7way-r1095_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5830         | 2.5498         | -0.0332 |
| ctrl_bpc best  | 2.4129         | 2.3998         | -0.0131 |

## Per-round trajectory (best bird: iBR0C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1096 | 6562 | 2.3998 | +0.2282 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1095_sym24`
  - `workers/dispatcher/harvest-7way-r1095_sym24`

## Output

`workers/dispatcher/harvest-7way-r1096_sym24/round-1096/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

