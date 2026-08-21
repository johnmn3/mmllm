# harvest-6way-r1272 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1272 ctrl_bpc |
|--------|--------|--------------:|
| nXxcg | fork-SeniorCareMarket-mmllm-claude-train-sym24-5f387702-nXxcg | 2.2399 |
| zhlkk | fork-SeniorCareMarket-mmllm-claude-train-sym24-2dfe40a1-zhlkk | 2.2484 |
| KFZWG | fork-joly-os-mmllm-claude-train-sym24-7a45a604-KFZWG | 2.2539 |
| GXVR1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5450744c-GXVR1 | 2.4213 |
| VMgZr | fork-slaa-us-mmllm-claude-train-sym24-7ac7725a-VMgZr | 2.4310 |
| 2JR3A | origin/claude/train-sym24-250eff5e-2JR3A | 2.6137 |
| **mean** | | **2.3680** |
| **best** | | **2.2399** |

## Chain progression R1271 → R1272

Previous harvest: `workers/dispatcher/harvest-7way-r1271_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4325         | 2.3680         | -0.0645 |
| ctrl_bpc best  | 2.2257         | 2.2399         | +0.0142 |

## Per-round trajectory (best bird: nXxcg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1272 | 3812 | 2.2399 | +0.2450 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1271_sym24`
  - `workers/dispatcher/harvest-7way-r1271_sym24`

## Output

`workers/dispatcher/harvest-6way-r1272_sym24/round-1272/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

