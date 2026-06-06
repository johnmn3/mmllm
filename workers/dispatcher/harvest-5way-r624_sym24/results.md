# harvest-5way-r624 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R624 ctrl_bpc |
|--------|--------|--------------:|
| CmZ1o | origin/claude/train-sym24-fd1719c3-CmZ1o | 2.1385 |
| DDhc6 | fork-davidwuchn-mmllm-claude-train-sym24-b950e5fd-DDhc6 | 2.1427 |
| zwXnT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5779781b-zwXnT | 2.3329 |
| JCoil | fork-joly-os-mmllm-claude-train-sym24-d9bdd04d-JCoil | 2.3344 |
| ur4uO | fork-slaa-us-mmllm-claude-train-sym24-1cc8789a-ur4uO | 2.5888 |
| **mean** | | **2.3075** |
| **best** | | **2.1385** |

## Chain progression R623 → R624

Previous harvest: `workers/dispatcher/harvest-5way-r623_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3029         | 2.3075         | +0.0046 |
| ctrl_bpc best  | 2.1235         | 2.1385         | +0.0150 |

## Per-round trajectory (best bird: CmZ1o)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 624 | 5209 | 2.1385 | +0.0486 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **750 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r623_sym24`

## Output

`workers/dispatcher/harvest-5way-r624_sym24/round-624/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

