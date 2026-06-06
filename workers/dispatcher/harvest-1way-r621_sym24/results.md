# harvest-1way-r621 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R621 ctrl_bpc |
|--------|--------|--------------:|
| gCigm | fork-joly-os-mmllm-claude-train-sym24-4b578dad-gCigm | 2.5851 |
| **mean** | | **2.5851** |
| **best** | | **2.5851** |

## Chain progression R620 → R621

Previous harvest: `workers/dispatcher/harvest-5way-r620_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3157         | 2.5851         | +0.2694 |
| ctrl_bpc best  | 2.1241         | 2.5851         | +0.4610 |

## Per-round trajectory (best bird: gCigm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 621 | 4534 | 2.5851 | +0.0342 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **850 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r620_sym24`

## Output

`workers/dispatcher/harvest-1way-r621_sym24/round-621/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

