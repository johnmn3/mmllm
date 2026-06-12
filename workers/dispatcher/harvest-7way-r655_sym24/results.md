# harvest-7way-r655 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R655 ctrl_bpc |
|--------|--------|--------------:|
| J1LhC | origin/claude/train-sym24-e747d256-J1LhC | 4.1119 |
| aPxHo | fork-SeniorCareMarket-mmllm-claude-train-sym24-f99668ed-aPxHo | 4.1141 |
| lqiVV | fork-joly-os-mmllm-claude-train-sym24-e6cd75c1-lqiVV | 4.1181 |
| CL5E6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-01b0bd8d-CL5E6 | 4.1313 |
| KgQBu | fork-slaa-us-mmllm-claude-train-sym24-3be8e61f-KgQBu | 4.1465 |
| seq37 | fork-joly-os-mmllm-claude-train-sym24-611599c2-seq37 | 4.1737 |
| ifbbM | fork-davidwuchn-mmllm-claude-train-sym24-bc2b586f-ifbbM | 4.4960 |
| **mean** | | **4.1845** |
| **best** | | **4.1119** |

## Chain progression R654 → R655

Previous harvest: `workers/dispatcher/harvest-4way-r654_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1818         | 4.1845         | +0.0027 |
| ctrl_bpc best  | 4.1656         | 4.1119         | -0.0537 |

## Per-round trajectory (best bird: J1LhC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 655 | 4280 | 4.1119 | +0.0365 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r654_sym24`
  - `workers/dispatcher/harvest-4way-r654_sym24`

## Output

`workers/dispatcher/harvest-7way-r655_sym24/round-655/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

