# harvest-8way-r657 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R657 ctrl_bpc |
|--------|--------|--------------:|
| XJYPe | fork-slaa-us-mmllm-claude-train-sym24-37cc62fd-XJYPe | 4.1004 |
| 33wJS | fork-joly-os-mmllm-claude-train-sym24-b9cf0cb3-33wJS | 4.1097 |
| 9wL7d | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2658cc69-9wL7d | 4.1107 |
| Dihej | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fa18ec2e-Dihej | 4.1313 |
| r5Qc3 | fork-slaa-us-mmllm-claude-train-sym24-ac2d4d7a-r5Qc3 | 4.1766 |
| XHGuV | origin/claude/train-sym24-40fe852b-XHGuV | 4.4555 |
| Vgr0c | origin/claude/train-sym24-62d0eae3-Vgr0c | 4.4601 |
| ho5DX | fork-davidwuchn-mmllm-claude-train-sym24-2bdf764c-ho5DX | 4.4785 |
| **mean** | | **4.2529** |
| **best** | | **4.1004** |

## Chain progression R656 → R657

Previous harvest: `workers/dispatcher/harvest-10way-r656_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1969         | 4.2529         | +0.0560 |
| ctrl_bpc best  | 4.0833         | 4.1004         | +0.0171 |

## Per-round trajectory (best bird: XJYPe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 657 | 4397 | 4.1004 | +0.0763 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r656_sym24`

## Output

`workers/dispatcher/harvest-8way-r657_sym24/round-657/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

