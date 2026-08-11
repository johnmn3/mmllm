# harvest-9way-r1175 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1175 ctrl_bpc |
|--------|--------|--------------:|
| Tmjjb | origin/claude/train-sym24-642d7d97-Tmjjb | 2.3243 |
| yrIDw | fork-joly-os-mmllm-claude-train-sym24-a378d2ae-yrIDw | 2.3279 |
| gtfvJ | fork-joly-os-mmllm-claude-train-sym24-06207983-gtfvJ | 2.3307 |
| 9DgCa | fork-slaa-us-mmllm-claude-train-sym24-4f42c0aa-9DgCa | 2.3352 |
| 0lmZG | origin/claude/train-sym24-e70fdc90-0lmZG | 2.5120 |
| SgQ32 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5385a4a8-SgQ32 | 2.5126 |
| cp4sP | fork-SeniorCareMarket-mmllm-claude-train-sym24-5b30c761-cp4sP | 2.7015 |
| UvUtx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4d1f059a-UvUtx | 2.7023 |
| pEevi | origin/claude/train-sym24-d9cc02e4-pEevi | 2.7049 |
| **mean** | | **2.4946** |
| **best** | | **2.3243** |

## Chain progression R1174 → R1175

Previous harvest: `workers/dispatcher/harvest-6way-r1174_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4812         | 2.4946         | +0.0134 |
| ctrl_bpc best  | 2.3127         | 2.3243         | +0.0116 |

## Per-round trajectory (best bird: Tmjjb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1175 | 6446 | 2.3243 | +0.2435 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1174_sym24`
  - `workers/dispatcher/harvest-6way-r1174_sym24`

## Output

`workers/dispatcher/harvest-9way-r1175_sym24/round-1175/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

