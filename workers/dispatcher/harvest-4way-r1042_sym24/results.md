# harvest-4way-r1042 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1042 ctrl_bpc |
|--------|--------|--------------:|
| 0af1J | fork-SeniorCareMarket-mmllm-claude-train-sym24-f59e1129-0af1J | 2.4828 |
| EOXqZ | fork-slaa-us-mmllm-claude-train-sym24-23ea20c5-EOXqZ | 2.5147 |
| hdzRj | fork-joly-os-mmllm-claude-train-sym24-55df1c7d-hdzRj | 2.8690 |
| YHK9t | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0ef87004-YHK9t | 2.8775 |
| **mean** | | **2.6860** |
| **best** | | **2.4828** |

## Chain progression R1041 → R1042

Previous harvest: `workers/dispatcher/harvest-6way-r1041_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6266         | 2.6860         | +0.0594 |
| ctrl_bpc best  | 2.4803         | 2.4828         | +0.0025 |

## Per-round trajectory (best bird: 0af1J)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1042 | 5304 | 2.4828 | +0.2072 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1041_sym24`

## Output

`workers/dispatcher/harvest-4way-r1042_sym24/round-1042/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

