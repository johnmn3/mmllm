# harvest-1way-r1131 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1131 ctrl_bpc |
|--------|--------|--------------:|
| myiYB | fork-joly-os-mmllm-claude-train-sym24-75c26605-myiYB | 2.3769 |
| **mean** | | **2.3769** |
| **best** | | **2.3769** |

## Chain progression R1130 → R1131

Previous harvest: `workers/dispatcher/harvest-2way-r1130_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5551         | 2.3769         | -0.1782 |
| ctrl_bpc best  | 2.5534         | 2.3769         | -0.1765 |

## Per-round trajectory (best bird: myiYB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1131 | 6447 | 2.3769 | +0.2376 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1130_sym24`

## Output

`workers/dispatcher/harvest-1way-r1131_sym24/round-1131/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

