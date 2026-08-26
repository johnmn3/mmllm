# harvest-2way-r1326 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1326 ctrl_bpc |
|--------|--------|--------------:|
| uN1wI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3b96b79-uN1wI | 3.4012 |
| 937mI | origin/claude/train-sym24-d03cb502-937mI | 3.4327 |
| **mean** | | **3.4169** |
| **best** | | **3.4012** |

## Chain progression R1325 → R1326

Previous harvest: `workers/dispatcher/harvest-7way-r1325_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5022         | 3.4169         | -0.0853 |
| ctrl_bpc best  | 3.3586         | 3.4012         | +0.0426 |

## Per-round trajectory (best bird: uN1wI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1326 | 3890 | 3.4012 | +0.0717 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1325_sym24`

## Output

`workers/dispatcher/harvest-2way-r1326_sym24/round-1326/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

