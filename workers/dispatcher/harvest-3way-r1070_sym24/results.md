# harvest-3way-r1070 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1070 ctrl_bpc |
|--------|--------|--------------:|
| XD790 | fork-SeniorCareMarket-mmllm-claude-train-sym24-c6b74390-XD790 | 2.4385 |
| ALCWg | fork-joly-os-mmllm-claude-train-sym24-bbea622d-ALCWg | 2.4692 |
| ztUrc | origin/claude/train-sym24-841623a9-ztUrc | 2.6422 |
| **mean** | | **2.5166** |
| **best** | | **2.4385** |

## Chain progression R1069 → R1070

Previous harvest: `workers/dispatcher/harvest-12way-r1069_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5689         | 2.5166         | -0.0523 |
| ctrl_bpc best  | 2.4445         | 2.4385         | -0.0060 |

## Per-round trajectory (best bird: XD790)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1070 | 3712 | 2.4385 | +0.2180 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1069_sym24`
  - `workers/dispatcher/harvest-9way-r1069_sym24`

## Output

`workers/dispatcher/harvest-3way-r1070_sym24/round-1070/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

