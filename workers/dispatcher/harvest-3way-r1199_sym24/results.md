# harvest-3way-r1199 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1199 ctrl_bpc |
|--------|--------|--------------:|
| T5DKl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-723c0e40-T5DKl | 2.2825 |
| pgfRK | fork-SeniorCareMarket-mmllm-claude-train-sym24-25f4382a-pgfRK | 2.3080 |
| Ky72m | fork-slaa-us-mmllm-claude-train-sym24-c208a083-Ky72m | 2.6862 |
| **mean** | | **2.4256** |
| **best** | | **2.2825** |

## Chain progression R1198 → R1199

Previous harvest: `workers/dispatcher/harvest-5way-r1198_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5613         | 2.4256         | -0.1357 |
| ctrl_bpc best  | 2.4742         | 2.2825         | -0.1917 |

## Per-round trajectory (best bird: T5DKl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1199 | 6745 | 2.2825 | +0.2482 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1198_sym24`

## Output

`workers/dispatcher/harvest-3way-r1199_sym24/round-1199/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

