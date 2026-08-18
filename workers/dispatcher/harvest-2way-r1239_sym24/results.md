# harvest-2way-r1239 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1239 ctrl_bpc |
|--------|--------|--------------:|
| BgsTL | fork-joly-os-mmllm-claude-train-sym24-413c088e-BgsTL | 2.2519 |
| hplup | origin/claude/train-sym24-5fd254de-hplup | 2.2564 |
| **mean** | | **2.2542** |
| **best** | | **2.2519** |

## Chain progression R1238 → R1239

Previous harvest: `workers/dispatcher/harvest-2way-r1238_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3567         | 2.2542         | -0.1025 |
| ctrl_bpc best  | 2.2565         | 2.2519         | -0.0046 |

## Per-round trajectory (best bird: BgsTL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1239 | 5361 | 2.2519 | +0.2489 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1238_sym24`

## Output

`workers/dispatcher/harvest-2way-r1239_sym24/round-1239/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

