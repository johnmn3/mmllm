# harvest-11way-r609 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R609 ctrl_bpc |
|--------|--------|--------------:|
| ZyM3b | fork-slaa-us-mmllm-claude-train-sym24-9d116e8c-ZyM3b | 2.1268 |
| 1lUk0 | fork-joly-os-mmllm-claude-train-sym24-b5b0f87e-1lUk0 | 2.1272 |
| 1loUu | fork-slaa-us-mmllm-claude-train-sym24-330d9c2d-1loUu | 2.1275 |
| mljo8 | fork-davidwuchn-mmllm-claude-train-sym24-7b4c6c4f-mljo8 | 2.1275 |
| bPtlU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-be0c7c7d-bPtlU | 2.1291 |
| 0tRpa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3bb7db90-0tRpa | 2.1485 |
| SvD15 | origin/claude/train-sym24-069a9928-SvD15 | 2.1503 |
| 2oufV | origin/claude/train-sym24-347724cc-2oufV | 2.3509 |
| qEpQF | fork-joly-os-mmllm-claude-train-sym24-814c2a8d-qEpQF | 2.3521 |
| LVI2Z | fork-davidwuchn-mmllm-claude-train-sym24-b32817a1-LVI2Z | 2.3539 |
| TaDnO | fork-SeniorCareMarket-mmllm-claude-train-sym24-cefb129a-TaDnO | 2.6059 |
| **mean** | | **2.2363** |
| **best** | | **2.1268** |

## Chain progression R607 → R609

Previous harvest: `workers/dispatcher/harvest-2way-merge-r607_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1495         | 2.2363         | +0.0868 |
| ctrl_bpc best  | 2.1266         | 2.1268         | +0.0002 |

## Per-round trajectory (best bird: ZyM3b)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 609 | 5240 | 2.1268 | +0.0203 |

## Cumulative training contribution

- This harvest: **550 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **550 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r608_sym24`

## Output

`workers/dispatcher/harvest-11way-r609_sym24/round-609/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

