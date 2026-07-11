# harvest-1way-r889 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R889 ctrl_bpc |
|--------|--------|--------------:|
| tbMru | fork-joly-os-mmllm-claude-train-sym24-6fcb8659-tbMru | 3.0220 |
| **mean** | | **3.0220** |
| **best** | | **3.0220** |

## Chain progression R888 → R889

Previous harvest: `workers/dispatcher/harvest-6way-r888_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9783         | 3.0220         | +0.0437 |
| ctrl_bpc best  | 2.8096         | 3.0220         | +0.2124 |

## Per-round trajectory (best bird: tbMru)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 889 | 5304 | 3.0220 | +0.2170 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r888_sym24`

## Output

`workers/dispatcher/harvest-1way-r889_sym24/round-889/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

