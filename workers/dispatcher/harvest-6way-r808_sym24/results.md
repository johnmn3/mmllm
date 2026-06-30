# harvest-6way-r808 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R808 ctrl_bpc |
|--------|--------|--------------:|
| thGsy | fork-joly-os-mmllm-claude-train-sym24-ed8d575d-thGsy | 3.1938 |
| 9S9w4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4d30f09a-9S9w4 | 3.1951 |
| o866j | fork-slaa-us-mmllm-claude-train-sym24-5cbcf364-o866j | 3.2082 |
| qO11g | origin/claude/train-sym24-75f2ecef-qO11g | 3.4397 |
| JA85m | fork-davidwuchn-mmllm-claude-train-sym24-05d43cdc-JA85m | 3.4453 |
| 1tCMW | fork-SeniorCareMarket-mmllm-claude-train-sym24-256559c8-1tCMW | 3.4456 |
| **mean** | | **3.3213** |
| **best** | | **3.1938** |

## Chain progression R807 → R808

Previous harvest: `workers/dispatcher/harvest-8way-r807_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2212         | 3.3213         | +0.1001 |
| ctrl_bpc best  | 3.0814         | 3.1938         | +0.1124 |

## Per-round trajectory (best bird: thGsy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 808 | 6564 | 3.1938 | +0.4695 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r807_sym24`
  - `workers/dispatcher/harvest-5way-r807_sym24`

## Output

`workers/dispatcher/harvest-6way-r808_sym24/round-808/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

