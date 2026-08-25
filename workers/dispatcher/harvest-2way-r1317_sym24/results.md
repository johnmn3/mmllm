# harvest-2way-r1317 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1317 ctrl_bpc |
|--------|--------|--------------:|
| sUlol | fork-SeniorCareMarket-mmllm-claude-train-sym24-168409e0-sUlol | 3.3877 |
| 3Bc6r | fork-joly-os-mmllm-claude-train-sym24-f6e61952-3Bc6r | 3.7528 |
| **mean** | | **3.5703** |
| **best** | | **3.3877** |

## Chain progression R1316 → R1317

Previous harvest: `workers/dispatcher/harvest-8way-r1316_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5390         | 3.5703         | +0.0312 |
| ctrl_bpc best  | 3.3853         | 3.3877         | +0.0024 |

## Per-round trajectory (best bird: sUlol)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1317 | 5579 | 3.3877 | +0.0714 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1316_sym24`

## Output

`workers/dispatcher/harvest-2way-r1317_sym24/round-1317/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

