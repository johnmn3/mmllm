# harvest-6way-r723 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R723 ctrl_bpc |
|--------|--------|--------------:|
| 9qZhY | fork-davidwuchn-mmllm-claude-train-sym24-3033060d-9qZhY | 3.5171 |
| 25Vll | origin/claude/train-sym24-6d63e9e2-25Vll | 3.5186 |
| SpqYL | fork-joly-os-mmllm-claude-train-sym24-93eca705-SpqYL | 3.5255 |
| 64iFi | fork-slaa-us-mmllm-claude-train-sym24-659ecfa3-64iFi | 3.5295 |
| BN8gd | fork-SeniorCareMarket-mmllm-claude-train-sym24-f778eb72-BN8gd | 3.5350 |
| xiThP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68f45cea-xiThP | 3.8380 |
| **mean** | | **3.5773** |
| **best** | | **3.5171** |

## Chain progression R722 → R723

Previous harvest: `workers/dispatcher/harvest-11way-r722_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6408         | 3.5773         | -0.0635 |
| ctrl_bpc best  | 3.4965         | 3.5171         | +0.0206 |

## Per-round trajectory (best bird: 9qZhY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 723 | 6368 | 3.5171 | +0.9530 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r722_sym24`
  - `workers/dispatcher/harvest-6way-r722_sym24`

## Output

`workers/dispatcher/harvest-6way-r723_sym24/round-723/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

