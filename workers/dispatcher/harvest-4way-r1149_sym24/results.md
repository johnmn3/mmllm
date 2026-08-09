# harvest-4way-r1149 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1149 ctrl_bpc |
|--------|--------|--------------:|
| F80nj | origin/claude/train-sym24-9d521da7-F80nj | 2.3364 |
| J6fwG | fork-SeniorCareMarket-mmllm-claude-train-sym24-cfb29c05-J6fwG | 2.3617 |
| w2t6F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7578b505-w2t6F | 2.7334 |
| shL2Q | fork-joly-os-mmllm-claude-train-sym24-4066b64e-shL2Q | 2.7336 |
| **mean** | | **2.5413** |
| **best** | | **2.3364** |

## Chain progression R1148 → R1149

Previous harvest: `workers/dispatcher/harvest-6way-r1148_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4845         | 2.5413         | +0.0568 |
| ctrl_bpc best  | 2.3408         | 2.3364         | -0.0044 |

## Per-round trajectory (best bird: F80nj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1149 | 7082 | 2.3364 | +0.2641 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1148_sym24`
  - `workers/dispatcher/harvest-5way-r1148_sym24`

## Output

`workers/dispatcher/harvest-4way-r1149_sym24/round-1149/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

