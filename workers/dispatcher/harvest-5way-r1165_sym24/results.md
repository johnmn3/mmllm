# harvest-5way-r1165 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1165 ctrl_bpc |
|--------|--------|--------------:|
| dZ54z | fork-joly-os-mmllm-claude-train-sym24-9aea8650-dZ54z | 2.3195 |
| ms90T | fork-slaa-us-mmllm-claude-train-sym24-029ec83f-ms90T | 2.3535 |
| KZ12J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-15d0256c-KZ12J | 2.7111 |
| 0gSpZ | origin/claude/train-sym24-65464433-0gSpZ | 2.7130 |
| rjmS5 | fork-slaa-us-mmllm-claude-train-sym24-fb1a12d2-rjmS5 | 2.7151 |
| **mean** | | **2.5624** |
| **best** | | **2.3195** |

## Chain progression R1164 → R1165

Previous harvest: `workers/dispatcher/harvest-10way-r1164_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5482         | 2.5624         | +0.0142 |
| ctrl_bpc best  | 2.3205         | 2.3195         | -0.0010 |

## Per-round trajectory (best bird: dZ54z)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1165 | 6708 | 2.3195 | +0.2595 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1164_sym24`
  - `workers/dispatcher/harvest-6way-r1164_sym24`

## Output

`workers/dispatcher/harvest-5way-r1165_sym24/round-1165/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

