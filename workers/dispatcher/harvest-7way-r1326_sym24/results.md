# harvest-7way-r1326 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1326 ctrl_bpc |
|--------|--------|--------------:|
| zCLqo | origin/claude/train-sym24-e1c43ede-zCLqo | 3.3055 |
| NQFeM | fork-slaa-us-mmllm-claude-train-sym24-61d8a124-NQFeM | 3.3379 |
| uN1wI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3b96b79-uN1wI | 3.4012 |
| Bj59b | fork-joly-os-mmllm-claude-train-sym24-18606f6a-Bj59b | 3.4061 |
| PCghy | fork-slaa-us-mmllm-claude-train-sym24-4fdff608-PCghy | 3.4288 |
| 937mI | origin/claude/train-sym24-d03cb502-937mI | 3.4327 |
| ibrol | fork-SeniorCareMarket-mmllm-claude-train-sym24-bbdca401-ibrol | 3.6547 |
| **mean** | | **3.4238** |
| **best** | | **3.3055** |

## Chain progression R1325 → R1326

Previous harvest: `workers/dispatcher/harvest-7way-r1325_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5022         | 3.4238         | -0.0784 |
| ctrl_bpc best  | 3.3586         | 3.3055         | -0.0531 |

## Per-round trajectory (best bird: zCLqo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1326 | 6491 | 3.3055 | +0.0874 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1325_sym24`
  - `workers/dispatcher/harvest-7way-r1325_sym24`

## Output

`workers/dispatcher/harvest-7way-r1326_sym24/round-1326/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

