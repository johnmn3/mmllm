# harvest-13way-r782 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R782 ctrl_bpc |
|--------|--------|--------------:|
| rFys3 | fork-davidwuchn-mmllm-claude-train-sym24-f0dbba8f-rFys3 | 3.1850 |
| 01aMy | origin/claude/train-sym24-9616f23b-01aMy | 3.1891 |
| LpLqy | fork-slaa-us-mmllm-claude-train-sym24-d237e881-LpLqy | 3.2120 |
| zfou2 | fork-davidwuchn-mmllm-claude-train-sym24-d3551c32-zfou2 | 3.2139 |
| W3Ib5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0243172b-W3Ib5 | 3.2178 |
| Z46uk | fork-slaa-us-mmllm-claude-train-sym24-79be89bc-Z46uk | 3.2193 |
| MM8Rh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-89d6d7d4-MM8Rh | 3.2194 |
| 6ICuC | origin/claude/train-sym24-27939f7f-6ICuC | 3.3053 |
| hl6Ym | fork-joly-os-mmllm-claude-train-sym24-b8d89b76-hl6Ym | 3.3061 |
| M56dS | origin/claude/train-sym24-f4e7d445-M56dS | 3.3296 |
| ISRrw | fork-joly-os-mmllm-claude-train-sym24-11637ad9-ISRrw | 3.5708 |
| cIckA | fork-SeniorCareMarket-mmllm-claude-train-sym24-b6ce4f53-cIckA | 3.5774 |
| oE16Y | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c2d575d0-oE16Y | 3.5830 |
| **mean** | | **3.3176** |
| **best** | | **3.1850** |

## Chain progression R781 → R782

Previous harvest: `workers/dispatcher/harvest-7way-r781_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2746         | 3.3176         | +0.0430 |
| ctrl_bpc best  | 3.1777         | 3.1850         | +0.0073 |

## Per-round trajectory (best bird: rFys3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 782 | 6569 | 3.1850 | +0.5944 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r781_sym24`
  - `workers/dispatcher/harvest-7way-r781_sym24`

## Output

`workers/dispatcher/harvest-13way-r782_sym24/round-782/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

