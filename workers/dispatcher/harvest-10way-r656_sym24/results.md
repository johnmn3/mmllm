# harvest-10way-r656 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R656 ctrl_bpc |
|--------|--------|--------------:|
| w5BXl | fork-slaa-us-mmllm-claude-train-sym24-4e57ab86-w5BXl | 4.0833 |
| cRWGl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-24381a14-cRWGl | 4.0842 |
| 1r4Fc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-60b3229d-1r4Fc | 4.1258 |
| fDzbx | fork-davidwuchn-mmllm-claude-train-sym24-375d8067-fDzbx | 4.1271 |
| T6REJ | fork-joly-os-mmllm-claude-train-sym24-1ff06b9f-T6REJ | 4.1397 |
| aOttd | fork-davidwuchn-mmllm-claude-train-sym24-fe23fa84-aOttd | 4.1425 |
| H4gsy | origin/claude/train-sym24-c86b88cc-H4gsy | 4.1493 |
| VayKm | fork-joly-os-mmllm-claude-train-sym24-7fcb8b10-VayKm | 4.1604 |
| O3uR2 | origin/claude/train-sym24-56dbbd0d-O3uR2 | 4.4637 |
| 73bZh | fork-SeniorCareMarket-mmllm-claude-train-sym24-c7182864-73bZh | 4.4931 |
| **mean** | | **4.1969** |
| **best** | | **4.0833** |

## Chain progression R655 → R656

Previous harvest: `workers/dispatcher/harvest-7way-r655_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1845         | 4.1969         | +0.0124 |
| ctrl_bpc best  | 4.1119         | 4.0833         | -0.0286 |

## Per-round trajectory (best bird: w5BXl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 656 | 6329 | 4.0833 | +0.1047 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r655_sym24`
  - `workers/dispatcher/harvest-7way-r655_sym24`

## Output

`workers/dispatcher/harvest-10way-r656_sym24/round-656/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

