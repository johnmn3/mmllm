# harvest-5way-r647 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R647 ctrl_bpc |
|--------|--------|--------------:|
| 81V0l | fork-joly-os-mmllm-claude-train-sym24-99c8f15e-81V0l | 4.4195 |
| sKKL1 | fork-davidwuchn-mmllm-claude-train-sym24-8489bf82-sKKL1 | 4.4305 |
| 9Li2m | origin/claude/train-sym24-7a267598-9Li2m | 4.4509 |
| X8Ptk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-375e376c-X8Ptk | 4.4929 |
| gKnre | fork-slaa-us-mmllm-claude-train-sym24-bf6dcc68-gKnre | 4.8705 |
| **mean** | | **4.5329** |
| **best** | | **4.4195** |

## Chain progression R646 → R647

Previous harvest: `workers/dispatcher/harvest-1way-r646_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.9277         | 4.5329         | -0.3948 |
| ctrl_bpc best  | 4.9277         | 4.4195         | -0.5082 |

## Per-round trajectory (best bird: 81V0l)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 647 | 6496 | 4.4195 | +0.0540 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r646_sym24`

## Output

`workers/dispatcher/harvest-5way-r647_sym24/round-647/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

