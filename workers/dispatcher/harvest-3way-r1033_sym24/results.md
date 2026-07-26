# harvest-3way-r1033 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1033 ctrl_bpc |
|--------|--------|--------------:|
| vr0Rs | origin/claude/train-sym24-b801574d-vr0Rs | 2.4924 |
| AwpLE | fork-joly-os-mmllm-claude-train-sym24-b77160ef-AwpLE | 2.5023 |
| 5yBRu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2fa0004b-5yBRu | 2.6932 |
| **mean** | | **2.5626** |
| **best** | | **2.4924** |

## Chain progression R1032 → R1033

Previous harvest: `workers/dispatcher/harvest-8way-r1032_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7283         | 2.5626         | -0.1657 |
| ctrl_bpc best  | 2.4974         | 2.4924         | -0.0050 |

## Per-round trajectory (best bird: vr0Rs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1033 | 6712 | 2.4924 | +0.2049 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1032_sym24`

## Output

`workers/dispatcher/harvest-3way-r1033_sym24/round-1033/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

