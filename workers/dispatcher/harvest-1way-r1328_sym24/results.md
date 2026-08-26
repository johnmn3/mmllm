# harvest-1way-r1328 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1328 ctrl_bpc |
|--------|--------|--------------:|
| pVYoT | fork-slaa-us-mmllm-claude-train-sym24-da055fab-pVYoT | 3.3676 |
| **mean** | | **3.3676** |
| **best** | | **3.3676** |

## Chain progression R1327 → R1328

Previous harvest: `workers/dispatcher/harvest-6way-r1327_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4177         | 3.3676         | -0.0501 |
| ctrl_bpc best  | 3.3393         | 3.3676         | +0.0283 |

## Per-round trajectory (best bird: pVYoT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1328 | 4293 | 3.3676 | +0.0841 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1327_sym24`

## Output

`workers/dispatcher/harvest-1way-r1328_sym24/round-1328/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

