# harvest-1way-r1271 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1271 ctrl_bpc |
|--------|--------|--------------:|
| O0gll | fork-slaa-us-mmllm-claude-train-sym24-52f96a39-O0gll | 2.6232 |
| **mean** | | **2.6232** |
| **best** | | **2.6232** |

## Chain progression R1270 → R1271

Previous harvest: `workers/dispatcher/harvest-6way-r1270_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3007         | 2.6232         | +0.3225 |
| ctrl_bpc best  | 2.2241         | 2.6232         | +0.3991 |

## Per-round trajectory (best bird: O0gll)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1271 | 3785 | 2.6232 | +0.2275 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1270_sym24`

## Output

`workers/dispatcher/harvest-1way-r1271_sym24/round-1271/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

