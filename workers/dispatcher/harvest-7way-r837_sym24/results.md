# harvest-7way-r837 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R837 ctrl_bpc |
|--------|--------|--------------:|
| UZORl | fork-joly-os-mmllm-claude-train-sym24-2314be44-UZORl | 2.9627 |
| LDxBO | origin/claude/train-sym24-8e7b03de-LDxBO | 2.9712 |
| DSCcl | fork-SeniorCareMarket-mmllm-claude-train-sym24-4d67e4a1-DSCcl | 2.9744 |
| nkIVl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-450ea0f1-nkIVl | 2.9805 |
| GVz8s | origin/claude/train-sym24-8db17352-GVz8s | 3.1237 |
| PB0t0 | fork-slaa-us-mmllm-claude-train-sym24-1e59400a-PB0t0 | 3.2028 |
| viAtq | fork-joly-os-mmllm-claude-train-sym24-b41d365f-viAtq | 3.3498 |
| **mean** | | **3.0807** |
| **best** | | **2.9627** |

## Chain progression R836 → R837

Previous harvest: `workers/dispatcher/harvest-9way-r836_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1129         | 3.0807         | -0.0322 |
| ctrl_bpc best  | 2.9654         | 2.9627         | -0.0027 |

## Per-round trajectory (best bird: UZORl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 837 | 6585 | 2.9627 | +0.3915 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r836_sym24`
  - `workers/dispatcher/harvest-5way-r836_sym24`
  - `workers/dispatcher/harvest-9way-r836_sym24`

## Output

`workers/dispatcher/harvest-7way-r837_sym24/round-837/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

