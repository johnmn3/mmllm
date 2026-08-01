# harvest-3way-r1080 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1080 ctrl_bpc |
|--------|--------|--------------:|
| pdzf4 | fork-joly-os-mmllm-claude-train-sym24-a5248cfb-pdzf4 | 2.4335 |
| ZqMDx | origin/claude/train-sym24-a27b8e76-ZqMDx | 2.4354 |
| 3RNb0 | origin/claude/train-sym24-87b836c8-3RNb0 | 2.4547 |
| **mean** | | **2.4412** |
| **best** | | **2.4335** |

## Chain progression R1079 → R1080

Previous harvest: `workers/dispatcher/harvest-4way-r1079_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6741         | 2.4412         | -0.2329 |
| ctrl_bpc best  | 2.6182         | 2.4335         | -0.1847 |

## Per-round trajectory (best bird: pdzf4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1080 | 6801 | 2.4335 | +0.2176 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1079_sym24`

## Output

`workers/dispatcher/harvest-3way-r1080_sym24/round-1080/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

