# harvest-5way-r1276 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1276 ctrl_bpc |
|--------|--------|--------------:|
| y12r1 | fork-slaa-us-mmllm-claude-train-sym24-c033df7b-y12r1 | 2.2570 |
| 655XV | fork-SeniorCareMarket-mmllm-claude-train-sym24-443c707a-655XV | 2.4186 |
| stHF4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68ef67a2-stHF4 | 2.4209 |
| 9iF1R | origin/claude/train-sym24-ae24696c-9iF1R | 2.4265 |
| GThXT | fork-joly-os-mmllm-claude-train-sym24-b836bef8-GThXT | 2.6134 |
| **mean** | | **2.4273** |
| **best** | | **2.2570** |

## Chain progression R1275 → R1276

Previous harvest: `workers/dispatcher/harvest-10way-r1275_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3838         | 2.4273         | +0.0435 |
| ctrl_bpc best  | 2.2257         | 2.2570         | +0.0313 |

## Per-round trajectory (best bird: y12r1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1276 | 6427 | 2.2570 | +0.2527 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1275_sym24`

## Output

`workers/dispatcher/harvest-5way-r1276_sym24/round-1276/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

