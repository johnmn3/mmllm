# harvest-6way-r1203 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1203 ctrl_bpc |
|--------|--------|--------------:|
| W14nG | fork-joly-os-mmllm-claude-train-sym24-f305c79e-W14nG | 2.2829 |
| PPrPh | fork-joly-os-mmllm-claude-train-sym24-0566f890-PPrPh | 2.2846 |
| IZfcH | fork-slaa-us-mmllm-claude-train-sym24-1f79584c-IZfcH | 2.4759 |
| utZYu | fork-SeniorCareMarket-mmllm-claude-train-sym24-afa5c1c1-utZYu | 2.4793 |
| XI2kf | origin/claude/train-sym24-e69253bb-XI2kf | 2.4800 |
| BsOfj | origin/claude/train-sym24-cfd64747-BsOfj | 2.6900 |
| **mean** | | **2.4488** |
| **best** | | **2.2829** |

## Chain progression R1202 → R1203

Previous harvest: `workers/dispatcher/harvest-7way-r1202_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5057         | 2.4488         | -0.0569 |
| ctrl_bpc best  | 2.2838         | 2.2829         | -0.0009 |

## Per-round trajectory (best bird: W14nG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1203 | 6908 | 2.2829 | +0.2498 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1202_sym24`
  - `workers/dispatcher/harvest-3way-r1202_sym24`

## Output

`workers/dispatcher/harvest-6way-r1203_sym24/round-1203/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

