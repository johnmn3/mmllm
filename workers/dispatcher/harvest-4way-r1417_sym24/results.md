# harvest-4way-r1417 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1417 ctrl_bpc |
|--------|--------|--------------:|
| krqFs | fork-joly-os-mmllm-claude-train-sym24-68d9c347-krqFs | 3.1065 |
| ENthI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-275a129b-ENthI | 3.1366 |
| vRuHa | fork-SeniorCareMarket-mmllm-claude-train-sym24-ae146bfe-vRuHa | 3.2279 |
| 5ch6T | origin/claude/train-sym24-888d340a-5ch6T | 3.2302 |
| **mean** | | **3.1753** |
| **best** | | **3.1065** |

## Chain progression R1416 → R1417

Previous harvest: `workers/dispatcher/harvest-4way-r1416_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1988         | 3.1753         | -0.0235 |
| ctrl_bpc best  | 3.1610         | 3.1065         | -0.0545 |

## Per-round trajectory (best bird: krqFs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1417 | 6426 | 3.1065 | +0.1176 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1416_sym24`

## Output

`workers/dispatcher/harvest-4way-r1417_sym24/round-1417/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

