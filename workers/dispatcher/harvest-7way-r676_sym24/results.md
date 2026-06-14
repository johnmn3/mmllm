# harvest-7way-r676 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R676 ctrl_bpc |
|--------|--------|--------------:|
| w8L6L | fork-davidwuchn-mmllm-claude-train-sym24-ce9d3dde-w8L6L | 3.8016 |
| KCtgk | fork-joly-os-mmllm-claude-train-sym24-38713b9e-KCtgk | 3.8094 |
| xlYOh | fork-slaa-us-mmllm-claude-train-sym24-1fc1154c-xlYOh | 3.8516 |
| w0MgJ | origin/claude/train-sym24-16b07108-w0MgJ | 3.8638 |
| XDIfX | origin/claude/train-sym24-594f6ceb-XDIfX | 3.8691 |
| SblWU | fork-slaa-us-mmllm-claude-train-sym24-ee95c01f-SblWU | 3.8947 |
| nbgJ2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cffb0019-nbgJ2 | 3.9135 |
| **mean** | | **3.8577** |
| **best** | | **3.8016** |

## Chain progression R675 → R676

Previous harvest: `workers/dispatcher/harvest-8way-r675_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9070         | 3.8577         | -0.0493 |
| ctrl_bpc best  | 3.8172         | 3.8016         | -0.0156 |

## Per-round trajectory (best bird: w8L6L)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 676 | 6503 | 3.8016 | +0.3995 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r675_sym24`

## Output

`workers/dispatcher/harvest-7way-r676_sym24/round-676/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

