# harvest-10way-r1205 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1205 ctrl_bpc |
|--------|--------|--------------:|
| HxFc5 | fork-joly-os-mmllm-claude-train-sym24-40eb9905-HxFc5 | 2.2714 |
| KZuSA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a79705fa-KZuSA | 2.2764 |
| msQQc | fork-slaa-us-mmllm-claude-train-sym24-d720a5d8-msQQc | 2.2810 |
| 2UEwo | origin/claude/train-sym24-f8d2a64d-2UEwo | 2.2815 |
| dVleC | fork-slaa-us-mmllm-claude-train-sym24-1f4ec497-dVleC | 2.2941 |
| aYaPW | origin/claude/train-sym24-3bfab1be-aYaPW | 2.3016 |
| 40paf | fork-SeniorCareMarket-mmllm-claude-train-sym24-34a48dea-40paf | 2.4713 |
| 4wv6N | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5fee8351-4wv6N | 2.6648 |
| PEqMp | fork-joly-os-mmllm-claude-train-sym24-718401e1-PEqMp | 2.6720 |
| bCVci | fork-SeniorCareMarket-mmllm-claude-train-sym24-af97bef5-bCVci | 2.6775 |
| **mean** | | **2.4192** |
| **best** | | **2.2714** |

## Chain progression R1204 → R1205

Previous harvest: `workers/dispatcher/harvest-6way-r1204_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4434         | 2.4192         | -0.0242 |
| ctrl_bpc best  | 2.2789         | 2.2714         | -0.0075 |

## Per-round trajectory (best bird: HxFc5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1205 | 6840 | 2.2714 | +0.2634 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1204_sym24`
  - `workers/dispatcher/harvest-6way-r1204_sym24`

## Output

`workers/dispatcher/harvest-10way-r1205_sym24/round-1205/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

