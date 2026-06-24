# harvest-9way-r757 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R757 ctrl_bpc |
|--------|--------|--------------:|
| RKapR | fork-slaa-us-mmllm-claude-train-sym24-2ba11a42-RKapR | 3.2940 |
| ZMwni | fork-joly-os-mmllm-claude-train-sym24-41604647-ZMwni | 3.2941 |
| srtec | fork-joly-os-mmllm-claude-train-sym24-abf2003b-srtec | 3.2979 |
| Q4tfg | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-64e32450-Q4tfg | 3.3011 |
| 6Y0CY | fork-davidwuchn-mmllm-claude-train-sym24-0b0949ed-6Y0CY | 3.3041 |
| LiTxe | origin/claude/train-sym24-f5ade697-LiTxe | 3.3044 |
| 0ZN5K | fork-davidwuchn-mmllm-claude-train-sym24-cc55a10b-0ZN5K | 3.3315 |
| WFLLU | fork-slaa-us-mmllm-claude-train-sym24-58128c71-WFLLU | 3.3332 |
| Cnf9D | fork-SeniorCareMarket-mmllm-claude-train-sym24-07824204-Cnf9D | 3.3994 |
| **mean** | | **3.3177** |
| **best** | | **3.2940** |

## Chain progression R756 → R757

Previous harvest: `workers/dispatcher/harvest-5way-r756_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4936         | 3.3177         | -0.1759 |
| ctrl_bpc best  | 3.3055         | 3.2940         | -0.0115 |

## Per-round trajectory (best bird: RKapR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 757 | 6428 | 3.2940 | +0.5164 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r756_sym24`
  - `workers/dispatcher/harvest-5way-r756_sym24`

## Output

`workers/dispatcher/harvest-9way-r757_sym24/round-757/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

