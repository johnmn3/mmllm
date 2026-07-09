# harvest-4way-r875 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R875 ctrl_bpc |
|--------|--------|--------------:|
| qMTbQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-47758f69-qMTbQ | 2.8377 |
| Cvg2j | origin/claude/train-sym24-1a46df14-Cvg2j | 2.8410 |
| Lb1RJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-24b34dbb-Lb1RJ | 2.8699 |
| 019kL | origin/claude/train-sym24-2759f611-019kL | 2.8773 |
| **mean** | | **2.8565** |
| **best** | | **2.8377** |

## Chain progression R874 → R875

Previous harvest: `workers/dispatcher/harvest-3way-r874_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1077         | 2.8565         | -0.2512 |
| ctrl_bpc best  | 3.0236         | 2.8377         | -0.1859 |

## Per-round trajectory (best bird: qMTbQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 875 | 6660 | 2.8377 | +0.3289 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r874_sym24`

## Output

`workers/dispatcher/harvest-4way-r875_sym24/round-875/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

