# harvest-2way-r925 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R925 ctrl_bpc |
|--------|--------|--------------:|
| UeQ1g | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7efc2042-UeQ1g | 2.9207 |
| F11Ec | fork-slaa-us-mmllm-claude-train-sym24-9ca033b6-F11Ec | 3.1274 |
| **mean** | | **3.0240** |
| **best** | | **2.9207** |

## Chain progression R924 → R925

Previous harvest: `workers/dispatcher/harvest-9way-r924_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8590         | 3.0240         | +0.1650 |
| ctrl_bpc best  | 2.7243         | 2.9207         | +0.1964 |

## Per-round trajectory (best bird: UeQ1g)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 925 | 4320 | 2.9207 | +0.1863 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r924_sym24`

## Output

`workers/dispatcher/harvest-2way-r925_sym24/round-925/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

