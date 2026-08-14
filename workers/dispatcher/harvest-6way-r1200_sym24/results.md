# harvest-6way-r1200 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1200 ctrl_bpc |
|--------|--------|--------------:|
| Sink1 | origin/claude/train-sym24-e9d3ce96-Sink1 | 2.2786 |
| ZrKZE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-abdb8d89-ZrKZE | 2.2827 |
| t63RZ | origin/claude/train-sym24-52ca0337-t63RZ | 2.2836 |
| gOxmW | fork-joly-os-mmllm-claude-train-sym24-7bb1e216-gOxmW | 2.2881 |
| CtRw2 | fork-slaa-us-mmllm-claude-train-sym24-635fea37-CtRw2 | 2.2928 |
| 7lLFm | origin/claude/train-sym24-e9bfdfa0-7lLFm | 2.6739 |
| **mean** | | **2.3500** |
| **best** | | **2.2786** |

## Chain progression R1199 → R1200

Previous harvest: `workers/dispatcher/harvest-3way-r1199_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4256         | 2.3500         | -0.0756 |
| ctrl_bpc best  | 2.2825         | 2.2786         | -0.0039 |

## Per-round trajectory (best bird: Sink1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1200 | 6398 | 2.2786 | +0.2665 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1199_sym24`
  - `workers/dispatcher/harvest-3way-r1199_sym24`

## Output

`workers/dispatcher/harvest-6way-r1200_sym24/round-1200/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

