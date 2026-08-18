# harvest-9way-r1246 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1246 ctrl_bpc |
|--------|--------|--------------:|
| A1qcc | origin/claude/train-sym24-9d87f845-A1qcc | 2.2411 |
| bJF2b | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-078c550d-bJF2b | 2.2590 |
| CjJlg | fork-SeniorCareMarket-mmllm-claude-train-sym24-88e419fb-CjJlg | 2.2626 |
| fjVSS | origin/claude/train-sym24-755d807e-fjVSS | 2.2660 |
| 5yiYN | fork-joly-os-mmllm-claude-train-sym24-9e964b75-5yiYN | 2.2729 |
| 5stsZ | fork-slaa-us-mmllm-claude-train-sym24-6aa2d63c-5stsZ | 2.4349 |
| foLFO | fork-SeniorCareMarket-mmllm-claude-train-sym24-549dabb3-foLFO | 2.6343 |
| XfHA0 | fork-slaa-us-mmllm-claude-train-sym24-57c54c17-XfHA0 | 2.6392 |
| rbI2s | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-63a61a40-rbI2s | 2.6467 |
| **mean** | | **2.4063** |
| **best** | | **2.2411** |

## Chain progression R1245 → R1246

Previous harvest: `workers/dispatcher/harvest-9way-r1245_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3652         | 2.4063         | +0.0411 |
| ctrl_bpc best  | 2.2568         | 2.2411         | -0.0157 |

## Per-round trajectory (best bird: A1qcc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1246 | 5567 | 2.2411 | +0.2544 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1245_sym24`
  - `workers/dispatcher/harvest-9way-r1245_sym24`

## Output

`workers/dispatcher/harvest-9way-r1246_sym24/round-1246/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

