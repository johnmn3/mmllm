# harvest-13way-r608 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R608 ctrl_bpc |
|--------|--------|--------------:|
| nbzNC | fork-slaa-us-mmllm-claude-train-sym24-878daef6-nbzNC | 2.1476 |
| PdY42 | fork-slaa-us-mmllm-claude-train-sym24-a4f6efb5-PdY42 | 2.1478 |
| 4RAVU | fork-slaa-us-mmllm-claude-train-sym24-c50de121-4RAVU | 2.1479 |
| Po47t | fork-joly-os-mmllm-claude-train-sym24-feb5b542-Po47t | 2.1499 |
| oyHDl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7823d151-oyHDl | 2.3512 |
| OZ4bU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f51012d-OZ4bU | 2.3522 |
| JeDqc | fork-davidwuchn-mmllm-claude-train-sym24-9a553f1e-JeDqc | 2.3554 |
| dZsz4 | fork-joly-os-mmllm-claude-train-sym24-0424e681-dZsz4 | 2.3597 |
| nKdDu | fork-SeniorCareMarket-mmllm-claude-train-sym24-720b720b-nKdDu | 2.6071 |
| dE6Hx | fork-joly-os-mmllm-claude-train-sym24-cbb738f1-dE6Hx | 2.6071 |
| I33gp | fork-davidwuchn-mmllm-claude-train-sym24-5b268cc6-I33gp | 2.6082 |
| qUnCg | fork-davidwuchn-mmllm-claude-train-sym24-265b68a5-qUnCg | 2.6109 |
| UfhtZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3780b8d5-UfhtZ | 2.6133 |
| **mean** | | **2.3891** |
| **best** | | **2.1476** |

## Chain progression R607 → R608

Previous harvest: `workers/dispatcher/harvest-2way-merge-r607_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1495         | 2.3891         | +0.2396 |
| ctrl_bpc best  | 2.1266         | 2.1476         | +0.0210 |

## Per-round trajectory (best bird: nbzNC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 608 | 5466 | 2.1476 | +0.0206 |

## Cumulative training contribution

- This harvest: **650 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **650 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-merge-r607_sym24`

## Output

`workers/dispatcher/harvest-13way-r608_sym24/round-608/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

