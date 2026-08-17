# harvest-6way-r1236 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1236 ctrl_bpc |
|--------|--------|--------------:|
| 1XBBv | fork-SeniorCareMarket-mmllm-claude-train-sym24-226db189-1XBBv | 2.2630 |
| RMchl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ef0c2506-RMchl | 2.2668 |
| kC9Gz | origin/claude/train-sym24-03e486b8-kC9Gz | 2.2682 |
| 9NtPr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cee584e0-9NtPr | 2.4558 |
| RcPfW | fork-slaa-us-mmllm-claude-train-sym24-3d2804a9-RcPfW | 2.6538 |
| xeqxJ | fork-joly-os-mmllm-claude-train-sym24-f9e1accf-xeqxJ | 2.6679 |
| **mean** | | **2.4293** |
| **best** | | **2.2630** |

## Chain progression R1235 → R1236

Previous harvest: `workers/dispatcher/harvest-6way-r1235_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4298         | 2.4293         | -0.0006 |
| ctrl_bpc best  | 2.2648         | 2.2630         | -0.0018 |

## Per-round trajectory (best bird: 1XBBv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1236 | 6524 | 2.2630 | +0.2439 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1235_sym24`
  - `workers/dispatcher/harvest-6way-r1235_sym24`

## Output

`workers/dispatcher/harvest-6way-r1236_sym24/round-1236/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

