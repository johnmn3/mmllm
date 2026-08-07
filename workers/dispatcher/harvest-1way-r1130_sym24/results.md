# harvest-1way-r1130 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1130 ctrl_bpc |
|--------|--------|--------------:|
| CK31C | fork-joly-os-mmllm-claude-train-sym24-ea1f7eac-CK31C | 2.5568 |
| **mean** | | **2.5568** |
| **best** | | **2.5568** |

## Chain progression R1129 → R1130

Previous harvest: `workers/dispatcher/harvest-6way-r1129_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5958         | 2.5568         | -0.0390 |
| ctrl_bpc best  | 2.3562         | 2.5568         | +0.2006 |

## Per-round trajectory (best bird: CK31C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1130 | 5275 | 2.5568 | +0.2140 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1129_sym24`

## Output

`workers/dispatcher/harvest-1way-r1130_sym24/round-1130/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

