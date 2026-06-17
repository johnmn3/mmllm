# harvest-3way-r695 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R695 ctrl_bpc |
|--------|--------|--------------:|
| 8orcu | fork-slaa-us-mmllm-claude-train-sym24-9a034cbe-8orcu | 3.6931 |
| Xfc6g | origin/claude/train-sym24-403c5822-Xfc6g | 3.6994 |
| OJ3IL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-555efb52-OJ3IL | 3.7041 |
| **mean** | | **3.6989** |
| **best** | | **3.6931** |

## Chain progression R694 → R695

Previous harvest: `workers/dispatcher/harvest-12way-r694_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8496         | 3.6989         | -0.1507 |
| ctrl_bpc best  | 3.6410         | 3.6931         | +0.0521 |

## Per-round trajectory (best bird: 8orcu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 695 | 6438 | 3.6931 | +0.4719 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r694_sym24`

## Output

`workers/dispatcher/harvest-3way-r695_sym24/round-695/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

