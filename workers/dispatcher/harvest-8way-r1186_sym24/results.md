# harvest-8way-r1186 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1186 ctrl_bpc |
|--------|--------|--------------:|
| 7LTz2 | origin/claude/train-sym24-31cb31f3-7LTz2 | 2.2986 |
| Em6gc | fork-slaa-us-mmllm-claude-train-sym24-4322023d-Em6gc | 2.3214 |
| DnaE6 | origin/claude/train-sym24-1c2d08f4-DnaE6 | 2.6794 |
| FcyST | fork-joly-os-mmllm-claude-train-sym24-e6e43de4-FcyST | 2.6815 |
| KHskj | fork-joly-os-mmllm-claude-train-sym24-ed4f6912-KHskj | 2.6931 |
| 0FaOb | fork-slaa-us-mmllm-claude-train-sym24-f3a63d24-0FaOb | 2.6951 |
| 1cEus | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-30bd1c91-1cEus | 2.6977 |
| yfdd8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-d4e61a57-yfdd8 | 2.7072 |
| **mean** | | **2.5968** |
| **best** | | **2.2986** |

## Chain progression R1185 → R1186

Previous harvest: `workers/dispatcher/harvest-5way-r1185_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5011         | 2.5968         | +0.0957 |
| ctrl_bpc best  | 2.3143         | 2.2986         | -0.0157 |

## Per-round trajectory (best bird: 7LTz2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1186 | 3795 | 2.2986 | +0.2601 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1185_sym24`
  - `workers/dispatcher/harvest-1way-r1185_sym24`
  - `workers/dispatcher/harvest-5way-r1185_sym24`

## Output

`workers/dispatcher/harvest-8way-r1186_sym24/round-1186/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

