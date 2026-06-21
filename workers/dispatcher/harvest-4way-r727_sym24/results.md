# harvest-4way-r727 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R727 ctrl_bpc |
|--------|--------|--------------:|
| GRmz7 | fork-slaa-us-mmllm-claude-train-sym24-28b432bc-GRmz7 | 3.4963 |
| z2eEO | fork-davidwuchn-mmllm-claude-train-sym24-7a7b9801-z2eEO | 3.5102 |
| KNYNK | fork-joly-os-mmllm-claude-train-sym24-a613303f-KNYNK | 3.8013 |
| 49V20 | fork-SeniorCareMarket-mmllm-claude-train-sym24-d6a9b9a0-49V20 | 3.8074 |
| **mean** | | **3.6538** |
| **best** | | **3.4963** |

## Chain progression R726 → R727

Previous harvest: `workers/dispatcher/harvest-16way-r726_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5848         | 3.6538         | +0.0690 |
| ctrl_bpc best  | 3.4616         | 3.4963         | +0.0347 |

## Per-round trajectory (best bird: GRmz7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 727 | 6526 | 3.4963 | +1.0183 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r726_sym24`
  - `workers/dispatcher/harvest-3way-r726_sym24`

## Output

`workers/dispatcher/harvest-4way-r727_sym24/round-727/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

