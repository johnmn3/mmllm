# harvest-5way-r623 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R623 ctrl_bpc |
|--------|--------|--------------:|
| ikGkq | fork-joly-os-mmllm-claude-train-sym24-93b6143e-ikGkq | 2.1235 |
| I7FGA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-da548f9b-I7FGA | 2.1237 |
| XCFPb | origin/claude/train-sym24-55560885-XCFPb | 2.3355 |
| rvY89 | fork-davidwuchn-mmllm-claude-train-sym24-dbb0b6dc-rvY89 | 2.3388 |
| rjUQz | fork-slaa-us-mmllm-claude-train-sym24-6f7f40cd-rjUQz | 2.5932 |
| **mean** | | **2.3029** |
| **best** | | **2.1235** |

## Chain progression R622 → R623

Previous harvest: `workers/dispatcher/harvest-4way-r622_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3567         | 2.3029         | -0.0538 |
| ctrl_bpc best  | 2.1214         | 2.1235         | +0.0021 |

## Per-round trajectory (best bird: ikGkq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 623 | 5476 | 2.1235 | +0.0413 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **750 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r622_sym24`

## Output

`workers/dispatcher/harvest-5way-r623_sym24/round-623/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

