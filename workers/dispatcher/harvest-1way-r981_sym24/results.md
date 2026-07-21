# harvest-1way-r981 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R981 ctrl_bpc |
|--------|--------|--------------:|
| DIENE | fork-joly-os-mmllm-claude-train-sym24-1a8b8918-DIENE | 2.9880 |
| **mean** | | **2.9880** |
| **best** | | **2.9880** |

## Chain progression R980 → R981

Previous harvest: `workers/dispatcher/harvest-4way-r980_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7536         | 2.9880         | +0.2344 |
| ctrl_bpc best  | 2.5967         | 2.9880         | +0.3913 |

## Per-round trajectory (best bird: DIENE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 981 | 3692 | 2.9880 | +0.1555 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r980_sym24`

## Output

`workers/dispatcher/harvest-1way-r981_sym24/round-981/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

