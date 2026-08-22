# harvest-11way-r1286 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1286 ctrl_bpc |
|--------|--------|--------------:|
| v8gRp | fork-SeniorCareMarket-mmllm-claude-train-sym24-1bd7718d-v8gRp | 2.2176 |
| Ib2oM | fork-slaa-us-mmllm-claude-train-sym24-6a37478b-Ib2oM | 2.2207 |
| tgf7t | origin/claude/train-sym24-b4a03409-tgf7t | 2.2271 |
| GexzI | fork-joly-os-mmllm-claude-train-sym24-87cfa571-GexzI | 2.2316 |
| duQYt | fork-joly-os-mmllm-claude-train-sym24-2e225c99-duQYt | 2.2320 |
| DR6qZ | fork-joly-os-mmllm-claude-train-sym24-5c83837a-DR6qZ | 2.2321 |
| YzSoi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-50f381dd-YzSoi | 2.2347 |
| BsOlt | fork-slaa-us-mmllm-claude-train-sym24-29cf4d92-BsOlt | 2.4149 |
| o0tS1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-7013e965-o0tS1 | 2.6122 |
| AQv3d | origin/claude/train-sym24-0d83c876-AQv3d | 2.6130 |
| ikUs3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4889a9ed-ikUs3 | 2.6265 |
| **mean** | | **2.3511** |
| **best** | | **2.2176** |

## Chain progression R1285 → R1286

Previous harvest: `workers/dispatcher/harvest-5way-r1285_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3422         | 2.3511         | +0.0089 |
| ctrl_bpc best  | 2.2170         | 2.2176         | +0.0006 |

## Per-round trajectory (best bird: v8gRp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1286 | 5271 | 2.2176 | +0.2520 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1285_sym24`
  - `workers/dispatcher/harvest-5way-r1285_sym24`

## Output

`workers/dispatcher/harvest-11way-r1286_sym24/round-1286/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

