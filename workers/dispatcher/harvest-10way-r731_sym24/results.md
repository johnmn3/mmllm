# harvest-10way-r731 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R731 ctrl_bpc |
|--------|--------|--------------:|
| JXJPb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-aee8c95e-JXJPb | 3.4225 |
| Vu50r | origin/claude/train-sym24-c64c0078-Vu50r | 3.4277 |
| Uapab | fork-joly-os-mmllm-claude-train-sym24-14a677c6-Uapab | 3.4283 |
| Zj4pL | origin/claude/train-sym24-4e301467-Zj4pL | 3.4628 |
| dpw3Q | fork-slaa-us-mmllm-claude-train-sym24-42fbc0e0-dpw3Q | 3.4782 |
| 70TZm | fork-SeniorCareMarket-mmllm-claude-train-sym24-a8b85487-70TZm | 3.4904 |
| BYQQ3 | fork-slaa-us-mmllm-claude-train-sym24-43f9cc78-BYQQ3 | 3.5010 |
| 55xpk | fork-davidwuchn-mmllm-claude-train-sym24-bd51ffd3-55xpk | 3.7926 |
| dsjDl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-079b7b67-dsjDl | 3.7991 |
| C911m | fork-davidwuchn-mmllm-claude-train-sym24-01258871-C911m | 3.8195 |
| **mean** | | **3.5622** |
| **best** | | **3.4225** |

## Chain progression R730 → R731

Previous harvest: `workers/dispatcher/harvest-6way-r730_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5244         | 3.5622         | +0.0378 |
| ctrl_bpc best  | 3.4270         | 3.4225         | -0.0045 |

## Per-round trajectory (best bird: JXJPb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 731 | 6366 | 3.4225 | +0.5616 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r730_sym24`

## Output

`workers/dispatcher/harvest-10way-r731_sym24/round-731/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

