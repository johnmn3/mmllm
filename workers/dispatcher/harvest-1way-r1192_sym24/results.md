# harvest-1way-r1192 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1192 ctrl_bpc |
|--------|--------|--------------:|
| feUDP | fork-joly-os-mmllm-claude-train-sym24-317fe1c4-feUDP | 2.4930 |
| **mean** | | **2.4930** |
| **best** | | **2.4930** |

## Chain progression R1191 → R1192

Previous harvest: `workers/dispatcher/harvest-11way-r1191_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4926         | 2.4930         | +0.0004 |
| ctrl_bpc best  | 2.2894         | 2.4930         | +0.2036 |

## Per-round trajectory (best bird: feUDP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1192 | 5323 | 2.4930 | +0.2229 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1191_sym24`

## Output

`workers/dispatcher/harvest-1way-r1192_sym24/round-1192/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

