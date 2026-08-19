# harvest-1way-r1250 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1250 ctrl_bpc |
|--------|--------|--------------:|
| K4LCf | fork-joly-os-mmllm-claude-train-sym24-432e7d01-K4LCf | 2.4437 |
| **mean** | | **2.4437** |
| **best** | | **2.4437** |

## Chain progression R1249 → R1250

Previous harvest: `workers/dispatcher/harvest-5way-r1249_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3684         | 2.4437         | +0.0753 |
| ctrl_bpc best  | 2.2424         | 2.4437         | +0.2013 |

## Per-round trajectory (best bird: K4LCf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1250 | 3696 | 2.4437 | +0.2205 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1249_sym24`

## Output

`workers/dispatcher/harvest-1way-r1250_sym24/round-1250/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

