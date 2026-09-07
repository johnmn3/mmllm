# harvest-4way-r1406 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1406 ctrl_bpc |
|--------|--------|--------------:|
| Y8dPv | fork-SeniorCareMarket-mmllm-claude-train-sym24-c398d613-Y8dPv | 3.2151 |
| lnGms | fork-joly-os-mmllm-claude-train-sym24-e7cce310-lnGms | 3.2287 |
| HjpbQ | origin/claude/train-sym24-b8696dc2-HjpbQ | 3.2479 |
| aCGkl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-63ab80e7-aCGkl | 3.6412 |
| **mean** | | **3.3332** |
| **best** | | **3.2151** |

## Chain progression R1405 → R1406

Previous harvest: `workers/dispatcher/harvest-3way-r1405_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4540         | 3.3332         | -0.1208 |
| ctrl_bpc best  | 3.3002         | 3.2151         | -0.0851 |

## Per-round trajectory (best bird: Y8dPv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1406 | 6395 | 3.2151 | +0.1200 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1405_sym24`

## Output

`workers/dispatcher/harvest-4way-r1406_sym24/round-1406/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

