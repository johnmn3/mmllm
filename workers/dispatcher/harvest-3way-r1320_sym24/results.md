# harvest-3way-r1320 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1320 ctrl_bpc |
|--------|--------|--------------:|
| U6qgo | fork-slaa-us-mmllm-claude-train-sym24-265d61ba-U6qgo | 3.4712 |
| aH1cs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7332c7c0-aH1cs | 3.4733 |
| uUajn | fork-SeniorCareMarket-mmllm-claude-train-sym24-f01d6c76-uUajn | 3.5000 |
| **mean** | | **3.4815** |
| **best** | | **3.4712** |

## Chain progression R1319 → R1320

Previous harvest: `workers/dispatcher/harvest-4way-r1319_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5528         | 3.4815         | -0.0713 |
| ctrl_bpc best  | 3.4495         | 3.4712         | +0.0217 |

## Per-round trajectory (best bird: U6qgo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1320 | 6640 | 3.4712 | +0.0499 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1319_sym24`

## Output

`workers/dispatcher/harvest-3way-r1320_sym24/round-1320/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

