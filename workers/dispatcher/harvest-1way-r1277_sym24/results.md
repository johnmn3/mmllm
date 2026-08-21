# harvest-1way-r1277 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1277 ctrl_bpc |
|--------|--------|--------------:|
| hsCut | fork-slaa-us-mmllm-claude-train-sym24-62577385-hsCut | 2.2280 |
| **mean** | | **2.2280** |
| **best** | | **2.2280** |

## Chain progression R1276 → R1277

Previous harvest: `workers/dispatcher/harvest-11way-r1276_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3970         | 2.2280         | -0.1690 |
| ctrl_bpc best  | 2.2483         | 2.2280         | -0.0203 |

## Per-round trajectory (best bird: hsCut)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1277 | 3964 | 2.2280 | +0.2473 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1276_sym24`

## Output

`workers/dispatcher/harvest-1way-r1277_sym24/round-1277/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

