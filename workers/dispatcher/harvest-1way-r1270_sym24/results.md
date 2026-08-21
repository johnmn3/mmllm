# harvest-1way-r1270 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1270 ctrl_bpc |
|--------|--------|--------------:|
| XTHCT | fork-joly-os-mmllm-claude-train-sym24-a19cb42e-XTHCT | 2.4272 |
| **mean** | | **2.4272** |
| **best** | | **2.4272** |

## Chain progression R1269 → R1270

Previous harvest: `workers/dispatcher/harvest-9way-r1269_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4298         | 2.4272         | -0.0026 |
| ctrl_bpc best  | 2.2426         | 2.4272         | +0.1846 |

## Per-round trajectory (best bird: XTHCT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1270 | 6889 | 2.4272 | +0.2209 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1269_sym24`

## Output

`workers/dispatcher/harvest-1way-r1270_sym24/round-1270/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

