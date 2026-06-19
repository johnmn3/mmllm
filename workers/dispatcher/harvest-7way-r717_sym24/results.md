# harvest-7way-r717 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R717 ctrl_bpc |
|--------|--------|--------------:|
| PctHA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-52004440-PctHA | 3.5196 |
| 2lIgh | fork-joly-os-mmllm-claude-train-sym24-ca86db66-2lIgh | 3.5525 |
| Zvuh3 | origin/claude/train-sym24-dda225c0-Zvuh3 | 3.5606 |
| nJjiG | fork-joly-os-mmllm-claude-train-sym24-8adfbbeb-nJjiG | 3.5649 |
| ggklZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-1b131367-ggklZ | 3.5682 |
| Gwl6M | fork-slaa-us-mmllm-claude-train-sym24-a3ee9a8d-Gwl6M | 3.6017 |
| QfuMo | fork-davidwuchn-mmllm-claude-train-sym24-f885ef3c-QfuMo | 3.8699 |
| **mean** | | **3.6053** |
| **best** | | **3.5196** |

## Chain progression R716 → R717

Previous harvest: `workers/dispatcher/harvest-16way-r716_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7053         | 3.6053         | -0.1000 |
| ctrl_bpc best  | 3.5587         | 3.5196         | -0.0391 |

## Per-round trajectory (best bird: PctHA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 717 | 6302 | 3.5196 | +0.6759 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r716_sym24`
  - `workers/dispatcher/harvest-6way-r716_sym24`

## Output

`workers/dispatcher/harvest-7way-r717_sym24/round-717/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

