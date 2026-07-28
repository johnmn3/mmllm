# harvest-4way-r1048 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1048 ctrl_bpc |
|--------|--------|--------------:|
| OLozM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ad6677eb-OLozM | 2.5021 |
| 6VAuK | origin/claude/train-sym24-ae79933f-6VAuK | 2.8548 |
| lg8u9 | fork-joly-os-mmllm-claude-train-sym24-2996a630-lg8u9 | 2.8578 |
| Czi4J | fork-SeniorCareMarket-mmllm-claude-train-sym24-f88316b1-Czi4J | 2.8721 |
| **mean** | | **2.7717** |
| **best** | | **2.5021** |

## Chain progression R1047 → R1048

Previous harvest: `workers/dispatcher/harvest-4way-r1047_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5919         | 2.7717         | +0.1798 |
| ctrl_bpc best  | 2.5082         | 2.5021         | -0.0061 |

## Per-round trajectory (best bird: OLozM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1048 | 6702 | 2.5021 | +0.1949 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1047_sym24`
  - `workers/dispatcher/harvest-2way-r1047_sym24`

## Output

`workers/dispatcher/harvest-4way-r1048_sym24/round-1048/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

