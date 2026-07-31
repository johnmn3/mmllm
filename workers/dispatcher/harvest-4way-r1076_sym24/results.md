# harvest-4way-r1076 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1076 ctrl_bpc |
|--------|--------|--------------:|
| ggXfZ | origin/claude/train-sym24-7daa7cf2-ggXfZ | 2.4349 |
| avNbf | fork-slaa-us-mmllm-claude-train-sym24-1e487d48-avNbf | 2.4669 |
| SNar5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-72c84eb0-SNar5 | 2.4678 |
| kTXDI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-00ae94fc-kTXDI | 2.6174 |
| **mean** | | **2.4968** |
| **best** | | **2.4349** |

## Chain progression R1075 → R1076

Previous harvest: `workers/dispatcher/harvest-9way-r1075_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5905         | 2.4968         | -0.0938 |
| ctrl_bpc best  | 2.4375         | 2.4349         | -0.0026 |

## Per-round trajectory (best bird: ggXfZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1076 | 6741 | 2.4349 | +0.2332 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1075_sym24`
  - `workers/dispatcher/harvest-7way-r1075_sym24`

## Output

`workers/dispatcher/harvest-4way-r1076_sym24/round-1076/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

