# harvest-3way-r115 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R115 ctrl_bpc |
|--------|--------|--------------:|
| LfYq6 | fork-davidwuchn-mmllm-claude-train-sym24-1bad6645-LfYq6 | 2.8368 |
| euLEB | fork-joly-os-mmllm-claude-train-sym24-ff720cad-euLEB | 3.1892 |
| xKmF3 | fork-slaa-us-mmllm-claude-train-sym24-3dcd10ce-xKmF3 | 3.2006 |
| **mean** | | **3.0755** |
| **best** | | **2.8368** |

## Per-round trajectory (best bird: LfYq6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 115 | 5504 | 2.8368 | +0.0579 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **150 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r114_sym24`

## Output

`workers/dispatcher/harvest-3way-r115_sym24/round-115/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

