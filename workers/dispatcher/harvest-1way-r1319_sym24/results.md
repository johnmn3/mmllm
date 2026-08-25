# harvest-1way-r1319 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1319 ctrl_bpc |
|--------|--------|--------------:|
| zF9pa | fork-slaa-us-mmllm-claude-train-sym24-b062cff8-zF9pa | 3.5485 |
| **mean** | | **3.5485** |
| **best** | | **3.5485** |

## Chain progression R1318 → R1319

Previous harvest: `workers/dispatcher/harvest-5way-r1318_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5564         | 3.5485         | -0.0079 |
| ctrl_bpc best  | 3.3899         | 3.5485         | +0.1586 |

## Per-round trajectory (best bird: zF9pa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1319 | 4426 | 3.5485 | +0.0471 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1318_sym24`

## Output

`workers/dispatcher/harvest-1way-r1319_sym24/round-1319/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

