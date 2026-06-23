# harvest-3way-r745 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R745 ctrl_bpc |
|--------|--------|--------------:|
| KpsDw | origin/claude/train-sym24-aa3cc493-KpsDw | 3.3637 |
| rilz1 | fork-joly-os-mmllm-claude-train-sym24-eafa1d64-rilz1 | 3.3784 |
| xQj5d | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-684d1f92-xQj5d | 3.4003 |
| **mean** | | **3.3808** |
| **best** | | **3.3637** |

## Chain progression R744 → R745

Previous harvest: `workers/dispatcher/harvest-5way-r744_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6056         | 3.3808         | -0.2248 |
| ctrl_bpc best  | 3.4064         | 3.3637         | -0.0427 |

## Per-round trajectory (best bird: KpsDw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 745 | 6682 | 3.3637 | +0.4983 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r744_sym24`

## Output

`workers/dispatcher/harvest-3way-r745_sym24/round-745/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

