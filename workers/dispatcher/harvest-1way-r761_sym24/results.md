# harvest-1way-r761 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R761 ctrl_bpc |
|--------|--------|--------------:|
| lcDEW | fork-joly-os-mmllm-claude-train-sym24-ed3e06c2-lcDEW | 3.3050 |
| **mean** | | **3.3050** |
| **best** | | **3.3050** |

## Chain progression R760 → R761

Previous harvest: `workers/dispatcher/harvest-13way-r760_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4714         | 3.3050         | -0.1664 |
| ctrl_bpc best  | 3.3115         | 3.3050         | -0.0065 |

## Per-round trajectory (best bird: lcDEW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 761 | 6730 | 3.3050 | +0.5912 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r760_sym24`

## Output

`workers/dispatcher/harvest-1way-r761_sym24/round-761/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

