# harvest-3way-r785 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R785 ctrl_bpc |
|--------|--------|--------------:|
| bHOmG | fork-slaa-us-mmllm-claude-train-sym24-88b70606-bHOmG | 3.1653 |
| zwxjB | origin/claude/train-sym24-2ee2e051-zwxjB | 3.5651 |
| 8V77o | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6f745003-8V77o | 3.5674 |
| **mean** | | **3.4326** |
| **best** | | **3.1653** |

## Chain progression R784 → R785

Previous harvest: `workers/dispatcher/harvest-9way-r784_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3099         | 3.4326         | +0.1227 |
| ctrl_bpc best  | 3.1626         | 3.1653         | +0.0027 |

## Per-round trajectory (best bird: bHOmG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 785 | 4748 | 3.1653 | +0.6491 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r784_sym24`

## Output

`workers/dispatcher/harvest-3way-r785_sym24/round-785/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

