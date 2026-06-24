# harvest-4way-r756 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R756 ctrl_bpc |
|--------|--------|--------------:|
| 62tyg | fork-slaa-us-mmllm-claude-train-sym24-e402818a-62tyg | 3.3055 |
| vjO5U | fork-davidwuchn-mmllm-claude-train-sym24-a41274ad-vjO5U | 3.4029 |
| oq34c | fork-joly-os-mmllm-claude-train-sym24-ce3e39ca-oq34c | 3.6679 |
| ONmhc | fork-joly-os-mmllm-claude-train-sym24-8d387438-ONmhc | 3.6862 |
| **mean** | | **3.5156** |
| **best** | | **3.3055** |

## Chain progression R755 → R756

Previous harvest: `workers/dispatcher/harvest-13way-r755_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4296         | 3.5156         | +0.0860 |
| ctrl_bpc best  | 3.3004         | 3.3055         | +0.0051 |

## Per-round trajectory (best bird: 62tyg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 756 | 6516 | 3.3055 | +0.7828 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r755_sym24`

## Output

`workers/dispatcher/harvest-4way-r756_sym24/round-756/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

