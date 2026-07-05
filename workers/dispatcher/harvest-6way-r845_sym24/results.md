# harvest-6way-r845 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R845 ctrl_bpc |
|--------|--------|--------------:|
| lKWuC | fork-slaa-us-mmllm-claude-train-sym24-8e114bda-lKWuC | 2.9493 |
| 7mzHY | fork-slaa-us-mmllm-claude-train-sym24-22175f3b-7mzHY | 3.0961 |
| t0b12 | fork-joly-os-mmllm-claude-train-sym24-a40888c9-t0b12 | 3.0965 |
| XRUT1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bd4531b6-XRUT1 | 3.1021 |
| OH2a7 | origin/claude/train-sym24-d971c400-OH2a7 | 3.1131 |
| 7i0TD | fork-SeniorCareMarket-mmllm-claude-train-sym24-32043435-7i0TD | 3.3190 |
| **mean** | | **3.1127** |
| **best** | | **2.9493** |

## Chain progression R844 → R845

Previous harvest: `workers/dispatcher/harvest-5way-r844_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1018         | 3.1127         | +0.0109 |
| ctrl_bpc best  | 2.9499         | 2.9493         | -0.0006 |

## Per-round trajectory (best bird: lKWuC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 845 | 3662 | 2.9493 | +0.2351 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r844_sym24`
  - `workers/dispatcher/harvest-5way-r844_sym24`

## Output

`workers/dispatcher/harvest-6way-r845_sym24/round-845/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

