# harvest-5way-r1321 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1321 ctrl_bpc |
|--------|--------|--------------:|
| WYvvM | fork-SeniorCareMarket-mmllm-claude-train-sym24-86c887e6-WYvvM | 3.3979 |
| 4pYBV | fork-slaa-us-mmllm-claude-train-sym24-23fedd0e-4pYBV | 3.4401 |
| LTHYb | origin/claude/train-sym24-a8313f35-LTHYb | 3.4407 |
| ytzmE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f8a82058-ytzmE | 3.4495 |
| eq39R | fork-SeniorCareMarket-mmllm-claude-train-sym24-024e2a72-eq39R | 3.4590 |
| **mean** | | **3.4374** |
| **best** | | **3.3979** |

## Chain progression R1320 → R1321

Previous harvest: `workers/dispatcher/harvest-3way-r1320_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4815         | 3.4374         | -0.0441 |
| ctrl_bpc best  | 3.4712         | 3.3979         | -0.0733 |

## Per-round trajectory (best bird: WYvvM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1321 | 3476 | 3.3979 | +0.0656 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1320_sym24`
  - `workers/dispatcher/harvest-3way-r1320_sym24`

## Output

`workers/dispatcher/harvest-5way-r1321_sym24/round-1321/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

