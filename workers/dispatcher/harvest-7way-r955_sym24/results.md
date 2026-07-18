# harvest-7way-r955 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R955 ctrl_bpc |
|--------|--------|--------------:|
| 1YfUV | origin/claude/train-sym24-f3f79e18-1YfUV | 2.6530 |
| XEwb3 | origin/claude/train-sym24-bdb4b4bf-XEwb3 | 2.6637 |
| N9GLa | fork-SeniorCareMarket-mmllm-claude-train-sym24-5fe36b14-N9GLa | 2.6675 |
| 9NSsV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-df15b6e9-9NSsV | 2.8487 |
| hp2mJ | fork-joly-os-mmllm-claude-train-sym24-62d0e993-hp2mJ | 3.0457 |
| JaMRQ | fork-joly-os-mmllm-claude-train-sym24-12e51668-JaMRQ | 3.0622 |
| 95nLR | fork-slaa-us-mmllm-claude-train-sym24-b4e8cb9b-95nLR | 3.0720 |
| **mean** | | **2.8590** |
| **best** | | **2.6530** |

## Chain progression R954 → R955

Previous harvest: `workers/dispatcher/harvest-9way-r954_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7679         | 2.8590         | +0.0911 |
| ctrl_bpc best  | 2.6476         | 2.6530         | +0.0054 |

## Per-round trajectory (best bird: 1YfUV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 955 | 6594 | 2.6530 | +0.1548 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r954_sym24`
  - `workers/dispatcher/harvest-6way-r954_sym24`

## Output

`workers/dispatcher/harvest-7way-r955_sym24/round-955/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

