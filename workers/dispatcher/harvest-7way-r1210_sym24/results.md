# harvest-7way-r1210 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1210 ctrl_bpc |
|--------|--------|--------------:|
| eEvRZ | origin/claude/train-sym24-8363bdc1-eEvRZ | 2.2869 |
| nwIT8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7f8e3efa-nwIT8 | 2.2931 |
| 5vHqs | fork-joly-os-mmllm-claude-train-sym24-812817a6-5vHqs | 2.2959 |
| JOuZx | fork-SeniorCareMarket-mmllm-claude-train-sym24-e2a0d065-JOuZx | 2.2986 |
| v9h1t | fork-joly-os-mmllm-claude-train-sym24-3c3207e8-v9h1t | 2.3094 |
| 2sW6c | origin/claude/train-sym24-1ec647cb-2sW6c | 2.4748 |
| smuPK | fork-slaa-us-mmllm-claude-train-sym24-25a311c4-smuPK | 2.6600 |
| **mean** | | **2.3741** |
| **best** | | **2.2869** |

## Chain progression R1209 → R1210

Previous harvest: `workers/dispatcher/harvest-6way-r1209_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4746         | 2.3741         | -0.1005 |
| ctrl_bpc best  | 2.2915         | 2.2869         | -0.0046 |

## Per-round trajectory (best bird: eEvRZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1210 | 6382 | 2.2869 | +0.2408 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1209_sym24`

## Output

`workers/dispatcher/harvest-7way-r1210_sym24/round-1210/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

