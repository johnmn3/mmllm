# harvest-10way-r1206 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1206 ctrl_bpc |
|--------|--------|--------------:|
| mhMAt | fork-joly-os-mmllm-claude-train-sym24-3508afd3-mhMAt | 2.2812 |
| cWPHA | fork-SeniorCareMarket-mmllm-claude-train-sym24-260f15ff-cWPHA | 2.2851 |
| lU9EH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-08d9db39-lU9EH | 2.2952 |
| WUi3u | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-71d70e3b-WUi3u | 2.2991 |
| LXJYn | fork-slaa-us-mmllm-claude-train-sym24-1aa79f7d-LXJYn | 2.4680 |
| LSsCw | fork-slaa-us-mmllm-claude-train-sym24-5fcf6a55-LSsCw | 2.4758 |
| NLN3V | origin/claude/train-sym24-c27b17fe-NLN3V | 2.6646 |
| Cajl0 | origin/claude/train-sym24-96792fec-Cajl0 | 2.6738 |
| 6UPjb | fork-slaa-us-mmllm-claude-train-sym24-3b7b1406-6UPjb | 2.6749 |
| cQAhJ | fork-joly-os-mmllm-claude-train-sym24-3f948b2f-cQAhJ | 2.6858 |
| **mean** | | **2.4804** |
| **best** | | **2.2812** |

## Chain progression R1205 → R1206

Previous harvest: `workers/dispatcher/harvest-7way-r1205_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3945         | 2.4804         | +0.0859 |
| ctrl_bpc best  | 2.2714         | 2.2812         | +0.0098 |

## Per-round trajectory (best bird: mhMAt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1206 | 6382 | 2.2812 | +0.2537 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1205_sym24`
  - `workers/dispatcher/harvest-7way-r1205_sym24`

## Output

`workers/dispatcher/harvest-10way-r1206_sym24/round-1206/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

