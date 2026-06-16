# harvest-6way-r691 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R691 ctrl_bpc |
|--------|--------|--------------:|
| BniYM | origin/claude/train-sym24-23590d81-BniYM | 3.6923 |
| 0n5Ue | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-95db1736-0n5Ue | 3.7260 |
| 54NtA | fork-davidwuchn-mmllm-claude-train-sym24-c60a6007-54NtA | 3.7278 |
| iRGQn | fork-davidwuchn-mmllm-claude-train-sym24-eadb46c9-iRGQn | 3.7395 |
| y4qfa | fork-joly-os-mmllm-claude-train-sym24-e63b5880-y4qfa | 4.0273 |
| 5PNpW | fork-slaa-us-mmllm-claude-train-sym24-4a98096a-5PNpW | 4.0320 |
| **mean** | | **3.8241** |
| **best** | | **3.6923** |

## Chain progression R690 → R691

Previous harvest: `workers/dispatcher/harvest-3way-r690_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8268         | 3.8241         | -0.0027 |
| ctrl_bpc best  | 3.7260         | 3.6923         | -0.0337 |

## Per-round trajectory (best bird: BniYM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 691 | 5363 | 3.6923 | +0.4792 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r690_sym24`

## Output

`workers/dispatcher/harvest-6way-r691_sym24/round-691/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

