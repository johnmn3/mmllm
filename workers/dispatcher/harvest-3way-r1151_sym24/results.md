# harvest-3way-r1151 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1151 ctrl_bpc |
|--------|--------|--------------:|
| zM0Qb | fork-slaa-us-mmllm-claude-train-sym24-3db6ffa0-zM0Qb | 2.5367 |
| pbbkM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-13a5d28a-pbbkM | 2.7345 |
| m3fIn | fork-joly-os-mmllm-claude-train-sym24-b9b0a2b6-m3fIn | 2.7394 |
| **mean** | | **2.6702** |
| **best** | | **2.5367** |

## Chain progression R1150 → R1151

Previous harvest: `workers/dispatcher/harvest-11way-r1150_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4455         | 2.6702         | +0.2247 |
| ctrl_bpc best  | 2.3280         | 2.5367         | +0.2087 |

## Per-round trajectory (best bird: zM0Qb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1151 | 6655 | 2.5367 | +0.2107 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1150_sym24`

## Output

`workers/dispatcher/harvest-3way-r1151_sym24/round-1151/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

