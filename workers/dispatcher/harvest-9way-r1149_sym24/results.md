# harvest-9way-r1149 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1149 ctrl_bpc |
|--------|--------|--------------:|
| F80nj | origin/claude/train-sym24-9d521da7-F80nj | 2.3364 |
| MeHqz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-10dd3217-MeHqz | 2.3364 |
| kdxYE | fork-slaa-us-mmllm-claude-train-sym24-99294d64-kdxYE | 2.3365 |
| f9xJw | fork-joly-os-mmllm-claude-train-sym24-132335ec-f9xJw | 2.3589 |
| 4Qmwb | origin/claude/train-sym24-7e8c8a85-4Qmwb | 2.3603 |
| J6fwG | fork-SeniorCareMarket-mmllm-claude-train-sym24-cfb29c05-J6fwG | 2.3617 |
| 3Skra | origin/claude/train-sym24-5211ba4c-3Skra | 2.5299 |
| w2t6F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7578b505-w2t6F | 2.7334 |
| shL2Q | fork-joly-os-mmllm-claude-train-sym24-4066b64e-shL2Q | 2.7336 |
| **mean** | | **2.4541** |
| **best** | | **2.3364** |

## Chain progression R1148 → R1149

Previous harvest: `workers/dispatcher/harvest-6way-r1148_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4845         | 2.4541         | -0.0304 |
| ctrl_bpc best  | 2.3408         | 2.3364         | -0.0044 |

## Per-round trajectory (best bird: F80nj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1149 | 7082 | 2.3364 | +0.2641 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1148_sym24`
  - `workers/dispatcher/harvest-5way-r1148_sym24`
  - `workers/dispatcher/harvest-6way-r1148_sym24`

## Output

`workers/dispatcher/harvest-9way-r1149_sym24/round-1149/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

