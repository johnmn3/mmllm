# harvest-3way-r1279 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1279 ctrl_bpc |
|--------|--------|--------------:|
| GLHLu | fork-joly-os-mmllm-claude-train-sym24-008b2f79-GLHLu | 2.2488 |
| 138rx | origin/claude/train-sym24-5e50caf7-138rx | 2.6136 |
| W3wrP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f89bca1-W3wrP | 2.6183 |
| **mean** | | **2.4936** |
| **best** | | **2.2488** |

## Chain progression R1278 → R1279

Previous harvest: `workers/dispatcher/harvest-6way-r1278_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2997         | 2.4936         | +0.1939 |
| ctrl_bpc best  | 2.2282         | 2.2488         | +0.0206 |

## Per-round trajectory (best bird: GLHLu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1279 | 3749 | 2.2488 | +0.2497 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1278_sym24`

## Output

`workers/dispatcher/harvest-3way-r1279_sym24/round-1279/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

