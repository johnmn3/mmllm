# harvest-8way-r675 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R675 ctrl_bpc |
|--------|--------|--------------:|
| WY5v1 | origin/claude/train-sym24-ddec8774-WY5v1 | 3.8172 |
| H2eB4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14c4d778-H2eB4 | 3.8288 |
| QmN3m | fork-SeniorCareMarket-mmllm-claude-train-sym24-744522dd-QmN3m | 3.8611 |
| 6EMhm | origin/claude/train-sym24-2e6ebe51-6EMhm | 3.8762 |
| D1juP | fork-davidwuchn-mmllm-claude-train-sym24-2b20e522-D1juP | 3.8768 |
| XmCep | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9e0cfcc4-XmCep | 3.8844 |
| 7XIJl | fork-joly-os-mmllm-claude-train-sym24-44bf52b1-7XIJl | 3.8978 |
| GWPVT | fork-slaa-us-mmllm-claude-train-sym24-eb097354-GWPVT | 4.2133 |
| **mean** | | **3.9070** |
| **best** | | **3.8172** |

## Chain progression R674 → R675

Previous harvest: `workers/dispatcher/harvest-12way-r674_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9220         | 3.9070         | -0.0151 |
| ctrl_bpc best  | 3.8302         | 3.8172         | -0.0130 |

## Per-round trajectory (best bird: WY5v1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 675 | 5518 | 3.8172 | +0.5895 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r674_sym24`

## Output

`workers/dispatcher/harvest-8way-r675_sym24/round-675/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

