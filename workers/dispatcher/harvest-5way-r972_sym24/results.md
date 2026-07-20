# harvest-5way-r972 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R972 ctrl_bpc |
|--------|--------|--------------:|
| ov3V8 | origin/claude/train-sym24-1b508a6c-ov3V8 | 2.6081 |
| eNj3S | fork-joly-os-mmllm-claude-train-sym24-dda4b139-eNj3S | 2.6363 |
| Hg5HE | fork-slaa-us-mmllm-claude-train-sym24-c482c55a-Hg5HE | 2.8024 |
| myu8P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc708d3e-myu8P | 2.8036 |
| XCLiG | origin/claude/train-sym24-23d6b92d-XCLiG | 3.0076 |
| **mean** | | **2.7716** |
| **best** | | **2.6081** |

## Chain progression R971 → R972

Previous harvest: `workers/dispatcher/harvest-2way-r971_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8342         | 2.7716         | -0.0626 |
| ctrl_bpc best  | 2.6572         | 2.6081         | -0.0491 |

## Per-round trajectory (best bird: ov3V8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 972 | 4155 | 2.6081 | +0.1663 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r971_sym24`
  - `workers/dispatcher/harvest-2way-r971_sym24`

## Output

`workers/dispatcher/harvest-5way-r972_sym24/round-972/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

