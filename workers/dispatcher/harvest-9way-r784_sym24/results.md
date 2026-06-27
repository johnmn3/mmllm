# harvest-9way-r784 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R784 ctrl_bpc |
|--------|--------|--------------:|
| nFNdF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1385be1e-nFNdF | 3.1626 |
| AitCB | fork-SeniorCareMarket-mmllm-claude-train-sym24-055c62c4-AitCB | 3.1683 |
| eLmfI | origin/claude/train-sym24-2cde51d4-eLmfI | 3.1991 |
| lMgvC | fork-slaa-us-mmllm-claude-train-sym24-994323bf-lMgvC | 3.2007 |
| 9QDMm | fork-davidwuchn-mmllm-claude-train-sym24-60e895e3-9QDMm | 3.3032 |
| 007j8 | fork-slaa-us-mmllm-claude-train-sym24-b843dd30-007j8 | 3.3106 |
| ZQlTU | origin/claude/train-sym24-3647b58c-ZQlTU | 3.3124 |
| 3bNnB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2a192c2d-3bNnB | 3.5603 |
| bzKMw | fork-joly-os-mmllm-claude-train-sym24-56225715-bzKMw | 3.5718 |
| **mean** | | **3.3099** |
| **best** | | **3.1626** |

## Chain progression R783 → R784

Previous harvest: `workers/dispatcher/harvest-10way-r783_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3778         | 3.3099         | -0.0679 |
| ctrl_bpc best  | 3.1869         | 3.1626         | -0.0243 |

## Per-round trajectory (best bird: nFNdF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 784 | 6797 | 3.1626 | +0.4613 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r783_sym24`

## Output

`workers/dispatcher/harvest-9way-r784_sym24/round-784/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

