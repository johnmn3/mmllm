# harvest-4way-r760 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R760 ctrl_bpc |
|--------|--------|--------------:|
| FHy8M | fork-davidwuchn-mmllm-claude-train-sym24-022b7390-FHy8M | 3.3175 |
| W2I3S | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-eb3f7c26-W2I3S | 3.3837 |
| Mh7b6 | fork-slaa-us-mmllm-claude-train-sym24-501b2443-Mh7b6 | 3.6450 |
| k3pij | fork-davidwuchn-mmllm-claude-train-sym24-24f699d3-k3pij | 3.6588 |
| **mean** | | **3.5012** |
| **best** | | **3.3175** |

## Chain progression R759 → R760

Previous harvest: `workers/dispatcher/harvest-7way-r759_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4292         | 3.5012         | +0.0720 |
| ctrl_bpc best  | 3.2800         | 3.3175         | +0.0375 |

## Per-round trajectory (best bird: FHy8M)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 760 | 6534 | 3.3175 | +0.6748 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r759_sym24`

## Output

`workers/dispatcher/harvest-4way-r760_sym24/round-760/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

