# harvest-4way-r729 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R729 ctrl_bpc |
|--------|--------|--------------:|
| xIiVv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-de2208e2-xIiVv | 3.4433 |
| mz9qr | fork-SeniorCareMarket-mmllm-claude-train-sym24-0ac6bcd7-mz9qr | 3.4653 |
| WLANN | origin/claude/train-sym24-77600a3e-WLANN | 3.4762 |
| aEHqg | origin/claude/train-sym24-c90de44d-aEHqg | 3.5182 |
| **mean** | | **3.4757** |
| **best** | | **3.4433** |

## Chain progression R728 → R729

Previous harvest: `workers/dispatcher/harvest-3way-r728_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4955         | 3.4757         | -0.0198 |
| ctrl_bpc best  | 3.4808         | 3.4433         | -0.0375 |

## Per-round trajectory (best bird: xIiVv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 729 | 6528 | 3.4433 | +0.8173 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r728_sym24`

## Output

`workers/dispatcher/harvest-4way-r729_sym24/round-729/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

