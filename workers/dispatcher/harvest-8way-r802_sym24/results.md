# harvest-8way-r802 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R802 ctrl_bpc |
|--------|--------|--------------:|
| GP63e | fork-SeniorCareMarket-mmllm-claude-train-sym24-94f40f84-GP63e | 3.1114 |
| bHezj | fork-joly-os-mmllm-claude-train-sym24-0da3ce5a-bHezj | 3.1127 |
| eGxQ8 | fork-davidwuchn-mmllm-claude-train-sym24-140db3bd-eGxQ8 | 3.1213 |
| krEed | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-566d62dc-krEed | 3.1237 |
| b5E92 | origin/claude/train-sym24-92eeffb6-b5E92 | 3.1245 |
| 60hUe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-554d67dc-60hUe | 3.4667 |
| Y8ggz | fork-slaa-us-mmllm-claude-train-sym24-72e777d4-Y8ggz | 3.4687 |
| VHop8 | origin/claude/train-sym24-9b8e5fa8-VHop8 | 3.5018 |
| **mean** | | **3.2538** |
| **best** | | **3.1114** |

## Chain progression R801 → R802

Previous harvest: `workers/dispatcher/harvest-6way-r801_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2697         | 3.2538         | -0.0158 |
| ctrl_bpc best  | 3.0870         | 3.1114         | +0.0244 |

## Per-round trajectory (best bird: GP63e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 802 | 6422 | 3.1114 | +0.5395 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r801_sym24`
  - `workers/dispatcher/harvest-6way-r801_sym24`

## Output

`workers/dispatcher/harvest-8way-r802_sym24/round-802/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

