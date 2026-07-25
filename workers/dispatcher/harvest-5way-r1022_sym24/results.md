# harvest-5way-r1022 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1022 ctrl_bpc |
|--------|--------|--------------:|
| HhuDw | fork-SeniorCareMarket-mmllm-claude-train-sym24-10cd208f-HhuDw | 2.5121 |
| qj9vd | origin/claude/train-sym24-a53db3a7-qj9vd | 2.5207 |
| asQJD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-38703b6b-asQJD | 2.5496 |
| YBMoU | origin/claude/train-sym24-c21c1a28-YBMoU | 2.5528 |
| OsrsF | fork-joly-os-mmllm-claude-train-sym24-5204ed33-OsrsF | 2.7132 |
| **mean** | | **2.5697** |
| **best** | | **2.5121** |

## Chain progression R1021 → R1022

Previous harvest: `workers/dispatcher/harvest-8way-r1021_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7490         | 2.5697         | -0.1793 |
| ctrl_bpc best  | 2.5260         | 2.5121         | -0.0139 |

## Per-round trajectory (best bird: HhuDw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1022 | 6529 | 2.5121 | +0.1923 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1021_sym24`

## Output

`workers/dispatcher/harvest-5way-r1022_sym24/round-1022/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

