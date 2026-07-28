# harvest-2way-r1052 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1052 ctrl_bpc |
|--------|--------|--------------:|
| dYfLq | fork-joly-os-mmllm-claude-train-sym24-3c4e9dca-dYfLq | 2.4693 |
| h07jU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d8fc7724-h07jU | 2.4883 |
| **mean** | | **2.4788** |
| **best** | | **2.4693** |

## Chain progression R1051 → R1052

Previous harvest: `workers/dispatcher/harvest-10way-r1051_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5863         | 2.4788         | -0.1075 |
| ctrl_bpc best  | 2.4703         | 2.4693         | -0.0010 |

## Per-round trajectory (best bird: dYfLq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1052 | 6132 | 2.4693 | +0.2152 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1051_sym24`
  - `workers/dispatcher/harvest-5way-r1051_sym24`

## Output

`workers/dispatcher/harvest-2way-r1052_sym24/round-1052/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

