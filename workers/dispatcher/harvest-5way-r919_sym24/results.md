# harvest-5way-r919 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R919 ctrl_bpc |
|--------|--------|--------------:|
| CpEQF | origin/claude/train-sym24-2abe1909-CpEQF | 2.7279 |
| TmZmS | fork-slaa-us-mmllm-claude-train-sym24-2b75438e-TmZmS | 2.7500 |
| Y9MRj | origin/claude/train-sym24-3e735949-Y9MRj | 2.9469 |
| SXSko | fork-SeniorCareMarket-mmllm-claude-train-sym24-00a86ab2-SXSko | 2.9495 |
| kaSSm | fork-joly-os-mmllm-claude-train-sym24-7a797ed6-kaSSm | 3.1314 |
| **mean** | | **2.9011** |
| **best** | | **2.7279** |

## Chain progression R918 → R919

Previous harvest: `workers/dispatcher/harvest-3way-r918_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8164         | 2.9011         | +0.0847 |
| ctrl_bpc best  | 2.7358         | 2.7279         | -0.0079 |

## Per-round trajectory (best bird: CpEQF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 919 | 3708 | 2.7279 | +0.2526 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r918_sym24`
  - `workers/dispatcher/harvest-3way-r918_sym24`

## Output

`workers/dispatcher/harvest-5way-r919_sym24/round-919/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

