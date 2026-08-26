# harvest-5way-r1324 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1324 ctrl_bpc |
|--------|--------|--------------:|
| s5m4E | fork-joly-os-mmllm-claude-train-sym24-a67a49ae-s5m4E | 3.3336 |
| a6KRe | fork-SeniorCareMarket-mmllm-claude-train-sym24-bec50038-a6KRe | 3.4023 |
| mHBH4 | fork-slaa-us-mmllm-claude-train-sym24-9a5e2407-mHBH4 | 3.4164 |
| GBBGB | origin/claude/train-sym24-59dbcb0b-GBBGB | 3.6848 |
| qkt5X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-601537d9-qkt5X | 3.7028 |
| **mean** | | **3.5080** |
| **best** | | **3.3336** |

## Chain progression R1323 → R1324

Previous harvest: `workers/dispatcher/harvest-7way-r1323_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5546         | 3.5080         | -0.0466 |
| ctrl_bpc best  | 3.3853         | 3.3336         | -0.0517 |

## Per-round trajectory (best bird: s5m4E)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1324 | 4463 | 3.3336 | +0.0837 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1323_sym24`
  - `workers/dispatcher/harvest-7way-r1323_sym24`

## Output

`workers/dispatcher/harvest-5way-r1324_sym24/round-1324/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

