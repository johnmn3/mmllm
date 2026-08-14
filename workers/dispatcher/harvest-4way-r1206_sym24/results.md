# harvest-4way-r1206 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1206 ctrl_bpc |
|--------|--------|--------------:|
| cWPHA | fork-SeniorCareMarket-mmllm-claude-train-sym24-260f15ff-cWPHA | 2.2851 |
| WUi3u | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-71d70e3b-WUi3u | 2.2991 |
| 6UPjb | fork-slaa-us-mmllm-claude-train-sym24-3b7b1406-6UPjb | 2.6749 |
| cQAhJ | fork-joly-os-mmllm-claude-train-sym24-3f948b2f-cQAhJ | 2.6858 |
| **mean** | | **2.4862** |
| **best** | | **2.2851** |

## Chain progression R1205 → R1206

Previous harvest: `workers/dispatcher/harvest-10way-r1205_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4192         | 2.4862         | +0.0670 |
| ctrl_bpc best  | 2.2714         | 2.2851         | +0.0137 |

## Per-round trajectory (best bird: cWPHA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1206 | 6393 | 2.2851 | +0.2512 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1205_sym24`

## Output

`workers/dispatcher/harvest-4way-r1206_sym24/round-1206/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

