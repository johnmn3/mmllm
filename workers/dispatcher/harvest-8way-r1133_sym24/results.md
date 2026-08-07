# harvest-8way-r1133 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1133 ctrl_bpc |
|--------|--------|--------------:|
| ZlR1S | origin/claude/train-sym24-a9067d9b-ZlR1S | 2.3493 |
| uS7yD | origin/claude/train-sym24-768e1d7c-uS7yD | 2.3563 |
| gc2Rw | fork-joly-os-mmllm-claude-train-sym24-15973095-gc2Rw | 2.3570 |
| BRdlN | origin/claude/train-sym24-52ded895-BRdlN | 2.3866 |
| pe8Nx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0081bd39-pe8Nx | 2.5582 |
| Frd0D | fork-SeniorCareMarket-mmllm-claude-train-sym24-7faec279-Frd0D | 2.5609 |
| aInoD | fork-slaa-us-mmllm-claude-train-sym24-66bb3fc2-aInoD | 2.5631 |
| 4sYjv | fork-slaa-us-mmllm-claude-train-sym24-7d5e3043-4sYjv | 2.7519 |
| **mean** | | **2.4854** |
| **best** | | **2.3493** |

## Chain progression R1132 → R1133

Previous harvest: `workers/dispatcher/harvest-6way-r1132_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5259         | 2.4854         | -0.0405 |
| ctrl_bpc best  | 2.3471         | 2.3493         | +0.0022 |

## Per-round trajectory (best bird: ZlR1S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1133 | 6370 | 2.3493 | +0.2490 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1132_sym24`
  - `workers/dispatcher/harvest-4way-r1132_sym24`

## Output

`workers/dispatcher/harvest-8way-r1133_sym24/round-1133/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

