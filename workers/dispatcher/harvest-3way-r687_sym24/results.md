# harvest-3way-r687 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R687 ctrl_bpc |
|--------|--------|--------------:|
| dIyWk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7498b62d-dIyWk | 3.7382 |
| aQ7VN | fork-slaa-us-mmllm-claude-train-sym24-c90d938d-aQ7VN | 3.7384 |
| HKPQf | origin/claude/train-sym24-13325ca2-HKPQf | 4.0510 |
| **mean** | | **3.8425** |
| **best** | | **3.7382** |

## Chain progression R686 → R687

Previous harvest: `workers/dispatcher/harvest-8way-r686_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8105         | 3.8425         | +0.0320 |
| ctrl_bpc best  | 3.7412         | 3.7382         | -0.0030 |

## Per-round trajectory (best bird: dIyWk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 687 | 6297 | 3.7382 | +1.1417 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r686_sym24`

## Output

`workers/dispatcher/harvest-3way-r687_sym24/round-687/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

