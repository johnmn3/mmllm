# harvest-7way-r894 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R894 ctrl_bpc |
|--------|--------|--------------:|
| paCeE | fork-joly-os-mmllm-claude-train-sym24-730efc43-paCeE | 2.8022 |
| NnFTT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-06895052-NnFTT | 2.8158 |
| sTrAh | origin/claude/train-sym24-7ccc8d1c-sTrAh | 2.8212 |
| bsc9i | fork-joly-os-mmllm-claude-train-sym24-9d72f4c8-bsc9i | 3.1771 |
| Z1psA | fork-SeniorCareMarket-mmllm-claude-train-sym24-43e9a0a9-Z1psA | 3.1794 |
| uxLW8 | origin/claude/train-sym24-cf109578-uxLW8 | 3.1897 |
| LrnFA | fork-slaa-us-mmllm-claude-train-sym24-c007c55e-LrnFA | 3.1986 |
| **mean** | | **3.0263** |
| **best** | | **2.8022** |

## Chain progression R893 → R894

Previous harvest: `workers/dispatcher/harvest-6way-r893_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8737         | 3.0263         | +0.1526 |
| ctrl_bpc best  | 2.8070         | 2.8022         | -0.0048 |

## Per-round trajectory (best bird: paCeE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 894 | 6451 | 2.8022 | +0.3205 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r893_sym24`
  - `workers/dispatcher/harvest-6way-r893_sym24`

## Output

`workers/dispatcher/harvest-7way-r894_sym24/round-894/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

