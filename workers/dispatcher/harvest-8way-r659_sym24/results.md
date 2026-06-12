# harvest-8way-r659 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R659 ctrl_bpc |
|--------|--------|--------------:|
| H8LGs | fork-davidwuchn-mmllm-claude-train-sym24-19f69dea-H8LGs | 4.0518 |
| En1Vi | fork-slaa-us-mmllm-claude-train-sym24-0e874734-En1Vi | 4.0547 |
| cplvV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4f7aa1f1-cplvV | 4.0684 |
| 0I0kU | origin/claude/train-sym24-289952cd-0I0kU | 4.0764 |
| HFjFf | fork-SeniorCareMarket-mmllm-claude-train-sym24-85a7a004-HFjFf | 4.0825 |
| nBfq2 | fork-joly-os-mmllm-claude-train-sym24-d375d677-nBfq2 | 4.1041 |
| pCoMy | origin/claude/train-sym24-3d7c986f-pCoMy | 4.4039 |
| PSt0n | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a78c7a4d-PSt0n | 4.4194 |
| **mean** | | **4.1577** |
| **best** | | **4.0518** |

## Chain progression R658 → R659

Previous harvest: `workers/dispatcher/harvest-6way-r658_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1495         | 4.1577         | +0.0082 |
| ctrl_bpc best  | 4.0878         | 4.0518         | -0.0360 |

## Per-round trajectory (best bird: H8LGs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 659 | 6481 | 4.0518 | +0.0384 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r658_sym24`
  - `workers/dispatcher/harvest-6way-r658_sym24`

## Output

`workers/dispatcher/harvest-8way-r659_sym24/round-659/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

