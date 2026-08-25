# harvest-6way-r1315 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1315 ctrl_bpc |
|--------|--------|--------------:|
| nxLZC | fork-SeniorCareMarket-mmllm-claude-train-sym24-8cb530b7-nxLZC | 3.3720 |
| 1waeM | origin/claude/train-sym24-0d3bd00c-1waeM | 3.4139 |
| b8ibu | fork-slaa-us-mmllm-claude-train-sym24-34d292c5-b8ibu | 3.4905 |
| fvTk3 | fork-slaa-us-mmllm-claude-train-sym24-44e3d09b-fvTk3 | 3.7395 |
| 4kVJ0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b0fa6220-4kVJ0 | 3.7697 |
| FKkH5 | fork-joly-os-mmllm-claude-train-sym24-d957314e-FKkH5 | 3.8126 |
| **mean** | | **3.5997** |
| **best** | | **3.3720** |

## Chain progression R1314 → R1315

Previous harvest: `workers/dispatcher/harvest-7way-r1314_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6515         | 3.5997         | -0.0518 |
| ctrl_bpc best  | 3.4246         | 3.3720         | -0.0526 |

## Per-round trajectory (best bird: nxLZC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1315 | 6337 | 3.3720 | +0.0671 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1314_sym24`
  - `workers/dispatcher/harvest-7way-r1314_sym24`

## Output

`workers/dispatcher/harvest-6way-r1315_sym24/round-1315/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

