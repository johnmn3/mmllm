# harvest-9way-r1016 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1016 ctrl_bpc |
|--------|--------|--------------:|
| EZdBN | origin/claude/train-sym24-32ff1295-EZdBN | 2.5242 |
| q5072 | fork-slaa-us-mmllm-claude-train-sym24-d28afd72-q5072 | 2.5252 |
| xKnk8 | origin/claude/train-sym24-f14b1f29-xKnk8 | 2.5471 |
| Sh2t8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1d7715a8-Sh2t8 | 2.5508 |
| K8y7r | fork-joly-os-mmllm-claude-train-sym24-1477be87-K8y7r | 2.5542 |
| yHn8G | origin/claude/train-sym24-f8433b26-yHn8G | 2.6038 |
| 7ZgTP | fork-SeniorCareMarket-mmllm-claude-train-sym24-0f6562ae-7ZgTP | 2.9243 |
| 0IuYk | fork-joly-os-mmllm-claude-train-sym24-61fac533-0IuYk | 2.9295 |
| NV6FU | fork-joly-os-mmllm-claude-train-sym24-2cd858ec-NV6FU | 2.9400 |
| **mean** | | **2.6777** |
| **best** | | **2.5242** |

## Chain progression R1015 → R1016

Previous harvest: `workers/dispatcher/harvest-7way-r1015_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7037         | 2.6777         | -0.0260 |
| ctrl_bpc best  | 2.5366         | 2.5242         | -0.0124 |

## Per-round trajectory (best bird: EZdBN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1016 | 6600 | 2.5242 | +0.1766 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1015_sym24`
  - `workers/dispatcher/harvest-3way-r1015_sym24`
  - `workers/dispatcher/harvest-7way-r1015_sym24`

## Output

`workers/dispatcher/harvest-9way-r1016_sym24/round-1016/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

