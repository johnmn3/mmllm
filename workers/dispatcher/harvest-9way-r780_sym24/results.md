# harvest-9way-r780 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R780 ctrl_bpc |
|--------|--------|--------------:|
| Eie61 | fork-davidwuchn-mmllm-claude-train-sym24-1bd816a4-Eie61 | 3.1952 |
| kN2zp | fork-SeniorCareMarket-mmllm-claude-train-sym24-1018b523-kN2zp | 3.2193 |
| sgRSA | origin/claude/train-sym24-27d707b8-sgRSA | 3.2223 |
| 5lJrO | origin/claude/train-sym24-66ba2304-5lJrO | 3.3140 |
| db1Bs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bd9e59be-db1Bs | 3.3313 |
| afSHM | fork-slaa-us-mmllm-claude-train-sym24-854b6de2-afSHM | 3.3329 |
| mwg1h | fork-joly-os-mmllm-claude-train-sym24-197346e9-mwg1h | 3.5654 |
| S0tnQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65946620-S0tnQ | 3.5697 |
| xTDiR | fork-joly-os-mmllm-claude-train-sym24-d32edd25-xTDiR | 3.5699 |
| **mean** | | **3.3689** |
| **best** | | **3.1952** |

## Chain progression R779 → R780

Previous harvest: `workers/dispatcher/harvest-3way-r779_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3528         | 3.3689         | +0.0161 |
| ctrl_bpc best  | 3.2283         | 3.1952         | -0.0331 |

## Per-round trajectory (best bird: Eie61)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 780 | 6770 | 3.1952 | +0.6172 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r779_sym24`
  - `workers/dispatcher/harvest-3way-r779_sym24`

## Output

`workers/dispatcher/harvest-9way-r780_sym24/round-780/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

