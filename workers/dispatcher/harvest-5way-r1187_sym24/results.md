# harvest-5way-r1187 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1187 ctrl_bpc |
|--------|--------|--------------:|
| clQyy | fork-joly-os-mmllm-claude-train-sym24-c4681bc9-clQyy | 2.3080 |
| dsLax | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0eb823c9-dsLax | 2.3168 |
| ovThz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-621941f6-ovThz | 2.3180 |
| 4Y76y | fork-SeniorCareMarket-mmllm-claude-train-sym24-971c1fba-4Y76y | 2.4891 |
| 5AzPM | fork-slaa-us-mmllm-claude-train-sym24-64b0ec87-5AzPM | 2.4990 |
| **mean** | | **2.3862** |
| **best** | | **2.3080** |

## Chain progression R1186 → R1187

Previous harvest: `workers/dispatcher/harvest-8way-r1186_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5968         | 2.3862         | -0.2106 |
| ctrl_bpc best  | 2.2986         | 2.3080         | +0.0094 |

## Per-round trajectory (best bird: clQyy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1187 | 6927 | 2.3080 | +0.2608 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1186_sym24`
  - `workers/dispatcher/harvest-8way-r1186_sym24`

## Output

`workers/dispatcher/harvest-5way-r1187_sym24/round-1187/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

