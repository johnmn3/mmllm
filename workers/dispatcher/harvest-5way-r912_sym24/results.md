# harvest-5way-r912 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R912 ctrl_bpc |
|--------|--------|--------------:|
| pvSXD | fork-SeniorCareMarket-mmllm-claude-train-sym24-7caf48cb-pvSXD | 2.7564 |
| MkXS2 | origin/claude/train-sym24-f6fa80b7-MkXS2 | 2.7694 |
| M41Jm | fork-slaa-us-mmllm-claude-train-sym24-622a811f-M41Jm | 2.9471 |
| yiEOC | origin/claude/train-sym24-1b18c510-yiEOC | 2.9503 |
| LpCcL | fork-joly-os-mmllm-claude-train-sym24-b1e856d7-LpCcL | 3.1841 |
| **mean** | | **2.9215** |
| **best** | | **2.7564** |

## Chain progression R911 → R912

Previous harvest: `workers/dispatcher/harvest-5way-r911_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8829         | 2.9215         | +0.0386 |
| ctrl_bpc best  | 2.7544         | 2.7564         | +0.0020 |

## Per-round trajectory (best bird: pvSXD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 912 | 6841 | 2.7564 | +0.2680 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r911_sym24`
  - `workers/dispatcher/harvest-5way-r911_sym24`

## Output

`workers/dispatcher/harvest-5way-r912_sym24/round-912/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

