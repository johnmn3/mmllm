# harvest-9way-r1136 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1136 ctrl_bpc |
|--------|--------|--------------:|
| CvBQm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b439957-CvBQm | 2.3420 |
| JTLCA | origin/claude/train-sym24-a006b8bd-JTLCA | 2.3463 |
| aT7e2 | fork-joly-os-mmllm-claude-train-sym24-d4bb54ad-aT7e2 | 2.3471 |
| Nezoc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3a14cebd-Nezoc | 2.3516 |
| 7IIuQ | origin/claude/train-sym24-4d488830-7IIuQ | 2.5477 |
| U7wDF | fork-SeniorCareMarket-mmllm-claude-train-sym24-02ebeafb-U7wDF | 2.5499 |
| AUCRE | fork-slaa-us-mmllm-claude-train-sym24-f0633ba9-AUCRE | 2.5679 |
| jTCDg | fork-slaa-us-mmllm-claude-train-sym24-554bd561-jTCDg | 2.7502 |
| FEeCp | fork-joly-os-mmllm-claude-train-sym24-9af31d2b-FEeCp | 2.7562 |
| **mean** | | **2.5065** |
| **best** | | **2.3420** |

## Chain progression R1135 → R1136

Previous harvest: `workers/dispatcher/harvest-5way-r1135_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3973         | 2.5065         | +0.1092 |
| ctrl_bpc best  | 2.3522         | 2.3420         | -0.0102 |

## Per-round trajectory (best bird: CvBQm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1136 | 4230 | 2.3420 | +0.2460 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1135_sym24`
  - `workers/dispatcher/harvest-5way-r1135_sym24`

## Output

`workers/dispatcher/harvest-9way-r1136_sym24/round-1136/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

