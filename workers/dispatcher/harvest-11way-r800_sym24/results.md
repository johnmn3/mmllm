# harvest-11way-r800 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R800 ctrl_bpc |
|--------|--------|--------------:|
| w5sD2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1a0d23a5-w5sD2 | 3.0950 |
| KZTAu | fork-slaa-us-mmllm-claude-train-sym24-6febf7c7-KZTAu | 3.1059 |
| soG0V | fork-SeniorCareMarket-mmllm-claude-train-sym24-12d63902-soG0V | 3.1284 |
| 83ZKC | fork-davidwuchn-mmllm-claude-train-sym24-8a0d83d6-83ZKC | 3.2303 |
| rUEEA | fork-slaa-us-mmllm-claude-train-sym24-9879993c-rUEEA | 3.2444 |
| nS8Nk | origin/claude/train-sym24-71ae97b9-nS8Nk | 3.2511 |
| tHiZL | fork-davidwuchn-mmllm-claude-train-sym24-6b52bb2d-tHiZL | 3.4693 |
| decCU | origin/claude/train-sym24-3c1bdb66-decCU | 3.4853 |
| VldwM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f31fcbb5-VldwM | 3.4893 |
| BSdGv | fork-joly-os-mmllm-claude-train-sym24-80c4ec60-BSdGv | 3.4896 |
| JSs59 | fork-joly-os-mmllm-claude-train-sym24-9faab3b0-JSs59 | 3.4951 |
| **mean** | | **3.3167** |
| **best** | | **3.0950** |

## Chain progression R799 → R800

Previous harvest: `workers/dispatcher/harvest-7way-r799_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3146         | 3.3167         | +0.0021 |
| ctrl_bpc best  | 3.0997         | 3.0950         | -0.0047 |

## Per-round trajectory (best bird: w5sD2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 800 | 6312 | 3.0950 | +0.4816 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r799_sym24`
  - `workers/dispatcher/harvest-7way-r799_sym24`

## Output

`workers/dispatcher/harvest-11way-r800_sym24/round-800/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

