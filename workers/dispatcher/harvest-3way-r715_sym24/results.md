# harvest-3way-r715 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R715 ctrl_bpc |
|--------|--------|--------------:|
| drleb | fork-slaa-us-mmllm-claude-train-sym24-738c2c00-drleb | 3.5700 |
| g3WGf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c59e94da-g3WGf | 3.8635 |
| npI3p | origin/claude/train-sym24-87c334e5-npI3p | 3.8708 |
| **mean** | | **3.7681** |
| **best** | | **3.5700** |

## Chain progression R714 → R715

Previous harvest: `workers/dispatcher/harvest-10way-r714_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5706         | 3.7681         | +0.1975 |
| ctrl_bpc best  | 3.5379         | 3.5700         | +0.0321 |

## Per-round trajectory (best bird: drleb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 715 | 6692 | 3.5700 | +0.8475 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r714_sym24`

## Output

`workers/dispatcher/harvest-3way-r715_sym24/round-715/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

