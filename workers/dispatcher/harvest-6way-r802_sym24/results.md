# harvest-6way-r802 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R802 ctrl_bpc |
|--------|--------|--------------:|
| bHezj | fork-joly-os-mmllm-claude-train-sym24-0da3ce5a-bHezj | 3.1127 |
| eGxQ8 | fork-davidwuchn-mmllm-claude-train-sym24-140db3bd-eGxQ8 | 3.1213 |
| b5E92 | origin/claude/train-sym24-92eeffb6-b5E92 | 3.1245 |
| 60hUe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-554d67dc-60hUe | 3.4667 |
| Y8ggz | fork-slaa-us-mmllm-claude-train-sym24-72e777d4-Y8ggz | 3.4687 |
| VHop8 | origin/claude/train-sym24-9b8e5fa8-VHop8 | 3.5018 |
| **mean** | | **3.2993** |
| **best** | | **3.1127** |

## Chain progression R801 → R802

Previous harvest: `workers/dispatcher/harvest-10way-r801_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2489         | 3.2993         | +0.0504 |
| ctrl_bpc best  | 3.0870         | 3.1127         | +0.0257 |

## Per-round trajectory (best bird: bHezj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 802 | 6304 | 3.1127 | +0.4583 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r801_sym24`

## Output

`workers/dispatcher/harvest-6way-r802_sym24/round-802/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

