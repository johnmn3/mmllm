# harvest-6way-r810 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R810 ctrl_bpc |
|--------|--------|--------------:|
| hFEEh | fork-slaa-us-mmllm-claude-train-sym24-af1be205-hFEEh | 3.0707 |
| D5oJO | fork-joly-os-mmllm-claude-train-sym24-cf2d77d1-D5oJO | 3.1979 |
| pu2IK | fork-davidwuchn-mmllm-claude-train-sym24-f4f0c4bf-pu2IK | 3.4325 |
| ZxuPZ | origin/claude/train-sym24-f777a4be-ZxuPZ | 3.4371 |
| IB98R | fork-slaa-us-mmllm-claude-train-sym24-66bd0b9f-IB98R | 3.4509 |
| kpnIO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4f00a92e-kpnIO | 3.4511 |
| **mean** | | **3.3400** |
| **best** | | **3.0707** |

## Chain progression R809 → R810

Previous harvest: `workers/dispatcher/harvest-2way-r809_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3095         | 3.3400         | +0.0305 |
| ctrl_bpc best  | 3.1896         | 3.0707         | -0.1189 |

## Per-round trajectory (best bird: hFEEh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 810 | 6598 | 3.0707 | +0.5437 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r809_sym24`

## Output

`workers/dispatcher/harvest-6way-r810_sym24/round-810/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

