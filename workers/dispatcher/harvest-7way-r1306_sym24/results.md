# harvest-7way-r1306 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1306 ctrl_bpc |
|--------|--------|--------------:|
| MvYJ9 | fork-slaa-us-mmllm-claude-train-sym24-26cdd484-MvYJ9 | 3.4164 |
| kVGY0 | fork-joly-os-mmllm-claude-train-sym24-50f0d9b2-kVGY0 | 3.5089 |
| N7tvr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4a3062de-N7tvr | 3.5106 |
| NIsQJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-b957c065-NIsQJ | 3.5361 |
| DcNX7 | fork-joly-os-mmllm-claude-train-sym24-c960af69-DcNX7 | 3.5765 |
| nzf2m | origin/claude/train-sym24-c0d27a7b-nzf2m | 3.6311 |
| nos6D | fork-slaa-us-mmllm-claude-train-sym24-d3a2ce77-nos6D | 3.8634 |
| **mean** | | **3.5776** |
| **best** | | **3.4164** |

## Chain progression R1305 → R1306

Previous harvest: `workers/dispatcher/harvest-9way-r1305_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6191         | 3.5776         | -0.0415 |
| ctrl_bpc best  | 3.4507         | 3.4164         | -0.0343 |

## Per-round trajectory (best bird: MvYJ9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1306 | 6619 | 3.4164 | +0.0839 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1305_sym24`
  - `workers/dispatcher/harvest-7way-r1305_sym24`

## Output

`workers/dispatcher/harvest-7way-r1306_sym24/round-1306/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

