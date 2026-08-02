# harvest-2way-r1091 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1091 ctrl_bpc |
|--------|--------|--------------:|
| FeK5K | origin/claude/train-sym24-e3f9e4a7-FeK5K | 2.4082 |
| PnKhD | fork-joly-os-mmllm-claude-train-sym24-3e3f0439-PnKhD | 2.8264 |
| **mean** | | **2.6173** |
| **best** | | **2.4082** |

## Chain progression R1090 → R1091

Previous harvest: `workers/dispatcher/harvest-5way-r1090_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5807         | 2.6173         | +0.0366 |
| ctrl_bpc best  | 2.4119         | 2.4082         | -0.0037 |

## Per-round trajectory (best bird: FeK5K)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1091 | 3672 | 2.4082 | +0.2301 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1090_sym24`

## Output

`workers/dispatcher/harvest-2way-r1091_sym24/round-1091/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

