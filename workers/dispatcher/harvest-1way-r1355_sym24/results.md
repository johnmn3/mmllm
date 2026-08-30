# harvest-1way-r1355 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1355 ctrl_bpc |
|--------|--------|--------------:|
| bvnn3 | fork-joly-os-mmllm-claude-train-sym24-0649fef9-bvnn3 | 3.2934 |
| **mean** | | **3.2934** |
| **best** | | **3.2934** |

## Chain progression R610 → R1355

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.2934         | +1.1562 |
| ctrl_bpc best  | 2.1268         | 3.2934         | +1.1666 |

## Per-round trajectory (best bird: bvnn3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1355 | 6834 | 3.2934 | +0.0863 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **80 steps** from 1 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1354_sym24`

## Output

`workers/dispatcher/harvest-1way-r1355_sym24/round-1355/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

