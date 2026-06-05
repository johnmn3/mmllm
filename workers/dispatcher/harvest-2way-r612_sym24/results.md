# harvest-2way-r612 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R612 ctrl_bpc |
|--------|--------|--------------:|
| P7DQG | fork-joly-os-mmllm-claude-train-sym24-44e715d5-P7DQG | 2.6027 |
| lle4Y | fork-davidwuchn-mmllm-claude-train-sym24-dbaec8dc-lle4Y | 2.6048 |
| **mean** | | **2.6037** |
| **best** | | **2.6027** |

## Chain progression R611 → R612

Previous harvest: `workers/dispatcher/harvest-4way-r611_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4219         | 2.6037         | +0.1818 |
| ctrl_bpc best  | 2.1281         | 2.6027         | +0.4746 |

## Per-round trajectory (best bird: P7DQG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 612 | 5352 | 2.6027 | +0.0215 |

## Cumulative training contribution

- This harvest: **100 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **300 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r611_sym24`

## Output

`workers/dispatcher/harvest-2way-r612_sym24/round-612/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

