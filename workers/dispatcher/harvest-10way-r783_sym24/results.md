# harvest-10way-r783 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R783 ctrl_bpc |
|--------|--------|--------------:|
| sWH1Q | fork-SeniorCareMarket-mmllm-claude-train-sym24-fd39a753-sWH1Q | 3.1869 |
| eiA2H | fork-SeniorCareMarket-mmllm-claude-train-sym24-30f128e3-eiA2H | 3.2087 |
| x8QKy | origin/claude/train-sym24-c8b5da9e-x8QKy | 3.2182 |
| ctkwR | fork-slaa-us-mmllm-claude-train-sym24-922f36e4-ctkwR | 3.3084 |
| DnjBk | fork-davidwuchn-mmllm-claude-train-sym24-9b79f25a-DnjBk | 3.3169 |
| vp9qs | fork-davidwuchn-mmllm-claude-train-sym24-3897664d-vp9qs | 3.3172 |
| NTbQ3 | fork-joly-os-mmllm-claude-train-sym24-0802f199-NTbQ3 | 3.5456 |
| HKIod | fork-slaa-us-mmllm-claude-train-sym24-5fd98002-HKIod | 3.5580 |
| U5jvY | fork-joly-os-mmllm-claude-train-sym24-899d7c83-U5jvY | 3.5587 |
| n5wiH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b737efc2-n5wiH | 3.5591 |
| **mean** | | **3.3778** |
| **best** | | **3.1869** |

## Chain progression R782 → R783

Previous harvest: `workers/dispatcher/harvest-17way-r782_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2967         | 3.3778         | +0.0811 |
| ctrl_bpc best  | 3.1844         | 3.1869         | +0.0025 |

## Per-round trajectory (best bird: sWH1Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 783 | 6472 | 3.1869 | +0.6227 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r782_sym24`
  - `workers/dispatcher/harvest-6way-r782_sym24`

## Output

`workers/dispatcher/harvest-10way-r783_sym24/round-783/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

