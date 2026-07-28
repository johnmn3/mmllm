# harvest-8way-r1043 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1043 ctrl_bpc |
|--------|--------|--------------:|
| 63xAC | fork-SeniorCareMarket-mmllm-claude-train-sym24-39620c60-63xAC | 2.4812 |
| Rpo2G | fork-slaa-us-mmllm-claude-train-sym24-f3044b64-Rpo2G | 2.4979 |
| sSk5B | fork-joly-os-mmllm-claude-train-sym24-c92cb28d-sSk5B | 2.5050 |
| 2Bq6B | origin/claude/train-sym24-1bdc4cdd-2Bq6B | 2.5171 |
| 6zrwB | fork-joly-os-mmllm-claude-train-sym24-d8e695c1-6zrwB | 2.5186 |
| zM7Qr | origin/claude/train-sym24-adf9f00b-zM7Qr | 2.5248 |
| T0wP2 | fork-slaa-us-mmllm-claude-train-sym24-fa70fa35-T0wP2 | 2.6764 |
| NZFEY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-631c3f8a-NZFEY | 2.6915 |
| **mean** | | **2.5516** |
| **best** | | **2.4812** |

## Chain progression R1042 → R1043

Previous harvest: `workers/dispatcher/harvest-4way-r1042_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6860         | 2.5516         | -0.1344 |
| ctrl_bpc best  | 2.4828         | 2.4812         | -0.0016 |

## Per-round trajectory (best bird: 63xAC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1043 | 6519 | 2.4812 | +0.2080 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1042_sym24`
  - `workers/dispatcher/harvest-4way-r1042_sym24`

## Output

`workers/dispatcher/harvest-8way-r1043_sym24/round-1043/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

