# harvest-6way-r626 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R626 ctrl_bpc |
|--------|--------|--------------:|
| Eqwrk | fork-SeniorCareMarket-mmllm-claude-train-sym24-c0654340-Eqwrk | 2.1252 |
| msQdJ | fork-slaa-us-mmllm-claude-train-sym24-f5811827-msQdJ | 2.1349 |
| b08Eh | fork-davidwuchn-mmllm-claude-train-sym24-eddebda3-b08Eh | 2.1351 |
| dc5MB | fork-joly-os-mmllm-claude-train-sym24-d850fb2d-dc5MB | 2.1379 |
| 4ppWS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-51fb6dc0-4ppWS | 2.1394 |
| Os8kT | origin/claude/train-sym24-699f6cb8-Os8kT | 2.3263 |
| **mean** | | **2.1665** |
| **best** | | **2.1252** |

## Chain progression R625 → R626

Previous harvest: `workers/dispatcher/harvest-5way-r625_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3459         | 2.1665         | -0.1794 |
| ctrl_bpc best  | 2.1361         | 2.1252         | -0.0109 |

## Per-round trajectory (best bird: Eqwrk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 626 | 4598 | 2.1252 | +0.0439 |

## Cumulative training contribution

- This harvest: **300 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1050 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r625_sym24`

## Output

`workers/dispatcher/harvest-6way-r626_sym24/round-626/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

