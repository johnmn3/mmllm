# harvest-5way-r927 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R927 ctrl_bpc |
|--------|--------|--------------:|
| K4wpZ | origin/claude/train-sym24-df358e44-K4wpZ | 2.7310 |
| gmPQU | fork-SeniorCareMarket-mmllm-claude-train-sym24-448d08ba-gmPQU | 2.7396 |
| RZgHS | origin/claude/train-sym24-7c14ea7f-RZgHS | 2.9108 |
| wnHvT | fork-slaa-us-mmllm-claude-train-sym24-78da3c0a-wnHvT | 3.1039 |
| DH2sL | fork-joly-os-mmllm-claude-train-sym24-0465022a-DH2sL | 3.1235 |
| **mean** | | **2.9218** |
| **best** | | **2.7310** |

## Chain progression R926 → R927

Previous harvest: `workers/dispatcher/harvest-4way-r926_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9775         | 2.9218         | -0.0557 |
| ctrl_bpc best  | 2.7653         | 2.7310         | -0.0343 |

## Per-round trajectory (best bird: K4wpZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 927 | 6639 | 2.7310 | +0.2023 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r926_sym24`
  - `workers/dispatcher/harvest-4way-r926_sym24`

## Output

`workers/dispatcher/harvest-5way-r927_sym24/round-927/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

