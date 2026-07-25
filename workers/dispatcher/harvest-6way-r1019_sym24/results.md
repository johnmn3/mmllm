# harvest-6way-r1019 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1019 ctrl_bpc |
|--------|--------|--------------:|
| Umolu | origin/claude/train-sym24-ec3e3b1e-Umolu | 2.5160 |
| ZEITy | fork-SeniorCareMarket-mmllm-claude-train-sym24-179fd04e-ZEITy | 2.5214 |
| x8Ue3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1b53a11f-x8Ue3 | 2.5513 |
| RiU63 | fork-slaa-us-mmllm-claude-train-sym24-b9faac92-RiU63 | 2.7302 |
| odIcF | fork-joly-os-mmllm-claude-train-sym24-26f394f4-odIcF | 2.9191 |
| agP7i | origin/claude/train-sym24-2e1bbfbf-agP7i | 2.9228 |
| **mean** | | **2.6935** |
| **best** | | **2.5160** |

## Chain progression R1018 → R1019

Previous harvest: `workers/dispatcher/harvest-5way-r1018_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8012         | 2.6935         | -0.1077 |
| ctrl_bpc best  | 2.5171         | 2.5160         | -0.0011 |

## Per-round trajectory (best bird: Umolu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1019 | 6587 | 2.5160 | +0.1741 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1018_sym24`
  - `workers/dispatcher/harvest-5way-r1018_sym24`

## Output

`workers/dispatcher/harvest-6way-r1019_sym24/round-1019/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

