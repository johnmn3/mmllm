# harvest-2way-r114 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R114 ctrl_bpc |
|--------|--------|--------------:|
| vK5KJ | fork-slaa-us-mmllm-claude-train-sym24-381eae05-vK5KJ | 3.1696 |
| zc3WZ | fork-davidwuchn-mmllm-claude-train-sym24-8c208d16-zc3WZ | 3.2376 |
| **mean** | | **3.2036** |
| **best** | | **3.1696** |

## Chain progression R112 → R114

Previous harvest: `workers/dispatcher/harvest-1way-r112_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1699         | 3.2036         | +0.0337 |
| ctrl_bpc best  | 3.1699         | 3.1696         | -0.0003 |

## Per-round trajectory (best bird: vK5KJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 113 | 1273 | 3.2140 | +0.0192 |
| 114 | 1219 | 3.1696 | +0.0094 |

## Cumulative training contribution

- This harvest: **40 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **100 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r112_sym24`

## Output

`workers/dispatcher/harvest-2way-r114_sym24/round-114/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

