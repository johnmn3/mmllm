# harvest-10way-r1298 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1298 ctrl_bpc |
|--------|--------|--------------:|
| ZjyS4 | fork-joly-os-mmllm-claude-train-sym24-b137e624-ZjyS4 | 3.7278 |
| LEzNg | fork-joly-os-mmllm-claude-train-sym24-dce01ef4-LEzNg | 3.7326 |
| Bvd9G | origin/claude/train-sym24-8138019a-Bvd9G | 3.8130 |
| UoYPA | fork-SeniorCareMarket-mmllm-claude-train-sym24-14881dbf-UoYPA | 3.8372 |
| mdHoJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-8e9b9f4b-mdHoJ | 3.8379 |
| EkeCj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cf420bb2-EkeCj | 4.1664 |
| qS1h8 | origin/claude/train-sym24-f6098fea-qS1h8 | 4.2938 |
| 782db | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-018e40e7-782db | 4.4698 |
| oOmAN | fork-slaa-us-mmllm-claude-train-sym24-84e4971b-oOmAN | 4.4771 |
| UPXpt | fork-slaa-us-mmllm-claude-train-sym24-2e008f9d-UPXpt | 4.4834 |
| **mean** | | **4.0839** |
| **best** | | **3.7278** |

## Chain progression R1297 → R1298

Previous harvest: `workers/dispatcher/harvest-6way-r1297_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1029         | 4.0839         | -0.0190 |
| ctrl_bpc best  | 3.8331         | 3.7278         | -0.1053 |

## Per-round trajectory (best bird: ZjyS4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1298 | 5366 | 3.7278 | +0.0458 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1297_sym24`
  - `workers/dispatcher/harvest-6way-r1297_sym24`

## Output

`workers/dispatcher/harvest-10way-r1298_sym24/round-1298/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

