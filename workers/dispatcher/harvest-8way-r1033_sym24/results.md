# harvest-8way-r1033 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1033 ctrl_bpc |
|--------|--------|--------------:|
| ZkADV | fork-joly-os-mmllm-claude-train-sym24-6c248dae-ZkADV | 2.4889 |
| vr0Rs | origin/claude/train-sym24-b801574d-vr0Rs | 2.4924 |
| AwpLE | fork-joly-os-mmllm-claude-train-sym24-b77160ef-AwpLE | 2.5023 |
| roFX0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e9e70851-roFX0 | 2.5122 |
| Sey29 | fork-slaa-us-mmllm-claude-train-sym24-ff4273c2-Sey29 | 2.5951 |
| fGYre | origin/claude/train-sym24-b1c5dc90-fGYre | 2.6915 |
| 5yBRu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2fa0004b-5yBRu | 2.6932 |
| qNbmY | origin/claude/train-sym24-9001bb8d-qNbmY | 2.8914 |
| **mean** | | **2.6084** |
| **best** | | **2.4889** |

## Chain progression R1032 → R1033

Previous harvest: `workers/dispatcher/harvest-8way-r1032_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7283         | 2.6084         | -0.1199 |
| ctrl_bpc best  | 2.4974         | 2.4889         | -0.0085 |

## Per-round trajectory (best bird: ZkADV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1033 | 6445 | 2.4889 | +0.1892 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1032_sym24`
  - `workers/dispatcher/harvest-6way-r1032_sym24`

## Output

`workers/dispatcher/harvest-8way-r1033_sym24/round-1033/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

