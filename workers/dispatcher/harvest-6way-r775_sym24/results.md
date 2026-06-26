# harvest-6way-r775 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R775 ctrl_bpc |
|--------|--------|--------------:|
| CPirH | fork-joly-os-mmllm-claude-train-sym24-9918fe2d-CPirH | 3.1992 |
| PjizB | origin/claude/train-sym24-6852c3d0-PjizB | 3.2145 |
| mQVeX | origin/claude/train-sym24-e8f22e83-mQVeX | 3.2428 |
| GjtKo | fork-SeniorCareMarket-mmllm-claude-train-sym24-f09c4b13-GjtKo | 3.3463 |
| vacvo | fork-davidwuchn-mmllm-claude-train-sym24-cf50c167-vacvo | 3.3558 |
| uf3cs | fork-joly-os-mmllm-claude-train-sym24-081e94e9-uf3cs | 3.5931 |
| **mean** | | **3.3253** |
| **best** | | **3.1992** |

## Chain progression R774 → R775

Previous harvest: `workers/dispatcher/harvest-8way-r774_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3357         | 3.3253         | -0.0104 |
| ctrl_bpc best  | 3.2072         | 3.1992         | -0.0080 |

## Per-round trajectory (best bird: CPirH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 775 | 6550 | 3.1992 | +0.5102 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r774_sym24`
  - `workers/dispatcher/harvest-4way-r774_sym24`

## Output

`workers/dispatcher/harvest-6way-r775_sym24/round-775/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

