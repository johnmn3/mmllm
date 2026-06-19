# harvest-4way-r716 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R716 ctrl_bpc |
|--------|--------|--------------:|
| zIX2b | fork-slaa-us-mmllm-claude-train-sym24-1cb703b3-zIX2b | 3.5587 |
| ziVwt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1516b110-ziVwt | 3.5872 |
| Ra4Mx | fork-davidwuchn-mmllm-claude-train-sym24-6b78abb1-Ra4Mx | 3.5876 |
| Hpqmk | fork-joly-os-mmllm-claude-train-sym24-32364c14-Hpqmk | 3.5954 |
| **mean** | | **3.5822** |
| **best** | | **3.5587** |

## Chain progression R715 → R716

Previous harvest: `workers/dispatcher/harvest-10way-r715_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7824         | 3.5822         | -0.2002 |
| ctrl_bpc best  | 3.5691         | 3.5587         | -0.0104 |

## Per-round trajectory (best bird: zIX2b)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 716 | 6498 | 3.5587 | +0.8729 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r715_sym24`

## Output

`workers/dispatcher/harvest-4way-r716_sym24/round-716/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

