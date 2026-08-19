# harvest-4way-r1253 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1253 ctrl_bpc |
|--------|--------|--------------:|
| MPPjS | fork-slaa-us-mmllm-claude-train-sym24-a574a27a-MPPjS | 2.2520 |
| ibhbL | fork-SeniorCareMarket-mmllm-claude-train-sym24-deb9d681-ibhbL | 2.4381 |
| SEswr | fork-joly-os-mmllm-claude-train-sym24-d5457a07-SEswr | 2.4385 |
| PdzAV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8be62f3f-PdzAV | 2.4388 |
| **mean** | | **2.3918** |
| **best** | | **2.2520** |

## Chain progression R1252 → R1253

Previous harvest: `workers/dispatcher/harvest-5way-r1252_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3627         | 2.3918         | +0.0292 |
| ctrl_bpc best  | 2.2402         | 2.2520         | +0.0118 |

## Per-round trajectory (best bird: MPPjS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1253 | 6556 | 2.2520 | +0.2335 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1252_sym24`

## Output

`workers/dispatcher/harvest-4way-r1253_sym24/round-1253/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

