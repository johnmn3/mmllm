# harvest-6way-r1191 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1191 ctrl_bpc |
|--------|--------|--------------:|
| TiE19 | origin/claude/train-sym24-ffc2aaab-TiE19 | 2.3077 |
| w4CBh | origin/claude/train-sym24-551462cb-w4CBh | 2.4864 |
| yANRB | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3fda58e-yANRB | 2.4911 |
| knZfV | fork-joly-os-mmllm-claude-train-sym24-35475cf3-knZfV | 2.4951 |
| r2Hx6 | fork-slaa-us-mmllm-claude-train-sym24-3360166f-r2Hx6 | 2.6847 |
| Nf7nj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-27e3ff20-Nf7nj | 2.6916 |
| **mean** | | **2.5261** |
| **best** | | **2.3077** |

## Chain progression R1190 → R1191

Previous harvest: `workers/dispatcher/harvest-1way-r1190_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2908         | 2.5261         | +0.2353 |
| ctrl_bpc best  | 2.2908         | 2.3077         | +0.0169 |

## Per-round trajectory (best bird: TiE19)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1191 | 6701 | 2.3077 | +0.2449 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1190_sym24`

## Output

`workers/dispatcher/harvest-6way-r1191_sym24/round-1191/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

