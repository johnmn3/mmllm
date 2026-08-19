# harvest-6way-r1253 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1253 ctrl_bpc |
|--------|--------|--------------:|
| MPPjS | fork-slaa-us-mmllm-claude-train-sym24-a574a27a-MPPjS | 2.2520 |
| LmDJH | fork-joly-os-mmllm-claude-train-sym24-217a426b-LmDJH | 2.2592 |
| ibhbL | fork-SeniorCareMarket-mmllm-claude-train-sym24-deb9d681-ibhbL | 2.4381 |
| SEswr | fork-joly-os-mmllm-claude-train-sym24-d5457a07-SEswr | 2.4385 |
| PdzAV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8be62f3f-PdzAV | 2.4388 |
| If4Tg | origin/claude/train-sym24-ac9b896e-If4Tg | 2.6406 |
| **mean** | | **2.4112** |
| **best** | | **2.2520** |

## Chain progression R1252 → R1253

Previous harvest: `workers/dispatcher/harvest-5way-r1252_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3627         | 2.4112         | +0.0485 |
| ctrl_bpc best  | 2.2402         | 2.2520         | +0.0118 |

## Per-round trajectory (best bird: MPPjS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1253 | 6556 | 2.2520 | +0.2335 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1252_sym24`

## Output

`workers/dispatcher/harvest-6way-r1253_sym24/round-1253/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

