# harvest-1way-r825 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R825 ctrl_bpc |
|--------|--------|--------------:|
| R6P31 | fork-slaa-us-mmllm-claude-train-sym24-e6884709-R6P31 | 3.1534 |
| **mean** | | **3.1534** |
| **best** | | **3.1534** |

## Chain progression R824 → R825

Previous harvest: `workers/dispatcher/harvest-2way-r824_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0838         | 3.1534         | +0.0696 |
| ctrl_bpc best  | 3.0164         | 3.1534         | +0.1370 |

## Per-round trajectory (best bird: R6P31)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 825 | 4430 | 3.1534 | +0.4393 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r824_sym24`

## Output

`workers/dispatcher/harvest-1way-r825_sym24/round-825/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

