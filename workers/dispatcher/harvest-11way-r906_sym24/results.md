# harvest-11way-r906 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R906 ctrl_bpc |
|--------|--------|--------------:|
| oeaPv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-90919d8e-oeaPv | 2.7678 |
| lxWjg | origin/claude/train-sym24-8f3c5a4d-lxWjg | 2.7693 |
| GHlBv | fork-SeniorCareMarket-mmllm-claude-train-sym24-80aa96ac-GHlBv | 2.7713 |
| PMzcn | fork-joly-os-mmllm-claude-train-sym24-f54706d8-PMzcn | 2.7776 |
| TlkS5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-32f5952c-TlkS5 | 2.7807 |
| DB3Pq | origin/claude/train-sym24-b1ea8a27-DB3Pq | 2.9571 |
| 8F99t | fork-slaa-us-mmllm-claude-train-sym24-3b31ed81-8F99t | 2.9573 |
| ZdFXa | fork-SeniorCareMarket-mmllm-claude-train-sym24-c70f607a-ZdFXa | 2.9600 |
| yGPN1 | fork-joly-os-mmllm-claude-train-sym24-2ecebf4c-yGPN1 | 2.9716 |
| Q8ehx | fork-slaa-us-mmllm-claude-train-sym24-43b84af7-Q8ehx | 3.1444 |
| riC4H | origin/claude/train-sym24-a2beccd2-riC4H | 3.1556 |
| **mean** | | **2.9102** |
| **best** | | **2.7678** |

## Chain progression R905 → R906

Previous harvest: `workers/dispatcher/harvest-5way-r905_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8930         | 2.9102         | +0.0172 |
| ctrl_bpc best  | 2.7738         | 2.7678         | -0.0060 |

## Per-round trajectory (best bird: oeaPv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 906 | 6538 | 2.7678 | +0.2667 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r905_sym24`
  - `workers/dispatcher/harvest-5way-r905_sym24`

## Output

`workers/dispatcher/harvest-11way-r906_sym24/round-906/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

