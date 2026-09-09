# harvest-4way-r1419 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1419 ctrl_bpc |
|--------|--------|--------------:|
| qi5uF | fork-joly-os-mmllm-claude-train-sym24-50092031-qi5uF | 3.0917 |
| UI1Kw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-85f49aba-UI1Kw | 3.1018 |
| Tna44 | origin/claude/train-sym24-76ac5e46-Tna44 | 3.2161 |
| 6k4uJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-dcc963a4-6k4uJ | 3.4719 |
| **mean** | | **3.2204** |
| **best** | | **3.0917** |

## Chain progression R1418 → R1419

Previous harvest: `workers/dispatcher/harvest-8way-r1418_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2587         | 3.2204         | -0.0383 |
| ctrl_bpc best  | 3.1174         | 3.0917         | -0.0257 |

## Per-round trajectory (best bird: qi5uF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1419 | 6520 | 3.0917 | +0.1717 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1418_sym24`

## Output

`workers/dispatcher/harvest-4way-r1419_sym24/round-1419/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

