# harvest-3way-r1045 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1045 ctrl_bpc |
|--------|--------|--------------:|
| YXV1O | fork-joly-os-mmllm-claude-train-sym24-16bd4925-YXV1O | 2.4859 |
| fb4DQ | origin/claude/train-sym24-fdfc084e-fb4DQ | 2.6808 |
| UuxTo | fork-slaa-us-mmllm-claude-train-sym24-2bfebac0-UuxTo | 2.8769 |
| **mean** | | **2.6812** |
| **best** | | **2.4859** |

## Chain progression R1044 → R1045

Previous harvest: `workers/dispatcher/harvest-4way-r1044_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6821         | 2.6812         | -0.0009 |
| ctrl_bpc best  | 2.4833         | 2.4859         | +0.0026 |

## Per-round trajectory (best bird: YXV1O)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1045 | 6339 | 2.4859 | +0.1984 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1044_sym24`
  - `workers/dispatcher/harvest-4way-r1044_sym24`

## Output

`workers/dispatcher/harvest-3way-r1045_sym24/round-1045/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

