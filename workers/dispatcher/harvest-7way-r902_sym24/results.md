# harvest-7way-r902 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R902 ctrl_bpc |
|--------|--------|--------------:|
| UNjhg | origin/claude/train-sym24-39e0fcaa-UNjhg | 2.7724 |
| I1rqa | fork-slaa-us-mmllm-claude-train-sym24-1cf09e19-I1rqa | 2.7815 |
| rRHkZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-2cd287cb-rRHkZ | 2.7816 |
| xF8ZQ | origin/claude/train-sym24-6779611a-xF8ZQ | 2.7837 |
| MxnQY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1572c574-MxnQY | 2.7854 |
| qELdY | origin/claude/train-sym24-af63ac83-qELdY | 2.7911 |
| OwNJa | fork-joly-os-mmllm-claude-train-sym24-ee140147-OwNJa | 2.9611 |
| **mean** | | **2.8081** |
| **best** | | **2.7724** |

## Chain progression R901 → R902

Previous harvest: `workers/dispatcher/harvest-4way-r901_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8413         | 2.8081         | -0.0332 |
| ctrl_bpc best  | 2.7967         | 2.7724         | -0.0243 |

## Per-round trajectory (best bird: UNjhg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 902 | 6568 | 2.7724 | +0.3197 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r901_sym24`
  - `workers/dispatcher/harvest-2way-r901_sym24`

## Output

`workers/dispatcher/harvest-7way-r902_sym24/round-902/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

