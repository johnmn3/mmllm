# harvest-5way-r1318 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1318 ctrl_bpc |
|--------|--------|--------------:|
| fSyGE | fork-slaa-us-mmllm-claude-train-sym24-9542c1bb-fSyGE | 3.3899 |
| kCrIs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-371729c0-kCrIs | 3.4593 |
| cfgsw | origin/claude/train-sym24-bf109b40-cfgsw | 3.4600 |
| 8EYpr | fork-joly-os-mmllm-claude-train-sym24-8e05a162-8EYpr | 3.7266 |
| ezhX2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-50134e71-ezhX2 | 3.7464 |
| **mean** | | **3.5564** |
| **best** | | **3.3899** |

## Chain progression R1317 → R1318

Previous harvest: `workers/dispatcher/harvest-6way-r1317_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6536         | 3.5564         | -0.0972 |
| ctrl_bpc best  | 3.3877         | 3.3899         | +0.0022 |

## Per-round trajectory (best bird: fSyGE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1318 | 6264 | 3.3899 | +0.0682 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1317_sym24`

## Output

`workers/dispatcher/harvest-5way-r1318_sym24/round-1318/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

