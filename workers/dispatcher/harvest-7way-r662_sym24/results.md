# harvest-7way-r662 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R662 ctrl_bpc |
|--------|--------|--------------:|
| CP1n3 | origin/claude/train-sym24-bd1b8fe6-CP1n3 | 3.9717 |
| YjFUZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c745defd-YjFUZ | 3.9780 |
| fCpPU | fork-SeniorCareMarket-mmllm-claude-train-sym24-e3d0f438-fCpPU | 3.9802 |
| 3vgZA | fork-joly-os-mmllm-claude-train-sym24-605ec2f9-3vgZA | 3.9866 |
| mGXrN | fork-slaa-us-mmllm-claude-train-sym24-dce6a368-mGXrN | 4.0226 |
| CdMmV | fork-davidwuchn-mmllm-claude-train-sym24-7fed1377-CdMmV | 4.3238 |
| aBsTP | fork-davidwuchn-mmllm-claude-train-sym24-7b07178d-aBsTP | 4.3915 |
| **mean** | | **4.0935** |
| **best** | | **3.9717** |

## Chain progression R661 → R662

Previous harvest: `workers/dispatcher/harvest-1way-r661_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0532         | 4.0935         | +0.0403 |
| ctrl_bpc best  | 4.0532         | 3.9717         | -0.0815 |

## Per-round trajectory (best bird: CP1n3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 662 | 6798 | 3.9717 | +0.1709 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r661_sym24`

## Output

`workers/dispatcher/harvest-7way-r662_sym24/round-662/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

