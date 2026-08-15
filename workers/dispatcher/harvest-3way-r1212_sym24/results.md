# harvest-3way-r1212 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1212 ctrl_bpc |
|--------|--------|--------------:|
| dYwLc | fork-slaa-us-mmllm-claude-train-sym24-2a679946-dYwLc | 2.2943 |
| QUsmm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2069bdf3-QUsmm | 2.4659 |
| 73Dd6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5fa065a3-73Dd6 | 2.4758 |
| **mean** | | **2.4120** |
| **best** | | **2.2943** |

## Chain progression R1211 → R1212

Previous harvest: `workers/dispatcher/harvest-11way-r1211_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5049         | 2.4120         | -0.0929 |
| ctrl_bpc best  | 2.2716         | 2.2943         | +0.0227 |

## Per-round trajectory (best bird: dYwLc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1212 | 5531 | 2.2943 | +0.2448 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1211_sym24`

## Output

`workers/dispatcher/harvest-3way-r1212_sym24/round-1212/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

