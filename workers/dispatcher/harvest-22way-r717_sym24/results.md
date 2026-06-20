# harvest-22way-r717 — sparse-delta merge of 22 birds

## Worker endpoints

| handle | branch | R717 ctrl_bpc |
|--------|--------|--------------:|
| qp1nP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-080fc1b2-qp1nP | 3.5106 |
| BY228 | fork-davidwuchn-mmllm-claude-train-sym24-ed3f597f-BY228 | 3.5129 |
| uUFTt | fork-slaa-us-mmllm-claude-train-sym24-ede8f827-uUFTt | 3.5144 |
| PaBdU | fork-slaa-us-mmllm-claude-train-sym24-b5105cbc-PaBdU | 3.5162 |
| PctHA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-52004440-PctHA | 3.5196 |
| 4ANEu | fork-SeniorCareMarket-mmllm-claude-train-sym24-9bfe80c4-4ANEu | 3.5223 |
| h2op1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-829b5ffb-h2op1 | 3.5224 |
| MuQM2 | fork-joly-os-mmllm-claude-train-sym24-06330e7b-MuQM2 | 3.5273 |
| khZnZ | fork-slaa-us-mmllm-claude-train-sym24-a5eba93a-khZnZ | 3.5300 |
| 2O8zf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4e392d9b-2O8zf | 3.5424 |
| 2lIgh | fork-joly-os-mmllm-claude-train-sym24-ca86db66-2lIgh | 3.5525 |
| U63XS | origin/claude/train-sym24-3c6348c8-U63XS | 3.5565 |
| JU4Ot | fork-davidwuchn-mmllm-claude-train-sym24-a8844484-JU4Ot | 3.5567 |
| Zvuh3 | origin/claude/train-sym24-dda225c0-Zvuh3 | 3.5606 |
| nJjiG | fork-joly-os-mmllm-claude-train-sym24-8adfbbeb-nJjiG | 3.5649 |
| ggklZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-1b131367-ggklZ | 3.5682 |
| jzKBM | origin/claude/train-sym24-0164432d-jzKBM | 3.5776 |
| NXmIt | fork-davidwuchn-mmllm-claude-train-sym24-7c4d47ef-NXmIt | 3.5779 |
| Gwl6M | fork-slaa-us-mmllm-claude-train-sym24-a3ee9a8d-Gwl6M | 3.6017 |
| IBFAb | origin/claude/train-sym24-c250d436-IBFAb | 3.8443 |
| KPjMA | fork-joly-os-mmllm-claude-train-sym24-7b7567c0-KPjMA | 3.8612 |
| QfuMo | fork-davidwuchn-mmllm-claude-train-sym24-f885ef3c-QfuMo | 3.8699 |
| **mean** | | **3.5868** |
| **best** | | **3.5106** |

## Chain progression R716 → R717

Previous harvest: `workers/dispatcher/harvest-6way-r716_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5769         | 3.5868         | +0.0099 |
| ctrl_bpc best  | 3.5587         | 3.5106         | -0.0481 |

## Per-round trajectory (best bird: qp1nP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 717 | 6632 | 3.5106 | +0.8158 |

## Cumulative training contribution

- This harvest: **1760 steps** from 22 bird(s)
- Across full ancestry (deduped by bird_id): **2240 steps** from 28 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r716_sym24`
  - `workers/dispatcher/harvest-16way-r716_sym24`
  - `workers/dispatcher/harvest-4way-r716_sym24`
  - `workers/dispatcher/harvest-6way-r716_sym24`

## Output

`workers/dispatcher/harvest-22way-r717_sym24/round-717/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 22 workers)
- `dense.pt` (averaged across 22 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

