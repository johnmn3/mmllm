# harvest-3way-r962 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R962 ctrl_bpc |
|--------|--------|--------------:|
| d70ji | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cd4e1f74-d70ji | 2.6221 |
| Xpsi2 | origin/claude/train-sym24-51a0b088-Xpsi2 | 2.6324 |
| dxcgx | fork-SeniorCareMarket-mmllm-claude-train-sym24-08f7b380-dxcgx | 3.0248 |
| **mean** | | **2.7598** |
| **best** | | **2.6221** |

## Chain progression R961 → R962

Previous harvest: `workers/dispatcher/harvest-3way-r961_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8916         | 2.7598         | -0.1318 |
| ctrl_bpc best  | 2.6222         | 2.6221         | -0.0001 |

## Per-round trajectory (best bird: d70ji)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 962 | 5314 | 2.6221 | +0.1734 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r961_sym24`

## Output

`workers/dispatcher/harvest-3way-r962_sym24/round-962/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

