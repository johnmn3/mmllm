# harvest-5way-r1309 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1309 ctrl_bpc |
|--------|--------|--------------:|
| GMFK6 | fork-joly-os-mmllm-claude-train-sym24-cbcbd8af-GMFK6 | 3.3840 |
| oOxZc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b8354729-oOxZc | 3.4214 |
| Ms3cW | fork-slaa-us-mmllm-claude-train-sym24-bee69b0d-Ms3cW | 3.4679 |
| VD9Pz | fork-SeniorCareMarket-mmllm-claude-train-sym24-dd3f861f-VD9Pz | 3.6526 |
| axiIK | fork-slaa-us-mmllm-claude-train-sym24-4bac3900-axiIK | 3.8552 |
| **mean** | | **3.5562** |
| **best** | | **3.3840** |

## Chain progression R1308 → R1309

Previous harvest: `workers/dispatcher/harvest-11way-r1308_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5716         | 3.5562         | -0.0154 |
| ctrl_bpc best  | 3.4082         | 3.3840         | -0.0242 |

## Per-round trajectory (best bird: GMFK6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1309 | 5385 | 3.3840 | +0.0902 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1308_sym24`
  - `workers/dispatcher/harvest-7way-r1308_sym24`

## Output

`workers/dispatcher/harvest-5way-r1309_sym24/round-1309/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

