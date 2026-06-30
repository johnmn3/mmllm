# harvest-6way-r812 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R812 ctrl_bpc |
|--------|--------|--------------:|
| 8sfJp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e4d28adc-8sfJp | 3.0603 |
| WiX8x | fork-joly-os-mmllm-claude-train-sym24-dcb054c2-WiX8x | 3.1869 |
| kUJjH | fork-slaa-us-mmllm-claude-train-sym24-27efc45b-kUJjH | 3.1886 |
| I0b9G | origin/claude/train-sym24-91829ce0-I0b9G | 3.2038 |
| XSN1U | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-09d608cf-XSN1U | 3.2225 |
| TtEHV | fork-slaa-us-mmllm-claude-train-sym24-f67e29d1-TtEHV | 3.4278 |
| **mean** | | **3.2150** |
| **best** | | **3.0603** |

## Chain progression R811 → R812

Previous harvest: `workers/dispatcher/harvest-9way-r811_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2641         | 3.2150         | -0.0491 |
| ctrl_bpc best  | 3.0709         | 3.0603         | -0.0106 |

## Per-round trajectory (best bird: 8sfJp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 812 | 6623 | 3.0603 | +0.6028 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r811_sym24`

## Output

`workers/dispatcher/harvest-6way-r812_sym24/round-812/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

