# harvest-6way-r1225 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1225 ctrl_bpc |
|--------|--------|--------------:|
| ecDn9 | fork-slaa-us-mmllm-claude-train-sym24-3b438609-ecDn9 | 2.2623 |
| KtA3X | fork-SeniorCareMarket-mmllm-claude-train-sym24-c59f2932-KtA3X | 2.2801 |
| ayBUu | origin/claude/train-sym24-bb739488-ayBUu | 2.2827 |
| AHYlI | fork-joly-os-mmllm-claude-train-sym24-c843bd3b-AHYlI | 2.4705 |
| JwQla | fork-slaa-us-mmllm-claude-train-sym24-680d179c-JwQla | 2.6580 |
| hdVUo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-564df4d6-hdVUo | 2.6621 |
| **mean** | | **2.4359** |
| **best** | | **2.2623** |

## Chain progression R1224 → R1225

Previous harvest: `workers/dispatcher/harvest-16way-r1224_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8325         | 2.4359         | -0.3966 |
| ctrl_bpc best  | 2.2554         | 2.2623         | +0.0069 |

## Per-round trajectory (best bird: ecDn9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1225 | 6400 | 2.2623 | +0.2560 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1224_sym24`
  - `workers/dispatcher/harvest-4way-r1224_sym24`

## Output

`workers/dispatcher/harvest-6way-r1225_sym24/round-1225/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

