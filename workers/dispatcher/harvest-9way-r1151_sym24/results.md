# harvest-9way-r1151 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1151 ctrl_bpc |
|--------|--------|--------------:|
| zHLq9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d355474b-zHLq9 | 2.3301 |
| 3XEJw | fork-SeniorCareMarket-mmllm-claude-train-sym24-587fb666-3XEJw | 2.3487 |
| eexZC | fork-joly-os-mmllm-claude-train-sym24-8b7bedee-eexZC | 2.3621 |
| 7qxI8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-9993a10f-7qxI8 | 2.5251 |
| xlh7F | fork-slaa-us-mmllm-claude-train-sym24-6fcbba44-xlh7F | 2.5300 |
| CAiGJ | origin/claude/train-sym24-72ed772a-CAiGJ | 2.5320 |
| zM0Qb | fork-slaa-us-mmllm-claude-train-sym24-3db6ffa0-zM0Qb | 2.5367 |
| pbbkM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-13a5d28a-pbbkM | 2.7345 |
| m3fIn | fork-joly-os-mmllm-claude-train-sym24-b9b0a2b6-m3fIn | 2.7394 |
| **mean** | | **2.5154** |
| **best** | | **2.3301** |

## Chain progression R1150 → R1151

Previous harvest: `workers/dispatcher/harvest-5way-r1150_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4542         | 2.5154         | +0.0612 |
| ctrl_bpc best  | 2.3323         | 2.3301         | -0.0022 |

## Per-round trajectory (best bird: zHLq9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1151 | 5357 | 2.3301 | +0.2586 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1150_sym24`
  - `workers/dispatcher/harvest-4way-r1150_sym24`
  - `workers/dispatcher/harvest-5way-r1150_sym24`

## Output

`workers/dispatcher/harvest-9way-r1151_sym24/round-1151/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

