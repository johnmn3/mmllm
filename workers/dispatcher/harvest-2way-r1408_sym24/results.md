# harvest-2way-r1408 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1408 ctrl_bpc |
|--------|--------|--------------:|
| NzKnx | fork-SeniorCareMarket-mmllm-claude-train-sym24-8db9038c-NzKnx | 3.2326 |
| e7kyv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1309e5ce-e7kyv | 3.2677 |
| **mean** | | **3.2502** |
| **best** | | **3.2326** |

## Chain progression R1407 → R1408

Previous harvest: `workers/dispatcher/harvest-6way-r1407_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3752         | 3.2502         | -0.1250 |
| ctrl_bpc best  | 3.2006         | 3.2326         | +0.0320 |

## Per-round trajectory (best bird: NzKnx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1408 | 4367 | 3.2326 | +0.0702 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1407_sym24`

## Output

`workers/dispatcher/harvest-2way-r1408_sym24/round-1408/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

