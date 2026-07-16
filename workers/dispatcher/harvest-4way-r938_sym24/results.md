# harvest-4way-r938 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R938 ctrl_bpc |
|--------|--------|--------------:|
| t3LFS | origin/claude/train-sym24-4b73aba4-t3LFS | 2.6748 |
| 65mDC | fork-slaa-us-mmllm-claude-train-sym24-2766d331-65mDC | 2.6889 |
| Rrym2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-cda1016a-Rrym2 | 2.7069 |
| imRRe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f04101bf-imRRe | 2.8950 |
| **mean** | | **2.7414** |
| **best** | | **2.6748** |

## Chain progression R937 → R938

Previous harvest: `workers/dispatcher/harvest-8way-r937_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7629         | 2.7414         | -0.0215 |
| ctrl_bpc best  | 2.6889         | 2.6748         | -0.0141 |

## Per-round trajectory (best bird: t3LFS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 938 | 6536 | 2.6748 | +0.2113 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r937_sym24`

## Output

`workers/dispatcher/harvest-4way-r938_sym24/round-938/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

