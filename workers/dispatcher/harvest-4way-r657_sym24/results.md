# harvest-4way-r657 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R657 ctrl_bpc |
|--------|--------|--------------:|
| 33wJS | fork-joly-os-mmllm-claude-train-sym24-b9cf0cb3-33wJS | 4.1097 |
| Dihej | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fa18ec2e-Dihej | 4.1313 |
| r5Qc3 | fork-slaa-us-mmllm-claude-train-sym24-ac2d4d7a-r5Qc3 | 4.1766 |
| XHGuV | origin/claude/train-sym24-40fe852b-XHGuV | 4.4555 |
| **mean** | | **4.2183** |
| **best** | | **4.1097** |

## Chain progression R656 → R657

Previous harvest: `workers/dispatcher/harvest-10way-r656_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1969         | 4.2183         | +0.0214 |
| ctrl_bpc best  | 4.0833         | 4.1097         | +0.0264 |

## Per-round trajectory (best bird: 33wJS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 657 | 6742 | 4.1097 | +0.0439 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r656_sym24`

## Output

`workers/dispatcher/harvest-4way-r657_sym24/round-657/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

