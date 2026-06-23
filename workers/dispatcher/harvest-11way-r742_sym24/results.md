# harvest-11way-r742 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R742 ctrl_bpc |
|--------|--------|--------------:|
| XGWBt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cf28e590-XGWBt | 3.3918 |
| TjmOr | fork-slaa-us-mmllm-claude-train-sym24-59f85df9-TjmOr | 3.4060 |
| GRJpV | fork-davidwuchn-mmllm-claude-train-sym24-ed363835-GRJpV | 3.4135 |
| jEy4l | fork-davidwuchn-mmllm-claude-train-sym24-aae9faf2-jEy4l | 3.4145 |
| zlabk | fork-SeniorCareMarket-mmllm-claude-train-sym24-077af999-zlabk | 3.4191 |
| Hewby | fork-joly-os-mmllm-claude-train-sym24-3e9f1ab8-Hewby | 3.4264 |
| oU8tN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-beef1392-oU8tN | 3.4452 |
| Gxw8K | fork-joly-os-mmllm-claude-train-sym24-01054dd3-Gxw8K | 3.4492 |
| 97Cjy | origin/claude/train-sym24-d68434a1-97Cjy | 3.4587 |
| Wu7IY | origin/claude/train-sym24-41585e84-Wu7IY | 3.7339 |
| lyJN1 | fork-slaa-us-mmllm-claude-train-sym24-08de5c9d-lyJN1 | 3.7379 |
| **mean** | | **3.4815** |
| **best** | | **3.3918** |

## Chain progression R741 → R742

Previous harvest: `workers/dispatcher/harvest-8way-r741_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4986         | 3.4815         | -0.0171 |
| ctrl_bpc best  | 3.3928         | 3.3918         | -0.0010 |

## Per-round trajectory (best bird: XGWBt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 742 | 6732 | 3.3918 | +0.5817 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r741_sym24`
  - `workers/dispatcher/harvest-8way-r741_sym24`

## Output

`workers/dispatcher/harvest-11way-r742_sym24/round-742/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

