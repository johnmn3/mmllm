# harvest-2way-r1100 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1100 ctrl_bpc |
|--------|--------|--------------:|
| PflfR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-03528719-PflfR | 2.3944 |
| 6F2gu | origin/claude/train-sym24-e7cb87ee-6F2gu | 2.4005 |
| **mean** | | **2.3975** |
| **best** | | **2.3944** |

## Chain progression R1099 → R1100

Previous harvest: `workers/dispatcher/harvest-3way-r1099_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4805         | 2.3975         | -0.0831 |
| ctrl_bpc best  | 2.4171         | 2.3944         | -0.0227 |

## Per-round trajectory (best bird: PflfR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1100 | 6509 | 2.3944 | +0.2340 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1099_sym24`

## Output

`workers/dispatcher/harvest-2way-r1100_sym24/round-1100/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

