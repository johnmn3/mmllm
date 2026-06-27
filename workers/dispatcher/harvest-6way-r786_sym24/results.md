# harvest-6way-r786 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R786 ctrl_bpc |
|--------|--------|--------------:|
| Bvd9y | origin/claude/train-sym24-7fb8a613-Bvd9y | 3.1602 |
| 5OR6G | fork-davidwuchn-mmllm-claude-train-sym24-87cc6520-5OR6G | 3.1623 |
| TdnfK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f12c70f-TdnfK | 3.1866 |
| CPqsv | fork-slaa-us-mmllm-claude-train-sym24-da8dda98-CPqsv | 3.2388 |
| Q7USx | fork-SeniorCareMarket-mmllm-claude-train-sym24-640bc4ad-Q7USx | 3.2914 |
| 0mkLn | fork-joly-os-mmllm-claude-train-sym24-8ef57532-0mkLn | 3.3023 |
| **mean** | | **3.2236** |
| **best** | | **3.1602** |

## Chain progression R785 → R786

Previous harvest: `workers/dispatcher/harvest-5way-r785_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3430         | 3.2236         | -0.1194 |
| ctrl_bpc best  | 3.1653         | 3.1602         | -0.0051 |

## Per-round trajectory (best bird: Bvd9y)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 786 | 4347 | 3.1602 | +0.5172 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r785_sym24`

## Output

`workers/dispatcher/harvest-6way-r786_sym24/round-786/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

