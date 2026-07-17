# harvest-8way-r948 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R948 ctrl_bpc |
|--------|--------|--------------:|
| C4vF9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-41196085-C4vF9 | 2.6590 |
| NFEEw | fork-joly-os-mmllm-claude-train-sym24-d7329a63-NFEEw | 2.8590 |
| mdWmC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3c55f175-mdWmC | 2.8622 |
| ZYCEq | origin/claude/train-sym24-a7fe35dc-ZYCEq | 2.8651 |
| 822wT | origin/claude/train-sym24-57046daa-822wT | 2.8669 |
| qAQRL | fork-slaa-us-mmllm-claude-train-sym24-b4df5733-qAQRL | 3.0581 |
| ACqnb | fork-SeniorCareMarket-mmllm-claude-train-sym24-3cb97ff1-ACqnb | 3.0590 |
| l5k5Z | fork-slaa-us-mmllm-claude-train-sym24-bd0befff-l5k5Z | 3.0603 |
| **mean** | | **2.9112** |
| **best** | | **2.6590** |

## Chain progression R947 → R948

Previous harvest: `workers/dispatcher/harvest-3way-r947_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7974         | 2.9112         | +0.1138 |
| ctrl_bpc best  | 2.6663         | 2.6590         | -0.0073 |

## Per-round trajectory (best bird: C4vF9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 948 | 6777 | 2.6590 | +0.1959 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r947_sym24`
  - `workers/dispatcher/harvest-3way-r947_sym24`

## Output

`workers/dispatcher/harvest-8way-r948_sym24/round-948/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

