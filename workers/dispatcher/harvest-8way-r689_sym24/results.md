# harvest-8way-r689 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R689 ctrl_bpc |
|--------|--------|--------------:|
| O9wVK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7f9f8930-O9wVK | 3.7351 |
| Hjiey | fork-davidwuchn-mmllm-claude-train-sym24-8c2627c3-Hjiey | 3.7443 |
| D0xHh | fork-slaa-us-mmllm-claude-train-sym24-fe5d4c5c-D0xHh | 3.7494 |
| 1pBOw | fork-slaa-us-mmllm-claude-train-sym24-2a977cbb-1pBOw | 3.7605 |
| jshSa | fork-joly-os-mmllm-claude-train-sym24-abfa3491-jshSa | 3.7613 |
| fZZhV | fork-davidwuchn-mmllm-claude-train-sym24-adab9942-fZZhV | 3.7874 |
| Wgi49 | origin/claude/train-sym24-dc4f20c1-Wgi49 | 3.7894 |
| 1KnIa | fork-joly-os-mmllm-claude-train-sym24-2a5d4654-1KnIa | 3.8002 |
| **mean** | | **3.7660** |
| **best** | | **3.7351** |

## Chain progression R688 → R689

Previous harvest: `workers/dispatcher/harvest-11way-r688_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8158         | 3.7660         | -0.0498 |
| ctrl_bpc best  | 3.6959         | 3.7351         | +0.0392 |

## Per-round trajectory (best bird: O9wVK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 689 | 6484 | 3.7351 | +0.4759 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r688_sym24`
  - `workers/dispatcher/harvest-5way-r688_sym24`

## Output

`workers/dispatcher/harvest-8way-r689_sym24/round-689/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

