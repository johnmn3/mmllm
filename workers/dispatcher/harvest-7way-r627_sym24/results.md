# harvest-7way-r627 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R627 ctrl_bpc |
|--------|--------|--------------:|
| MUmeK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d419bba8-MUmeK | 2.1248 |
| J2H5G | fork-joly-os-mmllm-claude-train-sym24-0b7e2730-J2H5G | 2.1344 |
| aYiSV | fork-SeniorCareMarket-mmllm-claude-train-sym24-dc3f79b8-aYiSV | 2.1356 |
| YWMp9 | fork-slaa-us-mmllm-claude-train-sym24-be6ae0d2-YWMp9 | 2.1379 |
| 6fpWh | fork-davidwuchn-mmllm-claude-train-sym24-89c0b3c8-6fpWh | 2.3318 |
| hXPYB | fork-joly-os-mmllm-claude-train-sym24-b5a20786-hXPYB | 2.3319 |
| 3kNci | origin/claude/train-sym24-a90ca430-3kNci | 2.3354 |
| **mean** | | **2.2188** |
| **best** | | **2.1248** |

## Chain progression R626 → R627

Previous harvest: `workers/dispatcher/harvest-6way-r626_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1665         | 2.2188         | +0.0523 |
| ctrl_bpc best  | 2.1252         | 2.1248         | -0.0004 |

## Per-round trajectory (best bird: MUmeK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 627 | 5439 | 2.1248 | +0.0462 |

## Cumulative training contribution

- This harvest: **350 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1150 steps** from 23 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r626_sym24`

## Output

`workers/dispatcher/harvest-7way-r627_sym24/round-627/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

