# harvest-8way-r748 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R748 ctrl_bpc |
|--------|--------|--------------:|
| x67Oj | fork-davidwuchn-mmllm-claude-train-sym24-2b64aba7-x67Oj | 3.3437 |
| qp715 | fork-joly-os-mmllm-claude-train-sym24-089b85f7-qp715 | 3.3452 |
| mkUjd | fork-slaa-us-mmllm-claude-train-sym24-8328f4ca-mkUjd | 3.3488 |
| NjIp5 | fork-davidwuchn-mmllm-claude-train-sym24-0135273f-NjIp5 | 3.3515 |
| c0fAT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-13734054-c0fAT | 3.3748 |
| tnq7X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6b730ae9-tnq7X | 3.3781 |
| 1FaHL | origin/claude/train-sym24-3153d8e1-1FaHL | 3.7242 |
| RR3uy | fork-slaa-us-mmllm-claude-train-sym24-f1d6d56a-RR3uy | 3.7297 |
| **mean** | | **3.4495** |
| **best** | | **3.3437** |

## Chain progression R747 → R748

Previous harvest: `workers/dispatcher/harvest-10way-r747_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5038         | 3.4495         | -0.0543 |
| ctrl_bpc best  | 3.3343         | 3.3437         | +0.0094 |

## Per-round trajectory (best bird: x67Oj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 748 | 6657 | 3.3437 | +0.3913 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r747_sym24`

## Output

`workers/dispatcher/harvest-8way-r748_sym24/round-748/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

