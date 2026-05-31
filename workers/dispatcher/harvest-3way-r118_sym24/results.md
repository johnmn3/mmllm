# harvest-3way-r118 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R118 ctrl_bpc |
|--------|--------|--------------:|
| WN1st | fork-SeniorCareMarket-mmllm-claude-train-sym24-1fba61ce-WN1st | 2.6739 |
| iYqal | origin/claude/train-sym24-e25750de-iYqal | 2.8122 |
| iYemo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14f52e6d-iYemo | 2.9587 |
| **mean** | | **2.8149** |
| **best** | | **2.6739** |

## Chain progression R117 → R118

Previous harvest: `workers/dispatcher/harvest-1way-r117_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7119         | 2.8149         | +0.1030 |
| ctrl_bpc best  | 2.7119         | 2.6739         | -0.0380 |

## Per-round trajectory (best bird: WN1st)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 118 | 5528 | 2.6739 | +0.0937 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **260 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r117_sym24`

## Output

`workers/dispatcher/harvest-3way-r118_sym24/round-118/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

