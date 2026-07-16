# harvest-4way-r933 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R933 ctrl_bpc |
|--------|--------|--------------:|
| SmDhh | origin/claude/train-sym24-19f5f277-SmDhh | 2.6912 |
| tZKWG | fork-slaa-us-mmllm-claude-train-sym24-fce233d1-tZKWG | 2.7021 |
| 41Lse | fork-joly-os-mmllm-claude-train-sym24-2758064e-41Lse | 2.7092 |
| GZ295 | origin/claude/train-sym24-f2602246-GZ295 | 3.0913 |
| **mean** | | **2.7984** |
| **best** | | **2.6912** |

## Chain progression R932 → R933

Previous harvest: `workers/dispatcher/harvest-3way-r932_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7818         | 2.7984         | +0.0166 |
| ctrl_bpc best  | 2.7116         | 2.6912         | -0.0204 |

## Per-round trajectory (best bird: SmDhh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 933 | 3616 | 2.6912 | +0.2158 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r932_sym24`

## Output

`workers/dispatcher/harvest-4way-r933_sym24/round-933/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

