# harvest-6way-r1286 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1286 ctrl_bpc |
|--------|--------|--------------:|
| Ib2oM | fork-slaa-us-mmllm-claude-train-sym24-6a37478b-Ib2oM | 2.2207 |
| tgf7t | origin/claude/train-sym24-b4a03409-tgf7t | 2.2271 |
| GexzI | fork-joly-os-mmllm-claude-train-sym24-87cfa571-GexzI | 2.2316 |
| DR6qZ | fork-joly-os-mmllm-claude-train-sym24-5c83837a-DR6qZ | 2.2321 |
| YzSoi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-50f381dd-YzSoi | 2.2347 |
| o0tS1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-7013e965-o0tS1 | 2.6122 |
| **mean** | | **2.2931** |
| **best** | | **2.2207** |

## Chain progression R1285 → R1286

Previous harvest: `workers/dispatcher/harvest-5way-r1285_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3422         | 2.2931         | -0.0491 |
| ctrl_bpc best  | 2.2170         | 2.2207         | +0.0037 |

## Per-round trajectory (best bird: Ib2oM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1286 | 3834 | 2.2207 | +0.2611 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1285_sym24`

## Output

`workers/dispatcher/harvest-6way-r1286_sym24/round-1286/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

