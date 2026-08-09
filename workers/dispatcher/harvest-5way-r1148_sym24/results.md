# harvest-5way-r1148 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1148 ctrl_bpc |
|--------|--------|--------------:|
| K8HkR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-84020dd6-K8HkR | 2.3408 |
| nPTGt | fork-slaa-us-mmllm-claude-train-sym24-a7791644-nPTGt | 2.3416 |
| CEtya | origin/claude/train-sym24-40742aec-CEtya | 2.3618 |
| SvNGw | fork-joly-os-mmllm-claude-train-sym24-1e656836-SvNGw | 2.3812 |
| iILm2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-4cf6be5e-iILm2 | 2.7320 |
| **mean** | | **2.4315** |
| **best** | | **2.3408** |

## Chain progression R1147 → R1148

Previous harvest: `workers/dispatcher/harvest-9way-r1147_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5859         | 2.4315         | -0.1544 |
| ctrl_bpc best  | 2.3595         | 2.3408         | -0.0187 |

## Per-round trajectory (best bird: K8HkR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1148 | 6526 | 2.3408 | +0.2484 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1147_sym24`
  - `workers/dispatcher/harvest-9way-r1147_sym24`

## Output

`workers/dispatcher/harvest-5way-r1148_sym24/round-1148/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

