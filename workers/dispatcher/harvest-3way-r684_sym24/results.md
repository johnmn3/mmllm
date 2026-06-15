# harvest-3way-r684 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R684 ctrl_bpc |
|--------|--------|--------------:|
| XH4Xe | fork-slaa-us-mmllm-claude-train-sym24-2c33f07f-XH4Xe | 3.7671 |
| YAPAM | origin/claude/train-sym24-b393038e-YAPAM | 3.7774 |
| s1ZrP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2c53b4d2-s1ZrP | 4.0715 |
| **mean** | | **3.8720** |
| **best** | | **3.7671** |

## Chain progression R683 → R684

Previous harvest: `workers/dispatcher/harvest-7way-r683_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8825         | 3.8720         | -0.0105 |
| ctrl_bpc best  | 3.7654         | 3.7671         | +0.0017 |

## Per-round trajectory (best bird: XH4Xe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 684 | 6347 | 3.7671 | +0.3646 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r683_sym24`

## Output

`workers/dispatcher/harvest-3way-r684_sym24/round-684/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

