# harvest-3way-r679 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R679 ctrl_bpc |
|--------|--------|--------------:|
| UyxTY | fork-davidwuchn-mmllm-claude-train-sym24-4aca478b-UyxTY | 3.8387 |
| 9nvp0 | fork-slaa-us-mmllm-claude-train-sym24-80f3a683-9nvp0 | 3.8476 |
| pCjR9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ae7a5920-pCjR9 | 4.1160 |
| **mean** | | **3.9341** |
| **best** | | **3.8387** |

## Chain progression R678 → R679

Previous harvest: `workers/dispatcher/harvest-9way-r678_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9481         | 3.9341         | -0.0140 |
| ctrl_bpc best  | 3.7932         | 3.8387         | +0.0455 |

## Per-round trajectory (best bird: UyxTY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 679 | 6333 | 3.8387 | +0.2802 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r678_sym24`

## Output

`workers/dispatcher/harvest-3way-r679_sym24/round-679/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

