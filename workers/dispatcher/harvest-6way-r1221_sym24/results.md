# harvest-6way-r1221 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1221 ctrl_bpc |
|--------|--------|--------------:|
| TJdpG | fork-SeniorCareMarket-mmllm-claude-train-sym24-9eb1163b-TJdpG | 2.2620 |
| QfK5K | origin/claude/train-sym24-55487bf7-QfK5K | 2.2866 |
| 1dSGE | fork-slaa-us-mmllm-claude-train-sym24-54a11103-1dSGE | 2.2881 |
| M812h | origin/claude/train-sym24-c883e745-M812h | 2.4626 |
| UP6zW | fork-joly-os-mmllm-claude-train-sym24-43532e22-UP6zW | 2.4678 |
| unCce | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4d2d80d9-unCce | 2.6695 |
| **mean** | | **2.4061** |
| **best** | | **2.2620** |

## Chain progression R1220 → R1221

Previous harvest: `workers/dispatcher/harvest-7way-r1220_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3068         | 2.4061         | +0.0993 |
| ctrl_bpc best  | 2.2654         | 2.2620         | -0.0034 |

## Per-round trajectory (best bird: TJdpG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1221 | 5393 | 2.2620 | +0.2653 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1220_sym24`

## Output

`workers/dispatcher/harvest-6way-r1221_sym24/round-1221/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

