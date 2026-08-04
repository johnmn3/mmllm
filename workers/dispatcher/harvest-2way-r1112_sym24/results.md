# harvest-2way-r1112 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1112 ctrl_bpc |
|--------|--------|--------------:|
| 6LZbt | fork-slaa-us-mmllm-claude-train-sym24-fc1b03de-6LZbt | 2.3913 |
| C5fuC | fork-joly-os-mmllm-claude-train-sym24-faa52fdb-C5fuC | 2.3980 |
| **mean** | | **2.3947** |
| **best** | | **2.3913** |

## Chain progression R1111 → R1112

Previous harvest: `workers/dispatcher/harvest-7way-r1111_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6122         | 2.3947         | -0.2175 |
| ctrl_bpc best  | 2.3767         | 2.3913         | +0.0146 |

## Per-round trajectory (best bird: 6LZbt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1112 | 6359 | 2.3913 | +0.2287 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1111_sym24`

## Output

`workers/dispatcher/harvest-2way-r1112_sym24/round-1112/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

