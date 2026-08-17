# harvest-2way-r1231 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1231 ctrl_bpc |
|--------|--------|--------------:|
| RMAzZ | fork-joly-os-mmllm-claude-train-sym24-5a02ac7f-RMAzZ | 2.2547 |
| rbdfq | origin/claude/train-sym24-0887576a-rbdfq | 2.2700 |
| **mean** | | **2.2624** |
| **best** | | **2.2547** |

## Chain progression R1230 → R1231

Previous harvest: `workers/dispatcher/harvest-5way-r1230_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4597         | 2.2624         | -0.1974 |
| ctrl_bpc best  | 2.2561         | 2.2547         | -0.0014 |

## Per-round trajectory (best bird: RMAzZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1231 | 6338 | 2.2547 | +0.2653 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1230_sym24`

## Output

`workers/dispatcher/harvest-2way-r1231_sym24/round-1231/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

