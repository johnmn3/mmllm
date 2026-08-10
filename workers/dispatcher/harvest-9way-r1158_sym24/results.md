# harvest-9way-r1158 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1158 ctrl_bpc |
|--------|--------|--------------:|
| mh761 | fork-slaa-us-mmllm-claude-train-sym24-176b0243-mh761 | 2.3258 |
| ofBDZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2487edff-ofBDZ | 2.3274 |
| qBVLF | fork-SeniorCareMarket-mmllm-claude-train-sym24-60ba5c3d-qBVLF | 2.3553 |
| 3Jygs | fork-slaa-us-mmllm-claude-train-sym24-8e3265c0-3Jygs | 2.3571 |
| uZSnV | fork-joly-os-mmllm-claude-train-sym24-1329454d-uZSnV | 2.3680 |
| 0hKZb | fork-SeniorCareMarket-mmllm-claude-train-sym24-04000517-0hKZb | 2.5271 |
| 5kk21 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2229134-5kk21 | 2.7049 |
| ggcAu | origin/claude/train-sym24-74281a97-ggcAu | 2.7249 |
| VBDR4 | fork-joly-os-mmllm-claude-train-sym24-b11384fe-VBDR4 | 2.7339 |
| **mean** | | **2.4916** |
| **best** | | **2.3258** |

## Chain progression R1157 → R1158

Previous harvest: `workers/dispatcher/harvest-5way-r1157_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4526         | 2.4916         | +0.0390 |
| ctrl_bpc best  | 2.3310         | 2.3258         | -0.0052 |

## Per-round trajectory (best bird: mh761)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1158 | 6666 | 2.3258 | +0.2516 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1157_sym24`
  - `workers/dispatcher/harvest-5way-r1157_sym24`

## Output

`workers/dispatcher/harvest-9way-r1158_sym24/round-1158/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

