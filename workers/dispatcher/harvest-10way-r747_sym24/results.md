# harvest-10way-r747 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R747 ctrl_bpc |
|--------|--------|--------------:|
| C49xn | fork-joly-os-mmllm-claude-train-sym24-a0f1bcf6-C49xn | 3.3343 |
| pVhaO | origin/claude/train-sym24-d993d0d5-pVhaO | 3.3517 |
| xxrFR | fork-joly-os-mmllm-claude-train-sym24-e60c833d-xxrFR | 3.3549 |
| 9Ef52 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b36c934d-9Ef52 | 3.3574 |
| qpyEC | fork-joly-os-mmllm-claude-train-sym24-5b65ecb7-qpyEC | 3.3769 |
| JIm8Z | fork-slaa-us-mmllm-claude-train-sym24-9cbc563a-JIm8Z | 3.4359 |
| zmR5X | fork-davidwuchn-mmllm-claude-train-sym24-b8d72c15-zmR5X | 3.6928 |
| 6n6SF | fork-davidwuchn-mmllm-claude-train-sym24-3e26ae01-6n6SF | 3.7052 |
| Rj5WI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6a2aa62e-Rj5WI | 3.7091 |
| P5DXU | origin/claude/train-sym24-9b956a82-P5DXU | 3.7196 |
| **mean** | | **3.5038** |
| **best** | | **3.3343** |

## Chain progression R746 → R747

Previous harvest: `workers/dispatcher/harvest-8way-r746_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4707         | 3.5038         | +0.0331 |
| ctrl_bpc best  | 3.3555         | 3.3343         | -0.0212 |

## Per-round trajectory (best bird: C49xn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 747 | 6510 | 3.3343 | +0.4978 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r746_sym24`
  - `workers/dispatcher/harvest-8way-r746_sym24`

## Output

`workers/dispatcher/harvest-10way-r747_sym24/round-747/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

