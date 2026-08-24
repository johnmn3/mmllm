# harvest-4way-r1301 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1301 ctrl_bpc |
|--------|--------|--------------:|
| yBq81 | fork-joly-os-mmllm-claude-train-sym24-4471e447-yBq81 | 3.6795 |
| 2WAc5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a5ca5a1f-2WAc5 | 3.7454 |
| asOCg | fork-slaa-us-mmllm-claude-train-sym24-9eb84665-asOCg | 4.0358 |
| VTxUM | origin/claude/train-sym24-1dd2a5d8-VTxUM | 4.0434 |
| **mean** | | **3.8760** |
| **best** | | **3.6795** |

## Chain progression R1300 → R1301

Previous harvest: `workers/dispatcher/harvest-7way-r1300_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8222         | 3.8760         | +0.0538 |
| ctrl_bpc best  | 3.5802         | 3.6795         | +0.0993 |

## Per-round trajectory (best bird: yBq81)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1301 | 6797 | 3.6795 | +0.0836 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1300_sym24`

## Output

`workers/dispatcher/harvest-4way-r1301_sym24/round-1301/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

