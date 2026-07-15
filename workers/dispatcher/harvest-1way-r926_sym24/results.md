# harvest-1way-r926 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R926 ctrl_bpc |
|--------|--------|--------------:|
| DIgu4 | fork-joly-os-mmllm-claude-train-sym24-f7450f73-DIgu4 | 3.1158 |
| **mean** | | **3.1158** |
| **best** | | **3.1158** |

## Chain progression R925 → R926

Previous harvest: `workers/dispatcher/harvest-2way-r925_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0240         | 3.1158         | +0.0918 |
| ctrl_bpc best  | 2.9207         | 3.1158         | +0.1951 |

## Per-round trajectory (best bird: DIgu4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 926 | 6468 | 3.1158 | +0.2025 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r925_sym24`

## Output

`workers/dispatcher/harvest-1way-r926_sym24/round-926/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

