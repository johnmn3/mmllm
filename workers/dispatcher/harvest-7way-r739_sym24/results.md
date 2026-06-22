# harvest-7way-r739 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R739 ctrl_bpc |
|--------|--------|--------------:|
| mbpyA | fork-SeniorCareMarket-mmllm-claude-train-sym24-23b73902-mbpyA | 3.3744 |
| EpDFt | fork-davidwuchn-mmllm-claude-train-sym24-d4e0d3d5-EpDFt | 3.4261 |
| g2zgU | fork-slaa-us-mmllm-claude-train-sym24-999bbf28-g2zgU | 3.4475 |
| wcGr3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-19b86443-wcGr3 | 3.4505 |
| yH2nf | origin/claude/train-sym24-752f084b-yH2nf | 3.4673 |
| ZLJH2 | fork-slaa-us-mmllm-claude-train-sym24-b9e91089-ZLJH2 | 3.7431 |
| 8VZ5Z | fork-joly-os-mmllm-claude-train-sym24-bb1f0b72-8VZ5Z | 3.7554 |
| **mean** | | **3.5235** |
| **best** | | **3.3744** |

## Chain progression R738 → R739

Previous harvest: `workers/dispatcher/harvest-2way-r738_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6100         | 3.5235         | -0.0865 |
| ctrl_bpc best  | 3.4614         | 3.3744         | -0.0870 |

## Per-round trajectory (best bird: mbpyA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 739 | 6355 | 3.3744 | +0.8781 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r738_sym24`

## Output

`workers/dispatcher/harvest-7way-r739_sym24/round-739/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

