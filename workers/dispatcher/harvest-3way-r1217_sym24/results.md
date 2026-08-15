# harvest-3way-r1217 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1217 ctrl_bpc |
|--------|--------|--------------:|
| WnWEG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cadcad20-WnWEG | 2.2915 |
| Iwube | origin/claude/train-sym24-fc956016-Iwube | 2.4662 |
| wRHLb | fork-joly-os-mmllm-claude-train-sym24-743e5af3-wRHLb | 2.4705 |
| **mean** | | **2.4094** |
| **best** | | **2.2915** |

## Chain progression R1216 → R1217

Previous harvest: `workers/dispatcher/harvest-5way-r1216_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3921         | 2.4094         | +0.0173 |
| ctrl_bpc best  | 2.2672         | 2.2915         | +0.0243 |

## Per-round trajectory (best bird: WnWEG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1217 | 5473 | 2.2915 | +0.2338 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1216_sym24`

## Output

`workers/dispatcher/harvest-3way-r1217_sym24/round-1217/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

