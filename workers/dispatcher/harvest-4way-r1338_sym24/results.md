# harvest-4way-r1338 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1338 ctrl_bpc |
|--------|--------|--------------:|
| pd9ka | origin/claude/train-sym24-b1a5986c-pd9ka | 3.2662 |
| ljOxA | origin/claude/train-sym24-8dfc95c1-ljOxA | 3.2993 |
| Q14V8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bade7066-Q14V8 | 3.3246 |
| Oq9k6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-68cc1467-Oq9k6 | 3.3518 |
| **mean** | | **3.3105** |
| **best** | | **3.2662** |

## Chain progression R1337 → R1338

Previous harvest: `workers/dispatcher/harvest-2way-r1337_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3310         | 3.3105         | -0.0205 |
| ctrl_bpc best  | 3.2950         | 3.2662         | -0.0288 |

## Per-round trajectory (best bird: pd9ka)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1338 | 6529 | 3.2662 | +0.1142 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1337_sym24`

## Output

`workers/dispatcher/harvest-4way-r1338_sym24/round-1338/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

