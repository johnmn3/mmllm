# harvest-6way-r1239 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1239 ctrl_bpc |
|--------|--------|--------------:|
| BgsTL | fork-joly-os-mmllm-claude-train-sym24-413c088e-BgsTL | 2.2519 |
| hplup | origin/claude/train-sym24-5fd254de-hplup | 2.2564 |
| sgy6k | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-eced0155-sgy6k | 2.4460 |
| P6wN3 | fork-slaa-us-mmllm-claude-train-sym24-02b1d4af-P6wN3 | 2.4476 |
| G4MlL | fork-SeniorCareMarket-mmllm-claude-train-sym24-c720f9a9-G4MlL | 2.4501 |
| ModJ8 | origin/claude/train-sym24-d3fb8c62-ModJ8 | 2.6444 |
| **mean** | | **2.4161** |
| **best** | | **2.2519** |

## Chain progression R1238 → R1239

Previous harvest: `workers/dispatcher/harvest-2way-r1238_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3567         | 2.4161         | +0.0594 |
| ctrl_bpc best  | 2.2565         | 2.2519         | -0.0046 |

## Per-round trajectory (best bird: BgsTL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1239 | 5361 | 2.2519 | +0.2489 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1238_sym24`

## Output

`workers/dispatcher/harvest-6way-r1239_sym24/round-1239/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

