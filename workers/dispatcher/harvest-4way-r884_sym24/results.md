# harvest-4way-r884 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R884 ctrl_bpc |
|--------|--------|--------------:|
| 9DDN4 | origin/claude/train-sym24-634aab80-9DDN4 | 2.8253 |
| G34cJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f6274881-G34cJ | 2.8690 |
| AXMJd | fork-joly-os-mmllm-claude-train-sym24-a0d72084-AXMJd | 2.9967 |
| dtDeL | fork-slaa-us-mmllm-claude-train-sym24-11022a3a-dtDeL | 3.2181 |
| **mean** | | **2.9773** |
| **best** | | **2.8253** |

## Chain progression R883 → R884

Previous harvest: `workers/dispatcher/harvest-6way-r883_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9553         | 2.9773         | +0.0220 |
| ctrl_bpc best  | 2.8263         | 2.8253         | -0.0010 |

## Per-round trajectory (best bird: 9DDN4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 884 | 6486 | 2.8253 | +0.3800 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r883_sym24`
  - `workers/dispatcher/harvest-6way-r883_sym24`

## Output

`workers/dispatcher/harvest-4way-r884_sym24/round-884/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

