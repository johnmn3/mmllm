# harvest-2way-r1200 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1200 ctrl_bpc |
|--------|--------|--------------:|
| gOxmW | fork-joly-os-mmllm-claude-train-sym24-7bb1e216-gOxmW | 2.2881 |
| 7lLFm | origin/claude/train-sym24-e9bfdfa0-7lLFm | 2.6739 |
| **mean** | | **2.4810** |
| **best** | | **2.2881** |

## Chain progression R1199 → R1200

Previous harvest: `workers/dispatcher/harvest-3way-r1199_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4256         | 2.4810         | +0.0554 |
| ctrl_bpc best  | 2.2825         | 2.2881         | +0.0056 |

## Per-round trajectory (best bird: gOxmW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1200 | 6753 | 2.2881 | +0.2542 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1199_sym24`

## Output

`workers/dispatcher/harvest-2way-r1200_sym24/round-1200/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

