# harvest-5way-r1195 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1195 ctrl_bpc |
|--------|--------|--------------:|
| KmHG8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0c4e6757-KmHG8 | 2.3101 |
| ohyXu | fork-joly-os-mmllm-claude-train-sym24-485fabeb-ohyXu | 2.4850 |
| CG5Eq | origin/claude/train-sym24-d6fda9c3-CG5Eq | 2.4963 |
| 0IRXW | fork-slaa-us-mmllm-claude-train-sym24-ecc2e52a-0IRXW | 2.6841 |
| PceKA | origin/claude/train-sym24-0d8534db-PceKA | 2.6899 |
| **mean** | | **2.5331** |
| **best** | | **2.3101** |

## Chain progression R1194 → R1195

Previous harvest: `workers/dispatcher/harvest-6way-r1194_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3659         | 2.5331         | +0.1672 |
| ctrl_bpc best  | 2.2894         | 2.3101         | +0.0207 |

## Per-round trajectory (best bird: KmHG8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1195 | 3731 | 2.3101 | +0.2419 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1194_sym24`

## Output

`workers/dispatcher/harvest-5way-r1195_sym24/round-1195/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

