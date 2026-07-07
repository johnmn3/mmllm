# harvest-8way-r865 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R865 ctrl_bpc |
|--------|--------|--------------:|
| VX4ZU | fork-joly-os-mmllm-claude-train-sym24-93b09261-VX4ZU | 2.8693 |
| PSy8A | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a65dc43d-PSy8A | 2.8746 |
| 0fkWZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8e228a86-0fkWZ | 2.8840 |
| IrkKr | fork-slaa-us-mmllm-claude-train-sym24-6f8e4ac0-IrkKr | 2.9096 |
| F3UCz | fork-joly-os-mmllm-claude-train-sym24-311bec61-F3UCz | 3.0432 |
| A93Ft | fork-SeniorCareMarket-mmllm-claude-train-sym24-e0ff5121-A93Ft | 3.2597 |
| h4OFC | origin/claude/train-sym24-6de11601-h4OFC | 3.2714 |
| 2tgeI | fork-slaa-us-mmllm-claude-train-sym24-92c50a1d-2tgeI | 3.2722 |
| **mean** | | **3.0480** |
| **best** | | **2.8693** |

## Chain progression R864 → R865

Previous harvest: `workers/dispatcher/harvest-4way-r864_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0241         | 3.0480         | +0.0239 |
| ctrl_bpc best  | 2.8695         | 2.8693         | -0.0002 |

## Per-round trajectory (best bird: VX4ZU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 865 | 5356 | 2.8693 | +0.4226 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r864_sym24`
  - `workers/dispatcher/harvest-4way-r864_sym24`

## Output

`workers/dispatcher/harvest-8way-r865_sym24/round-865/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

