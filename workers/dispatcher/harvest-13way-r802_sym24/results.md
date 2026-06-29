# harvest-13way-r802 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R802 ctrl_bpc |
|--------|--------|--------------:|
| Kk6CB | fork-davidwuchn-mmllm-claude-train-sym24-d14e4e37-Kk6CB | 3.1107 |
| GP63e | fork-SeniorCareMarket-mmllm-claude-train-sym24-94f40f84-GP63e | 3.1114 |
| czDrO | fork-slaa-us-mmllm-claude-train-sym24-dbd3ccf3-czDrO | 3.1120 |
| bHezj | fork-joly-os-mmllm-claude-train-sym24-0da3ce5a-bHezj | 3.1127 |
| eGxQ8 | fork-davidwuchn-mmllm-claude-train-sym24-140db3bd-eGxQ8 | 3.1213 |
| jHGUE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3702c55-jHGUE | 3.1215 |
| krEed | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-566d62dc-krEed | 3.1237 |
| b5E92 | origin/claude/train-sym24-92eeffb6-b5E92 | 3.1245 |
| 5MqIE | origin/claude/train-sym24-fb096d8c-5MqIE | 3.2246 |
| 60hUe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-554d67dc-60hUe | 3.4667 |
| Y8ggz | fork-slaa-us-mmllm-claude-train-sym24-72e777d4-Y8ggz | 3.4687 |
| XnyR7 | fork-joly-os-mmllm-claude-train-sym24-cc8706c5-XnyR7 | 3.4853 |
| VHop8 | origin/claude/train-sym24-9b8e5fa8-VHop8 | 3.5018 |
| **mean** | | **3.2373** |
| **best** | | **3.1107** |

## Chain progression R801 → R802

Previous harvest: `workers/dispatcher/harvest-6way-r801_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2697         | 3.2373         | -0.0324 |
| ctrl_bpc best  | 3.0870         | 3.1107         | +0.0237 |

## Per-round trajectory (best bird: Kk6CB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 802 | 6578 | 3.1107 | +0.5070 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r801_sym24`
  - `workers/dispatcher/harvest-6way-r801_sym24`

## Output

`workers/dispatcher/harvest-13way-r802_sym24/round-802/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

