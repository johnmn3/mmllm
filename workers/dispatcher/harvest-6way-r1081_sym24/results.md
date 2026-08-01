# harvest-6way-r1081 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1081 ctrl_bpc |
|--------|--------|--------------:|
| 3AylK | fork-slaa-us-mmllm-claude-train-sym24-fa0dbced-3AylK | 2.4487 |
| NDG3j | origin/claude/train-sym24-58db97a6-NDG3j | 2.4546 |
| G9Ev2 | fork-joly-os-mmllm-claude-train-sym24-5421d6f9-G9Ev2 | 2.4636 |
| 8IqnJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-d7678223-8IqnJ | 2.6168 |
| 2NX30 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6efde84e-2NX30 | 2.8244 |
| OTDYX | origin/claude/train-sym24-96e51b49-OTDYX | 2.8277 |
| **mean** | | **2.6060** |
| **best** | | **2.4487** |

## Chain progression R1080 → R1081

Previous harvest: `workers/dispatcher/harvest-3way-r1080_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4412         | 2.6060         | +0.1648 |
| ctrl_bpc best  | 2.4335         | 2.4487         | +0.0152 |

## Per-round trajectory (best bird: 3AylK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1081 | 6945 | 2.4487 | +0.2219 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1080_sym24`
  - `workers/dispatcher/harvest-3way-r1080_sym24`

## Output

`workers/dispatcher/harvest-6way-r1081_sym24/round-1081/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

