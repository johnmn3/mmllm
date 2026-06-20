# harvest-5way-r718 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R718 ctrl_bpc |
|--------|--------|--------------:|
| n0X4D | fork-joly-os-mmllm-claude-train-sym24-7f2b8f27-n0X4D | 3.5185 |
| jYfWX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-00fc2b0d-jYfWX | 3.5698 |
| 9V4AK | fork-davidwuchn-mmllm-claude-train-sym24-c63a4d2a-9V4AK | 3.8588 |
| dVRyh | fork-slaa-us-mmllm-claude-train-sym24-b9d40fe5-dVRyh | 3.8630 |
| 6I8iz | fork-SeniorCareMarket-mmllm-claude-train-sym24-aca3fb37-6I8iz | 3.8712 |
| **mean** | | **3.7363** |
| **best** | | **3.5185** |

## Chain progression R717 → R718

Previous harvest: `workers/dispatcher/harvest-22way-r717_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5868         | 3.7363         | +0.1495 |
| ctrl_bpc best  | 3.5106         | 3.5185         | +0.0079 |

## Per-round trajectory (best bird: n0X4D)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 718 | 6362 | 3.5185 | +0.8097 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 22 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-17way-r717_sym24`
  - `workers/dispatcher/harvest-7way-r717_sym24`

## Output

`workers/dispatcher/harvest-5way-r718_sym24/round-718/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

