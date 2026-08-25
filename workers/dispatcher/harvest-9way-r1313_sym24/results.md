# harvest-9way-r1313 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1313 ctrl_bpc |
|--------|--------|--------------:|
| N3ccL | fork-SeniorCareMarket-mmllm-claude-train-sym24-93f7f4bc-N3ccL | 3.4215 |
| zLjgE | fork-slaa-us-mmllm-claude-train-sym24-36e35dc3-zLjgE | 3.4580 |
| zFa8K | fork-slaa-us-mmllm-claude-train-sym24-9a5acd8f-zFa8K | 3.4759 |
| IBsS0 | origin/claude/train-sym24-f7789663-IBsS0 | 3.4803 |
| kuBUQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-40d37acd-kuBUQ | 3.4871 |
| gC7Ac | fork-slaa-us-mmllm-claude-train-sym24-2438c945-gC7Ac | 3.4925 |
| PW19i | fork-joly-os-mmllm-claude-train-sym24-e65f69c8-PW19i | 3.5109 |
| FMSGn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f5a3751c-FMSGn | 3.5111 |
| mWbgK | fork-joly-os-mmllm-claude-train-sym24-9d97c102-mWbgK | 3.7914 |
| **mean** | | **3.5143** |
| **best** | | **3.4215** |

## Chain progression R1312 → R1313

Previous harvest: `workers/dispatcher/harvest-7way-r1312_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5125         | 3.5143         | +0.0018 |
| ctrl_bpc best  | 3.4164         | 3.4215         | +0.0051 |

## Per-round trajectory (best bird: N3ccL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1313 | 6644 | 3.4215 | +0.0615 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1312_sym24`
  - `workers/dispatcher/harvest-3way-r1312_sym24`
  - `workers/dispatcher/harvest-7way-r1312_sym24`

## Output

`workers/dispatcher/harvest-9way-r1313_sym24/round-1313/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

