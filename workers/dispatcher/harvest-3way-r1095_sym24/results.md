# harvest-3way-r1095 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1095 ctrl_bpc |
|--------|--------|--------------:|
| La1Rh | fork-slaa-us-mmllm-claude-train-sym24-5d873c18-La1Rh | 2.4129 |
| 0tJvc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b8b4df98-0tJvc | 2.6122 |
| Yu6V0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3fdc1ce-Yu6V0 | 2.8121 |
| **mean** | | **2.6124** |
| **best** | | **2.4129** |

## Chain progression R1094 → R1095

Previous harvest: `workers/dispatcher/harvest-8way-r1094_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5071         | 2.6124         | +0.1053 |
| ctrl_bpc best  | 2.3966         | 2.4129         | +0.0163 |

## Per-round trajectory (best bird: La1Rh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1095 | 6636 | 2.4129 | +0.2299 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1094_sym24`

## Output

`workers/dispatcher/harvest-3way-r1095_sym24/round-1095/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

