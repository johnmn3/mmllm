# harvest-7way-r1305 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1305 ctrl_bpc |
|--------|--------|--------------:|
| J4si2 | fork-slaa-us-mmllm-claude-train-sym24-02d3febc-J4si2 | 3.4799 |
| FdZ10 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f5466cbb-FdZ10 | 3.4957 |
| qCeme | fork-slaa-us-mmllm-claude-train-sym24-8e5dd6fe-qCeme | 3.5197 |
| giF6J | fork-joly-os-mmllm-claude-train-sym24-aea9dda0-giF6J | 3.5602 |
| YxsoF | fork-joly-os-mmllm-claude-train-sym24-92084002-YxsoF | 3.8556 |
| 71NB4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9bd5f108-71NB4 | 3.8571 |
| AFIAh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-33d7a723-AFIAh | 3.8674 |
| **mean** | | **3.6622** |
| **best** | | **3.4799** |

## Chain progression R1304 → R1305

Previous harvest: `workers/dispatcher/harvest-5way-r1304_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6270         | 3.6622         | +0.0352 |
| ctrl_bpc best  | 3.5458         | 3.4799         | -0.0659 |

## Per-round trajectory (best bird: J4si2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1305 | 3531 | 3.4799 | +0.0526 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1304_sym24`
  - `workers/dispatcher/harvest-5way-r1304_sym24`

## Output

`workers/dispatcher/harvest-7way-r1305_sym24/round-1305/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

