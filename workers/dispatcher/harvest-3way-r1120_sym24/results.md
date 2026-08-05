# harvest-3way-r1120 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1120 ctrl_bpc |
|--------|--------|--------------:|
| AvrnV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c890c963-AvrnV | 2.3612 |
| HY8Hf | fork-joly-os-mmllm-claude-train-sym24-6a318c60-HY8Hf | 2.3704 |
| q31ct | fork-SeniorCareMarket-mmllm-claude-train-sym24-4d825625-q31ct | 2.7609 |
| **mean** | | **2.4975** |
| **best** | | **2.3612** |

## Chain progression R1119 → R1120

Previous harvest: `workers/dispatcher/harvest-6way-r1119_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5387         | 2.4975         | -0.0412 |
| ctrl_bpc best  | 2.3615         | 2.3612         | -0.0003 |

## Per-round trajectory (best bird: AvrnV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1120 | 6411 | 2.3612 | +0.2467 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1119_sym24`

## Output

`workers/dispatcher/harvest-3way-r1120_sym24/round-1120/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

