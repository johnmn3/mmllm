# harvest-10way-r665 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R665 ctrl_bpc |
|--------|--------|--------------:|
| g6m8Y | fork-slaa-us-mmllm-claude-train-sym24-85abd1aa-g6m8Y | 3.9294 |
| 80vBv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65c20a86-80vBv | 3.9679 |
| m4wnp | fork-davidwuchn-mmllm-claude-train-sym24-105b59d1-m4wnp | 3.9683 |
| gUuW2 | origin/claude/train-sym24-f01c6016-gUuW2 | 3.9690 |
| tPQBh | fork-davidwuchn-mmllm-claude-train-sym24-0c27a493-tPQBh | 3.9725 |
| KC825 | fork-joly-os-mmllm-claude-train-sym24-d8745339-KC825 | 3.9818 |
| JGEpJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b923b65e-JGEpJ | 3.9964 |
| 3pisK | origin/claude/train-sym24-3f844fa4-3pisK | 4.2514 |
| eVx8J | fork-slaa-us-mmllm-claude-train-sym24-0565d755-eVx8J | 4.2750 |
| GWA1r | fork-joly-os-mmllm-claude-train-sym24-6613bc3b-GWA1r | 4.2896 |
| **mean** | | **4.0601** |
| **best** | | **3.9294** |

## Chain progression R664 → R665

Previous harvest: `workers/dispatcher/harvest-3way-r664_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9933         | 4.0601         | +0.0668 |
| ctrl_bpc best  | 3.9597         | 3.9294         | -0.0303 |

## Per-round trajectory (best bird: g6m8Y)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 665 | 4452 | 3.9294 | +0.2086 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r664_sym24`
  - `workers/dispatcher/harvest-3way-r664_sym24`

## Output

`workers/dispatcher/harvest-10way-r665_sym24/round-665/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

