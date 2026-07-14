# harvest-2way-r919 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R919 ctrl_bpc |
|--------|--------|--------------:|
| CpEQF | origin/claude/train-sym24-2abe1909-CpEQF | 2.7279 |
| SXSko | fork-SeniorCareMarket-mmllm-claude-train-sym24-00a86ab2-SXSko | 2.9495 |
| **mean** | | **2.8387** |
| **best** | | **2.7279** |

## Chain progression R918 → R919

Previous harvest: `workers/dispatcher/harvest-3way-r918_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8164         | 2.8387         | +0.0223 |
| ctrl_bpc best  | 2.7358         | 2.7279         | -0.0079 |

## Per-round trajectory (best bird: CpEQF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 919 | 3708 | 2.7279 | +0.2526 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r918_sym24`

## Output

`workers/dispatcher/harvest-2way-r919_sym24/round-919/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

