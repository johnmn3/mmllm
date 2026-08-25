# harvest-8way-r1311 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1311 ctrl_bpc |
|--------|--------|--------------:|
| rfxcV | fork-slaa-us-mmllm-claude-train-sym24-f4ffad81-rfxcV | 3.4361 |
| ZJg3A | fork-SeniorCareMarket-mmllm-claude-train-sym24-1b5fac74-ZJg3A | 3.4445 |
| nVE4m | fork-joly-os-mmllm-claude-train-sym24-23939cc3-nVE4m | 3.5149 |
| FpGHz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fd728751-FpGHz | 3.5235 |
| X9c4N | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fb5d383e-X9c4N | 3.5344 |
| OdT8M | origin/claude/train-sym24-0fb107a5-OdT8M | 3.5366 |
| kXMjw | fork-joly-os-mmllm-claude-train-sym24-c20b9f20-kXMjw | 3.8507 |
| FUj1t | fork-SeniorCareMarket-mmllm-claude-train-sym24-efd21a07-FUj1t | 3.8540 |
| **mean** | | **3.5868** |
| **best** | | **3.4361** |

## Chain progression R1310 → R1311

Previous harvest: `workers/dispatcher/harvest-3way-r1310_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5482         | 3.5868         | +0.0386 |
| ctrl_bpc best  | 3.5297         | 3.4361         | -0.0936 |

## Per-round trajectory (best bird: rfxcV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1311 | 4143 | 3.4361 | +0.0664 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1310_sym24`
  - `workers/dispatcher/harvest-3way-r1310_sym24`

## Output

`workers/dispatcher/harvest-8way-r1311_sym24/round-1311/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

