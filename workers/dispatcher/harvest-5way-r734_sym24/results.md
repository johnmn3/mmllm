# harvest-5way-r734 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R734 ctrl_bpc |
|--------|--------|--------------:|
| dnaE9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-04ab93ab-dnaE9 | 3.4465 |
| OCmS9 | fork-davidwuchn-mmllm-claude-train-sym24-b05a70e7-OCmS9 | 3.4771 |
| 5gQ4Y | fork-SeniorCareMarket-mmllm-claude-train-sym24-0160e3bb-5gQ4Y | 3.4800 |
| rbqSu | fork-joly-os-mmllm-claude-train-sym24-c0bf733e-rbqSu | 3.4900 |
| Cj6eQ | fork-slaa-us-mmllm-claude-train-sym24-156ae9cd-Cj6eQ | 3.5172 |
| **mean** | | **3.4822** |
| **best** | | **3.4465** |

## Chain progression R733 → R734

Previous harvest: `workers/dispatcher/harvest-16way-r733_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5398         | 3.4822         | -0.0576 |
| ctrl_bpc best  | 3.4157         | 3.4465         | +0.0308 |

## Per-round trajectory (best bird: dnaE9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 734 | 6506 | 3.4465 | +0.5269 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r733_sym24`

## Output

`workers/dispatcher/harvest-5way-r734_sym24/round-734/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

