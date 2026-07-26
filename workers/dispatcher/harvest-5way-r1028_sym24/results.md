# harvest-5way-r1028 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1028 ctrl_bpc |
|--------|--------|--------------:|
| YrqtJ | origin/claude/train-sym24-12c64173-YrqtJ | 2.5027 |
| r81pJ | fork-slaa-us-mmllm-claude-train-sym24-2c6b47e5-r81pJ | 2.5051 |
| ehwO9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-376ea5ee-ehwO9 | 2.5403 |
| bldUO | fork-SeniorCareMarket-mmllm-claude-train-sym24-698ad14b-bldUO | 2.7092 |
| KOjRI | fork-joly-os-mmllm-claude-train-sym24-736ad6f5-KOjRI | 2.9040 |
| **mean** | | **2.6323** |
| **best** | | **2.5027** |

## Chain progression R1027 → R1028

Previous harvest: `workers/dispatcher/harvest-4way-r1027_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6040         | 2.6323         | +0.0283 |
| ctrl_bpc best  | 2.5032         | 2.5027         | -0.0005 |

## Per-round trajectory (best bird: YrqtJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1028 | 6546 | 2.5027 | +0.1792 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1027_sym24`

## Output

`workers/dispatcher/harvest-5way-r1028_sym24/round-1028/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

