# harvest-2way-r1093 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1093 ctrl_bpc |
|--------|--------|--------------:|
| Sub9I | origin/claude/train-sym24-e12fbe44-Sub9I | 2.4075 |
| 9RiO6 | fork-joly-os-mmllm-claude-train-sym24-a6f673c7-9RiO6 | 2.6068 |
| **mean** | | **2.5072** |
| **best** | | **2.4075** |

## Chain progression R1092 → R1093

Previous harvest: `workers/dispatcher/harvest-3way-r1092_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6131         | 2.5072         | -0.1059 |
| ctrl_bpc best  | 2.4116         | 2.4075         | -0.0041 |

## Per-round trajectory (best bird: Sub9I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1093 | 5282 | 2.4075 | +0.2383 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1092_sym24`

## Output

`workers/dispatcher/harvest-2way-r1093_sym24/round-1093/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

