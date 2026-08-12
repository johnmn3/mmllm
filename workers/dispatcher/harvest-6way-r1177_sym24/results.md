# harvest-6way-r1177 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1177 ctrl_bpc |
|--------|--------|--------------:|
| wDIep | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6349eb49-wDIep | 2.3027 |
| BJYOA | fork-SeniorCareMarket-mmllm-claude-train-sym24-a4de196a-BJYOA | 2.3104 |
| KcO8P | fork-slaa-us-mmllm-claude-train-sym24-a3bf874d-KcO8P | 2.3211 |
| t3UIe | fork-joly-os-mmllm-claude-train-sym24-45ee89c4-t3UIe | 2.3278 |
| arQLe | origin/claude/train-sym24-d9492ba6-arQLe | 2.3361 |
| nDmkC | fork-SeniorCareMarket-mmllm-claude-train-sym24-325538f7-nDmkC | 2.5006 |
| **mean** | | **2.3498** |
| **best** | | **2.3027** |

## Chain progression R1176 → R1177

Previous harvest: `workers/dispatcher/harvest-10way-r1176_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3958         | 2.3498         | -0.0460 |
| ctrl_bpc best  | 2.3036         | 2.3027         | -0.0009 |

## Per-round trajectory (best bird: wDIep)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1177 | 6335 | 2.3027 | +0.2584 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1176_sym24`
  - `workers/dispatcher/harvest-8way-r1176_sym24`

## Output

`workers/dispatcher/harvest-6way-r1177_sym24/round-1177/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

