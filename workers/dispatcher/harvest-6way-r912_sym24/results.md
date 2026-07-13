# harvest-6way-r912 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R912 ctrl_bpc |
|--------|--------|--------------:|
| pvSXD | fork-SeniorCareMarket-mmllm-claude-train-sym24-7caf48cb-pvSXD | 2.7564 |
| MkXS2 | origin/claude/train-sym24-f6fa80b7-MkXS2 | 2.7694 |
| M41Jm | fork-slaa-us-mmllm-claude-train-sym24-622a811f-M41Jm | 2.9471 |
| yiEOC | origin/claude/train-sym24-1b18c510-yiEOC | 2.9503 |
| LpCcL | fork-joly-os-mmllm-claude-train-sym24-b1e856d7-LpCcL | 3.1841 |
| fcFu4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b52adee5-fcFu4 | 3.1897 |
| **mean** | | **2.9662** |
| **best** | | **2.7564** |

## Chain progression R911 → R912

Previous harvest: `workers/dispatcher/harvest-5way-r911_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8829         | 2.9662         | +0.0833 |
| ctrl_bpc best  | 2.7544         | 2.7564         | +0.0020 |

## Per-round trajectory (best bird: pvSXD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 912 | 6841 | 2.7564 | +0.2680 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r911_sym24`
  - `workers/dispatcher/harvest-5way-r911_sym24`

## Output

`workers/dispatcher/harvest-6way-r912_sym24/round-912/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

