# harvest-4way-r1163 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1163 ctrl_bpc |
|--------|--------|--------------:|
| z8GPY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82d1da51-z8GPY | 2.3258 |
| 2dUVZ | origin/claude/train-sym24-32cf3e3b-2dUVZ | 2.3487 |
| FRuH2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-50eb7ae5-FRuH2 | 2.3518 |
| ZYeP5 | origin/claude/train-sym24-4d364cbf-ZYeP5 | 2.7338 |
| **mean** | | **2.4400** |
| **best** | | **2.3258** |

## Chain progression R1162 → R1163

Previous harvest: `workers/dispatcher/harvest-9way-r1162_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4810         | 2.4400         | -0.0410 |
| ctrl_bpc best  | 2.3184         | 2.3258         | +0.0074 |

## Per-round trajectory (best bird: z8GPY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1163 | 6652 | 2.3258 | +0.2435 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1162_sym24`

## Output

`workers/dispatcher/harvest-4way-r1163_sym24/round-1163/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

