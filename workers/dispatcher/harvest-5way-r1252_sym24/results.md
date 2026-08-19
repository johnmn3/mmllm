# harvest-5way-r1252 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1252 ctrl_bpc |
|--------|--------|--------------:|
| ayiLv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8e4a175b-ayiLv | 2.2402 |
| 13elt | fork-SeniorCareMarket-mmllm-claude-train-sym24-d1c83778-13elt | 2.2562 |
| MnedN | fork-slaa-us-mmllm-claude-train-sym24-c902db10-MnedN | 2.4359 |
| SqUAd | fork-slaa-us-mmllm-claude-train-sym24-d4b6a981-SqUAd | 2.4393 |
| 43IUP | origin/claude/train-sym24-1c308a95-43IUP | 2.4420 |
| **mean** | | **2.3627** |
| **best** | | **2.2402** |

## Chain progression R1251 → R1252

Previous harvest: `workers/dispatcher/harvest-11way-r1251_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4963         | 2.3627         | -0.1336 |
| ctrl_bpc best  | 2.2391         | 2.2402         | +0.0011 |

## Per-round trajectory (best bird: ayiLv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1252 | 4351 | 2.2402 | +0.2452 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1251_sym24`

## Output

`workers/dispatcher/harvest-5way-r1252_sym24/round-1252/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

