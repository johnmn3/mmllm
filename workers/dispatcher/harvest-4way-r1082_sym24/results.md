# harvest-4way-r1082 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1082 ctrl_bpc |
|--------|--------|--------------:|
| Ovio7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-c3883c37-Ovio7 | 2.4308 |
| nMWAJ | origin/claude/train-sym24-39dfed67-nMWAJ | 2.6123 |
| hNrkQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1482b963-hNrkQ | 2.6167 |
| iP1WI | fork-slaa-us-mmllm-claude-train-sym24-9600ed4c-iP1WI | 2.8196 |
| **mean** | | **2.6199** |
| **best** | | **2.4308** |

## Chain progression R1081 → R1082

Previous harvest: `workers/dispatcher/harvest-6way-r1081_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6060         | 2.6199         | +0.0139 |
| ctrl_bpc best  | 2.4487         | 2.4308         | -0.0179 |

## Per-round trajectory (best bird: Ovio7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1082 | 6757 | 2.4308 | +0.2319 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1081_sym24`

## Output

`workers/dispatcher/harvest-4way-r1082_sym24/round-1082/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

