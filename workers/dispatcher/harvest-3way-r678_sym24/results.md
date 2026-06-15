# harvest-3way-r678 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R678 ctrl_bpc |
|--------|--------|--------------:|
| DVpLD | fork-slaa-us-mmllm-claude-train-sym24-3e66e3b0-DVpLD | 3.8350 |
| tO6dk | origin/claude/train-sym24-d3f9a54d-tO6dk | 3.9135 |
| gyKTr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c0ff045a-gyKTr | 4.1263 |
| **mean** | | **3.9583** |
| **best** | | **3.8350** |

## Chain progression R677 → R678

Previous harvest: `workers/dispatcher/harvest-8way-r677_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9321         | 3.9583         | +0.0262 |
| ctrl_bpc best  | 3.8053         | 3.8350         | +0.0297 |

## Per-round trajectory (best bird: DVpLD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 678 | 6661 | 3.8350 | +0.5037 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r677_sym24`

## Output

`workers/dispatcher/harvest-3way-r678_sym24/round-678/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

