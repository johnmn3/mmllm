# harvest-1way-r671 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R671 ctrl_bpc |
|--------|--------|--------------:|
| PPhTZ | fork-joly-os-mmllm-claude-train-sym24-d30b6338-PPhTZ | 3.9317 |
| **mean** | | **3.9317** |
| **best** | | **3.9317** |

## Chain progression R670 → R671

Previous harvest: `workers/dispatcher/harvest-10way-r670_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9811         | 3.9317         | -0.0494 |
| ctrl_bpc best  | 3.8853         | 3.9317         | +0.0464 |

## Per-round trajectory (best bird: PPhTZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 671 | 4330 | 3.9317 | +0.5215 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r670_sym24`

## Output

`workers/dispatcher/harvest-1way-r671_sym24/round-671/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

