# harvest-5way-r1119 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1119 ctrl_bpc |
|--------|--------|--------------:|
| bvTDl | fork-SeniorCareMarket-mmllm-claude-train-sym24-deb4d5ff-bvTDl | 2.3615 |
| egKNn | fork-joly-os-mmllm-claude-train-sym24-89452461-egKNn | 2.3714 |
| dsaRq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5aacbdf7-dsaRq | 2.5677 |
| VkgGN | origin/claude/train-sym24-081ffaf2-VkgGN | 2.7714 |
| isgo2 | origin/claude/train-sym24-7f5d8bc4-isgo2 | 2.7921 |
| **mean** | | **2.5728** |
| **best** | | **2.3615** |

## Chain progression R1118 → R1119

Previous harvest: `workers/dispatcher/harvest-6way-r1118_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5160         | 2.5728         | +0.0568 |
| ctrl_bpc best  | 2.3683         | 2.3615         | -0.0068 |

## Per-round trajectory (best bird: bvTDl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1119 | 6519 | 2.3615 | +0.2499 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1118_sym24`
  - `workers/dispatcher/harvest-3way-r1118_sym24`

## Output

`workers/dispatcher/harvest-5way-r1119_sym24/round-1119/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

