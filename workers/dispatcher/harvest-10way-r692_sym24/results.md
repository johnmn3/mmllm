# harvest-10way-r692 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R692 ctrl_bpc |
|--------|--------|--------------:|
| GdvPA | origin/claude/train-sym24-92f125d9-GdvPA | 3.6828 |
| D9C4C | fork-SeniorCareMarket-mmllm-claude-train-sym24-884c2255-D9C4C | 3.6856 |
| T9VFc | fork-davidwuchn-mmllm-claude-train-sym24-abfdf1e2-T9VFc | 3.6920 |
| HEDQB | fork-joly-os-mmllm-claude-train-sym24-21784500-HEDQB | 3.6988 |
| SHl46 | fork-slaa-us-mmllm-claude-train-sym24-16c7a262-SHl46 | 3.7041 |
| FSCdz | origin/claude/train-sym24-9676c95e-FSCdz | 3.7134 |
| phfp4 | fork-joly-os-mmllm-claude-train-sym24-64e193cd-phfp4 | 3.7206 |
| NcV9N | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f6dd82d1-NcV9N | 3.7286 |
| hDjRD | fork-slaa-us-mmllm-claude-train-sym24-7962ec9d-hDjRD | 3.7519 |
| jIJyC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-249135c4-jIJyC | 4.0476 |
| **mean** | | **3.7425** |
| **best** | | **3.6828** |

## Chain progression R691 → R692

Previous harvest: `workers/dispatcher/harvest-6way-r691_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8241         | 3.7425         | -0.0816 |
| ctrl_bpc best  | 3.6923         | 3.6828         | -0.0095 |

## Per-round trajectory (best bird: GdvPA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 692 | 6398 | 3.6828 | +0.4303 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r691_sym24`
  - `workers/dispatcher/harvest-6way-r691_sym24`

## Output

`workers/dispatcher/harvest-10way-r692_sym24/round-692/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

