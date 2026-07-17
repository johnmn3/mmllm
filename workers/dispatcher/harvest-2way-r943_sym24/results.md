# harvest-2way-r943 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R943 ctrl_bpc |
|--------|--------|--------------:|
| gcHsN | origin/claude/train-sym24-dedd77e1-gcHsN | 2.6902 |
| LuRsn | fork-joly-os-mmllm-claude-train-sym24-392f1a8f-LuRsn | 3.0747 |
| **mean** | | **2.8824** |
| **best** | | **2.6902** |

## Chain progression R942 → R943

Previous harvest: `workers/dispatcher/harvest-2way-r942_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9839         | 2.8824         | -0.1015 |
| ctrl_bpc best  | 2.8853         | 2.6902         | -0.1951 |

## Per-round trajectory (best bird: gcHsN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 943 | 6330 | 2.6902 | +0.1593 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r942_sym24`

## Output

`workers/dispatcher/harvest-2way-r943_sym24/round-943/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

