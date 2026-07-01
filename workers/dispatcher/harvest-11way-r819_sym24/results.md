# harvest-11way-r819 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R819 ctrl_bpc |
|--------|--------|--------------:|
| N77eD | origin/claude/train-sym24-2110b5ba-N77eD | 3.0247 |
| bqxoI | fork-davidwuchn-mmllm-claude-train-sym24-f07c7c38-bqxoI | 3.0377 |
| WCqIk | fork-SeniorCareMarket-mmllm-claude-train-sym24-47072ca1-WCqIk | 3.0507 |
| iMBtl | fork-joly-os-mmllm-claude-train-sym24-837490a8-iMBtl | 3.1649 |
| 2COaI | fork-slaa-us-mmllm-claude-train-sym24-ce3f5b99-2COaI | 3.1668 |
| 7QC1Q | fork-davidwuchn-mmllm-claude-train-sym24-b514ec61-7QC1Q | 3.1695 |
| 8eyet | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-096d4175-8eyet | 3.1697 |
| VlXeq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-79a0f6d4-VlXeq | 3.1745 |
| jL0Kr | origin/claude/train-sym24-37d7a00b-jL0Kr | 3.1753 |
| MMjJ7 | fork-joly-os-mmllm-claude-train-sym24-45c17a46-MMjJ7 | 3.3847 |
| b9aKV | fork-slaa-us-mmllm-claude-train-sym24-a3cda75e-b9aKV | 3.4041 |
| **mean** | | **3.1748** |
| **best** | | **3.0247** |

## Chain progression R818 → R819

Previous harvest: `workers/dispatcher/harvest-6way-r818_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1540         | 3.1748         | +0.0208 |
| ctrl_bpc best  | 3.0316         | 3.0247         | -0.0069 |

## Per-round trajectory (best bird: N77eD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 819 | 6660 | 3.0247 | +0.5511 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r818_sym24`
  - `workers/dispatcher/harvest-6way-r818_sym24`

## Output

`workers/dispatcher/harvest-11way-r819_sym24/round-819/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

