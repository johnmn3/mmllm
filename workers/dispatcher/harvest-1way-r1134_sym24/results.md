# harvest-1way-r1134 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1134 ctrl_bpc |
|--------|--------|--------------:|
| T5myH | fork-joly-os-mmllm-claude-train-sym24-2d420276-T5myH | 2.7457 |
| **mean** | | **2.7457** |
| **best** | | **2.7457** |

## Chain progression R1133 → R1134

Previous harvest: `workers/dispatcher/harvest-8way-r1133_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4854         | 2.7457         | +0.2603 |
| ctrl_bpc best  | 2.3493         | 2.7457         | +0.3964 |

## Per-round trajectory (best bird: T5myH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1134 | 6308 | 2.7457 | +0.2158 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1133_sym24`

## Output

`workers/dispatcher/harvest-1way-r1134_sym24/round-1134/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

