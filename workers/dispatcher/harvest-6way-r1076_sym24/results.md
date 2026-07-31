# harvest-6way-r1076 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1076 ctrl_bpc |
|--------|--------|--------------:|
| dEGol | fork-joly-os-mmllm-claude-train-sym24-038b84fc-dEGol | 2.4328 |
| ggXfZ | origin/claude/train-sym24-7daa7cf2-ggXfZ | 2.4349 |
| avNbf | fork-slaa-us-mmllm-claude-train-sym24-1e487d48-avNbf | 2.4669 |
| SNar5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-72c84eb0-SNar5 | 2.4678 |
| kTXDI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-00ae94fc-kTXDI | 2.6174 |
| GNmTB | origin/claude/train-sym24-6b30ac33-GNmTB | 2.8281 |
| **mean** | | **2.5413** |
| **best** | | **2.4328** |

## Chain progression R1075 → R1076

Previous harvest: `workers/dispatcher/harvest-9way-r1075_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5905         | 2.5413         | -0.0492 |
| ctrl_bpc best  | 2.4375         | 2.4328         | -0.0047 |

## Per-round trajectory (best bird: dEGol)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1076 | 6301 | 2.4328 | +0.2198 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1075_sym24`
  - `workers/dispatcher/harvest-7way-r1075_sym24`

## Output

`workers/dispatcher/harvest-6way-r1076_sym24/round-1076/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

