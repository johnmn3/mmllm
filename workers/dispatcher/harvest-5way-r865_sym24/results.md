# harvest-5way-r865 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R865 ctrl_bpc |
|--------|--------|--------------:|
| PSy8A | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a65dc43d-PSy8A | 2.8746 |
| F3UCz | fork-joly-os-mmllm-claude-train-sym24-311bec61-F3UCz | 3.0432 |
| A93Ft | fork-SeniorCareMarket-mmllm-claude-train-sym24-e0ff5121-A93Ft | 3.2597 |
| h4OFC | origin/claude/train-sym24-6de11601-h4OFC | 3.2714 |
| 2tgeI | fork-slaa-us-mmllm-claude-train-sym24-92c50a1d-2tgeI | 3.2722 |
| **mean** | | **3.1442** |
| **best** | | **2.8746** |

## Chain progression R864 → R865

Previous harvest: `workers/dispatcher/harvest-4way-r864_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0241         | 3.1442         | +0.1201 |
| ctrl_bpc best  | 2.8695         | 2.8746         | +0.0051 |

## Per-round trajectory (best bird: PSy8A)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 865 | 6569 | 2.8746 | +0.3965 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r864_sym24`

## Output

`workers/dispatcher/harvest-5way-r865_sym24/round-865/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

