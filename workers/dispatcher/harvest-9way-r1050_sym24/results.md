# harvest-9way-r1050 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1050 ctrl_bpc |
|--------|--------|--------------:|
| Hmzzi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f2393dc-Hmzzi | 2.4684 |
| F0SWA | fork-joly-os-mmllm-claude-train-sym24-57835779-F0SWA | 2.4812 |
| bKpHI | fork-slaa-us-mmllm-claude-train-sym24-1a4eeb80-bKpHI | 2.4889 |
| 3rUUO | origin/claude/train-sym24-071bce98-3rUUO | 2.4951 |
| AJqct | fork-SeniorCareMarket-mmllm-claude-train-sym24-36e3cdf5-AJqct | 2.5040 |
| LPT3o | origin/claude/train-sym24-99b16257-LPT3o | 2.5156 |
| KdCpB | origin/claude/train-sym24-162c0527-KdCpB | 2.5173 |
| vyXuq | origin/claude/train-sym24-2f685f87-vyXuq | 2.8527 |
| 62RBc | fork-joly-os-mmllm-claude-train-sym24-06e31b8c-62RBc | 2.8646 |
| **mean** | | **2.5764** |
| **best** | | **2.4684** |

## Chain progression R1049 → R1050

Previous harvest: `workers/dispatcher/harvest-5way-r1049_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6423         | 2.5764         | -0.0659 |
| ctrl_bpc best  | 2.4705         | 2.4684         | -0.0021 |

## Per-round trajectory (best bird: Hmzzi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1050 | 6452 | 2.4684 | +0.2138 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1049_sym24`
  - `workers/dispatcher/harvest-2way-r1049_sym24`
  - `workers/dispatcher/harvest-5way-r1049_sym24`

## Output

`workers/dispatcher/harvest-9way-r1050_sym24/round-1050/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

