# harvest-6way-r1297 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1297 ctrl_bpc |
|--------|--------|--------------:|
| wQjBH | origin/claude/train-sym24-496407a0-wQjBH | 3.8331 |
| epucm | fork-slaa-us-mmllm-claude-train-sym24-646fa089-epucm | 3.8413 |
| iazTq | fork-SeniorCareMarket-mmllm-claude-train-sym24-00888612-iazTq | 3.9081 |
| 2jYJC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6eb59e1b-2jYJC | 4.2397 |
| UCe0z | fork-joly-os-mmllm-claude-train-sym24-5730b2ca-UCe0z | 4.2788 |
| 50qhH | fork-joly-os-mmllm-claude-train-sym24-c6ce4866-50qhH | 4.5166 |
| **mean** | | **4.1029** |
| **best** | | **3.8331** |

## Chain progression R1296 → R1297

Previous harvest: `workers/dispatcher/harvest-4way-r1296_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9848         | 4.1029         | +0.1181 |
| ctrl_bpc best  | 3.9342         | 3.8331         | -0.1011 |

## Per-round trajectory (best bird: wQjBH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1297 | 6390 | 3.8331 | +0.0253 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1296_sym24`

## Output

`workers/dispatcher/harvest-6way-r1297_sym24/round-1297/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

