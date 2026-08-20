# harvest-8way-r1258 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1258 ctrl_bpc |
|--------|--------|--------------:|
| QlonI | fork-SeniorCareMarket-mmllm-claude-train-sym24-8dda44c0-QlonI | 2.2323 |
| SL7DV | fork-SeniorCareMarket-mmllm-claude-train-sym24-9289b392-SL7DV | 2.2337 |
| NslCe | fork-slaa-us-mmllm-claude-train-sym24-55ba4c78-NslCe | 2.2362 |
| i5Suo | origin/claude/train-sym24-e903f2a6-i5Suo | 2.2375 |
| kfufL | fork-joly-os-mmllm-claude-train-sym24-1a7487d3-kfufL | 2.2532 |
| p4ykN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e78684d1-p4ykN | 2.2579 |
| DlYNJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-101e9a42-DlYNJ | 2.2602 |
| RzqcC | fork-slaa-us-mmllm-claude-train-sym24-84e186e7-RzqcC | 2.6337 |
| **mean** | | **2.2931** |
| **best** | | **2.2323** |

## Chain progression R1257 → R1258

Previous harvest: `workers/dispatcher/harvest-9way-r1257_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3775         | 2.2931         | -0.0844 |
| ctrl_bpc best  | 2.2354         | 2.2323         | -0.0031 |

## Per-round trajectory (best bird: QlonI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1258 | 3762 | 2.2323 | +0.2478 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1257_sym24`
  - `workers/dispatcher/harvest-9way-r1257_sym24`

## Output

`workers/dispatcher/harvest-8way-r1258_sym24/round-1258/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

