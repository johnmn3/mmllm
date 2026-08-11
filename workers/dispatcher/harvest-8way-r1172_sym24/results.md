# harvest-8way-r1172 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1172 ctrl_bpc |
|--------|--------|--------------:|
| jBZir | origin/claude/train-sym24-ec318ae9-jBZir | 2.3251 |
| Mc0i0 | fork-joly-os-mmllm-claude-train-sym24-a2dbb7bb-Mc0i0 | 2.3400 |
| po0wG | origin/claude/train-sym24-26e7ebc7-po0wG | 2.3451 |
| FY6Ol | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c4e5ba0d-FY6Ol | 2.5129 |
| IEuuA | fork-slaa-us-mmllm-claude-train-sym24-ea8c0ba6-IEuuA | 2.5158 |
| lreHf | fork-joly-os-mmllm-claude-train-sym24-adb8e9b5-lreHf | 2.5192 |
| gchFc | origin/claude/train-sym24-4cd713c8-gchFc | 2.7083 |
| ldLHI | fork-slaa-us-mmllm-claude-train-sym24-11e2914a-ldLHI | 2.7128 |
| **mean** | | **2.4974** |
| **best** | | **2.3251** |

## Chain progression R1171 → R1172

Previous harvest: `workers/dispatcher/harvest-7way-r1171_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4683         | 2.4974         | +0.0291 |
| ctrl_bpc best  | 2.3347         | 2.3251         | -0.0096 |

## Per-round trajectory (best bird: jBZir)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1172 | 6580 | 2.3251 | +0.2453 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1171_sym24`
  - `workers/dispatcher/harvest-4way-r1171_sym24`
  - `workers/dispatcher/harvest-7way-r1171_sym24`

## Output

`workers/dispatcher/harvest-8way-r1172_sym24/round-1172/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

