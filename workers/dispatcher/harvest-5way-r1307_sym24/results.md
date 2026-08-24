# harvest-5way-r1307 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1307 ctrl_bpc |
|--------|--------|--------------:|
| jAILm | fork-SeniorCareMarket-mmllm-claude-train-sym24-d73cfb38-jAILm | 3.4116 |
| ivIGT | fork-slaa-us-mmllm-claude-train-sym24-2845d528-ivIGT | 3.4127 |
| RyN46 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5ec40753-RyN46 | 3.4256 |
| ia9Am | fork-joly-os-mmllm-claude-train-sym24-1934be90-ia9Am | 3.8491 |
| 1pNR6 | fork-slaa-us-mmllm-claude-train-sym24-dd5db80f-1pNR6 | 3.9966 |
| **mean** | | **3.6191** |
| **best** | | **3.4116** |

## Chain progression R1306 → R1307

Previous harvest: `workers/dispatcher/harvest-12way-r1306_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6245         | 3.6191         | -0.0054 |
| ctrl_bpc best  | 3.4164         | 3.4116         | -0.0048 |

## Per-round trajectory (best bird: jAILm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1307 | 3591 | 3.4116 | +0.0915 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r1306_sym24`
  - `workers/dispatcher/harvest-7way-r1306_sym24`

## Output

`workers/dispatcher/harvest-5way-r1307_sym24/round-1307/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

