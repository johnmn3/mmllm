# harvest-1way-r1330 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1330 ctrl_bpc |
|--------|--------|--------------:|
| yuVTb | fork-joly-os-mmllm-claude-train-sym24-e602d7a4-yuVTb | 3.6510 |
| **mean** | | **3.6510** |
| **best** | | **3.6510** |

## Chain progression R1329 → R1330

Previous harvest: `workers/dispatcher/harvest-1way-r1329_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2964         | 3.6510         | +0.3546 |
| ctrl_bpc best  | 3.2964         | 3.6510         | +0.3546 |

## Per-round trajectory (best bird: yuVTb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1330 | 6301 | 3.6510 | +0.0841 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1329_sym24`

## Output

`workers/dispatcher/harvest-1way-r1330_sym24/round-1330/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

