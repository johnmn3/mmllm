# harvest-4way-r1039 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1039 ctrl_bpc |
|--------|--------|--------------:|
| GFcnr | fork-joly-os-mmllm-claude-train-sym24-00b58076-GFcnr | 2.4825 |
| m3orv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ebde86ab-m3orv | 2.4936 |
| BxtTZ | fork-slaa-us-mmllm-claude-train-sym24-6249c8ab-BxtTZ | 2.5184 |
| bYF6T | fork-SeniorCareMarket-mmllm-claude-train-sym24-3982374f-bYF6T | 2.5532 |
| **mean** | | **2.5119** |
| **best** | | **2.4825** |

## Chain progression R1038 → R1039

Previous harvest: `workers/dispatcher/harvest-2way-r1038_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6914         | 2.5119         | -0.1795 |
| ctrl_bpc best  | 2.5060         | 2.4825         | -0.0235 |

## Per-round trajectory (best bird: GFcnr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1039 | 6764 | 2.4825 | +0.1951 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1038_sym24`

## Output

`workers/dispatcher/harvest-4way-r1039_sym24/round-1039/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

