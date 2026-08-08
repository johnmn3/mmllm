# harvest-4way-r1144 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1144 ctrl_bpc |
|--------|--------|--------------:|
| ryt4T | fork-slaa-us-mmllm-claude-train-sym24-a72f1168-ryt4T | 2.3660 |
| 4w13o | origin/claude/train-sym24-5365ec5f-4w13o | 2.5418 |
| WLiGc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-baf4f6a4-WLiGc | 2.5452 |
| 8n4KI | fork-SeniorCareMarket-mmllm-claude-train-sym24-efb4e9cb-8n4KI | 2.7340 |
| **mean** | | **2.5467** |
| **best** | | **2.3660** |

## Chain progression R1143 → R1144

Previous harvest: `workers/dispatcher/harvest-17way-r1143_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4402         | 2.5467         | +0.1065 |
| ctrl_bpc best  | 2.3368         | 2.3660         | +0.0292 |

## Per-round trajectory (best bird: ryt4T)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1144 | 6616 | 2.3660 | +0.2501 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1143_sym24`

## Output

`workers/dispatcher/harvest-4way-r1144_sym24/round-1144/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

