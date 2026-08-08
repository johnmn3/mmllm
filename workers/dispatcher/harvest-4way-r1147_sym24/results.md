# harvest-4way-r1147 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1147 ctrl_bpc |
|--------|--------|--------------:|
| hXPQX | fork-SeniorCareMarket-mmllm-claude-train-sym24-6610d53a-hXPQX | 2.3629 |
| KlCNf | origin/claude/train-sym24-dd833eac-KlCNf | 2.5440 |
| gAOkN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ce446b24-gAOkN | 2.5450 |
| NhsQT | fork-slaa-us-mmllm-claude-train-sym24-dca3e6df-NhsQT | 2.7306 |
| **mean** | | **2.5456** |
| **best** | | **2.3629** |

## Chain progression R1146 → R1147

Previous harvest: `workers/dispatcher/harvest-14way-r1146_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5151         | 2.5456         | +0.0305 |
| ctrl_bpc best  | 2.3370         | 2.3629         | +0.0259 |

## Per-round trajectory (best bird: hXPQX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1147 | 6258 | 2.3629 | +0.2309 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1146_sym24`

## Output

`workers/dispatcher/harvest-4way-r1147_sym24/round-1147/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

