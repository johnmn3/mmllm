# harvest-3way-r714 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R714 ctrl_bpc |
|--------|--------|--------------:|
| j7gWw | fork-slaa-us-mmllm-claude-train-sym24-cac427ae-j7gWw | 3.5427 |
| A8uD3 | origin/claude/train-sym24-9e30e2b1-A8uD3 | 3.5778 |
| 3lpD3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e780095c-3lpD3 | 3.5831 |
| **mean** | | **3.5679** |
| **best** | | **3.5427** |

## Chain progression R713 → R714

Previous harvest: `workers/dispatcher/harvest-10way-r713_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7013         | 3.5679         | -0.1334 |
| ctrl_bpc best  | 3.5473         | 3.5427         | -0.0046 |

## Per-round trajectory (best bird: j7gWw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 714 | 6536 | 3.5427 | +1.5014 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r713_sym24`

## Output

`workers/dispatcher/harvest-3way-r714_sym24/round-714/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

