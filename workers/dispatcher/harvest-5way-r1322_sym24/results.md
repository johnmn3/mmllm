# harvest-5way-r1322 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1322 ctrl_bpc |
|--------|--------|--------------:|
| KHHOJ | fork-slaa-us-mmllm-claude-train-sym24-ea3687dc-KHHOJ | 3.4065 |
| 332UA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b96127dc-332UA | 3.4219 |
| Vpgks | fork-SeniorCareMarket-mmllm-claude-train-sym24-04fcee7a-Vpgks | 3.4422 |
| qqnDx | fork-joly-os-mmllm-claude-train-sym24-159d151b-qqnDx | 3.4565 |
| UDMO0 | origin/claude/train-sym24-2139fb23-UDMO0 | 3.7062 |
| **mean** | | **3.4867** |
| **best** | | **3.4065** |

## Chain progression R1321 → R1322

Previous harvest: `workers/dispatcher/harvest-5way-r1321_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4374         | 3.4867         | +0.0493 |
| ctrl_bpc best  | 3.3979         | 3.4065         | +0.0086 |

## Per-round trajectory (best bird: KHHOJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1322 | 6691 | 3.4065 | +0.0577 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1321_sym24`

## Output

`workers/dispatcher/harvest-5way-r1322_sym24/round-1322/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

