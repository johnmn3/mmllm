# harvest-3way-r855 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R855 ctrl_bpc |
|--------|--------|--------------:|
| voRmD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0ddb3ff8-voRmD | 2.9259 |
| FfMhF | fork-slaa-us-mmllm-claude-train-sym24-23a7cd46-FfMhF | 3.2840 |
| LrFNA | origin/claude/train-sym24-b8d99a9b-LrFNA | 3.3067 |
| **mean** | | **3.1722** |
| **best** | | **2.9259** |

## Chain progression R854 → R855

Previous harvest: `workers/dispatcher/harvest-3way-r854_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9761         | 3.1722         | +0.1961 |
| ctrl_bpc best  | 2.9177         | 2.9259         | +0.0082 |

## Per-round trajectory (best bird: voRmD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 855 | 6478 | 2.9259 | +0.3172 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r854_sym24`

## Output

`workers/dispatcher/harvest-3way-r855_sym24/round-855/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

