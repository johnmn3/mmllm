# harvest-1way-r904 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R904 ctrl_bpc |
|--------|--------|--------------:|
| 2ej36 | fork-joly-os-mmllm-claude-train-sym24-c05b845c-2ej36 | 2.7666 |
| **mean** | | **2.7666** |
| **best** | | **2.7666** |

## Chain progression R903 → R904

Previous harvest: `workers/dispatcher/harvest-7way-r903_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9488         | 2.7666         | -0.1822 |
| ctrl_bpc best  | 2.7893         | 2.7666         | -0.0227 |

## Per-round trajectory (best bird: 2ej36)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 904 | 4407 | 2.7666 | +0.3558 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r903_sym24`

## Output

`workers/dispatcher/harvest-1way-r904_sym24/round-904/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

