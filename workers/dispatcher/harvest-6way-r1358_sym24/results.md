# harvest-6way-r1358 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1358 ctrl_bpc |
|--------|--------|--------------:|
| L1DT0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-22289920-L1DT0 | 3.1601 |
| bXEjc | origin/claude/train-sym24-09298f96-bXEjc | 3.2026 |
| BAbpj | fork-SeniorCareMarket-mmllm-claude-train-sym24-0a07d4b7-BAbpj | 3.2700 |
| LjtaT | origin/claude/train-sym24-7efb0113-LjtaT | 3.2703 |
| spYHD | fork-joly-os-mmllm-claude-train-sym24-81be7d33-spYHD | 3.5994 |
| KbcBS | origin/claude/train-sym24-581be4da-KbcBS | 3.6180 |
| **mean** | | **3.3534** |
| **best** | | **3.1601** |

## Chain progression R1357 → R1358

Previous harvest: `workers/dispatcher/harvest-4way-r1357_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3670         | 3.3534         | -0.0136 |
| ctrl_bpc best  | 3.2695         | 3.1601         | -0.1094 |

## Per-round trajectory (best bird: L1DT0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1358 | 6801 | 3.1601 | +0.1389 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1357_sym24`
  - `workers/dispatcher/harvest-4way-r1357_sym24`

## Output

`workers/dispatcher/harvest-6way-r1358_sym24/round-1358/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

