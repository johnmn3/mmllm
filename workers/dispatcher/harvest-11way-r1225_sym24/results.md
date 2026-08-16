# harvest-11way-r1225 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1225 ctrl_bpc |
|--------|--------|--------------:|
| 1JctP | origin/claude/train-sym24-7d57d46b-1JctP | 2.2601 |
| LwO8u | fork-slaa-us-mmllm-claude-train-sym24-ea4a15a4-LwO8u | 2.2605 |
| ecDn9 | fork-slaa-us-mmllm-claude-train-sym24-3b438609-ecDn9 | 2.2623 |
| KtA3X | fork-SeniorCareMarket-mmllm-claude-train-sym24-c59f2932-KtA3X | 2.2801 |
| ayBUu | origin/claude/train-sym24-bb739488-ayBUu | 2.2827 |
| TZBKc | fork-SeniorCareMarket-mmllm-claude-train-sym24-3937c4c4-TZBKc | 2.4560 |
| 4C6Gh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-85f3a5fd-4C6Gh | 2.4606 |
| AHYlI | fork-joly-os-mmllm-claude-train-sym24-c843bd3b-AHYlI | 2.4705 |
| JwQla | fork-slaa-us-mmllm-claude-train-sym24-680d179c-JwQla | 2.6580 |
| hdVUo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-564df4d6-hdVUo | 2.6621 |
| sMfkp | fork-joly-os-mmllm-claude-train-sym24-5ba262d7-sMfkp | 2.6653 |
| **mean** | | **2.4289** |
| **best** | | **2.2601** |

## Chain progression R1224 → R1225

Previous harvest: `workers/dispatcher/harvest-16way-r1224_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8325         | 2.4289         | -0.4036 |
| ctrl_bpc best  | 2.2554         | 2.2601         | +0.0047 |

## Per-round trajectory (best bird: 1JctP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1225 | 6355 | 2.2601 | +0.2619 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1224_sym24`
  - `workers/dispatcher/harvest-4way-r1224_sym24`

## Output

`workers/dispatcher/harvest-11way-r1225_sym24/round-1225/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

