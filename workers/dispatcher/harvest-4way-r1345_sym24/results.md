# harvest-4way-r1345 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1345 ctrl_bpc |
|--------|--------|--------------:|
| t2Z4f | origin/claude/train-sym24-59c2efc0-t2Z4f | 3.2448 |
| eaY1v | origin/claude/train-sym24-f7676886-eaY1v | 3.2736 |
| hbQIx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-47628c28-hbQIx | 3.6847 |
| Ph81o | fork-SeniorCareMarket-mmllm-claude-train-sym24-24caabbb-Ph81o | 3.7055 |
| **mean** | | **3.4771** |
| **best** | | **3.2448** |

## Chain progression R1344 → R1345

Previous harvest: `workers/dispatcher/harvest-3way-r1344_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2879         | 3.4771         | +0.1892 |
| ctrl_bpc best  | 3.2132         | 3.2448         | +0.0316 |

## Per-round trajectory (best bird: t2Z4f)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1345 | 6233 | 3.2448 | +0.1038 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1344_sym24`
  - `workers/dispatcher/harvest-3way-r1344_sym24`

## Output

`workers/dispatcher/harvest-4way-r1345_sym24/round-1345/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

