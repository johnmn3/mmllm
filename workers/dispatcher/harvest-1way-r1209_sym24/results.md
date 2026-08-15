# harvest-1way-r1209 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1209 ctrl_bpc |
|--------|--------|--------------:|
| fHqIW | fork-joly-os-mmllm-claude-train-sym24-a0e0c82c-fHqIW | 2.6564 |
| **mean** | | **2.6564** |
| **best** | | **2.6564** |

## Chain progression R1208 → R1209

Previous harvest: `workers/dispatcher/harvest-8way-r1208_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4342         | 2.6564         | +0.2222 |
| ctrl_bpc best  | 2.2958         | 2.6564         | +0.3606 |

## Per-round trajectory (best bird: fHqIW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1209 | 6412 | 2.6564 | +0.2394 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1208_sym24`

## Output

`workers/dispatcher/harvest-1way-r1209_sym24/round-1209/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

