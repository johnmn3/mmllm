# harvest-17way-r793 — sparse-delta merge of 17 birds

## Worker endpoints

| handle | branch | R793 ctrl_bpc |
|--------|--------|--------------:|
| dh8Lg | fork-joly-os-mmllm-claude-train-sym24-29124fc4-dh8Lg | 3.1185 |
| 6MlwF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-54af17ed-6MlwF | 3.1300 |
| Kfidk | origin/claude/train-sym24-b2ed085e-Kfidk | 3.1424 |
| qOkSl | origin/claude/train-sym24-7c5a1838-qOkSl | 3.1539 |
| UuJaI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bb0477ef-UuJaI | 3.1609 |
| EF21v | fork-slaa-us-mmllm-claude-train-sym24-f79cfe30-EF21v | 3.1657 |
| BMX9O | fork-davidwuchn-mmllm-claude-train-sym24-9164becc-BMX9O | 3.2544 |
| lxvbA | fork-SeniorCareMarket-mmllm-claude-train-sym24-a3eca02b-lxvbA | 3.2631 |
| E8bEO | fork-davidwuchn-mmllm-claude-train-sym24-f9c70ab1-E8bEO | 3.2640 |
| xwXZu | fork-slaa-us-mmllm-claude-train-sym24-5d59cb19-xwXZu | 3.2653 |
| gdXtb | fork-SeniorCareMarket-mmllm-claude-train-sym24-8b3b428e-gdXtb | 3.2665 |
| G69Yl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-565f626b-G69Yl | 3.2686 |
| fmPNq | fork-joly-os-mmllm-claude-train-sym24-ce282bcb-fmPNq | 3.2694 |
| w9jvu | origin/claude/train-sym24-02c0fe3a-w9jvu | 3.5196 |
| ZyPIK | fork-joly-os-mmllm-claude-train-sym24-b629f517-ZyPIK | 3.5198 |
| p5sLv | fork-davidwuchn-mmllm-claude-train-sym24-5591e592-p5sLv | 3.5234 |
| prtFg | fork-slaa-us-mmllm-claude-train-sym24-b5914a8c-prtFg | 3.5235 |
| **mean** | | **3.2829** |
| **best** | | **3.1185** |

## Chain progression R792 → R793

Previous harvest: `workers/dispatcher/harvest-8way-r792_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2426         | 3.2829         | +0.0403 |
| ctrl_bpc best  | 3.1350         | 3.1185         | -0.0165 |

## Per-round trajectory (best bird: dh8Lg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 793 | 6455 | 3.1185 | +0.4350 |

## Cumulative training contribution

- This harvest: **1360 steps** from 17 bird(s)
- Across full ancestry (deduped by bird_id): **2000 steps** from 25 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r792_sym24`
  - `workers/dispatcher/harvest-5way-r792_sym24`
  - `workers/dispatcher/harvest-8way-r792_sym24`

## Output

`workers/dispatcher/harvest-17way-r793_sym24/round-793/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 17 workers)
- `dense.pt` (averaged across 17 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

