# harvest-1way-r953 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R953 ctrl_bpc |
|--------|--------|--------------:|
| cSgFs | fork-joly-os-mmllm-claude-train-sym24-ffb40b6a-cSgFs | 3.0430 |
| **mean** | | **3.0430** |
| **best** | | **3.0430** |

## Chain progression R952 → R953

Previous harvest: `workers/dispatcher/harvest-4way-r952_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8001         | 3.0430         | +0.2429 |
| ctrl_bpc best  | 2.6406         | 3.0430         | +0.4024 |

## Per-round trajectory (best bird: cSgFs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 953 | 6766 | 3.0430 | +0.1574 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r952_sym24`

## Output

`workers/dispatcher/harvest-1way-r953_sym24/round-953/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

