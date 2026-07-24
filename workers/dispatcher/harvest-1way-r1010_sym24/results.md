# harvest-1way-r1010 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1010 ctrl_bpc |
|--------|--------|--------------:|
| oiMYF | fork-slaa-us-mmllm-claude-train-sym24-6ac848e5-oiMYF | 2.9247 |
| **mean** | | **2.9247** |
| **best** | | **2.9247** |

## Chain progression R1009 → R1010

Previous harvest: `workers/dispatcher/harvest-6way-r1009_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7386         | 2.9247         | +0.1861 |
| ctrl_bpc best  | 2.5354         | 2.9247         | +0.3893 |

## Per-round trajectory (best bird: oiMYF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1010 | 4483 | 2.9247 | +0.1575 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1009_sym24`

## Output

`workers/dispatcher/harvest-1way-r1010_sym24/round-1010/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

