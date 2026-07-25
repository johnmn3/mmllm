# harvest-8way-r1021 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1021 ctrl_bpc |
|--------|--------|--------------:|
| eKTm5 | origin/claude/train-sym24-9fcc029f-eKTm5 | 2.5260 |
| 4n4Kg | origin/claude/train-sym24-8bb5c31b-4n4Kg | 2.5483 |
| lrBsX | fork-slaa-us-mmllm-claude-train-sym24-442a2c62-lrBsX | 2.5518 |
| 15I9H | fork-SeniorCareMarket-mmllm-claude-train-sym24-b3b8c2f1-15I9H | 2.7335 |
| QtP9u | fork-slaa-us-mmllm-claude-train-sym24-60dbc4d7-QtP9u | 2.9024 |
| q4tr8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2efcfee-q4tr8 | 2.9042 |
| 5fAiz | fork-joly-os-mmllm-claude-train-sym24-db689f1e-5fAiz | 2.9049 |
| luZoN | fork-joly-os-mmllm-claude-train-sym24-8956836b-luZoN | 2.9210 |
| **mean** | | **2.7490** |
| **best** | | **2.5260** |

## Chain progression R1020 → R1021

Previous harvest: `workers/dispatcher/harvest-8way-r1020_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6291         | 2.7490         | +0.1199 |
| ctrl_bpc best  | 2.5192         | 2.5260         | +0.0068 |

## Per-round trajectory (best bird: eKTm5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1021 | 6499 | 2.5260 | +0.1868 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1020_sym24`
  - `workers/dispatcher/harvest-7way-r1020_sym24`
  - `workers/dispatcher/harvest-8way-r1020_sym24`

## Output

`workers/dispatcher/harvest-8way-r1021_sym24/round-1021/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

