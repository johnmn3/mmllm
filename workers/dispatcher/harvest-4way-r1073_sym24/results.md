# harvest-4way-r1073 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1073 ctrl_bpc |
|--------|--------|--------------:|
| hxEgp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cceb6830-hxEgp | 2.4531 |
| HsMr3 | fork-slaa-us-mmllm-claude-train-sym24-eb47626f-HsMr3 | 2.6377 |
| evWBx | origin/claude/train-sym24-c9ad4087-evWBx | 2.8252 |
| p337j | fork-SeniorCareMarket-mmllm-claude-train-sym24-17e3d7c4-p337j | 2.8333 |
| **mean** | | **2.6873** |
| **best** | | **2.4531** |

## Chain progression R1072 → R1073

Previous harvest: `workers/dispatcher/harvest-3way-r1072_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5136         | 2.6873         | +0.1737 |
| ctrl_bpc best  | 2.4406         | 2.4531         | +0.0125 |

## Per-round trajectory (best bird: hxEgp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1073 | 6736 | 2.4531 | +0.2221 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1072_sym24`

## Output

`workers/dispatcher/harvest-4way-r1073_sym24/round-1073/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

