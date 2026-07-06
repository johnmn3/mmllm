# harvest-4way-r852 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R852 ctrl_bpc |
|--------|--------|--------------:|
| KigtO | origin/claude/train-sym24-e86288e4-KigtO | 2.9180 |
| WEIqe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cfccb10a-WEIqe | 2.9211 |
| OxbfC | fork-slaa-us-mmllm-claude-train-sym24-607df5ff-OxbfC | 2.9265 |
| EAc8L | fork-joly-os-mmllm-claude-train-sym24-2177fe42-EAc8L | 3.0747 |
| **mean** | | **2.9601** |
| **best** | | **2.9180** |

## Chain progression R851 → R852

Previous harvest: `workers/dispatcher/harvest-10way-r851_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1524         | 2.9601         | -0.1923 |
| ctrl_bpc best  | 2.9281         | 2.9180         | -0.0101 |

## Per-round trajectory (best bird: KigtO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 852 | 6377 | 2.9180 | +0.3926 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r851_sym24`

## Output

`workers/dispatcher/harvest-4way-r852_sym24/round-852/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

