# harvest-2way-r1179 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1179 ctrl_bpc |
|--------|--------|--------------:|
| 0OYhm | fork-joly-os-mmllm-claude-train-sym24-efd3422e-0OYhm | 2.3190 |
| RwNYZ | fork-slaa-us-mmllm-claude-train-sym24-5cfc8e91-RwNYZ | 2.7228 |
| **mean** | | **2.5209** |
| **best** | | **2.3190** |

## Chain progression R1178 → R1179

Previous harvest: `workers/dispatcher/harvest-6way-r1178_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4492         | 2.5209         | +0.0717 |
| ctrl_bpc best  | 2.3074         | 2.3190         | +0.0116 |

## Per-round trajectory (best bird: 0OYhm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1179 | 6521 | 2.3190 | +0.2545 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1178_sym24`
  - `workers/dispatcher/harvest-4way-r1178_sym24`

## Output

`workers/dispatcher/harvest-2way-r1179_sym24/round-1179/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

