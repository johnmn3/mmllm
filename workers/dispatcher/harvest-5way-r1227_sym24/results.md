# harvest-5way-r1227 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1227 ctrl_bpc |
|--------|--------|--------------:|
| VB6sv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b173ad56-VB6sv | 2.2704 |
| wHazj | origin/claude/train-sym24-19625922-wHazj | 2.4539 |
| Hbl0T | fork-slaa-us-mmllm-claude-train-sym24-20a6f3aa-Hbl0T | 2.4591 |
| PRvcV | fork-joly-os-mmllm-claude-train-sym24-881a30a3-PRvcV | 2.4597 |
| EuveL | fork-SeniorCareMarket-mmllm-claude-train-sym24-09dfd6a6-EuveL | 2.6577 |
| **mean** | | **2.4602** |
| **best** | | **2.2704** |

## Chain progression R1226 → R1227

Previous harvest: `workers/dispatcher/harvest-10way-r1226_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3641         | 2.4602         | +0.0961 |
| ctrl_bpc best  | 2.2534         | 2.2704         | +0.0170 |

## Per-round trajectory (best bird: VB6sv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1227 | 4179 | 2.2704 | +0.2544 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1226_sym24`

## Output

`workers/dispatcher/harvest-5way-r1227_sym24/round-1227/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

