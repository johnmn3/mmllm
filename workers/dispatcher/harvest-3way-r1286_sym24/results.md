# harvest-3way-r1286 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1286 ctrl_bpc |
|--------|--------|--------------:|
| Ib2oM | fork-slaa-us-mmllm-claude-train-sym24-6a37478b-Ib2oM | 2.2207 |
| DR6qZ | fork-joly-os-mmllm-claude-train-sym24-5c83837a-DR6qZ | 2.2321 |
| YzSoi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-50f381dd-YzSoi | 2.2347 |
| **mean** | | **2.2292** |
| **best** | | **2.2207** |

## Chain progression R1285 → R1286

Previous harvest: `workers/dispatcher/harvest-5way-r1285_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3422         | 2.2292         | -0.1130 |
| ctrl_bpc best  | 2.2170         | 2.2207         | +0.0037 |

## Per-round trajectory (best bird: Ib2oM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1286 | 3834 | 2.2207 | +0.2611 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1285_sym24`

## Output

`workers/dispatcher/harvest-3way-r1286_sym24/round-1286/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

