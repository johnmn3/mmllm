# harvest-13way-r755 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R755 ctrl_bpc |
|--------|--------|--------------:|
| BphXz | fork-joly-os-mmllm-claude-train-sym24-a6af0e9a-BphXz | 3.3004 |
| A6Ubx | fork-SeniorCareMarket-mmllm-claude-train-sym24-4d9f6002-A6Ubx | 3.3058 |
| BTukE | fork-joly-os-mmllm-claude-train-sym24-91b366a7-BTukE | 3.3086 |
| 2cczP | origin/claude/train-sym24-d55f0ab5-2cczP | 3.3091 |
| azZ3V | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e4b62abc-azZ3V | 3.3104 |
| hr2M6 | origin/claude/train-sym24-1687d37c-hr2M6 | 3.3109 |
| XafTX | fork-slaa-us-mmllm-claude-train-sym24-a650e284-XafTX | 3.3115 |
| YBFuJ | fork-slaa-us-mmllm-claude-train-sym24-762736a0-YBFuJ | 3.3332 |
| QRm9s | fork-davidwuchn-mmllm-claude-train-sym24-62cdfc39-QRm9s | 3.3987 |
| bLrMH | fork-davidwuchn-mmllm-claude-train-sym24-93972904-bLrMH | 3.6680 |
| 4nlvx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-053674e7-4nlvx | 3.6704 |
| WyPYT | fork-joly-os-mmllm-claude-train-sym24-c5850e06-WyPYT | 3.6784 |
| 93Au9 | origin/claude/train-sym24-4cee1f5b-93Au9 | 3.6794 |
| **mean** | | **3.4296** |
| **best** | | **3.3004** |

## Chain progression R754 → R755

Previous harvest: `workers/dispatcher/harvest-6way-r754_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4219         | 3.4296         | +0.0077 |
| ctrl_bpc best  | 3.3056         | 3.3004         | -0.0052 |

## Per-round trajectory (best bird: BphXz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 755 | 6602 | 3.3004 | +0.6573 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r754_sym24`
  - `workers/dispatcher/harvest-6way-r754_sym24`

## Output

`workers/dispatcher/harvest-13way-r755_sym24/round-755/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

