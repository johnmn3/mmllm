# harvest-2way-r664 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R664 ctrl_bpc |
|--------|--------|--------------:|
| YQA4R | origin/claude/train-sym24-5c8244d9-YQA4R | 3.9597 |
| hOm9R | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f2718d95-hOm9R | 3.9816 |
| **mean** | | **3.9707** |
| **best** | | **3.9597** |

## Chain progression R663 → R664

Previous harvest: `workers/dispatcher/harvest-7way-r663_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1668         | 3.9707         | -0.1962 |
| ctrl_bpc best  | 3.9529         | 3.9597         | +0.0068 |

## Per-round trajectory (best bird: YQA4R)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 664 | 6424 | 3.9597 | +0.1781 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r663_sym24`

## Output

`workers/dispatcher/harvest-2way-r664_sym24/round-664/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

