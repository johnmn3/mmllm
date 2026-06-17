# harvest-11way-r700 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R700 ctrl_bpc |
|--------|--------|--------------:|
| SdScY | origin/claude/train-sym24-82ec80c7-SdScY | 3.6138 |
| H1vI3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4efbe626-H1vI3 | 3.6314 |
| oocFm | fork-joly-os-mmllm-claude-train-sym24-6930ebda-oocFm | 3.6445 |
| OGvSX | fork-joly-os-mmllm-claude-train-sym24-7b408469-OGvSX | 3.6717 |
| DR8DH | fork-slaa-us-mmllm-claude-train-sym24-6b7db928-DR8DH | 3.6722 |
| 0TD2u | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4782da70-0TD2u | 3.6746 |
| u7hw9 | fork-slaa-us-mmllm-claude-train-sym24-a8f70586-u7hw9 | 3.6797 |
| 19VHX | origin/claude/train-sym24-cf60a9ea-19VHX | 3.6936 |
| URYC3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-616bf557-URYC3 | 3.9726 |
| 2EHlC | fork-davidwuchn-mmllm-claude-train-sym24-0b39fa9f-2EHlC | 3.9852 |
| fOCWT | fork-davidwuchn-mmllm-claude-train-sym24-bae85563-fOCWT | 3.9886 |
| **mean** | | **3.7480** |
| **best** | | **3.6138** |

## Chain progression R699 → R700

Previous harvest: `workers/dispatcher/harvest-4way-r699_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8112         | 3.7480         | -0.0632 |
| ctrl_bpc best  | 3.6203         | 3.6138         | -0.0065 |

## Per-round trajectory (best bird: SdScY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 700 | 6664 | 3.6138 | +0.4727 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r699_sym24`
  - `workers/dispatcher/harvest-4way-r699_sym24`

## Output

`workers/dispatcher/harvest-11way-r700_sym24/round-700/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

