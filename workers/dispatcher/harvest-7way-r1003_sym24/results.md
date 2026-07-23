# harvest-7way-r1003 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1003 ctrl_bpc |
|--------|--------|--------------:|
| jbVgf | origin/claude/train-sym24-0d63647b-jbVgf | 2.5522 |
| iipfp | origin/claude/train-sym24-4c8e9a70-iipfp | 2.5769 |
| W7ri4 | fork-slaa-us-mmllm-claude-train-sym24-46c45633-W7ri4 | 2.7349 |
| FNq3S | origin/claude/train-sym24-64435894-FNq3S | 2.7494 |
| cp4xi | fork-SeniorCareMarket-mmllm-claude-train-sym24-2f7ea460-cp4xi | 2.7513 |
| MlEiD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4e43394a-MlEiD | 2.9475 |
| l8Yev | fork-joly-os-mmllm-claude-train-sym24-fa7692d3-l8Yev | 2.9995 |
| **mean** | | **2.7588** |
| **best** | | **2.5522** |

## Chain progression R1002 → R1003

Previous harvest: `workers/dispatcher/harvest-5way-r1002_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7112         | 2.7588         | +0.0476 |
| ctrl_bpc best  | 2.5607         | 2.5522         | -0.0085 |

## Per-round trajectory (best bird: jbVgf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1003 | 4424 | 2.5522 | +0.1644 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1002_sym24`
  - `workers/dispatcher/harvest-3way-r1002_sym24`

## Output

`workers/dispatcher/harvest-7way-r1003_sym24/round-1003/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

