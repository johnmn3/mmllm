# harvest-6way-r778 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R778 ctrl_bpc |
|--------|--------|--------------:|
| TIP3E | origin/claude/train-sym24-fb3b2607-TIP3E | 3.1993 |
| 8CkUf | fork-davidwuchn-mmllm-claude-train-sym24-47e0f867-8CkUf | 3.2210 |
| hdBuM | fork-joly-os-mmllm-claude-train-sym24-ac551a66-hdBuM | 3.2352 |
| wvgN3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d45a8841-wvgN3 | 3.2389 |
| mTO9N | fork-slaa-us-mmllm-claude-train-sym24-c85659bb-mTO9N | 3.2401 |
| B7WwU | fork-joly-os-mmllm-claude-train-sym24-bcf0e881-B7WwU | 3.2537 |
| **mean** | | **3.2314** |
| **best** | | **3.1993** |

## Chain progression R777 → R778

Previous harvest: `workers/dispatcher/harvest-19way-r777_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3845         | 3.2314         | -0.1531 |
| ctrl_bpc best  | 3.2230         | 3.1993         | -0.0237 |

## Per-round trajectory (best bird: TIP3E)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 778 | 6594 | 3.1993 | +0.5894 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r777_sym24`
  - `workers/dispatcher/harvest-6way-r777_sym24`

## Output

`workers/dispatcher/harvest-6way-r778_sym24/round-778/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

