# harvest-1way-r1254 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1254 ctrl_bpc |
|--------|--------|--------------:|
| hV2uo | fork-joly-os-mmllm-claude-train-sym24-c556be66-hV2uo | 2.6392 |
| **mean** | | **2.6392** |
| **best** | | **2.6392** |

## Chain progression R1253 → R1254

Previous harvest: `workers/dispatcher/harvest-6way-r1253_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4112         | 2.6392         | +0.2280 |
| ctrl_bpc best  | 2.2520         | 2.6392         | +0.3872 |

## Per-round trajectory (best bird: hV2uo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1254 | 4478 | 2.6392 | +0.2084 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1253_sym24`

## Output

`workers/dispatcher/harvest-1way-r1254_sym24/round-1254/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

