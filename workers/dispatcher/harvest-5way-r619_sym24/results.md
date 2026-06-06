# harvest-5way-r619 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R619 ctrl_bpc |
|--------|--------|--------------:|
| B721C | fork-slaa-us-mmllm-claude-train-sym24-aec4ab9a-B721C | 2.1229 |
| ktnA0 | fork-joly-os-mmllm-claude-train-sym24-67f8af3d-ktnA0 | 2.1447 |
| og6f4 | origin/claude/train-sym24-bc878a23-og6f4 | 2.3409 |
| uSkJz | fork-davidwuchn-mmllm-claude-train-sym24-2453093f-uSkJz | 2.3412 |
| qV0nB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7c4406d5-qV0nB | 2.5933 |
| **mean** | | **2.3086** |
| **best** | | **2.1229** |

## Chain progression R618 → R619

Previous harvest: `workers/dispatcher/harvest-6way-r618_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3246         | 2.3086         | -0.0160 |
| ctrl_bpc best  | 2.1206         | 2.1229         | +0.0023 |

## Per-round trajectory (best bird: B721C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 619 | 4478 | 2.1229 | +0.0349 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **750 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r618_sym24`

## Output

`workers/dispatcher/harvest-5way-r619_sym24/round-619/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

