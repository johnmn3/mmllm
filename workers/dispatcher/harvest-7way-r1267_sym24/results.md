# harvest-7way-r1267 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1267 ctrl_bpc |
|--------|--------|--------------:|
| t8Xkk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4324c471-t8Xkk | 2.2200 |
| iw10A | fork-joly-os-mmllm-claude-train-sym24-2c5154fc-iw10A | 2.2406 |
| yX8nw | fork-slaa-us-mmllm-claude-train-sym24-a4d7b31f-yX8nw | 2.2439 |
| GLvAc | fork-slaa-us-mmllm-claude-train-sym24-f544c763-GLvAc | 2.4293 |
| eqEUQ | fork-joly-os-mmllm-claude-train-sym24-27d23b4b-eqEUQ | 2.4316 |
| Evbt9 | origin/claude/train-sym24-8c14b0bf-Evbt9 | 2.4331 |
| aaUB8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-6105eba8-aaUB8 | 2.6275 |
| **mean** | | **2.3751** |
| **best** | | **2.2200** |

## Chain progression R1266 → R1267

Previous harvest: `workers/dispatcher/harvest-9way-r1266_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3898         | 2.3751         | -0.0147 |
| ctrl_bpc best  | 2.2289         | 2.2200         | -0.0089 |

## Per-round trajectory (best bird: t8Xkk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1267 | 6742 | 2.2200 | +0.2473 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1266_sym24`
  - `workers/dispatcher/harvest-5way-r1266_sym24`

## Output

`workers/dispatcher/harvest-7way-r1267_sym24/round-1267/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

