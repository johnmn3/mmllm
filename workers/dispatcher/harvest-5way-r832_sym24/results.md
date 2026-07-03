# harvest-5way-r832 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R832 ctrl_bpc |
|--------|--------|--------------:|
| hnYU1 | origin/claude/train-sym24-5b91a94c-hnYU1 | 2.9736 |
| XXGNa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a3d848b3-XXGNa | 2.9738 |
| LizSA | fork-SeniorCareMarket-mmllm-claude-train-sym24-68c2d9ea-LizSA | 2.9915 |
| dKJxc | fork-slaa-us-mmllm-claude-train-sym24-cbf62396-dKJxc | 2.9956 |
| ia1Yh | fork-joly-os-mmllm-claude-train-sym24-5e40ad0c-ia1Yh | 3.1402 |
| **mean** | | **3.0149** |
| **best** | | **2.9736** |

## Chain progression R831 → R832

Previous harvest: `workers/dispatcher/harvest-3way-r831_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1250         | 3.0149         | -0.1101 |
| ctrl_bpc best  | 2.9870         | 2.9736         | -0.0134 |

## Per-round trajectory (best bird: hnYU1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 832 | 6661 | 2.9736 | +0.4541 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r831_sym24`

## Output

`workers/dispatcher/harvest-5way-r832_sym24/round-832/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

