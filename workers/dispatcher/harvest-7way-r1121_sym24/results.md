# harvest-7way-r1121 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1121 ctrl_bpc |
|--------|--------|--------------:|
| iOvyl | fork-SeniorCareMarket-mmllm-claude-train-sym24-c9a7c7ea-iOvyl | 2.3944 |
| 4K4tv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-931a9181-4K4tv | 2.5676 |
| khKsr | fork-SeniorCareMarket-mmllm-claude-train-sym24-b8532241-khKsr | 2.5680 |
| S2BGe | origin/claude/train-sym24-ba3f7c0b-S2BGe | 2.7569 |
| 0QS3K | origin/claude/train-sym24-40a66ace-0QS3K | 2.7622 |
| e0fjb | fork-slaa-us-mmllm-claude-train-sym24-6321aa07-e0fjb | 2.7657 |
| GIvOJ | fork-joly-os-mmllm-claude-train-sym24-3ba35398-GIvOJ | 2.7739 |
| **mean** | | **2.6555** |
| **best** | | **2.3944** |

## Chain progression R1120 → R1121

Previous harvest: `workers/dispatcher/harvest-8way-r1120_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4964         | 2.6555         | +0.1591 |
| ctrl_bpc best  | 2.3612         | 2.3944         | +0.0332 |

## Per-round trajectory (best bird: iOvyl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1121 | 6507 | 2.3944 | +0.2362 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1120_sym24`
  - `workers/dispatcher/harvest-5way-r1120_sym24`

## Output

`workers/dispatcher/harvest-7way-r1121_sym24/round-1121/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

