# harvest-5way-r1018 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1018 ctrl_bpc |
|--------|--------|--------------:|
| j8sPS | fork-slaa-us-mmllm-claude-train-sym24-e81595e7-j8sPS | 2.5171 |
| 2O6qc | fork-SeniorCareMarket-mmllm-claude-train-sym24-e2639fee-2O6qc | 2.7276 |
| 3kQJF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-aa798304-3kQJF | 2.9084 |
| A1wnS | fork-joly-os-mmllm-claude-train-sym24-ea489e21-A1wnS | 2.9208 |
| n5o8v | origin/claude/train-sym24-004abb66-n5o8v | 2.9323 |
| **mean** | | **2.8012** |
| **best** | | **2.5171** |

## Chain progression R1017 → R1018

Previous harvest: `workers/dispatcher/harvest-6way-r1017_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6004         | 2.8012         | +0.2008 |
| ctrl_bpc best  | 2.5254         | 2.5171         | -0.0083 |

## Per-round trajectory (best bird: j8sPS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1018 | 6574 | 2.5171 | +0.1792 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1017_sym24`
  - `workers/dispatcher/harvest-4way-r1017_sym24`

## Output

`workers/dispatcher/harvest-5way-r1018_sym24/round-1018/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

