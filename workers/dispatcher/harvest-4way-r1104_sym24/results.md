# harvest-4way-r1104 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1104 ctrl_bpc |
|--------|--------|--------------:|
| LeAdj | origin/claude/train-sym24-dc6772e0-LeAdj | 2.3954 |
| BfbIi | fork-joly-os-mmllm-claude-train-sym24-d7c4d352-BfbIi | 2.4194 |
| SFCQ7 | origin/claude/train-sym24-186d592b-SFCQ7 | 2.4273 |
| 7hodh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3f2b714e-7hodh | 2.5757 |
| **mean** | | **2.4544** |
| **best** | | **2.3954** |

## Chain progression R1103 → R1104

Previous harvest: `workers/dispatcher/harvest-5way-r1103_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4784         | 2.4544         | -0.0240 |
| ctrl_bpc best  | 2.3906         | 2.3954         | +0.0048 |

## Per-round trajectory (best bird: LeAdj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1104 | 3739 | 2.3954 | +0.2498 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1103_sym24`

## Output

`workers/dispatcher/harvest-4way-r1104_sym24/round-1104/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

