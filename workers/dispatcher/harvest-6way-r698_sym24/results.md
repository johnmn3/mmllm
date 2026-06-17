# harvest-6way-r698 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R698 ctrl_bpc |
|--------|--------|--------------:|
| 3e14E | fork-slaa-us-mmllm-claude-train-sym24-7e945c9f-3e14E | 3.6856 |
| oEL1X | fork-joly-os-mmllm-claude-train-sym24-ec0f93e5-oEL1X | 3.6929 |
| VZkFI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e7e28031-VZkFI | 3.6945 |
| vKbQh | origin/claude/train-sym24-35921d64-vKbQh | 3.9762 |
| QZEVT | fork-davidwuchn-mmllm-claude-train-sym24-451230bd-QZEVT | 3.9764 |
| li833 | fork-davidwuchn-mmllm-claude-train-sym24-ae369571-li833 | 3.9884 |
| **mean** | | **3.8357** |
| **best** | | **3.6856** |

## Chain progression R697 → R698

Previous harvest: `workers/dispatcher/harvest-1way-r697_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6939         | 3.8357         | +0.1418 |
| ctrl_bpc best  | 3.6939         | 3.6856         | -0.0083 |

## Per-round trajectory (best bird: 3e14E)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 698 | 6818 | 3.6856 | +0.9362 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r697_sym24`

## Output

`workers/dispatcher/harvest-6way-r698_sym24/round-698/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

