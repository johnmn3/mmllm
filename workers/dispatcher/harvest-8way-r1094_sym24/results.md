# harvest-8way-r1094 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1094 ctrl_bpc |
|--------|--------|--------------:|
| rgQId | origin/claude/train-sym24-da375b69-rgQId | 2.3966 |
| QcjIY | fork-SeniorCareMarket-mmllm-claude-train-sym24-7fb1eca2-QcjIY | 2.4023 |
| HLgGz | fork-slaa-us-mmllm-claude-train-sym24-81527675-HLgGz | 2.4028 |
| 1Z3iM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31f8f239-1Z3iM | 2.4100 |
| NgZQa | origin/claude/train-sym24-87a68c48-NgZQa | 2.4224 |
| pG6mN | fork-joly-os-mmllm-claude-train-sym24-f7eab00e-pG6mN | 2.6000 |
| JoQC4 | fork-joly-os-mmllm-claude-train-sym24-d3cd9a48-JoQC4 | 2.6107 |
| oOYiZ | fork-slaa-us-mmllm-claude-train-sym24-3886c770-oOYiZ | 2.8123 |
| **mean** | | **2.5071** |
| **best** | | **2.3966** |

## Chain progression R1093 → R1094

Previous harvest: `workers/dispatcher/harvest-8way-r1093_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6369         | 2.5071         | -0.1298 |
| ctrl_bpc best  | 2.4075         | 2.3966         | -0.0109 |

## Per-round trajectory (best bird: rgQId)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1094 | 6530 | 2.3966 | +0.2447 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1093_sym24`
  - `workers/dispatcher/harvest-2way-r1093_sym24`
  - `workers/dispatcher/harvest-8way-r1093_sym24`

## Output

`workers/dispatcher/harvest-8way-r1094_sym24/round-1094/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

