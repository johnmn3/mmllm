# harvest-2way-r655 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R655 ctrl_bpc |
|--------|--------|--------------:|
| J1LhC | origin/claude/train-sym24-e747d256-J1LhC | 4.1119 |
| lqiVV | fork-joly-os-mmllm-claude-train-sym24-e6cd75c1-lqiVV | 4.1181 |
| **mean** | | **4.1150** |
| **best** | | **4.1119** |

## Chain progression R654 → R655

Previous harvest: `workers/dispatcher/harvest-4way-r654_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1818         | 4.1150         | -0.0668 |
| ctrl_bpc best  | 4.1656         | 4.1119         | -0.0537 |

## Per-round trajectory (best bird: J1LhC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 655 | 4280 | 4.1119 | +0.0365 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r654_sym24`
  - `workers/dispatcher/harvest-4way-r654_sym24`

## Output

`workers/dispatcher/harvest-2way-r655_sym24/round-655/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

