# harvest-6way-r985 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R985 ctrl_bpc |
|--------|--------|--------------:|
| 0lJBe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a76fab60-0lJBe | 2.6128 |
| KPhsb | origin/claude/train-sym24-b3d0c426-KPhsb | 2.6484 |
| hRLJy | fork-SeniorCareMarket-mmllm-claude-train-sym24-aa3a013f-hRLJy | 2.7739 |
| C4xKc | fork-joly-os-mmllm-claude-train-sym24-9211efa7-C4xKc | 2.7808 |
| GWIgD | fork-joly-os-mmllm-claude-train-sym24-fccb6878-GWIgD | 2.7883 |
| duQzS | fork-slaa-us-mmllm-claude-train-sym24-d32219dc-duQzS | 2.9648 |
| **mean** | | **2.7615** |
| **best** | | **2.6128** |

## Chain progression R984 → R985

Previous harvest: `workers/dispatcher/harvest-6way-r984_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7619         | 2.7615         | -0.0004 |
| ctrl_bpc best  | 2.5851         | 2.6128         | +0.0277 |

## Per-round trajectory (best bird: 0lJBe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 985 | 6455 | 2.6128 | +0.1407 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r984_sym24`
  - `workers/dispatcher/harvest-6way-r984_sym24`

## Output

`workers/dispatcher/harvest-6way-r985_sym24/round-985/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

