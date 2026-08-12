# harvest-2way-r1178 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1178 ctrl_bpc |
|--------|--------|--------------:|
| gjN5c | fork-joly-os-mmllm-claude-train-sym24-5c332205-gjN5c | 2.3124 |
| vLaCx | origin/claude/train-sym24-188d6cfc-vLaCx | 2.3259 |
| **mean** | | **2.3191** |
| **best** | | **2.3124** |

## Chain progression R1177 → R1178

Previous harvest: `workers/dispatcher/harvest-12way-r1177_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4429         | 2.3191         | -0.1238 |
| ctrl_bpc best  | 2.3020         | 2.3124         | +0.0104 |

## Per-round trajectory (best bird: gjN5c)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1178 | 6588 | 2.3124 | +0.2644 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1177_sym24`

## Output

`workers/dispatcher/harvest-2way-r1178_sym24/round-1178/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

