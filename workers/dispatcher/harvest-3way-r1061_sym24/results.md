# harvest-3way-r1061 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1061 ctrl_bpc |
|--------|--------|--------------:|
| xe71e | fork-slaa-us-mmllm-claude-train-sym24-e019bd4b-xe71e | 2.4906 |
| 7hntC | fork-joly-os-mmllm-claude-train-sym24-9994af28-7hntC | 2.4946 |
| BpHCz | fork-SeniorCareMarket-mmllm-claude-train-sym24-9da16164-BpHCz | 2.8590 |
| **mean** | | **2.6147** |
| **best** | | **2.4906** |

## Chain progression R1060 → R1061

Previous harvest: `workers/dispatcher/harvest-10way-r1060_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5517         | 2.6147         | +0.0630 |
| ctrl_bpc best  | 2.4603         | 2.4906         | +0.0303 |

## Per-round trajectory (best bird: xe71e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1061 | 5362 | 2.4906 | +0.1993 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1060_sym24`
  - `workers/dispatcher/harvest-7way-r1060_sym24`

## Output

`workers/dispatcher/harvest-3way-r1061_sym24/round-1061/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

