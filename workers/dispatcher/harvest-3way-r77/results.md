# harvest-3way-r77 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R77 ctrl_bpc |
|--------|--------|--------------:|
| 5KVHI | fork-SeniorCareMarket-mmllm-claude-train-97d4fcb1-5KVHI | 0.9015 |
| jx7pd | fork-SeniorCareMarket-mmllm-claude-train-818ee7ad-jx7pd | 0.9191 |
| cQLX9 | fork-SeniorCareMarket-mmllm-claude-train-2c4c4df7-cQLX9 | 0.9836 |
| **mean** | | **0.9347** |
| **best** | | **0.9015** |

## Chain progression R76 → R77

Previous harvest: `workers/dispatcher/harvest-3way-r76`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0025         | 0.9347         | -0.0678 |
| ctrl_bpc best  | 0.9654         | 0.9015         | -0.0639 |

## Per-round trajectory (best bird: 5KVHI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 77 | 3376 | 0.9015 | +0.0038 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r76`

## Output

`workers/dispatcher/harvest-3way-r77/round-77/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

