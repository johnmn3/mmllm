# harvest-4way-r1386 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1386 ctrl_bpc |
|--------|--------|--------------:|
| YEnyK | fork-SeniorCareMarket-mmllm-claude-train-sym24-52c6f83b-YEnyK | 3.0663 |
| 5HLT8 | origin/claude/train-sym24-71d8ca45-5HLT8 | 3.0898 |
| nq8Ly | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-94ef8e0b-nq8Ly | 3.1580 |
| vUVBw | fork-joly-os-mmllm-claude-train-sym24-b02300ef-vUVBw | 3.5102 |
| **mean** | | **3.2061** |
| **best** | | **3.0663** |

## Chain progression R1385 → R1386

Previous harvest: `workers/dispatcher/harvest-2way-r1385_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1164         | 3.2061         | +0.0897 |
| ctrl_bpc best  | 3.0910         | 3.0663         | -0.0247 |

## Per-round trajectory (best bird: YEnyK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1386 | 4319 | 3.0663 | +0.1213 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1385_sym24`

## Output

`workers/dispatcher/harvest-4way-r1386_sym24/round-1386/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

