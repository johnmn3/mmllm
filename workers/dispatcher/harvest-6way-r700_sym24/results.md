# harvest-6way-r700 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R700 ctrl_bpc |
|--------|--------|--------------:|
| H1vI3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4efbe626-H1vI3 | 3.6314 |
| OGvSX | fork-joly-os-mmllm-claude-train-sym24-7b408469-OGvSX | 3.6717 |
| DR8DH | fork-slaa-us-mmllm-claude-train-sym24-6b7db928-DR8DH | 3.6722 |
| 19VHX | origin/claude/train-sym24-cf60a9ea-19VHX | 3.6936 |
| URYC3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-616bf557-URYC3 | 3.9726 |
| fOCWT | fork-davidwuchn-mmllm-claude-train-sym24-bae85563-fOCWT | 3.9886 |
| **mean** | | **3.7717** |
| **best** | | **3.6314** |

## Chain progression R699 → R700

Previous harvest: `workers/dispatcher/harvest-10way-r699_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7866         | 3.7717         | -0.0149 |
| ctrl_bpc best  | 3.6203         | 3.6314         | +0.0111 |

## Per-round trajectory (best bird: H1vI3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 700 | 6580 | 3.6314 | +0.6094 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r699_sym24`
  - `workers/dispatcher/harvest-4way-r699_sym24`

## Output

`workers/dispatcher/harvest-6way-r700_sym24/round-700/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

