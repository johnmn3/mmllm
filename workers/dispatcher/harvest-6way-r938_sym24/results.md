# harvest-6way-r938 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R938 ctrl_bpc |
|--------|--------|--------------:|
| t3LFS | origin/claude/train-sym24-4b73aba4-t3LFS | 2.6748 |
| C0WfA | origin/claude/train-sym24-ac639464-C0WfA | 2.6777 |
| 65mDC | fork-slaa-us-mmllm-claude-train-sym24-2766d331-65mDC | 2.6889 |
| Rrym2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-cda1016a-Rrym2 | 2.7069 |
| imRRe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f04101bf-imRRe | 2.8950 |
| LNWSs | fork-joly-os-mmllm-claude-train-sym24-307112ef-LNWSs | 3.0720 |
| **mean** | | **2.7859** |
| **best** | | **2.6748** |

## Chain progression R937 → R938

Previous harvest: `workers/dispatcher/harvest-8way-r937_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7629         | 2.7859         | +0.0230 |
| ctrl_bpc best  | 2.6889         | 2.6748         | -0.0141 |

## Per-round trajectory (best bird: t3LFS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 938 | 6536 | 2.6748 | +0.2113 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r937_sym24`
  - `workers/dispatcher/harvest-5way-r937_sym24`

## Output

`workers/dispatcher/harvest-6way-r938_sym24/round-938/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

