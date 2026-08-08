# harvest-1way-r1141 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1141 ctrl_bpc |
|--------|--------|--------------:|
| UrkhK | fork-slaa-us-mmllm-claude-train-sym24-7522c18d-UrkhK | 2.3461 |
| **mean** | | **2.3461** |
| **best** | | **2.3461** |

## Chain progression R1140 → R1141

Previous harvest: `workers/dispatcher/harvest-6way-r1140_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4548         | 2.3461         | -0.1087 |
| ctrl_bpc best  | 2.3424         | 2.3461         | +0.0037 |

## Per-round trajectory (best bird: UrkhK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1141 | 3735 | 2.3461 | +0.2485 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1140_sym24`

## Output

`workers/dispatcher/harvest-1way-r1141_sym24/round-1141/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

