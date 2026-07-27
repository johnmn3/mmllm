# harvest-5way-r1036 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1036 ctrl_bpc |
|--------|--------|--------------:|
| QB2Uy | fork-slaa-us-mmllm-claude-train-sym24-bebed214-QB2Uy | 2.5111 |
| V85Bo | origin/claude/train-sym24-e8395dd4-V85Bo | 2.5333 |
| 5GHzq | fork-SeniorCareMarket-mmllm-claude-train-sym24-da8e9b96-5GHzq | 2.8902 |
| wsu4f | origin/claude/train-sym24-e3219fa4-wsu4f | 2.8921 |
| YpZlk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f7ccad60-YpZlk | 2.9020 |
| **mean** | | **2.7457** |
| **best** | | **2.5111** |

## Chain progression R1035 → R1036

Previous harvest: `workers/dispatcher/harvest-6way-r1035_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6826         | 2.7457         | +0.0631 |
| ctrl_bpc best  | 2.4881         | 2.5111         | +0.0230 |

## Per-round trajectory (best bird: QB2Uy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1036 | 6530 | 2.5111 | +0.1744 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1035_sym24`
  - `workers/dispatcher/harvest-6way-r1035_sym24`

## Output

`workers/dispatcher/harvest-5way-r1036_sym24/round-1036/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

