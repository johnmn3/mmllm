# harvest-6way-r1226 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1226 ctrl_bpc |
|--------|--------|--------------:|
| JQMvf | fork-SeniorCareMarket-mmllm-claude-train-sym24-3ba6946a-JQMvf | 2.2534 |
| OWHcO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fcfa2807-OWHcO | 2.2565 |
| gij0L | fork-joly-os-mmllm-claude-train-sym24-e03b3d6f-gij0L | 2.4550 |
| pmscz | origin/claude/train-sym24-6fa69794-pmscz | 2.4580 |
| 3ouHG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1fd9815d-3ouHG | 2.4622 |
| 69JPV | fork-slaa-us-mmllm-claude-train-sym24-82a986f8-69JPV | 2.4636 |
| **mean** | | **2.3914** |
| **best** | | **2.2534** |

## Chain progression R1225 → R1226

Previous harvest: `workers/dispatcher/harvest-14way-r1225_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4368         | 2.3914         | -0.0454 |
| ctrl_bpc best  | 2.2601         | 2.2534         | -0.0067 |

## Per-round trajectory (best bird: JQMvf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1226 | 6643 | 2.2534 | +0.2714 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1225_sym24`

## Output

`workers/dispatcher/harvest-6way-r1226_sym24/round-1226/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

