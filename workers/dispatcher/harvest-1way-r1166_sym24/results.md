# harvest-1way-r1166 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1166 ctrl_bpc |
|--------|--------|--------------:|
| xfKIw | fork-joly-os-mmllm-claude-train-sym24-de98d170-xfKIw | 2.3492 |
| **mean** | | **2.3492** |
| **best** | | **2.3492** |

## Chain progression R1165 → R1166

Previous harvest: `workers/dispatcher/harvest-9way-r1165_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5667         | 2.3492         | -0.2175 |
| ctrl_bpc best  | 2.3195         | 2.3492         | +0.0297 |

## Per-round trajectory (best bird: xfKIw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1166 | 3933 | 2.3492 | +0.2337 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1165_sym24`

## Output

`workers/dispatcher/harvest-1way-r1166_sym24/round-1166/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

