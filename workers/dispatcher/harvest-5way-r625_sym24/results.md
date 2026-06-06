# harvest-5way-r625 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R625 ctrl_bpc |
|--------|--------|--------------:|
| Ba9Pc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-854b91a1-Ba9Pc | 2.1361 |
| Ga4mZ | fork-slaa-us-mmllm-claude-train-sym24-2719c736-Ga4mZ | 2.3328 |
| jFS2f | fork-davidwuchn-mmllm-claude-train-sym24-de5d1f13-jFS2f | 2.3356 |
| PW2Jx | fork-joly-os-mmllm-claude-train-sym24-17460286-PW2Jx | 2.3361 |
| jmPqu | origin/claude/train-sym24-c7f29e67-jmPqu | 2.5887 |
| **mean** | | **2.3459** |
| **best** | | **2.1361** |

## Chain progression R624 → R625

Previous harvest: `workers/dispatcher/harvest-5way-r624_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3075         | 2.3459         | +0.0384 |
| ctrl_bpc best  | 2.1385         | 2.1361         | -0.0024 |

## Per-round trajectory (best bird: Ba9Pc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 625 | 5527 | 2.1361 | +0.0499 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **950 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r624_sym24`

## Output

`workers/dispatcher/harvest-5way-r625_sym24/round-625/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

