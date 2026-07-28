# harvest-5way-r1051 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1051 ctrl_bpc |
|--------|--------|--------------:|
| 4zfx4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-37fded23-4zfx4 | 2.4703 |
| AeUGu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-39ba14a4-AeUGu | 2.4724 |
| qxbL3 | fork-slaa-us-mmllm-claude-train-sym24-1b5db6a4-qxbL3 | 2.4990 |
| 56r70 | fork-joly-os-mmllm-claude-train-sym24-bc705ce5-56r70 | 2.4993 |
| IOxYa | origin/claude/train-sym24-96d55aea-IOxYa | 2.6678 |
| **mean** | | **2.5218** |
| **best** | | **2.4703** |

## Chain progression R1050 → R1051

Previous harvest: `workers/dispatcher/harvest-9way-r1050_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5764         | 2.5218         | -0.0546 |
| ctrl_bpc best  | 2.4684         | 2.4703         | +0.0019 |

## Per-round trajectory (best bird: 4zfx4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1051 | 6420 | 2.4703 | +0.2104 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1050_sym24`
  - `workers/dispatcher/harvest-4way-r1050_sym24`

## Output

`workers/dispatcher/harvest-5way-r1051_sym24/round-1051/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

