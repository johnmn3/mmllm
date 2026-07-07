# harvest-6way-r859 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R859 ctrl_bpc |
|--------|--------|--------------:|
| 8CQ6R | fork-SeniorCareMarket-mmllm-claude-train-sym24-86c6c5a0-8CQ6R | 2.8979 |
| iHCJk | fork-slaa-us-mmllm-claude-train-sym24-8d43bc05-iHCJk | 2.9024 |
| 88s2X | origin/claude/train-sym24-ee1ea4c1-88s2X | 2.9111 |
| oYAQC | fork-joly-os-mmllm-claude-train-sym24-a0046722-oYAQC | 2.9135 |
| 4W4am | fork-joly-os-mmllm-claude-train-sym24-f71f7d70-4W4am | 2.9164 |
| 00kBC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-94856f86-00kBC | 3.0691 |
| **mean** | | **2.9351** |
| **best** | | **2.8979** |

## Chain progression R858 → R859

Previous harvest: `workers/dispatcher/harvest-5way-r858_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9047         | 2.9351         | +0.0304 |
| ctrl_bpc best  | 2.8982         | 2.8979         | -0.0003 |

## Per-round trajectory (best bird: 8CQ6R)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 859 | 6520 | 2.8979 | +0.3411 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r858_sym24`
  - `workers/dispatcher/harvest-5way-r858_sym24`

## Output

`workers/dispatcher/harvest-6way-r859_sym24/round-859/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

