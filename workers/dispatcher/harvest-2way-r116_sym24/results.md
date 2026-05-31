# harvest-2way-r116 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R116 ctrl_bpc |
|--------|--------|--------------:|
| yYtvm | fork-joly-os-mmllm-claude-train-sym24-b058972d-yYtvm | 2.8642 |
| Lwnd7 | fork-davidwuchn-mmllm-claude-train-sym24-4ee73387-Lwnd7 | 3.1643 |
| **mean** | | **3.0142** |
| **best** | | **2.8642** |

## Per-round trajectory (best bird: yYtvm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 115 | 1194 | 2.8595 | +0.0519 |
| 116 | 1209 | 2.8642 | +0.0507 |

## Cumulative training contribution

- This harvest: **40 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **40 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r114_sym24`

## Output

`workers/dispatcher/harvest-2way-r116_sym24/round-116/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

