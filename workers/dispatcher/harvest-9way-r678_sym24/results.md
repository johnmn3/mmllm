# harvest-9way-r678 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R678 ctrl_bpc |
|--------|--------|--------------:|
| vzGg6 | fork-davidwuchn-mmllm-claude-train-sym24-dc2466b5-vzGg6 | 3.7932 |
| DVpLD | fork-slaa-us-mmllm-claude-train-sym24-3e66e3b0-DVpLD | 3.8350 |
| qAmvB | fork-joly-os-mmllm-claude-train-sym24-5987684b-qAmvB | 3.8515 |
| jyKoy | fork-SeniorCareMarket-mmllm-claude-train-sym24-d70fb3db-jyKoy | 3.8528 |
| 3AjpB | origin/claude/train-sym24-65eae54d-3AjpB | 3.8717 |
| tO6dk | origin/claude/train-sym24-d3f9a54d-tO6dk | 3.9135 |
| gyKTr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c0ff045a-gyKTr | 4.1263 |
| uYzq6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1a991435-uYzq6 | 4.1376 |
| XmmU8 | fork-slaa-us-mmllm-claude-train-sym24-2b403000-XmmU8 | 4.1517 |
| **mean** | | **3.9481** |
| **best** | | **3.7932** |

## Chain progression R677 → R678

Previous harvest: `workers/dispatcher/harvest-8way-r677_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9321         | 3.9481         | +0.0160 |
| ctrl_bpc best  | 3.8053         | 3.7932         | -0.0121 |

## Per-round trajectory (best bird: vzGg6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 678 | 6461 | 3.7932 | +0.4814 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r677_sym24`

## Output

`workers/dispatcher/harvest-9way-r678_sym24/round-678/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

