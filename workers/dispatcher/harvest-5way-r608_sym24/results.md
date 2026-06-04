# harvest-5way-r608 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R608 ctrl_bpc |
|--------|--------|--------------:|
| PdY42 | fork-slaa-us-mmllm-claude-train-sym24-a4f6efb5-PdY42 | 2.1478 |
| 9dMdV | origin/claude/train-sym24-638732a4-9dMdV | 2.3551 |
| dZsz4 | fork-joly-os-mmllm-claude-train-sym24-0424e681-dZsz4 | 2.3597 |
| qUnCg | fork-davidwuchn-mmllm-claude-train-sym24-265b68a5-qUnCg | 2.6109 |
| UfhtZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3780b8d5-UfhtZ | 2.6133 |
| **mean** | | **2.4174** |
| **best** | | **2.1478** |

## Chain progression R607 → R608

Previous harvest: `workers/dispatcher/harvest-2way-merge-r607_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1495         | 2.4174         | +0.2678 |
| ctrl_bpc best  | 2.1266         | 2.1478         | +0.0212 |

## Per-round trajectory (best bird: PdY42)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 608 | 4518 | 2.1478 | +0.0201 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **250 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-merge-r607_sym24`

## Output

`workers/dispatcher/harvest-5way-r608_sym24/round-608/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

