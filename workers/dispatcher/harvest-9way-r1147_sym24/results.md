# harvest-9way-r1147 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1147 ctrl_bpc |
|--------|--------|--------------:|
| GqUhv | fork-SeniorCareMarket-mmllm-claude-train-sym24-e7f21f54-GqUhv | 2.3595 |
| hXPQX | fork-SeniorCareMarket-mmllm-claude-train-sym24-6610d53a-hXPQX | 2.3629 |
| O3gN6 | fork-slaa-us-mmllm-claude-train-sym24-ec820b64-O3gN6 | 2.5401 |
| KlCNf | origin/claude/train-sym24-dd833eac-KlCNf | 2.5440 |
| gAOkN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ce446b24-gAOkN | 2.5450 |
| 7M2Cx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7e51fde4-7M2Cx | 2.7176 |
| NhsQT | fork-slaa-us-mmllm-claude-train-sym24-dca3e6df-NhsQT | 2.7306 |
| a0DwR | fork-slaa-us-mmllm-claude-train-sym24-18a2202b-a0DwR | 2.7322 |
| UTJC8 | fork-joly-os-mmllm-claude-train-sym24-c632a3e4-UTJC8 | 2.7411 |
| **mean** | | **2.5859** |
| **best** | | **2.3595** |

## Chain progression R1146 → R1147

Previous harvest: `workers/dispatcher/harvest-14way-r1146_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5151         | 2.5859         | +0.0708 |
| ctrl_bpc best  | 2.3370         | 2.3595         | +0.0225 |

## Per-round trajectory (best bird: GqUhv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1147 | 6465 | 2.3595 | +0.2372 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1146_sym24`
  - `workers/dispatcher/harvest-4way-r1146_sym24`

## Output

`workers/dispatcher/harvest-9way-r1147_sym24/round-1147/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

