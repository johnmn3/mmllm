# harvest-6way-r954 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R954 ctrl_bpc |
|--------|--------|--------------:|
| 96Rch | fork-joly-os-mmllm-claude-train-sym24-eddcf52b-96Rch | 2.6544 |
| 7j0gz | origin/claude/train-sym24-ce857137-7j0gz | 2.6557 |
| Qmufp | origin/claude/train-sym24-53a66c07-Qmufp | 2.6629 |
| Hmrbo | fork-joly-os-mmllm-claude-train-sym24-963a4183-Hmrbo | 2.6758 |
| lHvMd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-db7f3d01-lHvMd | 2.8336 |
| wR0Fu | fork-slaa-us-mmllm-claude-train-sym24-ee1dfc18-wR0Fu | 3.0546 |
| **mean** | | **2.7562** |
| **best** | | **2.6544** |

## Chain progression R953 → R954

Previous harvest: `workers/dispatcher/harvest-5way-r953_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8516         | 2.7562         | -0.0954 |
| ctrl_bpc best  | 2.6462         | 2.6544         | +0.0082 |

## Per-round trajectory (best bird: 96Rch)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 954 | 6657 | 2.6544 | +0.1963 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r953_sym24`
  - `workers/dispatcher/harvest-5way-r953_sym24`

## Output

`workers/dispatcher/harvest-6way-r954_sym24/round-954/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

