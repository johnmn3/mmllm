# harvest-11way-r1299 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1299 ctrl_bpc |
|--------|--------|--------------:|
| LFr3i | fork-slaa-us-mmllm-claude-train-sym24-618bcce8-LFr3i | 3.6474 |
| ZATne | fork-joly-os-mmllm-claude-train-sym24-57a8d3f3-ZATne | 3.7226 |
| 5p5GV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2ee76928-5p5GV | 3.7478 |
| KBeXD | fork-SeniorCareMarket-mmllm-claude-train-sym24-6f07c9db-KBeXD | 3.7747 |
| glw65 | fork-joly-os-mmllm-claude-train-sym24-0bcad6af-glw65 | 3.7776 |
| d0KCs | fork-SeniorCareMarket-mmllm-claude-train-sym24-84fcfcc4-d0KCs | 3.7826 |
| 0kh1b | fork-slaa-us-mmllm-claude-train-sym24-b6e6d258-0kh1b | 4.0295 |
| PBy06 | origin/claude/train-sym24-df28a7e6-PBy06 | 4.0746 |
| ohzL0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5eabe5a9-ohzL0 | 4.0746 |
| ZEMvU | fork-joly-os-mmllm-claude-train-sym24-f82d44f3-ZEMvU | 4.1153 |
| XLCdL | origin/claude/train-sym24-226ef472-XLCdL | 4.2850 |
| **mean** | | **3.9120** |
| **best** | | **3.6474** |

## Chain progression R1298 → R1299

Previous harvest: `workers/dispatcher/harvest-6way-r1298_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9602         | 3.9120         | -0.0482 |
| ctrl_bpc best  | 3.7278         | 3.6474         | -0.0804 |

## Per-round trajectory (best bird: LFr3i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1299 | 6514 | 3.6474 | +0.0461 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1298_sym24`
  - `workers/dispatcher/harvest-6way-r1298_sym24`

## Output

`workers/dispatcher/harvest-11way-r1299_sym24/round-1299/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

