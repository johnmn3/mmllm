# harvest-3way-r1280 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1280 ctrl_bpc |
|--------|--------|--------------:|
| F2EUA | fork-slaa-us-mmllm-claude-train-sym24-4279b51b-F2EUA | 2.4158 |
| mvPEF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4f2ca899-mvPEF | 2.6170 |
| 8qt2H | fork-SeniorCareMarket-mmllm-claude-train-sym24-26c3aaf1-8qt2H | 2.6240 |
| **mean** | | **2.5523** |
| **best** | | **2.4158** |

## Chain progression R1279 → R1280

Previous harvest: `workers/dispatcher/harvest-8way-r1279_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4284         | 2.5523         | +0.1239 |
| ctrl_bpc best  | 2.2426         | 2.4158         | +0.1732 |

## Per-round trajectory (best bird: F2EUA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1280 | 6300 | 2.4158 | +0.2324 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1279_sym24`

## Output

`workers/dispatcher/harvest-3way-r1280_sym24/round-1280/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

