# harvest-9way-r710 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R710 ctrl_bpc |
|--------|--------|--------------:|
| y2OOx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b90e81e9-y2OOx | 3.5547 |
| opR6X | fork-joly-os-mmllm-claude-train-sym24-a48f33f2-opR6X | 3.5599 |
| exDvQ | fork-slaa-us-mmllm-claude-train-sym24-d28b1c13-exDvQ | 3.5607 |
| YJzY9 | fork-joly-os-mmllm-claude-train-sym24-56e66360-YJzY9 | 3.5995 |
| S3IGb | fork-slaa-us-mmllm-claude-train-sym24-bfd9af8b-S3IGb | 3.6036 |
| 4cFg8 | origin/claude/train-sym24-50424cea-4cFg8 | 3.6047 |
| 5CNsN | fork-davidwuchn-mmllm-claude-train-sym24-d45b670b-5CNsN | 3.6106 |
| Q6g7B | fork-davidwuchn-mmllm-claude-train-sym24-07340b2d-Q6g7B | 3.6209 |
| 7NheT | origin/claude/train-sym24-feb054eb-7NheT | 3.9031 |
| **mean** | | **3.6242** |
| **best** | | **3.5547** |

## Chain progression R709 → R710

Previous harvest: `workers/dispatcher/harvest-7way-r709_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6355         | 3.6242         | -0.0113 |
| ctrl_bpc best  | 3.5610         | 3.5547         | -0.0063 |

## Per-round trajectory (best bird: y2OOx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 710 | 6641 | 3.5547 | +0.8098 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r709_sym24`
  - `workers/dispatcher/harvest-7way-r709_sym24`

## Output

`workers/dispatcher/harvest-9way-r710_sym24/round-710/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

