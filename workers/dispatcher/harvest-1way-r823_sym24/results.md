# harvest-1way-r823 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R823 ctrl_bpc |
|--------|--------|--------------:|
| T4CfH | fork-joly-os-mmllm-claude-train-sym24-551d2099-T4CfH | 3.0171 |
| **mean** | | **3.0171** |
| **best** | | **3.0171** |

## Chain progression R822 → R823

Previous harvest: `workers/dispatcher/harvest-8way-r822_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0565         | 3.0171         | -0.0394 |
| ctrl_bpc best  | 3.0094         | 3.0171         | +0.0077 |

## Per-round trajectory (best bird: T4CfH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 823 | 6851 | 3.0171 | +0.3854 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-8way-r822_sym24`

## Output

`workers/dispatcher/harvest-1way-r823_sym24/round-823/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

