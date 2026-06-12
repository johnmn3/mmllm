# harvest-4way-r654 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R654 ctrl_bpc |
|--------|--------|--------------:|
| 62kHx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c4afde83-62kHx | 4.1656 |
| DbVfp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e3c6e63d-DbVfp | 4.1777 |
| GfF4T | fork-joly-os-mmllm-claude-train-sym24-6805d57b-GfF4T | 4.1891 |
| 4prj5 | fork-davidwuchn-mmllm-claude-train-sym24-feffa3bb-4prj5 | 4.1950 |
| **mean** | | **4.1818** |
| **best** | | **4.1656** |

## Chain progression R653 → R654

Previous harvest: `workers/dispatcher/harvest-17way-r653_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.4032         | 4.1818         | -0.2214 |
| ctrl_bpc best  | 4.1705         | 4.1656         | -0.0049 |

## Per-round trajectory (best bird: 62kHx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 654 | 5343 | 4.1656 | +0.0677 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r653_sym24`

## Output

`workers/dispatcher/harvest-4way-r654_sym24/round-654/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

