# harvest-5way-r1127 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1127 ctrl_bpc |
|--------|--------|--------------:|
| x9gnM | fork-slaa-us-mmllm-claude-train-sym24-a97e5105-x9gnM | 2.3575 |
| wUluV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4730857d-wUluV | 2.3690 |
| p3nmr | origin/claude/train-sym24-f5eaadf9-p3nmr | 2.3704 |
| qw28Q | fork-joly-os-mmllm-claude-train-sym24-943a6369-qw28Q | 2.7532 |
| c2Oal | fork-SeniorCareMarket-mmllm-claude-train-sym24-4191fb51-c2Oal | 2.7555 |
| **mean** | | **2.5211** |
| **best** | | **2.3575** |

## Chain progression R1126 → R1127

Previous harvest: `workers/dispatcher/harvest-6way-r1126_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4762         | 2.5211         | +0.0449 |
| ctrl_bpc best  | 2.3597         | 2.3575         | -0.0022 |

## Per-round trajectory (best bird: x9gnM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1127 | 6496 | 2.3575 | +0.2534 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1126_sym24`
  - `workers/dispatcher/harvest-5way-r1126_sym24`

## Output

`workers/dispatcher/harvest-5way-r1127_sym24/round-1127/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

