# harvest-6way-r754 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R754 ctrl_bpc |
|--------|--------|--------------:|
| wlPl8 | fork-slaa-us-mmllm-claude-train-sym24-deeb74cd-wlPl8 | 3.3056 |
| vviI7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ab77f42f-vviI7 | 3.3392 |
| bp8n0 | fork-davidwuchn-mmllm-claude-train-sym24-ee61b16c-bp8n0 | 3.3562 |
| iMbFp | fork-joly-os-mmllm-claude-train-sym24-821011d5-iMbFp | 3.4089 |
| lzrXF | origin/claude/train-sym24-c394d870-lzrXF | 3.4137 |
| EiEf0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-27d1df1e-EiEf0 | 3.7075 |
| **mean** | | **3.4219** |
| **best** | | **3.3056** |

## Chain progression R753 → R754

Previous harvest: `workers/dispatcher/harvest-11way-r753_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3575         | 3.4219         | +0.0644 |
| ctrl_bpc best  | 3.3141         | 3.3056         | -0.0085 |

## Per-round trajectory (best bird: wlPl8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 754 | 6548 | 3.3056 | +0.6565 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r753_sym24`

## Output

`workers/dispatcher/harvest-6way-r754_sym24/round-754/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

