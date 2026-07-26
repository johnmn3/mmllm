# harvest-5way-r1024 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1024 ctrl_bpc |
|--------|--------|--------------:|
| 2FwK7 | fork-slaa-us-mmllm-claude-train-sym24-6954869b-2FwK7 | 2.5182 |
| LOqPJ | fork-joly-os-mmllm-claude-train-sym24-24d103f7-LOqPJ | 2.5207 |
| QHLUI | origin/claude/train-sym24-f18c5217-QHLUI | 2.5417 |
| 8sKWH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-267f6fed-8sKWH | 2.7080 |
| yPbDW | fork-SeniorCareMarket-mmllm-claude-train-sym24-88b00dc1-yPbDW | 2.9117 |
| **mean** | | **2.6401** |
| **best** | | **2.5182** |

## Chain progression R1023 → R1024

Previous harvest: `workers/dispatcher/harvest-2way-r1023_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7259         | 2.6401         | -0.0858 |
| ctrl_bpc best  | 2.5369         | 2.5182         | -0.0187 |

## Per-round trajectory (best bird: 2FwK7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1024 | 6712 | 2.5182 | +0.2048 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1023_sym24`

## Output

`workers/dispatcher/harvest-5way-r1024_sym24/round-1024/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

