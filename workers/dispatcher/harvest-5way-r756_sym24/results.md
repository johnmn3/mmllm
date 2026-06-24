# harvest-5way-r756 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R756 ctrl_bpc |
|--------|--------|--------------:|
| 62tyg | fork-slaa-us-mmllm-claude-train-sym24-e402818a-62tyg | 3.3055 |
| vjO5U | fork-davidwuchn-mmllm-claude-train-sym24-a41274ad-vjO5U | 3.4029 |
| QezR1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-be7f82db-QezR1 | 3.4055 |
| oq34c | fork-joly-os-mmllm-claude-train-sym24-ce3e39ca-oq34c | 3.6679 |
| ONmhc | fork-joly-os-mmllm-claude-train-sym24-8d387438-ONmhc | 3.6862 |
| **mean** | | **3.4936** |
| **best** | | **3.3055** |

## Chain progression R755 → R756

Previous harvest: `workers/dispatcher/harvest-13way-r755_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4296         | 3.4936         | +0.0640 |
| ctrl_bpc best  | 3.3004         | 3.3055         | +0.0051 |

## Per-round trajectory (best bird: 62tyg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 756 | 6516 | 3.3055 | +0.7828 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r755_sym24`

## Output

`workers/dispatcher/harvest-5way-r756_sym24/round-756/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

