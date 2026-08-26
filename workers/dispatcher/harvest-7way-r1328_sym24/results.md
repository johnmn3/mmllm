# harvest-7way-r1328 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1328 ctrl_bpc |
|--------|--------|--------------:|
| qy8B2 | fork-slaa-us-mmllm-claude-train-sym24-cc19ba4b-qy8B2 | 3.3057 |
| wRrm6 | fork-joly-os-mmllm-claude-train-sym24-86ca18cc-wRrm6 | 3.3215 |
| pVYoT | fork-slaa-us-mmllm-claude-train-sym24-da055fab-pVYoT | 3.3676 |
| 69NBh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-63137b3d-69NBh | 3.4047 |
| iiYIp | origin/claude/train-sym24-2032b45f-iiYIp | 3.6617 |
| 30uRm | fork-joly-os-mmllm-claude-train-sym24-83e228ac-30uRm | 3.6710 |
| bHr5O | fork-SeniorCareMarket-mmllm-claude-train-sym24-b62b3b01-bHr5O | 3.6861 |
| **mean** | | **3.4883** |
| **best** | | **3.3057** |

## Chain progression R1327 → R1328

Previous harvest: `workers/dispatcher/harvest-6way-r1327_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4177         | 3.4883         | +0.0706 |
| ctrl_bpc best  | 3.3393         | 3.3057         | -0.0336 |

## Per-round trajectory (best bird: qy8B2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1328 | 6436 | 3.3057 | +0.0784 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1327_sym24`
  - `workers/dispatcher/harvest-6way-r1327_sym24`

## Output

`workers/dispatcher/harvest-7way-r1328_sym24/round-1328/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

