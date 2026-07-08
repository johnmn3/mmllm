# harvest-7way-r872 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R872 ctrl_bpc |
|--------|--------|--------------:|
| VYDJ6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b4a48380-VYDJ6 | 2.8674 |
| jCh6Y | fork-slaa-us-mmllm-claude-train-sym24-fcf97c0f-jCh6Y | 2.8687 |
| BVKfb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-84a7f8f3-BVKfb | 2.8688 |
| Kw15s | origin/claude/train-sym24-fa15bbc5-Kw15s | 2.8700 |
| u79vG | fork-joly-os-mmllm-claude-train-sym24-93a4abcc-u79vG | 2.8819 |
| EY5Mr | origin/claude/train-sym24-7bf530f4-EY5Mr | 2.8891 |
| ehZcy | fork-slaa-us-mmllm-claude-train-sym24-bfcb58c6-ehZcy | 3.2412 |
| **mean** | | **2.9267** |
| **best** | | **2.8674** |

## Chain progression R871 → R872

Previous harvest: `workers/dispatcher/harvest-5way-r871_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0090         | 2.9267         | -0.0823 |
| ctrl_bpc best  | 2.8608         | 2.8674         | +0.0066 |

## Per-round trajectory (best bird: VYDJ6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 872 | 6495 | 2.8674 | +0.5558 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r871_sym24`
  - `workers/dispatcher/harvest-5way-r871_sym24`

## Output

`workers/dispatcher/harvest-7way-r872_sym24/round-872/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

