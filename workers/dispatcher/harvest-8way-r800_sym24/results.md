# harvest-8way-r800 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R800 ctrl_bpc |
|--------|--------|--------------:|
| KZTAu | fork-slaa-us-mmllm-claude-train-sym24-6febf7c7-KZTAu | 3.1059 |
| soG0V | fork-SeniorCareMarket-mmllm-claude-train-sym24-12d63902-soG0V | 3.1284 |
| nS8Nk | origin/claude/train-sym24-71ae97b9-nS8Nk | 3.2511 |
| tHiZL | fork-davidwuchn-mmllm-claude-train-sym24-6b52bb2d-tHiZL | 3.4693 |
| decCU | origin/claude/train-sym24-3c1bdb66-decCU | 3.4853 |
| VldwM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f31fcbb5-VldwM | 3.4893 |
| BSdGv | fork-joly-os-mmllm-claude-train-sym24-80c4ec60-BSdGv | 3.4896 |
| JSs59 | fork-joly-os-mmllm-claude-train-sym24-9faab3b0-JSs59 | 3.4951 |
| **mean** | | **3.3643** |
| **best** | | **3.1059** |

## Chain progression R799 → R800

Previous harvest: `workers/dispatcher/harvest-10way-r799_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2920         | 3.3643         | +0.0723 |
| ctrl_bpc best  | 3.0997         | 3.1059         | +0.0062 |

## Per-round trajectory (best bird: KZTAu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 800 | 6356 | 3.1059 | +0.5489 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r799_sym24`
  - `workers/dispatcher/harvest-7way-r799_sym24`

## Output

`workers/dispatcher/harvest-8way-r800_sym24/round-800/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

