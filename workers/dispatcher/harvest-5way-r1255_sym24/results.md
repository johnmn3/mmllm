# harvest-5way-r1255 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1255 ctrl_bpc |
|--------|--------|--------------:|
| rkoA7 | fork-joly-os-mmllm-claude-train-sym24-d3f33f51-rkoA7 | 2.2357 |
| NY2mq | fork-SeniorCareMarket-mmllm-claude-train-sym24-6e331ddd-NY2mq | 2.2391 |
| NcRMf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5a45fbb9-NcRMf | 2.4437 |
| xqdIF | fork-slaa-us-mmllm-claude-train-sym24-33548e6c-xqdIF | 2.4480 |
| NU6DV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c10d3b6e-NU6DV | 2.6311 |
| **mean** | | **2.3995** |
| **best** | | **2.2357** |

## Chain progression R1254 → R1255

Previous harvest: `workers/dispatcher/harvest-6way-r1254_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5481         | 2.3995         | -0.1486 |
| ctrl_bpc best  | 2.2375         | 2.2357         | -0.0018 |

## Per-round trajectory (best bird: rkoA7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1255 | 3591 | 2.2357 | +0.2443 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1254_sym24`
  - `workers/dispatcher/harvest-6way-r1254_sym24`

## Output

`workers/dispatcher/harvest-5way-r1255_sym24/round-1255/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

