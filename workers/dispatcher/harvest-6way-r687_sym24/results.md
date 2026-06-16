# harvest-6way-r687 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R687 ctrl_bpc |
|--------|--------|--------------:|
| rQhv6 | fork-davidwuchn-mmllm-claude-train-sym24-d765a6b3-rQhv6 | 3.7212 |
| dIyWk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7498b62d-dIyWk | 3.7382 |
| aQ7VN | fork-slaa-us-mmllm-claude-train-sym24-c90d938d-aQ7VN | 3.7384 |
| 01REV | fork-joly-os-mmllm-claude-train-sym24-8205649b-01REV | 3.7617 |
| HKPQf | origin/claude/train-sym24-13325ca2-HKPQf | 4.0510 |
| 9GQJ2 | fork-slaa-us-mmllm-claude-train-sym24-c22546a1-9GQJ2 | 4.1029 |
| **mean** | | **3.8522** |
| **best** | | **3.7212** |

## Chain progression R686 → R687

Previous harvest: `workers/dispatcher/harvest-8way-r686_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8105         | 3.8522         | +0.0417 |
| ctrl_bpc best  | 3.7412         | 3.7212         | -0.0200 |

## Per-round trajectory (best bird: rQhv6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 687 | 6590 | 3.7212 | +0.3973 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r686_sym24`

## Output

`workers/dispatcher/harvest-6way-r687_sym24/round-687/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

