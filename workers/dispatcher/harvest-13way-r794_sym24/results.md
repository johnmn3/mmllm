# harvest-13way-r794 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R794 ctrl_bpc |
|--------|--------|--------------:|
| eQqYb | origin/claude/train-sym24-6cc73ef8-eQqYb | 3.1174 |
| MID40 | fork-joly-os-mmllm-claude-train-sym24-2283cb11-MID40 | 3.1226 |
| rrt9B | fork-SeniorCareMarket-mmllm-claude-train-sym24-05829b40-rrt9B | 3.1240 |
| ibyyj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d609607b-ibyyj | 3.1303 |
| pEEfK | fork-slaa-us-mmllm-claude-train-sym24-0920b25a-pEEfK | 3.1653 |
| kle0k | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0e4ed3e0-kle0k | 3.1674 |
| ICv0o | fork-slaa-us-mmllm-claude-train-sym24-676082c9-ICv0o | 3.1740 |
| 33xFj | fork-joly-os-mmllm-claude-train-sym24-dd079ed5-33xFj | 3.2568 |
| fGw91 | fork-davidwuchn-mmllm-claude-train-sym24-dbe356a7-fGw91 | 3.2620 |
| q0P1T | fork-joly-os-mmllm-claude-train-sym24-961ba47c-q0P1T | 3.5069 |
| jlAMt | fork-davidwuchn-mmllm-claude-train-sym24-bb857d20-jlAMt | 3.5183 |
| EYvqX | fork-slaa-us-mmllm-claude-train-sym24-0884a071-EYvqX | 3.5187 |
| QviG1 | origin/claude/train-sym24-fedd1d7e-QviG1 | 3.5204 |
| **mean** | | **3.2757** |
| **best** | | **3.1174** |

## Chain progression R793 → R794

Previous harvest: `workers/dispatcher/harvest-8way-r793_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3279         | 3.2757         | -0.0522 |
| ctrl_bpc best  | 3.1185         | 3.1174         | -0.0011 |

## Per-round trajectory (best bird: eQqYb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 794 | 6700 | 3.1174 | +0.5233 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-17way-r793_sym24`
  - `workers/dispatcher/harvest-5way-r793_sym24`
  - `workers/dispatcher/harvest-8way-r793_sym24`

## Output

`workers/dispatcher/harvest-13way-r794_sym24/round-794/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

