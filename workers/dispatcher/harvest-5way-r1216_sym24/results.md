# harvest-5way-r1216 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1216 ctrl_bpc |
|--------|--------|--------------:|
| JXqbB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-10ca2c4f-JXqbB | 2.2672 |
| El4nU | fork-SeniorCareMarket-mmllm-claude-train-sym24-243a0ef6-El4nU | 2.2750 |
| fDSNM | fork-slaa-us-mmllm-claude-train-sym24-9d8127a0-fDSNM | 2.2996 |
| Ka7rk | fork-joly-os-mmllm-claude-train-sym24-fdf214cd-Ka7rk | 2.4576 |
| pWIGo | origin/claude/train-sym24-d205bc47-pWIGo | 2.6609 |
| **mean** | | **2.3921** |
| **best** | | **2.2672** |

## Chain progression R1215 → R1216

Previous harvest: `workers/dispatcher/harvest-10way-r1215_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3999         | 2.3921         | -0.0078 |
| ctrl_bpc best  | 2.2702         | 2.2672         | -0.0030 |

## Per-round trajectory (best bird: JXqbB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1216 | 4269 | 2.2672 | +0.2533 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1215_sym24`

## Output

`workers/dispatcher/harvest-5way-r1216_sym24/round-1216/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

