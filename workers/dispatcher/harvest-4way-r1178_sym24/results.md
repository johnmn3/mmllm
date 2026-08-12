# harvest-4way-r1178 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1178 ctrl_bpc |
|--------|--------|--------------:|
| l6f61 | fork-slaa-us-mmllm-claude-train-sym24-580f2c50-l6f61 | 2.3074 |
| gjN5c | fork-joly-os-mmllm-claude-train-sym24-5c332205-gjN5c | 2.3124 |
| vLaCx | origin/claude/train-sym24-188d6cfc-vLaCx | 2.3259 |
| UKEyC | origin/claude/train-sym24-07e3d9ed-UKEyC | 2.3473 |
| **mean** | | **2.3232** |
| **best** | | **2.3074** |

## Chain progression R1177 → R1178

Previous harvest: `workers/dispatcher/harvest-12way-r1177_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4429         | 2.3232         | -0.1197 |
| ctrl_bpc best  | 2.3020         | 2.3074         | +0.0054 |

## Per-round trajectory (best bird: l6f61)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1178 | 6342 | 2.3074 | +0.2534 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1177_sym24`

## Output

`workers/dispatcher/harvest-4way-r1178_sym24/round-1178/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

