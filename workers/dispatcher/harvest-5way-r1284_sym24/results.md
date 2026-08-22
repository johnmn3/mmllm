# harvest-5way-r1284 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1284 ctrl_bpc |
|--------|--------|--------------:|
| 7qiAb | origin/claude/train-sym24-384bbfe0-7qiAb | 2.2378 |
| mrM39 | fork-slaa-us-mmllm-claude-train-sym24-451fb64e-mrM39 | 2.2416 |
| WT7A0 | fork-joly-os-mmllm-claude-train-sym24-9354c3bb-WT7A0 | 2.4153 |
| mepId | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-df7dd809-mepId | 2.4170 |
| EuoYN | fork-SeniorCareMarket-mmllm-claude-train-sym24-391d8eaf-EuoYN | 2.4213 |
| **mean** | | **2.3466** |
| **best** | | **2.2378** |

## Chain progression R1283 → R1284

Previous harvest: `workers/dispatcher/harvest-11way-r1283_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3335         | 2.3466         | +0.0131 |
| ctrl_bpc best  | 2.2156         | 2.2378         | +0.0222 |

## Per-round trajectory (best bird: 7qiAb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1284 | 4486 | 2.2378 | +0.2439 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1283_sym24`

## Output

`workers/dispatcher/harvest-5way-r1284_sym24/round-1284/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

