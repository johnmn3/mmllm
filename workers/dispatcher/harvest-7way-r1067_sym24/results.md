# harvest-7way-r1067 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1067 ctrl_bpc |
|--------|--------|--------------:|
| zVrT7 | fork-slaa-us-mmllm-claude-train-sym24-905e1d60-zVrT7 | 2.4475 |
| ezWAj | origin/claude/train-sym24-deacc721-ezWAj | 2.4671 |
| nqOUj | origin/claude/train-sym24-84f1b36a-nqOUj | 2.4733 |
| I9slv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31474b34-I9slv | 2.6289 |
| XQ5qd | fork-SeniorCareMarket-mmllm-claude-train-sym24-86fea8c4-XQ5qd | 2.6337 |
| MO9w5 | fork-joly-os-mmllm-claude-train-sym24-3b081645-MO9w5 | 2.6375 |
| Uf2xT | origin/claude/train-sym24-36acac36-Uf2xT | 2.6557 |
| **mean** | | **2.5634** |
| **best** | | **2.4475** |

## Chain progression R1066 → R1067

Previous harvest: `workers/dispatcher/harvest-6way-r1066_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5977         | 2.5634         | -0.0343 |
| ctrl_bpc best  | 2.4812         | 2.4475         | -0.0337 |

## Per-round trajectory (best bird: zVrT7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1067 | 3827 | 2.4475 | +0.2175 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1066_sym24`
  - `workers/dispatcher/harvest-4way-r1066_sym24`

## Output

`workers/dispatcher/harvest-7way-r1067_sym24/round-1067/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

