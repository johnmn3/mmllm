# harvest-1way-r1346 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1346 ctrl_bpc |
|--------|--------|--------------:|
| VOW3Q | fork-joly-os-mmllm-claude-train-sym24-18c9d8c1-VOW3Q | 3.2506 |
| **mean** | | **3.2506** |
| **best** | | **3.2506** |

## Chain progression R610 → R1346

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.2506         | +1.1134 |
| ctrl_bpc best  | 2.1268         | 3.2506         | +1.1238 |

## Per-round trajectory (best bird: VOW3Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1346 | 3830 | 3.2506 | +0.1033 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **80 steps** from 1 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1345_sym24`

## Output

`workers/dispatcher/harvest-1way-r1346_sym24/round-1346/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

