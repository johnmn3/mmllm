# harvest-1way-r1202 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1202 ctrl_bpc |
|--------|--------|--------------:|
| iY8Xg | fork-joly-os-mmllm-claude-train-sym24-ea02950c-iY8Xg | 2.2838 |
| **mean** | | **2.2838** |
| **best** | | **2.2838** |

## Chain progression R1201 → R1202

Previous harvest: `workers/dispatcher/harvest-5way-r1201_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4151         | 2.2838         | -0.1313 |
| ctrl_bpc best  | 2.2929         | 2.2838         | -0.0091 |

## Per-round trajectory (best bird: iY8Xg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1202 | 3804 | 2.2838 | +0.2541 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1201_sym24`

## Output

`workers/dispatcher/harvest-1way-r1202_sym24/round-1202/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

