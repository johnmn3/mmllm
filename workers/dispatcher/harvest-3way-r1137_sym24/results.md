# harvest-3way-r1137 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1137 ctrl_bpc |
|--------|--------|--------------:|
| B7b7X | fork-SeniorCareMarket-mmllm-claude-train-sym24-fe7d4f4f-B7b7X | 2.3697 |
| JlwZ3 | fork-joly-os-mmllm-claude-train-sym24-7de3b412-JlwZ3 | 2.3724 |
| 15Pt8 | fork-slaa-us-mmllm-claude-train-sym24-4736f009-15Pt8 | 2.5420 |
| **mean** | | **2.4280** |
| **best** | | **2.3697** |

## Chain progression R1136 → R1137

Previous harvest: `workers/dispatcher/harvest-9way-r1136_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5065         | 2.4280         | -0.0785 |
| ctrl_bpc best  | 2.3420         | 2.3697         | +0.0277 |

## Per-round trajectory (best bird: B7b7X)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1137 | 6490 | 2.3697 | +0.2365 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1136_sym24`

## Output

`workers/dispatcher/harvest-3way-r1137_sym24/round-1137/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

