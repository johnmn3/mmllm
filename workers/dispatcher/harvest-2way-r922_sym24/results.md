# harvest-2way-r922 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R922 ctrl_bpc |
|--------|--------|--------------:|
| 5zOyL | fork-SeniorCareMarket-mmllm-claude-train-sym24-72fa4f50-5zOyL | 2.7258 |
| uM9Ud | origin/claude/train-sym24-0e3a797d-uM9Ud | 2.7557 |
| **mean** | | **2.7408** |
| **best** | | **2.7258** |

## Chain progression R921 → R922

Previous harvest: `workers/dispatcher/harvest-11way-r921_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9054         | 2.7408         | -0.1646 |
| ctrl_bpc best  | 2.7224         | 2.7258         | +0.0034 |

## Per-round trajectory (best bird: 5zOyL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 922 | 4409 | 2.7258 | +0.2053 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r921_sym24`

## Output

`workers/dispatcher/harvest-2way-r922_sym24/round-922/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

