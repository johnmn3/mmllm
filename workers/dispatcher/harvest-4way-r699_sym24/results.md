# harvest-4way-r699 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R699 ctrl_bpc |
|--------|--------|--------------:|
| st0WW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0e0b3b74-st0WW | 3.6203 |
| Hbo13 | fork-joly-os-mmllm-claude-train-sym24-5ec7fd25-Hbo13 | 3.6886 |
| yjLm7 | fork-slaa-us-mmllm-claude-train-sym24-6f81f11f-yjLm7 | 3.9678 |
| Qdqp9 | origin/claude/train-sym24-f408aeab-Qdqp9 | 3.9682 |
| **mean** | | **3.8112** |
| **best** | | **3.6203** |

## Chain progression R698 → R699

Previous harvest: `workers/dispatcher/harvest-6way-r698_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8357         | 3.8112         | -0.0245 |
| ctrl_bpc best  | 3.6856         | 3.6203         | -0.0653 |

## Per-round trajectory (best bird: st0WW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 699 | 6670 | 3.6203 | +0.6347 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r698_sym24`

## Output

`workers/dispatcher/harvest-4way-r699_sym24/round-699/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

