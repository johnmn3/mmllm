# harvest-4way-r1408 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1408 ctrl_bpc |
|--------|--------|--------------:|
| dLUb8 | fork-joly-os-mmllm-claude-train-sym24-4e7bcdd0-dLUb8 | 3.2298 |
| NzKnx | fork-SeniorCareMarket-mmllm-claude-train-sym24-8db9038c-NzKnx | 3.2326 |
| e7kyv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1309e5ce-e7kyv | 3.2677 |
| mj7Ef | origin/claude/train-sym24-08c41169-mj7Ef | 3.6619 |
| **mean** | | **3.3480** |
| **best** | | **3.2298** |

## Chain progression R1407 → R1408

Previous harvest: `workers/dispatcher/harvest-6way-r1407_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3752         | 3.3480         | -0.0272 |
| ctrl_bpc best  | 3.2006         | 3.2298         | +0.0292 |

## Per-round trajectory (best bird: dLUb8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1408 | 6516 | 3.2298 | +0.2960 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1407_sym24`

## Output

`workers/dispatcher/harvest-4way-r1408_sym24/round-1408/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

