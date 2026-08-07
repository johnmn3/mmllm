# harvest-6way-r1128 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1128 ctrl_bpc |
|--------|--------|--------------:|
| 4vXPW | origin/claude/train-sym24-bea47d2b-4vXPW | 2.3548 |
| AY5Wk | origin/claude/train-sym24-c7b0845c-AY5Wk | 2.3651 |
| 0AI7e | fork-SeniorCareMarket-mmllm-claude-train-sym24-75d32c75-0AI7e | 2.3668 |
| xo6uI | fork-joly-os-mmllm-claude-train-sym24-ff42287d-xo6uI | 2.5605 |
| fAn1C | origin/claude/train-sym24-45085100-fAn1C | 2.7520 |
| KHjm0 | fork-slaa-us-mmllm-claude-train-sym24-9294594b-KHjm0 | 2.7634 |
| **mean** | | **2.5271** |
| **best** | | **2.3548** |

## Chain progression R1127 → R1128

Previous harvest: `workers/dispatcher/harvest-5way-r1127_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5211         | 2.5271         | +0.0060 |
| ctrl_bpc best  | 2.3575         | 2.3548         | -0.0027 |

## Per-round trajectory (best bird: 4vXPW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1128 | 3956 | 2.3548 | +0.2537 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1127_sym24`
  - `workers/dispatcher/harvest-5way-r1127_sym24`

## Output

`workers/dispatcher/harvest-6way-r1128_sym24/round-1128/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

