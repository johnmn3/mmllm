# harvest-6way-r1132 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1132 ctrl_bpc |
|--------|--------|--------------:|
| 2DEwC | origin/claude/train-sym24-835faeaf-2DEwC | 2.3471 |
| p6JZh | origin/claude/train-sym24-b8038002-p6JZh | 2.3774 |
| wzfwQ | fork-slaa-us-mmllm-claude-train-sym24-7df31ff6-wzfwQ | 2.5541 |
| C7peR | fork-SeniorCareMarket-mmllm-claude-train-sym24-bbf5d33e-C7peR | 2.5558 |
| nYVNh | fork-joly-os-mmllm-claude-train-sym24-e1f440b2-nYVNh | 2.5609 |
| DlWYS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3989098d-DlWYS | 2.7601 |
| **mean** | | **2.5259** |
| **best** | | **2.3471** |

## Chain progression R1131 → R1132

Previous harvest: `workers/dispatcher/harvest-4way-r1131_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5097         | 2.5259         | +0.0162 |
| ctrl_bpc best  | 2.3510         | 2.3471         | -0.0039 |

## Per-round trajectory (best bird: 2DEwC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1132 | 6388 | 2.3471 | +0.2442 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1131_sym24`
  - `workers/dispatcher/harvest-4way-r1131_sym24`

## Output

`workers/dispatcher/harvest-6way-r1132_sym24/round-1132/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

