# harvest-5way-r848 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R848 ctrl_bpc |
|--------|--------|--------------:|
| iIk5g | fork-joly-os-mmllm-claude-train-sym24-2b02bb87-iIk5g | 2.9339 |
| RLmgJ | origin/claude/train-sym24-e7010630-RLmgJ | 2.9341 |
| FVW8u | fork-slaa-us-mmllm-claude-train-sym24-c23b1462-FVW8u | 2.9356 |
| HDGei | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cd4b8f59-HDGei | 2.9476 |
| IlADd | fork-SeniorCareMarket-mmllm-claude-train-sym24-a5262a87-IlADd | 3.3086 |
| **mean** | | **3.0120** |
| **best** | | **2.9339** |

## Chain progression R847 → R848

Previous harvest: `workers/dispatcher/harvest-1way-r847_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3164         | 3.0120         | -0.3044 |
| ctrl_bpc best  | 3.3164         | 2.9339         | -0.3825 |

## Per-round trajectory (best bird: iIk5g)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 848 | 6508 | 2.9339 | +0.4506 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r847_sym24`

## Output

`workers/dispatcher/harvest-5way-r848_sym24/round-848/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

