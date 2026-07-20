# harvest-2way-r978 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R978 ctrl_bpc |
|--------|--------|--------------:|
| nBbXE | fork-joly-os-mmllm-claude-train-sym24-f9e0b953-nBbXE | 2.6021 |
| pdjip | fork-slaa-us-mmllm-claude-train-sym24-ff8ecfcd-pdjip | 2.6099 |
| **mean** | | **2.6060** |
| **best** | | **2.6021** |

## Chain progression R977 → R978

Previous harvest: `workers/dispatcher/harvest-7way-r977_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7526         | 2.6060         | -0.1466 |
| ctrl_bpc best  | 2.6082         | 2.6021         | -0.0061 |

## Per-round trajectory (best bird: nBbXE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 978 | 6345 | 2.6021 | +0.2062 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r977_sym24`

## Output

`workers/dispatcher/harvest-2way-r978_sym24/round-978/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

