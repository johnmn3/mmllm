# harvest-12way-r1177 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R1177 ctrl_bpc |
|--------|--------|--------------:|
| EQK0O | origin/claude/train-sym24-a5e02874-EQK0O | 2.3020 |
| wDIep | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6349eb49-wDIep | 2.3027 |
| BJYOA | fork-SeniorCareMarket-mmllm-claude-train-sym24-a4de196a-BJYOA | 2.3104 |
| KcO8P | fork-slaa-us-mmllm-claude-train-sym24-a3bf874d-KcO8P | 2.3211 |
| t3UIe | fork-joly-os-mmllm-claude-train-sym24-45ee89c4-t3UIe | 2.3278 |
| arQLe | origin/claude/train-sym24-d9492ba6-arQLe | 2.3361 |
| poS9F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c84938b4-poS9F | 2.5002 |
| nDmkC | fork-SeniorCareMarket-mmllm-claude-train-sym24-325538f7-nDmkC | 2.5006 |
| 3uUC2 | fork-slaa-us-mmllm-claude-train-sym24-70fd8dc2-3uUC2 | 2.5085 |
| nlTnN | fork-joly-os-mmllm-claude-train-sym24-6603aef1-nlTnN | 2.5095 |
| OJ540 | fork-joly-os-mmllm-claude-train-sym24-e350146a-OJ540 | 2.6933 |
| 6Vuj0 | fork-slaa-us-mmllm-claude-train-sym24-d129a286-6Vuj0 | 2.7023 |
| **mean** | | **2.4429** |
| **best** | | **2.3020** |

## Chain progression R1176 → R1177

Previous harvest: `workers/dispatcher/harvest-8way-r1176_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4172         | 2.4429         | +0.0257 |
| ctrl_bpc best  | 2.3108         | 2.3020         | -0.0088 |

## Per-round trajectory (best bird: EQK0O)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1177 | 6786 | 2.3020 | +0.2810 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1176_sym24`
  - `workers/dispatcher/harvest-4way-r1176_sym24`
  - `workers/dispatcher/harvest-8way-r1176_sym24`

## Output

`workers/dispatcher/harvest-12way-r1177_sym24/round-1177/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

