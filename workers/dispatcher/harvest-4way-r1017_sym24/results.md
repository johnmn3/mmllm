# harvest-4way-r1017 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1017 ctrl_bpc |
|--------|--------|--------------:|
| 9WDnU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c7dd98ef-9WDnU | 2.5260 |
| HnchH | fork-SeniorCareMarket-mmllm-claude-train-sym24-6f53fb85-HnchH | 2.5483 |
| UPg0w | origin/claude/train-sym24-2992c2ce-UPg0w | 2.5522 |
| YUGND | fork-slaa-us-mmllm-claude-train-sym24-aab4b1d8-YUGND | 2.9047 |
| **mean** | | **2.6328** |
| **best** | | **2.5260** |

## Chain progression R1016 → R1017

Previous harvest: `workers/dispatcher/harvest-9way-r1016_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6777         | 2.6328         | -0.0449 |
| ctrl_bpc best  | 2.5242         | 2.5260         | +0.0018 |

## Per-round trajectory (best bird: 9WDnU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1017 | 6556 | 2.5260 | +0.1716 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1016_sym24`
  - `workers/dispatcher/harvest-8way-r1016_sym24`

## Output

`workers/dispatcher/harvest-4way-r1017_sym24/round-1017/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

