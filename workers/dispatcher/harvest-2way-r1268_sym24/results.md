# harvest-2way-r1268 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1268 ctrl_bpc |
|--------|--------|--------------:|
| DQati | fork-SeniorCareMarket-mmllm-claude-train-sym24-f1144534-DQati | 2.4168 |
| a41S5 | fork-slaa-us-mmllm-claude-train-sym24-48fbd7e0-a41S5 | 2.4222 |
| **mean** | | **2.4195** |
| **best** | | **2.4168** |

## Chain progression R1267 → R1268

Previous harvest: `workers/dispatcher/harvest-9way-r1267_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3654         | 2.4195         | +0.0541 |
| ctrl_bpc best  | 2.2200         | 2.4168         | +0.1968 |

## Per-round trajectory (best bird: DQati)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1268 | 3752 | 2.4168 | +0.2253 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1267_sym24`

## Output

`workers/dispatcher/harvest-2way-r1268_sym24/round-1268/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

