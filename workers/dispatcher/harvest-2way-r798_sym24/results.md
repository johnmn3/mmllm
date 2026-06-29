# harvest-2way-r798 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R798 ctrl_bpc |
|--------|--------|--------------:|
| 9Qokt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-58da584b-9Qokt | 3.1143 |
| EShSp | origin/claude/train-sym24-eedf5491-EShSp | 3.1305 |
| **mean** | | **3.1224** |
| **best** | | **3.1143** |

## Chain progression R797 → R798

Previous harvest: `workers/dispatcher/harvest-3way-r797_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4189         | 3.1224         | -0.2965 |
| ctrl_bpc best  | 3.2583         | 3.1143         | -0.1440 |

## Per-round trajectory (best bird: 9Qokt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 798 | 4158 | 3.1143 | +0.4943 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r797_sym24`

## Output

`workers/dispatcher/harvest-2way-r798_sym24/round-798/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

