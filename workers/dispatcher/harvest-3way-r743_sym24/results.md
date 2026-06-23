# harvest-3way-r743 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R743 ctrl_bpc |
|--------|--------|--------------:|
| eYEAY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-64f756ad-eYEAY | 3.3924 |
| DqQpn | fork-slaa-us-mmllm-claude-train-sym24-626212a8-DqQpn | 3.7203 |
| snHgD | fork-davidwuchn-mmllm-claude-train-sym24-c0acafaf-snHgD | 3.7232 |
| **mean** | | **3.6120** |
| **best** | | **3.3924** |

## Chain progression R742 → R743

Previous harvest: `workers/dispatcher/harvest-11way-r742_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4815         | 3.6120         | +0.1305 |
| ctrl_bpc best  | 3.3918         | 3.3924         | +0.0006 |

## Per-round trajectory (best bird: eYEAY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 743 | 5276 | 3.3924 | +0.8540 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r742_sym24`

## Output

`workers/dispatcher/harvest-3way-r743_sym24/round-743/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

