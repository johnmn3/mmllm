# harvest-3way-r1092 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1092 ctrl_bpc |
|--------|--------|--------------:|
| COWdJ | fork-slaa-us-mmllm-claude-train-sym24-f5aac6bd-COWdJ | 2.4116 |
| NS0oK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-49c2e470-NS0oK | 2.6118 |
| oZgfW | fork-joly-os-mmllm-claude-train-sym24-7fbc1b07-oZgfW | 2.8158 |
| **mean** | | **2.6131** |
| **best** | | **2.4116** |

## Chain progression R1091 → R1092

Previous harvest: `workers/dispatcher/harvest-5way-r1091_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4916         | 2.6131         | +0.1215 |
| ctrl_bpc best  | 2.4054         | 2.4116         | +0.0062 |

## Per-round trajectory (best bird: COWdJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1092 | 6419 | 2.4116 | +0.2426 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1091_sym24`
  - `workers/dispatcher/harvest-5way-r1091_sym24`

## Output

`workers/dispatcher/harvest-3way-r1092_sym24/round-1092/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

