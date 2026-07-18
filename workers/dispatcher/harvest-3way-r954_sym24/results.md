# harvest-3way-r954 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R954 ctrl_bpc |
|--------|--------|--------------:|
| 96Rch | fork-joly-os-mmllm-claude-train-sym24-eddcf52b-96Rch | 2.6544 |
| 7j0gz | origin/claude/train-sym24-ce857137-7j0gz | 2.6557 |
| lHvMd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-db7f3d01-lHvMd | 2.8336 |
| **mean** | | **2.7146** |
| **best** | | **2.6544** |

## Chain progression R953 → R954

Previous harvest: `workers/dispatcher/harvest-5way-r953_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8516         | 2.7146         | -0.1370 |
| ctrl_bpc best  | 2.6462         | 2.6544         | +0.0082 |

## Per-round trajectory (best bird: 96Rch)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 954 | 6657 | 2.6544 | +0.1963 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r953_sym24`
  - `workers/dispatcher/harvest-5way-r953_sym24`

## Output

`workers/dispatcher/harvest-3way-r954_sym24/round-954/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

