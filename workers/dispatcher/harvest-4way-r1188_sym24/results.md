# harvest-4way-r1188 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1188 ctrl_bpc |
|--------|--------|--------------:|
| bYdRn | fork-joly-os-mmllm-claude-train-sym24-abbe8a4b-bYdRn | 2.3138 |
| cusuP | fork-SeniorCareMarket-mmllm-claude-train-sym24-abde9e47-cusuP | 2.3170 |
| ZPKvM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b3fc202d-ZPKvM | 2.4967 |
| 3ghDr | fork-joly-os-mmllm-claude-train-sym24-7213f59f-3ghDr | 2.6897 |
| **mean** | | **2.4543** |
| **best** | | **2.3138** |

## Chain progression R610 → R1188

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.4543         | +0.3171 |
| ctrl_bpc best  | 2.1268         | 2.3138         | +0.1870 |

## Per-round trajectory (best bird: bYdRn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1188 | 6540 | 2.3138 | +0.2454 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1187_sym24`
  - `workers/dispatcher/harvest-5way-r1187_sym24`

## Output

`workers/dispatcher/harvest-4way-r1188_sym24/round-1188/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

