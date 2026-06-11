# harvest-5way-r651 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R651 ctrl_bpc |
|--------|--------|--------------:|
| cGaiw | origin/claude/train-sym24-1739bfce-cGaiw | 4.2378 |
| Q7y0F | fork-slaa-us-mmllm-claude-train-sym24-45390e71-Q7y0F | 4.2575 |
| qajf6 | fork-davidwuchn-mmllm-claude-train-sym24-357d3370-qajf6 | 4.2675 |
| j5VdA | fork-joly-os-mmllm-claude-train-sym24-a7d37ac8-j5VdA | 4.2688 |
| pNmmi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7ebbd772-pNmmi | 4.2779 |
| **mean** | | **4.2619** |
| **best** | | **4.2378** |

## Chain progression R650 → R651

Previous harvest: `workers/dispatcher/harvest-4way-r650_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.3006         | 4.2619         | -0.0387 |
| ctrl_bpc best  | 4.2784         | 4.2378         | -0.0406 |

## Per-round trajectory (best bird: cGaiw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 651 | 6406 | 4.2378 | +0.0588 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r650_sym24`

## Output

`workers/dispatcher/harvest-5way-r651_sym24/round-651/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

