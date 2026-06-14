# harvest-2way-r672 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R672 ctrl_bpc |
|--------|--------|--------------:|
| kotwm | fork-SeniorCareMarket-mmllm-claude-train-sym24-86b8f563-kotwm | 3.9034 |
| OG2zm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68101f7a-OG2zm | 4.2110 |
| **mean** | | **4.0572** |
| **best** | | **3.9034** |

## Chain progression R671 → R672

Previous harvest: `workers/dispatcher/harvest-1way-r671_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9317         | 4.0572         | +0.1255 |
| ctrl_bpc best  | 3.9317         | 3.9034         | -0.0283 |

## Per-round trajectory (best bird: kotwm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 672 | 3562 | 3.9034 | +0.3493 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r671_sym24`

## Output

`workers/dispatcher/harvest-2way-r672_sym24/round-672/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

