# harvest-6way-r1268 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1268 ctrl_bpc |
|--------|--------|--------------:|
| aRooc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-987bbf9d-aRooc | 2.2296 |
| XGHvU | fork-joly-os-mmllm-claude-train-sym24-94e47822-XGHvU | 2.2450 |
| DQati | fork-SeniorCareMarket-mmllm-claude-train-sym24-f1144534-DQati | 2.4168 |
| a41S5 | fork-slaa-us-mmllm-claude-train-sym24-48fbd7e0-a41S5 | 2.4222 |
| uFp7G | origin/claude/train-sym24-8ec9ac1c-uFp7G | 2.6209 |
| P688P | fork-slaa-us-mmllm-claude-train-sym24-abec65d2-P688P | 2.6230 |
| **mean** | | **2.4263** |
| **best** | | **2.2296** |

## Chain progression R1267 → R1268

Previous harvest: `workers/dispatcher/harvest-9way-r1267_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3654         | 2.4263         | +0.0608 |
| ctrl_bpc best  | 2.2200         | 2.2296         | +0.0096 |

## Per-round trajectory (best bird: aRooc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1268 | 6405 | 2.2296 | +0.2480 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1267_sym24`
  - `workers/dispatcher/harvest-9way-r1267_sym24`

## Output

`workers/dispatcher/harvest-6way-r1268_sym24/round-1268/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

