# harvest-1way-r1086 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1086 ctrl_bpc |
|--------|--------|--------------:|
| th8jH | fork-joly-os-mmllm-claude-train-sym24-bcd681bb-th8jH | 2.4211 |
| **mean** | | **2.4211** |
| **best** | | **2.4211** |

## Chain progression R1085 → R1086

Previous harvest: `workers/dispatcher/harvest-6way-r1085_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6627         | 2.4211         | -0.2416 |
| ctrl_bpc best  | 2.4499         | 2.4211         | -0.0288 |

## Per-round trajectory (best bird: th8jH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1086 | 3740 | 2.4211 | +0.2293 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1085_sym24`

## Output

`workers/dispatcher/harvest-1way-r1086_sym24/round-1086/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

