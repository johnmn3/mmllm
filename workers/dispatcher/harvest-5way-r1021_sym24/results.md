# harvest-5way-r1021 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1021 ctrl_bpc |
|--------|--------|--------------:|
| eKTm5 | origin/claude/train-sym24-9fcc029f-eKTm5 | 2.5260 |
| lrBsX | fork-slaa-us-mmllm-claude-train-sym24-442a2c62-lrBsX | 2.5518 |
| 15I9H | fork-SeniorCareMarket-mmllm-claude-train-sym24-b3b8c2f1-15I9H | 2.7335 |
| q4tr8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2efcfee-q4tr8 | 2.9042 |
| 5fAiz | fork-joly-os-mmllm-claude-train-sym24-db689f1e-5fAiz | 2.9049 |
| **mean** | | **2.7241** |
| **best** | | **2.5260** |

## Chain progression R1020 → R1021

Previous harvest: `workers/dispatcher/harvest-8way-r1020_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6291         | 2.7241         | +0.0950 |
| ctrl_bpc best  | 2.5192         | 2.5260         | +0.0068 |

## Per-round trajectory (best bird: eKTm5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1021 | 6499 | 2.5260 | +0.1868 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1020_sym24`
  - `workers/dispatcher/harvest-8way-r1020_sym24`

## Output

`workers/dispatcher/harvest-5way-r1021_sym24/round-1021/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

