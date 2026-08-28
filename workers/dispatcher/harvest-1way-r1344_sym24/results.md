# harvest-1way-r1344 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1344 ctrl_bpc |
|--------|--------|--------------:|
| wEylN | fork-joly-os-mmllm-claude-train-sym24-c27ddbbd-wEylN | 3.3586 |
| **mean** | | **3.3586** |
| **best** | | **3.3586** |

## Chain progression R1343 → R1344

Previous harvest: `workers/dispatcher/harvest-2way-r1343_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5273         | 3.3586         | -0.1687 |
| ctrl_bpc best  | 3.2806         | 3.3586         | +0.0780 |

## Per-round trajectory (best bird: wEylN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1344 | 6494 | 3.3586 | +0.0855 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1343_sym24`

## Output

`workers/dispatcher/harvest-1way-r1344_sym24/round-1344/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

