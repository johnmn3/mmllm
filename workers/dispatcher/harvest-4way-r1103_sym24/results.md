# harvest-4way-r1103 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1103 ctrl_bpc |
|--------|--------|--------------:|
| siCD5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-cfccaf6b-siCD5 | 2.3906 |
| lA4QJ | origin/claude/train-sym24-65441ac4-lA4QJ | 2.3908 |
| LS0i1 | fork-joly-os-mmllm-claude-train-sym24-c0afdff3-LS0i1 | 2.4077 |
| vQwFk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-12448e22-vQwFk | 2.7931 |
| **mean** | | **2.4955** |
| **best** | | **2.3906** |

## Chain progression R1102 → R1103

Previous harvest: `workers/dispatcher/harvest-6way-r1102_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5368         | 2.4955         | -0.0413 |
| ctrl_bpc best  | 2.3890         | 2.3906         | +0.0016 |

## Per-round trajectory (best bird: siCD5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1103 | 4190 | 2.3906 | +0.2379 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1102_sym24`
  - `workers/dispatcher/harvest-4way-r1102_sym24`

## Output

`workers/dispatcher/harvest-4way-r1103_sym24/round-1103/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

