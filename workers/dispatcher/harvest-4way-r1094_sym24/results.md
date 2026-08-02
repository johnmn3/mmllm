# harvest-4way-r1094 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1094 ctrl_bpc |
|--------|--------|--------------:|
| 1Z3iM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31f8f239-1Z3iM | 2.4100 |
| NgZQa | origin/claude/train-sym24-87a68c48-NgZQa | 2.4224 |
| pG6mN | fork-joly-os-mmllm-claude-train-sym24-f7eab00e-pG6mN | 2.6000 |
| oOYiZ | fork-slaa-us-mmllm-claude-train-sym24-3886c770-oOYiZ | 2.8123 |
| **mean** | | **2.5612** |
| **best** | | **2.4100** |

## Chain progression R1093 → R1094

Previous harvest: `workers/dispatcher/harvest-8way-r1093_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6369         | 2.5612         | -0.0757 |
| ctrl_bpc best  | 2.4075         | 2.4100         | +0.0025 |

## Per-round trajectory (best bird: 1Z3iM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1094 | 6612 | 2.4100 | +0.2144 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1093_sym24`
  - `workers/dispatcher/harvest-2way-r1093_sym24`

## Output

`workers/dispatcher/harvest-4way-r1094_sym24/round-1094/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

