# harvest-4way-r1176 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1176 ctrl_bpc |
|--------|--------|--------------:|
| 7ExRT | fork-joly-os-mmllm-claude-train-sym24-49b35ba5-7ExRT | 2.3108 |
| pD8rV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c50155e7-pD8rV | 2.3145 |
| bPl6x | origin/claude/train-sym24-6f58e8b1-bPl6x | 2.5086 |
| zxAbQ | fork-slaa-us-mmllm-claude-train-sym24-48f0b86c-zxAbQ | 2.5214 |
| **mean** | | **2.4138** |
| **best** | | **2.3108** |

## Chain progression R1175 → R1176

Previous harvest: `workers/dispatcher/harvest-9way-r1175_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4946         | 2.4138         | -0.0808 |
| ctrl_bpc best  | 2.3243         | 2.3108         | -0.0135 |

## Per-round trajectory (best bird: 7ExRT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1176 | 6566 | 2.3108 | +0.2520 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1175_sym24`

## Output

`workers/dispatcher/harvest-4way-r1176_sym24/round-1176/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

