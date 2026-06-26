# harvest-4way-r772 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R772 ctrl_bpc |
|--------|--------|--------------:|
| MJVer | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a5642975-MJVer | 3.2130 |
| DFipy | origin/claude/train-sym24-dafa657a-DFipy | 3.2213 |
| B8G7V | fork-joly-os-mmllm-claude-train-sym24-45f437e0-B8G7V | 3.2611 |
| c5meL | fork-davidwuchn-mmllm-claude-train-sym24-10475343-c5meL | 3.3478 |
| **mean** | | **3.2608** |
| **best** | | **3.2130** |

## Chain progression R771 → R772

Previous harvest: `workers/dispatcher/harvest-3way-r771_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4973         | 3.2608         | -0.2365 |
| ctrl_bpc best  | 3.2597         | 3.2130         | -0.0467 |

## Per-round trajectory (best bird: MJVer)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 772 | 6354 | 3.2130 | +0.6568 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r771_sym24`

## Output

`workers/dispatcher/harvest-4way-r772_sym24/round-772/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

