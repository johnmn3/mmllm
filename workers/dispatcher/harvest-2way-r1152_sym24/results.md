# harvest-2way-r1152 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1152 ctrl_bpc |
|--------|--------|--------------:|
| WG8kL | fork-slaa-us-mmllm-claude-train-sym24-1bc3be28-WG8kL | 2.5324 |
| V2ir7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-bb20c8bf-V2ir7 | 2.5630 |
| **mean** | | **2.5477** |
| **best** | | **2.5324** |

## Chain progression R1151 → R1152

Previous harvest: `workers/dispatcher/harvest-9way-r1151_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5154         | 2.5477         | +0.0323 |
| ctrl_bpc best  | 2.3301         | 2.5324         | +0.2023 |

## Per-round trajectory (best bird: WG8kL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1152 | 5364 | 2.5324 | +0.2225 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1151_sym24`

## Output

`workers/dispatcher/harvest-2way-r1152_sym24/round-1152/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

