# harvest-2way-r1045 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1045 ctrl_bpc |
|--------|--------|--------------:|
| fb4DQ | origin/claude/train-sym24-fdfc084e-fb4DQ | 2.6808 |
| UuxTo | fork-slaa-us-mmllm-claude-train-sym24-2bfebac0-UuxTo | 2.8769 |
| **mean** | | **2.7789** |
| **best** | | **2.6808** |

## Chain progression R1044 → R1045

Previous harvest: `workers/dispatcher/harvest-4way-r1044_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6821         | 2.7789         | +0.0968 |
| ctrl_bpc best  | 2.4833         | 2.6808         | +0.1975 |

## Per-round trajectory (best bird: fb4DQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1045 | 6556 | 2.6808 | +0.1928 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1044_sym24`

## Output

`workers/dispatcher/harvest-2way-r1045_sym24/round-1045/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

