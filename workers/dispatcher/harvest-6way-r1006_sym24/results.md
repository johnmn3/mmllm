# harvest-6way-r1006 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1006 ctrl_bpc |
|--------|--------|--------------:|
| ev2Xo | origin/claude/train-sym24-5bc4a64a-ev2Xo | 2.5450 |
| d5Q29 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7771f4e9-d5Q29 | 2.5614 |
| ugwfn | fork-joly-os-mmllm-claude-train-sym24-ce9ad9ac-ugwfn | 2.5637 |
| Q3vQX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b2dfb8a-Q3vQX | 2.7571 |
| 1wb0v | fork-SeniorCareMarket-mmllm-claude-train-sym24-0a193354-1wb0v | 2.9267 |
| Iere6 | fork-slaa-us-mmllm-claude-train-sym24-81b6938d-Iere6 | 2.9489 |
| **mean** | | **2.7171** |
| **best** | | **2.5450** |

## Chain progression R1005 → R1006

Previous harvest: `workers/dispatcher/harvest-9way-r1005_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7793         | 2.7171         | -0.0622 |
| ctrl_bpc best  | 2.5466         | 2.5450         | -0.0016 |

## Per-round trajectory (best bird: ev2Xo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1006 | 6523 | 2.5450 | +0.1710 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1005_sym24`
  - `workers/dispatcher/harvest-5way-r1005_sym24`
  - `workers/dispatcher/harvest-9way-r1005_sym24`

## Output

`workers/dispatcher/harvest-6way-r1006_sym24/round-1006/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

