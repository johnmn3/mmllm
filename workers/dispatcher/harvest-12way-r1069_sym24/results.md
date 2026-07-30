# harvest-12way-r1069 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R1069 ctrl_bpc |
|--------|--------|--------------:|
| A3lGE | fork-slaa-us-mmllm-claude-train-sym24-4d6bc7db-A3lGE | 2.4445 |
| 0AcjU | fork-joly-os-mmllm-claude-train-sym24-e4ec8c79-0AcjU | 2.4445 |
| PdUye | origin/claude/train-sym24-0568bbaa-PdUye | 2.4454 |
| CCTJR | fork-SeniorCareMarket-mmllm-claude-train-sym24-aed6fa2a-CCTJR | 2.4573 |
| dFP3x | fork-SeniorCareMarket-mmllm-claude-train-sym24-4abd6505-dFP3x | 2.4714 |
| OrdFT | fork-slaa-us-mmllm-claude-train-sym24-622b0b01-OrdFT | 2.4899 |
| 5ndTC | origin/claude/train-sym24-ff27546a-5ndTC | 2.5029 |
| UxbF6 | origin/claude/train-sym24-71e9aeb3-UxbF6 | 2.6330 |
| p9WRC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0076bcca-p9WRC | 2.6354 |
| AhvAA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7eb9812e-AhvAA | 2.6418 |
| DtYCm | fork-joly-os-mmllm-claude-train-sym24-a131e7c4-DtYCm | 2.8256 |
| 6XqIJ | origin/claude/train-sym24-a6017705-6XqIJ | 2.8356 |
| **mean** | | **2.5689** |
| **best** | | **2.4445** |

## Chain progression R1068 → R1069

Previous harvest: `workers/dispatcher/harvest-8way-r1068_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5985         | 2.5689         | -0.0296 |
| ctrl_bpc best  | 2.4399         | 2.4445         | +0.0046 |

## Per-round trajectory (best bird: A3lGE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1069 | 6262 | 2.4445 | +0.2206 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1068_sym24`
  - `workers/dispatcher/harvest-6way-r1068_sym24`
  - `workers/dispatcher/harvest-8way-r1068_sym24`

## Output

`workers/dispatcher/harvest-12way-r1069_sym24/round-1069/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

