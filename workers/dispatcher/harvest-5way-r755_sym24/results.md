# harvest-5way-r755 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R755 ctrl_bpc |
|--------|--------|--------------:|
| BphXz | fork-joly-os-mmllm-claude-train-sym24-a6af0e9a-BphXz | 3.3004 |
| azZ3V | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e4b62abc-azZ3V | 3.3104 |
| hr2M6 | origin/claude/train-sym24-1687d37c-hr2M6 | 3.3109 |
| XafTX | fork-slaa-us-mmllm-claude-train-sym24-a650e284-XafTX | 3.3115 |
| bLrMH | fork-davidwuchn-mmllm-claude-train-sym24-93972904-bLrMH | 3.6680 |
| **mean** | | **3.3802** |
| **best** | | **3.3004** |

## Chain progression R754 → R755

Previous harvest: `workers/dispatcher/harvest-6way-r754_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4219         | 3.3802         | -0.0417 |
| ctrl_bpc best  | 3.3056         | 3.3004         | -0.0052 |

## Per-round trajectory (best bird: BphXz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 755 | 6602 | 3.3004 | +0.6573 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r754_sym24`

## Output

`workers/dispatcher/harvest-5way-r755_sym24/round-755/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

