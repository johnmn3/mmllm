# harvest-2way-r890 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R890 ctrl_bpc |
|--------|--------|--------------:|
| hVH87 | fork-slaa-us-mmllm-claude-train-sym24-abbbee82-hVH87 | 2.8163 |
| URrUT | origin/claude/train-sym24-af6c2aa2-URrUT | 2.8200 |
| **mean** | | **2.8182** |
| **best** | | **2.8163** |

## Chain progression R889 → R890

Previous harvest: `workers/dispatcher/harvest-5way-r889_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9755         | 2.8182         | -0.1573 |
| ctrl_bpc best  | 2.8175         | 2.8163         | -0.0012 |

## Per-round trajectory (best bird: hVH87)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 890 | 4348 | 2.8163 | +0.3231 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r889_sym24`

## Output

`workers/dispatcher/harvest-2way-r890_sym24/round-890/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

