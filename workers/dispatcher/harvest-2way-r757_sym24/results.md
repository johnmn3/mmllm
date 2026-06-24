# harvest-2way-r757 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R757 ctrl_bpc |
|--------|--------|--------------:|
| RKapR | fork-slaa-us-mmllm-claude-train-sym24-2ba11a42-RKapR | 3.2940 |
| ZMwni | fork-joly-os-mmllm-claude-train-sym24-41604647-ZMwni | 3.2941 |
| **mean** | | **3.2940** |
| **best** | | **3.2940** |

## Chain progression R756 → R757

Previous harvest: `workers/dispatcher/harvest-10way-r756_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4466         | 3.2940         | -0.1526 |
| ctrl_bpc best  | 3.2952         | 3.2940         | -0.0012 |

## Per-round trajectory (best bird: RKapR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 757 | 6428 | 3.2940 | +0.5164 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r756_sym24`

## Output

`workers/dispatcher/harvest-2way-r757_sym24/round-757/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

