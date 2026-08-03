# harvest-3way-r1101 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1101 ctrl_bpc |
|--------|--------|--------------:|
| hVKRb | fork-slaa-us-mmllm-claude-train-sym24-0c66e1cb-hVKRb | 2.4013 |
| 8wLOh | origin/claude/train-sym24-1613f1d7-8wLOh | 2.4180 |
| H8TV5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-29743184-H8TV5 | 2.5957 |
| **mean** | | **2.4717** |
| **best** | | **2.4013** |

## Chain progression R1100 → R1101

Previous harvest: `workers/dispatcher/harvest-5way-r1100_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4820         | 2.4717         | -0.0103 |
| ctrl_bpc best  | 2.3944         | 2.4013         | +0.0069 |

## Per-round trajectory (best bird: hVKRb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1101 | 6656 | 2.4013 | +0.2600 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1100_sym24`

## Output

`workers/dispatcher/harvest-3way-r1101_sym24/round-1101/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

