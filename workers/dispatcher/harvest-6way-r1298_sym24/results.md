# harvest-6way-r1298 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1298 ctrl_bpc |
|--------|--------|--------------:|
| ZjyS4 | fork-joly-os-mmllm-claude-train-sym24-b137e624-ZjyS4 | 3.7278 |
| LEzNg | fork-joly-os-mmllm-claude-train-sym24-dce01ef4-LEzNg | 3.7326 |
| Bvd9G | origin/claude/train-sym24-8138019a-Bvd9G | 3.8130 |
| mdHoJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-8e9b9f4b-mdHoJ | 3.8379 |
| EkeCj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cf420bb2-EkeCj | 4.1664 |
| UPXpt | fork-slaa-us-mmllm-claude-train-sym24-2e008f9d-UPXpt | 4.4834 |
| **mean** | | **3.9602** |
| **best** | | **3.7278** |

## Chain progression R1297 → R1298

Previous harvest: `workers/dispatcher/harvest-6way-r1297_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1029         | 3.9602         | -0.1427 |
| ctrl_bpc best  | 3.8331         | 3.7278         | -0.1053 |

## Per-round trajectory (best bird: ZjyS4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1298 | 5366 | 3.7278 | +0.0458 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1297_sym24`

## Output

`workers/dispatcher/harvest-6way-r1298_sym24/round-1298/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

