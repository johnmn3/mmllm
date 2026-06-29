# harvest-2way-r801 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R801 ctrl_bpc |
|--------|--------|--------------:|
| rFDaO | origin/claude/train-sym24-ce4d5288-rFDaO | 3.0870 |
| 9ktXw | fork-joly-os-mmllm-claude-train-sym24-af42139c-9ktXw | 3.4626 |
| **mean** | | **3.2748** |
| **best** | | **3.0870** |

## Chain progression R800 → R801

Previous harvest: `workers/dispatcher/harvest-11way-r800_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3167         | 3.2748         | -0.0419 |
| ctrl_bpc best  | 3.0950         | 3.0870         | -0.0080 |

## Per-round trajectory (best bird: rFDaO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 801 | 6659 | 3.0870 | +0.5701 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r800_sym24`

## Output

`workers/dispatcher/harvest-2way-r801_sym24/round-801/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

