# harvest-1way-r915 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R915 ctrl_bpc |
|--------|--------|--------------:|
| IJgnh | origin/claude/train-sym24-66a20752-IJgnh | 2.7591 |
| **mean** | | **2.7591** |
| **best** | | **2.7591** |

## Chain progression R914 → R915

Previous harvest: `workers/dispatcher/harvest-2way-r914_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7747         | 2.7591         | -0.0156 |
| ctrl_bpc best  | 2.7730         | 2.7591         | -0.0139 |

## Per-round trajectory (best bird: IJgnh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 915 | 6419 | 2.7591 | +0.2242 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r914_sym24`

## Output

`workers/dispatcher/harvest-1way-r915_sym24/round-915/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

