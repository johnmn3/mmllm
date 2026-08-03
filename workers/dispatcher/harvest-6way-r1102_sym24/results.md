# harvest-6way-r1102 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1102 ctrl_bpc |
|--------|--------|--------------:|
| FGuT8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-73458cc8-FGuT8 | 2.3890 |
| pkisN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d7ba6ab9-pkisN | 2.3941 |
| 1LSfZ | origin/claude/train-sym24-32a40ffb-1LSfZ | 2.4061 |
| f3bZy | fork-slaa-us-mmllm-claude-train-sym24-0d5ef097-f3bZy | 2.4175 |
| eQx7n | fork-slaa-us-mmllm-claude-train-sym24-68a6c7fa-eQx7n | 2.7972 |
| ukjbu | fork-joly-os-mmllm-claude-train-sym24-1bddb41a-ukjbu | 2.8168 |
| **mean** | | **2.5368** |
| **best** | | **2.3890** |

## Chain progression R1101 → R1102

Previous harvest: `workers/dispatcher/harvest-6way-r1101_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5380         | 2.5368         | -0.0012 |
| ctrl_bpc best  | 2.4013         | 2.3890         | -0.0123 |

## Per-round trajectory (best bird: FGuT8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1102 | 6364 | 2.3890 | +0.2475 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1101_sym24`
  - `workers/dispatcher/harvest-6way-r1101_sym24`

## Output

`workers/dispatcher/harvest-6way-r1102_sym24/round-1102/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

