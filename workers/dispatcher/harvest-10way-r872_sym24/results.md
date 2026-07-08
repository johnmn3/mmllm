# harvest-10way-r872 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R872 ctrl_bpc |
|--------|--------|--------------:|
| XP7ub | fork-SeniorCareMarket-mmllm-claude-train-sym24-40c2febf-XP7ub | 2.8667 |
| VYDJ6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b4a48380-VYDJ6 | 2.8674 |
| jCh6Y | fork-slaa-us-mmllm-claude-train-sym24-fcf97c0f-jCh6Y | 2.8687 |
| BVKfb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-84a7f8f3-BVKfb | 2.8688 |
| Kw15s | origin/claude/train-sym24-fa15bbc5-Kw15s | 2.8700 |
| u79vG | fork-joly-os-mmllm-claude-train-sym24-93a4abcc-u79vG | 2.8819 |
| EY5Mr | origin/claude/train-sym24-7bf530f4-EY5Mr | 2.8891 |
| S5ZgB | fork-joly-os-mmllm-claude-train-sym24-efddcf62-S5ZgB | 3.0268 |
| PVe6V | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9a96c8af-PVe6V | 3.2317 |
| ehZcy | fork-slaa-us-mmllm-claude-train-sym24-bfcb58c6-ehZcy | 3.2412 |
| **mean** | | **2.9612** |
| **best** | | **2.8667** |

## Chain progression R871 → R872

Previous harvest: `workers/dispatcher/harvest-5way-r871_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0090         | 2.9612         | -0.0478 |
| ctrl_bpc best  | 2.8608         | 2.8667         | +0.0059 |

## Per-round trajectory (best bird: XP7ub)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 872 | 6678 | 2.8667 | +0.3484 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r871_sym24`
  - `workers/dispatcher/harvest-5way-r871_sym24`

## Output

`workers/dispatcher/harvest-10way-r872_sym24/round-872/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

